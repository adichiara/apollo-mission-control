from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import project_controller_products  # noqa: E402
from apollo_mission_control.pc2_nominal import hms_to_seconds, load_fixture  # noqa: E402
from apollo_mission_control.scenario_injection import (  # noqa: E402
    EvidenceClass,
    StateInjection,
    apply_state_injection,
    run_with_injections,
)
from apollo_mission_control.shutdown_rules import (  # noqa: E402
    RuleState,
    evaluate_pc2_shutdown_rules,
)


class ScenarioInjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(
            ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json"
        )

    def test_timed_chamber_pressure_injection_reaches_control_rule_path(self):
        injection = StateInjection(
            injection_id="test-low-chamber-pressure",
            get_s=hms_to_seconds("79:29:00"),
            target="dps_chamber_pressure_psi",
            value=80.0,
            evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
            provenance=(
                "Synthetic rule-boundary test value below the documented "
                "85-psi PC+2 ground criterion; not a historical Apollo 13 failure."
            ),
        )
        state = run_with_injections(
            self.fixture,
            [injection],
            stop_get_s=hms_to_seconds("79:29:00"),
        )
        products = project_controller_products(state, self.fixture)
        evaluations = evaluate_pc2_shutdown_rules(products, self.fixture)

        self.assertEqual(
            products["CONTROL"].products["dps.chamber_pressure_psi"].value,
            80.0,
        )
        self.assertEqual(
            evaluations["ground_chamber_pressure"].state,
            RuleState.TRIGGERED,
        )
        self.assertEqual(state.shutdown_rule_triggers, [])
        self.assertTrue(state.engine_running)

    def test_delta_p_above_25_triggers_ground_rule_without_commanding_cutoff(self):
        injection = StateInjection(
            injection_id="test-high-fuel-oxidizer-delta-p",
            get_s=hms_to_seconds("79:29:00"),
            target="dps_fuel_oxidizer_delta_p_psi",
            value=26.0,
            evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
            provenance=(
                "Synthetic ground-product boundary test above the documented "
                "25-psi PC+2 criterion; not historical telemetry."
            ),
        )
        state = run_with_injections(
            self.fixture,
            [injection],
            stop_get_s=hms_to_seconds("79:29:00"),
        )
        products = project_controller_products(state, self.fixture)
        evaluations = evaluate_pc2_shutdown_rules(products, self.fixture)

        self.assertEqual(
            products["CONTROL"].products["dps.fuel_oxidizer_delta_p_psi"].value,
            26.0,
        )
        self.assertEqual(
            evaluations["fuel_oxidizer_delta_p"].state,
            RuleState.TRIGGERED,
        )
        self.assertTrue(state.engine_running)
        self.assertFalse(state.cutoff_complete)
        self.assertEqual(state.shutdown_rule_triggers, [])

    def test_delta_p_exactly_25_is_clear_because_rule_is_greater_than(self):
        injection = StateInjection(
            injection_id="test-delta-p-threshold",
            get_s=hms_to_seconds("79:29:00"),
            target="dps_fuel_oxidizer_delta_p_psi",
            value=25.0,
            evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
            provenance="Synthetic exact-boundary implementation test.",
        )
        state = run_with_injections(
            self.fixture,
            [injection],
            stop_get_s=hms_to_seconds("79:29:00"),
        )
        products = project_controller_products(state, self.fixture)
        evaluations = evaluate_pc2_shutdown_rules(products, self.fixture)
        self.assertEqual(evaluations["fuel_oxidizer_delta_p"].state, RuleState.CLEAR)

    def test_injection_does_not_script_cutoff_or_abort(self):
        injection = StateInjection(
            injection_id="test-low-chamber-pressure",
            get_s=hms_to_seconds("79:29:00"),
            target="dps_chamber_pressure_psi",
            value=80.0,
            evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
            provenance="Synthetic implementation test.",
        )
        state = run_with_injections(
            self.fixture,
            [injection],
            stop_get_s=hms_to_seconds("79:29:00"),
        )
        self.assertTrue(state.engine_running)
        self.assertFalse(state.cutoff_complete)
        self.assertEqual(state.shutdown_rule_triggers, [])

    def test_unsupported_target_is_rejected(self):
        state = run_with_injections(self.fixture, [], stop_get_s=hms_to_seconds("79:29:00"))
        injection = StateInjection(
            injection_id="invalid-target",
            get_s=state.get_s,
            target="burn_abort",
            value=True,
            evidence_class=EvidenceClass.PROJECT_HYPOTHETICAL,
            provenance="Negative interface test.",
        )
        with self.assertRaises(ValueError):
            apply_state_injection(state, injection)

    def test_injection_after_stop_time_is_not_applied(self):
        injection = StateInjection(
            injection_id="future-low-pressure",
            get_s=hms_to_seconds("79:30:00"),
            target="dps_chamber_pressure_psi",
            value=80.0,
            evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
            provenance="Synthetic implementation test.",
        )
        state = run_with_injections(
            self.fixture,
            [injection],
            stop_get_s=hms_to_seconds("79:29:00"),
        )
        self.assertIsNone(state.dps_chamber_pressure_psi)


if __name__ == "__main__":
    unittest.main()
