"""Historical measurement/output profile catalog.

This module binds source-backed spacecraft measurement identities to the generic
measurement/output mapping model while keeping later telemetry-loading and
ground-presentation gates explicit.

A profile may therefore be executable at the vehicle measurement boundary while
remaining non-executable as a historical Mission Control product.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping

from .measurement_output_model import (
    MeasurementDefinition,
    MeasurementKind,
    MeasurementOutputSet,
    MeasurementSourceKind,
    evaluate_measurement_outputs,
)

ROOT = Path(__file__).resolve().parents[2]
MEASUREMENT_PROFILE_ROOT = ROOT / "data" / "measurement_profiles"


def _text(data: Mapping[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"measurement profile {key!r} must be a non-empty string")
    return value.strip()


def _strings(data: Mapping[str, Any], key: str) -> tuple[str, ...]:
    raw = data.get(key, [])
    if not isinstance(raw, list) or not all(
        isinstance(item, str) and item.strip() for item in raw
    ):
        raise ValueError(f"measurement profile {key!r} must be a list of strings")
    return tuple(item.strip() for item in raw)


@dataclass(frozen=True)
class HistoricalMeasurementRecord:
    measurement_id: str
    description: str
    kind: MeasurementKind
    source_kind: MeasurementSourceKind
    source_key: str | None
    fixed_value: float | bool | None
    unit: str | None
    provenance: tuple[str, ...]
    evidence_note: str

    def to_definition(self, *, vehicle_effectivity_id: str) -> MeasurementDefinition:
        return MeasurementDefinition(
            measurement_id=self.measurement_id,
            description=self.description,
            kind=self.kind,
            source_kind=self.source_kind,
            source_key=self.source_key,
            fixed_value=self.fixed_value,
            unit=self.unit,
            applicable_profiles=(vehicle_effectivity_id,),
            provenance=self.provenance,
        ).validated()

    def to_public_dict(self) -> dict[str, object]:
        return {
            "measurement_id": self.measurement_id,
            "description": self.description,
            "kind": self.kind.value,
            "source_kind": self.source_kind.value,
            "source_key": self.source_key,
            "fixed_value": self.fixed_value,
            "unit": self.unit,
            "provenance": list(self.provenance),
            "evidence_note": self.evidence_note,
        }


@dataclass(frozen=True)
class MeasurementProfileRecord:
    profile_id: str
    mission_profile_id: str
    vehicle_effectivity_id: str
    status: str
    applicability: str
    measurement_mapping_executable: bool
    historical_ground_product_executable: bool
    measurements: tuple[HistoricalMeasurementRecord, ...]
    downstream_gates: tuple[str, ...]
    source_count: int
    profile_path: Path

    def measurement(self, measurement_id: str) -> HistoricalMeasurementRecord:
        requested = str(measurement_id).strip()
        for record in self.measurements:
            if record.measurement_id == requested:
                return record
        raise ValueError(
            f"unknown measurement_id {requested!r} in measurement profile "
            f"{self.profile_id}"
        )

    def definitions(self) -> tuple[MeasurementDefinition, ...]:
        if not self.measurement_mapping_executable:
            raise ValueError(
                f"measurement profile {self.profile_id!r} is not executable at "
                "the source-to-measurement boundary"
            )
        return tuple(
            record.to_definition(
                vehicle_effectivity_id=self.vehicle_effectivity_id
            )
            for record in self.measurements
        )

    def evaluate_source_state(
        self,
        source_state: Mapping[str, Any],
    ) -> MeasurementOutputSet:
        """Evaluate the sourced vehicle measurement boundary only.

        This method does not imply that the measurement was loaded into the
        mission's live PCM format, routed through MCC, or visible at a controller
        console. Those are separate downstream gates.
        """

        return evaluate_measurement_outputs(
            source_state,
            self.definitions(),
            active_profile=self.vehicle_effectivity_id,
            applicability=(
                f"historical measurement profile {self.profile_id}; "
                "vehicle measurement boundary only"
            ),
            provenance=tuple(
                provenance
                for record in self.measurements
                for provenance in record.provenance
            ),
        )

    def require_historical_ground_product(self) -> None:
        if not self.historical_ground_product_executable:
            unresolved = "; ".join(self.downstream_gates) or "downstream gates unresolved"
            raise ValueError(
                f"historical ground product is unresolved for measurement profile "
                f"{self.profile_id!r}: {unresolved}"
            )

    def to_public_dict(self) -> dict[str, object]:
        return {
            "profile_id": self.profile_id,
            "mission_profile_id": self.mission_profile_id,
            "vehicle_effectivity_id": self.vehicle_effectivity_id,
            "status": self.status,
            "applicability": self.applicability,
            "measurement_mapping_executable": self.measurement_mapping_executable,
            "historical_ground_product_executable": (
                self.historical_ground_product_executable
            ),
            "measurement_stage": "vehicle_measurement_output_pre_ground_loading",
            "measurements": [
                measurement.to_public_dict() for measurement in self.measurements
            ],
            "downstream_gates": list(self.downstream_gates),
            "source_count": self.source_count,
        }


def _measurement(payload: Any) -> HistoricalMeasurementRecord:
    if not isinstance(payload, dict):
        raise ValueError("historical measurement record must be an object")

    kind = MeasurementKind(_text(payload, "kind"))
    source_kind = MeasurementSourceKind(_text(payload, "source_kind"))

    source_key = payload.get("source_key")
    if source_key is not None:
        if not isinstance(source_key, str) or not source_key.strip():
            raise ValueError("measurement profile source_key must be non-empty or null")
        source_key = source_key.strip()

    fixed_value = payload.get("fixed_value")
    unit = payload.get("unit")
    if unit is not None:
        if not isinstance(unit, str) or not unit.strip():
            raise ValueError("measurement profile unit must be non-empty or null")
        unit = unit.strip()

    provenance = _strings(payload, "provenance")

    record = HistoricalMeasurementRecord(
        measurement_id=_text(payload, "measurement_id"),
        description=_text(payload, "description"),
        kind=kind,
        source_kind=source_kind,
        source_key=source_key,
        fixed_value=fixed_value,
        unit=unit,
        provenance=provenance,
        evidence_note=_text(payload, "evidence_note"),
    )

    # Reuse the generic contract as the final shape validator without claiming
    # any particular mission effectivity here.
    record.to_definition(vehicle_effectivity_id="validation_only")
    return record


def load_measurement_profile(path: str | Path) -> MeasurementProfileRecord:
    profile_path = Path(path)
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load measurement profile {profile_path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("measurement profile must contain a JSON object")

    raw_measurements = data.get("measurements")
    if not isinstance(raw_measurements, list) or not raw_measurements:
        raise ValueError("measurement profile measurements must be a non-empty list")
    measurements = tuple(_measurement(item) for item in raw_measurements)

    ids = [item.measurement_id for item in measurements]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate historical measurement_id values")

    mapping_executable = data.get("measurement_mapping_executable")
    if not isinstance(mapping_executable, bool):
        raise ValueError(
            "measurement profile 'measurement_mapping_executable' must be boolean"
        )
    ground_executable = data.get("historical_ground_product_executable")
    if not isinstance(ground_executable, bool):
        raise ValueError(
            "measurement profile 'historical_ground_product_executable' must be boolean"
        )

    downstream_gates = _strings(data, "downstream_gates")
    if ground_executable and downstream_gates:
        raise ValueError(
            "ground-executable measurement profile must not retain downstream_gates"
        )

    sources = _strings(data, "sources")
    if not sources:
        raise ValueError("measurement profile requires at least one source")

    record = MeasurementProfileRecord(
        profile_id=_text(data, "profile_id"),
        mission_profile_id=_text(data, "mission_profile_id"),
        vehicle_effectivity_id=_text(data, "vehicle_effectivity_id"),
        status=_text(data, "status"),
        applicability=_text(data, "applicability"),
        measurement_mapping_executable=mapping_executable,
        historical_ground_product_executable=ground_executable,
        measurements=measurements,
        downstream_gates=downstream_gates,
        source_count=len(sources),
        profile_path=profile_path,
    )

    if record.measurement_mapping_executable:
        record.definitions()

    return record


def discover_measurement_profiles(
    root: str | Path = MEASUREMENT_PROFILE_ROOT,
) -> tuple[MeasurementProfileRecord, ...]:
    profile_root = Path(root)
    records = tuple(
        load_measurement_profile(path)
        for path in sorted(profile_root.glob("*.json"))
    )

    ids = [record.profile_id for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate measurement profile_id values")
    return records


def get_measurement_profile(
    profile_id: str,
    root: str | Path = MEASUREMENT_PROFILE_ROOT,
) -> MeasurementProfileRecord:
    requested = str(profile_id).strip()
    if not requested:
        raise ValueError("profile_id must not be empty")
    for record in discover_measurement_profiles(root):
        if record.profile_id == requested:
            return record
    raise ValueError(f"unknown measurement profile_id: {requested}")
