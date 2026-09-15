"""Authoritative single-process session orchestration for the Apollo 13 PC+2 slice.

This module is intentionally framework-neutral. It joins the existing domain
model, controller projections, player presentations, controller reporting,
communications, and selected source-bounded nonnominal workflows into one
authoritative session without adding network/UI policy.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Iterable

from .capcom_presentation import build_pc2_capcom_presentation
from .control_presentation import build_pc2_control_presentation
from .controller_decisions import call_out_shutdown_criterion
from .controller_products import project_controller_products
from .event_eligibility import evaluate_event_eligibility
from .fido_retro_presentation import build_pc2_fido_retro_presentation
from .flight_presentation import build_pc2_flight_presentation
from .guido_presentation import build_pc2_guido_presentation
from .inco_presentation import build_pc2_inco_presentation
from .pc2_event_rules import PC2_EVENT_RULES
from .pc2_nominal import PC2State, SimEvent, apply_event, build_events
from .restart_logic import RestartEvaluation
from .scenario_injection import StateInjection, apply_state_injection
from .session_runtime import SessionStatus
from .simulated_crew import CrewInstructionRule, CrewProcedureRule, SimulatedCrew
from .shutdown_rules import RuleState, evaluate_pc2_shutdown_rules
from .telmu_presentation import build_pc2_telmu_presentation


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
    """Serializable single-station player snapshot retained for compatibility."""

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


PC2_INVERTER_TRANSFER_SEQUENCE = (
    "CB(11) EPS: INV 1 — close",
    "INVERTER — 1",
    "CB(16) EPS: INV 2 — open",
)
PC2_RESTART_PROCEDURE_ID = "pc2_premature_shutdown_restart"
PC2_RESTART_PROCEDURE_SEQUENCE = (
    "proceed_noun_97",
    "restart_manual_ullage",
    "press_engine_start",
    "descent_engine_command_override_on",
)
PC2_RESTART_PROCEDURE_PROVENANCE = (
    "Apollo 13 PC+2 Mission Rules Review and contemporaneous CAPCOM read-up; "
    "procedure briefed before the playable window; no response delay asserted"
)


PC2_INVERTER_TRANSFER_PROVENANCE = (
    "Apollo 13 LM Malfunction Procedures INVERTER caution flowchart; "
    "inverter 2 operating, alternate transfer to inverter 1; "
    "no numeric post-transfer dwell established"
)


@dataclass(frozen=True)
class BundledPlayerSessionSnapshot:
    """Serializable snapshot for a player owning multiple original stations.

    Station identities are deliberately preserved as keys.  A bundled player
    gains access to multiple station-scoped presentations; the underlying
    products, actions, readiness reports, and audit actors are not merged into a
    synthetic domain station.
    """

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


def _build_pc2_simulated_crew() -> SimulatedCrew:
    return SimulatedCrew(
        crew_id="CREW",
        procedures={
            PC2_RESTART_PROCEDURE_ID: CrewProcedureRule(
                procedure_id=PC2_RESTART_PROCEDURE_ID,
                steps=PC2_RESTART_PROCEDURE_SEQUENCE,
                provenance=PC2_RESTART_PROCEDURE_PROVENANCE,
            ),
        },
        rules={
            "callout_dps_shutdown_criterion": CrewInstructionRule(
                capcom_action="callout_dps_shutdown_criterion",
                acknowledgement="received",
                crew_action="command_dps_shutdown",
                forwarded_parameters=("criterion",),
                provenance=(
                    "Apollo 13 PC+2 ground-call shutdown rule; "
                    "exact cockpit choreography and response latency unresolved"
                ),
            ),
            "switch_lm_inverter": CrewInstructionRule(
                capcom_action="switch_lm_inverter",
                acknowledgement="received",
                crew_action="switch_lm_inverter",
                forwarded_parameters=("from_inverter", "to_inverter", "control_sequence"),
                provenance=PC2_INVERTER_TRANSFER_PROVENANCE,
            ),
        },
    )


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
    # Compatibility projection for existing one-player/one-station callers.
    # For multi-station players this stores the first assigned station only;
    # authoritative ownership lives in player_station_sets.
    station_assignments: dict[str, str] = field(default_factory=dict)
    player_station_sets: dict[str, tuple[str, ...]] = field(default_factory=dict)
    readiness_reports: list[ReadinessReport] = field(default_factory=list)
    capcom_queue: list[CapcomQueueItem] = field(default_factory=list)
    simulated_crew: SimulatedCrew = field(default_factory=_build_pc2_simulated_crew)
    restart_evaluation: RestartEvaluation | None = None
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

    @property
    def assigned_stations(self) -> tuple[str, ...]:
        return tuple(
            station
            for stations in self.player_station_sets.values()
            for station in stations
        )

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
        """Assign one station, preserving the original public API."""
        self.assign_stations(player_id, (station,))

    def assign_stations(self, player_id: str, stations: Iterable[str]) -> None:
        """Assign one player a set of original station identities.

        This supports low-player-count presentation without creating synthetic
        domain stations.  An original station may still belong to only one
        player at a time.
        """
        normalized = tuple(station.upper() for station in stations)
        if not normalized:
            raise ValueError("At least one station must be assigned")
        if len(set(normalized)) != len(normalized):
            raise ValueError("Duplicate station in player assignment")
        unsupported = [station for station in normalized if station not in _PRESENTATION_BUILDERS]
        if unsupported:
            raise ValueError(f"Unsupported station: {unsupported[0]}")
        if player_id in self.player_station_sets or player_id in self.station_assignments:
            raise ValueError(f"Player already assigned: {player_id}")

        occupied = set(self.assigned_stations)
        conflict = next((station for station in normalized if station in occupied), None)
        if conflict is not None:
            raise ValueError(f"Station already assigned: {conflict}")

        self.player_station_sets[player_id] = normalized
        self.station_assignments[player_id] = normalized[0]
        if len(normalized) == 1:
            self._audit(
                "station_assigned",
                "SESSION",
                player_id=player_id,
                station=normalized[0],
            )
        else:
            self._audit(
                "station_set_assigned",
                "SESSION",
                player_id=player_id,
                stations=list(normalized),
            )

    def join_or_rejoin_stations(
        self,
        player_id: str,
        stations: Iterable[str],
    ) -> None:
        """Join/rejoin an exact station set using runtime-owned semantics."""

        normalized = tuple(station.upper() for station in stations)
        existing = self.player_station_sets.get(player_id)
        if existing is None and player_id in self.station_assignments:
            existing = (self.station_assignments[player_id],)
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
        if stations is not None:
            return stations
        # Defensive compatibility for sessions constructed before the station-set
        # field existed or tests that manipulate the legacy mapping directly.
        if player_id in self.station_assignments:
            return (self.station_assignments[player_id],)
        raise ValueError(f"Player has no station assignment: {player_id}")

    def station_for(self, player_id: str) -> str:
        stations = self.stations_for(player_id)
        if len(stations) != 1:
            raise ValueError(
                f"Player {player_id} owns multiple stations; specify the station explicitly"
            )
        return stations[0]

    def owns_station(self, player_id: str, station: str) -> bool:
        return station.upper() in self.stations_for(player_id)

    def _require_station(self, player_id: str, station: str) -> str:
        normalized = station.upper()
        if normalized not in self.stations_for(player_id):
            raise ValueError(f"Player {player_id} is not assigned to {normalized}")
        return normalized

    def start(self) -> None:
        if self.status != SessionStatus.CREATED:
            raise ValueError("Session can only be started once")
        self.status = SessionStatus.RUNNING
        self.pause_reason = None
        self._audit("session_started", "SESSION")

    def pause(self) -> None:
        """Explicitly pause simulated mission time.

        Controller decisions do not pause GET. This method represents an actual
        game/session pause requested by the players or operator.
        """
        if self.status != SessionStatus.RUNNING:
            raise ValueError("Only a running session can be paused")
        self.status = SessionStatus.PAUSED
        self.pause_reason = "manual"
        self._audit("session_paused", "SESSION", reason=self.pause_reason)

    def resume(self) -> None:
        if self.status != SessionStatus.PAUSED:
            raise ValueError("Only a paused session can be resumed")
        prior_reason = self.pause_reason
        self.status = SessionStatus.RUNNING
        self.pause_reason = None
        self._audit("session_resumed", "SESSION", prior_reason=prior_reason)

    def _open_gate(self, gate: str, *, source_event: str) -> None:
        """Open a controller decision gate without stopping mission time."""
        self.pending_gate = gate
        self._audit(
            "decision_gate_opened",
            "SESSION",
            gate=gate,
            source_event=source_event,
            simulation_paused=False,
        )

    def advance_to(self, target_get_s: float) -> float:
        """Advance authoritative mission GET continuously up to ``target_get_s``.

        Controller gates constrain actions and downstream event eligibility; they
        do not stop GET. Only an explicit session pause stops advancement.

        Historical fixture events are nominal milestones. If their declared
        prerequisites are absent when their GET arrives, the event is recorded as
        missed and is not replayed retroactively after a late player decision.
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

            self.state.get_s = event.get_s

            if event.name == "final_go_no_go_poll":
                self.state.phase = "pc2_final_readiness"
                self.next_event_index += 1
                self._open_gate("flight_go", source_event=event.name)
                continue

            eligible, reason = evaluate_event_eligibility(
                self.state,
                event.name,
                PC2_EVENT_RULES,
            )
            self.next_event_index += 1
            if not eligible:
                self._audit(
                    "scenario_event_missed",
                    "SESSION",
                    event=event.name,
                    reason=reason,
                    pending_gate=self.pending_gate,
                )
                continue

            apply_event(self.state, event, self.fixture)
            self._audit("scenario_event_applied", "SESSION", event=event.name)

        self.state.get_s = target

        if self.next_event_index >= len(self.events):
            self.status = SessionStatus.COMPLETE
            self.pause_reason = None
            self._audit("session_completed", "SESSION")

        return float(self.state.get_s)

    def apply_session_injection(self, injection: StateInjection) -> None:
        """Apply an explicit source-state injection at the current session GET.

        This is a scenario-authoring / validation operation, not a controller
        action. It changes only the whitelisted source observation represented by
        ``StateInjection`` and does not evaluate a rule or announce a diagnosis.
        """
        if self.status != SessionStatus.RUNNING:
            raise ValueError("Session must be running to apply a scenario injection")
        if abs(float(injection.get_s) - float(self.state.get_s)) > 1e-6:
            raise ValueError("Session injection GET must equal the current authoritative GET")
        apply_state_injection(self.state, injection)
        self._audit(
            "state_injection_applied",
            "SIMSUP",
            injection_id=injection.injection_id,
            target=injection.target,
            value=injection.value,
            evidence_class=injection.evidence_class.value,
            provenance=injection.provenance,
        )

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
                "requested_by": item.requested_by,
                "action": item.action,
                "parameters": dict(item.parameters),
                "basis": item.basis,
                "transmitted": item.transmitted,
                "transmitted_get_s": item.transmitted_get_s,
            }
            for item in self.capcom_queue
        ]

    def get_station_view(self, player_id: str, station: str | None = None) -> Any:
        if station is None:
            station = self.station_for(player_id)
        else:
            station = self._require_station(player_id, station)
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
        view = self.get_station_view(player_id, station)
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

    def bundled_player_snapshot(self, player_id: str) -> BundledPlayerSessionSnapshot:
        stations = self.stations_for(player_id)
        return BundledPlayerSessionSnapshot(
            player_id=player_id,
            stations=stations,
            get_s=float(self.state.get_s),
            session_status=self.status.value,
            mission_phase=self.state.phase,
            pending_gate=self.pending_gate,
            pause_reason=self.pause_reason,
            presentations={
                station: asdict(self.get_station_view(player_id, station))
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
    ) -> ReadinessReport:
        if station is None:
            station = self.station_for(player_id)
        else:
            station = self._require_station(player_id, station)
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
        if not self.owns_station(player_id, "FLIGHT"):
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
        else:
            self.state.phase = "pc2_final_readiness"

    def _queue_capcom_item(
        self,
        *,
        requested_by: str,
        action: str,
        parameters: dict[str, Any] | None,
        basis: str,
    ) -> CapcomQueueItem:
        item = CapcomQueueItem(
            item_id=self._next_capcom_item_id,
            get_s=float(self.state.get_s),
            requested_by=requested_by,
            action=action,
            parameters=dict(parameters or {}),
            basis=basis,
        )
        self._next_capcom_item_id += 1
        self.capcom_queue.append(item)
        self._audit(
            "capcom_item_queued",
            requested_by,
            item_id=item.item_id,
            action=action,
            parameters=item.parameters,
            basis=basis,
        )
        return item

    def queue_capcom_instruction(
        self,
        flight_player_id: str,
        *,
        action: str,
        parameters: dict[str, Any] | None = None,
        basis: str,
    ) -> CapcomQueueItem:
        if not self.owns_station(flight_player_id, "FLIGHT"):
            raise ValueError("Only FLIGHT can approve this generic CAPCOM queue operation")
        return self._queue_capcom_item(
            requested_by="FLIGHT",
            action=action,
            parameters=parameters,
            basis=basis,
        )

    def record_control_delta_p_callout(self, control_player_id: str, *, basis: str) -> CapcomQueueItem:
        """Record CONTROL's ground-only ΔP shutdown callout decision.

        Primary Apollo 13 sources establish that fuel/oxidizer differential
        pressure greater than 25 psi was a ground-callout shutdown criterion.
        They do not establish an exact internal CONTROL→FLIGHT→CAPCOM approval
        sequence. The CAPCOM queue used here is therefore a project transport
        mechanism, not a claim about historical loop routing.
        """
        if not self.owns_station(control_player_id, "CONTROL"):
            raise ValueError("Only the CONTROL player can issue the PC+2 delta-P ground callout")

        projections = project_controller_products(self.state, self.fixture)
        rules = evaluate_pc2_shutdown_rules(projections, self.fixture)
        rule = rules["fuel_oxidizer_delta_p"]
        if rule.state != RuleState.TRIGGERED:
            raise ValueError("Fuel/oxidizer delta-P shutdown criterion is not currently triggered")

        decision = call_out_shutdown_criterion(
            get_s=self.state.get_s,
            station="CONTROL",
            product_name="dps.fuel_oxidizer_delta_p_psi",
            basis=basis,
        )
        self._audit(
            "controller_shutdown_callout_decision",
            "CONTROL",
            player_id=control_player_id,
            product_name=decision.product_name,
            decision=decision.decision.value,
            basis=decision.basis,
        )

        product = projections["CONTROL"].products["dps.fuel_oxidizer_delta_p_psi"]
        return self._queue_capcom_item(
            requested_by="CONTROL",
            action="callout_dps_shutdown_criterion",
            parameters={
                "criterion": "fuel_oxidizer_delta_p",
                "observed_delta_p_psi": product.value,
                "routing_note": "project CAPCOM queue; exact internal Apollo routing unresolved",
            },
            basis=basis,
        )

    def queue_inverter_transfer_instruction(
        self,
        flight_player_id: str,
        *,
        basis: str,
    ) -> CapcomQueueItem:
        """Queue the sourced inverter-2 to inverter-1 contingency transfer.

        This models FLIGHT approval and CAPCOM transport as project workflow
        boundaries. The exact historical front-room voice sequence for the
        hypothetical failure remains unresolved.
        """
        if not self.owns_station(flight_player_id, "FLIGHT"):
            raise ValueError("Only FLIGHT can approve the inverter-transfer instruction")
        if self.state.crew_inverter_warning_report is not True:
            raise ValueError(
                "Inverter transfer requires a current crew report of the onboard "
                "INVERTER caution"
            )
        if self.state.lm_inverter_switch_attempted:
            raise ValueError("Inverter transfer has already been attempted")

        return self._queue_capcom_item(
            requested_by="FLIGHT",
            action="switch_lm_inverter",
            parameters={
                "from_inverter": 2,
                "to_inverter": 1,
                "control_sequence": list(PC2_INVERTER_TRANSFER_SEQUENCE),
                "routing_note": (
                    "project FLIGHT→CAPCOM queue; exact hypothetical Apollo "
                    "front-room call sequence unresolved"
                ),
            },
            basis=basis,
        )

    def transmit_capcom_item(self, capcom_player_id: str, item_id: int) -> CapcomQueueItem:
        if not self.owns_station(capcom_player_id, "CAPCOM"):
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
            requested_by=item.requested_by,
            action=item.action,
            parameters=item.parameters,
        )
        return item
