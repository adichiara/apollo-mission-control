"""Deterministic Level-1 propulsion maneuver model proof.

This module is intentionally mission-neutral. Callers must supply every
vehicle/mission parameter; no Apollo mission constant is frozen here. The model
proves the causal contract

    delivered thrust history + mass + thrust direction -> mass and vector delta-v

without gravity, position propagation, attitude dynamics, gimbal dynamics,
pressurization physics, or telemetry modeling.

A segment may use constant thrust or a linear start-to-end thrust profile. The
latter is a generic numerical input mechanism for sourced startup, shutdown, or
blowdown histories; it is not itself an engine transient model.

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
    """One supplied portion of a delivered-thrust profile.

    ``thrust_n`` is the segment-start thrust. If ``end_thrust_n`` is omitted,
    thrust is constant. If supplied, thrust is linearly interpolated from start
    to end over the segment. ``specific_impulse_s`` optionally overrides the
    run-wide value for this segment. ``regime`` is provenance/interpretation
    metadata only; it does not select hidden physics.
    """

    duration_s: float
    thrust_n: float
    direction: Vector3
    end_thrust_n: float | None = None
    specific_impulse_s: float | None = None
    regime: str = "regulated"

    def validated(self) -> "BurnSegment":
        duration_s = _finite(self.duration_s, "duration_s")
        thrust_n = _finite(self.thrust_n, "thrust_n")
        end_thrust_n = (
            thrust_n
            if self.end_thrust_n is None
            else _finite(self.end_thrust_n, "end_thrust_n")
        )
        specific_impulse_s = (
            None
            if self.specific_impulse_s is None
            else _finite(self.specific_impulse_s, "specific_impulse_s")
        )
        regime = str(self.regime).strip()

        if duration_s < 0.0:
            raise ValueError("duration_s must be non-negative")
        if thrust_n < 0.0:
            raise ValueError("thrust_n must be non-negative")
        if end_thrust_n < 0.0:
            raise ValueError("end_thrust_n must be non-negative")
        if specific_impulse_s is not None and specific_impulse_s <= 0.0:
            raise ValueError("specific_impulse_s must be positive when supplied")
        if not regime:
            raise ValueError("regime must not be empty")

        return BurnSegment(
            duration_s=duration_s,
            thrust_n=thrust_n,
            direction=_unit_direction(
                self.direction,
                thrust_n=max(thrust_n, end_thrust_n),
            ),
            end_thrust_n=end_thrust_n,
            specific_impulse_s=specific_impulse_s,
            regime=regime,
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
        "thrust is constant within a segment unless an end thrust is supplied; then it is linearly interpolated",
        "thrust direction is constant within each segment",
        "specific impulse is constant for the run unless a segment override is supplied",
        "no gravity or external forces",
        "no position or attitude dynamics",
        "segment boundaries are exact; no implicit engine transient physics is added",
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
    """Integrate supplied thrust history and propellant depletion.

    Segment boundaries are exact. Constant-thrust segments retain the previous
    Level-1 behavior. When an end thrust is supplied, thrust is evaluated by
    linear interpolation at each integration-step midpoint. Mass flow follows
    the supplied effective specific impulse, and acceleration is evaluated at
    midpoint mass.

    This is a generic numerical profile mechanism, not an engine transient,
    pressurization, or blowdown physics model.
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
            midpoint_fraction = (step_index + 0.5) / step_count
            thrust_n = segment.thrust_n + (
                end_thrust_n - segment.thrust_n
            ) * midpoint_fraction
            mass_flow_kg_s = thrust_n / (
                specific_impulse_s * STANDARD_GRAVITY_M_S2
            )
            next_mass_kg = mass_kg - mass_flow_kg_s * dt
            if next_mass_kg < checked_config.dry_mass_kg:
                raise ValueError(
                    "burn would consume mass below the configured dry_mass_kg"
                )
            midpoint_mass_kg = (mass_kg + next_mass_kg) / 2.0
            acceleration_scale = thrust_n / midpoint_mass_kg
            for axis in range(3):
                velocity[axis] += (
                    segment.direction[axis] * acceleration_scale * dt
                )
            mass_kg = next_mass_kg
            elapsed_s += dt
            impulse_n_s += thrust_n * dt
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
