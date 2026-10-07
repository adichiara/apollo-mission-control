"""Generic powered-descent nominal phase skeleton.

This module intentionally represents discrete plan anchors, not continuous
trajectory or propulsion dynamics. Flown/postflight observations may accompany
a profile, but they never drive phase selection unless explicitly encoded as
nominal anchors by that profile.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import isfinite
from typing import Iterable


class PoweredDescentPhase(str, Enum):
    PRE_PDI = "pre_pdi"
    BRAKING = "braking"
    APPROACH = "approach"
    LANDING = "landing"
    POST_PLANNED_TOUCHDOWN = "post_planned_touchdown"


@dataclass(frozen=True)
class PoweredDescentAnchor:
    event_id: str
    tfi_s: float
    phase_after: PoweredDescentPhase
    nominal_altitude_ft: float | None = None
    evidence_basis: str = "planned_nominal"

    def validated(self) -> "PoweredDescentAnchor":
        event_id = str(self.event_id).strip()
        if not event_id:
            raise ValueError("event_id must not be empty")
        tfi_s = float(self.tfi_s)
        if not isfinite(tfi_s) or tfi_s < 0.0:
            raise ValueError("anchor tfi_s must be finite and non-negative")
        altitude = self.nominal_altitude_ft
        if altitude is not None:
            altitude = float(altitude)
            if not isfinite(altitude) or altitude < 0.0:
                raise ValueError(
                    "nominal_altitude_ft must be finite and non-negative"
                )
        basis = str(self.evidence_basis).strip()
        if not basis:
            raise ValueError("evidence_basis must not be empty")
        return PoweredDescentAnchor(
            event_id=event_id,
            tfi_s=tfi_s,
            phase_after=self.phase_after,
            nominal_altitude_ft=altitude,
            evidence_basis=basis,
        )

    def to_dict(self) -> dict[str, object]:
        checked = self.validated()
        return {
            "event_id": checked.event_id,
            "tfi_s": checked.tfi_s,
            "phase_after": checked.phase_after.value,
            "nominal_altitude_ft": checked.nominal_altitude_ft,
            "evidence_basis": checked.evidence_basis,
        }


@dataclass(frozen=True)
class FlownPropulsionObservation:
    key: str
    value: float
    unit: str
    qualifier: str
    evidence_basis: str = "flown_postflight"

    def validated(self) -> "FlownPropulsionObservation":
        key = str(self.key).strip()
        unit = str(self.unit).strip()
        qualifier = str(self.qualifier).strip()
        basis = str(self.evidence_basis).strip()
        value = float(self.value)
        if not key:
            raise ValueError("observation key must not be empty")
        if not unit:
            raise ValueError("observation unit must not be empty")
        if not qualifier:
            raise ValueError("observation qualifier must not be empty")
        if not basis:
            raise ValueError("observation evidence_basis must not be empty")
        if not isfinite(value):
            raise ValueError("observation value must be finite")
        return FlownPropulsionObservation(
            key=key,
            value=value,
            unit=unit,
            qualifier=qualifier,
            evidence_basis=basis,
        )

    def to_dict(self) -> dict[str, object]:
        checked = self.validated()
        return {
            "key": checked.key,
            "value": checked.value,
            "unit": checked.unit,
            "qualifier": checked.qualifier,
            "evidence_basis": checked.evidence_basis,
        }


@dataclass(frozen=True)
class PoweredDescentPhaseConfig:
    profile_id: str
    mission_profile_id: str
    anchors: tuple[PoweredDescentAnchor, ...]
    flown_observations: tuple[FlownPropulsionObservation, ...] = ()
    untimed_nominal_events: tuple[str, ...] = ()
    applicability: str = (
        "nominal powered-descent phase skeleton; not continuous flown trajectory"
    )
    provenance: tuple[str, ...] = ()
    unresolved: tuple[str, ...] = ()

    def validated(self) -> "PoweredDescentPhaseConfig":
        profile_id = str(self.profile_id).strip()
        mission_profile_id = str(self.mission_profile_id).strip()
        applicability = str(self.applicability).strip()
        if not profile_id:
            raise ValueError("profile_id must not be empty")
        if not mission_profile_id:
            raise ValueError("mission_profile_id must not be empty")
        if not applicability:
            raise ValueError("applicability must not be empty")

        anchors = tuple(anchor.validated() for anchor in self.anchors)
        if not anchors:
            raise ValueError("anchors must not be empty")
        ids = [anchor.event_id for anchor in anchors]
        if len(ids) != len(set(ids)):
            raise ValueError("anchor event_id values must be unique")
        times = [anchor.tfi_s for anchor in anchors]
        if times != sorted(times):
            raise ValueError("anchors must be ordered by non-decreasing tfi_s")

        observations = tuple(
            observation.validated() for observation in self.flown_observations
        )
        observation_keys = [observation.key for observation in observations]
        if len(observation_keys) != len(set(observation_keys)):
            raise ValueError("flown observation keys must be unique")

        untimed = tuple(str(item).strip() for item in self.untimed_nominal_events)
        if any(not item for item in untimed):
            raise ValueError("untimed_nominal_events must not contain empty values")

        return PoweredDescentPhaseConfig(
            profile_id=profile_id,
            mission_profile_id=mission_profile_id,
            anchors=anchors,
            flown_observations=observations,
            untimed_nominal_events=untimed,
            applicability=applicability,
            provenance=tuple(self.provenance),
            unresolved=tuple(self.unresolved),
        )


@dataclass(frozen=True)
class PoweredDescentPhaseSnapshot:
    profile_id: str
    mission_profile_id: str
    tfi_s: float
    phase: PoweredDescentPhase
    most_recent_anchor: PoweredDescentAnchor | None
    next_anchor: PoweredDescentAnchor | None
    anchors: tuple[PoweredDescentAnchor, ...]
    flown_observations: tuple[FlownPropulsionObservation, ...]
    untimed_nominal_events: tuple[str, ...]
    applicability: str
    provenance: tuple[str, ...]
    unresolved: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "powered_descent_nominal_phase_skeleton",
            "profile_id": self.profile_id,
            "mission_profile_id": self.mission_profile_id,
            "tfi_s": self.tfi_s,
            "phase": self.phase.value,
            "phase_basis": "planned_nominal_anchors_only",
            "most_recent_anchor": (
                None
                if self.most_recent_anchor is None
                else self.most_recent_anchor.to_dict()
            ),
            "next_anchor": (
                None if self.next_anchor is None else self.next_anchor.to_dict()
            ),
            "anchors": [anchor.to_dict() for anchor in self.anchors],
            "flown_observations": [
                observation.to_dict() for observation in self.flown_observations
            ],
            "flown_observations_drive_phase": False,
            "untimed_nominal_events": list(self.untimed_nominal_events),
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "unresolved": list(self.unresolved),
        }


def evaluate_powered_descent_phase(
    tfi_s: float,
    config: PoweredDescentPhaseConfig,
) -> PoweredDescentPhaseSnapshot:
    """Evaluate a deterministic nominal phase from explicit plan anchors only."""

    checked = config.validated()
    time_s = float(tfi_s)
    if not isfinite(time_s):
        raise ValueError("tfi_s must be finite")

    phase = PoweredDescentPhase.PRE_PDI
    previous: PoweredDescentAnchor | None = None
    upcoming: PoweredDescentAnchor | None = None

    for anchor in checked.anchors:
        if time_s >= anchor.tfi_s:
            previous = anchor
            phase = anchor.phase_after
            continue
        upcoming = anchor
        break

    return PoweredDescentPhaseSnapshot(
        profile_id=checked.profile_id,
        mission_profile_id=checked.mission_profile_id,
        tfi_s=time_s,
        phase=phase,
        most_recent_anchor=previous,
        next_anchor=upcoming,
        anchors=checked.anchors,
        flown_observations=checked.flown_observations,
        untimed_nominal_events=checked.untimed_nominal_events,
        applicability=checked.applicability,
        provenance=checked.provenance,
        unresolved=checked.unresolved,
    )
