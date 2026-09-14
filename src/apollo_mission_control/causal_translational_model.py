"""Mission-neutral translational dynamics proof.

This module extends the causal propulsion proof from velocity-only integration to
position + velocity propagation with optional inverse-square central gravity.

It contains no Apollo, Earth, or Moon constants. Callers supply the gravitational
parameter, initial state, thrust profile, mass floor, and provenance.

The model is intentionally narrow:
- point-mass translation only;
- inertial thrust direction supplied by the caller;
- optional central-body gravity about a caller-supplied origin;
- no attitude, gimbal, multi-body gravity, atmosphere, oblateness, or telemetry.

Units are SI throughout.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, isfinite, sqrt
from typing import Iterable

from .causal_dps_model import (
    STANDARD_GRAVITY_M_S2,
    BurnSegment,
    Vector3,
)


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


def _add(a: Vector3, b: Vector3) -> Vector3:
    return tuple(a[i] + b[i] for i in range(3))  # type: ignore[return-value]


def _scale(vector: Vector3, factor: float) -> Vector3:
    return tuple(component * factor for component in vector)  # type: ignore[return-value]


def _gravity_acceleration(
    position_m: Vector3,
    *,
    mu_m3_s2: float,
    center_m: Vector3,
) -> Vector3:
    if mu_m3_s2 == 0.0:
        return (0.0, 0.0, 0.0)

    relative = tuple(position_m[i] - center_m[i] for i in range(3))
    radius_m = _magnitude(relative)  # type: ignore[arg-type]
    if radius_m == 0.0:
        raise ValueError("position must not coincide with gravity center when mu is positive")

    factor = -mu_m3_s2 / (radius_m ** 3)
    return tuple(component * factor for component in relative)  # type: ignore[return-value]


@dataclass(frozen=True)
class TranslationalState:
    time_s: float
    position_m: Vector3
    velocity_m_s: Vector3
    mass_kg: float

    def validated(self, *, dry_mass_kg: float, mu_m3_s2: float, center_m: Vector3) -> "TranslationalState":
        time_s = _finite(self.time_s, "time_s")
        position_m = _vector(self.position_m, "position_m")
        velocity_m_s = _vector(self.velocity_m_s, "velocity_m_s")
        mass_kg = _finite(self.mass_kg, "mass_kg")

        if mass_kg <= 0.0:
            raise ValueError("mass_kg must be positive")
        if mass_kg <= dry_mass_kg:
            raise ValueError("initial mass_kg must exceed dry_mass_kg")
        if mu_m3_s2 > 0.0:
            relative = tuple(position_m[i] - center_m[i] for i in range(3))
            if _magnitude(relative) == 0.0:  # type: ignore[arg-type]
                raise ValueError(
                    "position must not coincide with gravity center when mu is positive"
                )
        return TranslationalState(
            time_s=time_s,
            position_m=position_m,
            velocity_m_s=velocity_m_s,
            mass_kg=mass_kg,
        )


@dataclass(frozen=True)
class TranslationalConfig:
    specific_impulse_s: float
    dry_mass_kg: float
    gravitational_parameter_m3_s2: float = 0.0
    gravity_center_m: Vector3 = (0.0, 0.0, 0.0)
    max_step_s: float = 0.25
    applicability: str = "generic translational model proof; not mission validated"
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "point-mass translational dynamics",
        "caller-supplied inertial thrust direction is constant within each segment",
        "thrust is constant unless a linear segment end-thrust is supplied",
        "specific impulse is constant unless a segment override is supplied",
        "optional gravity is a single inverse-square central field",
        "no atmosphere, oblateness, third bodies, attitude, gimbal, or rotational dynamics",
        "segment boundaries are exact; no hidden engine transient physics is added",
    )

    def validated(self) -> "TranslationalConfig":
        specific_impulse_s = _finite(self.specific_impulse_s, "specific_impulse_s")
        dry_mass_kg = _finite(self.dry_mass_kg, "dry_mass_kg")
        mu = _finite(self.gravitational_parameter_m3_s2, "gravitational_parameter_m3_s2")
        center = _vector(self.gravity_center_m, "gravity_center_m")
        max_step_s = _finite(self.max_step_s, "max_step_s")
        applicability = self.applicability.strip()

        if specific_impulse_s <= 0.0:
            raise ValueError("specific_impulse_s must be positive")
        if dry_mass_kg < 0.0:
            raise ValueError("dry_mass_kg must be non-negative")
        if mu < 0.0:
            raise ValueError("gravitational_parameter_m3_s2 must be non-negative")
        if max_step_s <= 0.0:
            raise ValueError("max_step_s must be positive")
        if not applicability:
            raise ValueError("applicability must not be empty")

        return TranslationalConfig(
            specific_impulse_s=specific_impulse_s,
            dry_mass_kg=dry_mass_kg,
            gravitational_parameter_m3_s2=mu,
            gravity_center_m=center,
            max_step_s=max_step_s,
            applicability=applicability,
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class TranslationalResult:
    initial_state: TranslationalState
    final_state: TranslationalState
    elapsed_s: float
    propulsive_impulse_n_s: float
    propellant_used_kg: float
    velocity_change_m_s: Vector3
    velocity_change_magnitude_m_s: float
    integration_steps: int
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "translational_model_proof_not_historically_validated",
            "applicability": self.applicability,
            "initial_state": {
                "time_s": self.initial_state.time_s,
                "position_m": list(self.initial_state.position_m),
                "velocity_m_s": list(self.initial_state.velocity_m_s),
                "mass_kg": self.initial_state.mass_kg,
            },
            "final_state": {
                "time_s": self.final_state.time_s,
                "position_m": list(self.final_state.position_m),
                "velocity_m_s": list(self.final_state.velocity_m_s),
                "mass_kg": self.final_state.mass_kg,
            },
            "elapsed_s": self.elapsed_s,
            "propulsive_impulse_n_s": self.propulsive_impulse_n_s,
            "propellant_used_kg": self.propellant_used_kg,
            "velocity_change_m_s": list(self.velocity_change_m_s),
            "velocity_change_magnitude_m_s": self.velocity_change_magnitude_m_s,
            "integration_steps": self.integration_steps,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def simulate_translational_maneuver(
    initial_state: TranslationalState,
    segments: Iterable[BurnSegment],
    config: TranslationalConfig,
) -> TranslationalResult:
    """Propagate position, velocity, and mass with supplied thrust and optional gravity.

    A second-order midpoint method is used for translation. Linear thrust
    segments are sampled at each substep midpoint, which also makes propellant
    depletion exact for a linear thrust profile with constant effective Isp.
    """

    checked_config = config.validated()
    checked_segments = tuple(segment.validated() for segment in segments)
    if not checked_segments:
        raise ValueError("at least one burn/coast segment is required")

    state = initial_state.validated(
        dry_mass_kg=checked_config.dry_mass_kg,
        mu_m3_s2=checked_config.gravitational_parameter_m3_s2,
        center_m=checked_config.gravity_center_m,
    )

    position = state.position_m
    velocity = state.velocity_m_s
    mass_kg = state.mass_kg
    elapsed_s = 0.0
    impulse_n_s = 0.0
    integration_steps = 0

    for segment in checked_segments:
        if segment.duration_s == 0.0:
            continue

        step_count = max(1, ceil(segment.duration_s / checked_config.max_step_s))
        dt = segment.duration_s / step_count
        end_thrust_n = (
            segment.thrust_n
            if segment.end_thrust_n is None
            else segment.end_thrust_n
        )
        specific_impulse_s = (
            checked_config.specific_impulse_s
            if segment.specific_impulse_s is None
            else segment.specific_impulse_s
        )

        for step_index in range(step_count):
            start_fraction = step_index / step_count
            midpoint_fraction = (step_index + 0.5) / step_count

            start_thrust_n = segment.thrust_n + (
                end_thrust_n - segment.thrust_n
            ) * start_fraction
            midpoint_thrust_n = segment.thrust_n + (
                end_thrust_n - segment.thrust_n
            ) * midpoint_fraction

            mass_flow_kg_s = midpoint_thrust_n / (
                specific_impulse_s * STANDARD_GRAVITY_M_S2
            )
            next_mass_kg = mass_kg - mass_flow_kg_s * dt
            if next_mass_kg < checked_config.dry_mass_kg:
                raise ValueError(
                    "burn would consume mass below the configured dry_mass_kg"
                )
            midpoint_mass_kg = (mass_kg + next_mass_kg) / 2.0

            gravity_start = _gravity_acceleration(
                position,
                mu_m3_s2=checked_config.gravitational_parameter_m3_s2,
                center_m=checked_config.gravity_center_m,
            )
            thrust_start = _scale(
                segment.direction,
                start_thrust_n / mass_kg,
            )
            acceleration_start = _add(gravity_start, thrust_start)

            midpoint_position = _add(position, _scale(velocity, dt / 2.0))
            midpoint_velocity = _add(
                velocity,
                _scale(acceleration_start, dt / 2.0),
            )

            gravity_midpoint = _gravity_acceleration(
                midpoint_position,
                mu_m3_s2=checked_config.gravitational_parameter_m3_s2,
                center_m=checked_config.gravity_center_m,
            )
            thrust_midpoint = _scale(
                segment.direction,
                midpoint_thrust_n / midpoint_mass_kg,
            )
            acceleration_midpoint = _add(gravity_midpoint, thrust_midpoint)

            position = _add(position, _scale(midpoint_velocity, dt))
            velocity = _add(velocity, _scale(acceleration_midpoint, dt))
            mass_kg = next_mass_kg
            elapsed_s += dt
            impulse_n_s += midpoint_thrust_n * dt
            integration_steps += 1

    final_state = TranslationalState(
        time_s=state.time_s + elapsed_s,
        position_m=position,
        velocity_m_s=velocity,
        mass_kg=mass_kg,
    )
    velocity_change = tuple(
        final_state.velocity_m_s[i] - state.velocity_m_s[i] for i in range(3)
    )

    return TranslationalResult(
        initial_state=state,
        final_state=final_state,
        elapsed_s=elapsed_s,
        propulsive_impulse_n_s=impulse_n_s,
        propellant_used_kg=state.mass_kg - mass_kg,
        velocity_change_m_s=velocity_change,  # type: ignore[arg-type]
        velocity_change_magnitude_m_s=_magnitude(velocity_change),  # type: ignore[arg-type]
        integration_steps=integration_steps,
        applicability=checked_config.applicability,
        provenance=checked_config.provenance,
        assumptions=checked_config.assumptions,
    )
