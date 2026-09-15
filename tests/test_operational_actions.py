from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import project_controller_products  # noqa: E402
from apollo_mission_control.operational_actions import OperationalAction, apply_operational_action  # noqa: E402
from apollo_mission_control.pc2_nominal import hms_to_seconds, load_fixture  # noqa: E402
from apollo_mission_control.scenario_injection import (  # noqa: E402
    EvidenceClass,
    StateInjection,
    apply_state_injection,
    run_with_injections,
)
from apollo_mission_control.shutdown_rules import RuleState, evaluate_pc2_shutdown_rules  # noqa: E402


class OperationalActionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")

    def burn_state(self):
        return run_with_injections(
            self.fixture, [], stop_get_s=hms_to_seconds("79:29:00")
        )

    def inject_warning(self, state, get_hms):
        apply_state_injection(
            state,
            StateInjection(
                injection_id=f"test-warning-{get_hms}",
                get_s=hms_to_seconds(get_hms),
                target="crew_inverter_warning_report",
                value=True,
                evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                provenance="Synthetic crew report for documented inverter rule ordering; direct caution telemetry is not assumed.",
            ),
        )

    def test_inverter_warning_before_switch_is_not_positive_rule(self):
        state = self.burn_state()
        self.inject_warning(state, "79:29:00")
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(state, self.fixture), self.fixture)
        self.assertEqual(evaluations["persistent_inverter_warning"].state, RuleState.NOT_EVALUABLE)

    def test_inverter_warning_requires_distinct_post_switch_observation(self):
        state = self.burn_state()
        self.inject_warning(state, "79:29:00")
        action = OperationalAction(
            action_id="test-switch-inverter",
            get_s=hms_to_seconds("79:29:02"),
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
        self.assertEqual(evaluations["persistent_inverter_warning"].state, RuleState.NOT_EVALUABLE)

        self.inject_warning(state, "79:29:04")
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
        self.assertIsNone(state.crew_inverter_warning_report)
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(state, self.fixture), self.fixture)
        self.assertEqual(
            evaluations["persistent_inverter_warning"].state,
            RuleState.NOT_EVALUABLE,
        )

    def test_hidden_onboard_warning_is_not_ground_rule_evidence(self):
        state = self.burn_state()
        apply_state_injection(
            state,
            StateInjection(
                injection_id="hidden-onboard-warning",
                get_s=hms_to_seconds("79:29:00"),
                target="lm_inverter_warning",
                value=True,
                evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                provenance=(
                    "Synthetic onboard caution state. Reviewed schematics do not "
                    "establish direct ground telemetry of this derived caution."
                ),
            ),
        )
        projections = project_controller_products(state, self.fixture)
        self.assertNotIn("lm.inverter_warning", projections["TELMU"].products)
        self.assertNotIn("crew.inverter_warning_report", projections["CAPCOM"].products)
        evaluations = evaluate_pc2_shutdown_rules(projections, self.fixture)
        self.assertEqual(
            evaluations["persistent_inverter_warning"].state,
            RuleState.NOT_EVALUABLE,
        )


if __name__ == "__main__":
    unittest.main()
