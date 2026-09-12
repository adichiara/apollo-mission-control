"""Station-specific controller product projections for the Apollo 13 PC+2 slice.

This module projects modeled scenario state into controller-facing information.
It intentionally keeps project implementation gaps separate from historical
telemetry validity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .pc2_nominal import PC2State, Product, Validity


@dataclass
class ProjectionSet:
    station: str
    products: dict[str, Product] = field(default_factory=dict)
    deferred_fields: tuple[str, ...] = ()


def _live_product(state: PC2State, value: Any, *, units: str | None = None,
                  source_layer: str, provenance: str,
                  validity: Validity = Validity.VALID) -> Product:
    """Create a nominal zero-delay live product.

    Equal source/sample/receive/display times are a prototype transport
    simplification, not a claim about Apollo CRT refresh cadence.
    """
    return Product(
        value=value, units=units,
        source_time_get=state.get_s, sample_time_get=state.get_s,
        receive_time_get=state.get_s, process_time_get=state.get_s,
        display_time_get=state.get_s, validity=validity,
        provenance=provenance, source_layer=source_layer,
    )


def _reference_product(value: Any, *, units: str | None = None,
                       source_layer: str, provenance: str) -> Product:
    """Create a static/reference product without asserting a live sample time."""
    return Product(value=value, units=units, validity=Validity.VALID,
                   provenance=provenance, source_layer=source_layer)


def project_controller_products(state: PC2State, fixture: dict[str, Any]) -> dict[str, ProjectionSet]:
    """Project authoritative/modelled state into the minimum PC+2 station set."""
    target = fixture["pc2_target"]
    pgns = fixture["pgns"]
    comm = fixture["communications"]
    lm_power = fixture["lm_power"]
    dps = fixture["dps"]
    vehicle_control = fixture["vehicle_control"]

    residual_validity = Validity.VALID if state.residual_review_complete else Validity.UNAVAILABLE
    residual_value = pgns["nominal_postburn_residual_fps"] if state.residual_review_complete else None

    power_mode = "low_power"
    if state.burn_powered:
        power_mode = "burn_configuration"
    if state.powerdown_started:
        power_mode = "powerdown_transition"

    control_products = {
        "dps.engine_running": _live_product(state, state.engine_running, source_layer="physical/control", provenance="pc2.state.dps.engine_running"),
        "dps.throttle_command_phase": _live_product(state, state.throttle_phase, source_layer="command", provenance="pc2.state.dps.throttle_command"),
        "rcs.ullage_active": _live_product(state, state.ullage_active, source_layer="physical/control", provenance="pc2.state.rcs.ullage"),
        "rcs.ullage_jets_count": _live_product(state, state.ullage_jets_count, source_layer="physical/control", provenance="pc2.state.rcs.ullage"),
        "dps.engine_gimbal_warning": _live_product(state, dps["engine_gimbal_warning"], source_layer="onboard/telemetry", provenance="pc2.fixture.dps.engine_gimbal_warning"),
        "ces.dc_failure": _live_product(state, vehicle_control["ces_dc_failure"], source_layer="onboard/telemetry", provenance="pc2.fixture.vehicle_control.ces_dc_failure"),
    }
    control_deferred = [
        "dps.inlet_pressure_psi",
        "vehicle.attitude_error_xyz_deg",
        "vehicle.body_rate_xyz_deg_s",
    ]
    if state.dps_chamber_pressure_psi is None:
        # Project-model gap, not a claim that Apollo telemetry was unavailable.
        control_deferred.insert(0, "dps.chamber_pressure_psi")
    else:
        control_products["dps.chamber_pressure_psi"] = _live_product(
            state,
            state.dps_chamber_pressure_psi,
            units="psi",
            source_layer="measurement/telemetry",
            provenance="LM-7-family GQ6510P thrust-chamber-pressure measurement",
        )

    if state.dps_fuel_oxidizer_delta_p_psi is None:
        control_deferred.append("dps.fuel_oxidizer_delta_p_psi")
    else:
        control_products["dps.fuel_oxidizer_delta_p_psi"] = _live_product(
            state,
            state.dps_fuel_oxidizer_delta_p_psi,
            units="psi",
            source_layer="ground-derived/propulsion-monitoring",
            provenance=(
                "Apollo 13 PC+2 ground fuel/oxidizer delta-P product; "
                "exact LM-measurement transformation/routing unresolved"
            ),
        )

    control = ProjectionSet(
        station="CONTROL",
        products=control_products,
        deferred_fields=tuple(control_deferred),
    )

    guido = ProjectionSet(
        station="GUIDO",
        products={
            "pg_ns.lgc.operating": _live_product(state, pgns["lgc_operating"], source_layer="onboard/telemetry", provenance="pc2.fixture.pgns.lgc_operating"),
            "pg_ns.lgc.program": _live_product(state, "P40" if state.p40_active else pgns["program"], source_layer="onboard/telemetry", provenance="pc2.state.pgns.program"),
            "pg_ns.lgc.program_alarm": _live_product(state, pgns["program_alarm"], source_layer="onboard/telemetry", provenance="pc2.fixture.pgns.program_alarm"),
            "pg_ns.iss.warning": _live_product(state, pgns["iss_warning"], source_layer="onboard/telemetry", provenance="pc2.fixture.pgns.iss_warning"),
            "pg_ns.lgc.warning": _live_product(state, pgns["lgc_warning"], source_layer="onboard/telemetry", provenance="pc2.fixture.pgns.lgc_warning"),
            "pg_ns.alignment.accepted": _reference_product(pgns["alignment_accepted"], source_layer="onboard/ground_assessment", provenance="pc2.fixture.pgns.alignment_accepted"),
            "pg_ns.state_vector_load_status": _reference_product(pgns["state_vector_load_status"], source_layer="onboard/uplink", provenance="pc2.fixture.pgns.state_vector_load_status"),
            "pg_ns.target_load_status": _reference_product(pgns["target_load_status"], source_layer="onboard/uplink", provenance="pc2.fixture.pgns.target_load_status"),
            "pg_ns.vg_imu_planned": _reference_product(pgns["planned_vg_imu_fps"], units="ft/s", source_layer="onboard/target", provenance="pc2.fixture.pgns.planned_vg_imu_fps"),
            "pg_ns.postburn_residual": _live_product(state, residual_value, units="ft/s", source_layer="onboard/telemetry", provenance="pc2.fixture.pgns.nominal_postburn_residual_fps", validity=residual_validity),
        },
        deferred_fields=("pg_ns.vg_remaining", "pg_ns.dv_gained", "ags.ullage_display", "ags.actual_velocity_display", "pg_ns.iss.warning_exact_lm7_telemetry_word", "pg_ns.iss.warning_exact_guido_crt_field"),
    )

    fido_retro = ProjectionSet(
        station="FIDO_RETRO",
        products={
            "ground.pc2.tig_get_s": _reference_product(target["tig_get_s"], units="s GET", source_layer="ground-derived", provenance="pc2.fixture.pc2_target.tig_get_s"),
            "ground.pc2.pad_dv_lvlh": _reference_product(target["pad_dv_lvlh_fps"], units="ft/s", source_layer="ground-derived", provenance="pc2.fixture.pc2_target.pad_dv_lvlh_fps"),
            "ground.pc2.expected_perigee_nmi": _reference_product(target["expected_perigee_nmi"], units="nmi", source_layer="ground-derived", provenance="pc2.fixture.pc2_target.expected_perigee_nmi"),
            "ground.return.plan": _reference_product(fixture["return_products"], source_layer="ground-derived", provenance="pc2.fixture.return_products"),
            "ground.rtcc.solution_valid": _live_product(state, True, source_layer="ground-derived", provenance="pc2.nominal.rtcc.solution_valid"),
        },
        deferred_fields=("ground.rtcc.cartesian_state_vector", "ground.postburn.propagated_trajectory"),
    )

    telmu = ProjectionSet(
        station="TELMU",
        products={
            "lm.power.mode": _live_product(state, power_mode, source_layer="physical/configuration", provenance="pc2.state.lm.power.mode"),
            "lm.power.burn_configuration_expected_current_range_a": _reference_product(lm_power["burn_configuration_current_expected_range_a"], units="A", source_layer="mission-report/reference", provenance="pc2.fixture.lm_power.burn_configuration_current_expected_range_a"),
            "lm.inverter_warning": _live_product(state, lm_power["inverter_warning"], source_layer="onboard/telemetry", provenance="pc2.fixture.lm_power.inverter_warning"),
            "lm.powerdown.started": _live_product(state, state.powerdown_started, source_layer="physical/configuration", provenance="pc2.state.lm.powerdown"),
        },
        deferred_fields=("lm.power.current_a",),
    )

    inco = ProjectionSet(
        station="INCO",
        products={
            "comm.air_ground_quality": _live_product(state, state.comm_quality, source_layer="communications", provenance="pc2.state.comm.air_ground_quality"),
            "comm.voice_available": _live_product(state, comm["voice_available"], source_layer="communications", provenance="pc2.fixture.communications.voice_available"),
            "comm.telemetry_available": _live_product(state, comm["telemetry_available"], source_layer="communications", provenance="pc2.fixture.communications.telemetry_available"),
            "comm.ranging_enabled": _live_product(state, state.ranging_enabled, source_layer="communications/navigation", provenance="pc2.state.comm.ranging"),
            "comm.uplink_state": _reference_product(comm["uplink_available"], source_layer="communications/command", provenance="pc2.fixture.communications.uplink_available"),
        },
    )

    flight = ProjectionSet(
        station="FLIGHT",
        products={
            "mission.phase": _live_product(state, state.phase, source_layer="mission/session", provenance="pc2.state.phase"),
            "flight.go_for_burn": _live_product(state, state.flight_go, source_layer="controller-decision", provenance="pc2.state.flight.go_for_burn"),
        },
        deferred_fields=("controller.readiness_reports",),
    )

    capcom = ProjectionSet(
        station="CAPCOM",
        products={
            "comm.air_ground_quality": _live_product(state, state.comm_quality, source_layer="communications", provenance="pc2.state.comm.air_ground_quality"),
            "ground.pc2.final_pad": _reference_product({"tig_get_s": target["tig_get_s"], "pad_dv_lvlh_fps": target["pad_dv_lvlh_fps"], "expected_perigee_nmi": target["expected_perigee_nmi"], "ullage": target["ullage"], "throttle_profile": target["throttle_profile"]}, source_layer="ground-derived/procedure", provenance="pc2.fixture.pc2_target"),
            "crew.report_stream": _live_product(state, [{"get_s": report.get_s, "report": report.report} for report in state.crew_reports], source_layer="crew-report", provenance="pc2.state.crew_reports"),
        },
    )

    return {projection.station: projection for projection in (control, guido, fido_retro, telmu, inco, flight, capcom)}
