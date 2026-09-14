from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.causal_translational_model import TranslationalState  # noqa: E402
from apollo_mission_control.electrical_power_model import (  # noqa: E402
    ElectricalBusConfig,
    ElectricalBusState,
    ElectricalLoadSpec,
    ElectricalSourceSpec,
    evaluate_electrical_bus,
)
from apollo_mission_control.resource_inventory_model import (  # noqa: E402
    ResourceFlowSegment,
    ResourceInventoryConfig,
    ResourceInventoryState,
    ResourceSpec,
    simulate_resource_inventory,
)
from apollo_mission_control.resource_power_coupling import (  # noqa: E402
    ResourceElectricalSourceRule,
    derive_electrical_source_availability,
)
from apollo_mission_control.tracking_observation import (  # noqa: E402
    TrackingObservationConfig,
    TrackingStationState,
    compute_geometric_tracking_truth,
    produce_tracking_observation,
)


class ResourcePowerObservationChainTests(unittest.TestCase):
    def resource_state_at(self, elapsed_s):
        result = simulate_resource_inventory(
            ResourceInventoryState(
                time_s=0.0,
                quantities={"energy": 5.0},
            ),
            [ResourceFlowSegment(elapsed_s, {"energy": 1.0}, label="load")],
            ResourceInventoryConfig(
                resources=(ResourceSpec("energy", "unit", 0.0, 5.0),)
            ),
        )
        return result.final_state

    def source_available(self, resource_state, *, hardware_available=True):
        coupling = derive_electrical_source_availability(
            resource_state,
            [
                ResourceElectricalSourceRule(
                    source_id="BATTERY_SOURCE",
                    resource_id="energy",
                    minimum_operating_quantity=0.0,
                    available_at_threshold=False,
                    provenance="synthetic coupling",
                )
            ],
            upstream_availability={"BATTERY_SOURCE": hardware_available},
        )
        return coupling[0]

    def power_result(self, available):
        return evaluate_electrical_bus(
            ElectricalBusConfig(
                bus_id="DATA_BUS",
                sources=(ElectricalSourceSpec("BATTERY_SOURCE", 100.0),),
                loads=(ElectricalLoadSpec("TRACKING_RECEIVER", 20.0, 0),),
            ),
            ElectricalBusState(
                source_available={"BATTERY_SOURCE": available},
                load_commanded_on={"TRACKING_RECEIVER": True},
            ),
        )

    def observation(self, powered, *, time_s):
        truth = compute_geometric_tracking_truth(
            TranslationalState(
                time_s=time_s,
                position_m=(1000.0, 0.0, 0.0),
                velocity_m_s=(1.0, 0.0, 0.0),
                mass_kg=1000.0,
            ),
            TrackingStationState(position_m=(0.0, 0.0, 0.0)),
        )
        return produce_tracking_observation(
            truth,
            TrackingObservationConfig(
                available=powered,
                valid=powered,
                source="synthetic powered tracking channel",
            ),
        )

    def test_resource_depletion_propagates_to_observation_without_scenario_branch(self):
        before_resource = self.resource_state_at(4.0)
        before_source = self.source_available(before_resource)
        before_power = self.power_result(before_source.available)
        before_observation = self.observation(
            before_power.load("TRACKING_RECEIVER").supplied,
            time_s=4.0,
        )

        after_resource = self.resource_state_at(6.0)
        after_source = self.source_available(after_resource)
        after_power = self.power_result(after_source.available)
        after_observation = self.observation(
            after_power.load("TRACKING_RECEIVER").supplied,
            time_s=6.0,
        )

        self.assertEqual(before_resource.quantities["energy"], 1.0)
        self.assertTrue(before_source.available)
        self.assertTrue(before_power.load("TRACKING_RECEIVER").supplied)
        self.assertTrue(before_observation.available)
        self.assertIsNotNone(before_observation.range_m)

        self.assertEqual(after_resource.quantities["energy"], 0.0)
        self.assertFalse(after_source.available)
        self.assertFalse(after_power.load("TRACKING_RECEIVER").supplied)
        self.assertFalse(after_observation.available)
        self.assertIsNone(after_observation.range_m)

    def test_hardware_failure_and_resource_depletion_are_separate_causes(self):
        resource = self.resource_state_at(1.0)
        resource_ok_hardware_failed = self.source_available(
            resource,
            hardware_available=False,
        )
        self.assertTrue(resource_ok_hardware_failed.resource_sufficient)
        self.assertFalse(resource_ok_hardware_failed.upstream_available)
        self.assertFalse(resource_ok_hardware_failed.available)

        depleted = self.source_available(self.resource_state_at(6.0))
        self.assertFalse(depleted.resource_sufficient)
        self.assertTrue(depleted.upstream_available)
        self.assertFalse(depleted.available)

    def test_threshold_semantics_are_explicit(self):
        state = ResourceInventoryState(0.0, {"energy": 2.0})
        strict = derive_electrical_source_availability(
            state,
            [
                ResourceElectricalSourceRule(
                    "S",
                    "energy",
                    minimum_operating_quantity=2.0,
                    available_at_threshold=False,
                )
            ],
        )[0]
        inclusive = derive_electrical_source_availability(
            state,
            [
                ResourceElectricalSourceRule(
                    "S",
                    "energy",
                    minimum_operating_quantity=2.0,
                    available_at_threshold=True,
                )
            ],
        )[0]
        self.assertFalse(strict.available)
        self.assertTrue(inclusive.available)

    def test_missing_resource_duplicate_source_and_unknown_upstream_are_rejected(self):
        state = ResourceInventoryState(0.0, {"energy": 1.0})
        with self.assertRaisesRegex(ValueError, "missing resource"):
            derive_electrical_source_availability(
                state,
                [ResourceElectricalSourceRule("S", "missing")],
            )

        with self.assertRaisesRegex(ValueError, "duplicate"):
            derive_electrical_source_availability(
                state,
                [
                    ResourceElectricalSourceRule("S", "energy"),
                    ResourceElectricalSourceRule("S", "energy"),
                ],
            )

        with self.assertRaisesRegex(ValueError, "uncoupled source"):
            derive_electrical_source_availability(
                state,
                [ResourceElectricalSourceRule("S", "energy")],
                upstream_availability={"OTHER": True},
            )


if __name__ == "__main__":
    unittest.main()
