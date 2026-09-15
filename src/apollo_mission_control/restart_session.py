"""Authoritative PC+2 premature-stop/restart workflow helpers.

This module composes already-researched boundaries without inventing a new
post-stop CAPCOM instruction:

premature physical stop
    -> explicit cause classification
    -> restart eligibility
    -> prebriefed crew procedure
    -> explicit physical restart response

Controller confirmation remains a separate observation/product path.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .controller_products import project_controller_products
from .dps_restart_response import apply_pc2_restart_response
from .operational_actions import OperationalAction, apply_operational_action
from .pc2_session import PC2Session, PC2_RESTART_SEQUENCE
from .restart_logic import RestartDisposition, RestartEvaluation, evaluate_premature_shutdown_restart
from .shutdown_rules import evaluate_pc2_shutdown_rules


def evaluate_session_restart(session: PC2Session) -> RestartEvaluation:
    """Evaluate restart eligibility from current rule evidence and explicit context."""

    rules = evaluate_pc2_shutdown_rules(
        project_controller_products(session.state, session.fixture),
        session.fixture,
    )
    return evaluate_premature_shutdown_restart(
        rules,
        early_engine_stop_observed=session.state.premature_dps_stop_observed,
        shutdown_cause_known_non_rule=(
            session.state.premature_dps_stop_cause_known_non_rule
        ),
        noun97_flashing=session.state.restart_noun97_flashing,
    )


def record_premature_dps_stop(
    session: PC2Session,
    *,
    noun97_flashing: bool | None,
    provenance: str,
) -> dict[str, Any]:
    """Apply a validation/source-bounded premature physical stop.

    The helper does not classify the cause. That must be supplied separately so
    an unexplained stop cannot silently become restart-eligible.
    """

    if not session.state.engine_running:
        raise ValueError("Premature DPS stop requires the engine to be running")
    if session.state.premature_dps_stop_observed:
        raise ValueError("Premature DPS stop has already been recorded")

    session.state.engine_running = False
    session.state.throttle_phase = "premature_stop"
    session.state.premature_dps_stop_observed = True
    session.state.premature_dps_stop_get_s = float(session.state.get_s)
    session.state.premature_dps_stop_cause_known_non_rule = False
    session.state.restart_noun97_flashing = noun97_flashing

    event = session._audit(
        "dps_premature_stop_physical_response",
        "VEHICLE",
        noun97_flashing=noun97_flashing,
        cause_classification="unresolved",
        provenance=provenance,
    )
    return asdict(event)


def classify_premature_stop_non_rule(
    session: PC2Session,
    *,
    provenance: str,
) -> dict[str, Any]:
    """Record affirmative evidence that the stop cause is outside listed rules.

    This classification alone does not authorize restart if a listed shutdown
    rule is currently triggered; the restart evaluator remains authoritative.
    """

    if not session.state.premature_dps_stop_observed:
        raise ValueError("A premature DPS stop must be recorded before cause classification")

    session.state.premature_dps_stop_cause_known_non_rule = True
    evaluation = evaluate_session_restart(session)
    event = session._audit(
        "premature_stop_cause_classified_non_rule",
        "SIMSUP",
        provenance=provenance,
        restart_disposition=evaluation.disposition.value,
        triggered_rule_ids=list(evaluation.triggered_rule_ids),
        unresolved_rule_ids=list(evaluation.unresolved_rule_ids),
    )
    return asdict(event)


def perform_prebriefed_restart_procedure(
    session: PC2Session,
    *,
    crew_id: str = "CREW",
) -> dict[str, Any]:
    """Perform the already-briefed crew procedure only when restart is eligible."""

    evaluation = evaluate_session_restart(session)
    if evaluation.disposition != RestartDisposition.RESTART_ELIGIBLE:
        raise ValueError(
            "PC+2 restart procedure requires RESTART_ELIGIBLE disposition; "
            f"current disposition is {evaluation.disposition.value}"
        )

    actor_action = session.simulated_crew.perform_prebriefed_procedure(
        "pc2_premature_shutdown_restart",
        get_s=float(session.state.get_s),
    )
    if actor_action.parameters.get("sequence") != list(PC2_RESTART_SEQUENCE):
        raise ValueError("Configured PC+2 restart procedure does not match sourced sequence")

    # PRO on flashing Noun 97 is retained in the procedure/audit record. The
    # three modeled vehicle/control actions below are the currently implemented
    # operational state changes. No action starts the engine by itself.
    for suffix, action_name in (
        ("ullage", "restart_manual_ullage"),
        ("engine-start", "press_engine_start"),
        ("override", "descent_engine_command_override_on"),
    ):
        apply_operational_action(
            session.state,
            OperationalAction(
                action_id=f"{actor_action.action_id}-{suffix}",
                get_s=actor_action.get_s,
                actor=crew_id,
                action=action_name,
                parameters={},
                provenance=actor_action.provenance,
            ),
        )

    event = session._audit(
        "crew_prebriefed_restart_procedure_performed",
        crew_id,
        procedure_id=actor_action.procedure_id,
        procedure_action_id=actor_action.action_id,
        sequence=list(PC2_RESTART_SEQUENCE),
        noun97_flashing=session.state.restart_noun97_flashing,
        live_capcom_transmission_required=False,
        provenance=actor_action.provenance,
    )
    return asdict(event)


def apply_session_restart_response(
    session: PC2Session,
    *,
    cause: str = "pc2_manual_restart_sequence",
) -> dict[str, Any]:
    """Apply explicit successful physical restart after eligible crew procedure."""

    evaluation = evaluate_session_restart(session)
    response = apply_pc2_restart_response(
        session.state,
        evaluation,
        get_s=float(session.state.get_s),
        cause=cause,
    )
    event = session._audit(
        "dps_restart_physical_response",
        "VEHICLE",
        cause=response.cause,
        engine_on_command_received=response.engine_on_command_received,
        pilot_valves_commanded_open=response.pilot_valves_commanded_open,
        propellant_shutoff_valves_commanded_open=(
            response.propellant_shutoff_valves_commanded_open
        ),
        thrust_level_known=response.thrust_level_known,
        restart_disposition=evaluation.disposition.value,
    )
    return {
        **asdict(response),
        "audit_sequence": event.sequence,
    }
