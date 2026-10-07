"""Reference probe for the bounded Apollo 11 descent runtime projection.

Cases are architecture demonstrations, not historical replay or validation.
They use the real GenericScenarioSession event/authority paths and then compose
the resulting artifacts with the Apollo 11 phase/product/alarm domains.
"""

from __future__ import annotations

from dataclasses import dataclass

from .apollo11_descent_runtime_projection import project_apollo11_descent_runtime
from .descent_decision_gate import (
    DescentControlMode,
    LandingRadarControllerState,
)
from .descent_decision_projection import DescentDecisionProjectionConfig
from .generic_runtime import GenericScenarioSession
from .guidance_computer_model import GuidanceComputerState
from .powered_descent_profiles import get_powered_descent_phase_profile


@dataclass(frozen=True)
class Apollo11DescentRuntimeProbeCase:
    case_id: str
    description: str
    projection: dict[str, object]

    def to_dict(self) -> dict[str, object]:
        return {
            "case_id": self.case_id,
            "description": self.description,
            "projection": self.projection,
        }


def _fixture(get_s: float) -> dict[str, object]:
    return {
        "start_get_s": 0.0,
        "generic_runtime": {
            "stations": ["GUIDANCE", "CONTROL", "FLIGHT", "CAPCOM"],
            "initial_phase": "apollo11_descent_reference",
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
                    "get_s": float(get_s),
                    "name": "landing_go_gate",
                    "gate": "landing_go",
                }
            ],
        },
    }


def _session(
    get_s: float,
    *,
    record_flight_decision: bool,
    transmit_relay: bool,
) -> GenericScenarioSession:
    session = GenericScenarioSession.create(_fixture(get_s))
    session.assign_stations("guidance-player", ["GUIDANCE"])
    session.assign_stations("control-player", ["CONTROL"])
    session.assign_stations("flight-player", ["FLIGHT"])
    session.assign_stations("capcom-player", ["CAPCOM"])
    session.start()
    session.advance_to(get_s)
    session.submit_readiness(
        "guidance-player",
        ready=True,
        station="GUIDANCE",
        note="synthetic architecture probe",
    )
    session.submit_readiness(
        "control-player",
        ready=True,
        station="CONTROL",
        note="synthetic architecture probe",
    )
    if record_flight_decision:
        session.record_flight_go(
            "flight-player",
            go=True,
            basis="synthetic architecture probe explicit FLIGHT decision",
        )
    if transmit_relay:
        item = session.queue_capcom_instruction(
            "capcom-player",
            action="landing_go",
            parameters={},
            basis="synthetic architecture probe explicit CAPCOM relay",
        )
        session.transmit_capcom_item("capcom-player", item.item_id)
    return session


def _projection(
    *,
    get_s: float,
    record_flight_decision: bool,
    transmit_relay: bool,
    control_mode: DescentControlMode,
    alarm_active: bool,
    expose_alarm_product: bool,
) -> dict[str, object]:
    session = _session(
        get_s,
        record_flight_decision=record_flight_decision,
        transmit_relay=transmit_relay,
    )
    products: dict[str, object] = {
        "lr.range_data_good": True,
        "lr.velocity_data_good": True,
        "lr.slant_range_ft": 7600.0 if get_s <= 504.0 else 500.0,
        "pgns.altitude_ft": 7550.0 if get_s <= 504.0 else 490.0,
        "control.lr_antenna_position": 2,
    }
    if expose_alarm_product:
        products["program.alarm_latest"] = "1202"

    guidance_state = GuidanceComputerState(
        time_s=get_s,
        active_program="P64" if get_s <= 608.0 else "P66",
        program_alarm_active=alarm_active,
        active_alarm_code="1202" if alarm_active else None,
        restart_count=1 if alarm_active else 0,
        recovery_status=(
            "restart_protected_program_resumed" if alarm_active else "normal"
        ),
        alarm_history=("1202",) if alarm_active else (),
    )

    result = project_apollo11_descent_runtime(
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
            slant_range_ft=float(products["lr.slant_range_ft"]),
            pgns_altitude_ft=float(products["pgns.altitude_ft"]),
            time_to_go_s=214.0,
        ),
        controller_product_values=products,
        decision_config=DescentDecisionProjectionConfig(
            gate_id="landing_go",
            capcom_go_action="landing_go",
            capcom_no_go_action="landing_no_go",
        ),
        guidance_computer_state=guidance_state,
        control_mode=control_mode,
        provenance=(
            "Apollo 11 bounded descent runtime architecture probe",
            "controller event timings/values in this probe are synthetic",
        ),
    )
    return result.to_dict()


def run_apollo11_descent_runtime_reference_probe() -> dict[str, object]:
    """Run bounded composition cases without claiming historical replay."""

    cases = (
        Apollo11DescentRuntimeProbeCase(
            case_id="high_gate_station_go_flight_undecided",
            description=(
                "Nominal high-gate phase with GUIDANCE/CONTROL GO but no FLIGHT "
                "decision or CAPCOM relay."
            ),
            projection=_projection(
                get_s=504.0,
                record_flight_decision=False,
                transmit_relay=False,
                control_mode=DescentControlMode.AUTOMATIC,
                alarm_active=False,
                expose_alarm_product=False,
            ),
        ),
        Apollo11DescentRuntimeProbeCase(
            case_id="high_gate_flight_go_capcom_relay",
            description=(
                "Same nominal high-gate phase with explicit FLIGHT GO and "
                "separate CAPCOM relay."
            ),
            projection=_projection(
                get_s=504.0,
                record_flight_decision=True,
                transmit_relay=True,
                control_mode=DescentControlMode.AUTOMATIC,
                alarm_active=False,
                expose_alarm_product=False,
            ),
        ),
        Apollo11DescentRuntimeProbeCase(
            case_id="manual_control_rule_authority",
            description=(
                "Landing-phase snapshot with explicit manual control; observations "
                "remain present while trajectory/guidance abort-rule authority changes."
            ),
            projection=_projection(
                get_s=650.0,
                record_flight_decision=True,
                transmit_relay=True,
                control_mode=DescentControlMode.MANUAL,
                alarm_active=False,
                expose_alarm_product=False,
            ),
        ),
        Apollo11DescentRuntimeProbeCase(
            case_id="alarm_not_backfilled_into_product",
            description=(
                "Active guidance-computer 1202 state while the controller-product "
                "alarm field is intentionally unsupplied."
            ),
            projection=_projection(
                get_s=550.0,
                record_flight_decision=False,
                transmit_relay=False,
                control_mode=DescentControlMode.AUTOMATIC,
                alarm_active=True,
                expose_alarm_product=False,
            ),
        ),
        Apollo11DescentRuntimeProbeCase(
            case_id="alarm_explicitly_supplied_to_product",
            description=(
                "Same active 1202 state with the controller-visible alarm field "
                "explicitly supplied through the product boundary."
            ),
            projection=_projection(
                get_s=550.0,
                record_flight_decision=False,
                transmit_relay=False,
                control_mode=DescentControlMode.AUTOMATIC,
                alarm_active=True,
                expose_alarm_product=True,
            ),
        ),
    )

    return {
        "model_status": "apollo11_descent_runtime_reference_probe",
        "scope": (
            "architecture composition only; controller event values/timings are "
            "synthetic and are not an Apollo 11 historical replay"
        ),
        "cases": [case.to_dict() for case in cases],
        "invariants": {
            "human_decisions_auto_generated": False,
            "hidden_state_auto_projected_to_controller_products": False,
            "probe_mutates_authoritative_live_session": False,
        },
    }
