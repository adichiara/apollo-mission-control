from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_decisions import (  # noqa: E402
    ControllerDecisionType,
    call_out_shutdown_criterion,
)
from apollo_mission_control.controller_products import project_controller_products  # noqa: E402
from apollo_mission_control.operational_actions import (  # noqa: E402
    OperationalAction,
    apply_operational_action,
)
from apollo_mission_control.pc2_nominal import PC2State, load_fixture  # noqa: E402
from apollo_mission_control.procedural_exchange import (  # noqa: E402
    ProcedureExchangeLog,
    record_delta_p_shutdown_callout,
)
from apollo_mission_control.shutdown_rules import RuleState, evaluate_pc2_shutdown_rules  # noqa: E402


FIXTURE = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")


class DeltaPGroundCalloutTests(unittest.TestCase):
    def _state_with_delta_p(self, value: float) -> PC2State:
        state = PC2State(get_s=286200.0, engine_running=True, throttle_phase="maximum")
        state.dps_fuel_oxidizer_delta_p_psi = value
        state.dps_fuel_oxidizer_delta_p_observed_get_s = state.get_s
        return state

    def test_exactly_25_psi_does_not_trigger(self):
        state = self._state_with_delta_p(25.0)
        projections = project_controller_products(state, FIXTURE)
        rules = evaluate_pc2_shutdown_rules(projections, FIXTURE)
        self.assertEqual(rules["fuel_oxidizer_delta_p"].state, RuleState.CLEAR)

    def test_26_psi_flows_through_decision_callout_and_crew_command(self):
        state = self._state_with_delta_p(26.0)
        projections = project_controller_products(state, FIXTURE)
        rules = evaluate_pc2_shutdown_rules(projections, FIXTURE)

        self.assertEqual(rules["fuel_oxidizer_delta_p"].state, RuleState.TRIGGERED)

        decision = call_out_shutdown_criterion(
            get_s=state.get_s,
            station="CONTROL",
            product_name="dps.fuel_oxidizer_delta_p_psi",
            basis="fuel/oxidizer differential pressure >25 psi; ground callout only",
        )
        self.assertEqual(decision.decision, ControllerDecisionType.CALL_OUT_SHUTDOWN_CRITERION)

        log = ProcedureExchangeLog()
        record_delta_p_shutdown_callout(
            log,
            event_id="synthetic-delta-p-callout",
            get_s=state.get_s + 1.0,
            delta_p_psi=26.0,
            provenance="synthetic boundary test; 26 psi is not a historical Apollo 13 measurement",
        )
        self.assertEqual(len(log.events), 1)
        self.assertEqual(log.events[0].sender, "CAPCOM")
        self.assertEqual(log.events[0].recipient, "CREW")
        self.assertEqual(log.events[0].kind, "callout")

        apply_operational_action(
            state,
            OperationalAction(
                action_id="synthetic-crew-dps-shutdown",
                get_s=state.get_s + 2.0,
                actor="CREW",
                action="command_dps_shutdown",
                parameters={"criterion": "fuel_oxidizer_delta_p"},
                provenance="synthetic boundary test based on PC+2 ground-callout shutdown rule",
            ),
        )
        self.assertTrue(state.crew_dps_shutdown_commanded)
        self.assertTrue(state.engine_running)

    def test_callout_helper_does_not_encode_internal_approval_sequence(self):
        log = ProcedureExchangeLog()
        record_delta_p_shutdown_callout(
            log,
            event_id="synthetic-delta-p-callout",
            get_s=1.0,
            delta_p_psi=26.0,
            provenance="test",
        )
        event = log.events[0]
        self.assertEqual(event.parameters["origin_discipline"], "CONTROL")
        self.assertNotIn("flight_approval", event.parameters)


if __name__ == "__main__":
    unittest.main()
