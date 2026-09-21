from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.descent_decision_gate import (  # noqa: E402
    LandingRadarControllerState,
    Readiness,
    RelayState,
)
from apollo_mission_control.descent_decision_projection import (  # noqa: E402
    DescentDecisionProjectionConfig,
    project_generic_runtime_descent_gate,
)
from apollo_mission_control.generic_runtime import (  # noqa: E402
    GenericAuditEvent,
    GenericCapcomQueueItem,
    GenericReadinessReport,
)


class DescentDecisionProjectionTests(unittest.TestCase):
    def config(self):
        return DescentDecisionProjectionConfig(
            gate_id="landing_go",
            capcom_go_action="landing_go",
            capcom_no_go_action="landing_no_go",
        )

    def test_station_go_calls_do_not_create_flight_decision(self):
        gate = project_generic_runtime_descent_gate(
            get_s=100.0,
            landing_radar=LandingRadarControllerState(antenna_position=2),
            readiness_reports=[
                GenericReadinessReport(90.0, "g", "GUIDANCE", True),
                GenericReadinessReport(91.0, "c", "CONTROL", True),
            ],
            audit_events=[],
            capcom_queue=[],
            config=self.config(),
        )
        self.assertEqual(gate.guidance_readiness, Readiness.GO)
        self.assertEqual(gate.control_readiness, Readiness.GO)
        self.assertEqual(gate.flight_decision, Readiness.UNKNOWN)
        self.assertEqual(gate.capcom_relay, RelayState.NOT_RELAYED)

    def test_latest_station_report_wins_without_touching_other_states(self):
        gate = project_generic_runtime_descent_gate(
            get_s=100.0,
            landing_radar=LandingRadarControllerState(),
            readiness_reports=[
                GenericReadinessReport(80.0, "g", "GUIDANCE", True),
                GenericReadinessReport(95.0, "g", "GUIDANCE", False),
                GenericReadinessReport(96.0, "c", "CONTROL", True),
            ],
            audit_events=[],
            capcom_queue=[],
            config=self.config(),
        )
        self.assertEqual(gate.guidance_readiness, Readiness.NO_GO)
        self.assertEqual(gate.control_readiness, Readiness.GO)
        self.assertEqual(gate.flight_decision, Readiness.UNKNOWN)

    def test_flight_decision_is_gate_scoped_and_time_scoped(self):
        events = [
            GenericAuditEvent(
                sequence=1,
                get_s=90.0,
                kind="flight_decision",
                actor="FLIGHT",
                details={"gate": "other_gate", "go": True},
            ),
            GenericAuditEvent(
                sequence=2,
                get_s=95.0,
                kind="flight_decision",
                actor="FLIGHT",
                details={"gate": "landing_go", "go": False},
            ),
            GenericAuditEvent(
                sequence=3,
                get_s=105.0,
                kind="flight_decision",
                actor="FLIGHT",
                details={"gate": "landing_go", "go": True},
            ),
        ]
        gate = project_generic_runtime_descent_gate(
            get_s=100.0,
            landing_radar=LandingRadarControllerState(),
            readiness_reports=[],
            audit_events=events,
            capcom_queue=[],
            config=self.config(),
        )
        self.assertEqual(gate.flight_decision, Readiness.NO_GO)

    def test_untransmitted_capcom_item_does_not_count_as_relay(self):
        item = GenericCapcomQueueItem(
            item_id=1,
            get_s=90.0,
            requested_by="cap",
            action="landing_go",
            parameters={},
            basis="test",
        )
        gate = project_generic_runtime_descent_gate(
            get_s=100.0,
            landing_radar=LandingRadarControllerState(),
            readiness_reports=[],
            audit_events=[],
            capcom_queue=[item],
            config=self.config(),
        )
        self.assertEqual(gate.capcom_relay, RelayState.NOT_RELAYED)

    def test_conflicting_transmitted_relay_is_exposed_not_repaired(self):
        item = GenericCapcomQueueItem(
            item_id=1,
            get_s=95.0,
            requested_by="cap",
            action="landing_go",
            parameters={},
            basis="test",
            transmitted=True,
            transmitted_get_s=99.0,
        )
        event = GenericAuditEvent(
            sequence=1,
            get_s=98.0,
            kind="flight_decision",
            actor="FLIGHT",
            details={"gate": "landing_go", "go": False},
        )
        gate = project_generic_runtime_descent_gate(
            get_s=100.0,
            landing_radar=LandingRadarControllerState(),
            readiness_reports=[],
            audit_events=[event],
            capcom_queue=[item],
            config=self.config(),
        )
        self.assertEqual(gate.flight_decision, Readiness.NO_GO)
        self.assertEqual(gate.capcom_relay, RelayState.GO_RELAYED)
        self.assertFalse(gate.relay_consistent_with_flight)

    def test_future_transmission_is_not_visible_yet(self):
        item = GenericCapcomQueueItem(
            item_id=1,
            get_s=95.0,
            requested_by="cap",
            action="landing_no_go",
            parameters={},
            basis="test",
            transmitted=True,
            transmitted_get_s=105.0,
        )
        gate = project_generic_runtime_descent_gate(
            get_s=100.0,
            landing_radar=LandingRadarControllerState(),
            readiness_reports=[],
            audit_events=[],
            capcom_queue=[item],
            config=self.config(),
        )
        self.assertEqual(gate.capcom_relay, RelayState.NOT_RELAYED)


if __name__ == "__main__":
    unittest.main()
