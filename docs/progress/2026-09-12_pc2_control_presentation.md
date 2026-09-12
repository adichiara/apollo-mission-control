# Progress — PC+2 first-pass CONTROL presentation

Date: 2026-09-12

## Completed

- Continued from the documented post-restart stopping point into the first player-facing CONTROL display boundary.
- Re-reviewed the mission-specific Apollo 13 ASPO 45 display evidence for MSK 1123 and MSK 1137.
- Confirmed a critical semantic mismatch that must be preserved: historical MSK 1137 `TCP` is chamber pressure in percent, while the executable PC+2 model's sourced GQ6510P quantity is in psi.
- Added `resources/research/073_pc2_control_player_presentation_boundary.md`.
- Added `resources/source-catalog/PC2_CONTROL_PRESENTATION_SOURCES.md`.
- Added `src/apollo_mission_control/control_presentation.py`.
- Added `tests/test_control_presentation.py`.
- Defined the first CONTROL player view as an explicitly labeled project rendering rather than a claimed CRT reconstruction.
- Preserved per-field value, units, validity, source layer, and provenance.
- Omitted deferred implementation gaps instead of presenting them as historical `UNAVAILABLE` telemetry.
- Kept hidden product-integrity metadata out of the player presentation.

## Presentation sections

- BURN / PROPULSION
- ATTITUDE / CONTROL
- ULLAGE

These are project groupings, not asserted Apollo 13 CRT section labels or coordinates.

## Historical boundary

No psi-to-`TCP` percent conversion, exact CRT field placement, refresh cadence, CONTROL display-selection sequence, or exact ΔP display location was invented.

## Test status

Tests are committed. No successful execution is recorded in this pass.

## Next work

Build the first-pass GUIDO player presentation from the already-modeled PC+2 products, using exact Apollo 13 MSK terminology only where field semantics and units are directly supported.
