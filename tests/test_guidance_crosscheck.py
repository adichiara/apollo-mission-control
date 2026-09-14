from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.guidance_crosscheck import (  # noqa: E402
    GuidanceCrosscheckConfig,
    GuidanceObservation,
    compare_guidance_observations,
)


class GuidanceCrosscheckTests(unittest.TestCase):
    def config(self):
        return GuidanceCrosscheckConfig(
            tolerances={
                "velocity_x": 2.0,
                "velocity_y": 2.0,
                "attitude_pitch": 1.0,
            },
            max_time_separation_s=1.0,
            applicability="synthetic independent-guidance test",
            provenance=("synthetic",),
        )

    def observation(
        self,
        source,
        *,
        time_s=10.0,
        valid=True,
        velocity_x=100.0,
        velocity_y=-20.0,
        attitude_pitch=5.0,
    ):
        return GuidanceObservation(
            source=source,
            time_s=time_s,
            valid=valid,
            values={
                "velocity_x": velocity_x,
                "velocity_y": velocity_y,
                "attitude_pitch": attitude_pitch,
            },
        )

    def test_independent_observations_can_agree_within_caller_tolerances(self):
        result = compare_guidance_observations(
            self.observation("PRIMARY"),
            self.observation(
                "BACKUP",
                velocity_x=101.0,
                velocity_y=-21.0,
                attitude_pitch=5.5,
            ),
            self.config(),
        )

        self.assertTrue(result.comparable)
        self.assertTrue(result.agreement)
        self.assertEqual(result.reasons, ())
        self.assertEqual(len(result.comparisons), 3)

    def test_disagreement_reports_field_differences_without_mission_decision(self):
        result = compare_guidance_observations(
            self.observation("PRIMARY"),
            self.observation("BACKUP", velocity_x=105.0),
            self.config(),
        )

        self.assertTrue(result.comparable)
        self.assertFalse(result.agreement)
        by_field = {item.field: item for item in result.comparisons}
        self.assertFalse(by_field["velocity_x"].within_tolerance)
        payload = result.to_dict()
        self.assertNotIn("abort", payload)
        self.assertNotIn("go", payload)

    def test_invalid_or_stale_observation_is_indeterminate(self):
        invalid = compare_guidance_observations(
            self.observation("PRIMARY", valid=False),
            self.observation("BACKUP"),
            self.config(),
        )
        self.assertFalse(invalid.comparable)
        self.assertIsNone(invalid.agreement)
        self.assertIn("PRIMARY_invalid", invalid.reasons)

        stale = compare_guidance_observations(
            self.observation("PRIMARY", time_s=10.0),
            self.observation("BACKUP", time_s=12.0),
            self.config(),
        )
        self.assertFalse(stale.comparable)
        self.assertIsNone(stale.agreement)
        self.assertIn("observations_too_far_apart_in_time", stale.reasons)

    def test_missing_required_field_is_indeterminate(self):
        second = GuidanceObservation(
            source="BACKUP",
            time_s=10.0,
            valid=True,
            values={
                "velocity_x": 100.0,
                "velocity_y": -20.0,
            },
        )
        result = compare_guidance_observations(
            self.observation("PRIMARY"),
            second,
            self.config(),
        )
        self.assertFalse(result.comparable)
        self.assertIsNone(result.agreement)
        self.assertIn("BACKUP_missing_attitude_pitch", result.reasons)

    def test_bad_tolerance_configuration_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "non-negative"):
            compare_guidance_observations(
                self.observation("PRIMARY"),
                self.observation("BACKUP"),
                GuidanceCrosscheckConfig(
                    tolerances={"velocity_x": -1.0},
                    max_time_separation_s=1.0,
                ),
            )


if __name__ == "__main__":
    unittest.main()
