from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.landing_radar_reference import (  # noqa: E402
    LandingRadarVelocityReferenceInput,
    compute_landing_radar_velocity_reference,
)

from apollo_mission_control.landing_radar_quality import (  # noqa: E402
    AffineResidualRule,
    LandingRadarQualityConfig,
    LandingRadarQualityInput,
    RadarScalarChannel,
    qualify_landing_radar_measurements,
)


class LandingRadarQualityTests(unittest.TestCase):
    def config(self):
        return LandingRadarQualityConfig(
            min_data_good_duration_s=4.0,
            min_range_scale_stable_s=1.0,
            scale_stability_channels=("altitude",),
            residual_rules={
                "altitude": AffineResidualRule(200.0, 0.125),
                "velocity_axis": AffineResidualRule(7.5, 0.125),
            },
            applicability="synthetic source-shaped test",
            provenance=("synthetic",),
        )

    def test_persistence_scale_stability_and_affine_residual_accept(self):
        result = qualify_landing_radar_measurements(
            LandingRadarQualityInput(
                time_s=10.0,
                data_good=True,
                data_good_since_s=5.0,
                range_scale_last_changed_s=8.0,
                channels={
                    "altitude": RadarScalarChannel(
                        measured_value=1040.0,
                        reference_value=1000.0,
                        unit="ft",
                    ),
                    "velocity_axis": RadarScalarChannel(
                        measured_value=105.0,
                        reference_value=100.0,
                        unit="ft/s",
                    ),
                },
            ),
            self.config(),
        )
        self.assertTrue(result.data_good_qualified)
        self.assertTrue(result.channel("altitude").accepted)
        self.assertTrue(result.channel("velocity_axis").accepted)
        self.assertAlmostEqual(result.channel("altitude").threshold, 325.0)
        self.assertAlmostEqual(result.channel("velocity_axis").threshold, 20.0)

    def test_data_good_must_persist(self):
        result = qualify_landing_radar_measurements(
            LandingRadarQualityInput(
                time_s=10.0,
                data_good=True,
                data_good_since_s=7.0,
                range_scale_last_changed_s=0.0,
                channels={
                    "altitude": RadarScalarChannel(1000.0, 1000.0, "ft"),
                    "velocity_axis": RadarScalarChannel(100.0, 100.0, "ft/s"),
                },
            ),
            self.config(),
        )
        self.assertFalse(result.data_good_qualified)
        self.assertFalse(result.channel("altitude").accepted)
        self.assertIn(
            "data_good_persistence_not_satisfied",
            result.channel("altitude").reasons,
        )

    def test_range_scale_stability_is_channel_specific(self):
        result = qualify_landing_radar_measurements(
            LandingRadarQualityInput(
                time_s=10.0,
                data_good=True,
                data_good_since_s=0.0,
                range_scale_last_changed_s=9.5,
                channels={
                    "altitude": RadarScalarChannel(1000.0, 1000.0, "ft"),
                    "velocity_axis": RadarScalarChannel(100.0, 100.0, "ft/s"),
                },
            ),
            self.config(),
        )
        self.assertFalse(result.channel("altitude").accepted)
        self.assertIn(
            "range_scale_not_stable_long_enough",
            result.channel("altitude").reasons,
        )
        self.assertTrue(result.channel("velocity_axis").accepted)

    def test_residual_limit_is_affine_in_reference_value(self):
        result = qualify_landing_radar_measurements(
            LandingRadarQualityInput(
                time_s=10.0,
                data_good=True,
                data_good_since_s=0.0,
                range_scale_last_changed_s=0.0,
                channels={
                    "altitude": RadarScalarChannel(1400.0, 1000.0, "ft"),
                    "velocity_axis": RadarScalarChannel(121.0, 100.0, "ft/s"),
                },
            ),
            self.config(),
        )
        self.assertFalse(result.channel("altitude").accepted)
        self.assertFalse(result.channel("velocity_axis").accepted)
        self.assertIn(
            "residual_outside_limit",
            result.channel("altitude").reasons,
        )

    def test_missing_or_invalid_channels_are_not_accepted(self):
        result = qualify_landing_radar_measurements(
            LandingRadarQualityInput(
                time_s=10.0,
                data_good=True,
                data_good_since_s=0.0,
                range_scale_last_changed_s=0.0,
                channels={
                    "altitude": RadarScalarChannel(
                        1000.0,
                        1000.0,
                        "ft",
                        valid=False,
                    )
                },
            ),
            self.config(),
        )
        self.assertFalse(result.channel("altitude").accepted)
        self.assertIn("channel_invalid", result.channel("altitude").reasons)
        self.assertFalse(result.channel("velocity_axis").accepted)
        self.assertIn(
            "measurement_missing",
            result.channel("velocity_axis").reasons,
        )


    def test_reference_projection_feeds_velocity_reasonableness_rule(self):
        reference = compute_landing_radar_velocity_reference(
            LandingRadarVelocityReferenceInput(
                estimated_velocity_m_s=(100.0, 20.0, -5.0),
                lunar_surface_velocity_m_s=(10.0, 2.0, -1.0),
                beam_unit_vector=(1.0, 0.0, 0.0),
            )
        )

        accepted = qualify_landing_radar_measurements(
            LandingRadarQualityInput(
                time_s=10.0,
                data_good=True,
                data_good_since_s=5.0,
                channels={
                    "velocity_axis": RadarScalarChannel(
                        measured_value=95.0,
                        reference_value=reference.reference_velocity_m_s,
                        unit="m/s",
                    )
                },
            ),
            LandingRadarQualityConfig(
                min_data_good_duration_s=4.0,
                residual_rules={
                    "velocity_axis": AffineResidualRule(
                        fixed_tolerance=7.5,
                        proportional_tolerance=0.125,
                    )
                },
            ),
        )
        self.assertTrue(accepted.channel("velocity_axis").accepted)
        self.assertEqual(
            accepted.channel("velocity_axis").residual,
            5.0,
        )

        rejected = qualify_landing_radar_measurements(
            LandingRadarQualityInput(
                time_s=10.0,
                data_good=True,
                data_good_since_s=5.0,
                channels={
                    "velocity_axis": RadarScalarChannel(
                        measured_value=120.0,
                        reference_value=reference.reference_velocity_m_s,
                        unit="m/s",
                    )
                },
            ),
            LandingRadarQualityConfig(
                min_data_good_duration_s=4.0,
                residual_rules={
                    "velocity_axis": AffineResidualRule(
                        fixed_tolerance=7.5,
                        proportional_tolerance=0.125,
                    )
                },
            ),
        )
        self.assertFalse(rejected.channel("velocity_axis").accepted)
        self.assertIn(
            "residual_outside_limit",
            rejected.channel("velocity_axis").reasons,
        )

if __name__ == "__main__":
    unittest.main()
