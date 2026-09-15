"""Minimal operational-action events for the Apollo 13 PC+2 slice.

Operational actions are separate from failure/scenario injections. They record
what a controller/crew actor did; they do not create a fault or a diagnosis.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .pc2_nominal import PC2State


@dataclass(frozen=True)
class OperationalAction:
    action_id: str
    get_s: float
    actor: str
    action: str
    parameters: dict[str, Any]
    provenance: str


_ALLOWED_ACTIONS = {
    "switch_lm_inverter",
    "restart_manual_ullage",
    "press_engine_start",
    "descent_engine_command_override_on",
    "command_dps_shutdown",
    "press_engine_stop",
}


def apply_operational_action(state: PC2State, action: OperationalAction) -> None:
    """Apply one researched operational action without deriving an outcome."""

    if action.action not in _ALLOWED_ACTIONS:
        raise ValueError(f"Unsupported operational action: {action.action}")

    state.get_s = action.get_s

    if action.action == "switch_lm_inverter":
        # Apollo 13 LM malfunction procedures source the inverter-2 to
        # inverter-1 transfer sequence. This state records only that the crew
        # action occurred; the post-transfer caution remains a separate observation.
        state.lm_inverter_switch_attempted = True
        state.lm_inverter_switch_attempt_get_s = action.get_s
    elif action.action == "restart_manual_ullage":
        # Record the historical restart action without assuming RCS performance.
        state.restart_manual_ullage_attempted = True
        state.restart_manual_ullage_get_s = action.get_s
    elif action.action == "press_engine_start":
        # The crew command is distinct from whether the DPS actually restarts.
        state.engine_start_push_attempted = True
        state.engine_start_push_get_s = action.get_s
    elif action.action == "descent_engine_command_override_on":
        # Again, command state is not aliased to physical engine response.
        state.descent_engine_command_override_on = True
        state.descent_engine_command_override_get_s = action.get_s
    elif action.action in {"command_dps_shutdown", "press_engine_stop"}:
        # Contemporary LM handbooks establish that either crew STOP pushbutton
        # initiates the descent-engine off command. Recording the push/command
        # remains separate from subsequent valve/engine physical response.
        state.crew_dps_shutdown_commanded = True
        state.crew_dps_shutdown_command_get_s = action.get_s
