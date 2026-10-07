"""Bounded Apollo 11 powered-descent runtime projection.

This module composes already-implemented domains without creating a second event
system or inferring controller decisions from hidden model state.

The projection reuses:
- GenericScenarioSession human/runtime artifacts;
- nominal powered-descent phase profiles;
- explicit Apollo 11 controller-product projection;
- descent decision-gate projection;
- guidance-computer alarm/restart state.

It is read-only. It does not advance a session, transmit CAPCOM traffic, derive
controller readiness, create FLIGHT decisions, or mutate spacecraft state.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Any, Mapping

from .apollo11_descent_products import (
    Apollo11DescentProductSet,
    project_apollo11_descent_products,
)
from .descent_decision_gate import (
    DescentControlMode,
    DescentDecisionGate,
    LandingRadarControllerState,
)
from .descent_decision_projection import (
    DescentDecisionProjectionConfig,
    project_generic_runtime_descent_gate,
)
from .generic_runtime import GenericScenarioSession
from .guidance_computer_model import GuidanceComputerState
from .powered_descent_phase import (
    PoweredDescentPhaseConfig,
    PoweredDescentPhaseSnapshot,
    evaluate_powered_descent_phase,
)


@dataclass(frozen=True)
class Apollo11DescentRuntimeProjection:
    get_s: float
    pdi_get_s: float
    tfi_s: float
    phase: PoweredDescentPhaseSnapshot
    controller_products: Apollo11DescentProductSet
    decision_gate: DescentDecisionGate
    guidance_computer_state: GuidanceComputerState
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "phase state is derived only from nominal powered-descent profile anchors",
        "controller products contain only explicitly supplied controller-visible values",
        "generic runtime readiness/FLIGHT/CAPCOM artifacts remain human-authored events",
        "guidance-computer state is supplied explicitly and is not auto-projected into controller products",
        "this projection is read-only and does not advance or mutate the session",
    )

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "apollo11_descent_runtime_projection",
            "get_s": self.get_s,
            "pdi_get_s": self.pdi_get_s,
            "tfi_s": self.tfi_s,
            "phase": self.phase.to_dict(),
            "controller_products": self.controller_products.to_dict(),
            "decision_gate": self.decision_gate.to_dict(),
            "guidance_computer_state": {
                "time_s": self.guidance_computer_state.time_s,
                "active_program": self.guidance_computer_state.active_program,
                "program_alarm_active": self.guidance_computer_state.program_alarm_active,
                "active_alarm_code": self.guidance_computer_state.active_alarm_code,
                "restart_count": self.guidance_computer_state.restart_count,
                "recovery_status": self.guidance_computer_state.recovery_status,
                "alarm_history": list(self.guidance_computer_state.alarm_history),
            },
            "human_decision_generated": False,
            "controller_products_derived_from_hidden_state": False,
            "session_mutated": False,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def project_apollo11_descent_runtime(
    *,
    session: GenericScenarioSession,
    pdi_get_s: float,
    phase_profile: PoweredDescentPhaseConfig,
    landing_radar: LandingRadarControllerState,
    controller_product_values: Mapping[str, Any],
    decision_config: DescentDecisionProjectionConfig,
    guidance_computer_state: GuidanceComputerState,
    control_mode: DescentControlMode = DescentControlMode.AUTOMATIC,
    field_provenance: Mapping[str, tuple[str, ...]] | None = None,
    provenance: tuple[str, ...] = (),
) -> Apollo11DescentRuntimeProjection:
    """Compose a read-only Apollo 11 descent snapshot from existing domains."""

    current_get = float(session.state.get_s)
    pdi = float(pdi_get_s)
    if not isfinite(current_get):
        raise ValueError("session GET must be finite")
    if not isfinite(pdi) or pdi < 0.0:
        raise ValueError("pdi_get_s must be finite and non-negative")

    checked_guidance = guidance_computer_state.validated()
    if checked_guidance.time_s > current_get:
        raise ValueError(
            "guidance_computer_state cannot be from the future relative to session GET"
        )

    tfi_s = current_get - pdi
    phase = evaluate_powered_descent_phase(tfi_s, phase_profile)

    products = project_apollo11_descent_products(
        controller_product_values,
        field_provenance=field_provenance,
        applicability=(
            "Apollo 11 powered-descent runtime projection; explicit controller-visible "
            "values only"
        ),
        provenance=tuple(provenance),
    )

    gate = project_generic_runtime_descent_gate(
        get_s=current_get,
        landing_radar=landing_radar,
        readiness_reports=session.readiness_reports,
        audit_events=session.audit_log,
        capcom_queue=session.capcom_queue,
        config=decision_config,
        control_mode=control_mode,
        provenance=tuple(provenance),
    )

    return Apollo11DescentRuntimeProjection(
        get_s=current_get,
        pdi_get_s=pdi,
        tfi_s=tfi_s,
        phase=phase,
        controller_products=products,
        decision_gate=gate,
        guidance_computer_state=checked_guidance,
        provenance=tuple(provenance),
    )
