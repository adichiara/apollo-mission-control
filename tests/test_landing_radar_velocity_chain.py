import unittest

from apollo_mission_control.landing_radar_propagation import LandingRadarMeasurementTimePropagationInput
from apollo_mission_control.landing_radar_quality import AffineResidualRule
from apollo_mission_control.landing_radar_velocity_chain import LandingRadarBeamGeometryInput, LandingRadarVelocityChainInput, evaluate_landing_radar_velocity_chain
from apollo_mission_control.landing_radar_velocity_update import LandingRadarVelocityWeightConfig


class LandingRadarVelocityChainTests(unittest.TestCase):
    def weighting(self):
        return LandingRadarVelocityWeightConfig(maximum_speed_m_s=600.0, low_speed_threshold_m_s=60.0, linear_component_weights={"x": 0.3}, low_speed_component_weights={"x": 0.2}, override_programs=("P66",), override_weight=0.1, provenance=("synthetic chain test",))

    def request(self, measured=12.0, data_good_since=0.0, **kwargs):
        values = dict(propagation=LandingRadarMeasurementTimePropagationInput(prior_guidance_velocity_m_s=(10.0, 0.0, 0.0), pipa_delta_velocity_m_s=(1.0, 0.0, 0.0), previous_gravity_m_s2=(0.5, 0.0, 0.0), delta_time_s=2.0, lunar_surface_velocity_m_s=(2.0, 0.0, 0.0), provenance=("synthetic chain test",)), measured_velocity_m_s=measured, beam_unit_vector=(1.0, 0.0, 0.0), component="x", estimated_speed_m_s=50.0, quality_time_s=10.0, data_good=True, data_good_since_s=data_good_since, residual_rule=AffineResidualRule(fixed_tolerance=5.0), min_data_good_duration_s=4.0, weighting=self.weighting(), program=None)
        values.update(kwargs)
        return LandingRadarVelocityChainInput(**values)

    def test_composes_propagation_projection_quality_and_update(self):
        result = evaluate_landing_radar_velocity_chain(self.request())
        self.assertEqual(result.propagation.measurement_time_velocity_m_s, (12.0, 0.0, 0.0))
        self.assertEqual(result.reference.reference_velocity_m_s, 10.0)
        self.assertEqual(result.quality.channel("x").residual, 2.0)
        self.assertTrue(result.quality.channel("x").accepted)
        self.assertEqual(result.update.selected_weight, 0.2)
        self.assertEqual(result.update.updated_velocity_m_s, (12.4, 0.0, 0.0))

    def test_failed_quality_prevents_state_correction(self):
        result = evaluate_landing_radar_velocity_chain(self.request(measured=30.0))
        self.assertFalse(result.quality.channel("x").accepted)
        self.assertFalse(result.update.update_applied)

    def test_data_good_persistence_failure_prevents_state_correction(self):
        result = evaluate_landing_radar_velocity_chain(self.request(data_good_since=8.0))
        self.assertFalse(result.quality.channel("x").accepted)
        self.assertFalse(result.update.update_applied)

    def test_geometry_path_replaces_explicit_beam_at_zero_angles(self):
        geometry = LandingRadarBeamGeometryInput(alpha_rad=0.0, beta_rad=0.0, cdu_y_rad=0.0, cdu_z_rad=0.0, cdu_x_rad=0.0)
        result = evaluate_landing_radar_velocity_chain(self.request(beam_unit_vector=None, beam_geometry=geometry))
        self.assertEqual(result.beam_unit_vector, (1.0, 0.0, 0.0))
        self.assertIn("SETPOS", result.beam_source)
        self.assertEqual(result.reference.reference_velocity_m_s, 10.0)

    def test_geometry_path_uses_measurement_time_nbs_m_transform(self):
        geometry = LandingRadarBeamGeometryInput(alpha_rad=0.0, beta_rad=0.0, cdu_y_rad=0.0, cdu_z_rad=0.0, cdu_x_rad=0.5)
        result = evaluate_landing_radar_velocity_chain(self.request(beam_unit_vector=None, beam_geometry=geometry))
        self.assertEqual(result.beam_unit_vector, (1.0, 0.0, 0.0))
        self.assertIn("measurement-time NBSM", result.beam_source)

    def test_requires_exactly_one_beam_source(self):
        geometry = LandingRadarBeamGeometryInput(alpha_rad=0.0, beta_rad=0.0, cdu_y_rad=0.0, cdu_z_rad=0.0, cdu_x_rad=0.0)
        with self.assertRaises(ValueError):
            evaluate_landing_radar_velocity_chain(self.request(beam_geometry=geometry))
        with self.assertRaises(ValueError):
            evaluate_landing_radar_velocity_chain(self.request(beam_unit_vector=None))


if __name__ == "__main__":
    unittest.main()
