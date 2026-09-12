"""Minimal timed scenario-injection layer for the Apollo 13 PC+2 slice.

Injections alter modeled source state only. They do not set diagnoses, rule
results, controller decisions, or crew/engine actions.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable

from .pc2_nominal import PC2State, SimEvent, apply_event, build_events


class EvidenceClass(str, Enum):
    HISTORICAL_EVENT = "historical_event"
    DOCUMENTED_SIMULATION_CASE = "documented_simulation_case"
    SOURCE_BOUNDED_TEST = "source_bounded_test"
    PROJECT_HYPOTHETICAL = "project_hypothetical"


@dataclass(frozen=True)
class StateInjection:
    injection_id: str
    get_s: float
    target: str
    value: Any
    evidence_class: EvidenceClass
    provenance: str


# Explicitly narrow by design. Additional targets are added only when their
# source-state representation has been researched and modeled.
_ALLOWED_STATE_TARGETS = {
    "dps_chamber_pressure_psi",
    "dps_fuel_oxidizer_delta_p_psi",
    "lm_inverter_warning",
}


def apply_state_injection(state: PC2State, injection: StateInjection) -> None:
    """Apply one whitelisted state mutation without deriving any outcome."""

    if injection.target not in _ALLOWED_STATE_TARGETS:
        raise ValueError(f"Unsupported scenario injection target: {injection.target}")

    state.get_s = injection.get_s
    setattr(state, injection.target, injection.value)

    if injection.target == "lm_inverter_warning":
        # Timestamp the observation separately from the switch action. This is
        # required by the PC+2 wording: the positive criterion is a warning
        # that remains after an inverter switch, not merely a warning that
        # existed before the action.
        state.lm_inverter_warning_observed_get_s = injection.get_s


def run_with_injections(
    fixture: dict[str, Any],
    injections: Iterable[StateInjection],
    *,
    stop_get_s: float | None = None,
) -> PC2State:
    """Run the source-backed event timeline plus explicit state injections.

    At identical GET values, historical timeline events are applied before
    scenario injections. This is a deterministic project convention, not a
    claim about historical SimSup execution ordering.
    """

    state = PC2State(get_s=float(fixture["start_get_s"]))

    timeline: list[tuple[float, int, SimEvent | StateInjection]] = [
        (event.get_s, 0, event) for event in build_events(fixture)
    ]
    timeline.extend((item.get_s, 1, item) for item in injections)
    timeline.sort(key=lambda row: (row[0], row[1]))

    for get_s, _, item in timeline:
        if stop_get_s is not None and get_s > stop_get_s:
            break
        if isinstance(item, SimEvent):
            apply_event(state, item, fixture)
        else:
            apply_state_injection(state, item)

    if stop_get_s is not None and state.get_s < stop_get_s:
        state.get_s = stop_get_s

    return state
