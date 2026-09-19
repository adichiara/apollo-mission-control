"""Composed landing-radar velocity-estimator proof boundary.

This module composes already source-controlled stages without synthesizing the
remaining historical inputs.  In particular, the measurement-time selected beam
is supplied explicitly; antenna/CDU beam synthesis remains a separate boundary.
"""

from __future__ import annotations

from dataclasses import dataclass

from .landing_radar_propagation import (
    LandingRadarMeasurementTimePropagationInput,
    LandingRadarMeasurementTimePropagationResult,
    propagate_landing_radar_measurement_time_velocity,
)
from .landing_radar_quality import (
    AffineResidualRule,
    LandingRadarQualityConfig,
    LandingRadarQualityInput,
    LandingRadarQualityResult,
    RadarScalarChannel,
    qualify_landing_radar_measurements,
)
from .landing_radar_reference import (
    LandingRadarVelocityReference,
    LandingRadarVelocityReferenceInput,
    compute_landing_radar_velocity_reference,
)
from .landing_radar_velocity_update import (
    LandingRadarVelocityUpdateInput,
    LandingRadarVelocityUpdateResult,
    LandingRadarVelocityWeightConfig,
    apply_landing_radar_velocity_update,
)

Vector3 = tuple[float, float, float]


@dataclass(frozen=True)
class LandingRadarVelocityChainInput:
    propagation: LandingRadarMeasurementTimePropagationInput
    measured_velocity_m_s: float
    beam_unit_vector: Vector3
    component: str
    estimated_speed_m_s: float
    quality_time_s: float
    data_good: bool
    data_good_since_s: float | None
    residual_rule: AffineResidualRule
    min_data_good_duration_s: float
    weighting: LandingRadarVelocityWeightConfig
    program: str | None = None
    updates_permitted: bool = True


@dataclass(frozen=True)
class LandingRadarVelocityChainResult:
    propagation: LandingRadarMeasurementTimePropagationResult
    reference: LandingRadarVelocityReference
    quality: LandingRadarQualityResult
    update: LandingRadarVelocityUpdateResult

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "landing_radar_composed_velocity_estimator_proof",
            "propagation": self.propagation.to_dict(),
            "reference": self.reference.to_dict(),
            "quality": self.quality.to_dict(),
            "update": self.update.to_dict(),
            "historical_boundary": (
                "measurement-time beam is caller supplied; this proof does not "
                "synthesize LM-5 antenna/CDU geometry, radar measurements, or noise"
            ),
        }


def evaluate_landing_radar_velocity_chain(
    request: LandingRadarVelocityChainInput,
) -> LandingRadarVelocityChainResult:
    """Compose propagation, projection, qualification, and weighted correction."""

    propagation = propagate_landing_radar_measurement_time_velocity(request.propagation)
    reference = compute_landing_radar_velocity_reference(
        LandingRadarVelocityReferenceInput(
            estimated_velocity_m_s=propagation.measurement_time_velocity_m_s,
            lunar_surface_velocity_m_s=request.propagation.lunar_surface_velocity_m_s,
            beam_unit_vector=request.beam_unit_vector,
            component=request.component,
            provenance=request.propagation.provenance,
            assumptions=(
                "beam_unit_vector is the selected measurement-time LR velocity beam",
                "LM-5 antenna/CDU beam synthesis is upstream and not inferred here",
            ),
        )
    )
    quality = qualify_landing_radar_measurements(
        LandingRadarQualityInput(
            time_s=request.quality_time_s,
            data_good=request.data_good,
            data_good_since_s=request.data_good_since_s,
            channels={
                request.component: RadarScalarChannel(
                    measured_value=request.measured_velocity_m_s,
                    reference_value=reference.reference_velocity_m_s,
                    unit="m/s",
                )
            },
            source="composed landing-radar velocity-estimator proof",
        ),
        LandingRadarQualityConfig(
            min_data_good_duration_s=request.min_data_good_duration_s,
            residual_rules={request.component: request.residual_rule},
            applicability="composed LR velocity residual qualification",
            provenance=request.propagation.provenance,
        ),
    )
    channel = quality.channel(request.component)
    update = apply_landing_radar_velocity_update(
        LandingRadarVelocityUpdateInput(
            prior_velocity_m_s=propagation.measurement_time_velocity_m_s,
            estimated_speed_m_s=request.estimated_speed_m_s,
            measured_minus_reference_m_s=channel.residual,
            beam_unit_vector=request.beam_unit_vector,
            component=request.component,
            program=request.program,
            reasonableness_passed=channel.accepted,
            updates_permitted=request.updates_permitted,
        ),
        request.weighting,
    )
    return LandingRadarVelocityChainResult(
        propagation=propagation,
        reference=reference,
        quality=quality,
        update=update,
    )
