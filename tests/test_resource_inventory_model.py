from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.resource_inventory_model import (  # noqa: E402
    ResourceFlowSegment,
    ResourceInventoryConfig,
    ResourceInventoryState,
    ResourceSpec,
    simulate_resource_inventory,
)


class ResourceInventoryModelTests(unittest.TestCase):
    def config(self):
        return ResourceInventoryConfig(
            resources=(
                ResourceSpec("battery_energy", "Wh", 0.0, 1000.0),
                ResourceSpec("oxygen", "kg", 0.0, 10.0),
            ),
            applicability="synthetic resource test",
            provenance=("synthetic",),
        )

    def test_piecewise_consumption_updates_multiple_resources(self):
        result = simulate_resource_inventory(
            ResourceInventoryState(
                time_s=100.0,
                quantities={"battery_energy": 800.0, "oxygen": 8.0},
            ),
            [
                ResourceFlowSegment(
                    10.0,
                    {"battery_energy": 2.0, "oxygen": 0.1},
                    label="high_load",
                ),
                ResourceFlowSegment(
                    20.0,
                    {"battery_energy": 1.0, "oxygen": 0.05},
                    label="low_load",
                ),
            ],
            self.config(),
        )
        self.assertEqual(result.final_state.time_s, 130.0)
        self.assertAlmostEqual(result.final_state.quantities["battery_energy"], 760.0)
        self.assertAlmostEqual(result.final_state.quantities["oxygen"], 6.0)
        self.assertAlmostEqual(result.consumed["battery_energy"], 40.0)
        self.assertAlmostEqual(result.consumed["oxygen"], 2.0)

    def test_depletion_clamps_at_minimum_and_reports_exact_boundary_time(self):
        result = simulate_resource_inventory(
            ResourceInventoryState(
                time_s=50.0,
                quantities={"battery_energy": 10.0, "oxygen": 8.0},
            ),
            [
                ResourceFlowSegment(
                    10.0,
                    {"battery_energy": 2.0},
                    label="draw",
                )
            ],
            self.config(),
        )
        self.assertEqual(result.final_state.quantities["battery_energy"], 0.0)
        self.assertEqual(result.unsatisfied_consumption["battery_energy"], 10.0)
        event = next(
            event
            for event in result.boundary_events
            if event.resource_id == "battery_energy"
        )
        self.assertEqual(event.boundary, "minimum")
        self.assertAlmostEqual(event.time_s, 55.0)

    def test_replenishment_clamps_at_maximum_and_reports_overflow(self):
        result = simulate_resource_inventory(
            ResourceInventoryState(
                time_s=0.0,
                quantities={"battery_energy": 900.0, "oxygen": 8.0},
            ),
            [
                ResourceFlowSegment(
                    10.0,
                    {"battery_energy": -20.0},
                    label="charge",
                )
            ],
            self.config(),
        )
        self.assertEqual(result.final_state.quantities["battery_energy"], 1000.0)
        self.assertEqual(result.replenished["battery_energy"], 100.0)
        self.assertEqual(result.overflow["battery_energy"], 100.0)
        event = next(
            event
            for event in result.boundary_events
            if event.resource_id == "battery_energy"
        )
        self.assertEqual(event.boundary, "maximum")
        self.assertAlmostEqual(event.time_s, 5.0)

    def test_unbounded_resource_can_replenish_without_overflow(self):
        config = ResourceInventoryConfig(
            resources=(ResourceSpec("tank", "kg", 0.0, None),)
        )
        result = simulate_resource_inventory(
            ResourceInventoryState(0.0, {"tank": 5.0}),
            [ResourceFlowSegment(10.0, {"tank": -1.0})],
            config,
        )
        self.assertEqual(result.final_state.quantities["tank"], 15.0)
        self.assertEqual(result.overflow["tank"], 0.0)

    def test_zero_rate_and_zero_duration_are_stable(self):
        result = simulate_resource_inventory(
            ResourceInventoryState(
                0.0,
                {"battery_energy": 500.0, "oxygen": 5.0},
            ),
            [
                ResourceFlowSegment(0.0, {"battery_energy": 100.0}, "zero"),
                ResourceFlowSegment(10.0, {}, "coast"),
            ],
            self.config(),
        )
        self.assertEqual(
            result.final_state.quantities,
            {"battery_energy": 500.0, "oxygen": 5.0},
        )

    def test_bad_initial_state_and_unknown_flows_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "missing initial quantity"):
            simulate_resource_inventory(
                ResourceInventoryState(0.0, {"battery_energy": 1.0}),
                [ResourceFlowSegment(1.0, {})],
                self.config(),
            )

        with self.assertRaisesRegex(ValueError, "unknown resource flow"):
            simulate_resource_inventory(
                ResourceInventoryState(
                    0.0,
                    {"battery_energy": 1.0, "oxygen": 1.0},
                ),
                [ResourceFlowSegment(1.0, {"water": 1.0})],
                self.config(),
            )

    def test_negative_duration_and_duplicate_resource_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "non-negative"):
            ResourceFlowSegment(-1.0, {}).validated(self.config())

        with self.assertRaisesRegex(ValueError, "duplicate resource_id"):
            ResourceInventoryConfig(
                resources=(
                    ResourceSpec("same", "kg"),
                    ResourceSpec("same", "kg"),
                )
            ).validated()


if __name__ == "__main__":
    unittest.main()
