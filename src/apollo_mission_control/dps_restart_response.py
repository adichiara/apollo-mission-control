"""Source-bounded physical response for an eligible Apollo 13 PC+2 DPS restart.

Crew restart commands remain separate from vehicle response.  This module
represents only the successful physical engine-on response supported by the
Apollo 13 restart rule and contemporary LM DPS documentation.  It deliberately
does not synthesize restart timing, thrust level, chamber-pressure rise, or
success probability.
"""

from __future__ import annotations

from dataclasses import dataclass

from .pc2_nominal import PC2State
from .restart_logic import RestartDisposition, RestartEvaluation


@dataclass(frozen=True)
class DPSEngineOnResponse:
    get_s: float
    cause: str
    engine_on_command_received: bool
    pilot_valves_commanded_open: bool
    propellant_shutoff_valves_commanded_open: bool
    thrust_level_known: bool = False


def restart_actions_complete(state: PC2State) -> bool:
    """Return whether the modeled PC+2 crew restart actions were completed."""
    return bool(
        state.restart_manual_ullage_attempted
        and state.engine_start_push_attempted
        and state.descent_engine_command_override_on
    )


def apply_pc2_restart_response(
    state: PC2State,
    restart: RestartEvaluation,
    *,
    get_s: float,
    cause: str = "pc2_manual_restart_sequence",
) -> DPSEngineOnResponse:
    """Apply a successful restart as an explicit physical-response event.

    The caller must supply a RESTART_ELIGIBLE decision and the modeled crew
    sequence must already have been performed.  Successful physical response is
    still explicit: executing the crew commands alone never starts the engine.

    Contemporary LM documentation supports engine-on command -> pilot-valve
    opening -> propellant-shutoff-valve opening -> propellant flow/combustion.
    No exact Apollo 13 restart delay, thrust command, pressure transient, or
    telemetry confirmation is inferred here.
    """
    if restart.disposition != RestartDisposition.RESTART_ELIGIBLE:
        raise ValueError("DPS restart response requires RESTART_ELIGIBLE disposition")
    if not restart_actions_complete(state):
        raise ValueError("DPS restart response requires the complete modeled PC+2 restart action sequence")

    state.get_s = float(get_s)
    state.engine_running = True
    # The reviewed PC+2 sources do not establish the exact thrust command after
    # this contingency restart, so do not alias it to minimum/40%/maximum.
    state.throttle_phase = "restart_thrust_unspecified"

    return DPSEngineOnResponse(
        get_s=float(get_s),
        cause=cause,
        engine_on_command_received=True,
        pilot_valves_commanded_open=True,
        propellant_shutoff_valves_commanded_open=True,
        thrust_level_known=False,
    )
