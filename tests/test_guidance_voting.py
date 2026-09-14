from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.guidance_crosscheck import GuidanceObservation  # noqa: E402
from apollo_mission_control.guidance_voting import (  # noqa: E402
    GuidanceVotingConfig,
    assess_guidance_consensus,
)


class GuidanceVotingTests(unittest.TestCase):
    def observation(self, source, value, *, time_s=10.0, valid=True):
        return GuidanceObservation(
            source=source,
            time_s=time_s,
            valid=valid,
            values={"radial_velocity": value},
        )

    def config(self, *, tolerance=2.0, freshness=1.0, quorum=2):
        return GuidanceVotingConfig(
            tolerances={"radial_velocity": tolerance},
            max_time_separation_s=freshness,
            minimum_agreeing_sources=quorum,
            applicability="synthetic voting test",
            provenance=("synthetic",),
        )

    def field(self, result):
        return result.fields[0]

    def test_two_of_three_consensus_identifies_outside_source_without_failure_label(self):
        result = assess_guidance_consensus(
            [
                self.observation("PRIMARY", 100.0),
                self.observation("BACKUP", 101.0),
                self.observation("GROUND", 120.0),
            ],
            self.config(),
        )
        field = self.field(result)

        self.assertEqual(field.status, "consensus")
        self.assertEqual(field.consensus_sources, ("PRIMARY", "BACKUP"))
        self.assertEqual(field.outside_consensus_sources, ("GROUND",))
        payload = result.to_dict()
        self.assertNotIn("failed_sources", payload)
        self.assertNotIn("truth_source", payload)

    def test_all_three_can_form_consensus(self):
        result = assess_guidance_consensus(
            [
                self.observation("PRIMARY", 100.0),
                self.observation("BACKUP", 100.5),
                self.observation("GROUND", 99.5),
            ],
            self.config(),
        )
        field = self.field(result)
        self.assertEqual(field.status, "consensus")
        self.assertEqual(
            field.consensus_sources,
            ("PRIMARY", "BACKUP", "GROUND"),
        )
        self.assertEqual(field.outside_consensus_sources, ())

    def test_no_pair_within_tolerance_has_no_consensus(self):
        result = assess_guidance_consensus(
            [
                self.observation("PRIMARY", 100.0),
                self.observation("BACKUP", 110.0),
                self.observation("GROUND", 120.0),
            ],
            self.config(),
        )
        field = self.field(result)
        self.assertEqual(field.status, "no_consensus")
        self.assertEqual(field.consensus_sources, ())
        self.assertIn("no_agreeing_quorum", field.reasons)

    def test_nontransitive_pair_agreement_is_ambiguous_not_false_three_way_consensus(self):
        result = assess_guidance_consensus(
            [
                self.observation("A", 0.0),
                self.observation("B", 1.0),
                self.observation("C", 2.0),
            ],
            self.config(tolerance=1.1),
        )
        field = self.field(result)
        self.assertEqual(field.status, "ambiguous")
        self.assertEqual(field.consensus_sources, ())
        self.assertIn("multiple_equal_consensus_groups", field.reasons)

    def test_invalid_source_can_leave_two_source_consensus(self):
        result = assess_guidance_consensus(
            [
                self.observation("PRIMARY", 100.0),
                self.observation("BACKUP", 101.0),
                self.observation("GROUND", 100.0, valid=False),
            ],
            self.config(),
        )
        field = self.field(result)
        self.assertEqual(field.status, "consensus")
        self.assertEqual(field.consensus_sources, ("PRIMARY", "BACKUP"))
        self.assertIn("GROUND_invalid", field.reasons)

    def test_stale_pair_does_not_vote_together(self):
        result = assess_guidance_consensus(
            [
                self.observation("PRIMARY", 100.0, time_s=10.0),
                self.observation("BACKUP", 100.5, time_s=12.0),
                self.observation("GROUND", 100.2, time_s=10.0),
            ],
            self.config(freshness=0.5),
        )
        field = self.field(result)
        self.assertEqual(field.status, "consensus")
        self.assertEqual(field.consensus_sources, ("PRIMARY", "GROUND"))
        self.assertEqual(field.outside_consensus_sources, ("BACKUP",))

    def test_quorum_validation(self):
        with self.assertRaisesRegex(ValueError, "at least 2"):
            self.config(quorum=1).validated()
        with self.assertRaisesRegex(ValueError, "smaller"):
            assess_guidance_consensus(
                [self.observation("ONLY", 1.0)],
                self.config(quorum=2),
            )


if __name__ == "__main__":
    unittest.main()
