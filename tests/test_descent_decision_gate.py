from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.descent_decision_gate import (  # noqa: E402
    DescentDecisionGate,
    LandingRadarControllerState,
    Readiness,
    RelayState,
)


class DescentDecisionGateTests(unittest.TestCase):
    def test_lr_antenna_position_does_not_imply_guidance_go(self):
        gate = DescentDecisionGate(
            get_s=369000.0,
            landing_radar=LandingRadarControllerState(antenna_position=2),
            control_readiness=Readiness.GO,
        )
        self.assertEqual(gate.guidance_readiness, Readiness.UNKNOWN)
        self.assertEqual(gate.flight_decision, Readiness.UNKNOWN)
        self.assertFalse(gate.front_room_inputs_complete)

    def test_lr_validity_fields_remain_distinct(self):
        gate = DescentDecisionGate(
            get_s=369000.0,
            landing_radar=LandingRadarControllerState(
                range_data_good=True,
                velocity_data_good=False,
                antenna_position=2,
            ),
        )
        payload = gate.to_dict()
        self.assertTrue(payload["landing_radar"]["range_data_good"])
        self.assertFalse(payload["landing_radar"]["velocity_data_good"])
        self.assertEqual(payload["landing_radar"]["antenna_position"], 2)

    def test_station_readiness_does_not_auto_create_flight_decision(self):
        gate = DescentDecisionGate(
            get_s=369000.0,
            landing_radar=LandingRadarControllerState(),
            guidance_readiness=Readiness.GO,
            control_readiness=Readiness.GO,
        )
        self.assertTrue(gate.front_room_inputs_complete)
        self.assertEqual(gate.flight_decision, Readiness.UNKNOWN)

    def test_capcom_relay_is_separate_and_chain_checked(self):
        inconsistent = DescentDecisionGate(
            get_s=369000.0,
            landing_radar=LandingRadarControllerState(),
            flight_decision=Readiness.NO_GO,
            capcom_relay=RelayState.GO_RELAYED,
        )
        self.assertFalse(inconsistent.relay_consistent_with_flight)

        consistent = DescentDecisionGate(
            get_s=369000.0,
            landing_radar=LandingRadarControllerState(),
            flight_decision=Readiness.GO,
            capcom_relay=RelayState.GO_RELAYED,
        )
        self.assertTrue(consistent.relay_consistent_with_flight)

    def test_invalid_antenna_position_is_rejected(self):
        with self.assertRaises(ValueError):
            DescentDecisionGate(
                get_s=369000.0,
                landing_radar=LandingRadarControllerState(antenna_position=3),
            ).validated()


if __name__ == "__main__":
    unittest.main()
