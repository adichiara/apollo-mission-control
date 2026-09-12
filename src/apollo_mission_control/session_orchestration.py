"""Framework-neutral multiplayer/session orchestration for the Apollo 13 PC+2 slice.

This module is project software architecture, not a claim about Apollo MCC
software internals.  It preserves the historically important operational
separation between controller readiness reports, the Flight Director decision,
and CAPCOM's crew-facing transmission.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class SessionEvent:
    sequence: int
    get_s: float
    kind: str
    actor: str
    payload: dict[str, Any]


@dataclass(frozen=True)
class ReadinessReport:
    station: str
    status: str
    get_s: float
    note: str = ""


@dataclass(frozen=True)
class FlightDecision:
    go_for_burn: bool
    get_s: float
    basis: str = "controller reports / Flight Director judgment"


@dataclass(frozen=True)
class CrewCallout:
    callout_id: str
    origin_station: str
    action: str
    requested_get_s: float
    parameters: dict[str, Any]
    transmitted_get_s: float | None = None


@dataclass
class PC2Session:
    """Minimal authoritative session state for first integrated PC+2 play.

    The session owns station assignment, event ordering, controller readiness,
    Flight's explicit burn decision, and a FLIGHT/discipline -> CAPCOM -> crew
    callout handoff.  It does not infer readiness or GO/NO-GO from hidden
    spacecraft state.
    """

    get_s: float
    station_assignments: dict[str, str] = field(default_factory=dict)
    readiness_reports: dict[str, ReadinessReport] = field(default_factory=dict)
    flight_decision: FlightDecision | None = None
    pending_callouts: dict[str, CrewCallout] = field(default_factory=dict)
    transmitted_callouts: list[CrewCallout] = field(default_factory=list)
    events: list[SessionEvent] = field(default_factory=list)
    _sequence: int = 0

    def _record(self, kind: str, actor: str, payload: dict[str, Any], *, get_s: float) -> SessionEvent:
        self._sequence += 1
        event = SessionEvent(
            sequence=self._sequence,
            get_s=float(get_s),
            kind=kind,
            actor=actor,
            payload=dict(payload),
        )
        self.events.append(event)
        return event

    def synchronize_get(self, get_s: float) -> None:
        if get_s < self.get_s:
            raise ValueError("Session GET cannot move backward")
        self.get_s = float(get_s)
        self._record("get_sync", "SESSION", {"get_s": self.get_s}, get_s=self.get_s)

    def assign_station(self, *, player_id: str, station: str, get_s: float | None = None) -> None:
        station = station.upper()
        if station in self.station_assignments and self.station_assignments[station] != player_id:
            raise ValueError(f"Station already assigned: {station}")
        self.station_assignments[station] = player_id
        when = self.get_s if get_s is None else float(get_s)
        self._record("station_assigned", "SESSION", {"station": station, "player_id": player_id}, get_s=when)

    def report_readiness(
        self,
        *,
        station: str,
        status: str,
        get_s: float | None = None,
        note: str = "",
    ) -> ReadinessReport:
        normalized = status.upper()
        if normalized not in {"GO", "NO-GO", "HOLD"}:
            raise ValueError("Readiness status must be GO, NO-GO, or HOLD")
        when = self.get_s if get_s is None else float(get_s)
        report = ReadinessReport(station=station.upper(), status=normalized, get_s=when, note=note)
        self.readiness_reports[report.station] = report
        self._record(
            "readiness_report",
            report.station,
            {"status": report.status, "note": report.note},
            get_s=when,
        )
        return report

    def record_flight_decision(
        self,
        *,
        go_for_burn: bool,
        get_s: float | None = None,
        basis: str = "controller reports / Flight Director judgment",
    ) -> FlightDecision:
        when = self.get_s if get_s is None else float(get_s)
        decision = FlightDecision(go_for_burn=bool(go_for_burn), get_s=when, basis=basis)
        self.flight_decision = decision
        self._record(
            "flight_decision",
            "FLIGHT",
            {"go_for_burn": decision.go_for_burn, "basis": decision.basis},
            get_s=when,
        )
        return decision

    def queue_crew_callout(
        self,
        *,
        callout_id: str,
        origin_station: str,
        action: str,
        parameters: dict[str, Any] | None = None,
        get_s: float | None = None,
    ) -> CrewCallout:
        if callout_id in self.pending_callouts or any(item.callout_id == callout_id for item in self.transmitted_callouts):
            raise ValueError(f"Duplicate callout id: {callout_id}")
        when = self.get_s if get_s is None else float(get_s)
        callout = CrewCallout(
            callout_id=callout_id,
            origin_station=origin_station.upper(),
            action=action,
            requested_get_s=when,
            parameters=dict(parameters or {}),
        )
        self.pending_callouts[callout_id] = callout
        self._record(
            "callout_queued",
            callout.origin_station,
            {"callout_id": callout_id, "action": action, "parameters": callout.parameters},
            get_s=when,
        )
        return callout

    def capcom_transmit(self, callout_id: str, *, get_s: float | None = None) -> CrewCallout:
        if callout_id not in self.pending_callouts:
            raise KeyError(callout_id)
        when = self.get_s if get_s is None else float(get_s)
        pending = self.pending_callouts.pop(callout_id)
        transmitted = CrewCallout(
            callout_id=pending.callout_id,
            origin_station=pending.origin_station,
            action=pending.action,
            requested_get_s=pending.requested_get_s,
            parameters=dict(pending.parameters),
            transmitted_get_s=when,
        )
        self.transmitted_callouts.append(transmitted)
        self._record(
            "capcom_to_crew",
            "CAPCOM",
            {
                "callout_id": transmitted.callout_id,
                "origin_station": transmitted.origin_station,
                "action": transmitted.action,
                "parameters": transmitted.parameters,
            },
            get_s=when,
        )
        return transmitted

    def audit_log(self) -> tuple[SessionEvent, ...]:
        return tuple(self.events)
