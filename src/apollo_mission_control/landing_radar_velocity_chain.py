"""Composed landing-radar velocity-estimator proof boundary.

This module composes source-controlled propagation, beam geometry, projection,
qualification, and correction. Radar measurements/noise remain caller supplied.
"""

from __future__ import annotations

from dataclasses import dataclass

from .landing_radar_propagation import LandingRadarMeasurementTimePropagationInput, LandingRadarMeasurementTimePropagationResult, propagate_landing_radar_measurement_time_velocity
from .landing_radar_quality import AffineResidualRule, LandingRadarQualityConfig, LandingRadarQualityInput, LandingRadarQualityResult, RadarScalarChannel, qualify_landing_radar_measurements
from .landing_radar_reference import LandingRadarVelocityReference, LandingRadarVelocityReferenceInput, compute_landing_radar_velocity_reference
from .landing_radar_transform import landing_radar_velocity_beams_navigation_base, navigation_base_to_stable_member
from .landing_radar_velocity_update import LandingRadarVelocityUpdateInput, LandingRadarVelocityUpdateResult, LandingRadarVelocityWeightConfig, apply_landing_radar_velocity_update

Vector3 = tuple[float, float, float]


@dataclass(frozen=True)
class LandingRadarBeamGeometryInput:
    """Source-controlled SETPOS + measurement-time NBSM inputs, in radians."""
    alpha_rad: float
    beta_rad: float
    cdu_y_rad: float
    cdu_z_rad: float
    cdu_x_rad: float

    def beam(self, component: str) -> Vector3:
        beams = dict(zip(("x", "y", "z"), landing_radar_velocity_beams_navigation_base(beta_rad=self.beta_rad, alpha_rad=self.alpha_rad)))
        try:
            nb = beams[component.lower()]
        except KeyError as exc:
            raise ValueError("component must be x, y, or z") from exc
        return navigation_base_to_stable_member(nb, cdu_y_rad=self.cdu_y_rad, cdu_z_rad=self.cdu_z_rad, cdu_x_rad=self.cdu_x_rad)


@dataclass(frozen=True)
class LandingRadarVelocityChainInput:
    propagation: LandingRadarMeasurementTimePropagationInput
    measured_velocity_m_s: float
    component: str
    estimated_speed_m_s: float
    quality_time_s: float
    data_good: bool
    data_good_since_s: float | None
    residual_rule: AffineResidualRule
    min_data_good_duration_s: float
    weighting: LandingRadarVelocityWeightConfig
    beam_unit_vector: Vector3 | None = None
    beam_geometry: LandingRadarBeamGeometryInput | None = None
    program: str | None = None
    updates_permitted: bool = True


@dataclass(frozen=True)
class LandingRadarVelocityChainResult:
    propagation: LandingRadarMeasurementTimePropagationResult
    reference: LandingRadarVelocityReference
    quality: LandingRadarQualityResult
    update: LandingRadarVelocityUpdateResult
    beam_unit_vector: Vector3
    beam_source: str

    def to_dict(self) -> dict[str, object]:
        return {"model_status": "landing_radar_composed_velocity_estimator_proof", "propagation": self.propagation.to_dict(), "reference": self.reference.to_dict(), "quality": self.quality.to_dict(), "update": self.update.to_dict(), "beam_unit_vector": self.beam_unit_vector, "beam_source": self.beam_source, "historical_boundary": "beam geometry may be synthesized from source-controlled SETPOS/NBSM inputs; radar measurement/noise remains caller supplied"}


def evaluate_landing_radar_velocity_chain(request: LandingRadarVelocityChainInput) -> LandingRadarVelocityChainResult:
    """Compose propagation, historical beam geometry, qualification, and correction."""
    if (request.beam_unit_vector is None) == (request.beam_geometry is None):
        raise ValueError("supply exactly one of beam_unit_vector or beam_geometry")
    if request.beam_geometry is not None:
        beam = request.beam_geometry.beam(request.component)
        beam_source = "source-controlled SETPOS antenna-to-NB plus measurement-time NBSM"
    else:
        beam = request.beam_unit_vector
        beam_source = "caller supplied"
    assert beam is not None

    propagation = propagate_landing_radar_measurement_time_velocity(request.propagation)
    reference = compute_landing_radar_velocity_reference(LandingRadarVelocityReferenceInput(estimated_velocity_m_s=propagation.measurement_time_velocity_m_s, lunar_surface_velocity_m_s=request.propagation.lunar_surface_velocity_m_s, beam_unit_vector=beam, component=request.component, provenance=request.propagation.provenance, assumptions=("beam is the selected measurement-time LR velocity beam", beam_source)))
    quality = qualify_landing_radar_measurements(LandingRadarQualityInput(time_s=request.quality_time_s, data_good=request.data_good, data_good_since_s=request.data_good_since_s, channels={request.component: RadarScalarChannel(measured_value=request.measured_velocity_m_s, reference_value=reference.reference_velocity_m_s, unit="m/s")}, source="composed landing-radar velocity-estimator proof"), LandingRadarQualityConfig(min_data_good_duration_s=request.min_data_good_duration_s, residual_rules={request.component: request.residual_rule}, applicability="composed LR velocity residual qualification", provenance=request.propagation.provenance))
    channel = quality.channel(request.component)
    update = apply_landing_radar_velocity_update(LandingRadarVelocityUpdateInput(prior_velocity_m_s=propagation.measurement_time_velocity_m_s, estimated_speed_m_s=request.estimated_speed_m_s, measured_minus_reference_m_s=channel.residual, beam_unit_vector=beam, component=request.component, program=request.program, reasonableness_passed=channel.accepted, updates_permitted=request.updates_permitted), request.weighting)
    return LandingRadarVelocityChainResult(propagation=propagation, reference=reference, quality=quality, update=update, beam_unit_vector=beam, beam_source=beam_source)
