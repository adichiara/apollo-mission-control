# Progress — PC+2 inverter TELMU indicator continuity

Date: 2026-09-14

## Completed

- Continued from research note 120's unresolved Apollo 13 inverter display-destination question.
- Reviewed primary pre-/post-Apollo-13 configuration evidence rather than inferring a missing AS-508 layout.
- Confirmed the SA-204/LM-1 Data Evaluation Guide listed `GC0071V` and `GC0155F` as explicit ground display/telemetry products with display requests 5746/5771 and channel/loadings `1022069 15` / `1041069 15`.
- Confirmed Apollo 15 PHO-TR155 identifies console 09 as LM TELMU and places `GC0071V * AC BUS V` and `GC0155F * AC BUS F` on TELMU module-05 operational indicators 07 and 16, sourced from MOC.
- Recorded that the base loading numbers persist into the later LM-10 telemetry packet, strengthening continuity without converting later values into Apollo 13 facts.
- Added `resources/research/121_pc2_inverter_telmu_indicator_continuity_boundary.md`.
- Updated `resources/source-catalog/PC2_INVERTER_TELEMETRY_PRESENTATION_SOURCES.md`.

## Result

The station-family uncertainty is narrower:

```text
GC0071V / GC0155F
    → established ground display products before Apollo 13
    → explicitly TELMU operational indicators by Apollo 15
    → TELMU is the best source-backed first-playable owner
```

This does **not** recover Apollo 13's exact console/module/indicator placement, display-request numbers, MSK, sampling cadence, or latency.

## Still unresolved

- Apollo 13 / AS-508 TELMU console-09 operational-indicator loading;
- exact Apollo 13 normal-format sample cadence for `GC0071V` / `GC0155F`;
- whether either measurement also appeared on a PC+2 CRT/MSK;
- exact Apollo 13 display-request/MSK numbers, precision, refresh, and latency;
- actual PC+2 controller use/selection and any CONTROL presentation.

## Validation

Research/documentation-only change. No physical-play PASS claim or station-maturity grade change is added.
