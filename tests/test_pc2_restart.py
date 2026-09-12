from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.operational_actions import (  # noqa: E402
    OperationalAction,
    apply_operational_action,
)
from apollo_mission_control.pc2_nominal import PC2State  # noqa: E402
from apollo_mission_control.procedural_exchange import (  # noqa: E402
    ProcedureExchangeLog,
    record_pc2_restart_instruction,
)
from apollo_mission_control.restart_logic import (  # noqa: E402
    RestartDisposition,
    evaluate_premature_shutdown_restart,
)
from apollo_mission_control.shutdown_rules import RuleEvaluation, RuleState  # noqa: E402


class PC2RestartTests(unittest.TestCase):
    def test_positive_non_rule_cause_is_restart_eligible(self):
        evaluations = {
            "engine_gimbal_warning": RuleEvaluation(
                "engine_gimbal_warning", RuleState.CLEAR, "CONTROL", "engine gimbal warning/light"
            ),
            "lgc_warning": RuleEvaluation(
                "lgc_warning", RuleState.CLEAR, "GUIDO", "LM guidance computer warning"
            ),
        }
        result = evaluate_premature_shutdown_restart(
            evaluations,
            early_engine_stop_observed=True,
            shutdown_cause_known_non_rule=True,
            noun97_flashing=True,
        )
        self.assertEqual(result.disposition, RestartDisposition.RESTART_ELIGIBLE)
        self.assertEqual(result.triggered_rule_ids, ())

    def test_absence_of_trigger_is_not_enough_when_cause_is_unknown(self):
        evaluations = {
            "crew_thrust_monitor": RuleEvaluation(
                "crew_thrust_monitor", RuleState.NOT_EVALUABLE, "CREW/CAPCOM", "onboard thrust monitor"
            )
        }
        result = evaluate_premature_shutdown_restart(
            evaluations,
            early_engine_stop_observed=True,
            noun97_flashing=True,
        )
        self.assertEqual(result.disposition, RestartDisposition.INSUFFICIENT_CONTEXT)
        self.assertEqual(result.unresolved_rule_ids, ("crew_thrust_monitor",))

    def test_rule_caused_shutdown_is_not_restart_eligible(self):
        evaluations = {
            "lgc_warning": RuleEvaluation(
                "lgc_warning", RuleState.TRIGGERED, "GUIDO", "LM guidance computer warning"
            )
        }
        result = evaluate_premature_shutdown_restart(
            evaluations,
            early_engine_stop_observed=True,
            shutdown_cause_known_non_rule=True,
            noun97_flashing=True,
        )
        self.assertEqual(result.disposition, RestartDisposition.DO_NOT_RESTART_RULE_SHUTDOWN)
        self.assertEqual(result.triggered_rule_ids, ("lgc_warning",))

    def test_restart_instruction_preserves_historical_sequence_without_outcome(self):
        log = ProcedureExchangeLog()
        record_pc2_restart_instruction(
            log,
            event_id="restart-readup",
            get_s=100.0,
            provenance="Apollo 13 PC+2 contemporaneous CAPCOM read-up",
        )
        self.assertEqual(
            log.events[0].parameters["sequence"],
            [
                "proceed_noun_97",
                "manual_ullage",
                "engine_start_push",
                "descent_engine_command_override_on",
            ],
        )

    def test_restart_actions_do_not_force_engine_running(self):
        state = PC2State(get_s=100.0, engine_running=False)
        actions = [
            OperationalAction("u", 101.0, "CREW", "restart_manual_ullage", {}, "PC+2 restart read-up"),
            OperationalAction("s", 102.0, "CREW", "press_engine_start", {}, "PC+2 restart read-up"),
            OperationalAction("o", 103.0, "CREW", "descent_engine_command_override_on", {}, "PC+2 restart read-up"),
        ]
        for action in actions:
            apply_operational_action(state, action)

        self.assertTrue(state.restart_manual_ullage_attempted)
        self.assertTrue(state.engine_start_push_attempted)
        self.assertTrue(state.descent_engine_command_override_on)
        self.assertFalse(state.engine_running)


if __name__ == "__main__":
    unittest.main()
