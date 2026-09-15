"""First-pass player-facing TELMU presentation for Apollo 13 PC+2.

This is a project rendering of documented LM electrical/configuration and
inverter-contingency information, not a transcription of an Apollo TELMU CRT.
Exact historical terminology is used only where the modeled product semantics
match the source evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .controller_products import ProjectionSet
from .pc2_nominal import Product


PROJECT_RENDERING_NOTICE = (
    "PROJECT RENDERING — documented PC+2 TELMU information; "
    "not an exact historical CRT transcription"
)


@dataclass(frozen=True)
class TelmuDisplayField:
    key: str
    label: str
    value: Any
    units: str | None
    validity: str
    source_layer: str
    provenance: str
    historical_analogue: str | None = None


@dataclass(frozen=True)
class TelmuDisplaySection:
    title: str
    fields: tuple[TelmuDisplayField, ...]


@dataclass(frozen=True)
class TelmuPresentation:
    title: str
    notice: str
    source_basis: tuple[str, ...]
    sections: tuple[TelmuDisplaySection, ...]


def _field(
    projection: ProjectionSet,
    key: str,
    label: str,
    *,
    historical_analogue: str | None = None,
) -> TelmuDisplayField | None:
    product: Product | None = projection.products.get(key)
    if product is None:
        return None
    return TelmuDisplayField(
        key=key,
        label=label,
        value=product.value,
        units=product.units,
        validity=product.validity.value,
        source_layer=product.source_layer,
        provenance=product.provenance,
        historical_analogue=historical_analogue,
    )


def _section(title: str, *fields: TelmuDisplayField | None) -> TelmuDisplaySection:
    return TelmuDisplaySection(title=title, fields=tuple(field for field in fields if field is not None))


def build_pc2_telmu_presentation(projection: ProjectionSet) -> TelmuPresentation:
    """Build the minimum PC+2 TELMU player view.

    The Apollo 13 Mission Operations Report establishes the burn power-up,
    approximately 38-40 A burn-configuration requirement, immediate post-burn
    power-down, and inverter-warning shutdown criterion. Reviewed LM
    instrumentation schematics do not establish direct ground telemetry of the
    derived INVERTER caution, so that caution is not rendered as a TELMU field.
    Exact TELMU CRT routing/layout is unresolved, so the remaining products are
    grouped as a project rendering rather than represented as a historical screen.

    Hidden integrity annotations and deferred project gaps are not rendered.
    The 38-40 A value is explicitly a documented reference range, not a live
    measured-current value.
    """
    if projection.station != "TELMU":
        raise ValueError("PC+2 TELMU presentation requires a TELMU projection")

    sections = (
        _section(
            "POWER CONFIGURATION",
            _field(
                projection,
                "lm.power.mode",
                "POWER MODE",
                historical_analogue="TELMU tracked LM electrical configuration; this project label is not asserted as a CRT literal",
            ),
            _field(
                projection,
                "lm.power.burn_configuration_expected_current_range_a",
                "BURN CONFIG CURRENT REF",
                historical_analogue="Apollo 13 Mission Operations Report states approximately 38-40 A was required to maintain the PC+2 burn configuration; this is a reference range, not measured current",
            ),
            _field(
                projection,
                "lm.powerdown.started",
                "POWERDOWN",
                historical_analogue="Mission Operations Report records LM power-down beginning at approximately 79:34 GET; this is a project configuration/event product",
            ),
        ),
        _section(
            "INVERTER / ELECTRICAL CONTINGENCY",
            _field(
                projection,
                "lm.inverter_switch_attempted",
                "INVERTER SWITCH",
                historical_analogue="Project operational-action state representing the documented switch-inverter contingency; not asserted as a historical CRT field",
            ),
            _field(
                projection,
                "lm.inverter_switch_attempt_get_s",
                "SWITCH GET",
                historical_analogue="Project event timestamp for the inverter-switch attempt; not asserted as a historical TELMU display field",
            ),
        ),
    )

    return TelmuPresentation(
        title="TELMU — PC+2 POWER / ELECTRICAL MONITOR",
        notice=PROJECT_RENDERING_NOTICE,
        source_basis=(
            "Apollo 13 Mission Operations Report — PC+2 chronology and Mission Rules",
            "Apollo 13 TELMU Post Mission Report — LM electrical/configuration operations",
            "Apollo 13 Review Board — LM power-conservation chronology",
        ),
        sections=sections,
    )
