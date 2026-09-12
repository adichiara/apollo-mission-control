# Progress — PC+2 GUIDO player presentation

Date: 2026-09-12

## Completed

- Continued from the first-pass CONTROL player-presentation boundary.
- Rechecked the mission-specific Apollo 13 MSK 1123/1137 evidence and the LUMINARY 1C R-567 data-link source chain.
- Added `resources/research/074_pc2_guido_player_presentation_boundary.md`.
- Added `resources/source-catalog/PC2_GUIDO_PRESENTATION_SOURCES.md`.
- Added `src/apollo_mission_control/guido_presentation.py`.
- Added `tests/test_guido_presentation.py`.
- Implemented a clearly labeled project rendering rather than claiming an exact Apollo CRT transcription.
- Grouped controller-visible products into LGC/guidance status, alignment/load status, and maneuver/residual sections.
- Preserved field value, units, validity, source layer, provenance, and bounded historical-analogue notes.
- Kept hidden integrity metadata out of the player view.
- Kept deferred `vg_remaining` / `dv_gained` implementation gaps out of the screen rather than presenting them as historical telemetry failures.

## Important fidelity boundaries

- `PROGRAM` and alarm/status families have direct Apollo 13 display/downlink analogues.
- Project `LGC` operating state is not claimed to be a literal historical `OPERATING` CRT field.
- Alignment/load-status fields are project assessment/verification products grounded in GUIDO responsibility and R-567 update verification, not asserted CRT literals.
- PC+2 postburn residual is historically documented, but exact CRT label/format is not asserted.
- Exact MSK field coordinates, request behavior, refresh cadence, and several routing details remain unresolved.

## Source-reader note

The repository already contains direct visual inspection of the Apollo 13 ASPO 45 pages. During this pass, an additional web screenshot attempt on the indexed R-567 PDF was unavailable because the web result was not exposed as a screenshot-capable PDF target. No new page-image claim is made from that attempt.

## Test status

The new tests are committed. No successful runtime execution is recorded in this pass.

## Next work

Proceed to the first-pass **TELMU** player presentation, prioritizing the already-modeled PC+2 power mode, expected-current reference, inverter warning/action state, and power-down transition. Continue to avoid invented Apollo CRT formatting where source routing remains incomplete.
