"""Implementation-neutral Apollo descent decision-gate contract.

The contract preserves documented station-scoped observations and human decisions
without deriving a landing GO/NO-GO automatically from hidden simulator state.

Research basis:
- resources/research/502_apollo11_descent_lr_controller_call_workflow.md
- NASA Apollo 11 Flight Mission Rules, rule 5-11 (7/16/69)
- NASA TM X-58038, Apollo 11 lunar-descent guidance monitoring
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Readiness(str, Enum):
    UNKNOWN = "unknown"
    GO = "go"
    NO_GO = "no_go"


class RelayState(str, Enum):
    NOT_RELAYED = "not_relayed"
    GO_RELAYED = "go_relayed"
    NO_GO_RELAYED = "no_go_relayed"


class DescentControlMode(str, Enum):
    """Crew-control boundary relevant to Apollo 11 Flight Mission Rule 5-11."""

    AUTOMATIC = "automatic"
    MANUAL = "manual"


@dataclass(frozen=True)
class LandingRadarControllerState:
    """Controller-visible LR state; fields remain deliberately independent."""

    range_data_good: bool | None = None
    velocity_data_good: bool | None = None
    antenna_position: int | None = None
    body_axis_velocity_fps: tuple[float, float, float] | None = None
    slant_range_ft: float | None = None
    pgns_altitude_ft: float | None = None
    time_to_go_s: float | None = None

    def validated(self) -> "LandingRadarControllerState":
        if self.antenna_position is not None and self.antenna_position not in (1, 2):
            raise ValueError("antenna_position must be 1, 2, or None")
        if self.body_axis_velocity_fps is not None and len(self.body_axis_velocity_fps) != 3:
            raise ValueError("body_axis_velocity_fps must contain exactly three components")
        return self


@dataclass(frozen=True)
class DescentDecisionGate:
    """Snapshot of the documented front-room landing-decision chain.

    No readiness or final decision is inferred from LR measurements. CONTROL,
    Guidance, FLIGHT, and CAPCOM states must be supplied explicitly by their
    respective controller/communication layers.

    ``control_mode`` changes rule applicability, not observation availability.
    Apollo 11 Flight Mission Rule 5-11 states that after crew takeover there are
    no trajectory or guidance constraints that are cause for abort.  The
    controller-visible observations therefore remain present in this object when
    manual control begins; only the trajectory/guidance abort-rule applicability
    changes.  Independently sourced systems/propellant criteria are outside this
    bounded flag and remain unaffected.
    """

    get_s: float
    landing_radar: LandingRadarControllerState
    guidance_readiness: Readiness = Readiness.UNKNOWN
    control_readiness: Readiness = Readiness.UNKNOWN
    flight_decision: Readiness = Readiness.UNKNOWN
    capcom_relay: RelayState = RelayState.NOT_RELAYED
    control_mode: DescentControlMode = DescentControlMode.AUTOMATIC
    provenance: tuple[str, ...] = ()

    def validated(self) -> "DescentDecisionGate":
        if self.get_s < 0:
            raise ValueError("get_s must be non-negative")
        self.landing_radar.validated()
        return self

    @property
    def trajectory_guidance_abort_constraints_applicable(self) -> bool:
        """Whether trajectory/guidance constraints may themselves cause abort.

        This is a rule-applicability statement, not an abort decision and not a
        statement about systems/propellant criteria.
        """

        return self.control_mode is not DescentControlMode.MANUAL

    @property
    def front_room_inputs_complete(self) -> bool:
        """Whether the two currently modeled station calls are explicit.

        This is not a landing decision. Other stations in the historical poll may
        remain outside this bounded contract.
        """

        return (
            self.guidance_readiness is not Readiness.UNKNOWN
            and self.control_readiness is not Readiness.UNKNOWN
        )

    @property
    def relay_consistent_with_flight(self) -> bool:
        """Check chain consistency without changing or inferring any decision."""

        if self.capcom_relay is RelayState.NOT_RELAYED:
            return True
        if self.capcom_relay is RelayState.GO_RELAYED:
            return self.flight_decision is Readiness.GO
        if self.capcom_relay is RelayState.NO_GO_RELAYED:
            return self.flight_decision is Readiness.NO_GO
        return False

    def to_dict(self) -> dict[str, object]:
        checked = self.validated()
        lr = checked.landing_radar
        return {
            "model_status": "apollo11_descent_decision_gate_contract",
            "get_s": checked.get_s,
            "control_mode": checked.control_mode.value,
            "trajectory_guidance_abort_constraints_applicable": (
                checked.trajectory_guidance_abort_constraints_applicable
            ),
            "landing_radar": {
                "range_data_good": lr.range_data_good,
                "velocity_data_good": lr.velocity_data_good,
                "antenna_position": lr.antenna_position,
                "body_axis_velocity_fps": (
                    None
                    if lr.body_axis_velocity_fps is None
                    else list(lr.body_axis_velocity_fps)
                ),
                "slant_range_ft": lr.slant_range_ft,
                "pgns_altitude_ft": lr.pgns_altitude_ft,
                "time_to_go_s": lr.time_to_go_s,
            },
            "guidance_readiness": checked.guidance_readiness.value,
            "control_readiness": checked.control_readiness.value,
            "flight_decision": checked.flight_decision.value,
            "capcom_relay": checked.capcom_relay.value,
            "front_room_inputs_complete": checked.front_room_inputs_complete,
            "relay_consistent_with_flight": checked.relay_consistent_with_flight,
            "provenance": list(checked.provenance),
        }
