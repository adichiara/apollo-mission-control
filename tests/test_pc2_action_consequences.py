from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_action_consequence_probe import (  # noqa: E402
    run_pc2_action_consequence_matrix,
)
from apollo_mission_control.pc2_nominal import load_fixture  # noqa: E402


class PC2ActionConsequenceProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(
            ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json"
        )

    def setUp(self):
        result = run_pc2_action_consequence_matrix(self.fixture)
        self.cases = {item["action_class"]: item for item in result["cases"]}

    def test_correct_action_preserves_nominal_chain(self):
        case = self.cases["correct"]
        self.assertTrue(case["action_accepted"])
        self.assertTrue(case["flight_go"])
        self.assertTrue(case["p40_active"])
        self.assertTrue(case["engine_running"])
        self.assertNotIn("p40_active_final_preburn", case["missed_events"])

    def test_late_action_is_accepted_but_does_not_replay_missed_event(self):
        case = self.cases["late"]
        self.assertTrue(case["action_accepted"])
        self.assertTrue(case["flight_go"])
        self.assertFalse(case["p40_active"])
        self.assertFalse(case["engine_running"])
        self.assertIn("p40_active_final_preburn", case["missed_events"])

    def test_omitted_action_causes_downstream_nominal_events_to_be_missed(self):
        case = self.cases["omitted"]
        self.assertIsNone(case["action_accepted"])
        self.assertFalse(case["flight_go"])
        self.assertFalse(case["engine_running"])
        self.assertIn("p40_active_final_preburn", case["missed_events"])
        self.assertIn("dps_ignition", case["missed_events"])
        self.assertIn("guided_cutoff", case["missed_events"])

    def test_wrong_actor_is_rejected_without_pausing_get(self):
        case = self.cases["wrong"]
        self.assertFalse(case["action_accepted"])
        self.assertIsNotNone(case["rejection_reason"])
        self.assertFalse(case["flight_go"])
        self.assertFalse(case["p40_active"])
        self.assertEqual(case["session_status"], "running")
        self.assertIn("p40_active_final_preburn", case["missed_events"])

    def test_late_semantics_do_not_claim_historical_grace_period(self):
        result = run_pc2_action_consequence_matrix(self.fixture)
        self.assertIn("no historical grace interval", result["late_semantics"])


if __name__ == "__main__":
    unittest.main()
