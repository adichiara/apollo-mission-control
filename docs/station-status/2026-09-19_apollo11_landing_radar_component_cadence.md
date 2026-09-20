# Station research status — Apollo 11 landing-radar cadence and display boundary

Date: 2026-09-19

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is constrained to one LR velocity component during each 2-second Average-G/PIPA interval, cycling `Vz`, `Vx`, `Vy`. Mission-specific MSK-1137 evidence constrains the corresponding controller-visible LR field family: GOOD/BAD range/velocity status, body-axis `VXB/VYB/VZB`, slant range, PGNS altitude, display masks, and separately ground-computed `ACT ΔV`.

A new primary-source architecture check constrains the intervening ground path without inventing field-level details. The Apollo 11 Mission Operation Report identifies CCATS, RTCC, Display/Control, and MOCR/SSR as distinct MCC elements and states that telemetry/operational data can be processed by CCATS and RTCC for flight-control evaluation. NASA TN D-8316 independently describes the Apollo real-time display system as distinct computer-input and display subsystems.

## Station boundary

Keep these stages separate:

`LR physical measurement/error → LGC estimator/update → downlink/telemetry → CCATS/RTCC ground processing → Display/Control projection → controller-visible field`

The first, second, and final field semantics are constrained to the extent already documented. The newly reviewed sources now control the existence of the intervening ground/display layers. They do not identify the exact Apollo 11 MSK-1137 per-field route, transformation, numeric CRT refresh period, latency, stale threshold, or GUIDO request/key sequence.

The sensor-error boundary is unchanged: no historical GUIDO product should acquire invented Gaussian jitter merely to appear dynamic.

## Maturity

No station maturity change. This evidence strengthens the architecture contract and prevents direct-state aliasing, but it is not sufficient for historically timed live display behavior. Do not add a two-second controller refresh/freshness rule.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting at the recorded level.
- **DOCUMENTED:** Apollo 11 MCC separates CCATS/RTCC ground processing from Display/Control and controller operations.
- **UNRESOLVED / BLOCKED:** flight-authentic numerical LR stochastic error generation.
- **UNRESOLVED:** exact per-field Apollo 11 CCATS/RTCC routing/transformation and GUIDO/MCC-visible refresh cadence, latency, freshness policy, and request/key workflow.
