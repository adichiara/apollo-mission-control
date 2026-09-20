# Station research status — Apollo 11 landing-radar cadence and error boundary

Date: 2026-09-19

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is constrained to one of the three LR velocity components during each 2-second Average-G/PIPA interval, cycling `Vz`, `Vx`, `Vy`.

The mission-specific AC Electronics Apollo 11 MSK-1137 definition now constrains the corresponding controller-visible LR field family without equating that onboard cadence to display cadence. It defines LR range and velocity validity as GOOD/BAD, `VXB/VYB/VZB` as landing-radar velocity in **body-axis coordinates** at `±XXXX FT/SEC`, landing-radar slant range as `XXXXX FT`, and PGNS-computed altitude as `XXXXX FT`. It also labels `ACT ΔV` separately as ground computed.

This matters because research note 030's direct source comparison shows Apollo 13 MSK-1137 changed the LR velocity family to stable-member coordinates and changed several altitude/comparison semantics. A generic cross-mission “MSK 1137 landing radar” product would therefore be historically wrong.

The sensor-error research also prevents an unsupported assumption from leaking into controller products. LM-5 primary test history says a preflight one-count velocity bias was corrected and that a Gaussian Doppler-simulator test-limit assumption required correction for heavier tails. Apollo 11 flight data were reported within specification limits apart from low/near-zero-Doppler behavior, but no numerical flight-effective stochastic distribution was recovered.

Therefore no historical GUIDO product should acquire invented Gaussian jitter merely to make the spacecraft estimator look dynamic.

## Station boundary

Keep these stages separate:

`LR physical measurement/error → LGC 2-s component-update schedule → downlink → ground processing → controller product/display`

The LGC component-update schedule is documented. The Apollo 11 MSK-1137 LR field identity/frame/units/display mask are documented. Flight-authentic stochastic sensor generation is **BLOCKED** pending numerical LM-5/Apollo-11-effective evidence. Exact downlink/ground routing and controller refresh cadence, latency, freshness, and request workflow remain unresolved.

## Maturity

No station maturity change. The new evidence is sufficient to prevent a wrong coordinate frame or Apollo-13-style residual presentation in an eventual Apollo 11 display profile, but it is not sufficient to implement historically timed live display behavior. Do not add a two-second controller refresh/freshness rule.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR status, body-axis velocity, slant-range, PGNS-altitude field semantics, units, and display masks.
- **DOCUMENTED:** `ACT ΔV` is identified by the Apollo 11 display definition as ground computed.
- **DOCUMENTED:** corrected LM-5 preflight one-count bias and non-adequacy of the cited Gaussian simulator test-limit assumption.
- **UNRESOLVED / BLOCKED:** flight-authentic numerical LR stochastic error generation.
- **UNRESOLVED:** exact Apollo 11 downlink/ground routing and GUIDO/MCC-visible refresh cadence, latency, freshness, and request workflow.
