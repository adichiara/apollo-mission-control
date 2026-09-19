"""Landing-radar velocity-reference projection.

This module implements only the source-backed vector boundary used by Apollo
landing-radar velocity reasonableness testing:

estimated vehicle velocity
- lunar-surface velocity
-> vehicle velocity relative to the lunar surface
-> projection on the selected landing-radar velocity-beam unit vector.

It deliberately does not determine the historical LM antenna attitude, transform
Navigation Base coordinates into the platform frame, generate radar measurements,
or perform the downstream state-vector update.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
from typing import Iterable


Vector3 = tuple[float, float, float]


def _finite(value: float, name: str) -> float:
    result = float(value)
    if not isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


def _vector(value: Iterable[float], name: str) -> Vector3:
    result = tuple(_finite(component, name) for component in value)
    if len(result) != 3:
        raise ValueError(f"{name} must have exactly three components")
    return result  # type: ignore[return-value]


def _text(value: str, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


def _norm(vector: Vector3) -> float:
    return sqrt(sum(component * component for component in vector))


@dataclass(frozen=True)
class LandingRadarVelocityReferenceInput:
    """Inputs already expressed in one common frame at measurement time."""

    estimated_velocity_m_s: Vector3
    lunar_surface_velocity_m_s: Vector3
    beam_unit_vector: Vector3
    component: str = "velocity_axis"
    unit_vector_tolerance: float = 1.0e-6
    applicability: str = (
        "landing-radar velocity-reference projection; "
        "historical beam/attitude transform supplied upstream"
    )
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "estimated velocity and lunar-surface velocity use the same coordinate frame and epoch",
        "beam_unit_vector is the selected landing-radar velocity axis expressed in that same frame",
        "historical antenna/vehicle/platform transformation is an upstream responsibility",
    )

    def validated(self) -> "LandingRadarVelocityReferenceInput":
        estimated = _vector(self.estimated_velocity_m_s, "estimated_velocity_m_s")
        surface = _vector(
            self.lunar_surface_velocity_m_s,
            "lunar_surface_velocity_m_s",
        )
        beam = _vector(self.beam_unit_vector, "beam_unit_vector")
        tolerance = _finite(self.unit_vector_tolerance, "unit_vector_tolerance")
        if tolerance < 0.0:
            raise ValueError("unit_vector_tolerance must be non-negative")
        beam_norm = _norm(beam)
        if beam_norm == 0.0:
            raise ValueError("beam_unit_vector must be non-zero")
        if abs(beam_norm - 1.0) > tolerance:
            raise ValueError(
                "beam_unit_vector must be unit length within unit_vector_tolerance"
            )
        return LandingRadarVelocityReferenceInput(
            estimated_velocity_m_s=estimated,
            lunar_surface_velocity_m_s=surface,
            beam_unit_vector=beam,
            component=_text(self.component, "component"),
            unit_vector_tolerance=tolerance,
            applicability=_text(self.applicability, "applicability"),
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class LandingRadarVelocityReference:
    component: str
    estimated_velocity_m_s: Vector3
    lunar_surface_velocity_m_s: Vector3
    relative_surface_velocity_m_s: Vector3
    beam_unit_vector: Vector3
    reference_velocity_m_s: float
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "landing_radar_velocity_reference_projection",
            "component": self.component,
            "estimated_velocity_m_s": list(self.estimated_velocity_m_s),
            "lunar_surface_velocity_m_s": list(self.lunar_surface_velocity_m_s),
            "relative_surface_velocity_m_s": list(
                self.relative_surface_velocity_m_s
            ),
            "beam_unit_vector": list(self.beam_unit_vector),
            "reference_velocity_m_s": self.reference_velocity_m_s,
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def compute_landing_radar_velocity_reference(
    request: LandingRadarVelocityReferenceInput,
) -> LandingRadarVelocityReference:
    """Project lunar-surface-relative estimated velocity on a selected LR beam."""

    checked = request.validated()
    relative = tuple(
        estimated - surface
        for estimated, surface in zip(
            checked.estimated_velocity_m_s,
            checked.lunar_surface_velocity_m_s,
        )
    )
    reference = sum(
        velocity * beam
        for velocity, beam in zip(relative, checked.beam_unit_vector)
    )
    return LandingRadarVelocityReference(
        component=checked.component,
        estimated_velocity_m_s=checked.estimated_velocity_m_s,
        lunar_surface_velocity_m_s=checked.lunar_surface_velocity_m_s,
        relative_surface_velocity_m_s=relative,  # type: ignore[arg-type]
        beam_unit_vector=checked.beam_unit_vector,
        reference_velocity_m_s=reference,
        applicability=checked.applicability,
        provenance=checked.provenance,
        assumptions=checked.assumptions,
    )
