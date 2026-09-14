"""Deterministic Level-1 DPS maneuver model proof.

This module is intentionally mission-neutral. Callers must supply every
vehicle/mission parameter; no Apollo 13 constant is frozen here. The model
proves the causal contract

    thrust history + mass + thrust direction -> mass and vector delta-v

without gravity, position propagation, engine transients, attitude dynamics,
gimbal dynamics, pressurization, or telemetry modeling.

Units are SI throughout.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, isfinite, sqrt
from typing import Iterable

STANDARD_GRAVITY_M_S2 = 9.80665
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


def _magnitude(vector: Vector3) -> float:
    return sqrt(sum(component * component for component in vector))


def _unit_direction(value: Iterable[float], *, thrust_n: float) -> Vector3:
    vector = _vector(value, "direction")
    magnitude = _magnitude(vector)
    if magnitude == 0.0:
        if thrust_n == 0.0:
            return (0.0, 0.0, 0.0)
        raise ValueError("direction must be non-zero when thrust is positive")
    return tuple(component / magnitude for component in vector)  # type: ignore[return-value]


@dataclass(frozen=True)
class BurnSegment:
    """One constant-command portion of a burn profile."""

    duration_s: float
    thrust_n: float
    direction: Vector3

    def validated(self) -> "BurnSegment":
        duration_s = _finite(self.duration_s, "duration_s")
        thrust_n = _finite(self.thrust_n, "thrust_n")
        if duration_s < 0.0:
            raise ValueError("duration_s must be non-negative")
        if thrust_n < 0.0:
            raise ValueError("thrust_n must be non-negative")
        return BurnSegment(
            duration_s=duration_s,
            thrust_n=thrust_n,
            direction=_unit_direction(self.direction, thrust_n=thrust_n),
        )


@dataclass(frozen=True)
class DPSModelConfig:
    """Caller-supplied assumptions for one model run."""

    specific_impulse_s: float
    dry_mass_kg: float
    max_step_s: float = 0.25
    applicability: str = "generic model proof; not mission validated"
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "constant thrust and direction within each segment",
        "specific impulse constant for the run",
        "no gravity or external forces",
        "no position or attitude dynamics",
        "instantaneous segment transitions",
    )

    def validated(self) -> "DPSModelConfig":
        specific_impulse_s = _finite(self.specific_impulse_s, "specific_impulse_s")
        dry_mass_kg = _finite(self.dry_mass_kg, "dry_mass_kg")
        max_step_s = _finite(self.max_step_s, "max_step_s")
        if specific_impulse_s <= 0.0:
            raise ValueError("specific_impulse_s must be positive")
        if dry_mass_kg < 0.0:
            raise ValueError("dry_mass_kg must be non-negative")
        if max_step_s <= 0.0:
            raise ValueError("max_step_s must be positive")
        if not self.applicability.strip():
            raise ValueError("applicability must not be empty")
        return DPSModelConfig(
            specific_impulse_s=specific_impulse_s,
            dry_mass_kg=dry_mass_kg,
            max_step_s=max_step_s,
            applicability=self.applicability.strip(),
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class ManeuverState:
    time_s: float
    mass_kg: float
    velocity_m_s: Vector3

    def validated(self, *, dry_mass_kg: float) -> "ManeuverState":
        time_s = _finite(self.time_s, "time_s")
        mass_kg = _finite(self.mass_kg, "mass_kg")
        velocity = _vector(self.velocity_m_s, "velocity_m_s")
        if mass_kg <= 0.0:
            raise ValueError("mass_kg must be positive")
        if mass_kg <= dry_mass_kg:
            raise ValueError("initial mass_kg must exceed dry_mass_kg")
        return ManeuverState(time_s=time_s, mass_kg=mass_kg, velocity_m_s=velocity)


@dataclass(frozen=True)
class ManeuverResult:
    """Computed result plus the assumptions needed to interpret it."""

    initial_state: ManeuverState
    final_state: ManeuverState
    elapsed_s: float
    impulse_n_s: float
    propellant_used_kg: float
    delta_v_m_s: Vector3
    delta_v_magnitude_m_s: float
    integration_steps: int
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "level_1_model_proof_not_historically_validated",
            "applicability": self.applicability,
            "initial_state": {
                "time_s": self.initial_state.time_s,
                "mass_kg": self.initial_state.mass_kg,
                "velocity_m_s": list(self.initial_state.velocity_m_s),
            },
            "final_state": {
                "time_s": self.final_state.time_s,
                "mass_kg": self.final_state.mass_kg,
                "velocity_m_s": list(self.final_state.velocity_m_s),
            },
            "elapsed_s": self.elapsed_s,
            "impulse_n_s": self.impulse_n_s,
            "propellant_used_kg": self.propellant_used_kg,
            "delta_v_m_s": list(self.delta_v_m_s),
            "delta_v_magnitude_m_s": self.delta_v_magnitude_m_s,
            "integration_steps": self.integration_steps,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def simulate_dps_maneuver(
    initial_state: ManeuverState,
    segments: Iterable[BurnSegment],
    config: DPSModelConfig,
) -> ManeuverResult:
    """Integrate thrust acceleration and propellant depletion with midpoint steps.

    Segment boundaries are exact. Within a segment, mass decreases linearly and
    acceleration is evaluated at midpoint mass. Reducing max_step_s must
    converge toward the constant-specific-impulse rocket-equation result.
    """

    checked_config = config.validated()
    state = initial_state.validated(dry_mass_kg=checked_config.dry_mass_kg)
    checked_segments = tuple(segment.validated() for segment in segments)
    if not checked_segments:
        raise ValueError("at least one burn segment is required")

    mass_kg = state.mass_kg
    velocity = list(state.velocity_m_s)
    elapsed_s = 0.0
    impulse_n_s = 0.0
    integration_steps = 0

    for segment in checked_segments:
        if segment.duration_s == 0.0:
            continue
        step_count = max(1, ceil(segment.duration_s / checked_config.max_step_s))
        dt = segment.duration_s / step_count
        mass_flow_kg_s = (
            segment.thrust_n
            / (checked_config.specific_impulse_s * STANDARD_GRAVITY_M_S2)
        )
        for _ in range(step_count):
            next_mass_kg = mass_kg - mass_flow_kg_s * dt
            if next_mass_kg < checked_config.dry_mass_kg:
                raise ValueError(
                    "burn would consume mass below the configured dry_mass_kg"
                )
            midpoint_mass_kg = (mass_kg + next_mass_kg) / 2.0
            acceleration_scale = segment.thrust_n / midpoint_mass_kg
            for axis in range(3):
                velocity[axis] += segment.direction[axis] * acceleration_scale * dt
            mass_kg = next_mass_kg
            elapsed_s += dt
            impulse_n_s += segment.thrust_n * dt
            integration_steps += 1

    final_velocity = tuple(velocity)
    delta_v = tuple(
        final_velocity[axis] - state.velocity_m_s[axis] for axis in range(3)
    )
    final_state = ManeuverState(
        time_s=state.time_s + elapsed_s,
        mass_kg=mass_kg,
        velocity_m_s=final_velocity,
    )
    return ManeuverResult(
        initial_state=state,
        final_state=final_state,
        elapsed_s=elapsed_s,
        impulse_n_s=impulse_n_s,
        propellant_used_kg=state.mass_kg - mass_kg,
        delta_v_m_s=delta_v,  # type: ignore[arg-type]
        delta_v_magnitude_m_s=_magnitude(delta_v),  # type: ignore[arg-type]
        integration_steps=integration_steps,
        applicability=checked_config.applicability,
        provenance=checked_config.provenance,
        assumptions=checked_config.assumptions,
    )
