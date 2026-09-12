from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import project_controller_products  # noqa: E402
from apollo_mission_control.pc2_nominal import load_fixture, run_nominal  # noqa: E402
from apollo_mission_control.shutdown_rules import RuleState, evaluate_pc2_shutdown_rules  # noqa: E402


class PC2AttitudeIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")

    def test_missing_attitude_observations_remain_project_deferred(self):
        control = project_controller_products(run_nominal(self.fixture), self.fixture)["CONTROL"]
        self.assertIn("vehicle.attitude_error_xyz_deg", control.deferred_fields)
        self.assertIn("vehicle.body_rate_xyz_deg_s", control.deferred_fields)
        self.assertNotIn("vehicle.attitude_error_xyz_deg", control.products)
        self.assertNotIn("vehicle.body_rate_xyz_deg_s", control.products)

    def test_modeled_attitude_observations_become_control_products(self):
        state = run_nominal(self.fixture)
        state.attitude_error_xyz_deg = {"roll": 7.0, "pitch": 0.0, "yaw": 0.0}
        state.body_rate_xyz_deg_s = {"roll": 1.0, "pitch": 0.0, "yaw": 0.0}
        control = project_controller_products(state, self.fixture)["CONTROL"]

        self.assertEqual(control.products["vehicle.attitude_error_xyz_deg"].units, "deg")
        self.assertEqual(control.products["vehicle.body_rate_xyz_deg_s"].units, "deg/s")
        self.assertNotIn("vehicle.attitude_error_xyz_deg", control.deferred_fields)
        self.assertNotIn("vehicle.body_rate_xyz_deg_s", control.deferred_fields)

    def test_historical_nominal_validation_envelope_clears_integrated_rules(self):
        state = run_nominal(self.fixture)
        # Postflight CONTROL report gives about 7 deg maximum roll error and
        # rates below 1 deg/s. These are validation-envelope observations, not
        # a reconstructed time history.
        state.attitude_error_xyz_deg = {"roll": 7.0, "pitch": 0.0, "yaw": 0.0}
        state.body_rate_xyz_deg_s = {"roll": 1.0, "pitch": 0.0, "yaw": 0.0}
        evaluations = evaluate_pc2_shutdown_rules(
            project_controller_products(state, self.fixture), self.fixture
        )
        self.assertEqual(evaluations["attitude_error"].state, RuleState.CLEAR)
        self.assertEqual(evaluations["attitude_rate"].state, RuleState.CLEAR)

    def test_overlimit_error_with_unknown_startup_context_is_not_evaluable(self):
        state = run_nominal(self.fixture)
        state.attitude_error_xyz_deg = {"roll": 10.1, "pitch": 0.0, "yaw": 0.0}
        evaluations = evaluate_pc2_shutdown_rules(
            project_controller_products(state, self.fixture), self.fixture,
            startup_transient_exception_active=None,
        )
        self.assertEqual(evaluations["attitude_error"].state, RuleState.NOT_EVALUABLE)

    def test_overlimit_error_outside_explicit_startup_context_triggers(self):
        state = run_nominal(self.fixture)
        state.attitude_error_xyz_deg = {"roll": 10.1, "pitch": 0.0, "yaw": 0.0}
        evaluations = evaluate_pc2_shutdown_rules(
            project_controller_products(state, self.fixture), self.fixture,
            startup_transient_exception_active=False,
        )
        self.assertEqual(evaluations["attitude_error"].state, RuleState.TRIGGERED)
        self.assertFalse(state.shutdown_rule_triggers)

    def test_overlimit_error_in_explicit_startup_context_is_not_applicable(self):
        state = run_nominal(self.fixture)
        state.attitude_error_xyz_deg = {"roll": 10.1, "pitch": 0.0, "yaw": 0.0}
        evaluations = evaluate_pc2_shutdown_rules(
            project_controller_products(state, self.fixture), self.fixture,
            startup_transient_exception_active=True,
        )
        self.assertEqual(evaluations["attitude_error"].state, RuleState.NOT_APPLICABLE)

    def test_rate_limit_has_no_implemented_startup_exception(self):
        state = run_nominal(self.fixture)
        state.body_rate_xyz_deg_s = {"roll": 10.1, "pitch": 0.0, "yaw": 0.0}
        evaluations = evaluate_pc2_shutdown_rules(
            project_controller_products(state, self.fixture), self.fixture,
            startup_transient_exception_active=True,
        )
        self.assertEqual(evaluations["attitude_rate"].state, RuleState.TRIGGERED)
        self.assertFalse(state.shutdown_rule_triggers)


if __name__ == "__main__":
    unittest.main()
