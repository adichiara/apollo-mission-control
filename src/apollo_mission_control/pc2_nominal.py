"""Minimal Apollo 13 PC+2 nominal domain prototype.

This module validates scenario/event architecture only. It does not yet claim
full spacecraft physics, RTCC dynamics, or historical CRT timing fidelity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import json
from typing import Any


class Validity(str, Enum):
    VALID = "valid"
    STALE = "stale"
    INVALID = "invalid"
    UNAVAILABLE = "unavailable"


@dataclass
class Product:
    value: Any
    units: str | None = None
    source_time_get: float | None = None
    sample_time_get: float | None = None
    receive_time_get: float | None = None
    process_time_get: float | None = None
    display_time_get: float | None = None
    validity: Validity = Validity.VALID
    source_layer: str = ""
    provenance: str = ""

    def age_at(self, get_s: float) -> float | None:
        """Return observation age without assigning a historical stale policy."""
        observed = self.sample_time_get
        if observed is None:
            observed = self.source_time_get
        if observed is None:
            return None
        return max(0.0, float(get_s) - float(observed))


@dataclass
class SimEvent:
    get_s: float
    name: str


@dataclass
class CrewReport:
    get_s: float
    report: str


@dataclass
class PC2State:
    get_s: float
    phase: str = "pc2_final_pad_link_weak"
    comm_quality: str = "weak"
    pad_transfer_complete: bool = False
    burn_powered: bool = False
    ranging_enabled: bool = False
    computer_with_crew: bool = False
    flight_go: bool = False
    p40_active: bool = False
    ullage_active: bool = False
    ullage_jets_count: int = 0
    engine_running: bool = False
    throttle_phase: str = "off"
    # Optional modeled observations. None means the project has not supplied a
    # numerical value; it is not a claim of telemetry/product loss.
    dps_chamber_pressure_psi: float | None = None
    dps_chamber_pressure_observed_get_s: float | None = None
    # Ground-derived PC+2 fuel/oxidizer differential-pressure product. The
    # exact transformation from LM source pressure measurements is unresolved.
    dps_fuel_oxidizer_delta_p_psi: float | None = None
    dps_fuel_oxidizer_delta_p_observed_get_s: float | None = None
    # Three-axis CONTROL-relevant guidance/control observations. The exact
    # LM-7 PCM assignments and CONTROL CRT fields remain unresolved; no nominal
    # time history is synthesized from the postflight maxima.
    attitude_error_xyz_deg: dict[str, float] | None = None
    attitude_error_observed_get_s: float | None = None
    body_rate_xyz_deg_s: dict[str, float] | None = None
    body_rate_observed_get_s: float | None = None
    # Runtime inverter caution observation. The exact PC+2 telemetry/display
    # route remains unresolved, but the caution-generation path is documented.
    lm_inverter_warning: bool = False
    lm_inverter_warning_observed_get_s: float | None = None
    # Operational action state, kept separate from fault/scenario injection.
    lm_inverter_switch_attempted: bool = False
    lm_inverter_switch_attempt_get_s: float | None = None
    # Source-backed PC+2 premature-shutdown restart actions. These fields record
    # crew actions/commands only; they do not force a successful engine restart.
    restart_manual_ullage_attempted: bool = False
    restart_manual_ullage_get_s: float | None = None
    engine_start_push_attempted: bool = False
    engine_start_push_get_s: float | None = None
    descent_engine_command_override_on: bool = False
    descent_engine_command_override_get_s: float | None = None
    # Ground-callout shutdown action. The mission rule establishes that the
    # crew should shut down for fuel/oxidizer Delta-P >25 psi after a ground
    # callout, but the exact cockpit control sequence is not asserted here.
    crew_dps_shutdown_commanded: bool = False
    crew_dps_shutdown_command_get_s: float | None = None
    crew_reports: list[CrewReport] = field(default_factory=list)
    cutoff_complete: bool = False
    residual_review_complete: bool = False
    powerdown_started: bool = False
    shutdown_rule_triggers: list[str] = field(default_factory=list)


def hms_to_seconds(value: str) -> float:
    raw = value.rstrip("~+")
    h, m, s = raw.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def load_fixture(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_events(fixture: dict[str, Any]) -> list[SimEvent]:
    events = []
    for item in fixture["events"]:
        get_hms = item["get_hms"]
        events.append(SimEvent(hms_to_seconds(get_hms), item["event"]))
    return sorted(events, key=lambda e: e.get_s)


def apply_event(state: PC2State, event: SimEvent, fixture: dict[str, Any]) -> None:
    state.get_s = event.get_s
    name = event.name

    if name == "scenario_start_weak_link":
        state.phase = "pc2_final_pad_link_weak"
        state.comm_quality = "weak"
    elif name == "final_p30_lm_pad_readup_begins":
        state.phase = "pc2_final_pad_transfer"
    elif name == "communications_loud_and_clear_after_sband_change":
        state.comm_quality = "good"
        state.pad_transfer_complete = True
    elif name == "lm_burn_configuration_powerup":
        state.phase = "pc2_burn_configuration_powerup"
        state.burn_powered = True
    elif name == "ranging_switch_verification_requested":
        state.phase = "pc2_final_ground_computer_support"
        state.ranging_enabled = True
    elif name == "computer_returned_to_crew":
        state.computer_with_crew = True
        state.phase = "pc2_final_readiness"
    elif name == "final_go_no_go_poll":
        state.flight_go = True
        state.phase = "pc2_go_for_burn"
    elif name == "p40_active_final_preburn":
        state.p40_active = True
        state.phase = "pc2_p40_preignition"
    elif name == "manual_two_jet_ullage_begins":
        state.ullage_active = True
        state.ullage_jets_count = int(fixture["pc2_target"]["ullage"]["jets"])
        state.phase = "pc2_ullage"
    elif name == "dps_ignition":
        state.ullage_active = False
        state.ullage_jets_count = 0
        state.engine_running = True
        state.throttle_phase = "minimum"
        state.phase = "pc2_dps_start_minimum_thrust"
    elif name == "throttle_command_40_percent":
        state.throttle_phase = "40_percent"
        state.phase = "pc2_40_percent_thrust"
    elif name == "crew_reports_40_percent":
        state.crew_reports.append(CrewReport(event.get_s, "40_percent"))
    elif name == "throttle_command_maximum":
        state.throttle_phase = "maximum"
        state.phase = "pc2_full_thrust"
    elif name == "crew_reports_100_percent":
        state.crew_reports.append(CrewReport(event.get_s, "100_percent"))
    elif name == "guided_cutoff":
        state.engine_running = False
        state.throttle_phase = "off"
        state.cutoff_complete = True
        state.phase = "pc2_guided_cutoff"
    elif name == "postburn_residual_review":
        state.residual_review_complete = True
        state.phase = "pc2_residual_review"
    elif name == "lm_powerdown_transition":
        state.powerdown_started = True
        state.phase = "pc2_postburn_powerdown"


def run_nominal(fixture: dict[str, Any]) -> PC2State:
    state = PC2State(
        get_s=float(fixture["start_get_s"]),
        lm_inverter_warning=bool(fixture["lm_power"]["inverter_warning"]),
    )
    for event in build_events(fixture):
        apply_event(state, event, fixture)
    return state


def validate_nominal(fixture: dict[str, Any], final_state: PC2State) -> list[str]:
    errors: list[str] = []
    expected = fixture["nominal_validation"]
    events = {event.name: event.get_s for event in build_events(fixture)}

    actual_cutoff = float(expected["actual_cutoff_get_s"])
    if "guided_cutoff" not in events:
        errors.append("Expected exactly one guided_cutoff event.")
    elif abs(events["guided_cutoff"] - actual_cutoff) > 1e-6:
        errors.append("Guided cutoff event does not match historical fixture.")

    tig = float(fixture["pc2_target"]["tig_get_s"])
    expected_profile = {
        "manual_two_jet_ullage_begins": tig - 10.0,
        "dps_ignition": tig,
        "throttle_command_40_percent": tig + 5.0,
        "throttle_command_maximum": tig + 26.0,
    }
    for event_name, expected_time in expected_profile.items():
        if event_name not in events:
            errors.append(f"Missing required nominal event: {event_name}.")
        elif abs(events[event_name] - expected_time) > 1e-6:
            errors.append(f"Unexpected timing for nominal event: {event_name}.")

    if final_state.shutdown_rule_triggers:
        errors.append("Nominal run triggered a shutdown rule.")
    if not final_state.cutoff_complete:
        errors.append("Nominal run never reached guided cutoff.")
    if not final_state.residual_review_complete:
        errors.append("Nominal run never reached residual review.")
    if not final_state.powerdown_started:
        errors.append("Nominal run never entered post-burn powerdown.")

    reports = [(report.get_s, report.report) for report in final_state.crew_reports]
    expected_reports = [
        (hms_to_seconds("79:27:51"), "40_percent"),
        (hms_to_seconds("79:28:09"), "100_percent"),
    ]
    if reports != expected_reports:
        errors.append("Crew throttle reports do not match the nominal voice chronology.")

    pgns = fixture["pgns"]
    residual = pgns["nominal_postburn_residual_fps"]
    if residual != {"x": 1.0, "y": 0.3, "z": 0.0}:
        errors.append("Historical PGNS residual fixture changed unexpectedly.")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    fixture_path = root / "data" / "scenarios" / "apollo13_pc2_nominal.json"
    fixture = load_fixture(fixture_path)
    final_state = run_nominal(fixture)
    errors = validate_nominal(fixture, final_state)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PC+2 nominal fixture validated:", f"final_phase={final_state.phase}", f"GET={final_state.get_s:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
