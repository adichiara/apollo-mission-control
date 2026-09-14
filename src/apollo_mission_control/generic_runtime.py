"""Generic scenario runtime for shared Mission Control exercise mechanics.

This runtime proves that lifecycle, station ownership, timed external events,
readiness, FLIGHT decisions, CAPCOM traffic, audit history, and controlled
state injection can execute without PC+2-specific domain code.

It is deliberately *not* a physics engine. Scenario event updates represent
external/discrete exercise inputs only. Causal subsystem consequences belong
in reusable numerical/subsystem models and scenario-specific adapters.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Iterable, Sequence

from .session_runtime import SessionStatus


@dataclass
class GenericRuntimeState:
    get_s: float
    phase: str
    variables: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class GenericTimedEvent:
    get_s: float
    name: str
    phase: str | None = None
    updates: dict[str, Any] = field(default_factory=dict)
    gate: str | None = None
    complete: bool = False


@dataclass(frozen=True)
class GenericAuditEvent:
    sequence: int
    get_s: float
    kind: str
    actor: str
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class GenericReadinessReport:
    get_s: float
    player_id: str
    station: str
    ready: bool
    note: str = ""


@dataclass
class GenericCapcomQueueItem:
    item_id: int
    get_s: float
    requested_by: str
    action: str
    parameters: dict[str, Any]
    basis: str
    transmitted: bool = False
    transmitted_get_s: float | None = None


@dataclass(frozen=True)
class GenericPlayerSnapshot:
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


@dataclass(frozen=True)
class GenericBundledPlayerSnapshot:
    player_id: str
    stations: tuple[str, ...]
    get_s: float
    session_status: str
    mission_phase: str
    pending_gate: str | None
    pause_reason: str | None
    presentations: dict[str, dict[str, Any]]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _nonempty_text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()


def _station_list(value: Any) -> tuple[str, ...]:
    if not isinstance(value, list) or not value:
        raise ValueError("generic_runtime stations must be a non-empty list")
    stations: list[str] = []
    for raw in value:
        station = _nonempty_text(raw, "station").upper()
        if station in stations:
            raise ValueError(f"duplicate generic_runtime station: {station}")
        stations.append(station)
    return tuple(stations)


def _event_list(
    value: Any,
    *,
    start_get_s: float,
    variable_names: frozenset[str],
) -> list[GenericTimedEvent]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError("generic_runtime events must be a list")

    events: list[GenericTimedEvent] = []
    for payload in value:
        if not isinstance(payload, dict):
            raise ValueError("generic_runtime event must be an object")
        raw_get = payload.get("get_s")
        if isinstance(raw_get, bool) or not isinstance(raw_get, (int, float)):
            raise ValueError("generic_runtime event get_s must be numeric")
        get_s = float(raw_get)
        if get_s < start_get_s:
            raise ValueError("generic_runtime event cannot precede scenario start")

        name = _nonempty_text(payload.get("name"), "event name")
        raw_phase = payload.get("phase")
        phase = None if raw_phase is None else _nonempty_text(raw_phase, "event phase")

        updates = payload.get("updates", {})
        if not isinstance(updates, dict):
            raise ValueError("generic_runtime event updates must be an object")
        unknown = sorted(set(updates) - set(variable_names))
        if unknown:
            raise ValueError(
                f"generic_runtime event updates unknown variable: {unknown[0]}"
            )

        raw_gate = payload.get("gate")
        gate = None if raw_gate is None else _nonempty_text(raw_gate, "event gate")
        complete = payload.get("complete", False)
        if not isinstance(complete, bool):
            raise ValueError("generic_runtime event complete must be boolean")

        events.append(
            GenericTimedEvent(
                get_s=get_s,
                name=name,
                phase=phase,
                updates=dict(updates),
                gate=gate,
                complete=complete,
            )
        )

    events.sort(key=lambda item: item.get_s)
    return events


@dataclass
class GenericScenarioSession:
    fixture: dict[str, Any]
    state: GenericRuntimeState
    events: list[GenericTimedEvent]
    stations: tuple[str, ...]
    station_views: dict[str, tuple[str, ...]]
    injectable_variables: frozenset[str]
    status: SessionStatus = SessionStatus.CREATED
    next_event_index: int = 0
    pending_gate: str | None = None
    pause_reason: str | None = None
    station_assignments: dict[str, str] = field(default_factory=dict)
    player_station_sets: dict[str, tuple[str, ...]] = field(default_factory=dict)
    readiness_reports: list[GenericReadinessReport] = field(default_factory=list)
    capcom_queue: list[GenericCapcomQueueItem] = field(default_factory=list)
    audit_log: list[GenericAuditEvent] = field(default_factory=list)
    _audit_sequence: int = 0
    _next_capcom_item_id: int = 1

    @classmethod
    def create(cls, fixture: dict[str, Any]) -> "GenericScenarioSession":
        runtime = fixture.get("generic_runtime")
        if not isinstance(runtime, dict):
            raise ValueError("generic_v1 scenario requires a generic_runtime object")

        start_raw = fixture.get("start_get_s")
        if isinstance(start_raw, bool) or not isinstance(start_raw, (int, float)):
            raise ValueError("scenario start_get_s must be numeric")
        start_get_s = float(start_raw)

        stations = _station_list(runtime.get("stations"))
        phase = _nonempty_text(
            runtime.get("initial_phase", "initial"),
            "generic_runtime initial_phase",
        )

        variables = runtime.get("initial_variables", {})
        if not isinstance(variables, dict):
            raise ValueError("generic_runtime initial_variables must be an object")
        for name in variables:
            _nonempty_text(name, "generic_runtime variable name")
        variable_names = frozenset(variables)

        raw_views = runtime.get("station_views", {})
        if not isinstance(raw_views, dict):
            raise ValueError("generic_runtime station_views must be an object")
        station_views: dict[str, tuple[str, ...]] = {}
        for station in stations:
            raw_names = raw_views.get(station, [])
            if not isinstance(raw_names, list):
                raise ValueError(f"station view for {station} must be a list")
            names: list[str] = []
            for raw_name in raw_names:
                name = _nonempty_text(raw_name, f"station view variable for {station}")
                if name not in variable_names:
                    raise ValueError(
                        f"station view for {station} references unknown variable: {name}"
                    )
                if name not in names:
                    names.append(name)
            station_views[station] = tuple(names)

        raw_injectable = runtime.get("injectable_variables", [])
        if not isinstance(raw_injectable, list):
            raise ValueError("generic_runtime injectable_variables must be a list")
        injectable: set[str] = set()
        for raw_name in raw_injectable:
            name = _nonempty_text(raw_name, "injectable variable")
            if name not in variable_names:
                raise ValueError(f"injectable variable is not in initial state: {name}")
            injectable.add(name)

        events = _event_list(
            runtime.get("events", []),
            start_get_s=start_get_s,
            variable_names=variable_names,
        )

        return cls(
            fixture=fixture,
            state=GenericRuntimeState(
                get_s=start_get_s,
                phase=phase,
                variables=dict(variables),
            ),
            events=events,
            stations=stations,
            station_views=station_views,
            injectable_variables=frozenset(injectable),
        )

    @property
    def available_stations(self) -> tuple[str, ...]:
        return self.stations

    @property
    def assigned_stations(self) -> tuple[str, ...]:
        return tuple(
            station
            for stations in self.player_station_sets.values()
            for station in stations
        )

    def _audit(self, kind: str, actor: str, **details: Any) -> GenericAuditEvent:
        self._audit_sequence += 1
        event = GenericAuditEvent(
            sequence=self._audit_sequence,
            get_s=float(self.state.get_s),
            kind=kind,
            actor=actor,
            details=dict(details),
        )
        self.audit_log.append(event)
        return event

    def assign_stations(self, player_id: str, stations: Sequence[str]) -> None:
        normalized = tuple(str(station).strip().upper() for station in stations)
        if not normalized or any(not station for station in normalized):
            raise ValueError("at least one station must be assigned")
        if len(set(normalized)) != len(normalized):
            raise ValueError("duplicate station in player assignment")
        unsupported = [station for station in normalized if station not in self.stations]
        if unsupported:
            raise ValueError(f"unsupported station: {unsupported[0]}")
        if player_id in self.player_station_sets:
            raise ValueError(f"player already assigned: {player_id}")

        occupied = set(self.assigned_stations)
        conflict = next((station for station in normalized if station in occupied), None)
        if conflict is not None:
            raise ValueError(f"station already assigned: {conflict}")

        self.player_station_sets[player_id] = normalized
        self.station_assignments[player_id] = normalized[0]
        self._audit(
            "station_set_assigned" if len(normalized) > 1 else "station_assigned",
            "SESSION",
            player_id=player_id,
            stations=list(normalized),
        )

    def join_or_rejoin_stations(
        self,
        player_id: str,
        stations: Sequence[str],
    ) -> None:
        normalized = tuple(str(station).strip().upper() for station in stations)
        existing = self.player_station_sets.get(player_id)
        if existing is None:
            self.assign_stations(player_id, normalized)
            return
        if existing != normalized:
            raise ValueError(
                f"Player {player_id} is already assigned to {list(existing)}; "
                f"cannot rejoin as {list(normalized)}"
            )
        self._audit(
            "player_rejoined",
            "SESSION",
            player_id=player_id,
            stations=list(normalized),
        )

    def stations_for(self, player_id: str) -> tuple[str, ...]:
        stations = self.player_station_sets.get(player_id)
        if stations is None:
            raise ValueError(f"player has no station assignment: {player_id}")
        return stations

    def owns_station(self, player_id: str, station: str) -> bool:
        return str(station).strip().upper() in self.stations_for(player_id)

    def _require_station(self, player_id: str, station: str) -> str:
        normalized = str(station).strip().upper()
        if not self.owns_station(player_id, normalized):
            raise ValueError(f"player {player_id} is not assigned to {normalized}")
        return normalized

    def start(self) -> None:
        if self.status != SessionStatus.CREATED:
            raise ValueError("session can only be started once")
        self.status = SessionStatus.RUNNING
        self.pause_reason = None
        self._audit("session_started", "SESSION")

    def pause(self) -> None:
        if self.status != SessionStatus.RUNNING:
            raise ValueError("only a running session can be paused")
        self.status = SessionStatus.PAUSED
        self.pause_reason = "manual"
        self._audit("session_paused", "SESSION", reason="manual")

    def resume(self) -> None:
        if self.status != SessionStatus.PAUSED:
            raise ValueError("only a paused session can be resumed")
        self.status = SessionStatus.RUNNING
        self.pause_reason = None
        self._audit("session_resumed", "SESSION")

    def advance_to(self, target_get_s: float) -> float:
        if self.status != SessionStatus.RUNNING:
            raise ValueError("session must be running to advance")
        target = float(target_get_s)
        if target < self.state.get_s:
            raise ValueError("session time cannot move backward")

        while self.next_event_index < len(self.events):
            event = self.events[self.next_event_index]
            if event.get_s > target:
                break

            self.state.get_s = event.get_s
            self.state.variables.update(event.updates)
            if event.phase is not None:
                self.state.phase = event.phase
            if event.gate is not None:
                self.pending_gate = event.gate
            self._audit(
                "scenario_event_applied",
                "SCENARIO",
                event=event.name,
                updates=sorted(event.updates),
                phase=event.phase,
                gate=event.gate,
            )
            self.next_event_index += 1

            if event.complete:
                self.status = SessionStatus.COMPLETE
                self._audit(
                    "session_completed",
                    "SESSION",
                    source_event=event.name,
                )
                break

        if self.status == SessionStatus.RUNNING:
            self.state.get_s = target
        return self.state.get_s

    def _presentation_for(self, station: str) -> dict[str, Any]:
        return {
            "phase": self.state.phase,
            "observations": {
                name: self.state.variables[name]
                for name in self.station_views.get(station, ())
            },
        }

    def player_snapshot(self, player_id: str) -> GenericPlayerSnapshot:
        stations = self.stations_for(player_id)
        if len(stations) != 1:
            raise ValueError(
                f"player {player_id} owns multiple stations; use bundled snapshot"
            )
        station = stations[0]
        return GenericPlayerSnapshot(
            player_id=player_id,
            station=station,
            get_s=self.state.get_s,
            session_status=self.status.value,
            mission_phase=self.state.phase,
            pending_gate=self.pending_gate,
            pause_reason=self.pause_reason,
            presentation=self._presentation_for(station),
        )

    def bundled_player_snapshot(
        self,
        player_id: str,
    ) -> GenericBundledPlayerSnapshot:
        stations = self.stations_for(player_id)
        return GenericBundledPlayerSnapshot(
            player_id=player_id,
            stations=stations,
            get_s=self.state.get_s,
            session_status=self.status.value,
            mission_phase=self.state.phase,
            pending_gate=self.pending_gate,
            pause_reason=self.pause_reason,
            presentations={
                station: self._presentation_for(station)
                for station in stations
            },
        )

    def submit_readiness(
        self,
        player_id: str,
        *,
        ready: bool,
        note: str = "",
        station: str | None = None,
    ) -> GenericReadinessReport:
        owned = self.stations_for(player_id)
        if station is None:
            if len(owned) != 1:
                raise ValueError("station must be specified for multi-station players")
            selected = owned[0]
        else:
            selected = self._require_station(player_id, station)

        report = GenericReadinessReport(
            get_s=self.state.get_s,
            player_id=player_id,
            station=selected,
            ready=bool(ready),
            note=str(note),
        )
        self.readiness_reports.append(report)
        self._audit(
            "readiness_reported",
            selected,
            player_id=player_id,
            ready=bool(ready),
            note=str(note),
        )
        return report

    def record_flight_go(self, player_id: str, *, go: bool, basis: str) -> None:
        self._require_station(player_id, "FLIGHT")
        basis = _nonempty_text(basis, "flight decision basis")
        if self.pending_gate is None:
            raise ValueError("no pending FLIGHT decision gate")
        gate = self.pending_gate
        self.pending_gate = None
        self._audit(
            "flight_decision",
            "FLIGHT",
            player_id=player_id,
            gate=gate,
            go=bool(go),
            basis=basis,
        )

    def queue_capcom_instruction(
        self,
        player_id: str,
        *,
        action: str,
        parameters: dict[str, Any],
        basis: str,
    ) -> GenericCapcomQueueItem:
        self._require_station(player_id, "CAPCOM")
        item = GenericCapcomQueueItem(
            item_id=self._next_capcom_item_id,
            get_s=self.state.get_s,
            requested_by=player_id,
            action=_nonempty_text(action, "CAPCOM action"),
            parameters=dict(parameters),
            basis=_nonempty_text(basis, "CAPCOM basis"),
        )
        self._next_capcom_item_id += 1
        self.capcom_queue.append(item)
        self._audit(
            "capcom_item_queued",
            "CAPCOM",
            player_id=player_id,
            item_id=item.item_id,
            action=item.action,
        )
        return item

    def transmit_capcom_item(
        self,
        player_id: str,
        item_id: int,
    ) -> GenericCapcomQueueItem:
        self._require_station(player_id, "CAPCOM")
        item = next(
            (candidate for candidate in self.capcom_queue if candidate.item_id == item_id),
            None,
        )
        if item is None:
            raise ValueError(f"unknown CAPCOM item: {item_id}")
        if item.transmitted:
            raise ValueError(f"CAPCOM item already transmitted: {item_id}")

        item.transmitted = True
        item.transmitted_get_s = self.state.get_s
        self._audit(
            "capcom_item_transmitted",
            "CAPCOM",
            player_id=player_id,
            item_id=item.item_id,
            action=item.action,
        )
        return item

    def apply_session_injection(self, injection: Any) -> None:
        target = _nonempty_text(getattr(injection, "target", None), "injection target")
        if target not in self.injectable_variables:
            raise ValueError(f"unsupported scenario injection target: {target}")

        injection_get_s = float(getattr(injection, "get_s"))
        if abs(injection_get_s - self.state.get_s) > 1e-9:
            raise ValueError("generic runtime injection must target current GET")

        self.state.variables[target] = getattr(injection, "value")
        evidence = getattr(injection, "evidence_class", "")
        evidence_value = getattr(evidence, "value", str(evidence))
        self._audit(
            "state_injection_applied",
            "SIMSUP",
            injection_id=str(getattr(injection, "injection_id", "")),
            target=target,
            evidence_class=evidence_value,
            provenance=str(getattr(injection, "provenance", "")),
        )
