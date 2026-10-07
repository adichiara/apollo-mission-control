"""Scenario discovery and metadata boundary for the reusable simulator.

This module deliberately knows nothing about PC+2 session behavior. It discovers
scenario fixtures, validates the small cross-scenario metadata contract, and
returns the raw fixture only when a runtime adapter asks for it.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SCENARIO_ROOT = ROOT / "data" / "scenarios"
DEFAULT_SCENARIO_ID = "apollo13_pc2_nominal"


def _text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"scenario metadata {key!r} must be a non-empty string")
    return value.strip()


def _number(data: dict[str, Any], key: str) -> float:
    value = data.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"scenario metadata {key!r} must be numeric")
    return float(value)


def _string_list(data: dict[str, Any], key: str) -> tuple[str, ...]:
    value = data.get(key)
    if not isinstance(value, list) or not value:
        raise ValueError(f"scenario metadata {key!r} must be a non-empty list")
    result: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ValueError(
                f"scenario metadata {key!r} must contain non-empty strings"
            )
        normalized = item.strip()
        if normalized not in result:
            result.append(normalized)
    return tuple(result)


@dataclass(frozen=True)
class ScenarioRecord:
    scenario_id: str
    title: str
    mission: str
    status: str
    scenario_class: str
    runtime_adapter: str
    mission_profile_id: str
    model_profile_id: str
    required_model_domains: tuple[str, ...]
    start_get_s: float
    start_get_hms: str
    end_target_get_hms: str
    vehicle_configuration: str
    source_count: int
    fixture_path: Path
    execution_enabled: bool = True
    execution_gate_reason: str | None = None

    def to_public_dict(self) -> dict[str, object]:
        return {
            "scenario_id": self.scenario_id,
            "title": self.title,
            "mission": self.mission,
            "status": self.status,
            "scenario_class": self.scenario_class,
            "runtime_adapter": self.runtime_adapter,
            "mission_profile_id": self.mission_profile_id,
            "model_profile_id": self.model_profile_id,
            "required_model_domains": list(self.required_model_domains),
            "start_get_s": self.start_get_s,
            "start_get_hms": self.start_get_hms,
            "end_target_get_hms": self.end_target_get_hms,
            "vehicle_configuration": self.vehicle_configuration,
            "source_count": self.source_count,
            "execution_enabled": self.execution_enabled,
            "execution_gate_reason": self.execution_gate_reason,
        }


def load_scenario_record(path: str | Path) -> ScenarioRecord:
    fixture_path = Path(path)
    try:
        data = json.loads(fixture_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load scenario fixture {fixture_path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"scenario fixture {fixture_path} must contain a JSON object")

    sources = data.get("sources", [])
    if not isinstance(sources, list) or not all(isinstance(item, str) for item in sources):
        raise ValueError("scenario metadata 'sources' must be a list of strings")

    execution_enabled = data.get("execution_enabled", True)
    if not isinstance(execution_enabled, bool):
        raise ValueError("scenario metadata 'execution_enabled' must be boolean")
    raw_gate_reason = data.get("execution_gate_reason")
    if raw_gate_reason is None:
        execution_gate_reason = None
    elif isinstance(raw_gate_reason, str) and raw_gate_reason.strip():
        execution_gate_reason = raw_gate_reason.strip()
    else:
        raise ValueError(
            "scenario metadata 'execution_gate_reason' must be a non-empty string or null"
        )
    if not execution_enabled and execution_gate_reason is None:
        raise ValueError(
            "execution_gate_reason is required when scenario execution is disabled"
        )

    return ScenarioRecord(
        scenario_id=_text(data, "scenario_id"),
        title=_text(data, "title"),
        mission=_text(data, "mission"),
        status=_text(data, "status"),
        scenario_class=_text(data, "scenario_class"),
        runtime_adapter=_text(data, "runtime_adapter"),
        mission_profile_id=_text(data, "mission_profile_id"),
        model_profile_id=_text(data, "model_profile_id"),
        required_model_domains=_string_list(data, "required_model_domains"),
        start_get_s=_number(data, "start_get_s"),
        start_get_hms=_text(data, "start_get_hms"),
        end_target_get_hms=_text(data, "end_target_get_hms"),
        vehicle_configuration=_text(data, "vehicle_configuration"),
        source_count=len(sources),
        fixture_path=fixture_path,
        execution_enabled=execution_enabled,
        execution_gate_reason=execution_gate_reason,
    )


def discover_scenarios(root: str | Path = SCENARIO_ROOT) -> tuple[ScenarioRecord, ...]:
    scenario_root = Path(root)
    records = tuple(
        load_scenario_record(path)
        for path in sorted(scenario_root.glob("*.json"))
    )
    seen: set[str] = set()
    for record in records:
        if record.scenario_id in seen:
            raise ValueError(f"duplicate scenario_id: {record.scenario_id}")
        seen.add(record.scenario_id)
    return records


def get_scenario_record(
    scenario_id: str,
    root: str | Path = SCENARIO_ROOT,
) -> ScenarioRecord:
    requested = str(scenario_id).strip()
    if not requested:
        raise ValueError("scenario_id must not be empty")
    for record in discover_scenarios(root):
        if record.scenario_id == requested:
            return record
    raise ValueError(f"unknown scenario_id: {requested}")


def load_scenario_fixture(record: ScenarioRecord) -> dict[str, Any]:
    try:
        data = json.loads(record.fixture_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"cannot load scenario fixture {record.fixture_path}: {exc}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError("scenario fixture must contain a JSON object")
    if data.get("scenario_id") != record.scenario_id:
        raise ValueError("scenario fixture identity changed after discovery")
    return data
