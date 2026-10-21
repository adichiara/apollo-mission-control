"""Source-bounded Apollo 11 controller-product reference feed.

The feed is intentionally separate from the authoritative scenario/runtime state.
It replays only values explicitly listed in a feed fixture and labels activation
time as a project reference convention rather than historical ground-display
availability.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping

from .apollo11_descent_products import (
    Apollo11DescentProductSet,
    project_apollo11_descent_products,
)


ROOT = Path(__file__).resolve().parents[2]
REFERENCE_PRODUCT_FEED_ROOT = ROOT / "data" / "controller_product_feeds"


def _text(data: Mapping[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"reference product feed {key!r} must be a non-empty string")
    return value.strip()


def _number(data: Mapping[str, Any], key: str) -> float:
    value = data.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"reference product feed {key!r} must be numeric")
    number = float(value)
    if number < 0.0:
        raise ValueError(f"reference product feed {key!r} must be non-negative")
    return number


def _strings(value: Any, name: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        raise ValueError(f"{name} must be a list of non-empty strings")
    return tuple(item.strip() for item in value)


@dataclass(frozen=True)
class ReferenceProductEvent:
    event_id: str
    source_get_s: float
    source_get_hms: str
    activation_get_s: float
    label: str
    values: Mapping[str, Any]
    field_provenance: Mapping[str, tuple[str, ...]]

    def validated(self) -> "ReferenceProductEvent":
        event_id = self.event_id.strip()
        label = self.label.strip()
        source_get_hms = self.source_get_hms.strip()
        if not event_id:
            raise ValueError("reference product event_id must not be empty")
        if not label:
            raise ValueError("reference product event label must not be empty")
        if not source_get_hms:
            raise ValueError("reference product event source_get_hms must not be empty")
        if self.source_get_s < 0.0 or self.activation_get_s < 0.0:
            raise ValueError("reference product event GET values must be non-negative")
        if not self.values:
            raise ValueError("reference product event must provide at least one value")
        unknown_provenance = set(self.field_provenance) - set(self.values)
        if unknown_provenance:
            raise ValueError(
                "reference product event provenance supplied for absent field: "
                f"{sorted(unknown_provenance)[0]}"
            )

        # Reuse the mission-specific product schema as the field-key validator.
        project_apollo11_descent_products(
            self.values,
            field_provenance=self.field_provenance,
            applicability="reference product event validation",
        )
        return self


@dataclass(frozen=True)
class ReferenceProductFeed:
    feed_id: str
    mission_profile_id: str
    status: str
    applicability: str
    timing_policy: str
    events: tuple[ReferenceProductEvent, ...]
    sources: tuple[str, ...]
    unresolved: tuple[str, ...]
    feed_path: Path

    def validated(self) -> "ReferenceProductFeed":
        if not self.feed_id.strip():
            raise ValueError("reference product feed_id must not be empty")
        if not self.mission_profile_id.strip():
            raise ValueError("reference product mission_profile_id must not be empty")
        if not self.status.strip():
            raise ValueError("reference product status must not be empty")
        if not self.applicability.strip():
            raise ValueError("reference product applicability must not be empty")
        if not self.timing_policy.strip():
            raise ValueError("reference product timing_policy must not be empty")
        if not self.events:
            raise ValueError("reference product feed must contain at least one event")

        ids: set[str] = set()
        previous_activation: float | None = None
        for event in self.events:
            event.validated()
            if event.event_id in ids:
                raise ValueError(
                    f"duplicate reference product event_id: {event.event_id}"
                )
            ids.add(event.event_id)
            if (
                previous_activation is not None
                and event.activation_get_s < previous_activation
            ):
                raise ValueError(
                    "reference product events must be ordered by activation_get_s"
                )
            previous_activation = event.activation_get_s
        return self

    def to_public_dict(self) -> dict[str, object]:
        return {
            "feed_id": self.feed_id,
            "mission_profile_id": self.mission_profile_id,
            "status": self.status,
            "applicability": self.applicability,
            "timing_policy": self.timing_policy,
            "event_count": len(self.events),
            "sources": list(self.sources),
            "unresolved": list(self.unresolved),
        }


@dataclass(frozen=True)
class ReferenceProductFeedSnapshot:
    feed_id: str
    get_s: float
    timing_policy: str
    product_set: Apollo11DescentProductSet
    applied_event_ids: tuple[str, ...]
    latest_applied_event: ReferenceProductEvent | None
    next_event: ReferenceProductEvent | None
    historical_ground_display_timing_claimed: bool = False

    def to_dict(self) -> dict[str, object]:
        def event_summary(event: ReferenceProductEvent | None) -> dict[str, object] | None:
            if event is None:
                return None
            return {
                "event_id": event.event_id,
                "source_get_s": event.source_get_s,
                "source_get_hms": event.source_get_hms,
                "activation_get_s": event.activation_get_s,
                "label": event.label,
                "fields": list(event.values),
            }

        return {
            "model_status": "apollo11_reference_product_feed",
            "feed_id": self.feed_id,
            "get_s": self.get_s,
            "timing_policy": self.timing_policy,
            "historical_ground_display_timing_claimed": (
                self.historical_ground_display_timing_claimed
            ),
            "applied_event_ids": list(self.applied_event_ids),
            "latest_applied_event": event_summary(self.latest_applied_event),
            "next_event": event_summary(self.next_event),
            "controller_products": self.product_set.to_dict(),
        }


def _event(payload: Any) -> ReferenceProductEvent:
    if not isinstance(payload, dict):
        raise ValueError("reference product feed event must be an object")
    raw_values = payload.get("values")
    if not isinstance(raw_values, dict) or not raw_values:
        raise ValueError("reference product event values must be a non-empty object")

    raw_provenance = payload.get("field_provenance", {})
    if not isinstance(raw_provenance, dict):
        raise ValueError("reference product field_provenance must be an object")
    provenance: dict[str, tuple[str, ...]] = {}
    for key, items in raw_provenance.items():
        if not isinstance(key, str) or not key.strip():
            raise ValueError("reference product provenance key must be non-empty")
        provenance[key.strip()] = _strings(
            items,
            f"reference product provenance for {key!r}",
        )

    return ReferenceProductEvent(
        event_id=_text(payload, "event_id"),
        source_get_s=_number(payload, "source_get_s"),
        source_get_hms=_text(payload, "source_get_hms"),
        activation_get_s=_number(payload, "activation_get_s"),
        label=_text(payload, "label"),
        values=dict(raw_values),
        field_provenance=provenance,
    ).validated()


def load_reference_product_feed(path: str | Path) -> ReferenceProductFeed:
    feed_path = Path(path)
    try:
        data = json.loads(feed_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load reference product feed {feed_path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("reference product feed must contain a JSON object")

    raw_events = data.get("events")
    if not isinstance(raw_events, list) or not raw_events:
        raise ValueError("reference product feed events must be a non-empty list")

    feed = ReferenceProductFeed(
        feed_id=_text(data, "feed_id"),
        mission_profile_id=_text(data, "mission_profile_id"),
        status=_text(data, "status"),
        applicability=_text(data, "applicability"),
        timing_policy=_text(data, "timing_policy"),
        events=tuple(_event(item) for item in raw_events),
        sources=_strings(data.get("sources", []), "reference product feed sources"),
        unresolved=_strings(
            data.get("unresolved", []),
            "reference product feed unresolved",
        ),
        feed_path=feed_path,
    )
    return feed.validated()


def discover_reference_product_feeds(
    root: str | Path = REFERENCE_PRODUCT_FEED_ROOT,
) -> tuple[ReferenceProductFeed, ...]:
    records = tuple(
        load_reference_product_feed(path)
        for path in sorted(Path(root).glob("*.json"))
    )
    ids = [record.feed_id for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate reference product feed_id")
    return records


def get_reference_product_feed(
    feed_id: str,
    root: str | Path = REFERENCE_PRODUCT_FEED_ROOT,
) -> ReferenceProductFeed:
    requested = str(feed_id).strip()
    if not requested:
        raise ValueError("feed_id must not be empty")
    for record in discover_reference_product_feeds(root):
        if record.feed_id == requested:
            return record
    raise ValueError(f"unknown reference product feed_id: {requested}")


def evaluate_reference_product_feed(
    feed: ReferenceProductFeed,
    *,
    get_s: float,
) -> ReferenceProductFeedSnapshot:
    checked = feed.validated()
    query_get_s = float(get_s)
    if query_get_s < 0.0:
        raise ValueError("get_s must be non-negative")

    values: dict[str, Any] = {}
    field_provenance: dict[str, tuple[str, ...]] = {}
    applied: list[ReferenceProductEvent] = []
    next_event: ReferenceProductEvent | None = None

    for event in checked.events:
        if event.activation_get_s <= query_get_s:
            applied.append(event)
            values.update(event.values)
            for key in event.values:
                field_provenance[key] = tuple(
                    event.field_provenance.get(key, ())
                ) + (
                    f"Feed activation convention: {checked.timing_policy}",
                )
            continue
        next_event = event
        break

    products = project_apollo11_descent_products(
        values,
        field_provenance=field_provenance,
        applicability=checked.applicability,
        provenance=checked.sources,
    )
    return ReferenceProductFeedSnapshot(
        feed_id=checked.feed_id,
        get_s=query_get_s,
        timing_policy=checked.timing_policy,
        product_set=products,
        applied_event_ids=tuple(event.event_id for event in applied),
        latest_applied_event=applied[-1] if applied else None,
        next_event=next_event,
    )
