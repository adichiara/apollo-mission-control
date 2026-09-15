from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import project_controller_products  # noqa: E402
from apollo_mission_control.operational_actions import OperationalAction, apply_operational_action  # noqa: E402
from apollo_mission_control.pc2_nominal import hms_to_seconds, load_fixture  # noqa: E402
from apollo_mission_control.procedural_exchange import (  # noqa: E402
    ProcedureExchangeLog,
    record_inverter_switch_completion,
    record_inverter_switch_instruction,
)
from apollo_mission_control.scenario_injection import (  # noqa: E402
    EvidenceClass,
    StateInjection,
    apply_state_injection,
    run_with_injections,
)
from apollo_mission_control.shutdown_rules import RuleState, evaluate_pc2_shutdown_rules  # noqa: E402


class InverterContingencyLoopTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(
            ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json"
        )

    def test_warning_switch_report_reobserve_loop(self):
        state = run_with_injections(
            self.fixture, [], stop_get_s=hms_to_seconds("79:29:00")
        )
        self.assertTrue(state.engine_running)

        # Synthetic, source-bounded crew warning report. This is not a claim
        # that Apollo 13 experienced an inverter fault during PC+2.
        apply_state_injection(
            state,
            StateInjection(
                injection_id="test-inverter-warning-pre-switch",
                get_s=hms_to_seconds("79:29:00"),
                target="crew_inverter_warning_report",
                value=True,
                evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                provenance="Synthetic observation for documented PC+2 inverter rule path.",
            ),
        )
        evaluations = evaluate_pc2_shutdown_rules(
            project_controller_products(state, self.fixture), self.fixture
        )
        self.assertEqual(
            evaluations["persistent_inverter_warning"].state,
            RuleState.NOT_EVALUABLE,
        )

        exchange = ProcedureExchangeLog()
        record_inverter_switch_instruction(
            exchange,
            event_id="capcom-switch-inverter",
            get_s=hms_to_seconds("79:29:01"),
            provenance="Source-bounded procedural test; inverter 2 to inverter 1 sequence sourced by Apollo 13 LM Malfunction Procedures.",
        )
        apply_operational_action(
            state,
            OperationalAction(
                action_id="crew-switch-inverter",
                get_s=hms_to_seconds("79:29:02"),
                actor="CREW",
                action="switch_lm_inverter",
                parameters={},
                provenance="Source-bounded procedural test; alternate inverter identity unresolved.",
            ),
        )
        record_inverter_switch_completion(
            exchange,
            event_id="crew-switch-complete",
            get_s=hms_to_seconds("79:29:03"),
            provenance="Synthetic completion report for the documented action sequence.",
        )

        # The original crew report alone is not enough after the switch. A distinct
        # post-switch crew report is required.
        evaluations = evaluate_pc2_shutdown_rules(
            project_controller_products(state, self.fixture), self.fixture
        )
        self.assertEqual(
            evaluations["persistent_inverter_warning"].state,
            RuleState.NOT_EVALUABLE,
        )

        apply_state_injection(
            state,
            StateInjection(
                injection_id="test-inverter-warning-post-switch",
                get_s=hms_to_seconds("79:29:04"),
                target="crew_inverter_warning_report",
                value=True,
                evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                provenance="Synthetic post-switch crew report; no persistence interval asserted.",
            ),
        )
        evaluations = evaluate_pc2_shutdown_rules(
            project_controller_products(state, self.fixture), self.fixture
        )
        self.assertEqual(
            evaluations["persistent_inverter_warning"].state,
            RuleState.TRIGGERED,
        )

        action_events = exchange.for_action("switch_lm_inverter")
        self.assertEqual([event.kind for event in action_events], ["instruction", "completion_report"])
        self.assertEqual(action_events[0].sender, "CAPCOM")
        self.assertEqual(action_events[1].sender, "CREW")
        self.assertEqual(action_events[0].parameters["from_inverter"], 2)
        self.assertEqual(action_events[0].parameters["to_inverter"], 1)
        self.assertEqual(
            action_events[0].parameters["control_sequence"],
            [
                "CB(11) EPS: INV 1 — close",
                "INVERTER — 1",
                "CB(16) EPS: INV 2 — open",
            ],
        )

        # Rule evaluation still does not issue an engine command or abort.
        self.assertTrue(state.engine_running)
        self.assertFalse(state.cutoff_complete)
        self.assertEqual(state.shutdown_rule_triggers, [])


if __name__ == "__main__":
    unittest.main()
