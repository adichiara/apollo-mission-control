from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_inverter_consequence_probe import (  # noqa: E402
    run_pc2_inverter_consequence_matrix,
)
from apollo_mission_control.pc2_nominal import load_fixture  # noqa: E402


class PC2InverterConsequenceProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(
            ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json"
        )

    def setUp(self):
        result = run_pc2_inverter_consequence_matrix(self.fixture)
        self.result = result
        self.cases = {item["action_class"]: item for item in result["cases"]}

    def test_correct_transfer_requires_fresh_post_transfer_warning(self):
        case = self.cases["correct"]
        self.assertEqual(case["pre_observation_rule_state"], "not_evaluable")
        self.assertEqual(case["final_rule_state"], "triggered")
        self.assertTrue(case["transfer_performed"])
        self.assertTrue(case["completion_reported"])
        self.assertTrue(case["engine_running"])

    def test_omitted_transfer_cannot_trigger_rule(self):
        case = self.cases["omitted"]
        self.assertFalse(case["transfer_performed"])
        self.assertEqual(case["final_rule_state"], "not_evaluable")
        self.assertTrue(case["engine_running"])

    def test_wrong_order_action_is_rejected_before_receipt(self):
        case = self.cases["wrong_order"]
        self.assertTrue(case["action_rejected"])
        self.assertFalse(case["receipt_recorded"])
        self.assertFalse(case["transfer_performed"])
        self.assertIn("receipt", case["rejection_reason"].lower())
        self.assertEqual(case["final_rule_state"], "not_evaluable")

    def test_fresh_clear_observation_clears_rule(self):
        case = self.cases["cleared"]
        self.assertTrue(case["transfer_performed"])
        self.assertFalse(case["post_observation_value"])
        self.assertEqual(case["final_rule_state"], "clear")
        self.assertTrue(case["engine_running"])

    def test_ordering_increment_is_not_historical_tolerance(self):
        self.assertEqual(self.result["ordering_increment_s"], 0.1)
        self.assertIn(
            "no historical dwell",
            self.result["ordering_increment_meaning"],
        )


if __name__ == "__main__":
    unittest.main()
