"""Landing-radar velocity weighting and state-vector correction.

This module models the reusable estimator/update boundary after a landing-radar
velocity component has already passed upstream measurement qualification.

The historical Apollo 11 profile supplies thresholds and weighting constants;
the generic implementation contains no Apollo constants.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
from typing import Iterable, Mapping


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


def _text(value: str, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


def _weights(values: Mapping[str, float], name: str) -> dict[str, float]:
    result: dict[str, float] = {}
    for raw_component, raw_value in dict(values).items():
        component = _text(raw_component, f"{name} component").lower()
        value = _finite(raw_value, f"{name}[{component}]")
        if value < 0.0:
            raise ValueError(f"{name}[{component}] must be non-negative")
        result[component] = value
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


def _norm(vector: Vector3) -> float:
    return sqrt(sum(component * component for component in vector))


@dataclass(frozen=True)
class LandingRadarVelocityWeightConfig:
    maximum_speed_m_s: float
    low_speed_threshold_m_s: float
    linear_component_weights: Mapping[str, float]
    low_speed_component_weights: Mapping[str, float]
    override_programs: tuple[str, ...] = ()
    override_weight: float | None = None
    unit_vector_tolerance: float = 1.0e-6
    applicability: str = (
        "generic landing-radar velocity weighting/update; "
        "historical constants supplied by profile"
    )
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "residual has already passed the upstream reasonableness test",
        "prior velocity and selected beam are expressed in the same frame",
        "selected beam is the measurement-time velocity-component direction",
        "program override semantics are supplied explicitly by the selected profile",
    )

    def validated(self) -> "LandingRadarVelocityWeightConfig":
        maximum = _finite(self.maximum_speed_m_s, "maximum_speed_m_s")
        low = _finite(self.low_speed_threshold_m_s, "low_speed_threshold_m_s")
        if maximum <= 0.0:
            raise ValueError("maximum_speed_m_s must be positive")
        if low < 0.0:
            raise ValueError("low_speed_threshold_m_s must be non-negative")
        if low >= maximum:
            raise ValueError(
                "low_speed_threshold_m_s must be below maximum_speed_m_s"
            )

        linear = _weights(self.linear_component_weights, "linear_component_weights")
        low_weights = _weights(
            self.low_speed_component_weights,
            "low_speed_component_weights",
        )
        if set(linear) != set(low_weights):
            raise ValueError(
                "linear_component_weights and low_speed_component_weights "
                "must define the same components"
            )

        programs = tuple(
            _text(program, "override program").upper()
            for program in self.override_programs
        )
        if len(programs) != len(set(programs)):
            raise ValueError("override_programs must be unique")

        override = (
            None
            if self.override_weight is None
            else _finite(self.override_weight, "override_weight")
        )
        if programs and override is None:
            raise ValueError(
                "override_weight is required when override_programs are configured"
            )
        if override is not None and override < 0.0:
            raise ValueError("override_weight must be non-negative")

        tolerance = _finite(self.unit_vector_tolerance, "unit_vector_tolerance")
        if tolerance < 0.0:
            raise ValueError("unit_vector_tolerance must be non-negative")

        return LandingRadarVelocityWeightConfig(
            maximum_speed_m_s=maximum,
            low_speed_threshold_m_s=low,
            linear_component_weights=linear,
            low_speed_component_weights=low_weights,
            override_programs=programs,
            override_weight=override,
            unit_vector_tolerance=tolerance,
            applicability=_text(self.applicability, "applicability"),
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class LandingRadarVelocityUpdateInput:
    prior_velocity_m_s: Vector3
    estimated_speed_m_s: float
    measured_minus_reference_m_s: float
    beam_unit_vector: Vector3
    component: str
    program: str | None = None
    reasonableness_passed: bool = True
    updates_permitted: bool = True

    def validated(
        self,
        *,
        unit_vector_tolerance: float,
    ) -> "LandingRadarVelocityUpdateInput":
        prior = _vector(self.prior_velocity_m_s, "prior_velocity_m_s")
        speed = _finite(self.estimated_speed_m_s, "estimated_speed_m_s")
        if speed < 0.0:
            raise ValueError("estimated_speed_m_s must be non-negative")
        residual = _finite(
            self.measured_minus_reference_m_s,
            "measured_minus_reference_m_s",
        )
        beam = _vector(self.beam_unit_vector, "beam_unit_vector")
        beam_norm = _norm(beam)
        if beam_norm == 0.0:
            raise ValueError("beam_unit_vector must be non-zero")
        if abs(beam_norm - 1.0) > unit_vector_tolerance:
            raise ValueError(
                "beam_unit_vector must be unit length within unit_vector_tolerance"
            )
        program = None if self.program is None else _text(self.program, "program").upper()
        return LandingRadarVelocityUpdateInput(
            prior_velocity_m_s=prior,
            estimated_speed_m_s=speed,
            measured_minus_reference_m_s=residual,
            beam_unit_vector=beam,
            component=_text(self.component, "component").lower(),
            program=program,
            reasonableness_passed=bool(self.reasonableness_passed),
            updates_permitted=bool(self.updates_permitted),
        )


@dataclass(frozen=True)
class LandingRadarVelocityUpdateResult:
    component: str
    program: str | None
    estimated_speed_m_s: float
    residual_m_s: float
    selected_weight: float
    weight_regime: str
    update_applied: bool
    delta_velocity_m_s: Vector3
    prior_velocity_m_s: Vector3
    updated_velocity_m_s: Vector3
    reasons: tuple[str, ...]
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "landing_radar_velocity_update",
            "component": self.component,
            "program": self.program,
            "estimated_speed_m_s": self.estimated_speed_m_s,
            "residual_m_s": self.residual_m_s,
            "selected_weight": self.selected_weight,
            "weight_regime": self.weight_regime,
            "update_applied": self.update_applied,
            "delta_velocity_m_s": list(self.delta_velocity_m_s),
            "prior_velocity_m_s": list(self.prior_velocity_m_s),
            "updated_velocity_m_s": list(self.updated_velocity_m_s),
            "reasons": list(self.reasons),
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def _select_weight(
    request: LandingRadarVelocityUpdateInput,
    config: LandingRadarVelocityWeightConfig,
) -> tuple[float, str]:
    component = request.component
    if component not in config.linear_component_weights:
        raise ValueError(f"unknown velocity component: {component!r}")

    if request.program is not None and request.program in config.override_programs:
        assert config.override_weight is not None
        return config.override_weight, "program_override"

    speed = request.estimated_speed_m_s
    if speed <= config.low_speed_threshold_m_s:
        return config.low_speed_component_weights[component], "low_speed_constant"
    if speed >= config.maximum_speed_m_s:
        return 0.0, "at_or_above_maximum_speed"

    weight = config.linear_component_weights[component] * (
        1.0 - (speed / config.maximum_speed_m_s)
    )
    return weight, "linear_with_speed"


def apply_landing_radar_velocity_update(
    request: LandingRadarVelocityUpdateInput,
    config: LandingRadarVelocityWeightConfig,
) -> LandingRadarVelocityUpdateResult:
    """Apply one accepted landing-radar velocity-component correction."""

    checked_config = config.validated()
    checked = request.validated(
        unit_vector_tolerance=checked_config.unit_vector_tolerance
    )

    reasons: list[str] = []
    if not checked.reasonableness_passed:
        reasons.append("reasonableness_test_failed")
    if not checked.updates_permitted:
        reasons.append("landing_radar_updates_inhibited")

    if reasons:
        weight = 0.0
        regime = "bypassed"
        applied = False
        delta = (0.0, 0.0, 0.0)
        updated = checked.prior_velocity_m_s
    else:
        weight, regime = _select_weight(checked, checked_config)
        scalar_correction = weight * checked.measured_minus_reference_m_s
        delta = tuple(
            scalar_correction * component
            for component in checked.beam_unit_vector
        )
        updated = tuple(
            prior + correction
            for prior, correction in zip(checked.prior_velocity_m_s, delta)
        )
        applied = weight != 0.0
        if not applied:
            reasons.append("weight_zero_at_or_above_maximum_speed")

    return LandingRadarVelocityUpdateResult(
        component=checked.component,
        program=checked.program,
        estimated_speed_m_s=checked.estimated_speed_m_s,
        residual_m_s=checked.measured_minus_reference_m_s,
        selected_weight=weight,
        weight_regime=regime,
        update_applied=applied,
        delta_velocity_m_s=delta,  # type: ignore[arg-type]
        prior_velocity_m_s=checked.prior_velocity_m_s,
        updated_velocity_m_s=updated,  # type: ignore[arg-type]
        reasons=tuple(reasons),
        applicability=checked_config.applicability,
        provenance=checked_config.provenance,
        assumptions=checked_config.assumptions,
    )
