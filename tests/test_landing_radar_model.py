from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.landing_radar_model import (  # noqa: E402
    LandingRadarGuidanceContext,
    LandingRadarMeasurement,
    LandingRadarUpdateConfig,
    assess_landing_radar_update,
)


class LandingRadarUpdateGateTests(unittest.TestCase):
    def assess(
        self,
        *,
        data_good=True,
        enabled=True,
        altitude=1000.0,
        velocity=(100.0, 0.0, 0.0),
        estimate=(500.0, 0.0, 0.0),
        threshold=600.0,
    ):
        return assess_landing_radar_update(
            LandingRadarMeasurement(
                time_s=11.0,
                data_good=data_good,
                altitude_m=altitude,
                velocity_m_s=velocity,
                source="synthetic radar",
            ),
            LandingRadarGuidanceContext(
                time_s=10.0,
                updates_enabled=enabled,
                estimated_velocity_m_s=estimate,
            ),
            LandingRadarUpdateConfig(
                velocity_update_speed_threshold_m_s=threshold,
                applicability="synthetic radar-gate test",
                provenance=("synthetic",),
            ),
        )

    def test_good_enabled_measurement_allows_altitude_and_low_speed_velocity(self):
        result = self.assess()
        self.assertTrue(result.altitude_eligible)
        self.assertTrue(result.velocity_eligible)
        self.assertEqual(result.reasons, ())

    def test_good_measurement_does_not_enter_guidance_before_updates_enabled(self):
        result = self.assess(enabled=False)
        self.assertFalse(result.altitude_eligible)
        self.assertFalse(result.velocity_eligible)
        self.assertIn("radar_updates_not_enabled", result.reasons)

    def test_bad_data_blocks_both_channels(self):
        result = self.assess(data_good=False)
        self.assertFalse(result.altitude_eligible)
        self.assertFalse(result.velocity_eligible)
        self.assertIn("radar_data_not_good", result.reasons)

    def test_velocity_threshold_can_block_velocity_while_altitude_remains_eligible(self):
        result = self.assess(estimate=(700.0, 0.0, 0.0))
        self.assertTrue(result.altitude_eligible)
        self.assertFalse(result.velocity_eligible)
        self.assertIn(
            "estimated_speed_above_velocity_update_threshold",
            result.reasons,
        )

    def test_no_threshold_allows_velocity_when_other_gates_pass(self):
        result = self.assess(
            estimate=(5000.0, 0.0, 0.0),
            threshold=None,
        )
        self.assertTrue(result.altitude_eligible)
        self.assertTrue(result.velocity_eligible)

    def test_missing_channels_are_reported_independently(self):
        no_altitude = self.assess(altitude=None)
        self.assertFalse(no_altitude.altitude_eligible)
        self.assertTrue(no_altitude.velocity_eligible)
        self.assertIn("altitude_measurement_missing", no_altitude.reasons)

        no_velocity = self.assess(velocity=None)
        self.assertTrue(no_velocity.altitude_eligible)
        self.assertFalse(no_velocity.velocity_eligible)
        self.assertIn("velocity_measurement_missing", no_velocity.reasons)

    def test_measurement_time_and_threshold_validation(self):
        with self.assertRaisesRegex(ValueError, "precede"):
            assess_landing_radar_update(
                LandingRadarMeasurement(
                    time_s=9.0,
                    data_good=True,
                    altitude_m=1.0,
                ),
                LandingRadarGuidanceContext(
                    time_s=10.0,
                    updates_enabled=True,
                    estimated_velocity_m_s=(0.0, 0.0, 0.0),
                ),
                LandingRadarUpdateConfig(),
            )

        with self.assertRaisesRegex(ValueError, "non-negative"):
            self.assess(threshold=-1.0)


if __name__ == "__main__":
    unittest.main()
