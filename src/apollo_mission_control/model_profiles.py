"""Numerical/causal model-profile catalog.

Mission profiles describe mission-era configuration and nomenclature.
Model profiles separately describe the evidence/readiness state of executable
causal/numerical domains that scenarios may reference.

This first schema is intentionally metadata-only. It does not make unresolved
historical constants executable merely to populate a configuration file.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
MODEL_PROFILE_ROOT = ROOT / "data" / "model_profiles"

_ALLOWED_DOMAIN_STATUS = {
    "unresolved",
    "partial",
    "validated",
    "not_applicable",
}


def _text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"model profile {key!r} must be a non-empty string")
    return value.strip()


@dataclass(frozen=True)
class ModelDomainRecord:
    status: str
    note: str

    def to_public_dict(self) -> dict[str, str]:
        return {
            "status": self.status,
            "note": self.note,
        }


@dataclass(frozen=True)
class ModelProfileRecord:
    model_profile_id: str
    mission_profile_id: str
    status: str
    validation_state: str
    domains: dict[str, ModelDomainRecord]
    source_count: int
    profile_path: Path

    def to_public_dict(self) -> dict[str, object]:
        return {
            "model_profile_id": self.model_profile_id,
            "mission_profile_id": self.mission_profile_id,
            "status": self.status,
            "validation_state": self.validation_state,
            "domains": {
                name: domain.to_public_dict()
                for name, domain in self.domains.items()
            },
            "source_count": self.source_count,
        }


def _domains(data: dict[str, Any]) -> dict[str, ModelDomainRecord]:
    value = data.get("domains")
    if not isinstance(value, dict) or not value:
        raise ValueError("model profile 'domains' must be a non-empty object")

    result: dict[str, ModelDomainRecord] = {}
    for name, payload in value.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError("model profile domains contains an invalid name")
        if not isinstance(payload, dict):
            raise ValueError(
                f"model profile domain {name!r} must be an object"
            )

        status = payload.get("status")
        note = payload.get("note")
        if not isinstance(status, str) or status not in _ALLOWED_DOMAIN_STATUS:
            raise ValueError(
                f"model profile domain {name!r} has invalid status"
            )
        if not isinstance(note, str) or not note.strip():
            raise ValueError(
                f"model profile domain {name!r} note must be a non-empty string"
            )

        result[name.strip()] = ModelDomainRecord(
            status=status,
            note=note.strip(),
        )

    return result


def load_model_profile_record(path: str | Path) -> ModelProfileRecord:
    profile_path = Path(path)
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load model profile {profile_path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"model profile {profile_path} must contain a JSON object")

    sources = data.get("sources", [])
    if not isinstance(sources, list) or not all(
        isinstance(item, str) and item.strip() for item in sources
    ):
        raise ValueError("model profile 'sources' must be a list of non-empty strings")

    return ModelProfileRecord(
        model_profile_id=_text(data, "model_profile_id"),
        mission_profile_id=_text(data, "mission_profile_id"),
        status=_text(data, "status"),
        validation_state=_text(data, "validation_state"),
        domains=_domains(data),
        source_count=len(sources),
        profile_path=profile_path,
    )


def discover_model_profiles(
    root: str | Path = MODEL_PROFILE_ROOT,
) -> tuple[ModelProfileRecord, ...]:
    profile_root = Path(root)
    records = tuple(
        load_model_profile_record(path)
        for path in sorted(profile_root.glob("*.json"))
    )
    seen: set[str] = set()
    for record in records:
        if record.model_profile_id in seen:
            raise ValueError(
                f"duplicate model_profile_id: {record.model_profile_id}"
            )
        seen.add(record.model_profile_id)
    return records


def get_model_profile(
    model_profile_id: str,
    root: str | Path = MODEL_PROFILE_ROOT,
) -> ModelProfileRecord:
    requested = str(model_profile_id).strip()
    if not requested:
        raise ValueError("model_profile_id must not be empty")
    for record in discover_model_profiles(root):
        if record.model_profile_id == requested:
            return record
    raise ValueError(f"unknown model_profile_id: {requested}")


@dataclass(frozen=True)
class ModelReadinessAssessment:
    required_domains: tuple[str, ...]
    domain_statuses: dict[str, str]
    missing_domains: tuple[str, ...]
    unvalidated_domains: tuple[str, ...]
    historical_validation_ready: bool

    def to_public_dict(self) -> dict[str, object]:
        return {
            "required_domains": list(self.required_domains),
            "domain_statuses": dict(self.domain_statuses),
            "missing_domains": list(self.missing_domains),
            "unvalidated_domains": list(self.unvalidated_domains),
            "historical_validation_ready": self.historical_validation_ready,
        }


def assess_model_readiness(
    profile: ModelProfileRecord,
    required_domains: list[str] | tuple[str, ...],
) -> ModelReadinessAssessment:
    normalized: list[str] = []
    for raw in required_domains:
        name = str(raw).strip()
        if not name:
            raise ValueError("required model domains must be non-empty strings")
        if name not in normalized:
            normalized.append(name)

    if not normalized:
        raise ValueError("at least one required model domain must be supplied")

    statuses: dict[str, str] = {}
    missing: list[str] = []
    unvalidated: list[str] = []

    for name in normalized:
        domain = profile.domains.get(name)
        if domain is None:
            statuses[name] = "missing"
            missing.append(name)
            unvalidated.append(name)
            continue

        statuses[name] = domain.status
        if domain.status != "validated":
            unvalidated.append(name)

    return ModelReadinessAssessment(
        required_domains=tuple(normalized),
        domain_statuses=statuses,
        missing_domains=tuple(missing),
        unvalidated_domains=tuple(unvalidated),
        historical_validation_ready=not unvalidated,
    )
