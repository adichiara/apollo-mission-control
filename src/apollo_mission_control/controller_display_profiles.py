"""Historical controller-display profile catalog.

A display profile can preserve field identity, semantics, units, provenance class,
and unresolved routing without pretending that controller-visible values can be
bound to simulation state. Runtime binding is explicitly gated.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CONTROLLER_DISPLAY_PROFILE_ROOT = ROOT / "data" / "controller_display_profiles"

ALLOWED_ORIGINS = {
    "spacecraft_downlink_or_ground_processing_unresolved",
    "ground_computed",
    "contextual",
}
ALLOWED_ROUTING = {"documented", "unresolved"}


def _text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"controller display profile {key!r} must be a non-empty string")
    return value.strip()


def _optional_text(data: dict[str, Any], key: str) -> str | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"controller display profile {key!r} must be text or null")
    return value.strip()


def _strings(data: dict[str, Any], key: str) -> tuple[str, ...]:
    raw = data.get(key, [])
    if not isinstance(raw, list) or not all(
        isinstance(item, str) and item.strip() for item in raw
    ):
        raise ValueError(f"controller display profile {key!r} must be a list of strings")
    return tuple(item.strip() for item in raw)


@dataclass(frozen=True)
class HistoricalDisplayField:
    field_id: str
    label: str
    meaning: str
    unit_or_states: str | None
    reference_frame: str | None
    data_origin: str
    routing_status: str
    source_category: str | None
    source_identifier: str | None
    display_mask: str | None
    provenance: tuple[str, ...]
    evidence_note: str

    def validated(self) -> "HistoricalDisplayField":
        if self.data_origin not in ALLOWED_ORIGINS:
            raise ValueError(f"unsupported data_origin: {self.data_origin!r}")
        if self.routing_status not in ALLOWED_ROUTING:
            raise ValueError(f"unsupported routing_status: {self.routing_status!r}")
        if self.routing_status == "unresolved":
            if self.source_identifier is not None:
                raise ValueError(
                    "unresolved field routing must not carry a source_identifier"
                )
        elif self.source_category is None or self.source_identifier is None:
            raise ValueError(
                "documented field routing requires source_category and source_identifier"
            )
        if not self.provenance:
            raise ValueError("historical display field requires provenance")
        return self

    @property
    def historically_bindable(self) -> bool:
        return self.routing_status == "documented"

    def to_public_dict(self) -> dict[str, object]:
        return {
            "field_id": self.field_id,
            "label": self.label,
            "meaning": self.meaning,
            "unit_or_states": self.unit_or_states,
            "reference_frame": self.reference_frame,
            "data_origin": self.data_origin,
            "routing_status": self.routing_status,
            "source_category": self.source_category,
            "source_identifier": self.source_identifier,
            "display_mask": self.display_mask,
            "historically_bindable": self.historically_bindable,
            "provenance": list(self.provenance),
            "evidence_note": self.evidence_note,
        }


@dataclass(frozen=True)
class ControllerDisplayProfileRecord:
    profile_id: str
    mission_profile_id: str
    display_id: str
    station_context: tuple[str, ...]
    status: str
    mixed_source_format_documented: bool
    historical_value_binding_executable: bool
    historical_display_timing_executable: bool
    fields: tuple[HistoricalDisplayField, ...]
    downstream_gates: tuple[str, ...]
    sources: tuple[str, ...]
    profile_path: Path

    def field(self, field_id: str) -> HistoricalDisplayField:
        requested = str(field_id).strip()
        for item in self.fields:
            if item.field_id == requested:
                return item
        raise ValueError(
            f"unknown field_id {requested!r} in display profile {self.profile_id!r}"
        )

    def require_historical_value_binding(self) -> None:
        if not self.historical_value_binding_executable:
            detail = "; ".join(self.downstream_gates) or "field routing unresolved"
            raise ValueError(
                f"historical field binding is unresolved for display profile "
                f"{self.profile_id!r}: {detail}"
            )

    def require_historical_display_timing(self) -> None:
        if not self.historical_display_timing_executable:
            raise ValueError(
                f"historical display timing is unresolved for display profile "
                f"{self.profile_id!r}"
            )

    def to_public_dict(self) -> dict[str, object]:
        return {
            "profile_id": self.profile_id,
            "mission_profile_id": self.mission_profile_id,
            "display_id": self.display_id,
            "station_context": list(self.station_context),
            "status": self.status,
            "mixed_source_format_documented": self.mixed_source_format_documented,
            "historical_value_binding_executable": self.historical_value_binding_executable,
            "historical_display_timing_executable": self.historical_display_timing_executable,
            "fields": [item.to_public_dict() for item in self.fields],
            "downstream_gates": list(self.downstream_gates),
            "sources": list(self.sources),
        }


def _field(payload: Any) -> HistoricalDisplayField:
    if not isinstance(payload, dict):
        raise ValueError("historical display field must be an object")
    record = HistoricalDisplayField(
        field_id=_text(payload, "field_id"),
        label=_text(payload, "label"),
        meaning=_text(payload, "meaning"),
        unit_or_states=_optional_text(payload, "unit_or_states"),
        reference_frame=_optional_text(payload, "reference_frame"),
        data_origin=_text(payload, "data_origin"),
        routing_status=_text(payload, "routing_status"),
        source_category=_optional_text(payload, "source_category"),
        source_identifier=_optional_text(payload, "source_identifier"),
        display_mask=_optional_text(payload, "display_mask"),
        provenance=_strings(payload, "provenance"),
        evidence_note=_text(payload, "evidence_note"),
    )
    return record.validated()


def load_controller_display_profile(
    path: str | Path,
) -> ControllerDisplayProfileRecord:
    profile_path = Path(path)
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"cannot load controller display profile {profile_path}: {exc}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError("controller display profile must contain a JSON object")

    raw_fields = data.get("fields")
    if not isinstance(raw_fields, list) or not raw_fields:
        raise ValueError("controller display profile fields must be a non-empty list")
    fields = tuple(_field(item) for item in raw_fields)
    ids = [item.field_id for item in fields]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate historical display field_id values")

    mixed = data.get("mixed_source_format_documented")
    binding = data.get("historical_value_binding_executable")
    timing = data.get("historical_display_timing_executable")
    if not isinstance(mixed, bool) or not isinstance(binding, bool) or not isinstance(timing, bool):
        raise ValueError("display profile execution flags must be boolean")

    gates = _strings(data, "downstream_gates")
    if binding and any(not item.historically_bindable for item in fields):
        raise ValueError(
            "binding-executable display profile cannot contain unresolved field routing"
        )
    if binding and gates:
        raise ValueError(
            "binding-executable display profile must not retain downstream_gates"
        )

    sources = _strings(data, "sources")
    if not sources:
        raise ValueError("controller display profile requires at least one source")

    return ControllerDisplayProfileRecord(
        profile_id=_text(data, "profile_id"),
        mission_profile_id=_text(data, "mission_profile_id"),
        display_id=_text(data, "display_id"),
        station_context=_strings(data, "station_context"),
        status=_text(data, "status"),
        mixed_source_format_documented=mixed,
        historical_value_binding_executable=binding,
        historical_display_timing_executable=timing,
        fields=fields,
        downstream_gates=gates,
        sources=sources,
        profile_path=profile_path,
    )


def discover_controller_display_profiles(
    root: str | Path = CONTROLLER_DISPLAY_PROFILE_ROOT,
) -> tuple[ControllerDisplayProfileRecord, ...]:
    records = tuple(
        load_controller_display_profile(path)
        for path in sorted(Path(root).glob("*.json"))
    )
    ids = [record.profile_id for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate controller display profile_id values")
    return records


def get_controller_display_profile(
    profile_id: str,
    root: str | Path = CONTROLLER_DISPLAY_PROFILE_ROOT,
) -> ControllerDisplayProfileRecord:
    requested = str(profile_id).strip()
    if not requested:
        raise ValueError("profile_id must not be empty")
    for record in discover_controller_display_profiles(root):
        if record.profile_id == requested:
            return record
    raise ValueError(f"unknown controller display profile_id: {requested}")
