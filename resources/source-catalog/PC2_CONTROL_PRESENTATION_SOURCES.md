# Apollo 13 PC+2 CONTROL Presentation Sources

Status: active source supplement for the first player-facing CONTROL presentation.

## 1. Apollo 13 Guidance & Navigation Summary

- **Organization:** AC Electronics / Delco Electronics
- **Mission:** Apollo 13
- **Source class:** PRIMARY, mission-specific engineering/operations reference
- **Relevant section:** ASPO 45 CRT Displays
- **Relevant pages:** PDF 186–190 / ASPO-8–12
- **Use:** Establishes the Apollo 13 MSK 1123 and MSK 1137 display families, their labels/units, and the historical visual/semantic vocabulary for LM guidance/control/propulsion monitoring.
- **Critical implementation constraint:** MSK 1137 `TCP` is chamber pressure expressed as percent. The executable PC+2 model currently carries GQ6510P chamber pressure in psi; no unsupported conversion or direct alias is permitted.
- **Repository inspection record:** `resources/research/029_apollo13_aspo45_direct_inspection.md`
- **Normalized 1137 inventory:** `resources/research/031_apollo13_msk1137_field_inventory.md`

## 2. Apollo 13 Mission Operations Report

- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes CONTROL's PC+2 monitoring responsibilities and shutdown criteria independently of exact display routing.
- **Implementation consequence:** Supports including already-modeled propulsion/control/rule quantities in a minimum CONTROL player view, but does not by itself establish exact CRT field positions.

## 3. Apollo 13 PC+2 contemporaneous Mission Rules / air-to-ground read-up

- **Source class:** PRIMARY, mission-specific operational record
- **Use:** Establishes the controller/crew decision criteria that the player-facing CONTROL information must support.
- **Implementation consequence:** Ground-only fuel/oxidizer differential-pressure monitoring remains distinct from crew-side information.

## 4. LM-7-family measurement evidence

- **GQ6510P:** DPS thrust-chamber pressure measurement.
- **Use:** Provides the executable chamber-pressure path in psi.
- **Constraint:** The current source chain does not establish the exact conversion from this engineering measurement to the MSK 1137 `TCP` percent field.

## Evidence rule

The first CONTROL interface may borrow documented Apollo terminology and grouping, but it must be labeled as a **project rendering** unless the exact field semantics, units, and layout are directly supported.

Do not:

- relabel GQ6510P psi as historical `TCP`;
- turn deferred implementation fields into simulated telemetry failures;
- expose hidden integrity metadata;
- invent a modern diagnostic/health dashboard.

## Research record

- `resources/research/073_pc2_control_player_presentation_boundary.md`
- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`
