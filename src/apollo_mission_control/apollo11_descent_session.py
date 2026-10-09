"""Apollo 11 powered-descent runtime adapter.

This adapter binds the shared GenericScenarioSession mechanics to the already
implemented read-only Apollo 11 descent projection. It does not make the
historical scenario executable and does not synthesize controller products,
readiness, FLIGHT decisions, or CAPCOM relays.
"""

from __future__ import annotations

from typing import Any, Mapping

from .apollo11_descent_runtime_projection import (
    Apollo11DescentRuntimeProjection,
    project_apollo11_descent_runtime,
)
from .descent_decision_gate import (
    DescentControlMode,
    LandingRadarControllerState,
)
from .descent_decision_projection import DescentDecisionProjectionConfig
from .generic_runtime import GenericScenarioSession
from .guidance_computer_model import GuidanceComputerState
from .powered_descent_phase import PoweredDescentPhaseConfig
from .powered_descent_profiles import get_powered_descent_phase_profile


def _nonempty_text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()


def _number(value: Any, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be numeric")
    return float(value)


class Apollo11DescentSession(GenericScenarioSession):
    """Generic Mission Control runtime plus a bound Apollo 11 projection."""

    def __init__(
        self,
        *,
        fixture: dict[str, Any],
        state: Any,
        events: list[Any],
        stations: tuple[str, ...],
        station_views: dict[str, tuple[str, ...]],
        injectable_variables: frozenset[str],
        pdi_get_s: float,
        phase_profile: PoweredDescentPhaseConfig,
        decision_config: DescentDecisionProjectionConfig,
    ) -> None:
        super().__init__(
            fixture=fixture,
            state=state,
            events=events,
            stations=stations,
            station_views=station_views,
            injectable_variables=injectable_variables,
        )
        self.pdi_get_s = float(pdi_get_s)
        self.phase_profile = phase_profile
        self.decision_config = decision_config.validated()

    @classmethod
    def create(cls, fixture: dict[str, Any]) -> "Apollo11DescentSession":
        raw = fixture.get("apollo11_descent_runtime")
        if not isinstance(raw, dict):
            raise ValueError(
                "apollo11_descent_v1 scenario requires an "
                "apollo11_descent_runtime object"
            )

        pdi_get_s = _number(raw.get("pdi_get_s"), "apollo11_descent_runtime pdi_get_s")
        if pdi_get_s < 0.0:
            raise ValueError("apollo11_descent_runtime pdi_get_s must be non-negative")

        phase_profile_id = _nonempty_text(
            raw.get("phase_profile_id"),
            "apollo11_descent_runtime phase_profile_id",
        )
        phase_profile = get_powered_descent_phase_profile(phase_profile_id)
        mission_profile_id = _nonempty_text(
            fixture.get("mission_profile_id"),
            "scenario mission_profile_id",
        )
        if phase_profile.mission_profile_id != mission_profile_id:
            raise ValueError(
                "Apollo 11 descent phase profile mission does not match scenario "
                f"mission profile: {phase_profile.mission_profile_id!r} != "
                f"{mission_profile_id!r}"
            )

        raw_decision = raw.get("decision_projection")
        if not isinstance(raw_decision, dict):
            raise ValueError(
                "apollo11_descent_runtime decision_projection must be an object"
            )
        decision_config = DescentDecisionProjectionConfig(
            gate_id=_nonempty_text(
                raw_decision.get("gate_id"),
                "decision_projection gate_id",
            ),
            capcom_go_action=_nonempty_text(
                raw_decision.get("capcom_go_action"),
                "decision_projection capcom_go_action",
            ),
            capcom_no_go_action=_nonempty_text(
                raw_decision.get("capcom_no_go_action"),
                "decision_projection capcom_no_go_action",
            ),
            guidance_station=_nonempty_text(
                raw_decision.get("guidance_station"),
                "decision_projection guidance_station",
            ),
            control_station=_nonempty_text(
                raw_decision.get("control_station"),
                "decision_projection control_station",
            ),
        ).validated()

        generic = GenericScenarioSession.create(fixture)
        if decision_config.guidance_station not in generic.available_stations:
            raise ValueError(
                "Apollo 11 descent guidance station is not available in generic runtime"
            )
        if decision_config.control_station not in generic.available_stations:
            raise ValueError(
                "Apollo 11 descent control station is not available in generic runtime"
            )

        return cls(
            fixture=fixture,
            state=generic.state,
            events=generic.events,
            stations=generic.stations,
            station_views=generic.station_views,
            injectable_variables=generic.injectable_variables,
            pdi_get_s=pdi_get_s,
            phase_profile=phase_profile,
            decision_config=decision_config,
        )

    def project_descent(
        self,
        *,
        landing_radar: LandingRadarControllerState,
        controller_product_values: Mapping[str, Any],
        guidance_computer_state: GuidanceComputerState,
        control_mode: DescentControlMode = DescentControlMode.AUTOMATIC,
        field_provenance: Mapping[str, tuple[str, ...]] | None = None,
        provenance: tuple[str, ...] = (),
    ) -> Apollo11DescentRuntimeProjection:
        """Compose a read-only descent projection from explicit inputs.

        The method intentionally requires controller-visible values and onboard
        guidance state as separate arguments. Generic runtime variables are not
        promoted into controller products implicitly.
        """

        return project_apollo11_descent_runtime(
            session=self,
            pdi_get_s=self.pdi_get_s,
            phase_profile=self.phase_profile,
            landing_radar=landing_radar,
            controller_product_values=controller_product_values,
            decision_config=self.decision_config,
            guidance_computer_state=guidance_computer_state,
            control_mode=control_mode,
            field_provenance=field_provenance,
            provenance=provenance,
        )
