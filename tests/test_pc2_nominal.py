from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import project_controller_products  # noqa: E402
from apollo_mission_control.pc2_nominal import (  # noqa: E402
    PC2State, Validity, apply_event, build_events, hms_to_seconds,
    load_fixture, run_nominal, validate_nominal,
)
from apollo_mission_control.shutdown_rules import (  # noqa: E402
    RuleState, evaluate_pc2_shutdown_rules, triggered_rules,
)


class PC2NominalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")

    def test_event_order(self):
        events = build_events(self.fixture)
        self.assertEqual([e.get_s for e in events], sorted(e.get_s for e in events))

    def test_historical_tig_and_cutoff(self):
        events = {e.name: e.get_s for e in build_events(self.fixture)}
        self.assertAlmostEqual(events["dps_ignition"], 286058.30)
        self.assertAlmostEqual(events["guided_cutoff"], 286322.12)

    def test_ullage_and_commanded_throttle_profile(self):
        events = {e.name: e.get_s for e in build_events(self.fixture)}
        tig = self.fixture["pc2_target"]["tig_get_s"]
        self.assertAlmostEqual(events["manual_two_jet_ullage_begins"], tig - 10.0)
        self.assertAlmostEqual(events["throttle_command_40_percent"], tig + 5.0)
        self.assertAlmostEqual(events["throttle_command_maximum"], tig + 26.0)

    def test_crew_reports_remain_separate_from_commands(self):
        state = run_nominal(self.fixture)
        reports = [(r.get_s, r.report) for r in state.crew_reports]
        self.assertEqual(reports, [
            (hms_to_seconds("79:27:51"), "40_percent"),
            (hms_to_seconds("79:28:09"), "100_percent"),
        ])

    def test_nominal_run_reaches_powerdown(self):
        state = run_nominal(self.fixture)
        self.assertTrue(state.cutoff_complete)
        self.assertTrue(state.residual_review_complete)
        self.assertTrue(state.powerdown_started)
        self.assertFalse(state.shutdown_rule_triggers)

    def test_nominal_validation_contract(self):
        self.assertEqual(validate_nominal(self.fixture, run_nominal(self.fixture)), [])

    def test_projection_has_required_station_boundaries(self):
        projections = project_controller_products(run_nominal(self.fixture), self.fixture)
        self.assertEqual(set(projections), {"CONTROL", "GUIDO", "FIDO_RETRO", "TELMU", "INCO", "FLIGHT", "CAPCOM"})
        self.assertNotIn("dps.engine_running", projections["FLIGHT"].products)
        self.assertIn("dps.engine_running", projections["CONTROL"].products)

    def test_projection_metadata_is_explicit(self):
        state = run_nominal(self.fixture)
        product = project_controller_products(state, self.fixture)["CONTROL"].products["dps.engine_running"]
        self.assertEqual(product.validity, Validity.VALID)
        self.assertTrue(product.source_layer)
        self.assertTrue(product.provenance)
        self.assertEqual(product.sample_time_get, state.get_s)

    def test_research_gaps_are_not_telemetry_failures(self):
        projections = project_controller_products(run_nominal(self.fixture), self.fixture)
        self.assertIn("dps.chamber_pressure_psi", projections["CONTROL"].deferred_fields)
        self.assertNotIn("dps.chamber_pressure_psi", projections["CONTROL"].products)

    def test_modeled_chamber_pressure_becomes_control_product(self):
        state = run_nominal(self.fixture)
        state.dps_chamber_pressure_psi = 100.0
        control = project_controller_products(state, self.fixture)["CONTROL"]
        self.assertNotIn("dps.chamber_pressure_psi", control.deferred_fields)
        product = control.products["dps.chamber_pressure_psi"]
        self.assertEqual(product.value, 100.0)
        self.assertEqual(product.units, "psi")
        self.assertEqual(product.validity, Validity.VALID)
        self.assertIn("GQ6510P", product.provenance)

    def test_postburn_residual_is_unavailable_before_review(self):
        state = PC2State(get_s=self.fixture["start_get_s"])
        for event in build_events(self.fixture):
            if event.name == "postburn_residual_review":
                break
            apply_event(state, event, self.fixture)
        residual = project_controller_products(state, self.fixture)["GUIDO"].products["pg_ns.postburn_residual"]
        self.assertEqual(residual.validity, Validity.UNAVAILABLE)
        self.assertIsNone(residual.value)

    def test_postburn_residual_becomes_available_after_review(self):
        residual = project_controller_products(run_nominal(self.fixture), self.fixture)["GUIDO"].products["pg_ns.postburn_residual"]
        self.assertEqual(residual.validity, Validity.VALID)
        self.assertEqual(residual.value, {"x": 1.0, "y": 0.3, "z": 0.0})

    def test_nominal_rule_audit_has_no_triggered_rules(self):
        products = project_controller_products(run_nominal(self.fixture), self.fixture)
        evaluations = evaluate_pc2_shutdown_rules(products, self.fixture)
        self.assertEqual(triggered_rules(evaluations), [])
        self.assertEqual(evaluations["iss_warning_plus_program_alarm"].state, RuleState.CLEAR)

    def test_unmodeled_numeric_rules_are_not_falsely_cleared(self):
        products = project_controller_products(run_nominal(self.fixture), self.fixture)
        evaluations = evaluate_pc2_shutdown_rules(products, self.fixture)
        for rule_id in ("ground_chamber_pressure", "crew_thrust_monitor", "ground_inlet_pressure", "crew_inlet_pressure", "fuel_oxidizer_delta_p", "attitude_error", "attitude_rate"):
            self.assertEqual(evaluations[rule_id].state, RuleState.NOT_EVALUABLE)

    def test_modeled_safe_chamber_pressure_clears_ground_rule(self):
        state = run_nominal(self.fixture)
        state.dps_chamber_pressure_psi = 100.0
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(state, self.fixture), self.fixture)
        self.assertEqual(evaluations["ground_chamber_pressure"].state, RuleState.CLEAR)

    def test_source_backed_low_chamber_pressure_rule_path(self):
        state = run_nominal(self.fixture)
        # Synthetic test value below the documented 85-psi ground criterion;
        # not a claim about a historical Apollo 13 failure.
        state.dps_chamber_pressure_psi = 80.0
        products = project_controller_products(state, self.fixture)
        evaluations = evaluate_pc2_shutdown_rules(products, self.fixture)
        self.assertEqual(evaluations["ground_chamber_pressure"].state, RuleState.TRIGGERED)
        self.assertIn("ground_chamber_pressure", [r.rule_id for r in triggered_rules(evaluations)])
        self.assertFalse(state.shutdown_rule_triggers)

    def test_modeled_gimbal_warning_can_trigger_rule_without_commanding_abort(self):
        fixture = deepcopy(self.fixture)
        fixture["dps"]["engine_gimbal_warning"] = True
        state = run_nominal(fixture)
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(state, fixture), fixture)
        self.assertEqual(evaluations["engine_gimbal_warning"].state, RuleState.TRIGGERED)
        self.assertFalse(state.shutdown_rule_triggers)

    def test_program_alarm_alone_does_not_trigger_conjunctive_iss_rule(self):
        fixture = deepcopy(self.fixture)
        fixture["pgns"]["program_alarm"] = "TEST_PRESENT"
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(run_nominal(fixture), fixture), fixture)
        self.assertEqual(evaluations["iss_warning_plus_program_alarm"].state, RuleState.CLEAR)

    def test_iss_warning_alone_does_not_trigger_conjunctive_rule(self):
        fixture = deepcopy(self.fixture)
        fixture["pgns"]["iss_warning"] = True
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(run_nominal(fixture), fixture), fixture)
        self.assertEqual(evaluations["iss_warning_plus_program_alarm"].state, RuleState.CLEAR)

    def test_source_backed_iss_warning_plus_program_alarm_rule_path(self):
        fixture = deepcopy(self.fixture)
        fixture["pgns"]["iss_warning"] = True
        fixture["pgns"]["program_alarm"] = "TEST_PRESENT"
        state = run_nominal(fixture)
        products = project_controller_products(state, fixture)
        self.assertTrue(products["GUIDO"].products["pg_ns.iss.warning"].value)
        evaluations = evaluate_pc2_shutdown_rules(products, fixture)
        self.assertEqual(evaluations["iss_warning_plus_program_alarm"].state, RuleState.TRIGGERED)
        self.assertIn("iss_warning_plus_program_alarm", [r.rule_id for r in triggered_rules(evaluations)])
        self.assertFalse(state.shutdown_rule_triggers)

    def test_inverter_warning_positive_case_requires_switch_attempt_state(self):
        fixture = deepcopy(self.fixture)
        fixture["lm_power"]["inverter_warning"] = True
        evaluations = evaluate_pc2_shutdown_rules(project_controller_products(run_nominal(fixture), fixture), fixture)
        self.assertEqual(evaluations["persistent_inverter_warning"].state, RuleState.NOT_EVALUABLE)


if __name__ == "__main__":
    unittest.main()
