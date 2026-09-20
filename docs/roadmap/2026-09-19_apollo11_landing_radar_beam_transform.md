# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-19
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. `SETPOS1` selects the first alpha/beta pair; `SETPOS2` selects the second pair, and the listing recomputes the antenna beam vectors after the physical antenna reaches position 2. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G G PRELAUNCH ERASABLE LOAD, SNA-8-D-027(II) Rev 1, Table LM5/4.5.1-1 directly supplies `LRALPHA1=0.0163371759 rev`, `LRBETA1=0.0665287037 rev`, `LRALPHA2=0.0161680555 rev`, and `LRBETA2=0.0001361111 rev` at addresses 2522–2525.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain. The Apollo 11 LM-5 profile now stores both position-specific angle pairs in their documented source unit (revolution), with a profile adapter converting to radians only when constructing `LandingRadarBeamGeometryInput`. Callers therefore select position 1 or 2 plus measurement-time CDUs without manually transcribing historical constants.

This closes the profile-adapter implementation item without inventing continuous antenna motion, attitude, radar measurements, or noise. Bit-for-bit AGC fixed-point equivalence is not claimed.

A renewed primary-source inspection of the mission-specific AC Electronics Apollo 11 guidance/navigation summary also narrows the controller-product boundary. MSK-1137 explicitly defines controller-visible landing-radar `LR RNG` and `VEL` GOOD/BAD status, `VXB/VYB/VZB` velocity in **body-axis coordinates** at `±XXXX FT/SEC`, landing-radar slant range at `XXXXX FT`, and PGNS-computed altitude at `XXXXX FT`. The same page distinguishes ground-computed `ACT ΔV` from onboard/spacecraft quantities. Existing research note 030 had already established that Apollo 13's same-numbered MSK-1137 changes the LR velocity presentation to stable-member coordinates and changes altitude/comparison semantics; therefore the Apollo 11 field contract must remain mission-specific.

This closes the previously broad **formatting** question only to the level directly printed on MSK-1137: field identity, meaning, frame, units, and displayed precision/mask for these LR families. It does **not** establish the exact ground transformation/routing for every field, display refresh cadence, latency, freshness, or station request workflow.

## Next work

1. Pursue Apollo-11-effective downlink/ground-routing provenance and exact CRT refresh behavior. Onboard 2-second component cadence is not a controller-display contract.
2. Keep historical stochastic LR measurement generation BLOCKED until flight-effective numerical error evidence is recovered.
3. Preserve optional yaAGC/AGC-fixed-point comparison as validation hardening if a later dependency requires machine-level rounding equivalence.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** SETPOS antenna→NB beam construction plus measurement-time NB→SM transform in the velocity chain.
- **DOCUMENTED / IMPLEMENTED:** LM-5 position-1/position-2 alpha/beta loads and provenance-bearing profile adapter.
- **DOCUMENTED:** discrete position-1/position-2 selection/recomputation behavior in flown LUMINARY 099.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field identities, body-axis velocity frame, units, displayed precision/masks, and distinction of ground-computed `ACT ΔV`.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point rounding equivalence.
- **BLOCKED:** historical stochastic LR measurement generation.
- **UNRESOLVED:** exact Apollo 11 downlink/ground routing and controller-display cadence, latency, freshness, and request workflow.
