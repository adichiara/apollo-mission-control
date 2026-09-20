"""Controller-product field provenance and historical routing gates.

This layer sits downstream of vehicle measurements / onboard state and upstream
of a player-facing controller rendering. It preserves field identity, origin,
routing confidence, units, and provenance without silently turning a semantic
field match into a historical data route.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[2]
CONTROLLER_PRODUCT_PROFILE_ROOT = ROOT / "data" / "controller_product_profiles"


class ControllerFieldOrigin(str, Enum):
    CONTEXTUAL = "contextual"
    SPACECRAFT_DOWNLINK = "spacecraft_downlink"
    ONBOARD_COMPUTED = "onboard_computed"
    GROUND_DERIVED = "ground_derived"
    MIXED = "mixed"
    UNRESOLVED = "unresolved"


class HistoricalRoutingState(str, Enum):
    RESOLVED = "resolved"
    PARTIAL = "partial"
    UNRESOLVED = "unresolved"


def _text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()


def _optional_text(value: Any, name: str) -> str | None:
    if value is None:
        return None
    return _text(value, name)


def _strings(value: Any, name: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        raise ValueError(f"{name} must be a list of non-empty strings")
    return tuple(item.strip() for item in value)


@dataclass(frozen=True)
class ControllerFieldDefinition:
    field_id: str
    label: str
    description: str
    origin: ControllerFieldOrigin
    routing_state: HistoricalRoutingState
    unit: str | None = None
    display_format: str | None = None
    source_key: str | None = None
    transform_id: str | None = None
    provenance: tuple[str, ...] = ()
    evidence_note: str = ""

    def validated(self) -> "ControllerFieldDefinition":
        field_id = _text(self.field_id, "field_id")
        routing = HistoricalRoutingState(self.routing_state)
        source_key = _optional_text(self.source_key, "source_key")
        transform_id = _optional_text(self.transform_id, "transform_id")

        if routing == HistoricalRoutingState.RESOLVED and source_key is None:
            raise ValueError(
                f"controller field {field_id} resolved route requires source_key"
            )
        if routing == HistoricalRoutingState.UNRESOLVED and (
            source_key is not None or transform_id is not None
        ):
            raise ValueError(
                f"controller field {field_id} unresolved route must not bind "
                "source_key or transform_id"
            )

        return ControllerFieldDefinition(
            field_id=field_id,
            label=_text(self.label, "label"),
            description=_text(self.description, "description"),
            origin=ControllerFieldOrigin(self.origin),
            routing_state=routing,
            unit=_optional_text(self.unit, "unit"),
            display_format=_optional_text(self.display_format, "display_format"),
            source_key=source_key,
            transform_id=transform_id,
            provenance=tuple(
                str(item).strip() for item in self.provenance if str(item).strip()
            ),
            evidence_note=_text(self.evidence_note, "evidence_note"),
        )

    def to_public_dict(self) -> dict[str, object]:
        return {
            "field_id": self.field_id,
            "label": self.label,
            "description": self.description,
            "origin": self.origin.value,
            "routing_state": self.routing_state.value,
            "unit": self.unit,
            "display_format": self.display_format,
            "source_key": self.source_key,
            "transform_id": self.transform_id,
            "provenance": list(self.provenance),
            "evidence_note": self.evidence_note,
        }


@dataclass(frozen=True)
class ControllerFieldValue:
    definition: ControllerFieldDefinition
    value: Any
    available: bool
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        payload = self.definition.to_public_dict()
        payload.update(
            {
                "value": self.value,
                "available": self.available,
                "reasons": list(self.reasons),
            }
        )
        return payload


@dataclass(frozen=True)
class ControllerProductProfile:
    profile_id: str
    mission_profile_id: str
    display_id: str
    status: str
    historical_rendering_executable: bool
    fields: tuple[ControllerFieldDefinition, ...]
    unresolved: tuple[str, ...]
    sources: tuple[str, ...]
    profile_path: Path

    def field(self, field_id: str) -> ControllerFieldDefinition:
        key = str(field_id).strip()
        for field in self.fields:
            if field.field_id == key:
                return field
        raise ValueError(f"unknown controller field {key!r} in {self.profile_id}")

    def require_historical_rendering(self) -> None:
        if not self.historical_rendering_executable:
            raise ValueError(
                f"controller product profile {self.profile_id!r} is not "
                "historically executable; unresolved field routing remains"
            )

    def evaluate(
        self,
        source_state: Mapping[str, Any],
    ) -> tuple[ControllerFieldValue, ...]:
        """Evaluate only fields whose historical route is explicitly resolved."""

        values: list[ControllerFieldValue] = []
        for definition in self.fields:
            field = definition.validated()
            if field.routing_state != HistoricalRoutingState.RESOLVED:
                values.append(
                    ControllerFieldValue(
                        definition=field,
                        value=None,
                        available=False,
                        reasons=(f"historical_route_{field.routing_state.value}",),
                    )
                )
                continue

            assert field.source_key is not None
            if field.source_key not in source_state:
                raise ValueError(
                    f"controller field {field.field_id} references missing source "
                    f"{field.source_key!r}"
                )
            values.append(
                ControllerFieldValue(
                    definition=field,
                    value=source_state[field.source_key],
                    available=True,
                    reasons=(),
                )
            )
        return tuple(values)

    def to_public_dict(self) -> dict[str, object]:
        return {
            "profile_id": self.profile_id,
            "mission_profile_id": self.mission_profile_id,
            "display_id": self.display_id,
            "status": self.status,
            "historical_rendering_executable": self.historical_rendering_executable,
            "fields": [field.to_public_dict() for field in self.fields],
            "unresolved": list(self.unresolved),
            "sources": list(self.sources),
        }


def _field(payload: Any) -> ControllerFieldDefinition:
    if not isinstance(payload, dict):
        raise ValueError("controller product field must be an object")
    return ControllerFieldDefinition(
        field_id=_text(payload.get("field_id"), "field_id"),
        label=_text(payload.get("label"), "label"),
        description=_text(payload.get("description"), "description"),
        origin=ControllerFieldOrigin(_text(payload.get("origin"), "origin")),
        routing_state=HistoricalRoutingState(
            _text(payload.get("routing_state"), "routing_state")
        ),
        unit=_optional_text(payload.get("unit"), "unit"),
        display_format=_optional_text(payload.get("display_format"), "display_format"),
        source_key=_optional_text(payload.get("source_key"), "source_key"),
        transform_id=_optional_text(payload.get("transform_id"), "transform_id"),
        provenance=_strings(payload.get("provenance", []), "provenance"),
        evidence_note=_text(payload.get("evidence_note"), "evidence_note"),
    ).validated()


def load_controller_product_profile(
    path: str | Path,
) -> ControllerProductProfile:
    profile_path = Path(path)
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"cannot load controller product profile {profile_path}: {exc}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError("controller product profile must contain an object")

    raw_fields = data.get("fields")
    if not isinstance(raw_fields, list) or not raw_fields:
        raise ValueError("controller product profile fields must be a non-empty list")
    fields = tuple(_field(item) for item in raw_fields)
    ids = [field.field_id for field in fields]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate controller product field_id")

    record = ControllerProductProfile(
        profile_id=_text(data.get("profile_id"), "profile_id"),
        mission_profile_id=_text(data.get("mission_profile_id"), "mission_profile_id"),
        display_id=_text(data.get("display_id"), "display_id"),
        status=_text(data.get("status"), "status"),
        historical_rendering_executable=bool(
            data.get("historical_rendering_executable", False)
        ),
        fields=fields,
        unresolved=_strings(data.get("unresolved", []), "unresolved"),
        sources=_strings(data.get("sources", []), "sources"),
        profile_path=profile_path,
    )

    if record.historical_rendering_executable and any(
        field.routing_state != HistoricalRoutingState.RESOLVED
        for field in record.fields
    ):
        raise ValueError(
            f"controller product profile {record.profile_id!r} claims historical "
            "execution with unresolved/partial field routing"
        )
    return record


def discover_controller_product_profiles(
    root: str | Path = CONTROLLER_PRODUCT_PROFILE_ROOT,
) -> tuple[ControllerProductProfile, ...]:
    records = tuple(
        load_controller_product_profile(path)
        for path in sorted(Path(root).glob("*.json"))
    )
    ids = [record.profile_id for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate controller product profile_id")
    return records


def get_controller_product_profile(
    profile_id: str,
    root: str | Path = CONTROLLER_PRODUCT_PROFILE_ROOT,
) -> ControllerProductProfile:
    requested = str(profile_id).strip()
    if not requested:
        raise ValueError("profile_id must not be empty")
    for record in discover_controller_product_profiles(root):
        if record.profile_id == requested:
            return record
    raise ValueError(f"unknown controller product profile_id: {requested}")
