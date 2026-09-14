"""Mission-neutral landing-radar guidance-update eligibility model.

This module does not generate radar measurements and does not update a vehicle
state vector. It decides only whether a supplied altitude/velocity measurement
is eligible to be handed to a downstream guidance estimator.

The separation is intentional:
measurement quality != crew/update enablement != estimator acceptance/update.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
from typing import Iterable


Vector3 = tuple[float, float, float]


def _finite(value: float, name: str) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def _vector(value: Iterable[float], name: str) -> Vector3:
    vector = tuple(_finite(component, name) for component in value)
    if len(vector) != 3:
        raise ValueError(f"{name} must have exactly three components")
    return vector  # type: ignore[return-value]


@dataclass(frozen=True)
class LandingRadarMeasurement:
    time_s: float
    data_good: bool
    altitude_m: float | None = None
    velocity_m_s: Vector3 | None = None
    source: str = "caller_supplied"

    def validated(self) -> "LandingRadarMeasurement":
        altitude = (
            None
            if self.altitude_m is None
            else _finite(self.altitude_m, "altitude_m")
        )
        if altitude is not None and altitude < 0.0:
            raise ValueError("altitude_m must be non-negative when supplied")
        velocity = (
            None
            if self.velocity_m_s is None
            else _vector(self.velocity_m_s, "velocity_m_s")
        )
        source = str(self.source).strip()
        if not source:
            raise ValueError("source must not be empty")
        return LandingRadarMeasurement(
            time_s=_finite(self.time_s, "time_s"),
            data_good=bool(self.data_good),
            altitude_m=altitude,
            velocity_m_s=velocity,
            source=source,
        )


@dataclass(frozen=True)
class LandingRadarGuidanceContext:
    time_s: float
    updates_enabled: bool
    estimated_velocity_m_s: Vector3

    def validated(self) -> "LandingRadarGuidanceContext":
        return LandingRadarGuidanceContext(
            time_s=_finite(self.time_s, "time_s"),
            updates_enabled=bool(self.updates_enabled),
            estimated_velocity_m_s=_vector(
                self.estimated_velocity_m_s,
                "estimated_velocity_m_s",
            ),
        )

    @property
    def estimated_speed_m_s(self) -> float:
        return sqrt(sum(component * component for component in self.estimated_velocity_m_s))


@dataclass(frozen=True)
class LandingRadarUpdateConfig:
    velocity_update_speed_threshold_m_s: float | None = None
    applicability: str = "generic landing-radar update gate; not mission validated"
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "radar data-good state is supplied by an upstream observation/quality model",
        "update enablement is supplied by crew/guidance configuration",
        "altitude is eligible when data are good, updates are enabled, and altitude is present",
        "velocity is eligible under the same conditions plus the optional caller-supplied speed threshold",
        "this model does not perform state-vector filtering or replacement",
    )

    def validated(self) -> "LandingRadarUpdateConfig":
        threshold = (
            None
            if self.velocity_update_speed_threshold_m_s is None
            else _finite(
                self.velocity_update_speed_threshold_m_s,
                "velocity_update_speed_threshold_m_s",
            )
        )
        if threshold is not None and threshold < 0.0:
            raise ValueError(
                "velocity_update_speed_threshold_m_s must be non-negative"
            )
        applicability = str(self.applicability).strip()
        if not applicability:
            raise ValueError("applicability must not be empty")
        return LandingRadarUpdateConfig(
            velocity_update_speed_threshold_m_s=threshold,
            applicability=applicability,
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class LandingRadarUpdateAssessment:
    measurement_time_s: float
    data_good: bool
    updates_enabled: bool
    estimated_speed_m_s: float
    altitude_present: bool
    velocity_present: bool
    altitude_eligible: bool
    velocity_eligible: bool
    reasons: tuple[str, ...]
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "landing_radar_update_gate_not_historically_validated",
            "measurement_time_s": self.measurement_time_s,
            "data_good": self.data_good,
            "updates_enabled": self.updates_enabled,
            "estimated_speed_m_s": self.estimated_speed_m_s,
            "altitude_present": self.altitude_present,
            "velocity_present": self.velocity_present,
            "altitude_eligible": self.altitude_eligible,
            "velocity_eligible": self.velocity_eligible,
            "reasons": list(self.reasons),
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def assess_landing_radar_update(
    measurement: LandingRadarMeasurement,
    context: LandingRadarGuidanceContext,
    config: LandingRadarUpdateConfig,
) -> LandingRadarUpdateAssessment:
    """Assess whether supplied radar channels may enter a downstream estimator."""

    checked_measurement = measurement.validated()
    checked_context = context.validated()
    checked_config = config.validated()

    if checked_measurement.time_s < checked_context.time_s:
        raise ValueError("measurement time cannot precede guidance context time")

    reasons: list[str] = []
    common_ok = checked_measurement.data_good and checked_context.updates_enabled

    if not checked_measurement.data_good:
        reasons.append("radar_data_not_good")
    if not checked_context.updates_enabled:
        reasons.append("radar_updates_not_enabled")

    altitude_present = checked_measurement.altitude_m is not None
    velocity_present = checked_measurement.velocity_m_s is not None

    if not altitude_present:
        reasons.append("altitude_measurement_missing")
    if not velocity_present:
        reasons.append("velocity_measurement_missing")

    altitude_eligible = common_ok and altitude_present

    threshold_ok = True
    threshold = checked_config.velocity_update_speed_threshold_m_s
    if threshold is not None and checked_context.estimated_speed_m_s >= threshold:
        threshold_ok = False
        reasons.append("estimated_speed_above_velocity_update_threshold")

    velocity_eligible = common_ok and velocity_present and threshold_ok

    return LandingRadarUpdateAssessment(
        measurement_time_s=checked_measurement.time_s,
        data_good=checked_measurement.data_good,
        updates_enabled=checked_context.updates_enabled,
        estimated_speed_m_s=checked_context.estimated_speed_m_s,
        altitude_present=altitude_present,
        velocity_present=velocity_present,
        altitude_eligible=altitude_eligible,
        velocity_eligible=velocity_eligible,
        reasons=tuple(reasons),
        applicability=checked_config.applicability,
        provenance=checked_config.provenance,
        assumptions=checked_config.assumptions,
    )
