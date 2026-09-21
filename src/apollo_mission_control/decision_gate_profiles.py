"""Historical controller decision-gate profile catalog.

Profiles describe sourced information/call topology. They do not encode or
execute an automatic mission GO/NO-GO decision.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

from .decision_gate import ControllerDecisionGateContract

ROOT = Path(__file__).resolve().parents[2]
DECISION_GATE_PROFILE_ROOT = ROOT / "data" / "decision_gate_profiles"


def _text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(
            f"decision-gate profile {key!r} must be a non-empty string"
        )
    return value.strip()


def _string_list(data: dict[str, Any], key: str) -> tuple[str, ...]:
    value = data.get(key, [])
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        raise ValueError(f"decision-gate profile {key!r} must be a list of strings")
    return tuple(item.strip() for item in value)


@dataclass(frozen=True)
class DecisionGateCueRecord:
    cue_id: str
    station_id: str
    historical_call_label: str
    evidence_kind: str
    source_reference: str
    semantics: str
    provenance: tuple[str, ...]

    def to_public_dict(self) -> dict[str, object]:
        return {
            "cue_id": self.cue_id,
            "station_id": self.station_id,
            "historical_call_label": self.historical_call_label,
            "evidence_kind": self.evidence_kind,
            "source_reference": self.source_reference,
            "semantics": self.semantics,
            "provenance": list(self.provenance),
        }


@dataclass(frozen=True)
class DecisionGatePollRecord:
    station_id: str
    historical_call_label: str

    def to_public_dict(self) -> dict[str, str]:
        return {
            "station_id": self.station_id,
            "historical_call_label": self.historical_call_label,
        }


@dataclass(frozen=True)
class DecisionGateProfileRecord:
    profile_id: str
    mission_profile_id: str
    gate_id: str
    status: str
    phase_context: str
    decision_mode: str
    decision_authority: str
    relay_station: str
    cues: tuple[DecisionGateCueRecord, ...]
    poll_order: tuple[DecisionGatePollRecord, ...]
    rule_references: tuple[str, ...]
    unresolved: tuple[str, ...]
    sources: tuple[str, ...]
    profile_path: Path

    def cue(self, cue_id: str) -> DecisionGateCueRecord:
        requested = str(cue_id).strip()
        for item in self.cues:
            if item.cue_id == requested:
                return item
        raise ValueError(
            f"unknown cue_id {requested!r} in decision-gate profile {self.profile_id}"
        )

    def to_contract(self) -> ControllerDecisionGateContract:
        return ControllerDecisionGateContract(
            gate_id=self.gate_id,
            phase_context=self.phase_context,
            decision_mode=self.decision_mode,
            decision_authority=self.decision_authority,
            relay_station=self.relay_station,
            cue_owners={item.cue_id: item.station_id for item in self.cues},
            poll_stations=tuple(item.station_id for item in self.poll_order),
            poll_labels={
                item.station_id: item.historical_call_label
                for item in self.poll_order
            },
            provenance=self.sources,
        ).validated()

    def to_public_dict(self) -> dict[str, object]:
        return {
            "profile_id": self.profile_id,
            "mission_profile_id": self.mission_profile_id,
            "gate_id": self.gate_id,
            "status": self.status,
            "phase_context": self.phase_context,
            "decision_mode": self.decision_mode,
            "decision_authority": self.decision_authority,
            "relay_station": self.relay_station,
            "cues": [item.to_public_dict() for item in self.cues],
            "poll_order": [item.to_public_dict() for item in self.poll_order],
            "rule_references": list(self.rule_references),
            "unresolved": list(self.unresolved),
            "sources": list(self.sources),
            "automatic_mission_decision": False,
        }


def _cue(payload: Any) -> DecisionGateCueRecord:
    if not isinstance(payload, dict):
        raise ValueError("decision-gate cue must be an object")
    provenance = _string_list(payload, "provenance")
    return DecisionGateCueRecord(
        cue_id=_text(payload, "cue_id"),
        station_id=_text(payload, "station_id"),
        historical_call_label=_text(payload, "historical_call_label"),
        evidence_kind=_text(payload, "evidence_kind"),
        source_reference=_text(payload, "source_reference"),
        semantics=_text(payload, "semantics"),
        provenance=provenance,
    )


def _poll_record(payload: Any) -> DecisionGatePollRecord:
    if not isinstance(payload, dict):
        raise ValueError("decision-gate poll entry must be an object")
    return DecisionGatePollRecord(
        station_id=_text(payload, "station_id"),
        historical_call_label=_text(payload, "historical_call_label"),
    )


def load_decision_gate_profile(path: str | Path) -> DecisionGateProfileRecord:
    profile_path = Path(path)
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"cannot load decision-gate profile {profile_path}: {exc}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError("decision-gate profile must contain a JSON object")

    raw_cues = data.get("cues")
    if not isinstance(raw_cues, list) or not raw_cues:
        raise ValueError("decision-gate profile cues must be a non-empty list")
    cues = tuple(_cue(item) for item in raw_cues)
    cue_ids = [item.cue_id for item in cues]
    if len(cue_ids) != len(set(cue_ids)):
        raise ValueError("duplicate decision-gate cue_id")

    raw_poll = data.get("poll_order")
    if not isinstance(raw_poll, list) or not raw_poll:
        raise ValueError("decision-gate profile poll_order must be a non-empty list")
    poll = tuple(_poll_record(item) for item in raw_poll)
    station_ids = [item.station_id for item in poll]
    if len(station_ids) != len(set(station_ids)):
        raise ValueError("duplicate decision-gate poll station")

    record = DecisionGateProfileRecord(
        profile_id=_text(data, "profile_id"),
        mission_profile_id=_text(data, "mission_profile_id"),
        gate_id=_text(data, "gate_id"),
        status=_text(data, "status"),
        phase_context=_text(data, "phase_context"),
        decision_mode=_text(data, "decision_mode"),
        decision_authority=_text(data, "decision_authority"),
        relay_station=_text(data, "relay_station"),
        cues=cues,
        poll_order=poll,
        rule_references=_string_list(data, "rule_references"),
        unresolved=_string_list(data, "unresolved"),
        sources=_string_list(data, "sources"),
        profile_path=profile_path,
    )
    record.to_contract()
    return record


def discover_decision_gate_profiles(
    root: str | Path = DECISION_GATE_PROFILE_ROOT,
) -> tuple[DecisionGateProfileRecord, ...]:
    records = tuple(
        load_decision_gate_profile(path)
        for path in sorted(Path(root).glob("*.json"))
    )
    ids = [item.profile_id for item in records]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate decision-gate profile_id")
    return records


def get_decision_gate_profile(
    profile_id: str,
    root: str | Path = DECISION_GATE_PROFILE_ROOT,
) -> DecisionGateProfileRecord:
    requested = str(profile_id).strip()
    if not requested:
        raise ValueError("profile_id must not be empty")
    for record in discover_decision_gate_profiles(root):
        if record.profile_id == requested:
            return record
    raise ValueError(f"unknown decision-gate profile_id: {requested}")
