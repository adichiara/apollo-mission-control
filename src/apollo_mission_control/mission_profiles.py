"""Mission-era configuration profile catalog.

Mission profiles hold sourced configuration that can be shared by multiple
scenarios from the same mission/era. They are intentionally narrower than a
universal Apollo configuration schema: fields are added when scenario work
establishes a reusable need.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
MISSION_PROFILE_ROOT = ROOT / "data" / "mission_profiles"


def _text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"mission profile {key!r} must be a non-empty string")
    return value.strip()


def _string_map(data: dict[str, Any], key: str) -> dict[str, str]:
    value = data.get(key, {})
    if not isinstance(value, dict):
        raise ValueError(f"mission profile {key!r} must be an object")
    result: dict[str, str] = {}
    for item_key, item_value in value.items():
        if not isinstance(item_key, str) or not item_key.strip():
            raise ValueError(f"mission profile {key!r} contains an invalid key")
        if not isinstance(item_value, str) or not item_value.strip():
            raise ValueError(
                f"mission profile {key!r}[{item_key!r}] must be a non-empty string"
            )
        result[item_key.strip()] = item_value.strip()
    return result


@dataclass(frozen=True)
class MissionProfileRecord:
    mission_profile_id: str
    mission: str
    mission_designation: str
    status: str
    launch_vehicle: str
    spacecraft: dict[str, str]
    controller_nomenclature: dict[str, str]
    ground_configuration_reference: str
    source_count: int
    profile_path: Path

    def to_public_dict(self) -> dict[str, object]:
        return {
            "mission_profile_id": self.mission_profile_id,
            "mission": self.mission,
            "mission_designation": self.mission_designation,
            "status": self.status,
            "launch_vehicle": self.launch_vehicle,
            "spacecraft": dict(self.spacecraft),
            "controller_nomenclature": dict(self.controller_nomenclature),
            "ground_configuration_reference": self.ground_configuration_reference,
            "source_count": self.source_count,
        }


def load_mission_profile_record(path: str | Path) -> MissionProfileRecord:
    profile_path = Path(path)
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load mission profile {profile_path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"mission profile {profile_path} must contain a JSON object")

    sources = data.get("sources", [])
    if not isinstance(sources, list) or not all(isinstance(item, str) for item in sources):
        raise ValueError("mission profile 'sources' must be a list of strings")

    return MissionProfileRecord(
        mission_profile_id=_text(data, "mission_profile_id"),
        mission=_text(data, "mission"),
        mission_designation=_text(data, "mission_designation"),
        status=_text(data, "status"),
        launch_vehicle=_text(data, "launch_vehicle"),
        spacecraft=_string_map(data, "spacecraft"),
        controller_nomenclature=_string_map(data, "controller_nomenclature"),
        ground_configuration_reference=_text(data, "ground_configuration_reference"),
        source_count=len(sources),
        profile_path=profile_path,
    )


def discover_mission_profiles(
    root: str | Path = MISSION_PROFILE_ROOT,
) -> tuple[MissionProfileRecord, ...]:
    profile_root = Path(root)
    records = tuple(
        load_mission_profile_record(path)
        for path in sorted(profile_root.glob("*.json"))
    )
    seen: set[str] = set()
    for record in records:
        if record.mission_profile_id in seen:
            raise ValueError(
                f"duplicate mission_profile_id: {record.mission_profile_id}"
            )
        seen.add(record.mission_profile_id)
    return records


def get_mission_profile(
    mission_profile_id: str,
    root: str | Path = MISSION_PROFILE_ROOT,
) -> MissionProfileRecord:
    requested = str(mission_profile_id).strip()
    if not requested:
        raise ValueError("mission_profile_id must not be empty")
    for record in discover_mission_profiles(root):
        if record.mission_profile_id == requested:
            return record
    raise ValueError(f"unknown mission_profile_id: {requested}")
