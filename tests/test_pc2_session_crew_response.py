from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.crew_response import (  # noqa: E402
    apply_session_engine_off_response,
    command_dps_shutdown_from_callout,
    record_crew_receipt,
)
from apollo_mission_control.pc2_nominal import hms_to_seconds, load_fixture  # noqa: E402
from apollo_mission_control.pc2_session import PC2Session  # noqa: E402
from apollo_mission_control.scenario_injection import EvidenceClass, StateInjection  # noqa: E402


class CrewResponseIntegrationTests(unittest.TestCase):
    def _transmitted_delta_p_callout(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        session = PC2Session.create(fixture)
        session.assign_station("flight", "FLIGHT")
        session.assign_station("control", "CONTROL")
        session.assign_station("capcom", "CAPCOM")
        session.start()
        session.advance_to(hms_to_seconds("79:17:00"))
        session.record_flight_go("flight", go=True, basis="synthetic integration test")
        session.advance_to(hms_to_seconds("79:29:00"))
        session.apply_session_injection(
            StateInjection(
                injection_id="test-delta-p-26",
                get_s=session.state.get_s,
                target="dps_fuel_oxidizer_delta_p_psi",
                value=26.0,
                evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                provenance="synthetic boundary test; not an Apollo 13 measurement",
            )
        )
        item = session.record_control_delta_p_callout(
            "control",
            basis="synthetic >25 psi rule exercise",
        )
        session.transmit_capcom_item("capcom", item.item_id)
        return session, item

    def test_transmission_does_not_imply_receipt_or_command(self):
        session, _item = self._transmitted_delta_p_callout()
        self.assertFalse(session.state.crew_dps_shutdown_commanded)
        self.assertTrue(session.state.engine_running)
        self.assertNotIn("crew_capcom_item_received", [event.kind for event in session.audit_log])

    def test_receipt_is_explicit_and_does_not_command_engine(self):
        session, item = self._transmitted_delta_p_callout()
        event = record_crew_receipt(session, item.item_id)
        self.assertEqual(event["kind"], "crew_capcom_item_received")
        self.assertFalse(session.state.crew_dps_shutdown_commanded)
        self.assertTrue(session.state.engine_running)

    def test_shutdown_command_requires_recorded_receipt(self):
        session, item = self._transmitted_delta_p_callout()
        with self.assertRaises(ValueError):
            command_dps_shutdown_from_callout(session, item.item_id)

    def test_command_and_physical_response_remain_separate(self):
        session, item = self._transmitted_delta_p_callout()
        record_crew_receipt(session, item.item_id)
        command_dps_shutdown_from_callout(session, item.item_id)

        self.assertTrue(session.state.crew_dps_shutdown_commanded)
        self.assertTrue(session.state.engine_running)

        response_get = session.state.get_s + 1.0
        response = apply_session_engine_off_response(session, get_s=response_get)
        self.assertFalse(session.state.engine_running)
        self.assertEqual(response["get_s"], response_get)

        kinds = [event.kind for event in session.audit_log]
        self.assertLess(kinds.index("capcom_item_transmitted"), kinds.index("crew_capcom_item_received"))
        self.assertLess(kinds.index("crew_capcom_item_received"), kinds.index("crew_dps_shutdown_commanded"))
        self.assertLess(kinds.index("crew_dps_shutdown_commanded"), kinds.index("dps_engine_off_physical_response"))


if __name__ == "__main__":
    unittest.main()
