from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.guidance_computer_model import (  # noqa: E402
    GuidanceComputerConfig,
    GuidanceComputerState,
    ProgramAlarmEvent,
    ProgramAlarmRule,
    apply_program_alarm,
    clear_program_alarm,
)


class GuidanceComputerModelTests(unittest.TestCase):
    def config(self):
        return GuidanceComputerConfig(
            alarm_rules={
                "A1": ProgramAlarmRule(
                    code="A1",
                    meaning="synthetic restart alarm",
                    software_restart=True,
                ),
                "A2": ProgramAlarmRule(
                    code="A2",
                    meaning="synthetic non-restart alarm",
                    software_restart=False,
                ),
            },
            restart_protected_programs=("P_ALPHA",),
            applicability="synthetic guidance model test",
            provenance=("synthetic test inputs",),
        )

    def test_restart_protected_program_resumes_without_abort_decision(self):
        result = apply_program_alarm(
            GuidanceComputerState(time_s=10.0, active_program="P_ALPHA"),
            ProgramAlarmEvent(time_s=11.0, code="A1"),
            self.config(),
        )

        self.assertTrue(result.restart_occurred)
        self.assertTrue(result.restart_protected_recovery)
        self.assertEqual(result.state.active_program, "P_ALPHA")
        self.assertEqual(result.state.restart_count, 1)
        self.assertEqual(
            result.state.recovery_status,
            "restart_protected_program_resumed",
        )
        self.assertNotIn("abort", result.to_dict())
        self.assertNotIn("continue", result.to_dict())

    def test_unprotected_restart_keeps_program_identity_but_marks_recovery_unknown(self):
        result = apply_program_alarm(
            GuidanceComputerState(time_s=0.0, active_program="P_OTHER"),
            ProgramAlarmEvent(time_s=1.0, code="A1"),
            self.config(),
        )

        self.assertEqual(result.state.active_program, "P_OTHER")
        self.assertEqual(
            result.state.recovery_status,
            "restart_occurred_program_recovery_unspecified",
        )
        self.assertFalse(result.restart_protected_recovery)

    def test_nonrestart_alarm_does_not_increment_restart_count(self):
        result = apply_program_alarm(
            GuidanceComputerState(time_s=0.0, active_program="P_ALPHA"),
            ProgramAlarmEvent(time_s=2.0, code="A2"),
            self.config(),
        )

        self.assertFalse(result.restart_occurred)
        self.assertEqual(result.state.restart_count, 0)
        self.assertEqual(
            result.state.recovery_status,
            "alarm_without_software_restart",
        )

    def test_alarm_history_accumulates_and_clear_preserves_history(self):
        first = apply_program_alarm(
            GuidanceComputerState(time_s=0.0, active_program="P_ALPHA"),
            ProgramAlarmEvent(time_s=1.0, code="A1"),
            self.config(),
        )
        cleared = clear_program_alarm(first.state, time_s=1.5)
        second = apply_program_alarm(
            cleared,
            ProgramAlarmEvent(time_s=2.0, code="A2"),
            self.config(),
        )

        self.assertFalse(cleared.program_alarm_active)
        self.assertIsNone(cleared.active_alarm_code)
        self.assertEqual(second.state.alarm_history, ("A1", "A2"))
        self.assertEqual(second.state.restart_count, 1)

    def test_unknown_alarm_and_backward_time_are_rejected(self):
        state = GuidanceComputerState(time_s=5.0, active_program="P_ALPHA")
        with self.assertRaisesRegex(ValueError, "unknown alarm code"):
            apply_program_alarm(
                state,
                ProgramAlarmEvent(time_s=6.0, code="NOPE"),
                self.config(),
            )
        with self.assertRaisesRegex(ValueError, "move backward"):
            apply_program_alarm(
                state,
                ProgramAlarmEvent(time_s=4.0, code="A1"),
                self.config(),
            )
        with self.assertRaisesRegex(ValueError, "move backward"):
            clear_program_alarm(state, time_s=4.0)


if __name__ == "__main__":
    unittest.main()
