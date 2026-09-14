from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.generic_runtime import GenericScenarioSession  # noqa: E402
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
            runtime_adapter="apollo11_descent_v1",
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
