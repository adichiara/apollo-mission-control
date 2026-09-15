"""Authoritative-session integration for the Apollo 13 PC+2 restart branch.

The historical contingency was pre-briefed before the burn. This module
therefore does not invent a new post-stop FLIGHT/CAPCOM approval step.

It keeps these layers separate:

premature physical stop
→ restart eligibility classification
→ ordered pre-briefed crew procedure
→ explicit successful physical restart response
→ later controller-observable evidence
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .controller_products import project_controller_products
from .dps_restart_response import apply_pc2_restart_response
from .operational_actions import OperationalAction, apply_operational_action
from .pc2_session import PC2Session, PC2_RESTART_PROCEDURE_ID
from .restart_logic import RestartEvaluation, evaluate_premature_shutdown_restart
from .shutdown_rules import evaluate_pc2_shutdown_rules


def record_premature_dps_stop(
    session: PC2Session,
    *,
    cause_known_non_rule: bool,
    noun97_flashing: bool | None,
    provenance: str,
) -> dict[str, Any]:
    """Record a source-bounded external premature stop without diagnosing mechanics."""
    if not session.state.engine_running:
        raise ValueError("Premature DPS stop requires the engine to be running")
    if session.state.premature_dps_stop_observed:
        raise ValueError("Premature DPS stop has already been recorded")

    session.state.engine_running = False
    session.state.throttle_phase = "off"
    session.state.premature_dps_stop_observed = True
    session.state.premature_dps_stop_get_s = float(session.state.get_s)
    session.state.premature_dps_stop_cause_known_non_rule = bool(cause_known_non_rule)
    session.state.premature_dps_stop_noun97_flashing = noun97_flashing

    event = session._audit(
        "premature_dps_stop_observed",
        "VEHICLE",
        cause_known_non_rule=bool(cause_known_non_rule),
        noun97_flashing=noun97_flashing,
        provenance=provenance,
        physical_failure_mechanism="not_asserted",
    )
    return asdict(event)


def evaluate_session_restart_eligibility(session: PC2Session) -> RestartEvaluation:
    """Evaluate the pre-briefed restart branch from current controller evidence."""
    evaluations = evaluate_pc2_shutdown_rules(
        project_controller_products(session.state, session.fixture),
        session.fixture,
    )
    return evaluate_premature_shutdown_restart(
        evaluations,
        early_engine_stop_observed=session.state.premature_dps_stop_observed,
        shutdown_cause_known_non_rule=session.state.premature_dps_stop_cause_known_non_rule,
        noun97_flashing=session.state.premature_dps_stop_noun97_flashing,
    )


def perform_pc2_restart_step(
    session: PC2Session,
    *,
    step_index: int,
) -> dict[str, Any]:
    """Perform one ordered step of the pre-briefed PC+2 restart procedure."""
    restart = evaluate_session_restart_eligibility(session)
    if restart.disposition.value != "restart_eligible":
        raise ValueError(
            "PC+2 restart procedure requires RESTART_ELIGIBLE disposition; "
            f"current disposition is {restart.disposition.value}"
        )

    crew_step = session.simulated_crew.perform_prebriefed_step(
        PC2_RESTART_PROCEDURE_ID,
        step_index=step_index,
        get_s=float(session.state.get_s),
    )

    operational_action_id: str | None = None
    if crew_step.action != "proceed_noun_97":
        operational = OperationalAction(
            action_id=crew_step.action_id,
            get_s=crew_step.get_s,
            actor=crew_step.crew_id,
            action=crew_step.action,
            parameters={},
            provenance=crew_step.provenance,
        )
        apply_operational_action(session.state, operational)
        operational_action_id = operational.action_id

    event = session._audit(
        "crew_restart_procedure_step",
        crew_step.crew_id,
        procedure_id=crew_step.procedure_id,
        step_index=crew_step.step_index,
        action=crew_step.action,
        operational_action_id=operational_action_id,
        provenance=crew_step.provenance,
    )
    return asdict(event)


def apply_session_restart_response(
    session: PC2Session,
    *,
    cause: str = "pc2_manual_restart_sequence",
) -> dict[str, Any]:
    """Apply explicit successful DPS restart only after the full eligible procedure."""
    restart = evaluate_session_restart_eligibility(session)
    if not session.simulated_crew.procedure_complete(PC2_RESTART_PROCEDURE_ID):
        raise ValueError("Physical DPS restart requires the complete pre-briefed crew procedure")

    response = apply_pc2_restart_response(
        session.state,
        restart,
        get_s=float(session.state.get_s),
        cause=cause,
    )
    session._audit(
        "dps_engine_on_physical_response",
        "VEHICLE",
        cause=response.cause,
        engine_on_command_received=response.engine_on_command_received,
        pilot_valves_commanded_open=response.pilot_valves_commanded_open,
        propellant_shutoff_valves_commanded_open=response.propellant_shutoff_valves_commanded_open,
        thrust_level_known=response.thrust_level_known,
    )
    return asdict(response)
