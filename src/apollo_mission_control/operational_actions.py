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


_ALLOWED_ACTIONS = {"switch_lm_inverter"}


def apply_operational_action(state: PC2State, action: OperationalAction) -> None:
    """Apply one researched operational action without deriving an outcome."""

    if action.action not in _ALLOWED_ACTIONS:
        raise ValueError(f"Unsupported operational action: {action.action}")

    state.get_s = action.get_s

    if action.action == "switch_lm_inverter":
        # Exact inverter identity and switch chronology remain unresolved for
        # PC+2, so this records only that a switch attempt occurred.
        state.lm_inverter_switch_attempted = True
        state.lm_inverter_switch_attempt_get_s = action.get_s
