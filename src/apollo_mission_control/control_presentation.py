"""First-pass player-facing CONTROL presentation for Apollo 13 PC+2.

This is intentionally a project rendering of documented controller information,
not a transcription of an Apollo CRT. Historical MSK 1123/1137 terminology is
used only where the modeled quantity has matching semantics and units.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .controller_products import ProjectionSet
from .pc2_nominal import Product


PROJECT_RENDERING_NOTICE = (
    "PROJECT RENDERING — documented PC+2 CONTROL information; "
    "not an exact historical CRT transcription"
)


@dataclass(frozen=True)
class ControlDisplayField:
    key: str
    label: str
    value: Any
    units: str | None
    validity: str
    source_layer: str
    provenance: str
    historical_analogue: str | None = None


@dataclass(frozen=True)
class ControlDisplaySection:
    title: str
    fields: tuple[ControlDisplayField, ...]


@dataclass(frozen=True)
class ControlPresentation:
    title: str
    notice: str
    source_basis: tuple[str, ...]
    sections: tuple[ControlDisplaySection, ...]


def _field(
    projection: ProjectionSet,
    key: str,
    label: str,
    *,
    historical_analogue: str | None = None,
) -> ControlDisplayField | None:
    product: Product | None = projection.products.get(key)
    if product is None:
        return None
    return ControlDisplayField(
        key=key,
        label=label,
        value=product.value,
        units=product.units,
        validity=product.validity.value,
        source_layer=product.source_layer,
        provenance=product.provenance,
        historical_analogue=historical_analogue,
    )


def _section(title: str, *fields: ControlDisplayField | None) -> ControlDisplaySection:
    return ControlDisplaySection(title=title, fields=tuple(field for field in fields if field is not None))


def build_pc2_control_presentation(projection: ProjectionSet) -> ControlPresentation:
    """Build the minimum PC+2 CONTROL view from controller-visible products.

    Deferred implementation fields are omitted rather than shown as historical
    telemetry failures. Hidden integrity annotations are intentionally ignored.

    Apollo 13 MSK 1137 defines TCP as chamber pressure in percent. The current
    PC+2 model carries sourced GQ6510P chamber pressure in psi, so it is rendered
    as CHAMBER P and is *not* relabeled TCP or converted to percent.
    """
    if projection.station != "CONTROL":
        raise ValueError("PC+2 CONTROL presentation requires a CONTROL projection")

    sections = (
        _section(
            "BURN / PROPULSION",
            _field(projection, "dps.engine_running", "ENGINE"),
            _field(projection, "dps.throttle_command_phase", "THROTTLE PHASE"),
            _field(
                projection,
                "dps.chamber_pressure_psi",
                "CHAMBER P",
                historical_analogue="MSK 1137 TCP is chamber pressure expressed as percent; no psi-to-TCP conversion is asserted",
            ),
            _field(projection, "dps.fuel_oxidizer_delta_p_psi", "F/O DELTA P"),
        ),
        _section(
            "ATTITUDE / CONTROL",
            _field(projection, "vehicle.attitude_error_xyz_deg", "ATT ERR"),
            _field(projection, "vehicle.body_rate_xyz_deg_s", "BODY RATE"),
            _field(projection, "dps.engine_gimbal_warning", "GIMBAL WARN"),
            _field(projection, "ces.dc_failure", "CES DC FAIL"),
        ),
        _section(
            "ULLAGE",
            _field(projection, "rcs.ullage_active", "ULLAGE"),
            _field(projection, "rcs.ullage_jets_count", "ULLAGE JETS"),
        ),
    )

    return ControlPresentation(
        title="CONTROL — PC+2 BURN MONITOR",
        notice=PROJECT_RENDERING_NOTICE,
        source_basis=(
            "Apollo 13 MSK 1123 — LM GUID, CONTROL AND PROP RT",
            "Apollo 13 MSK 1137 — powered-descent/control display",
            "Apollo 13 PC+2 Mission Rules / Mission Operations Report",
        ),
        sections=sections,
    )
