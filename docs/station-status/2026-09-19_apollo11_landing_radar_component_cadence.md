# Station research status — Apollo 11 landing-radar cadence and display boundary

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is constrained to one LR velocity component during each 2-second Average-G/PIPA interval, cycling `Vz`, `Vx`, `Vy`. Mission-specific MSK-1137 evidence constrains the controller-visible LR field family: GOOD/BAD range/velocity status, body-axis `VXB/VYB/VZB`, slant range, PGNS altitude, display masks, and separately ground-computed `ACT ΔV`.

Apollo 11 ground-system evidence constrains the intervening CCATS/RTCC and Display/Control layers. NASA TN D-8316 establishes buffered dynamic display updates independent of CRT refresh and separates reference-slide access from dynamic-word update.

A primary Apollo 12 flight manual provides adjacent-effectivity evidence for the request mechanism: a DRK could request a specific RTCC display format directly by labeled PBI and was described as having the same capability as the MSK in display-request mode, except that DRK callup avoided thumbwheel selection. This clarifies the architectural distinction between direct-format PBIs and MSK coded selection. It does not establish Apollo 11 GUIDO hardware assignment or the descent workflow.

## Station boundary

`LR physical measurement/error → LGC estimator/update → downlink/telemetry → CCATS/RTCC ground processing → Display/Control dynamic-word update/presentation → controller-visible field`

Keep display content, display-data update, CRT refresh, and operator format request as separate concepts. Do not expose a DRK on Apollo 11 GUIDO merely because a later mission manual documents the device.

## Maturity

No station maturity change. Apollo-11-effective evidence is still required before implementing GUIDO's exact request controls or powered-descent display-selection workflow.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting at the recorded level.
- **DOCUMENTED:** Apollo MCC separates CCATS/RTCC processing from Display/Control/controller operations.
- **DOCUMENTED:** D/TV dynamic updates were buffered and independent of CRT refresh requirements; the four-second TN D-8316 figure concerns reference-slide access.
- **DOCUMENTED, ADJACENT EFFECTIVITY:** Apollo 12 flight manual defines DRK direct-PBI request behavior and equivalence to MSK display-request mode.
- **DOCUMENTED:** PHO-TN401 identity and physical archival location.
- **BLOCKED:** direct PHO-TN401 inspection; flight-authentic numerical LR stochastic error generation.
- **UNRESOLVED:** Apollo 11 GUIDO DRK/MSK equipment and request sequence, exact per-field CCATS/RTCC routing/transformation, numeric dynamic-data cadence/latency/freshness, and powered-descent format selection.
