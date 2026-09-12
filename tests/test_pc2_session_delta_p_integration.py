from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_nominal import hms_to_seconds, load_fixture  # noqa: E402
from apollo_mission_control.pc2_session import PC2Session  # noqa: E402
from apollo_mission_control.scenario_injection import (  # noqa: E402
    EvidenceClass,
    StateInjection,
)


class DeltaPSessionIntegrationTests(unittest.TestCase):
    def _session(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        session = PC2Session.create(fixture)
        session.assign_station("flight", "FLIGHT")
        session.assign_station("control", "CONTROL")
        session.assign_station("capcom", "CAPCOM")
        session.start()
        session.advance_to(hms_to_seconds("79:17:00"))
        session.record_flight_go("flight", go=True, basis="test nominal readiness")
        session.advance_to(hms_to_seconds("79:29:00"))
        return session

    def test_delta_p_injection_is_visible_without_automatic_diagnosis(self):
        session = self._session()
        session.apply_session_injection(
            StateInjection(
                injection_id="test-delta-p-26",
                get_s=session.state.get_s,
                target="dps_fuel_oxidizer_delta_p_psi",
                value=26.0,
                evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                provenance="synthetic boundary test; 26 psi is not an Apollo 13 measurement",
            )
        )

        self.assertEqual(session.state.dps_fuel_oxidizer_delta_p_psi, 26.0)
        self.assertEqual(len(session.capcom_queue), 0)
        control = session.player_snapshot("control").to_dict()
        fields = [
            field
            for section in control["presentation"]["sections"]
            for field in section["fields"]
        ]
        delta_p = next(field for field in fields if field["key"] == "dps.fuel_oxidizer_delta_p_psi")
        self.assertEqual(delta_p["value"], 26.0)

    def test_control_decision_then_capcom_transmission_are_separate(self):
        session = self._session()
        session.apply_session_injection(
            StateInjection(
                injection_id="test-delta-p-26",
                get_s=session.state.get_s,
                target="dps_fuel_oxidizer_delta_p_psi",
                value=26.0,
                evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                provenance="synthetic boundary test; 26 psi is not an Apollo 13 measurement",
            )
        )

        item = session.record_control_delta_p_callout(
            "control",
            basis="fuel/oxidizer differential pressure >25 psi; ground callout only",
        )
        self.assertEqual(item.requested_by, "CONTROL")
        self.assertFalse(item.transmitted)
        self.assertTrue(session.state.engine_running)
        self.assertFalse(session.state.crew_dps_shutdown_commanded)

        capcom = session.player_snapshot("capcom").to_dict()
        queue = capcom["presentation"]["queue_items"]
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue[0]["requested_by"], "CONTROL")
        self.assertIn("exact internal Apollo routing unresolved", queue[0]["parameters"]["routing_note"])

        session.transmit_capcom_item("capcom", item.item_id)
        self.assertTrue(item.transmitted)
        self.assertTrue(session.state.engine_running)
        self.assertFalse(session.state.crew_dps_shutdown_commanded)

        kinds = [event.kind for event in session.audit_log]
        self.assertIn("state_injection_applied", kinds)
        self.assertIn("controller_shutdown_callout_decision", kinds)
        self.assertIn("capcom_item_transmitted", kinds)

    def test_callout_rejected_when_rule_not_triggered(self):
        session = self._session()
        session.apply_session_injection(
            StateInjection(
                injection_id="test-delta-p-25",
                get_s=session.state.get_s,
                target="dps_fuel_oxidizer_delta_p_psi",
                value=25.0,
                evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                provenance="synthetic boundary test",
            )
        )
        with self.assertRaises(ValueError):
            session.record_control_delta_p_callout("control", basis="should not trigger")


if __name__ == "__main__":
    unittest.main()
