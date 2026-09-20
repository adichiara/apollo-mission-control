"""Landing-radar DATA GOOD transition replay.

This module replays discrete source-backed DATA GOOD / NOT GOOD transitions and
computes the separate persistence qualification used by downstream measurement
admission. It does not synthesize stochastic dropout behavior.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


def _finite(value: float, name: str) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


@dataclass(frozen=True)
class LandingRadarDataGoodTransition:
    time_s: float
    data_good: bool
    label: str
    source_resolution_s: float | None = None
    provenance: tuple[str, ...] = ()

    def validated(self) -> "LandingRadarDataGoodTransition":
        time_s = _finite(self.time_s, "transition time_s")
        label = str(self.label).strip()
        if not label:
            raise ValueError("transition label must not be empty")
        resolution = (
            None
            if self.source_resolution_s is None
            else _finite(self.source_resolution_s, "source_resolution_s")
        )
        if resolution is not None and resolution <= 0.0:
            raise ValueError("source_resolution_s must be positive")
        return LandingRadarDataGoodTransition(
            time_s=time_s,
            data_good=bool(self.data_good),
            label=label,
            source_resolution_s=resolution,
            provenance=tuple(self.provenance),
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "time_s": self.time_s,
            "data_good": self.data_good,
            "label": self.label,
            "source_resolution_s": self.source_resolution_s,
            "provenance": list(self.provenance),
        }


@dataclass(frozen=True)
class LandingRadarDataGoodReplayInput:
    initial_time_s: float
    initial_data_good: bool
    initial_data_good_since_s: float | None
    query_time_s: float
    min_data_good_duration_s: float
    transitions: tuple[LandingRadarDataGoodTransition, ...]
    applicability: str = "source-backed landing-radar DATA GOOD transition replay"
    assumptions: tuple[str, ...] = (
        "initial DATA GOOD state is caller supplied rather than inferred outside the source-bounded interval",
        "transition times are replay anchors at their stated source resolution",
        "no stochastic dropout probability or sub-source-resolution timing is inferred",
    )


@dataclass(frozen=True)
class LandingRadarDataGoodReplayResult:
    query_time_s: float
    data_good: bool
    data_good_since_s: float | None
    data_good_duration_s: float | None
    data_good_qualified: bool
    min_data_good_duration_s: float
    applied_transitions: tuple[LandingRadarDataGoodTransition, ...]
    next_transition: LandingRadarDataGoodTransition | None
    applicability: str
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "landing_radar_data_good_transition_replay",
            "query_time_s": self.query_time_s,
            "data_good": self.data_good,
            "data_good_since_s": self.data_good_since_s,
            "data_good_duration_s": self.data_good_duration_s,
            "data_good_qualified": self.data_good_qualified,
            "min_data_good_duration_s": self.min_data_good_duration_s,
            "applied_transitions": [item.to_dict() for item in self.applied_transitions],
            "next_transition": (
                None if self.next_transition is None else self.next_transition.to_dict()
            ),
            "applicability": self.applicability,
            "assumptions": list(self.assumptions),
        }


def replay_landing_radar_data_good(
    request: LandingRadarDataGoodReplayInput,
) -> LandingRadarDataGoodReplayResult:
    initial_time = _finite(request.initial_time_s, "initial_time_s")
    query_time = _finite(request.query_time_s, "query_time_s")
    if query_time < initial_time:
        raise ValueError("query_time_s must not precede initial_time_s")

    minimum = _finite(request.min_data_good_duration_s, "min_data_good_duration_s")
    if minimum < 0.0:
        raise ValueError("min_data_good_duration_s must be non-negative")

    good_since = (
        None
        if request.initial_data_good_since_s is None
        else _finite(request.initial_data_good_since_s, "initial_data_good_since_s")
    )
    if good_since is not None and good_since > initial_time:
        raise ValueError("initial_data_good_since_s cannot be after initial_time_s")
    if not request.initial_data_good and good_since is not None:
        raise ValueError(
            "initial_data_good_since_s must be null when initial_data_good is false"
        )

    transitions = tuple(item.validated() for item in request.transitions)
    times = [item.time_s for item in transitions]
    if times != sorted(times) or len(times) != len(set(times)):
        raise ValueError("transitions must have unique ascending times")
    if transitions and transitions[0].time_s < initial_time:
        raise ValueError("transition time cannot precede initial_time_s")

    state = bool(request.initial_data_good)
    applied: list[LandingRadarDataGoodTransition] = []
    next_transition: LandingRadarDataGoodTransition | None = None

    for item in transitions:
        if item.time_s > query_time:
            next_transition = item
            break
        state = item.data_good
        good_since = item.time_s if item.data_good else None
        applied.append(item)

    duration = None if not state or good_since is None else query_time - good_since
    qualified = state and duration is not None and duration >= minimum

    return LandingRadarDataGoodReplayResult(
        query_time_s=query_time,
        data_good=state,
        data_good_since_s=good_since,
        data_good_duration_s=duration,
        data_good_qualified=qualified,
        min_data_good_duration_s=minimum,
        applied_transitions=tuple(applied),
        next_transition=next_transition,
        applicability=str(request.applicability).strip()
        or "source-backed landing-radar DATA GOOD transition replay",
        assumptions=tuple(request.assumptions),
    )
