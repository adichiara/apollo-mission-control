# Station research status — Apollo 11 landing-radar cadence and error boundary

Date: 2026-09-19

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is constrained to one of the three LR velocity components during each 2-second Average-G/PIPA interval, cycling `Vz`, `Vx`, `Vy`.

Research note 501 also prevents an unsupported sensor assumption from leaking into controller products. LM-5 primary test history says a preflight one-count velocity bias was corrected and that a Gaussian Doppler-simulator test-limit assumption required correction for heavier tails. Apollo 11 flight data were reported within specification limits apart from low/near-zero-Doppler behavior, but no numerical flight-effective stochastic distribution was recovered.

Therefore no historical GUIDO product should acquire invented Gaussian jitter merely to make the spacecraft estimator look dynamic.

## Station boundary

Keep these stages separate:

`LR physical measurement/error → LGC 2-s component-update schedule → downlink → ground processing → controller product/display`

The LGC component-update schedule is documented. Flight-authentic stochastic sensor generation is **BLOCKED** pending numerical LM-5/Apollo-11-effective evidence. Downstream ground/display cadence and formatting remain unresolved.

## Maturity

No station maturity change. Do not add a two-second controller refresh/freshness rule or an invented stochastic display-noise rule from this evidence.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule.
- **DOCUMENTED:** corrected LM-5 preflight one-count bias and non-adequacy of the cited Gaussian simulator test-limit assumption.
- **UNRESOLVED / BLOCKED:** flight-authentic numerical LR stochastic error generation.
- **UNRESOLVED:** GUIDO/MCC-visible landing-radar or derived-guidance product cadence, latency, freshness, and formatting.
