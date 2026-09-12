from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.dps_restart_response import (  # noqa: E402
    apply_pc2_restart_response,
    restart_actions_complete,
)
from apollo_mission_control.operational_actions import (  # noqa: E402
    OperationalAction,
    apply_operational_action,
)
from apollo_mission_control.pc2_nominal import PC2State  # noqa: E402
from apollo_mission_control.restart_logic import (  # noqa: E402
    RestartDisposition,
    RestartEvaluation,
)


class PC2RestartResponseTests(unittest.TestCase):
    def _eligible(self):
        return RestartEvaluation(
            RestartDisposition.RESTART_ELIGIBLE,
            "synthetic test: cause affirmatively outside listed shutdown criteria",
        )

    def _perform_actions(self, state):
        for action in (
            OperationalAction("u", 101.0, "CREW", "restart_manual_ullage", {}, "PC+2 restart procedure"),
            OperationalAction("s", 102.0, "CREW", "press_engine_start", {}, "PC+2 restart procedure"),
            OperationalAction("o", 103.0, "CREW", "descent_engine_command_override_on", {}, "PC+2 restart procedure"),
        ):
            apply_operational_action(state, action)

    def test_commands_alone_do_not_restart_engine(self):
        state = PC2State(get_s=100.0, engine_running=False)
        self._perform_actions(state)
        self.assertTrue(restart_actions_complete(state))
        self.assertFalse(state.engine_running)

    def test_success_response_opens_valve_path_without_inventing_thrust(self):
        state = PC2State(get_s=100.0, engine_running=False)
        self._perform_actions(state)

        response = apply_pc2_restart_response(state, self._eligible(), get_s=104.0)

        self.assertTrue(state.engine_running)
        self.assertEqual(state.throttle_phase, "restart_thrust_unspecified")
        self.assertTrue(response.engine_on_command_received)
        self.assertTrue(response.pilot_valves_commanded_open)
        self.assertTrue(response.propellant_shutoff_valves_commanded_open)
        self.assertFalse(response.thrust_level_known)
        self.assertIsNone(state.dps_chamber_pressure_psi)

    def test_rule_caused_shutdown_cannot_use_restart_response(self):
        state = PC2State(get_s=100.0, engine_running=False)
        self._perform_actions(state)
        blocked = RestartEvaluation(
            RestartDisposition.DO_NOT_RESTART_RULE_SHUTDOWN,
            "synthetic test: listed rule triggered",
            triggered_rule_ids=("fuel_oxidizer_delta_p",),
        )
        with self.assertRaises(ValueError):
            apply_pc2_restart_response(state, blocked, get_s=104.0)
        self.assertFalse(state.engine_running)

    def test_incomplete_crew_sequence_cannot_apply_success_response(self):
        state = PC2State(get_s=100.0, engine_running=False)
        apply_operational_action(
            state,
            OperationalAction("s", 102.0, "CREW", "press_engine_start", {}, "PC+2 restart procedure"),
        )
        with self.assertRaises(ValueError):
            apply_pc2_restart_response(state, self._eligible(), get_s=104.0)


if __name__ == "__main__":
    unittest.main()
