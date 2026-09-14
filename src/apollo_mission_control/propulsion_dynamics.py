"""Framework-neutral Level-1 propulsion/translational dynamics.

This module is the first causal numerical proof for the Apollo Mission Control
simulation. It deliberately models only thrust, propellant mass depletion, and
vector delta-V. It does not yet claim orbital propagation, gravity, rotational
dynamics, detailed DPS feed-system behavior, or Apollo-13-specific engine
performance.

All calculations use SI internally. Mission/scenario adapters may convert
Apollo source units at their boundary.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from math import isfinite, log, sqrt
from typing import Iterable


STANDARD_GRAVITY_M_S2 = 9.80665
LBF_TO_NEWTON = 4.4482216152605
LBM_TO_KG = 0.45359237
FT_TO_M = 0.3048


@dataclass(frozen=True)
class Vector3:
    x: float
    y: float
    z: float

    def __add__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def scale(self, scalar: float) -> "Vector3":
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def magnitude(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalized(self) -> "Vector3":
        mag = self.magnitude()
        if mag <= 0.0:
            raise ValueError("Thrust direction must be non-zero")
        return self.scale(1.0 / mag)

    def is_finite(self) -> bool:
        return isfinite(self.x) and isfinite(self.y) and isfinite(self.z)


ZERO_VECTOR = Vector3(0.0, 0.0, 0.0)
UNIT_X = Vector3(1.0, 0.0, 0.0)


@dataclass(frozen=True)
class PropulsionModel:
    """Source/profile-specific constants used by the Level-1 model."""

    full_thrust_n: float
    specific_impulse_s: float
    standard_gravity_m_s2: float = STANDARD_GRAVITY_M_S2

    def __post_init__(self) -> None:
        if not isfinite(self.full_thrust_n) or self.full_thrust_n <= 0.0:
            raise ValueError("full_thrust_n must be positive and finite")
        if not isfinite(self.specific_impulse_s) or self.specific_impulse_s <= 0.0:
            raise ValueError("specific_impulse_s must be positive and finite")
        if (
            not isfinite(self.standard_gravity_m_s2)
            or self.standard_gravity_m_s2 <= 0.0
        ):
            raise ValueError("standard_gravity_m_s2 must be positive and finite")

    @property
    def effective_exhaust_velocity_m_s(self) -> float:
        return self.specific_impulse_s * self.standard_gravity_m_s2


@dataclass(frozen=True)
class PropulsionState:
    """Authoritative Level-1 physical state.

    Position and gravity are intentionally absent from this first slice.
    velocity_m_s is therefore a working-frame velocity whose change is the
    thrust-produced vector delta-V.
    """

    elapsed_s: float
    mass_kg: float
    velocity_m_s: Vector3 = ZERO_VECTOR
    engine_running: bool = False
    throttle_fraction: float = 0.0
    thrust_direction: Vector3 = UNIT_X
    accumulated_impulse_n_s: float = 0.0
    propellant_used_kg: float = 0.0

    def __post_init__(self) -> None:
        if not isfinite(self.elapsed_s) or self.elapsed_s < 0.0:
            raise ValueError("elapsed_s must be non-negative and finite")
        if not isfinite(self.mass_kg) or self.mass_kg <= 0.0:
            raise ValueError("mass_kg must be positive and finite")
        if not self.velocity_m_s.is_finite():
            raise ValueError("velocity_m_s must be finite")
        if (
            not isfinite(self.throttle_fraction)
            or not 0.0 <= self.throttle_fraction <= 1.0
        ):
            raise ValueError("throttle_fraction must be between 0 and 1")
        if not self.thrust_direction.is_finite():
            raise ValueError("thrust_direction must be finite")
        if (
            not isfinite(self.accumulated_impulse_n_s)
            or self.accumulated_impulse_n_s < 0.0
        ):
            raise ValueError("accumulated_impulse_n_s must be non-negative and finite")
        if not isfinite(self.propellant_used_kg) or self.propellant_used_kg < 0.0:
            raise ValueError("propellant_used_kg must be non-negative and finite")


@dataclass(frozen=True)
class BurnSegment:
    """Piecewise-constant crew/engine command used by validation profiles."""

    duration_s: float
    throttle_fraction: float
    thrust_direction: Vector3 = UNIT_X
    engine_running: bool = True

    def __post_init__(self) -> None:
        if not isfinite(self.duration_s) or self.duration_s < 0.0:
            raise ValueError("duration_s must be non-negative and finite")
        if (
            not isfinite(self.throttle_fraction)
            or not 0.0 <= self.throttle_fraction <= 1.0
        ):
            raise ValueError("throttle_fraction must be between 0 and 1")
        if not self.thrust_direction.is_finite():
            raise ValueError("thrust_direction must be finite")


def command_propulsion(
    state: PropulsionState,
    *,
    engine_running: bool | None = None,
    throttle_fraction: float | None = None,
    thrust_direction: Vector3 | None = None,
) -> PropulsionState:
    """Apply a crew/commanded propulsion configuration without advancing time."""

    kwargs: dict[str, object] = {}
    if engine_running is not None:
        kwargs["engine_running"] = bool(engine_running)
    if throttle_fraction is not None:
        if not isfinite(throttle_fraction) or not 0.0 <= throttle_fraction <= 1.0:
            raise ValueError("throttle_fraction must be between 0 and 1")
        kwargs["throttle_fraction"] = float(throttle_fraction)
    if thrust_direction is not None:
        if not thrust_direction.is_finite():
            raise ValueError("thrust_direction must be finite")
        kwargs["thrust_direction"] = thrust_direction
    return replace(state, **kwargs)


def step_propulsion(
    state: PropulsionState,
    model: PropulsionModel,
    dt_s: float,
) -> PropulsionState:
    """Advance the Level-1 propulsion state by dt_s.

    During one step thrust and direction are constant. Mass flow is derived
    from thrust and specific impulse. The velocity increment uses the ideal
    variable-mass rocket equation for that interval.

    No gravity or external force is included. This is a thrust-produced
    delta-V proof, not yet an orbital trajectory solution.
    """

    if not isfinite(dt_s) or dt_s < 0.0:
        raise ValueError("dt_s must be non-negative and finite")
    if dt_s == 0.0:
        return state

    if not state.engine_running or state.throttle_fraction == 0.0:
        return replace(state, elapsed_s=state.elapsed_s + dt_s)

    direction = state.thrust_direction.normalized()
    thrust_n = model.full_thrust_n * state.throttle_fraction
    exhaust_velocity = model.effective_exhaust_velocity_m_s
    mass_flow_kg_s = thrust_n / exhaust_velocity
    propellant_kg = mass_flow_kg_s * dt_s
    final_mass_kg = state.mass_kg - propellant_kg
    if final_mass_kg <= 0.0:
        raise ValueError("Propulsion step would consume all vehicle mass")

    delta_v_m_s = exhaust_velocity * log(state.mass_kg / final_mass_kg)
    final_velocity = state.velocity_m_s + direction.scale(delta_v_m_s)

    return replace(
        state,
        elapsed_s=state.elapsed_s + dt_s,
        mass_kg=final_mass_kg,
        velocity_m_s=final_velocity,
        accumulated_impulse_n_s=state.accumulated_impulse_n_s + thrust_n * dt_s,
        propellant_used_kg=state.propellant_used_kg + propellant_kg,
    )


def run_burn_segments(
    initial_state: PropulsionState,
    model: PropulsionModel,
    segments: Iterable[BurnSegment],
    *,
    step_s: float = 0.1,
) -> PropulsionState:
    """Run arbitrary piecewise-constant commands through one causal model."""

    if not isfinite(step_s) or step_s <= 0.0:
        raise ValueError("step_s must be positive and finite")

    state = initial_state
    for segment in segments:
        state = command_propulsion(
            state,
            engine_running=segment.engine_running,
            throttle_fraction=segment.throttle_fraction,
            thrust_direction=segment.thrust_direction,
        )
        remaining = segment.duration_s
        while remaining > 0.0:
            dt = min(step_s, remaining)
            state = step_propulsion(state, model, dt)
            remaining -= dt
            if remaining < 1e-12:
                remaining = 0.0
    return state


def delta_v_vector(
    initial_velocity_m_s: Vector3,
    final_state: PropulsionState,
) -> Vector3:
    return final_state.velocity_m_s - initial_velocity_m_s


def lbf_to_newtons(value: float) -> float:
    return float(value) * LBF_TO_NEWTON


def pounds_mass_to_kg(value: float) -> float:
    return float(value) * LBM_TO_KG


def feet_per_second_to_meters_per_second(value: float) -> float:
    return float(value) * FT_TO_M


def meters_per_second_to_feet_per_second(value: float) -> float:
    return float(value) / FT_TO_M
