"""Authoritative single-process session orchestration for the Apollo 13 PC+2 slice.

This module is intentionally framework-neutral. It joins the existing domain
model, controller projections, player presentations, controller reporting, and
communications into one authoritative session without adding network/UI policy.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any

from .capcom_presentation import build_pc2_capcom_presentation
from .control_presentation import build_pc2_control_presentation
from .controller_products import project_controller_products
from .fido_retro_presentation import build_pc2_fido_retro_presentation
from .flight_presentation import build_pc2_flight_presentation
from .guido_presentation import build_pc2_guido_presentation
from .inco_presentation import build_pc2_inco_presentation
from .pc2_nominal import PC2State, SimEvent, apply_event, build_events
from .telmu_presentation import build_pc2_telmu_presentation


class SessionStatus(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETE = "complete"


@dataclass(frozen=True)
class SessionAuditEvent:
    sequence: int
    get_s: float
    kind: str
    actor: str
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ReadinessReport:
    get_s: float
    player_id: str
    station: str
    ready: bool
    note: str = ""


@dataclass
class CapcomQueueItem:
    item_id: int
    get_s: float
    requested_by: str
    action: str
    parameters: dict[str, Any]
    basis: str
    transmitted: bool = False
    transmitted_get_s: float | None = None


@dataclass(frozen=True)
class PlayerSessionSnapshot:
    """Serializable player-scoped session snapshot for a future client/API."""

    player_id: str
    station: str
    get_s: float
    session_status: str
    mission_phase: str
    pending_gate: str | None
    pause_reason: str | None
    presentation: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


_PRESENTATION_BUILDERS = {
    "CONTROL": build_pc2_control_presentation,
    "GUIDO": build_pc2_guido_presentation,
    "TELMU": build_pc2_telmu_presentation,
    "FIDO_RETRO": build_pc2_fido_retro_presentation,
    "INCO": build_pc2_inco_presentation,
    "FLIGHT": build_pc2_flight_presentation,
    "CAPCOM": build_pc2_capcom_presentation,
}


@dataclass
class PC2Session:
    fixture: dict[str, Any]
    state: PC2State
    events: list[SimEvent]
    status: SessionStatus = SessionStatus.CREATED
    next_event_index: int = 0
    pending_gate: str | None = None
    pause_reason: str | None = None
    station_assignments: dict[str, str] = field(default_factory=dict)
    readiness_reports: list[ReadinessReport] = field(default_factory=list)
    capcom_queue: list[CapcomQueueItem] = field(default_factory=list)
    audit_log: list[SessionAuditEvent] = field(default_factory=list)
    _audit_sequence: int = 0
    _next_capcom_item_id: int = 1

    @classmethod
    def create(cls, fixture: dict[str, Any]) -> "PC2Session":
        state = PC2State(
            get_s=float(fixture["start_get_s"]),
            lm_inverter_warning=bool(fixture["lm_power"]["inverter_warning"]),
        )
        return cls(fixture=fixture, state=state, events=build_events(fixture))

    @property
    def available_stations(self) -> tuple[str, ...]:
        return tuple(_PRESENTATION_BUILDERS)

    def _audit(self, kind: str, actor: str, **details: Any) -> SessionAuditEvent:
        self._audit_sequence += 1
        event = SessionAuditEvent(
            sequence=self._audit_sequence,
            get_s=float(self.state.get_s),
            kind=kind,
            actor=actor,
            details=dict(details),
        )
        self.audit_log.append(event)
        return event

    def assign_station(self, player_id: str, station: str) -> None:
        station = station.upper()
        if station not in _PRESENTATION_BUILDERS:
            raise ValueError(f"Unsupported station: {station}")
        if player_id in self.station_assignments:
            raise ValueError(f"Player already assigned: {player_id}")
        if station in self.station_assignments.values():
            raise ValueError(f"Station already assigned: {station}")
        self.station_assignments[player_id] = station
        self._audit("station_assigned", "SESSION", player_id=player_id, station=station)

    def station_for(self, player_id: str) -> str:
        try:
            return self.station_assignments[player_id]
        except KeyError as exc:
            raise ValueError(f"Player has no station assignment: {player_id}") from exc

    def start(self) -> None:
        if self.status != SessionStatus.CREATED:
            raise ValueError("Session can only be started once")
        self.status = SessionStatus.RUNNING
        self.pause_reason = None
        self._audit("session_started", "SESSION")

    def pause(self) -> None:
        if self.status != SessionStatus.RUNNING:
            raise ValueError("Only a running session can be paused")
        self.status = SessionStatus.PAUSED
        self.pause_reason = "manual"
        self._audit("session_paused", "SESSION", reason=self.pause_reason)

    def resume(self) -> None:
        if self.status != SessionStatus.PAUSED:
            raise ValueError("Only a paused session can be resumed")
        if self.pending_gate is not None:
            raise ValueError("Cannot resume while a controller decision gate is pending")
        prior_reason = self.pause_reason
        self.status = SessionStatus.RUNNING
        self.pause_reason = None
        self._audit("session_resumed", "SESSION", prior_reason=prior_reason)

    def _pause_for_gate(self, gate: str, *, source_event: str) -> None:
        """Pause simulation time explicitly while a controller decision is pending.

        Apollo GET did not historically stop. This is a project playability policy:
        the simulation is explicitly paused so source-backed downstream event times
        are not applied retroactively while players deliberate.
        """
        self.pending_gate = gate
        self.status = SessionStatus.PAUSED
        self.pause_reason = f"decision_gate:{gate}"
        self._audit(
            "decision_gate_opened",
            "SESSION",
            gate=gate,
            source_event=source_event,
            simulation_paused=True,
        )

    def advance_to(self, target_get_s: float) -> float:
        """Advance authoritative scenario time up to target GET.

        Timed historical events are applied only while the simulation is RUNNING.
        A controller decision gate explicitly pauses the simulation; it is not a
        claim that historical Apollo GET stopped. This prevents later historical
        events from being applied retroactively while a player decision is pending.
        """
        if self.status != SessionStatus.RUNNING:
            raise ValueError("Session must be running to advance")
        target = float(target_get_s)
        if target < self.state.get_s:
            raise ValueError("Session time cannot move backward")

        while self.next_event_index < len(self.events):
            event = self.events[self.next_event_index]
            if event.get_s > target:
                break

            if event.name == "final_go_no_go_poll":
                self.state.get_s = event.get_s
                self.state.phase = "pc2_final_readiness"
                self.next_event_index += 1
                self._pause_for_gate("flight_go", source_event=event.name)
                return float(self.state.get_s)

            apply_event(self.state, event, self.fixture)
            self.next_event_index += 1
            self._audit("scenario_event_applied", "SESSION", event=event.name)

        self.state.get_s = target

        if self.next_event_index >= len(self.events):
            self.status = SessionStatus.COMPLETE
            self.pause_reason = None
            self._audit("session_completed", "SESSION")

        return float(self.state.get_s)

    def _readiness_payload(self) -> list[dict[str, Any]]:
        return [
            {
                "get_s": report.get_s,
                "station": report.station,
                "ready": report.ready,
                "note": report.note,
            }
            for report in self.readiness_reports
        ]

    def _capcom_queue_payload(self) -> list[dict[str, Any]]:
        return [
            {
                "item_id": item.item_id,
                "get_s": item.get_s,
                "action": item.action,
                "parameters": dict(item.parameters),
                "basis": item.basis,
                "transmitted": item.transmitted,
                "transmitted_get_s": item.transmitted_get_s,
            }
            for item in self.capcom_queue
        ]

    def get_station_view(self, player_id: str) -> Any:
        station = self.station_for(player_id)
        projections = project_controller_products(self.state, self.fixture)
        projection = projections[station]
        if station == "FLIGHT":
            return build_pc2_flight_presentation(
                projection,
                readiness_reports=self._readiness_payload(),
            )
        if station == "CAPCOM":
            return build_pc2_capcom_presentation(
                projection,
                queue_items=self._capcom_queue_payload(),
            )
        return _PRESENTATION_BUILDERS[station](projection)

    def player_snapshot(self, player_id: str) -> PlayerSessionSnapshot:
        station = self.station_for(player_id)
        view = self.get_station_view(player_id)
        return PlayerSessionSnapshot(
            player_id=player_id,
            station=station,
            get_s=float(self.state.get_s),
            session_status=self.status.value,
            mission_phase=self.state.phase,
            pending_gate=self.pending_gate,
            pause_reason=self.pause_reason,
            presentation=asdict(view),
        )

    def submit_readiness(self, player_id: str, *, ready: bool, note: str = "") -> ReadinessReport:
        station = self.station_for(player_id)
        report = ReadinessReport(
            get_s=float(self.state.get_s),
            player_id=player_id,
            station=station,
            ready=bool(ready),
            note=note,
        )
        self.readiness_reports.append(report)
        self._audit(
            "controller_readiness_report",
            station,
            player_id=player_id,
            ready=bool(ready),
            note=note,
        )
        return report

    def latest_readiness_by_station(self) -> dict[str, ReadinessReport]:
        latest: dict[str, ReadinessReport] = {}
        for report in self.readiness_reports:
            latest[report.station] = report
        return latest

    def record_flight_go(self, player_id: str, *, go: bool, basis: str) -> None:
        if self.station_for(player_id) != "FLIGHT":
            raise ValueError("Only the FLIGHT player can record the PC+2 GO/NO-GO decision")
        if self.pending_gate != "flight_go":
            raise ValueError("FLIGHT GO/NO-GO decision is not currently pending")

        self.state.flight_go = bool(go)
        self._audit(
            "flight_go_decision",
            "FLIGHT",
            player_id=player_id,
            go=bool(go),
            basis=basis,
            readiness={
                station: report.ready
                for station, report in self.latest_readiness_by_station().items()
            },
        )

        if go:
            self.state.phase = "pc2_go_for_burn"
            self.pending_gate = None
            if self.pause_reason == "decision_gate:flight_go":
                self.status = SessionStatus.RUNNING
                self.pause_reason = None
                self._audit("session_resumed_after_decision", "SESSION", gate="flight_go")
        else:
            self.state.phase = "pc2_final_readiness"

    def queue_capcom_instruction(
        self,
        flight_player_id: str,
        *,
        action: str,
        parameters: dict[str, Any] | None = None,
        basis: str,
    ) -> CapcomQueueItem:
        if self.station_for(flight_player_id) != "FLIGHT":
            raise ValueError("Only FLIGHT can approve an item into the CAPCOM queue in this prototype")
        item = CapcomQueueItem(
            item_id=self._next_capcom_item_id,
            get_s=float(self.state.get_s),
            requested_by="FLIGHT",
            action=action,
            parameters=dict(parameters or {}),
            basis=basis,
        )
        self._next_capcom_item_id += 1
        self.capcom_queue.append(item)
        self._audit(
            "capcom_item_queued",
            "FLIGHT",
            item_id=item.item_id,
            action=action,
            parameters=item.parameters,
            basis=basis,
        )
        return item

    def transmit_capcom_item(self, capcom_player_id: str, item_id: int) -> CapcomQueueItem:
        if self.station_for(capcom_player_id) != "CAPCOM":
            raise ValueError("Only CAPCOM can transmit an approved CAPCOM queue item")
        item = next((item for item in self.capcom_queue if item.item_id == item_id), None)
        if item is None:
            raise ValueError(f"Unknown CAPCOM queue item: {item_id}")
        if item.transmitted:
            raise ValueError(f"CAPCOM queue item already transmitted: {item_id}")
        item.transmitted = True
        item.transmitted_get_s = float(self.state.get_s)
        self._audit(
            "capcom_item_transmitted",
            "CAPCOM",
            player_id=capcom_player_id,
            item_id=item.item_id,
            action=item.action,
            parameters=item.parameters,
        )
        return item
