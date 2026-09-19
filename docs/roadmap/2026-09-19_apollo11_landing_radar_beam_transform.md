# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-19
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. `SETPOS1` selects the first alpha/beta pair; `SETPOS2` selects the second pair, and the listing recomputes the antenna beam vectors after the physical antenna reaches position 2. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G G PRELAUNCH ERASABLE LOAD, SNA-8-D-027(II) Rev 1, Table LM5/4.5.1-1 directly supplies `LRALPHA1=0.0163371759 rev`, `LRBETA1=0.0665287037 rev`, `LRALPHA2=0.0161680555 rev`, and `LRBETA2=0.0001361111 rev` at addresses 2522–2525.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain. The Apollo 11 LM-5 profile now stores both position-specific angle pairs in their documented source unit (revolution), with a profile adapter converting to radians only when constructing `LandingRadarBeamGeometryInput`. Callers therefore select position 1 or 2 plus measurement-time CDUs without manually transcribing historical constants.

This closes the profile-adapter implementation item without inventing continuous antenna motion, attitude, radar measurements, or noise. Bit-for-bit AGC fixed-point equivalence is not claimed.

## Next work

1. Pursue spacecraft downlink, ground processing, and controller-visible cadence/formatting as the next independent evidence thread; onboard 2-second component cadence is not a controller-display contract.
2. Keep historical stochastic LR measurement generation BLOCKED until flight-effective numerical error evidence is recovered.
3. Preserve optional yaAGC/AGC-fixed-point comparison as validation hardening if a later dependency requires machine-level rounding equivalence.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** SETPOS antenna→NB beam construction plus measurement-time NB→SM transform in the velocity chain.
- **DOCUMENTED / IMPLEMENTED:** LM-5 position-1/position-2 alpha/beta loads and provenance-bearing profile adapter.
- **DOCUMENTED:** discrete position-1/position-2 selection/recomputation behavior in flown LUMINARY 099.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point rounding equivalence.
- **BLOCKED:** historical stochastic LR measurement generation.
- **UNRESOLVED:** controller-visible product timing/formatting.
