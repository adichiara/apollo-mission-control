from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.powered_descent_phase import (  # noqa: E402
    PoweredDescentPhase,
    evaluate_powered_descent_phase,
)
from apollo_mission_control.powered_descent_profiles import (  # noqa: E402
    get_powered_descent_phase_profile,
)


class PoweredDescentPhaseTests(unittest.TestCase):
    def setUp(self):
        self.profile = get_powered_descent_phase_profile(
            "apollo11_g_powered_descent_phase_skeleton"
        )

    def test_profile_preserves_nominal_anchor_sequence(self):
        self.assertEqual(
            [(a.event_id, a.tfi_s, a.phase_after.value) for a in self.profile.anchors],
            [
                ("pdi", 0.0, "braking"),
                ("high_gate", 504.0, "approach"),
                ("low_gate", 608.0, "landing"),
                ("planned_touchdown", 718.0, "post_planned_touchdown"),
            ],
        )

    def test_negative_time_is_pre_pdi(self):
        result = evaluate_powered_descent_phase(-1.0, self.profile)
        self.assertEqual(result.phase, PoweredDescentPhase.PRE_PDI)
        self.assertIsNone(result.most_recent_anchor)
        self.assertEqual(result.next_anchor.event_id, "pdi")

    def test_pdi_enters_braking(self):
        result = evaluate_powered_descent_phase(0.0, self.profile)
        self.assertEqual(result.phase, PoweredDescentPhase.BRAKING)
        self.assertEqual(result.most_recent_anchor.event_id, "pdi")
        self.assertEqual(result.next_anchor.event_id, "high_gate")

    def test_high_gate_boundary_enters_approach(self):
        before = evaluate_powered_descent_phase(503.999, self.profile)
        at = evaluate_powered_descent_phase(504.0, self.profile)
        self.assertEqual(before.phase, PoweredDescentPhase.BRAKING)
        self.assertEqual(at.phase, PoweredDescentPhase.APPROACH)
        self.assertEqual(at.most_recent_anchor.nominal_altitude_ft, 7600.0)

    def test_low_gate_boundary_enters_landing(self):
        result = evaluate_powered_descent_phase(608.0, self.profile)
        self.assertEqual(result.phase, PoweredDescentPhase.LANDING)
        self.assertEqual(result.most_recent_anchor.nominal_altitude_ft, 500.0)

    def test_planned_touchdown_does_not_erase_flown_duration_observation(self):
        result = evaluate_powered_descent_phase(730.0, self.profile)
        self.assertEqual(
            result.phase,
            PoweredDescentPhase.POST_PLANNED_TOUCHDOWN,
        )
        observations = {
            item.key: item for item in result.flown_observations
        }
        self.assertEqual(
            observations["powered_descent_duration"].value,
            756.3,
        )
        self.assertFalse(result.to_dict()["flown_observations_drive_phase"])

    def test_flown_throttle_observations_do_not_create_phase_boundaries(self):
        result = evaluate_powered_descent_phase(26.0, self.profile)
        self.assertEqual(result.phase, PoweredDescentPhase.BRAKING)
        self.assertEqual(result.most_recent_anchor.event_id, "pdi")
        self.assertEqual(result.next_anchor.event_id, "high_gate")

    def test_profile_carries_untimed_nominal_events_without_assigning_times(self):
        self.assertIn("throttle recovery", self.profile.untimed_nominal_events)
        result = evaluate_powered_descent_phase(300.0, self.profile).to_dict()
        self.assertIn("throttle recovery", result["untimed_nominal_events"])


if __name__ == "__main__":
    unittest.main()
