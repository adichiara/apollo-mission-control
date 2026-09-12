from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.dps_response import apply_engine_off_response  # noqa: E402
from apollo_mission_control.operational_actions import (  # noqa: E402
    OperationalAction,
    apply_operational_action,
)
from apollo_mission_control.pc2_nominal import PC2State  # noqa: E402


class DPSShutdownResponseTests(unittest.TestCase):
    def test_stop_pushbutton_records_command_without_forcing_physical_shutdown(self):
        state = PC2State(get_s=100.0, engine_running=True, throttle_phase="maximum")
        apply_operational_action(
            state,
            OperationalAction(
                action_id="stop-push",
                get_s=101.0,
                actor="CREW",
                action="press_engine_stop",
                parameters={},
                provenance="contemporary LM manual STOP-pushbutton control path",
            ),
        )

        self.assertTrue(state.crew_dps_shutdown_commanded)
        self.assertEqual(state.crew_dps_shutdown_command_get_s, 101.0)
        self.assertTrue(state.engine_running)
        self.assertEqual(state.throttle_phase, "maximum")

    def test_explicit_physical_response_stops_engine_without_synthesizing_pressure(self):
        state = PC2State(
            get_s=100.0,
            engine_running=True,
            throttle_phase="maximum",
            dps_chamber_pressure_psi=100.0,
            dps_chamber_pressure_observed_get_s=100.0,
        )
        response = apply_engine_off_response(state, get_s=101.2)

        self.assertFalse(state.engine_running)
        self.assertEqual(state.throttle_phase, "off")
        self.assertTrue(response.engine_off_discrete_received)
        self.assertTrue(response.pilot_valves_commanded_closed)
        self.assertTrue(response.propellant_shutoff_valves_commanded_closed)
        # No unsupported pressure tailoff is fabricated by the response helper.
        self.assertEqual(state.dps_chamber_pressure_psi, 100.0)
        self.assertEqual(state.dps_chamber_pressure_observed_get_s, 100.0)

    def test_response_time_is_supplied_not_invented(self):
        state = PC2State(get_s=100.0, engine_running=True, throttle_phase="maximum")
        response = apply_engine_off_response(state, get_s=103.75)
        self.assertEqual(response.get_s, 103.75)
        self.assertEqual(state.get_s, 103.75)


if __name__ == "__main__":
    unittest.main()
