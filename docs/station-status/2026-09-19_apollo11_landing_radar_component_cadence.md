# Station research status — Apollo 11 landing-radar component cadence

Date: 2026-09-19

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is now better constrained: Apollo 11 technical documentation states that one of the three LR velocity components is used during each 2-second Average-G/PIPA interval, with the illustrated sequence cycling `Vz`, `Vx`, `Vy`.

This improves the source boundary for the simulated spacecraft estimator but does **not** raise GUIDO/controller-product maturity. No direct evidence in this slice establishes that Mission Control received, processed, or displayed a fresh LR-derived product every two seconds.

## Station boundary

Keep these clocks separate in implementation and documentation:

`LR measurement/read → LGC 2-s component-update schedule → downlink → ground processing → controller product/display`

Only the LGC component-update schedule is closed here. The downstream ground/display cadence and formatting remain unresolved.

## Maturity

No station maturity change. Do not add a two-second controller refresh or freshness rule from this evidence alone.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule.
- **UNRESOLVED:** GUIDO/MCC-visible landing-radar or derived-guidance product cadence, latency, freshness, and formatting.
