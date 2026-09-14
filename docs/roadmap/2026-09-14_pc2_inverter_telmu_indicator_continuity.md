# Roadmap addendum — PC+2 inverter TELMU indicator continuity

Date: 2026-09-14

## Resolved this pass

Primary configuration evidence now supports **TELMU as the station-family owner** for the inverter-bus electrical measurements without claiming an Apollo 13 panel reconstruction:

- LM-1 records `GC0071V` and `GC0155F` as explicit ground display/telemetry products.
- Apollo 15 PHO-TR155 identifies console 09 as LM TELMU and places both measurements on TELMU operational indicators.
- LM-1 and LM-10 retain the same base loading numbers for the two measurements.

Research note: `resources/research/121_pc2_inverter_telmu_indicator_continuity_boundary.md`.

## First-playable consequence

Keep inverter voltage/frequency evidence with TELMU. Do not copy Apollo 15 console/module/indicator coordinates, LM-1 display-request numbers, or LM-10 cadence/MSKs into Apollo 13.

## Next archival target

1. Apollo 13 / AS-508 MCC operational-configuration or MOC console-loading sheets for TELMU console 09.
2. AS-508 display-request / indicator-loading records containing `GC0071V` or `GC0155F`.
3. Apollo 13 TELMU logs/checklists/configuration changes identifying the PC+2 electrical presentation.
4. Mission-specific telemetry loading sufficient to close the live sample cadence.

Physical seven-seat nominal, synthetic ΔP, and five-player compact validation remain the principal unclosed PASS boundaries; this archival refinement does not displace them.
