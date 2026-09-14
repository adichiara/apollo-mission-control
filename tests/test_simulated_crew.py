from dataclasses import dataclass
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.simulated_crew import (  # noqa: E402
    CrewInstructionRule,
    SimulatedCrew,
)


@dataclass
class Item:
    item_id: int = 1
    action: str = "configure_system"
    parameters: dict = None
    basis: str = "test"
    transmitted: bool = True
    transmitted_get_s: float | None = 10.0

    def __post_init__(self):
        if self.parameters is None:
            self.parameters = {"mode": "A", "hidden": 99}


class SimulatedCrewTests(unittest.TestCase):
    def crew(self):
        return SimulatedCrew(
            crew_id="CREW",
            rules={
                "configure_system": CrewInstructionRule(
                    capcom_action="configure_system",
                    acknowledgement="Roger",
                    crew_action="set_system_mode",
                    forwarded_parameters=("mode",),
                    provenance="synthetic rule",
                )
            },
        )

    def test_receipt_and_action_are_separate(self):
        crew = self.crew()
        item = Item()

        receipt = crew.receive_instruction(item, get_s=10.0)
        self.assertEqual(receipt.acknowledgement, "Roger")
        self.assertNotIn(item.item_id, crew.actions)

        action = crew.perform_supported_action(item, get_s=10.0)
        self.assertEqual(action.action, "set_system_mode")
        self.assertEqual(action.parameters, {"mode": "A"})
        self.assertNotIn("hidden", action.parameters)

    def test_untransmitted_instruction_cannot_be_received(self):
        crew = self.crew()
        with self.assertRaisesRegex(ValueError, "untransmitted"):
            crew.receive_instruction(
                Item(transmitted=False, transmitted_get_s=None),
                get_s=10.0,
            )

    def test_receipt_cannot_precede_transmission(self):
        crew = self.crew()
        with self.assertRaisesRegex(ValueError, "precede"):
            crew.receive_instruction(Item(transmitted_get_s=10.0), get_s=9.0)

    def test_action_requires_receipt(self):
        crew = self.crew()
        with self.assertRaisesRegex(ValueError, "receipt"):
            crew.perform_supported_action(Item(), get_s=10.0)

    def test_no_response_delay_is_inserted(self):
        crew = self.crew()
        item = Item()
        receipt = crew.receive_instruction(item, get_s=10.0)
        action = crew.perform_supported_action(item, get_s=10.0)

        self.assertEqual(receipt.received_get_s, 10.0)
        self.assertEqual(action.get_s, 10.0)

    def test_caller_may_supply_later_action_time_without_actor_advancing_time(self):
        crew = self.crew()
        item = Item()
        crew.receive_instruction(item, get_s=11.5)
        action = crew.perform_supported_action(item, get_s=14.0)
        self.assertEqual(action.get_s, 14.0)

    def test_duplicate_receipt_and_action_are_rejected(self):
        crew = self.crew()
        item = Item()
        crew.receive_instruction(item, get_s=10.0)
        with self.assertRaisesRegex(ValueError, "already recorded"):
            crew.receive_instruction(item, get_s=10.0)

        crew.perform_supported_action(item, get_s=10.0)
        with self.assertRaisesRegex(ValueError, "already recorded"):
            crew.perform_supported_action(item, get_s=10.0)

    def test_unsupported_capcom_action_is_rejected(self):
        crew = self.crew()
        with self.assertRaisesRegex(ValueError, "unsupported"):
            crew.receive_instruction(
                Item(action="unknown_action"),
                get_s=10.0,
            )

    def test_missing_forwarded_parameter_is_rejected_only_when_action_occurs(self):
        crew = self.crew()
        item = Item(parameters={})
        crew.receive_instruction(item, get_s=10.0)
        with self.assertRaisesRegex(ValueError, "missing required parameter"):
            crew.perform_supported_action(item, get_s=10.0)

    def test_rule_key_must_match_capcom_action(self):
        with self.assertRaisesRegex(ValueError, "does not match"):
            SimulatedCrew(
                crew_id="CREW",
                rules={
                    "wrong": CrewInstructionRule(
                        capcom_action="actual",
                        acknowledgement="Roger",
                        crew_action="do_thing",
                    )
                },
            )


if __name__ == "__main__":
    unittest.main()
