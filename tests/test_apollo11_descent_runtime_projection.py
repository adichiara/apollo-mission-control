from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.apollo11_descent_runtime_projection import (  # noqa: E402
    project_apollo11_descent_runtime,
)
from apollo_mission_control.descent_decision_gate import (  # noqa: E402
    DescentControlMode,
    LandingRadarControllerState,
    Readiness,
    RelayState,
)
from apollo_mission_control.descent_decision_projection import (  # noqa: E402
    DescentDecisionProjectionConfig,
)
from apollo_mission_control.generic_runtime import GenericScenarioSession  # noqa: E402
from apollo_mission_control.guidance_computer_model import (  # noqa: E402
    GuidanceComputerState,
)
from apollo_mission_control.powered_descent_profiles import (  # noqa: E402
    get_powered_descent_phase_profile,
)


class Apollo11DescentRuntimeProjectionTests(unittest.TestCase):
    def fixture(self):
        return {
            "start_get_s": 0.0,
            "generic_runtime": {
                "stations": ["GUIDANCE", "CONTROL", "FLIGHT", "CAPCOM"],
                "initial_phase": "descent",
                "initial_variables": {},
                "station_views": {
                    "GUIDANCE": [],
                    "CONTROL": [],
                    "FLIGHT": [],
                    "CAPCOM": [],
                },
                "injectable_variables": [],
                "events": [
                    {
                        "get_s": 504.0,
                        "name": "landing_go_gate",
                        "gate": "landing_go",
                    }
                ],
            },
        }

    def session(self, *, decide=True, relay=True):
        session = GenericScenarioSession.create(self.fixture())
        session.assign_stations("guidance", ["GUIDANCE"])
        session.assign_stations("control", ["CONTROL"])
        session.assign_stations("flight", ["FLIGHT"])
        session.assign_stations("capcom", ["CAPCOM"])
        session.start()
        session.advance_to(504.0)
        session.submit_readiness(
            "guidance",
            ready=True,
            station="GUIDANCE",
        )
        session.submit_readiness(
            "control",
            ready=True,
            station="CONTROL",
        )
        if decide:
            session.record_flight_go(
                "flight",
                go=True,
                basis="explicit test decision",
            )
        if relay:
            item = session.queue_capcom_instruction(
                "capcom",
                action="landing_go",
                parameters={},
                basis="relay explicit FLIGHT decision",
            )
            session.transmit_capcom_item("capcom", item.item_id)
        return session

    def decision_config(self):
        return DescentDecisionProjectionConfig(
            gate_id="landing_go",
            capcom_go_action="landing_go",
            capcom_no_go_action="landing_no_go",
        )

    def project(
        self,
        session,
        *,
        products=None,
        guidance_state=None,
        mode=DescentControlMode.AUTOMATIC,
    ):
        return project_apollo11_descent_runtime(
            session=session,
            pdi_get_s=0.0,
            phase_profile=get_powered_descent_phase_profile(
                "apollo11_g_powered_descent_phase_skeleton"
            ),
            landing_radar=LandingRadarControllerState(
                range_data_good=True,
                velocity_data_good=True,
                antenna_position=2,
                body_axis_velocity_fps=(10.0, -2.0, 1.0),
                slant_range_ft=7600.0,
                pgns_altitude_ft=7550.0,
                time_to_go_s=214.0,
            ),
            controller_product_values=(
                {
                    "lr.range_data_good": True,
                    "lr.velocity_data_good": True,
                    "lr.slant_range_ft": 7600.0,
                    "pgns.altitude_ft": 7550.0,
                    "control.lr_antenna_position": 2,
                }
                if products is None
                else products
            ),
            decision_config=self.decision_config(),
            guidance_computer_state=(
                GuidanceComputerState(
                    time_s=session.state.get_s,
                    active_program="P64",
                )
                if guidance_state is None
                else guidance_state
            ),
            control_mode=mode,
            provenance=("runtime projection unit test",),
        )

    def test_composes_phase_products_and_human_decision_chain(self):
        result = self.project(self.session())

        self.assertEqual(result.phase.phase.value, "approach")
        self.assertEqual(result.phase.most_recent_anchor.event_id, "high_gate")

        gate = result.decision_gate
        self.assertEqual(gate.guidance_readiness, Readiness.GO)
        self.assertEqual(gate.control_readiness, Readiness.GO)
        self.assertEqual(gate.flight_decision, Readiness.GO)
        self.assertEqual(gate.capcom_relay, RelayState.GO_RELAYED)

        products = result.controller_products
        self.assertTrue(products.product("lr.range_data_good").available)
        self.assertEqual(products.product("control.lr_antenna_position").value, 2)

        payload = result.to_dict()
        self.assertFalse(payload["human_decision_generated"])
        self.assertFalse(payload["controller_products_derived_from_hidden_state"])
        self.assertFalse(payload["session_mutated"])

    def test_station_go_calls_do_not_auto_create_flight_decision(self):
        session = self.session(decide=False, relay=False)
        result = self.project(session)
        self.assertEqual(result.decision_gate.guidance_readiness, Readiness.GO)
        self.assertEqual(result.decision_gate.control_readiness, Readiness.GO)
        self.assertEqual(result.decision_gate.flight_decision, Readiness.UNKNOWN)
        self.assertEqual(result.decision_gate.capcom_relay, RelayState.NOT_RELAYED)

    def test_guidance_alarm_state_does_not_backfill_controller_product(self):
        session = self.session()
        alarm_state = GuidanceComputerState(
            time_s=session.state.get_s,
            active_program="P63",
            program_alarm_active=True,
            active_alarm_code="1202",
            restart_count=1,
            recovery_status="restart_protected_program_resumed",
            alarm_history=("1202",),
        )
        result = self.project(
            session,
            products={"lr.range_data_good": True},
            guidance_state=alarm_state,
        )
        self.assertEqual(result.guidance_computer_state.active_alarm_code, "1202")
        alarm_product = result.controller_products.product("program.alarm_latest")
        self.assertFalse(alarm_product.available)
        self.assertIsNone(alarm_product.to_dict()["value"])

    def test_manual_control_changes_rule_authority_not_phase_or_products(self):
        session = self.session()
        automatic = self.project(session, mode=DescentControlMode.AUTOMATIC)
        manual = self.project(session, mode=DescentControlMode.MANUAL)

        self.assertEqual(automatic.phase.to_dict(), manual.phase.to_dict())
        self.assertEqual(
            automatic.controller_products.to_dict(),
            manual.controller_products.to_dict(),
        )
        self.assertTrue(
            automatic.decision_gate.trajectory_guidance_abort_constraints_applicable
        )
        self.assertFalse(
            manual.decision_gate.trajectory_guidance_abort_constraints_applicable
        )

    def test_projection_is_read_only(self):
        session = self.session()
        before = (
            session.state.get_s,
            session.state.phase,
            dict(session.state.variables),
            list(session.readiness_reports),
            list(session.audit_log),
            [
                (
                    item.item_id,
                    item.transmitted,
                    item.transmitted_get_s,
                )
                for item in session.capcom_queue
            ],
        )

        self.project(session)

        after = (
            session.state.get_s,
            session.state.phase,
            dict(session.state.variables),
            list(session.readiness_reports),
            list(session.audit_log),
            [
                (
                    item.item_id,
                    item.transmitted,
                    item.transmitted_get_s,
                )
                for item in session.capcom_queue
            ],
        )
        self.assertEqual(after, before)

    def test_future_guidance_state_is_rejected(self):
        session = self.session()
        with self.assertRaisesRegex(ValueError, "cannot be from the future"):
            self.project(
                session,
                guidance_state=GuidanceComputerState(
                    time_s=session.state.get_s + 1.0,
                    active_program="P64",
                ),
            )


if __name__ == "__main__":
    unittest.main()
