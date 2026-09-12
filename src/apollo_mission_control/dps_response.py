"""Source-bounded DPS physical response helpers for the PC+2 prototype.

Crew/controller actions remain separate from vehicle response. These helpers
represent only the physical consequences supported by contemporary LM system
sources and do not synthesize unsupported timing or analog traces.
"""

from __future__ import annotations

from dataclasses import dataclass

from .pc2_nominal import PC2State


@dataclass(frozen=True)
class DPSEngineOffResponse:
    get_s: float
    cause: str
    engine_off_discrete_received: bool
    pilot_valves_commanded_closed: bool
    propellant_shutoff_valves_commanded_closed: bool


@dataclass(frozen=True)
class DPSEngineOnResponse:
    get_s: float
    cause: str
    engine_on_discrete_received: bool
    pilot_valves_commanded_open: bool
    propellant_shutoff_valves_commanded_open: bool


def apply_engine_off_response(
    state: PC2State,
    *,
    get_s: float,
    cause: str = "crew_stop_pushbutton",
) -> DPSEngineOffResponse:
    """Apply the physical engine-off response as an explicit vehicle event.

    Contemporary LM handbooks document that a crew STOP pushbutton initiates an
    engine-off discrete and that engine on/off commands actuate the pilot valves,
    which hydraulically open/close the fuel and oxidizer shutoff valves.

    No delay, chamber-pressure decay curve, or telemetry confirmation is
    synthesized here. The caller supplies the response GET when a scenario or
    future dynamics model can justify it.
    """
    state.get_s = float(get_s)
    state.engine_running = False
    state.throttle_phase = "off"
    return DPSEngineOffResponse(
        get_s=float(get_s),
        cause=cause,
        engine_off_discrete_received=True,
        pilot_valves_commanded_closed=True,
        propellant_shutoff_valves_commanded_closed=True,
    )


def apply_engine_on_response(
    state: PC2State,
    *,
    get_s: float,
    cause: str = "pc2_restart_command_path",
) -> DPSEngineOnResponse:
    """Apply a successful physical DPS re-ignition as a distinct vehicle event.

    Apollo 13 PC+2 procedures explicitly provided for restarting the descent
    engine after an eligible premature shutdown. Contemporary LM documentation
    establishes that manual engine-on commands route through DECA to the pilot
    valves and propellant shutoff-valve system.

    This helper represents only the successful engine-on response. It is never
    called automatically merely because the crew performed the restart actions.
    The caller supplies the response GET; no ignition delay is invented.

    No chamber-pressure value, pressure-rise curve, post-restart throttle phase,
    or controller confirmation is synthesized here.
    """
    state.get_s = float(get_s)
    state.engine_running = True
    return DPSEngineOnResponse(
        get_s=float(get_s),
        cause=cause,
        engine_on_discrete_received=True,
        pilot_valves_commanded_open=True,
        propellant_shutoff_valves_commanded_open=True,
    )
