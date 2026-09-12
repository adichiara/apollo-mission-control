import unittest
from dataclasses import dataclass

from apollo_mission_control.event_eligibility import (
    EventEligibilityRule,
    StateRequirement,
    evaluate_event_eligibility,
)


@dataclass
class State:
    ready: bool = False
    mode: str = "idle"


class EventEligibilityTests(unittest.TestCase):
    def test_event_without_rule_is_eligible(self):
        self.assertEqual(evaluate_event_eligibility(State(), "unruled", {}), (True, None))

    def test_all_declared_requirements_must_match(self):
        rules = {
            "event": EventEligibilityRule(
                "event",
                (
                    StateRequirement("ready", True, "system ready"),
                    StateRequirement("mode", "armed", "mode armed"),
                ),
            )
        }

        eligible, reason = evaluate_event_eligibility(State(ready=True, mode="idle"), "event", rules)
        self.assertFalse(eligible)
        self.assertIn("mode armed", reason)

        eligible, reason = evaluate_event_eligibility(State(ready=True, mode="armed"), "event", rules)
        self.assertTrue(eligible)
        self.assertIsNone(reason)


if __name__ == "__main__":
    unittest.main()
