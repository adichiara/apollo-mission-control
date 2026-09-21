"""Project existing generic-runtime human events into a descent decision gate.

This adapter deliberately reuses GenericScenarioSession artifacts rather than
creating a second controller-event model. Historical/controller-visible landing
radar state is supplied separately and is never interpreted here.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .descent_decision_gate import (
    DescentDecisionGate,
    LandingRadarControllerState,
    Readiness,
    RelayState,
)
from .generic_runtime import (
    GenericAuditEvent,
    GenericCapcomQueueItem,
    GenericReadinessReport,
)


@dataclass(frozen=True)
class DescentDecisionProjectionConfig:
    """Explicit mapping between runtime identifiers and the bounded gate contract."""

    gate_id: str
    capcom_go_action: str
    capcom_no_go_action: str

    def validated(self) -> "DescentDecisionProjectionConfig":
        values = {
            "gate_id": self.gate_id,
            "capcom_go_action": self.capcom_go_action,
            "capcom_no_go_action": self.capcom_no_go_action,
        }
        for name, value in values.items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be non-empty")
        if self.capcom_go_action == self.capcom_no_go_action:
            raise ValueError("CAPCOM GO and NO-GO actions must be distinct")
        return DescentDecisionProjectionConfig(
            gate_id=self.gate_id.strip(),
            capcom_go_action=self.capcom_go_action.strip(),
            capcom_no_go_action=self.capcom_no_go_action.strip(),
        )


def _latest_readiness(
    reports: Sequence[GenericReadinessReport],
    *,
    station: str,
    get_s: float,
) -> Readiness:
    candidates = [
        (index, report)
        for index, report in enumerate(reports)
        if report.station.upper() == station.upper() and report.get_s <= get_s
    ]
    if not candidates:
        return Readiness.UNKNOWN
    _, latest = max(candidates, key=lambda item: (item[1].get_s, item[0]))
    return Readiness.GO if latest.ready else Readiness.NO_GO


def _latest_flight_decision(
    events: Sequence[GenericAuditEvent],
    *,
    gate_id: str,
    get_s: float,
) -> Readiness:
    candidates = [
        (index, event)
        for index, event in enumerate(events)
        if event.kind == "flight_decision"
        and event.actor.upper() == "FLIGHT"
        and event.details.get("gate") == gate_id
        and event.get_s <= get_s
    ]
    if not candidates:
        return Readiness.UNKNOWN
    _, latest = max(
        candidates,
        key=lambda item: (item[1].get_s, item[1].sequence, item[0]),
    )
    go = latest.details.get("go")
    if not isinstance(go, bool):
        return Readiness.UNKNOWN
    return Readiness.GO if go else Readiness.NO_GO


def _latest_capcom_relay(
    items: Sequence[GenericCapcomQueueItem],
    *,
    go_action: str,
    no_go_action: str,
    get_s: float,
) -> RelayState:
    candidates: list[tuple[int, GenericCapcomQueueItem, RelayState]] = []
    for index, item in enumerate(items):
        if not item.transmitted or item.transmitted_get_s is None:
            continue
        if item.transmitted_get_s > get_s:
            continue
        if item.action == go_action:
            relay = RelayState.GO_RELAYED
        elif item.action == no_go_action:
            relay = RelayState.NO_GO_RELAYED
        else:
            continue
        candidates.append((index, item, relay))

    if not candidates:
        return RelayState.NOT_RELAYED

    _, _, relay = max(
        candidates,
        key=lambda item: (
            float(item[1].transmitted_get_s or 0.0),
            item[1].item_id,
            item[0],
        ),
    )
    return relay


def project_generic_runtime_descent_gate(
    *,
    get_s: float,
    landing_radar: LandingRadarControllerState,
    readiness_reports: Sequence[GenericReadinessReport],
    audit_events: Sequence[GenericAuditEvent],
    capcom_queue: Sequence[GenericCapcomQueueItem],
    config: DescentDecisionProjectionConfig,
    provenance: tuple[str, ...] = (),
) -> DescentDecisionGate:
    """Build a gate snapshot from explicit human/runtime events.

    This function does not derive controller readiness from telemetry, does not
    create a FLIGHT decision from station calls, and does not transmit anything.
    """

    cfg = config.validated()
    if get_s < 0:
        raise ValueError("get_s must be non-negative")

    return DescentDecisionGate(
        get_s=float(get_s),
        landing_radar=landing_radar.validated(),
        guidance_readiness=_latest_readiness(
            readiness_reports, station="GUIDANCE", get_s=get_s
        ),
        control_readiness=_latest_readiness(
            readiness_reports, station="CONTROL", get_s=get_s
        ),
        flight_decision=_latest_flight_decision(
            audit_events, gate_id=cfg.gate_id, get_s=get_s
        ),
        capcom_relay=_latest_capcom_relay(
            capcom_queue,
            go_action=cfg.capcom_go_action,
            no_go_action=cfg.capcom_no_go_action,
            get_s=get_s,
        ),
        provenance=tuple(provenance),
    ).validated()
