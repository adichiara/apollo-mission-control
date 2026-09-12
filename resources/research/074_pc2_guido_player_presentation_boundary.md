# Apollo 13 PC+2 — GUIDO player-presentation boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — first-pass project rendering justified; exact CRT routing/coordinates remain unresolved**

## Question

What can the first player-facing GUIDO screen show for the PC+2 vertical slice without pretending that every modeled guidance product is a verbatim Apollo CRT field?

## Primary-source basis

### Apollo 13 Guidance & Navigation Summary — ASPO 45 CRT Displays

Direct inspection already recorded in research note 029 confirms mission-specific Apollo 13 layouts for:

- **MSK 1123 — LM GUID, CONTROL AND PROP RT**;
- **MSK 1137 — LM powered-descent/control display**.

The definition pages establish relevant field families including:

- LGC downlist/list identity context;
- program / verb / noun information;
- restart/alarm information;
- guidance and velocity-change quantities;
- desired/actual guidance/control quantities;
- ground-derived comparisons.

This proves that GUIDO worked from a structured, processed real-time guidance picture. It does **not** prove that every modeled project product below appeared verbatim under the same label on one specific GUIDO CRT.

### MIT Instrumentation Laboratory R-567, LUMINARY 1C, Section 2 — Data Links, Rev. 8 (March 1970)

This Apollo 13 LM software-era source documents:

- program-dependent LGC downlists;
- P27 update and verification behavior;
- DSKY/display-table information;
- failure/status and restart information;
- desired/actual attitude/rate quantities;
- PIPA / velocity-change information;
- TIG and maneuver-related quantities;
- snapshot/coherency handling for multiregister downlink values.

It therefore supports presenting LGC/program state and upload-verification state to GUIDO while preserving the distinction between onboard data, ground assessment, and display routing.

A web PDF screenshot attempt during this pass was not available through the web reader because the indexed copy was not exposed as an application/pdf screenshot target. The source itself remains independently indexed and already has repository field-provenance work based on direct document inspection.

### Apollo 13 Mission Operations Report

The PC+2 chronology documents nominal PGNS residuals after the burn and the broader GUIDO role in guidance/computer/alignment monitoring. Those residuals justify a postburn guidance result in the player workflow, but they do not establish an exact CRT label or formatting convention for the project product.

## First-pass GUIDO information groups

The implemented project rendering groups existing controller products into:

### LGC / Guidance Status

- LGC operating state;
- active program (P40 during the modeled burn state);
- program alarm;
- ISS warning;
- LGC warning/status.

Historical terminology is bounded carefully:

- `PROGRAM` has a direct analogue in the Apollo 13 display family;
- alarm-code/status information is directly documented;
- `ISS WARNING` is required by the PC+2 shutdown rule but its exact GUIDO CRT field remains unresolved;
- the project `LGC` operating boolean is not claimed to be a literal historical `OPERATING` CRT field.

### Alignment / Load Status

- alignment accepted;
- state-vector load status;
- target-load status.

These are operationally appropriate GUIDO products. R-567 supports update/downlink verification, and Apollo 13 operations establish GUIDO alignment responsibility. The current project values are nevertheless rendered as **assessment/verification products**, not asserted CRT literals.

### Maneuver / Residual

- planned PGNS Vg;
- postburn residual.

LUMINARY documentation supports maneuver/velocity-change data in the guidance data path, and the Mission Operations Report records the PC+2 PGNS residuals. Exact Apollo 13 CRT labels and routing for the project products are not asserted.

## Explicit exclusions

The first pass does not invent or expose:

- exact CRT coordinates;
- display selection/request sequence;
- refresh cadence;
- exact mapping from each LGC downlist word to an MSK 1123/1137 field;
- hidden simulator product-integrity metadata;
- deferred `vg_remaining` or `dv_gained` fields as fake telemetry failures;
- an exact GUIDO field for ISS warning where the route is still unresolved.

## Implementation

Added:

- `src/apollo_mission_control/guido_presentation.py`
- `tests/test_guido_presentation.py`

The screen carries per-field:

- value;
- units;
- validity;
- source layer;
- provenance;
- optional historical-analogue note.

This mirrors the CONTROL presentation boundary while respecting the stronger LGC/PGNS provenance available to GUIDO.

## Architectural rule

Player presentation consumes controller-visible products only:

`source/onboard state → ground processing → controller product → player rendering`

Hidden integrity metadata remains outside the rendering layer. Project implementation gaps remain distinct from historical `UNAVAILABLE` telemetry.

## Sources

Primary / mission-specific:

- AC Electronics, *Apollo 13 Guidance & Navigation Summary*, ASPO 45 CRT Displays, MSK 1123/1137; repository direct-inspection record: `resources/research/029_apollo13_aspo45_direct_inspection.md`.
- MIT Instrumentation Laboratory, R-567, *Guidance System Operations Plan for Manned LM Earth Orbital and Lunar Missions Using Program LUMINARY 1C (LM131 Rev. 1), Section 2 — Data Links*, Rev. 8, March 1970.
- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970.

Repository provenance work:

- `resources/research/032_apollo13_lm_crt_field_provenance.md`
- `resources/research/035_apollo13_msk1123_field_provenance.md`
- `resources/research/052_pc2_controller_product_projection.md`
- `resources/research/073_pc2_control_player_presentation_boundary.md`

## Stop condition / next work

The minimum GUIDO screen is now sufficient for the PC+2 player-interface layer. Do not pursue exact CRT coordinates or full field transcription merely for appearance.

The next useful player-presentation target is **TELMU**, because PC+2 already has modeled power-mode, expected-current reference, inverter-warning/action, and power-down products, including a real contingency decision dependency. Exact Apollo formatting should again be used only where directly supported.
