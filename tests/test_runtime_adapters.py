from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.apollo11_descent_session import (  # noqa: E402
    Apollo11DescentSession,
)
from apollo_mission_control.descent_decision_gate import (  # noqa: E402
    LandingRadarControllerState,
    Readiness,
    RelayState,
)
from apollo_mission_control.generic_runtime import GenericScenarioSession  # noqa: E402
from apollo_mission_control.guidance_computer_model import (  # noqa: E402
    GuidanceComputerState,
)
from apollo_mission_control.pc2_session import PC2Session  # noqa: E402
from apollo_mission_control.runtime_adapters import (  # noqa: E402
    create_runtime,
    has_runtime_adapter,
    runtime_capabilities,
    supported_runtime_adapters,
)
from apollo_mission_control.scenario_catalog import (  # noqa: E402
    DEFAULT_SCENARIO_ID,
    ScenarioRecord,
    get_scenario_record,
)
from apollo_mission_control.session_runtime import SessionRuntime  # noqa: E402


class RuntimeAdapterTests(unittest.TestCase):
    def test_pc2_adapter_builds_shared_runtime_contract(self):
        record = get_scenario_record(DEFAULT_SCENARIO_ID)
        runtime = create_runtime(record)

        self.assertIsInstance(runtime, PC2Session)
        self.assertIsInstance(runtime, SessionRuntime)
        self.assertEqual(runtime.state.get_s, record.start_get_s)
        self.assertIn("pc2_v1", supported_runtime_adapters())
        self.assertTrue(has_runtime_adapter("pc2_v1"))

    def test_generic_adapter_is_registered_without_pc2_capabilities(self):
        self.assertIn("generic_v1", supported_runtime_adapters())
        self.assertTrue(has_runtime_adapter("generic_v1"))
        capabilities = runtime_capabilities("generic_v1")
        self.assertIn("mission_control_core", capabilities)
        self.assertIn("state_injection", capabilities)
        self.assertIn("generic_timed_events", capabilities)
        self.assertNotIn("pc2_delta_p", capabilities)
        self.assertNotIn("pc2_dps_shutdown", capabilities)

    def test_apollo11_adapter_binds_generic_runtime_to_descent_projection(self):
        record = get_scenario_record(
            "apollo11_descent_program_alarm_reference"
        )
        self.assertTrue(record.execution_enabled)
        self.assertTrue(record.execution_requires_validated_model)
        self.assertTrue(has_runtime_adapter("apollo11_descent_v1"))

        runtime = create_runtime(record)
        self.assertIsInstance(runtime, Apollo11DescentSession)
        self.assertIsInstance(runtime, GenericScenarioSession)
        self.assertIsInstance(runtime, SessionRuntime)
        self.assertEqual(runtime.state.get_s, 369450.0)
        self.assertEqual(runtime.state.phase, "braking")
        self.assertEqual(runtime.pdi_get_s, 369185.2)
        self.assertEqual(
            runtime.decision_config.guidance_station,
            "GUIDO",
        )
        self.assertEqual(
            runtime.available_stations,
            ("FLIGHT", "CAPCOM", "GUIDO", "CONTROL", "TELCOM"),
        )

        capabilities = runtime_capabilities("apollo11_descent_v1")
        self.assertIn("mission_control_core", capabilities)
        self.assertIn("generic_timed_events", capabilities)
        self.assertIn("apollo11_descent_reference", capabilities)
        self.assertIn("apollo11_descent_projection", capabilities)
        self.assertNotIn("state_injection", capabilities)
        self.assertNotIn("pc2_delta_p", capabilities)

        runtime.assign_stations("guido", ["GUIDO"])
        runtime.assign_stations("control", ["CONTROL"])
        runtime.assign_stations("flight", ["FLIGHT"])
        runtime.assign_stations("capcom", ["CAPCOM"])
        runtime.start()
        runtime.advance_to(369692.0)

        self.assertEqual(runtime.state.phase, "approach")
        self.assertEqual(runtime.state.variables["program.number"], "P64")
        self.assertEqual(runtime.pending_gate, "landing_go")
        self.assertEqual(
            runtime.player_snapshot("guido").presentation["observations"],
            {},
        )

        runtime.submit_readiness(
            "guido",
            ready=True,
            station="GUIDO",
            note="explicit architecture-test call",
        )
        runtime.submit_readiness(
            "control",
            ready=True,
            station="CONTROL",
            note="explicit architecture-test call",
        )
        runtime.record_flight_go(
            "flight",
            go=True,
            basis="explicit architecture-test FLIGHT decision",
        )
        item = runtime.queue_capcom_instruction(
            "capcom",
            action="landing_go",
            parameters={},
            basis="explicit architecture-test CAPCOM relay",
        )
        runtime.transmit_capcom_item("capcom", item.item_id)

        projection = runtime.project_descent(
            landing_radar=LandingRadarControllerState(
                range_data_good=True,
                velocity_data_good=True,
                antenna_position=2,
                slant_range_ft=7600.0,
                pgns_altitude_ft=7550.0,
            ),
            controller_product_values={
                "lr.range_data_good": True,
                "lr.velocity_data_good": True,
                "lr.slant_range_ft": 7600.0,
                "pgns.altitude_ft": 7550.0,
                "control.lr_antenna_position": 2,
            },
            guidance_computer_state=GuidanceComputerState(
                time_s=runtime.state.get_s,
                active_program="P64",
                program_alarm_active=True,
                active_alarm_code="1202",
                restart_count=2,
                recovery_status="restart_protected_program_resumed",
                alarm_history=("1202", "1202"),
            ),
            provenance=("adapter architecture test",),
        )

        self.assertEqual(projection.decision_gate.guidance_readiness, Readiness.GO)
        self.assertEqual(projection.decision_gate.control_readiness, Readiness.GO)
        self.assertEqual(projection.decision_gate.flight_decision, Readiness.GO)
        self.assertEqual(projection.decision_gate.capcom_relay, RelayState.GO_RELAYED)
        self.assertFalse(
            projection.controller_products.product(
                "program.alarm_latest"
            ).available
        )

        runtime.advance_to(369802.0)
        self.assertEqual(runtime.state.phase, "landing")
        self.assertEqual(runtime.state.variables["program.number"], "P66")
        self.assertEqual(runtime.state.variables["control.mode"], "manual")

    def test_capabilities_keep_pc2_specific_operations_explicit(self):
        capabilities = runtime_capabilities("pc2_v1")
        self.assertIn("mission_control_core", capabilities)
        self.assertIn("state_injection", capabilities)
        self.assertIn("pc2_delta_p", capabilities)
        self.assertIn("pc2_dps_shutdown", capabilities)
        self.assertEqual(runtime_capabilities("not-implemented"), frozenset())

    def test_unknown_adapter_is_rejected(self):
        source = get_scenario_record(DEFAULT_SCENARIO_ID)
        unsupported = ScenarioRecord(
            scenario_id="synthetic_unimplemented",
            title="Synthetic unimplemented runtime",
            mission=source.mission,
            status="test",
            scenario_class="test",
            runtime_adapter="not_implemented_v1",
            mission_profile_id="apollo11_g",
            model_profile_id="synthetic_model_profile",
            required_model_domains=("test",),
            start_get_s=0.0,
            start_get_hms="00:00:00",
            end_target_get_hms="00:01:00",
            vehicle_configuration="test",
            source_count=0,
            fixture_path=source.fixture_path,
        )
        self.assertFalse(has_runtime_adapter(unsupported.runtime_adapter))
        with self.assertRaisesRegex(ValueError, "unsupported runtime adapter"):
            create_runtime(unsupported)


if __name__ == "__main__":
    unittest.main()
