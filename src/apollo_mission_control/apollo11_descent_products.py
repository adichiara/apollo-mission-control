"""Apollo 11 descent controller-product schema.

This module defines a mission-specific controller-product boundary from source-backed
MSK-1137 field semantics while keeping exact ground routing unresolved where the
available Mission-G evidence does not close it.

The projector accepts only explicitly supplied controller-visible values. It never
fills a product from hidden spacecraft/model state.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping


class ProductRouteStatus(str, Enum):
    """Historical routing confidence for one controller-visible field."""

    FIELD_SEMANTICS_ONLY = "field_semantics_only"
    DOWNLINK_FAMILY_ROUTE_UNRESOLVED = "downlink_family_route_unresolved"
    MIXED_DOWNLINK_RTCC_UNRESOLVED = "mixed_downlink_rtcc_unresolved"
    CONTROLLER_REPORTED = "controller_reported"


@dataclass(frozen=True)
class Apollo11DescentFieldDefinition:
    key: str
    label: str
    units: str | None
    route_status: ProductRouteStatus
    source_candidates: tuple[str, ...]
    evidence_note: str

    def to_dict(self) -> dict[str, object]:
        return {
            "key": self.key,
            "label": self.label,
            "units": self.units,
            "route_status": self.route_status.value,
            "source_candidates": list(self.source_candidates),
            "evidence_note": self.evidence_note,
        }


@dataclass(frozen=True)
class Apollo11DescentProduct:
    key: str
    label: str
    value: Any
    units: str | None
    available: bool
    route_status: ProductRouteStatus
    source_candidates: tuple[str, ...]
    provenance: tuple[str, ...]
    evidence_note: str

    def to_dict(self) -> dict[str, object]:
        return {
            "key": self.key,
            "label": self.label,
            "value": self.value if self.available else None,
            "units": self.units,
            "available": self.available,
            "route_status": self.route_status.value,
            "source_candidates": list(self.source_candidates),
            "provenance": list(self.provenance),
            "evidence_note": self.evidence_note,
        }


@dataclass(frozen=True)
class Apollo11DescentProductSet:
    products: tuple[Apollo11DescentProduct, ...]
    applicability: str
    provenance: tuple[str, ...]

    def product(self, key: str) -> Apollo11DescentProduct:
        requested = str(key).strip()
        for product in self.products:
            if product.key == requested:
                return product
        raise ValueError(f"unknown Apollo 11 descent product key: {requested!r}")

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "apollo11_descent_controller_product_schema",
            "applicability": self.applicability,
            "products": [product.to_dict() for product in self.products],
            "provenance": list(self.provenance),
        }


# Field semantics are sourced from Apollo 11 MSK-1137 and research 502/600.
#
# Routing is deliberately conservative:
# - LUMINARY 099 proves an LR velocity/altitude downlink family exists, but the exact
#   ground mapping into each MSK-1137 LR field remains unresolved.
# - For other MSK-1137 values, current Mission-G evidence establishes display
#   semantics but not exact D/L/RTCC/display-database routing.
# - CONTROL's LR antenna-position call is a controller-reported state, not a
#   substitute for LR validity or acceptance.
APOLLO11_DESCENT_FIELDS: tuple[Apollo11DescentFieldDefinition, ...] = (
    Apollo11DescentFieldDefinition(
        "lr.range_data_good",
        "LR RNG",
        None,
        ProductRouteStatus.DOWNLINK_FAMILY_ROUTE_UNRESOLVED,
        ("LGC downlink", "ground display processing"),
        "MSK-1137 range-data GOOD/BAD; exact Mission-G parameter route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "lr.velocity_data_good",
        "VEL",
        None,
        ProductRouteStatus.DOWNLINK_FAMILY_ROUTE_UNRESOLVED,
        ("LGC downlink", "ground display processing"),
        "MSK-1137 velocity-data GOOD/BAD; exact Mission-G parameter route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "lr.vxb_fps",
        "VXB",
        "ft/s",
        ProductRouteStatus.DOWNLINK_FAMILY_ROUTE_UNRESOLVED,
        ("LGC landing-radar downlink family", "ground engineering conversion"),
        "MSK-1137 LR body-axis X velocity; exact downlink-to-display conversion unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "lr.vyb_fps",
        "VYB",
        "ft/s",
        ProductRouteStatus.DOWNLINK_FAMILY_ROUTE_UNRESOLVED,
        ("LGC landing-radar downlink family", "ground engineering conversion"),
        "MSK-1137 LR body-axis Y velocity; exact downlink-to-display conversion unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "lr.vzb_fps",
        "VZB",
        "ft/s",
        ProductRouteStatus.DOWNLINK_FAMILY_ROUTE_UNRESOLVED,
        ("LGC landing-radar downlink family", "ground engineering conversion"),
        "MSK-1137 LR body-axis Z velocity; exact downlink-to-display conversion unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "lr.slant_range_ft",
        "RNG",
        "ft",
        ProductRouteStatus.DOWNLINK_FAMILY_ROUTE_UNRESOLVED,
        ("LGC landing-radar downlink family", "ground engineering conversion"),
        "MSK-1137 LR slant range; exact DNLRALT-to-display mapping unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "pgns.altitude_ft",
        "ALT",
        "ft",
        ProductRouteStatus.MIXED_DOWNLINK_RTCC_UNRESOLVED,
        ("D/L", "RTCC/ground processing"),
        "MSK-1137 PGNS altitude semantics documented; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "guidance.tgo_s",
        "TGO",
        "s",
        ProductRouteStatus.MIXED_DOWNLINK_RTCC_UNRESOLVED,
        ("D/L", "RTCC/ground processing"),
        "MSK-1137 time-to-engine-cutoff field; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "guidance.time_to_phase_end_s",
        "T/P",
        "s",
        ProductRouteStatus.MIXED_DOWNLINK_RTCC_UNRESOLVED,
        ("D/L", "RTCC/ground processing"),
        "MSK-1137 descent-only time-to-end-of-phase field; exact route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "lgc.warning",
        "LGC WARN",
        None,
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 LGC warning-lamp field; exact Mission-G source route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "iss.warning",
        "ISS WARN",
        None,
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 ISS warning-lamp field; exact Mission-G source route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "pgncs.caution",
        "PGNCS CAUTION",
        None,
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 PGNCS caution-lamp field; exact Mission-G source route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "program.caution",
        "PROG CAUTION",
        None,
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 program caution-lamp field; exact Mission-G source route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "program.alarm_first",
        "FREG0",
        "octal",
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 first alarm-code field; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "program.alarm_second",
        "FREG1",
        "octal",
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 second alarm-code field; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "program.alarm_latest",
        "FREG2",
        "octal",
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 most-recent alarm-code field; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "program.restart_count",
        "REDO",
        "octal",
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 restart-count field; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "program.number",
        "PROG",
        None,
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 computer-program field; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "dsky.verb",
        "VERB",
        None,
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 DSKY verb field; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "dsky.noun",
        "NOUN",
        None,
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 DSKY noun field; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "dsky.flasher",
        "FL",
        None,
        ProductRouteStatus.FIELD_SEMANTICS_ONLY,
        ("ground display database",),
        "MSK-1137 verb/noun flasher field; exact Mission-G route unresolved.",
    ),
    Apollo11DescentFieldDefinition(
        "control.lr_antenna_position",
        "LR POSITION",
        None,
        ProductRouteStatus.CONTROLLER_REPORTED,
        ("CONTROL report",),
        "Apollo 11 console recording documents CONTROL reporting LR position 2.",
    ),
)


def project_apollo11_descent_products(
    values: Mapping[str, Any],
    *,
    field_provenance: Mapping[str, tuple[str, ...]] | None = None,
    applicability: str = (
        "Apollo 11 powered-descent controller-product boundary; "
        "field semantics source-backed, exact routing unresolved where noted"
    ),
    provenance: tuple[str, ...] = (),
) -> Apollo11DescentProductSet:
    """Project only explicitly supplied controller-visible values.

    Unknown keys fail. Missing known keys remain unavailable. No hidden source state
    is consulted and no cross-field derivation is performed.
    """

    supplied = dict(values)
    definitions = {definition.key: definition for definition in APOLLO11_DESCENT_FIELDS}
    unknown = sorted(set(supplied) - set(definitions))
    if unknown:
        raise ValueError(f"unknown Apollo 11 descent product key: {unknown[0]}")

    per_field = {} if field_provenance is None else dict(field_provenance)
    unknown_provenance = sorted(set(per_field) - set(definitions))
    if unknown_provenance:
        raise ValueError(
            f"unknown Apollo 11 descent provenance key: {unknown_provenance[0]}"
        )

    products: list[Apollo11DescentProduct] = []
    for definition in APOLLO11_DESCENT_FIELDS:
        available = definition.key in supplied
        products.append(
            Apollo11DescentProduct(
                key=definition.key,
                label=definition.label,
                value=supplied.get(definition.key),
                units=definition.units,
                available=available,
                route_status=definition.route_status,
                source_candidates=definition.source_candidates,
                provenance=tuple(per_field.get(definition.key, ())),
                evidence_note=definition.evidence_note,
            )
        )

    return Apollo11DescentProductSet(
        products=tuple(products),
        applicability=str(applicability).strip(),
        provenance=tuple(provenance),
    )
