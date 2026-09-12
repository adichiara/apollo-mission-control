"""PC+2 shutdown-rule audit evaluation.

Rule results are derived audit objects. They do not command a shutdown and are
not exposed as an omniscient burn-abort flag to flight controllers.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from .controller_products import ProjectionSet


class RuleState(str, Enum):
    CLEAR = "clear"
    TRIGGERED = "triggered"
    NOT_EVALUABLE = "not_evaluable"
    NOT_APPLICABLE = "not_applicable"


@dataclass(frozen=True)
class RuleEvaluation:
    rule_id: str
    state: RuleState
    owner: str
    basis: str
    observation: Any = None


def evaluate_pc2_shutdown_rules(
    projections: dict[str, ProjectionSet],
    fixture: dict[str, Any],
) -> dict[str, RuleEvaluation]:
    """Evaluate only PC+2 criteria supported by currently modeled observations.

    Missing project-model values produce NOT_EVALUABLE, not CLEAR and not a
    simulated telemetry failure.
    """
    control = projections["CONTROL"]
    guido = projections["GUIDO"]
    telmu = projections["TELMU"]

    def deferred(rule_id: str, owner: str, basis: str) -> RuleEvaluation:
        return RuleEvaluation(rule_id, RuleState.NOT_EVALUABLE, owner, basis)

    results: dict[str, RuleEvaluation] = {}

    chamber_product = control.products.get("dps.chamber_pressure_psi")
    if chamber_product is None:
        results["ground_chamber_pressure"] = deferred("ground_chamber_pressure", "CONTROL", "ground chamber pressure <= 85 psi")
    else:
        chamber_pressure = float(chamber_product.value)
        threshold = float(fixture["shutdown_rules"]["ground_chamber_pressure_min_psi"])
        results["ground_chamber_pressure"] = RuleEvaluation(
            "ground_chamber_pressure", RuleState.TRIGGERED if chamber_pressure <= threshold else RuleState.CLEAR,
            "CONTROL", "ground chamber pressure <= 85 psi",
            observation={"pressure_psi": chamber_pressure, "threshold_psi": threshold},
        )

    results["crew_thrust_monitor"] = deferred("crew_thrust_monitor", "CREW/CAPCOM", "onboard thrust monitor <= 77 percent")
    results["ground_inlet_pressure"] = deferred("ground_inlet_pressure", "CONTROL", "ground engine inlet pressure <= 150 psi")
    results["crew_inlet_pressure"] = deferred("crew_inlet_pressure", "CREW/CAPCOM", "onboard engine inlet pressure <= 160 psi")

    delta_p_product = control.products.get("dps.fuel_oxidizer_delta_p_psi")
    if delta_p_product is None:
        results["fuel_oxidizer_delta_p"] = deferred("fuel_oxidizer_delta_p", "CONTROL", "fuel/oxidizer differential pressure > 25 psi; ground callout only")
    else:
        delta_p = float(delta_p_product.value)
        threshold = float(fixture["shutdown_rules"]["fuel_oxidizer_delta_p_max_psi"])
        results["fuel_oxidizer_delta_p"] = RuleEvaluation(
            "fuel_oxidizer_delta_p", RuleState.TRIGGERED if delta_p > threshold else RuleState.CLEAR,
            "CONTROL", "fuel/oxidizer differential pressure > 25 psi; ground callout only",
            observation={"delta_p_psi": delta_p, "threshold_psi": threshold},
        )

    results["attitude_error"] = deferred("attitude_error", "CONTROL/GUIDO", "absolute attitude error approximately 10 deg limit; startup wording unresolved")
    results["attitude_rate"] = deferred("attitude_rate", "CONTROL", "absolute attitude rate approximately 10 deg/s limit; startup wording unresolved")

    gimbal = control.products["dps.engine_gimbal_warning"].value
    results["engine_gimbal_warning"] = RuleEvaluation("engine_gimbal_warning", RuleState.TRIGGERED if gimbal else RuleState.CLEAR, "CONTROL", "engine gimbal warning/light", observation=gimbal)

    program_alarm = guido.products["pg_ns.lgc.program_alarm"].value
    iss_warning = guido.products["pg_ns.iss.warning"].value
    results["iss_warning_plus_program_alarm"] = RuleEvaluation(
        "iss_warning_plus_program_alarm",
        RuleState.TRIGGERED if bool(iss_warning) and program_alarm is not None else RuleState.CLEAR,
        "GUIDO", "inertial-reference/ISS warning plus computer program alarm",
        observation={"program_alarm": program_alarm, "iss_warning": iss_warning},
    )

    lgc_warning = guido.products["pg_ns.lgc.warning"].value
    results["lgc_warning"] = RuleEvaluation("lgc_warning", RuleState.TRIGGERED if lgc_warning else RuleState.CLEAR, "GUIDO", "LM guidance computer warning", observation=lgc_warning)

    ces_failure = control.products["ces.dc_failure"].value
    results["ces_dc_failure"] = RuleEvaluation("ces_dc_failure", RuleState.TRIGGERED if ces_failure else RuleState.CLEAR, "CONTROL", "control electronics system DC power failure", observation=ces_failure)

    inverter_warning = bool(telmu.products["lm.inverter_warning"].value)
    switch_attempted = bool(telmu.products["lm.inverter_switch_attempted"].value)
    switch_get = telmu.products["lm.inverter_switch_attempt_get_s"].value
    if not inverter_warning:
        inverter_state = RuleState.CLEAR
    elif not switch_attempted:
        inverter_state = RuleState.NOT_EVALUABLE
    else:
        # No invented persistence timer: the rule is satisfied when the modeled
        # warning is still present in the post-switch state.
        inverter_state = RuleState.TRIGGERED
    results["persistent_inverter_warning"] = RuleEvaluation(
        "persistent_inverter_warning", inverter_state, "TELMU/CONTROL",
        "inverter warning remaining after switching inverters",
        observation={"warning": inverter_warning, "switch_attempted": switch_attempted, "switch_get_s": switch_get},
    )

    return results


def triggered_rules(evaluations: dict[str, RuleEvaluation]) -> list[RuleEvaluation]:
    return [item for item in evaluations.values() if item.state == RuleState.TRIGGERED]
