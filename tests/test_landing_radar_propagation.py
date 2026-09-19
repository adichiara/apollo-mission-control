import unittest

from apollo_mission_control.landing_radar_propagation import (
    LandingRadarMeasurementTimePropagationInput,
    propagate_landing_radar_measurement_time_velocity,
)


class LandingRadarPropagationTests(unittest.TestCase):
    def test_composes_pipa_gravity_and_surface_terms(self):
        result = propagate_landing_radar_measurement_time_velocity(
            LandingRadarMeasurementTimePropagationInput(
                prior_guidance_velocity_m_s=(10.0, 20.0, 30.0),
                pipa_delta_velocity_m_s=(1.0, -2.0, 3.0),
                previous_gravity_m_s2=(0.5, 1.0, -0.5),
                delta_time_s=2.0,
                lunar_surface_velocity_m_s=(2.0, 3.0, 4.0),
            )
        )
        self.assertEqual(result.gravity_delta_velocity_m_s, (1.0, 2.0, -1.0))
        self.assertEqual(result.measurement_time_velocity_m_s, (12.0, 20.0, 32.0))
        self.assertEqual(result.relative_surface_velocity_m_s, (10.0, 17.0, 28.0))

    def test_zero_delta_time_does_not_add_gravity(self):
        result = propagate_landing_radar_measurement_time_velocity(
            LandingRadarMeasurementTimePropagationInput(
                prior_guidance_velocity_m_s=(1.0, 2.0, 3.0),
                pipa_delta_velocity_m_s=(0.1, 0.2, 0.3),
                previous_gravity_m_s2=(9.0, 9.0, 9.0),
                delta_time_s=0.0,
                lunar_surface_velocity_m_s=(0.0, 0.0, 0.0),
            )
        )
        self.assertEqual(result.measurement_time_velocity_m_s, (1.1, 2.2, 3.3))

    def test_rejects_negative_delta_time(self):
        with self.assertRaisesRegex(ValueError, "delta_time_s"):
            propagate_landing_radar_measurement_time_velocity(
                LandingRadarMeasurementTimePropagationInput(
                    prior_guidance_velocity_m_s=(0.0, 0.0, 0.0),
                    pipa_delta_velocity_m_s=(0.0, 0.0, 0.0),
                    previous_gravity_m_s2=(0.0, 0.0, 0.0),
                    delta_time_s=-0.1,
                    lunar_surface_velocity_m_s=(0.0, 0.0, 0.0),
                )
            )


if __name__ == "__main__":
    unittest.main()
