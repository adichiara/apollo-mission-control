# Station-status addendum — PC+2 inverter telemetry format boundary

Date: 2026-09-14

## TELMU

**Maturity remains B.**

New mission-specific ground-system evidence confirms Apollo 13 had normal LM-capable network formats and a separate high-rate post-pass playback facility. It does not recover the live PC+2 TELMU display/MSK, `GC0071V` / `GC0155F` normal-format loading, or CRT cadence.

First-playable TELMU rendering therefore remains a project presentation of source-backed inverter electrical telemetry rather than an exact historical CRT reconstruction.

## CONTROL

**Maturity remains B.**

The same boundary applies if inverter electrical evidence is surfaced to CONTROL. No mission-specific source reviewed in this pass establishes a CONTROL-selected inverter format or field layout.

## NETWORK / ground instrumentation

**Maturity remains C for full station reconstruction, with the PC+2 functional boundary improved.**

AS-508 identifies normal LM-capable format families and explicitly separates High Speed Format 30 as post-pass playback selected by CEF at the TICC. This improves the modeled telemetry architecture without reconstructing the Network/TICC console itself.

## Consequence

Do not treat Format-30 10/50-sample/s values as live TELMU/CONTROL update rates. Exact live sample loading, display refresh, and post-pass playback remain separate evidence questions.
