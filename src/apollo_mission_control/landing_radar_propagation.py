"""Mission-neutral landing-radar measurement-time velocity propagation.

The flown Apollo 11 LUMINARY 099 VELUPDAT path advances the prior guidance
velocity to the radar measurement epoch using a caller-supplied PIPA-derived
increment and previous-gravity contribution, then subtracts the lunar-rotation
velocity correction before beam projection. This module preserves that boundary
without inventing a gravity field, PIPA/noise model, or radar measurement model.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable

Vector3 = tuple[float, float, float]


def _vector(value: Iterable[float], name: str) -> Vector3:
    result = tuple(float(component) for component in value)
    if len(result) != 3 or not all(isfinite(component) for component in result):
        raise ValueError(f"{name} must contain exactly three finite components")
    return result  # type: ignore[return-value]


@dataclass(frozen=True)
class LandingRadarMeasurementTimePropagationInput:
    prior_guidance_velocity_m_s: Vector3
    pipa_delta_velocity_m_s: Vector3
    previous_gravity_m_s2: Vector3
    delta_time_s: float
    lunar_surface_velocity_m_s: Vector3
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "all vectors use one common frame",
        "pipa_delta_velocity_m_s is already converted to physical velocity units",
        "previous_gravity_m_s2 is the caller-supplied previous guidance gravity vector",
        "delta_time_s is measurement epoch minus prior guidance/PIPA epoch",
        "no PIPA, gravity-field, radar-noise, or measurement-generation model is implied",
    )

    def validated(self) -> "LandingRadarMeasurementTimePropagationInput":
        dt = float(self.delta_time_s)
        if not isfinite(dt) or dt < 0.0:
            raise ValueError("delta_time_s must be finite and non-negative")
        return LandingRadarMeasurementTimePropagationInput(
            prior_guidance_velocity_m_s=_vector(self.prior_guidance_velocity_m_s, "prior_guidance_velocity_m_s"),
            pipa_delta_velocity_m_s=_vector(self.pipa_delta_velocity_m_s, "pipa_delta_velocity_m_s"),
            previous_gravity_m_s2=_vector(self.previous_gravity_m_s2, "previous_gravity_m_s2"),
            delta_time_s=dt,
            lunar_surface_velocity_m_s=_vector(self.lunar_surface_velocity_m_s, "lunar_surface_velocity_m_s"),
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class LandingRadarMeasurementTimePropagationResult:
    measurement_time_velocity_m_s: Vector3
    relative_surface_velocity_m_s: Vector3
    gravity_delta_velocity_m_s: Vector3
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "landing_radar_measurement_time_propagation",
            "measurement_time_velocity_m_s": list(self.measurement_time_velocity_m_s),
            "relative_surface_velocity_m_s": list(self.relative_surface_velocity_m_s),
            "gravity_delta_velocity_m_s": list(self.gravity_delta_velocity_m_s),
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def propagate_landing_radar_measurement_time_velocity(
    request: LandingRadarMeasurementTimePropagationInput,
) -> LandingRadarMeasurementTimePropagationResult:
    checked = request.validated()
    gravity_dv = tuple(component * checked.delta_time_s for component in checked.previous_gravity_m_s2)
    measurement_velocity = tuple(
        prior + pipa + gravity
        for prior, pipa, gravity in zip(
            checked.prior_guidance_velocity_m_s,
            checked.pipa_delta_velocity_m_s,
            gravity_dv,
        )
    )
    relative_surface = tuple(
        velocity - surface
        for velocity, surface in zip(measurement_velocity, checked.lunar_surface_velocity_m_s)
    )
    return LandingRadarMeasurementTimePropagationResult(
        measurement_time_velocity_m_s=measurement_velocity,  # type: ignore[arg-type]
        relative_surface_velocity_m_s=relative_surface,  # type: ignore[arg-type]
        gravity_delta_velocity_m_s=gravity_dv,  # type: ignore[arg-type]
        provenance=checked.provenance,
        assumptions=checked.assumptions,
    )
