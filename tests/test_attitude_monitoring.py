import unittest

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.attitude_monitoring import (  # noqa: E402
    AttitudeRuleState,
    evaluate_attitude_error,
    evaluate_attitude_rate,
)


class PC2AttitudeMonitoringTests(unittest.TestCase):
    def test_missing_error_observation_is_not_evaluable(self):
        self.assertEqual(
            evaluate_attitude_error(None).state,
            AttitudeRuleState.NOT_EVALUABLE,
        )

    def test_historical_nominal_error_envelope_is_clear(self):
        # Apollo 13 CONTROL postflight account reports a maximum observed
        # PC+2 error of about 7 deg in roll. This is a validation-bound test,
        # not a reconstructed full time history.
        result = evaluate_attitude_error({"roll": 7.0, "pitch": 0.0, "yaw": 0.0})
        self.assertEqual(result.state, AttitudeRuleState.CLEAR)
        self.assertEqual(result.max_abs_value, 7.0)

    def test_historical_nominal_rate_envelope_is_clear(self):
        # CONTROL reports rates never exceeded 1 deg/s during PC+2.
        result = evaluate_attitude_rate({"roll": 1.0, "pitch": 0.0, "yaw": 0.0})
        self.assertEqual(result.state, AttitudeRuleState.CLEAR)
        self.assertEqual(result.max_abs_value, 1.0)

    def test_synthetic_overlimit_error_outside_startup_triggers(self):
        result = evaluate_attitude_error(
            {"roll": 10.1, "pitch": 0.0, "yaw": 0.0},
            startup_transient_exception_active=False,
        )
        self.assertEqual(result.state, AttitudeRuleState.TRIGGERED)

    def test_synthetic_overlimit_error_during_explicit_startup_exception_is_not_applicable(self):
        result = evaluate_attitude_error(
            {"roll": 10.1, "pitch": 0.0, "yaw": 0.0},
            startup_transient_exception_active=True,
        )
        self.assertEqual(result.state, AttitudeRuleState.NOT_APPLICABLE)

    def test_unknown_startup_context_does_not_falsely_clear_overlimit_error(self):
        result = evaluate_attitude_error(
            {"roll": 10.1, "pitch": 0.0, "yaw": 0.0},
            startup_transient_exception_active=None,
        )
        self.assertEqual(result.state, AttitudeRuleState.NOT_EVALUABLE)

    def test_synthetic_overlimit_rate_triggers_without_startup_exception(self):
        result = evaluate_attitude_rate({"roll": 10.1, "pitch": 0.0, "yaw": 0.0})
        self.assertEqual(result.state, AttitudeRuleState.TRIGGERED)


if __name__ == "__main__":
    unittest.main()
