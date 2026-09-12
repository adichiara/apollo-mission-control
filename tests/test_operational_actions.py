from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import project_controller_products  # noqa: E402
from apollo_mission_control.operational_actions import OperationalAction, apply_operational_action  # noqa: E402
from apollo_mission_control.pc2_nominal import hms_to_seconds, load_fixture  # noqa: E402
from apollo_mission_control.scenario_injection import run_with_injections  # noqa: E402
from apollo_mission_control.shutdown_rules import RuleState, evaluate_pc2_shutdown_rules  # noqa: E402


class OperationalActionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")

    def burn_state(self):
        return run_with_injections(
            self.fixture, [], stop_get_s=hms_to_seconds("79:29:00")
        )

    def test_inverter_warning_before_switch_is_not_positive_rule(self):
        state = self.burn_state()
        state.lm_inverter_warning = True
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(state, self.fixture), self.fixture)
        self.assertEqual(evaluations["persistent_inverter_warning"].state, RuleState.NOT_EVALUABLE)

    def test_inverter_warning_remaining_after_switch_triggers_rule(self):
        state = self.burn_state()
        state.lm_inverter_warning = True
        action = OperationalAction(
            action_id="test-switch-inverter",
            get_s=hms_to_seconds("79:29:00"),
            actor="CREW",
            action="switch_lm_inverter",
            parameters={},
            provenance=(
                "Source-bounded procedural test of the Apollo 13 PC+2 criterion; "
                "exact inverter identity and switch chronology are not asserted."
            ),
        )
        apply_operational_action(state, action)
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(state, self.fixture), self.fixture)
        self.assertEqual(evaluations["persistent_inverter_warning"].state, RuleState.TRIGGERED)
        self.assertTrue(state.engine_running)
        self.assertFalse(state.cutoff_complete)
        self.assertEqual(state.shutdown_rule_triggers, [])

    def test_switch_action_does_not_create_warning(self):
        state = self.burn_state()
        action = OperationalAction(
            action_id="test-switch-no-warning",
            get_s=hms_to_seconds("79:29:00"),
            actor="CREW",
            action="switch_lm_inverter",
            parameters={},
            provenance="Synthetic implementation test.",
        )
        apply_operational_action(state, action)
        self.assertFalse(state.lm_inverter_warning)
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(state, self.fixture), self.fixture)
        self.assertEqual(evaluations["persistent_inverter_warning"].state, RuleState.CLEAR)


if __name__ == "__main__":
    unittest.main()
