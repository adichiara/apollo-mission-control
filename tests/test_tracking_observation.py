from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.causal_translational_model import TranslationalState  # noqa: E402
from apollo_mission_control.tracking_observation import (  # noqa: E402
    GeometricTrackingTruth,
    TrackingObservationConfig,
    TrackingStationState,
    compute_geometric_tracking_truth,
    produce_tracking_observation,
)


class TrackingObservationTests(unittest.TestCase):
    def test_geometric_range_and_range_rate(self):
        vehicle = TranslationalState(
            time_s=123.0,
            position_m=(3.0, 4.0, 0.0),
            velocity_m_s=(6.0, 8.0, 1.0),
            mass_kg=1000.0,
        )
        station = TrackingStationState(
            position_m=(0.0, 0.0, 0.0),
            velocity_m_s=(1.0, 0.0, 0.0),
        )

        truth = compute_geometric_tracking_truth(vehicle, station)

        self.assertAlmostEqual(truth.range_m, 5.0, places=12)
        self.assertEqual(truth.source_time_s, 123.0)
        self.assertAlmostEqual(truth.line_of_sight_unit[0], 0.6, places=12)
        self.assertAlmostEqual(truth.line_of_sight_unit[1], 0.8, places=12)
        expected_rate = (5.0 * 0.6) + (8.0 * 0.8)
        self.assertAlmostEqual(truth.range_rate_m_s, expected_rate, places=12)

    def test_delay_and_bias_are_observation_effects_not_truth_mutations(self):
        truth = GeometricTrackingTruth(
            source_time_s=100.0,
            range_m=1000.0,
            range_rate_m_s=-4.0,
            line_of_sight_unit=(1.0, 0.0, 0.0),
        )
        observation = produce_tracking_observation(
            truth,
            TrackingObservationConfig(
                receive_delay_s=2.5,
                range_bias_m=12.0,
                range_rate_bias_m_s=0.5,
                source="synthetic biased product",
                provenance=("unit-test input",),
            ),
        )

        self.assertEqual(truth.range_m, 1000.0)
        self.assertEqual(truth.range_rate_m_s, -4.0)
        self.assertEqual(observation.source_time_s, 100.0)
        self.assertEqual(observation.received_time_s, 102.5)
        self.assertEqual(observation.age_s, 2.5)
        self.assertEqual(observation.range_m, 1012.0)
        self.assertEqual(observation.range_rate_m_s, -3.5)
        self.assertTrue(observation.available)
        self.assertTrue(observation.valid)

    def test_unavailable_observation_withholds_values(self):
        observation = produce_tracking_observation(
            GeometricTrackingTruth(
                source_time_s=10.0,
                range_m=200.0,
                range_rate_m_s=3.0,
                line_of_sight_unit=(1.0, 0.0, 0.0),
            ),
            TrackingObservationConfig(
                available=False,
                valid=False,
                source="synthetic outage",
            ),
        )

        self.assertIsNone(observation.range_m)
        self.assertIsNone(observation.range_rate_m_s)
        self.assertFalse(observation.available)
        self.assertFalse(observation.valid)

    def test_invalid_but_available_value_remains_visible_and_flagged(self):
        observation = produce_tracking_observation(
            GeometricTrackingTruth(
                source_time_s=10.0,
                range_m=200.0,
                range_rate_m_s=3.0,
                line_of_sight_unit=(1.0, 0.0, 0.0),
            ),
            TrackingObservationConfig(
                valid=False,
                range_bias_m=50.0,
                source="synthetic bad processing",
            ),
        )

        self.assertEqual(observation.range_m, 250.0)
        self.assertEqual(observation.range_rate_m_s, 3.0)
        self.assertTrue(observation.available)
        self.assertFalse(observation.valid)

    def test_rejects_coincident_geometry(self):
        with self.assertRaisesRegex(ValueError, "must not coincide"):
            compute_geometric_tracking_truth(
                TranslationalState(
                    time_s=0.0,
                    position_m=(1.0, 2.0, 3.0),
                    velocity_m_s=(0.0, 0.0, 0.0),
                    mass_kg=1000.0,
                ),
                TrackingStationState(position_m=(1.0, 2.0, 3.0)),
            )

    def test_rejects_negative_delay(self):
        with self.assertRaisesRegex(ValueError, "receive_delay_s"):
            produce_tracking_observation(
                GeometricTrackingTruth(
                    source_time_s=0.0,
                    range_m=1.0,
                    range_rate_m_s=0.0,
                    line_of_sight_unit=(1.0, 0.0, 0.0),
                ),
                TrackingObservationConfig(receive_delay_s=-1.0),
            )


if __name__ == "__main__":
    unittest.main()
