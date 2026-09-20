import unittest

from apollo_mission_control.landing_radar_data_good import (
    LandingRadarDataGoodReplayInput,
    LandingRadarDataGoodTransition,
    replay_landing_radar_data_good,
)


class LandingRadarDataGoodReplayTests(unittest.TestCase):
    def transitions(self):
        return (
            LandingRadarDataGoodTransition(369851.0, False, "not good 102:44:11", 1.0),
            LandingRadarDataGoodTransition(369861.0, True, "good 102:44:21", 1.0),
            LandingRadarDataGoodTransition(369899.0, False, "not good 102:44:59", 1.0),
            LandingRadarDataGoodTransition(369903.0, True, "good 102:45:03", 1.0),
        )

    def replay(self, query_time_s):
        return replay_landing_radar_data_good(
            LandingRadarDataGoodReplayInput(
                initial_time_s=369850.0,
                initial_data_good=True,
                initial_data_good_since_s=369840.0,
                query_time_s=query_time_s,
                min_data_good_duration_s=4.0,
                transitions=self.transitions(),
            )
        )

    def test_first_loss_and_reacquisition_are_distinct_from_requalification(self):
        before = self.replay(369850.5)
        self.assertTrue(before.data_good)
        self.assertTrue(before.data_good_qualified)

        lost = self.replay(369851.0)
        self.assertFalse(lost.data_good)
        self.assertFalse(lost.data_good_qualified)
        self.assertIsNone(lost.data_good_since_s)

        reacquired = self.replay(369861.0)
        self.assertTrue(reacquired.data_good)
        self.assertFalse(reacquired.data_good_qualified)
        self.assertEqual(reacquired.data_good_duration_s, 0.0)

        not_yet = self.replay(369864.999)
        self.assertFalse(not_yet.data_good_qualified)

        qualified = self.replay(369865.0)
        self.assertTrue(qualified.data_good_qualified)
        self.assertEqual(qualified.data_good_duration_s, 4.0)

    def test_second_loss_replays_four_second_interval_and_requalification(self):
        lost = self.replay(369899.0)
        self.assertFalse(lost.data_good)

        reacquired = self.replay(369903.0)
        self.assertTrue(reacquired.data_good)
        self.assertFalse(reacquired.data_good_qualified)

        qualified = self.replay(369907.0)
        self.assertTrue(qualified.data_good_qualified)

    def test_reports_next_transition_without_inventing_intermediate_events(self):
        result = self.replay(369870.0)
        self.assertEqual(len(result.applied_transitions), 2)
        self.assertIsNotNone(result.next_transition)
        self.assertEqual(result.next_transition.time_s, 369899.0)

    def test_initial_state_must_be_explicit_and_consistent(self):
        with self.assertRaisesRegex(ValueError, "must be null"):
            replay_landing_radar_data_good(
                LandingRadarDataGoodReplayInput(
                    initial_time_s=0.0,
                    initial_data_good=False,
                    initial_data_good_since_s=-1.0,
                    query_time_s=1.0,
                    min_data_good_duration_s=4.0,
                    transitions=(),
                )
            )

    def test_transitions_must_be_ascending_and_unique(self):
        with self.assertRaisesRegex(ValueError, "unique ascending"):
            replay_landing_radar_data_good(
                LandingRadarDataGoodReplayInput(
                    initial_time_s=0.0,
                    initial_data_good=True,
                    initial_data_good_since_s=0.0,
                    query_time_s=10.0,
                    min_data_good_duration_s=4.0,
                    transitions=(
                        LandingRadarDataGoodTransition(5.0, False, "a"),
                        LandingRadarDataGoodTransition(4.0, True, "b"),
                    ),
                )
            )


if __name__ == "__main__":
    unittest.main()
