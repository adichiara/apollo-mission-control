"""Minimal procedural communication events for the Apollo 13 PC+2 slice.

These events record approved crew-facing instructions and crew completion
reports. They do not alter spacecraft state or infer procedure outcomes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ProcedureCommunication:
    event_id: str
    get_s: float
    sender: str
    recipient: str
    kind: str
    action: str
    parameters: dict[str, Any]
    provenance: str


@dataclass
class ProcedureExchangeLog:
    events: list[ProcedureCommunication] = field(default_factory=list)

    def record(self, event: ProcedureCommunication) -> None:
        if event.kind not in {"instruction", "completion_report", "readback"}:
            raise ValueError(f"Unsupported procedure communication kind: {event.kind}")
        self.events.append(event)
        self.events.sort(key=lambda item: item.get_s)

    def for_action(self, action: str) -> list[ProcedureCommunication]:
        return [event for event in self.events if event.action == action]


def record_inverter_switch_instruction(
    log: ProcedureExchangeLog,
    *,
    event_id: str,
    get_s: float,
    provenance: str,
) -> None:
    """Record a CAPCOM request to perform the PC+2 inverter-switch contingency.

    Exact alternate-inverter identity remains unresolved, so no inverter number
    is accepted here.
    """
    log.record(
        ProcedureCommunication(
            event_id=event_id,
            get_s=get_s,
            sender="CAPCOM",
            recipient="CREW",
            kind="instruction",
            action="switch_lm_inverter",
            parameters={},
            provenance=provenance,
        )
    )


def record_inverter_switch_completion(
    log: ProcedureExchangeLog,
    *,
    event_id: str,
    get_s: float,
    provenance: str,
) -> None:
    """Record crew report that the requested switch action was performed.

    This communication event does not assert whether the inverter warning
    cleared or remained on; that is an independent observation.
    """
    log.record(
        ProcedureCommunication(
            event_id=event_id,
            get_s=get_s,
            sender="CREW",
            recipient="CAPCOM",
            kind="completion_report",
            action="switch_lm_inverter",
            parameters={},
            provenance=provenance,
        )
    )
