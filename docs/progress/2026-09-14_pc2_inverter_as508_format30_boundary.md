# Progress — PC+2 inverter AS-508 telemetry-format boundary

Date: 2026-09-14

## Completed

- Continued from research note 119's unresolved Apollo 13 live telemetry cadence/display-loading question.
- Reviewed the mission-specific March 1970 *AS-508 MCC/MSFN Mission Configuration/System Description*.
- Confirmed AS-508 normal 2.4-kb/s formats with LM data content, including LM ONLY, CSM-LM PCM, CSM + LM BACKUP, and ASCENT/DESCENT.
- Confirmed High Speed Format 30 was explicitly a **post-pass playback** facility for pre-defined high-rate CSM/LM subformats selected by CEF at the TICC.
- Recorded the critical boundary that Format-30 50-s/s and 10-s/s analog slots are **not** evidence for live TELMU/CONTROL CRT cadence during PC+2.
- Added `resources/research/120_pc2_inverter_as508_format30_boundary.md`.
- Updated `resources/source-catalog/PC2_INVERTER_TELEMETRY_PRESENTATION_SOURCES.md`.

## Result

Apollo 13's own mission configuration materially narrows the cadence question without supplying a missing number. It supports this separation:

```text
normal LM telemetry / controller product
!=
CRT refresh cadence
!=
Format-30 post-pass high-rate playback
```

The current simulator must therefore continue to label inverter electrical display timing as project presentation behavior rather than recovered Apollo 13 timing.

## Still unresolved

- exact AS-508/LM-7 normal-format placement for `GC0071V` and `GC0155F`;
- exact live sample cadence during PC+2;
- exact Apollo 13 MSK destination and TELMU/CONTROL selection;
- whether either parameter belonged to an AS-508 Format-30 LM subformat;
- exact CRT refresh/latency and any actual PC+2 replay request.

## Validation

Research/documentation-only change. No physical-play PASS claim or station-maturity grade change is added.
