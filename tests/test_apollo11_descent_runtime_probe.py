from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.apollo11_descent_runtime_probe import (  # noqa: E402
    run_apollo11_descent_runtime_reference_probe,
)


class Apollo11DescentRuntimeProbeTests(unittest.TestCase):
    def setUp(self):
        self.result = run_apollo11_descent_runtime_reference_probe()
        self.cases = {
            item["case_id"]: item["projection"]
            for item in self.result["cases"]
        }

    def test_probe_preserves_human_decision_boundary(self):
        undecided = self.cases["high_gate_station_go_flight_undecided"]
        relayed = self.cases["high_gate_flight_go_capcom_relay"]

        self.assertEqual(
            undecided["decision_gate"]["guidance_readiness"],
            "go",
        )
        self.assertEqual(
            undecided["decision_gate"]["control_readiness"],
            "go",
        )
        self.assertEqual(
            undecided["decision_gate"]["flight_decision"],
            "unknown",
        )
        self.assertEqual(
            undecided["decision_gate"]["capcom_relay"],
            "not_relayed",
        )

        self.assertEqual(relayed["decision_gate"]["flight_decision"], "go")
        self.assertEqual(relayed["decision_gate"]["capcom_relay"], "go_relayed")
        self.assertFalse(relayed["human_decision_generated"])

    def test_manual_control_changes_authority_without_removing_observations(self):
        manual = self.cases["manual_control_rule_authority"]
        gate = manual["decision_gate"]

        self.assertEqual(manual["phase"]["phase"], "landing")
        self.assertEqual(gate["control_mode"], "manual")
        self.assertFalse(
            gate["trajectory_guidance_abort_constraints_applicable"]
        )
        self.assertEqual(gate["landing_radar"]["antenna_position"], 2)
        self.assertTrue(gate["landing_radar"]["range_data_good"])

    def test_alarm_state_is_not_backfilled_into_controller_product(self):
        hidden = self.cases["alarm_not_backfilled_into_product"]
        explicit = self.cases["alarm_explicitly_supplied_to_product"]

        self.assertEqual(
            hidden["guidance_computer_state"]["active_alarm_code"],
            "1202",
        )
        hidden_products = {
            item["key"]: item
            for item in hidden["controller_products"]["products"]
        }
        explicit_products = {
            item["key"]: item
            for item in explicit["controller_products"]["products"]
        }

        self.assertFalse(hidden_products["program.alarm_latest"]["available"])
        self.assertIsNone(hidden_products["program.alarm_latest"]["value"])
        self.assertTrue(explicit_products["program.alarm_latest"]["available"])
        self.assertEqual(explicit_products["program.alarm_latest"]["value"], "1202")
        self.assertFalse(hidden["controller_products_derived_from_hidden_state"])

    def test_probe_declares_synthetic_event_scope_and_invariants(self):
        self.assertIn("not an Apollo 11 historical replay", self.result["scope"])
        self.assertEqual(
            self.result["invariants"],
            {
                "human_decisions_auto_generated": False,
                "hidden_state_auto_projected_to_controller_products": False,
                "probe_mutates_authoritative_live_session": False,
            },
        )


if __name__ == "__main__":
    unittest.main()
