from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.electrical_power_model import (  # noqa: E402
    ElectricalBusConfig,
    ElectricalBusState,
    ElectricalLoadSpec,
    ElectricalSourceSpec,
    evaluate_electrical_bus,
)


class ElectricalPowerModelTests(unittest.TestCase):
    def config(self):
        return ElectricalBusConfig(
            bus_id="BUS_A",
            sources=(
                ElectricalSourceSpec("SOURCE_1", 1000.0),
                ElectricalSourceSpec("SOURCE_2", 500.0),
            ),
            loads=(
                ElectricalLoadSpec("critical", 600.0, priority=0),
                ElectricalLoadSpec("guidance", 300.0, priority=1),
                ElectricalLoadSpec("comfort_a", 200.0, priority=2),
                ElectricalLoadSpec("comfort_b", 200.0, priority=2),
            ),
            applicability="synthetic power test",
            provenance=("synthetic",),
        )

    def evaluate(
        self,
        *,
        source_1=True,
        source_2=True,
        bus_enabled=True,
        loads=None,
    ):
        if loads is None:
            loads = {
                "critical": True,
                "guidance": True,
                "comfort_a": True,
                "comfort_b": True,
            }
        return evaluate_electrical_bus(
            self.config(),
            ElectricalBusState(
                source_available={
                    "SOURCE_1": source_1,
                    "SOURCE_2": source_2,
                },
                load_commanded_on=loads,
                bus_enabled=bus_enabled,
            ),
        )

    def test_all_loads_supplied_when_capacity_is_sufficient(self):
        result = self.evaluate()
        self.assertEqual(result.available_capacity_w, 1500.0)
        self.assertEqual(result.commanded_demand_w, 1300.0)
        self.assertEqual(result.supplied_demand_w, 1300.0)
        self.assertEqual(result.overload_w, 0.0)
        self.assertTrue(all(item.supplied for item in result.loads))

    def test_source_loss_causes_priority_based_load_shedding(self):
        result = self.evaluate(source_2=False)
        self.assertEqual(result.available_capacity_w, 1000.0)
        self.assertTrue(result.load("critical").supplied)
        self.assertTrue(result.load("guidance").supplied)
        self.assertFalse(result.load("comfort_a").supplied)
        self.assertFalse(result.load("comfort_b").supplied)
        self.assertEqual(
            result.load("comfort_a").reason,
            "insufficient_capacity_at_priority",
        )
        self.assertEqual(result.supplied_demand_w, 900.0)

    def test_equal_priority_group_is_all_or_none(self):
        loads = {
            "critical": False,
            "guidance": True,
            "comfort_a": True,
            "comfort_b": True,
        }
        result = self.evaluate(source_2=False, loads=loads)
        self.assertTrue(result.load("guidance").supplied)
        self.assertTrue(result.load("comfort_a").supplied)
        self.assertTrue(result.load("comfort_b").supplied)

        constrained = evaluate_electrical_bus(
            ElectricalBusConfig(
                bus_id="BUS",
                sources=(ElectricalSourceSpec("S", 650.0),),
                loads=(
                    ElectricalLoadSpec("first", 300.0, 0),
                    ElectricalLoadSpec("equal_a", 200.0, 1),
                    ElectricalLoadSpec("equal_b", 200.0, 1),
                ),
            ),
            ElectricalBusState(
                source_available={"S": True},
                load_commanded_on={
                    "first": True,
                    "equal_a": True,
                    "equal_b": True,
                },
            ),
        )
        self.assertTrue(constrained.load("first").supplied)
        self.assertFalse(constrained.load("equal_a").supplied)
        self.assertFalse(constrained.load("equal_b").supplied)
        self.assertEqual(constrained.supplied_demand_w, 300.0)

    def test_disabled_bus_supplies_nothing(self):
        result = self.evaluate(bus_enabled=False)
        self.assertFalse(result.bus_power_available)
        self.assertEqual(result.available_capacity_w, 0.0)
        self.assertEqual(result.supplied_demand_w, 0.0)
        self.assertTrue(all(not item.supplied for item in result.loads))
        self.assertTrue(all(
            item.reason == "bus_disabled" for item in result.loads
        ))

    def test_commanded_off_load_does_not_consume_capacity(self):
        result = self.evaluate(
            source_2=False,
            loads={
                "critical": True,
                "guidance": True,
                "comfort_a": False,
                "comfort_b": False,
            },
        )
        self.assertEqual(result.commanded_demand_w, 900.0)
        self.assertEqual(result.supplied_demand_w, 900.0)
        self.assertEqual(result.load("comfort_a").reason, "commanded_off")

    def test_unknown_state_keys_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown electrical source"):
            evaluate_electrical_bus(
                self.config(),
                ElectricalBusState(
                    source_available={"SOURCE_1": True, "UNKNOWN": True},
                    load_commanded_on={},
                ),
            )

        with self.assertRaisesRegex(ValueError, "unknown electrical load"):
            evaluate_electrical_bus(
                self.config(),
                ElectricalBusState(
                    source_available={},
                    load_commanded_on={"UNKNOWN": True},
                ),
            )

    def test_duplicate_ids_and_negative_power_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate electrical source"):
            ElectricalBusConfig(
                bus_id="BUS",
                sources=(
                    ElectricalSourceSpec("S", 1.0),
                    ElectricalSourceSpec("S", 2.0),
                ),
                loads=(),
            ).validated()

        with self.assertRaisesRegex(ValueError, "non-negative"):
            ElectricalLoadSpec("bad", -1.0).validated()


if __name__ == "__main__":
    unittest.main()
