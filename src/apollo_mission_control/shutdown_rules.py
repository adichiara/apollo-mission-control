"""PC+2 shutdown-rule audit evaluation.

Rule results are derived audit objects. They do not command a shutdown and are
not exposed as an omniscient burn-abort flag to flight controllers.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from .attitude_monitoring import evaluate_attitude_error, evaluate_attitude_rate
from .controller_products import ProjectionSet
from .pc2_nominal import Product


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


def _observation_age(product: Product | None) -> float | None:
    if product is None or product.display_time_get is None:
        return None
    return product.age_at(product.display_time_get)


def evaluate_pc2_shutdown_rules(
    projections: dict[str, ProjectionSet],
    fixture: dict[str, Any],
    *,
    startup_transient_exception_active: bool | None = None,
) -> dict[str, RuleEvaluation]:
    """Evaluate only PC+2 criteria supported by currently modeled observations.

    Missing project-model values produce NOT_EVALUABLE, not CLEAR and not a
    simulated telemetry failure. Observation age is reported but no generic
    age-based stale cutoff is applied because no reviewed PC+2 source defines
    one. The attitude-error startup exception requires explicit context; this
    function never derives it from throttle phase or seconds since ignition.
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
            observation={"pressure_psi": chamber_pressure, "threshold_psi": threshold, "observation_age_s": _observation_age(chamber_product)},
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
            observation={"delta_p_psi": delta_p, "threshold_psi": threshold, "observation_age_s": _observation_age(delta_p_product)},
        )

    attitude_error_product = control.products.get("vehicle.attitude_error_xyz_deg")
    attitude_error = evaluate_attitude_error(
        None if attitude_error_product is None else attitude_error_product.value,
        threshold_deg=float(fixture["shutdown_rules"]["attitude_error_abs_max_deg"]),
        startup_transient_exception_active=startup_transient_exception_active,
    )
    results["attitude_error"] = RuleEvaluation(
        "attitude_error",
        RuleState(attitude_error.state.value),
        "CONTROL",
        attitude_error.basis,
        observation={
            "vector_deg": attitude_error.vector,
            "max_abs_deg": attitude_error.max_abs_value,
            "threshold_deg": attitude_error.threshold,
            "startup_transient_exception_active": startup_transient_exception_active,
            "observation_age_s": _observation_age(attitude_error_product),
        },
    )

    attitude_rate_product = control.products.get("vehicle.body_rate_xyz_deg_s")
    attitude_rate = evaluate_attitude_rate(
        None if attitude_rate_product is None else attitude_rate_product.value,
        threshold_deg_s=float(fixture["shutdown_rules"]["body_rate_abs_max_deg_s"]),
    )
    results["attitude_rate"] = RuleEvaluation(
        "attitude_rate",
        RuleState(attitude_rate.state.value),
        "CONTROL",
        attitude_rate.basis,
        observation={
            "vector_deg_s": attitude_rate.vector,
            "max_abs_deg_s": attitude_rate.max_abs_value,
            "threshold_deg_s": attitude_rate.threshold,
            "observation_age_s": _observation_age(attitude_rate_product),
        },
    )

    gimbal_product = control.products["dps.engine_gimbal_warning"]
    gimbal = gimbal_product.value
    results["engine_gimbal_warning"] = RuleEvaluation("engine_gimbal_warning", RuleState.TRIGGERED if gimbal else RuleState.CLEAR, "CONTROL", "engine gimbal warning/light", observation={"warning": gimbal, "observation_age_s": _observation_age(gimbal_product)})

    program_alarm_product = guido.products["pg_ns.lgc.program_alarm"]
    iss_warning_product = guido.products["pg_ns.iss.warning"]
    program_alarm = program_alarm_product.value
    iss_warning = iss_warning_product.value
    results["iss_warning_plus_program_alarm"] = RuleEvaluation(
        "iss_warning_plus_program_alarm",
        RuleState.TRIGGERED if bool(iss_warning) and program_alarm is not None else RuleState.CLEAR,
        "GUIDO", "inertial-reference/ISS warning plus computer program alarm",
        observation={"program_alarm": program_alarm, "iss_warning": iss_warning, "iss_observation_age_s": _observation_age(iss_warning_product), "program_alarm_observation_age_s": _observation_age(program_alarm_product)},
    )

    lgc_warning_product = guido.products["pg_ns.lgc.warning"]
    lgc_warning = lgc_warning_product.value
    results["lgc_warning"] = RuleEvaluation("lgc_warning", RuleState.TRIGGERED if lgc_warning else RuleState.CLEAR, "GUIDO", "LM guidance computer warning", observation={"warning": lgc_warning, "observation_age_s": _observation_age(lgc_warning_product)})

    ces_product = control.products["ces.dc_failure"]
    ces_failure = ces_product.value
    results["ces_dc_failure"] = RuleEvaluation("ces_dc_failure", RuleState.TRIGGERED if ces_failure else RuleState.CLEAR, "CONTROL", "control electronics system DC power failure", observation={"failure": ces_failure, "observation_age_s": _observation_age(ces_product)})

    inverter_product = telmu.products["lm.inverter_warning"]
    inverter_warning = bool(inverter_product.value)
    warning_observed_get = inverter_product.source_time_get
    switch_attempted = bool(telmu.products["lm.inverter_switch_attempted"].value)
    switch_get = telmu.products["lm.inverter_switch_attempt_get_s"].value

    if not inverter_warning:
        inverter_state = RuleState.CLEAR
    elif not switch_attempted or switch_get is None:
        inverter_state = RuleState.NOT_EVALUABLE
    elif warning_observed_get is None or warning_observed_get <= float(switch_get):
        inverter_state = RuleState.NOT_EVALUABLE
    else:
        inverter_state = RuleState.TRIGGERED

    results["persistent_inverter_warning"] = RuleEvaluation(
        "persistent_inverter_warning", inverter_state, "TELMU/CONTROL",
        "inverter warning remaining after switching inverters",
        observation={
            "warning": inverter_warning,
            "warning_observed_get_s": warning_observed_get,
            "warning_observation_age_s": _observation_age(inverter_product),
            "switch_attempted": switch_attempted,
            "switch_get_s": switch_get,
        },
    )

    return results


def triggered_rules(evaluations: dict[str, RuleEvaluation]) -> list[RuleEvaluation]:
    return [item for item in evaluations.values() if item.state == RuleState.TRIGGERED]
