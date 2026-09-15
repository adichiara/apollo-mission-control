"""Crew-response integration for source-bounded PC+2 CAPCOM callouts.

This module deliberately keeps three layers separate:

1. crew receipt of a transmitted ground call;
2. crew operational command;
3. physical DPS engine response.

It does not invent response latency, cockpit choreography, or telemetry
confirmation thresholds for the hypothetical fuel/oxidizer delta-P branch.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .dps_response import apply_engine_off_response
from .dps_restart_response import apply_pc2_restart_response
from .operational_actions import OperationalAction, apply_operational_action
from .restart_logic import (
    RestartDisposition,
    evaluate_premature_shutdown_restart,
)
from .shutdown_rules import evaluate_pc2_shutdown_rules
from .controller_products import project_controller_products
from .pc2_session import (
    PC2Session,
    PC2_INVERTER_TRANSFER_PROVENANCE,
    PC2_INVERTER_TRANSFER_SEQUENCE,
    PC2_RESTART_PROCEDURE_ID,
    PC2_RESTART_PROCEDURE_PROVENANCE,
)


def _transmitted_supported_crew_item(session: PC2Session, item_id: int):
    item = next((item for item in session.capcom_queue if item.item_id == item_id), None)
    if item is None:
        raise ValueError(f"Unknown CAPCOM queue item: {item_id}")
    if not item.transmitted:
        raise ValueError("Crew cannot receive a CAPCOM item that has not been transmitted")
    session.simulated_crew.rule_for(item)
    return item


def _transmitted_shutdown_callout(session: PC2Session, item_id: int):
    item = _transmitted_supported_crew_item(session, item_id)
    if item.action != "callout_dps_shutdown_criterion":
        raise ValueError("CAPCOM item is not a DPS shutdown-criterion callout")
    return item


def record_crew_receipt(
    session: PC2Session,
    item_id: int,
    *,
    crew_id: str = "CREW",
    response: str = "received",
) -> dict[str, Any]:
    """Record explicit crew receipt/readback state without performing the action."""
    item = _transmitted_supported_crew_item(session, item_id)
    receipt = session.simulated_crew.receive_instruction(
        item,
        get_s=float(session.state.get_s),
    )
    event = session._audit(
        "crew_capcom_item_received",
        crew_id,
        item_id=item.item_id,
        action=item.action,
        response=response,
        actor_acknowledgement=receipt.acknowledgement,
        rule_provenance=receipt.provenance,
    )
    return asdict(event)


def command_dps_shutdown_from_callout(
    session: PC2Session,
    item_id: int,
    *,
    crew_id: str = "CREW",
    provenance: str = "Apollo 13 PC+2 ground-call shutdown rule; exact cockpit choreography unresolved",
) -> OperationalAction:
    """Record the crew DPS shutdown command after an explicit transmitted call."""
    item = _transmitted_shutdown_callout(session, item_id)
    crew_action = session.simulated_crew.perform_supported_action(
        item,
        get_s=float(session.state.get_s),
    )

    action = OperationalAction(
        action_id=f"crew-dps-shutdown-{item_id}",
        get_s=crew_action.get_s,
        actor=crew_id,
        action=crew_action.action,
        parameters={
            "capcom_item_id": item_id,
            **crew_action.parameters,
        },
        provenance=provenance,
    )
    apply_operational_action(session.state, action)
    session._audit(
        "crew_dps_shutdown_commanded",
        crew_id,
        item_id=item_id,
        action_id=action.action_id,
        criterion=item.parameters.get("criterion"),
        provenance=provenance,
        simulated_crew_action_id=crew_action.action_id,
        rule_provenance=crew_action.provenance,
    )
    return action


def perform_inverter_transfer_from_callout(
    session: PC2Session,
    item_id: int,
    *,
    crew_id: str = "CREW",
    provenance: str = PC2_INVERTER_TRANSFER_PROVENANCE,
) -> OperationalAction:
    """Perform the sourced inverter-2 to inverter-1 transfer after receipt.

    The crew action records the recovered three-control sequence but does not
    alter the inverter-warning observation. A fresh post-transfer observation
    remains required before the shutdown rule can become positive.
    """
    item = _transmitted_supported_crew_item(session, item_id)
    if item.action != "switch_lm_inverter":
        raise ValueError("CAPCOM item is not an inverter-transfer instruction")

    expected_sequence = list(PC2_INVERTER_TRANSFER_SEQUENCE)
    if item.parameters.get("from_inverter") != 2:
        raise ValueError("Inverter-transfer instruction must start from inverter 2")
    if item.parameters.get("to_inverter") != 1:
        raise ValueError("Inverter-transfer instruction must select inverter 1")
    if item.parameters.get("control_sequence") != expected_sequence:
        raise ValueError("Inverter-transfer instruction does not match the sourced control sequence")

    crew_action = session.simulated_crew.perform_supported_action(
        item,
        get_s=float(session.state.get_s),
    )
    action = OperationalAction(
        action_id=crew_action.action_id,
        get_s=crew_action.get_s,
        actor=crew_id,
        action=crew_action.action,
        parameters={
            "capcom_item_id": item_id,
            **crew_action.parameters,
        },
        provenance=provenance,
    )
    apply_operational_action(session.state, action)
    session._audit(
        "crew_inverter_transfer_performed",
        crew_id,
        item_id=item_id,
        action_id=action.action_id,
        from_inverter=2,
        to_inverter=1,
        control_sequence=expected_sequence,
        provenance=provenance,
        rule_provenance=crew_action.provenance,
    )
    return action


def record_inverter_transfer_completion_report(
    session: PC2Session,
    item_id: int,
    *,
    crew_id: str = "CREW",
) -> dict[str, Any]:
    """Record crew completion report without asserting warning outcome."""
    item = _transmitted_supported_crew_item(session, item_id)
    if item.action != "switch_lm_inverter":
        raise ValueError("CAPCOM item is not an inverter-transfer instruction")
    action = session.simulated_crew.actions.get(item_id)
    if action is None:
        raise ValueError("Crew inverter-transfer action must occur before completion report")
    event = session._audit(
        "crew_inverter_transfer_reported",
        crew_id,
        item_id=item_id,
        action=action.action,
        reported_state="transfer_complete",
        observation_consequence="not_asserted",
        rule_provenance=action.provenance,
    )
    return asdict(event)


def record_premature_dps_stop(
    session: PC2Session,
    *,
    shutdown_cause_known_non_rule: bool,
    noun97_flashing: bool | None,
    cause: str = "premature_stop_mechanism_unspecified",
) -> dict[str, Any]:
    """Record an early physical engine stop and conservatively classify restart eligibility.

    The stop event does not assert a valve/discrete mechanism. The facilitator/
    scenario explicitly states whether the cause is affirmatively known to be
    outside the listed shutdown criteria; absence of a modeled trigger is not enough.
    """
    if not session.state.engine_running:
        raise ValueError("Premature DPS stop requires the engine to be running")

    session.state.engine_running = False
    session.state.throttle_phase = "off"

    evaluations = evaluate_pc2_shutdown_rules(
        project_controller_products(session.state, session.fixture),
        session.fixture,
    )
    restart = evaluate_premature_shutdown_restart(
        evaluations,
        early_engine_stop_observed=True,
        shutdown_cause_known_non_rule=shutdown_cause_known_non_rule,
        noun97_flashing=noun97_flashing,
    )
    session.restart_evaluation = restart
    event = session._audit(
        "dps_premature_engine_stop",
        "VEHICLE",
        cause=cause,
        stop_mechanism="unspecified",
        shutdown_cause_known_non_rule=shutdown_cause_known_non_rule,
        noun97_flashing=noun97_flashing,
        restart_disposition=restart.disposition.value,
        restart_basis=restart.basis,
        triggered_rule_ids=list(restart.triggered_rule_ids),
        unresolved_rule_ids=list(restart.unresolved_rule_ids),
    )
    return {
        "event": asdict(event),
        "restart_evaluation": {
            "disposition": restart.disposition.value,
            "basis": restart.basis,
            "triggered_rule_ids": list(restart.triggered_rule_ids),
            "unresolved_rule_ids": list(restart.unresolved_rule_ids),
            "noun97_flashing": restart.noun97_flashing,
        },
    }


def perform_prebriefed_pc2_restart_procedure(
    session: PC2Session,
    *,
    crew_id: str = "CREW",
) -> list[dict[str, Any]]:
    """Execute the prebriefed crew restart sequence only when restart is eligible."""
    restart = session.restart_evaluation
    if restart is None:
        raise ValueError("Restart procedure requires a classified premature engine stop")
    if restart.disposition != RestartDisposition.RESTART_ELIGIBLE:
        raise ValueError(
            f"Restart procedure requires restart_eligible disposition, got {restart.disposition.value}"
        )

    crew_actions = session.simulated_crew.perform_prebriefed_procedure(
        PC2_RESTART_PROCEDURE_ID,
        get_s=float(session.state.get_s),
    )
    recorded: list[dict[str, Any]] = []
    for crew_action in crew_actions:
        if crew_action.action == "proceed_noun_97":
            event = session._audit(
                "crew_restart_procedure_step",
                crew_id,
                procedure_id=crew_action.procedure_id,
                action=crew_action.action,
                sequence_index=crew_action.sequence_index,
                provenance=crew_action.provenance,
                state_effect="none_modeled",
            )
            recorded.append(asdict(event))
            continue

        action = OperationalAction(
            action_id=crew_action.action_id,
            get_s=crew_action.get_s,
            actor=crew_id,
            action=crew_action.action,
            parameters={},
            provenance=PC2_RESTART_PROCEDURE_PROVENANCE,
        )
        apply_operational_action(session.state, action)
        event = session._audit(
            "crew_restart_procedure_step",
            crew_id,
            procedure_id=crew_action.procedure_id,
            action=crew_action.action,
            action_id=crew_action.action_id,
            sequence_index=crew_action.sequence_index,
            provenance=crew_action.provenance,
        )
        recorded.append(asdict(event))

    return recorded


def apply_session_restart_response(
    session: PC2Session,
    *,
    cause: str = "pc2_manual_restart_sequence",
) -> dict[str, Any]:
    """Apply successful physical restart only after eligibility and crew procedure."""
    restart = session.restart_evaluation
    if restart is None:
        raise ValueError("Physical DPS restart requires a classified premature stop")
    response = apply_pc2_restart_response(
        session.state,
        restart,
        get_s=float(session.state.get_s),
        cause=cause,
    )
    session._audit(
        "dps_restart_physical_response",
        "VEHICLE",
        cause=response.cause,
        engine_on_command_received=response.engine_on_command_received,
        pilot_valves_commanded_open=response.pilot_valves_commanded_open,
        propellant_shutoff_valves_commanded_open=response.propellant_shutoff_valves_commanded_open,
        thrust_level_known=response.thrust_level_known,
    )
    return asdict(response)


def apply_session_engine_off_response(
    session: PC2Session,
    *,
    get_s: float,
    cause: str = "crew_stop_pushbutton",
) -> dict[str, Any]:
    """Apply an explicit physical DPS-off response at authoritative session GET.

    The caller chooses the response time by advancing the session clock first.
    This helper refuses to advance time itself, preventing a physical response
    from silently skipping scheduled scenario events. No LM-7 response delay,
    chamber-pressure decay, or controller confirmation is synthesized.
    """
    if not session.state.crew_dps_shutdown_commanded:
        raise ValueError("Physical DPS shutdown response requires a prior crew shutdown command")
    if abs(float(get_s) - float(session.state.get_s)) > 1e-6:
        raise ValueError("Physical response GET must equal the current authoritative session GET")

    response = apply_engine_off_response(session.state, get_s=float(get_s), cause=cause)
    session._audit(
        "dps_engine_off_physical_response",
        "VEHICLE",
        cause=response.cause,
        engine_off_discrete_received=response.engine_off_discrete_received,
        pilot_valves_commanded_closed=response.pilot_valves_commanded_closed,
        propellant_shutoff_valves_commanded_closed=response.propellant_shutoff_valves_commanded_closed,
    )
    return asdict(response)
