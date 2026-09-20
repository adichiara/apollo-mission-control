# Station research status — Apollo 11 landing-radar cadence and display boundary

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is constrained to one LR velocity component during each 2-second Average-G/PIPA interval, cycling `Vz`, `Vx`, `Vy`. Mission-specific MSK-1137 evidence constrains the controller-visible LR field family: GOOD/BAD range/velocity status, body-axis `VXB/VYB/VZB`, slant range, PGNS altitude, display masks, and separately ground-computed `ACT ΔV`.

Apollo 11 ground-system evidence constrains the intervening CCATS/RTCC and Display/Control layers. PHO-TN401 is identified to a physical archival holding but direct inspection is **BLOCKED**.

NASA TN D-8316 additionally establishes that D/TV generators buffered dynamic display data: computers could update a complete instruction list or a single data word independently of CRT refresh requirements. Its four-second timing figure is for reference-slide access. Thus display selection, reference-slide access, dynamic-word update, and CRT refresh are distinct and must not be assigned one inferred cadence.

## Station boundary

`LR physical measurement/error → LGC estimator/update → downlink/telemetry → CCATS/RTCC ground processing → Display/Control dynamic-word update/presentation → controller-visible field`

The reviewed sources do not identify the exact Apollo 11 MSK-1137 per-field route, transformation, numeric dynamic-data update period, latency, stale threshold, GUIDO request/key sequence, or powered-descent display-selection pattern. The sensor-error boundary is unchanged: no historical GUIDO product should acquire invented Gaussian jitter merely to appear dynamic.

## Maturity

No station maturity change. Do not add a two-second controller refresh/freshness rule, and do not reinterpret the four-second reference-slide access requirement as dynamic telemetry cadence.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting at the recorded level.
- **DOCUMENTED:** Apollo MCC separates CCATS/RTCC processing from Display/Control/controller operations.
- **DOCUMENTED:** D/TV dynamic updates were buffered and independent of CRT refresh requirements; the four-second TN D-8316 figure concerns reference-slide access.
- **DOCUMENTED:** PHO-TN401 identity and physical archival location.
- **BLOCKED:** direct PHO-TN401 inspection; flight-authentic numerical LR stochastic error generation.
- **UNRESOLVED:** exact per-field Apollo 11 CCATS/RTCC routing/transformation, numeric dynamic-data cadence/latency/freshness, GUIDO request/key workflow, and powered-descent format selection.