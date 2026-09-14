from dataclasses import dataclass
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.generic_runtime import GenericScenarioSession  # noqa: E402
from apollo_mission_control.runtime_adapters import (  # noqa: E402
    create_runtime,
    runtime_capabilities,
)
from apollo_mission_control.scenario_catalog import ScenarioRecord  # noqa: E402
from apollo_mission_control.session_runtime import SessionRuntime, SessionStatus  # noqa: E402


FIXTURE = ROOT / "tests" / "fixtures" / "generic_runtime_scenario.json"


def record() -> ScenarioRecord:
    return ScenarioRecord(
        scenario_id="synthetic_generic_runtime",
        title="Synthetic Generic Runtime",
        mission="Synthetic",
        status="test fixture",
        scenario_class="synthetic_validation",
        runtime_adapter="generic_v1",
        mission_profile_id="synthetic",
        model_profile_id="synthetic",
        required_model_domains=("synthetic",),
        start_get_s=100.0,
        start_get_hms="00:01:40",
        end_target_get_hms="00:02:10",
        vehicle_configuration="synthetic",
        source_count=0,
        fixture_path=FIXTURE,
    )


@dataclass(frozen=True)
class Injection:
    injection_id: str
    get_s: float
    target: str
    value: object
    evidence_class: str = "source_bounded_test"
    provenance: str = "synthetic runtime test"


class GenericRuntimeTests(unittest.TestCase):
    def setUp(self):
        runtime = create_runtime(record())
        self.assertIsInstance(runtime, GenericScenarioSession)
        self.assertIsInstance(runtime, SessionRuntime)
        self.session = runtime

    def test_second_runtime_adapter_is_executable_without_pc2_session(self):
        self.assertEqual(self.session.state.get_s, 100.0)
        self.assertEqual(
            self.session.available_stations,
            ("FLIGHT", "CAPCOM", "SYSTEMS"),
        )
        capabilities = runtime_capabilities("generic_v1")
        self.assertIn("mission_control_core", capabilities)
        self.assertIn("state_injection", capabilities)
        self.assertNotIn("pc2_delta_p", capabilities)

    def test_timed_external_event_updates_state_and_opens_gate(self):
        self.session.start()
        reached = self.session.advance_to(115.0)

        self.assertEqual(reached, 115.0)
        self.assertEqual(self.session.state.phase, "response")
        self.assertTrue(self.session.state.variables["system_alert"])
        self.assertEqual(self.session.pending_gate, "continue_or_hold")
        self.assertEqual(
            [event.kind for event in self.session.audit_log].count(
                "scenario_event_applied"
            ),
            1,
        )

    def test_station_projection_does_not_expose_hidden_state(self):
        self.session.join_or_rejoin_stations("systems", ("SYSTEMS",))
        snapshot = self.session.player_snapshot("systems").to_dict()

        self.assertEqual(
            snapshot["presentation"]["observations"],
            {"system_alert": False},
        )
        self.assertNotIn(
            "private_source_state",
            snapshot["presentation"]["observations"],
        )

    def test_readiness_flight_and_capcom_workflow_is_generic(self):
        self.session.join_or_rejoin_stations("flight", ("FLIGHT",))
        self.session.join_or_rejoin_stations("capcom", ("CAPCOM",))
        self.session.start()
        self.session.advance_to(110.0)

        report = self.session.submit_readiness(
            "flight",
            ready=True,
            note="synthetic go",
        )
        self.assertTrue(report.ready)

        self.session.record_flight_go(
            "flight",
            go=True,
            basis="synthetic decision",
        )
        self.assertIsNone(self.session.pending_gate)

        item = self.session.queue_capcom_instruction(
            "capcom",
            action="report_status",
            parameters={"channel": "voice"},
            basis="synthetic test",
        )
        transmitted = self.session.transmit_capcom_item("capcom", item.item_id)
        self.assertTrue(transmitted.transmitted)
        self.assertEqual(transmitted.transmitted_get_s, 110.0)

    def test_controlled_injection_changes_only_whitelisted_source_state(self):
        self.session.start()
        self.session.apply_session_injection(
            Injection(
                injection_id="alert-on",
                get_s=self.session.state.get_s,
                target="system_alert",
                value=True,
            )
        )
        self.assertTrue(self.session.state.variables["system_alert"])

        with self.assertRaisesRegex(ValueError, "unsupported"):
            self.session.apply_session_injection(
                Injection(
                    injection_id="hidden-change",
                    get_s=self.session.state.get_s,
                    target="private_source_state",
                    value=99,
                )
            )

    def test_completion_event_stops_at_event_get(self):
        self.session.start()
        reached = self.session.advance_to(150.0)

        self.assertEqual(reached, 130.0)
        self.assertEqual(self.session.status, SessionStatus.COMPLETE)
        self.assertEqual(self.session.state.phase, "complete")

    def test_station_rejoin_and_conflicts_match_shared_contract(self):
        self.session.join_or_rejoin_stations("operator", ("SYSTEMS",))
        self.session.join_or_rejoin_stations("operator", ("SYSTEMS",))
        with self.assertRaisesRegex(ValueError, "already assigned"):
            self.session.join_or_rejoin_stations("other", ("SYSTEMS",))
        with self.assertRaisesRegex(ValueError, "cannot rejoin"):
            self.session.join_or_rejoin_stations("operator", ("FLIGHT",))


if __name__ == "__main__":
    unittest.main()
