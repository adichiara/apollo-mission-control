"""Controller-judgment decision-gate contract.

The contract assembles documented station cues and readiness reports for a
decision point without turning them into an automatic mission decision.

It is intentionally mission-neutral. Historical cue identity, station
ownership, poll order, and authority live in mission-specific profile data.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable, Mapping


def _text(value: str, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


class ReadinessCallState(str, Enum):
    GO = "go"
    NO_GO = "no_go"
    NOT_REPORTED = "not_reported"


@dataclass(frozen=True)
class CueEvidence:
    """Caller-supplied observation for one documented decision cue."""

    value: Any = None
    available: bool = True
    provenance: tuple[str, ...] = ()

    def validated(self) -> "CueEvidence":
        return CueEvidence(
            value=self.value,
            available=bool(self.available),
            provenance=tuple(
                _text(item, "cue provenance") for item in self.provenance
            ),
        )


@dataclass(frozen=True)
class ControllerReadinessReport:
    station_id: str
    state: ReadinessCallState
    basis: str = ""

    def validated(self) -> "ControllerReadinessReport":
        basis = str(self.basis).strip()
        return ControllerReadinessReport(
            station_id=_text(self.station_id, "readiness station_id"),
            state=ReadinessCallState(self.state),
            basis=basis,
        )


@dataclass(frozen=True)
class ControllerDecisionGateContract:
    gate_id: str
    phase_context: str
    decision_mode: str
    decision_authority: str
    relay_station: str
    cue_owners: Mapping[str, str]
    poll_stations: tuple[str, ...]
    poll_labels: Mapping[str, str]
    provenance: tuple[str, ...] = ()

    def validated(self) -> "ControllerDecisionGateContract":
        gate_id = _text(self.gate_id, "gate_id")
        phase_context = _text(self.phase_context, "phase_context")
        mode = _text(self.decision_mode, "decision_mode")
        if mode != "controller_judgment":
            raise ValueError(
                "controller decision-gate contract requires "
                "decision_mode='controller_judgment'"
            )
        authority = _text(self.decision_authority, "decision_authority")
        relay = _text(self.relay_station, "relay_station")

        cue_owners: dict[str, str] = {}
        for raw_cue, raw_station in self.cue_owners.items():
            cue = _text(raw_cue, "cue_id")
            station = _text(raw_station, f"owner for cue {cue}")
            if cue in cue_owners:
                raise ValueError(f"duplicate cue_id: {cue}")
            cue_owners[cue] = station
        if not cue_owners:
            raise ValueError("at least one documented cue is required")

        stations = tuple(_text(item, "poll station") for item in self.poll_stations)
        if not stations:
            raise ValueError("at least one poll station is required")
        if len(stations) != len(set(stations)):
            raise ValueError("poll stations must be unique")

        labels: dict[str, str] = {}
        for station in stations:
            raw = self.poll_labels.get(station)
            if raw is None:
                raise ValueError(f"missing poll label for station {station}")
            labels[station] = _text(raw, f"poll label for {station}")

        unknown_labels = set(self.poll_labels) - set(stations)
        if unknown_labels:
            raise ValueError(
                "poll labels contain stations outside poll order: "
                + ", ".join(sorted(unknown_labels))
            )

        return ControllerDecisionGateContract(
            gate_id=gate_id,
            phase_context=phase_context,
            decision_mode=mode,
            decision_authority=authority,
            relay_station=relay,
            cue_owners=cue_owners,
            poll_stations=stations,
            poll_labels=labels,
            provenance=tuple(
                _text(item, "contract provenance") for item in self.provenance
            ),
        )


@dataclass(frozen=True)
class DecisionCueSnapshot:
    cue_id: str
    station_id: str
    available: bool
    value: Any
    provenance: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "cue_id": self.cue_id,
            "station_id": self.station_id,
            "available": self.available,
            "value": self.value,
            "provenance": list(self.provenance),
        }


@dataclass(frozen=True)
class DecisionGateSnapshot:
    gate_id: str
    phase_context: str
    decision_mode: str
    decision_authority: str
    relay_station: str
    cues: tuple[DecisionCueSnapshot, ...]
    readiness_reports: tuple[ControllerReadinessReport, ...]
    poll_order: tuple[str, ...]
    provenance: tuple[str, ...]

    @property
    def cue_coverage_complete(self) -> bool:
        """Whether every documented cue has an explicit available observation.

        This is a contract/debugging completeness signal, not a GO/NO-GO rule.
        """
        return all(item.available for item in self.cues)

    @property
    def poll_complete(self) -> bool:
        """Whether every station in the documented poll has reported."""
        by_station = {item.station_id: item.state for item in self.readiness_reports}
        return all(
            by_station.get(station) not in (None, ReadinessCallState.NOT_REPORTED)
            for station in self.poll_order
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "gate_id": self.gate_id,
            "phase_context": self.phase_context,
            "decision_mode": self.decision_mode,
            "decision_authority": self.decision_authority,
            "relay_station": self.relay_station,
            "cues": [item.to_dict() for item in self.cues],
            "readiness_reports": [
                {
                    "station_id": item.station_id,
                    "state": item.state.value,
                    "basis": item.basis,
                }
                for item in self.readiness_reports
            ],
            "poll_order": list(self.poll_order),
            "cue_coverage_complete": self.cue_coverage_complete,
            "poll_complete": self.poll_complete,
            "controller_decision_required": True,
            "provenance": list(self.provenance),
        }


def assemble_decision_gate_snapshot(
    contract: ControllerDecisionGateContract,
    *,
    cues: Mapping[str, CueEvidence] | None = None,
    readiness_reports: Iterable[ControllerReadinessReport] = (),
) -> DecisionGateSnapshot:
    """Assemble decision evidence without computing the controller decision."""

    checked = contract.validated()
    supplied = dict(cues or {})

    unknown_cues = set(supplied) - set(checked.cue_owners)
    if unknown_cues:
        raise ValueError(
            "unknown decision-gate cues: " + ", ".join(sorted(unknown_cues))
        )

    cue_snapshots: list[DecisionCueSnapshot] = []
    for cue_id, station_id in checked.cue_owners.items():
        evidence = supplied.get(cue_id)
        if evidence is None:
            cue_snapshots.append(
                DecisionCueSnapshot(
                    cue_id=cue_id,
                    station_id=station_id,
                    available=False,
                    value=None,
                    provenance=("not_supplied",),
                )
            )
            continue
        item = evidence.validated()
        cue_snapshots.append(
            DecisionCueSnapshot(
                cue_id=cue_id,
                station_id=station_id,
                available=item.available,
                value=item.value,
                provenance=item.provenance,
            )
        )

    reports: list[ControllerReadinessReport] = []
    seen: set[str] = set()
    allowed = set(checked.poll_stations)
    for raw_report in readiness_reports:
        report = raw_report.validated()
        if report.station_id not in allowed:
            raise ValueError(
                f"station {report.station_id!r} is not in gate poll order"
            )
        if report.station_id in seen:
            raise ValueError(
                f"duplicate readiness report for station {report.station_id}"
            )
        seen.add(report.station_id)
        reports.append(report)

    return DecisionGateSnapshot(
        gate_id=checked.gate_id,
        phase_context=checked.phase_context,
        decision_mode=checked.decision_mode,
        decision_authority=checked.decision_authority,
        relay_station=checked.relay_station,
        cues=tuple(cue_snapshots),
        readiness_reports=tuple(reports),
        poll_order=checked.poll_stations,
        provenance=checked.provenance,
    )
