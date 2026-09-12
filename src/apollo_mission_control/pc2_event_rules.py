"""Declarative eligibility rules for Apollo 13 PC+2 nominal milestones."""

from __future__ import annotations

from .event_eligibility import EventEligibilityRule, StateRequirement


def _req(path: str, description: str) -> StateRequirement:
    return StateRequirement(path=path, expected=True, description=description)


PC2_EVENT_RULES: dict[str, EventEligibilityRule] = {
    "p40_active_final_preburn": EventEligibilityRule(
        "p40_active_final_preburn",
        (_req("flight_go", "FLIGHT GO recorded"),),
    ),
    "manual_two_jet_ullage_begins": EventEligibilityRule(
        "manual_two_jet_ullage_begins",
        (
            _req("flight_go", "FLIGHT GO recorded"),
            _req("p40_active", "P40 active"),
        ),
    ),
    "dps_ignition": EventEligibilityRule(
        "dps_ignition",
        (
            _req("flight_go", "FLIGHT GO recorded"),
            _req("p40_active", "P40 active"),
            _req("ullage_active", "nominal ullage active"),
        ),
    ),
    "throttle_command_40_percent": EventEligibilityRule(
        "throttle_command_40_percent",
        (_req("engine_running", "DPS engine running"),),
    ),
    "crew_reports_40_percent": EventEligibilityRule(
        "crew_reports_40_percent",
        (_req("engine_running", "DPS engine running"),),
    ),
    "throttle_command_maximum": EventEligibilityRule(
        "throttle_command_maximum",
        (_req("engine_running", "DPS engine running"),),
    ),
    "crew_reports_100_percent": EventEligibilityRule(
        "crew_reports_100_percent",
        (_req("engine_running", "DPS engine running"),),
    ),
    "guided_cutoff": EventEligibilityRule(
        "guided_cutoff",
        (_req("engine_running", "DPS engine running"),),
    ),
    "postburn_residual_review": EventEligibilityRule(
        "postburn_residual_review",
        (_req("cutoff_complete", "nominal cutoff complete"),),
    ),
    "lm_powerdown_transition": EventEligibilityRule(
        "lm_powerdown_transition",
        (_req("cutoff_complete", "nominal cutoff complete"),),
    ),
}
