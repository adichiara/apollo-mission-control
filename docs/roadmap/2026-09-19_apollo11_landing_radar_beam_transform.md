# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-19
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. `SETPOS1` selects the first alpha/beta pair; `SETPOS2` selects the second pair, and the listing recomputes the antenna beam vectors after the physical antenna reaches position 2. Memo #95 controls antenna→NB beta-then-alpha semantics; the LM-5 Mission G load remains the authority for the actual position-specific alpha/beta values.

## Completed

The equation-level SETPOS and SM/NB transforms are now composed into the landing-radar velocity estimator chain. The chain can either retain an explicit beam for synthetic/unit work or accept explicit historical geometry inputs (alpha, beta, and saved measurement-time CDUs), construct the selected X/Y/Z beam in NB, transform it NB→SM, then continue through propagation, projection, residual qualification, and weighted correction.

This closes the former beam-synthesis implementation gate without hard-coding or inventing LM-5 angles/CDUs. It does not claim bit-for-bit AGC fixed-point equivalence.

## Next work

1. Add a controlled LM-5 profile adapter for the recovered position-1/position-2 pad-load angles so callers do not manually transcribe them; retain mission/configuration provenance.
2. Keep historical stochastic LR measurement generation BLOCKED until flight-effective numerical error evidence is recovered.
3. Pursue spacecraft downlink, ground processing, and controller-visible cadence/formatting separately from onboard estimator behavior.
4. Preserve optional yaAGC/AGC-fixed-point comparison as validation hardening if a later dependency requires machine-level rounding equivalence.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** SETPOS antenna→NB beam construction plus measurement-time NB→SM transform in the velocity chain.
- **DOCUMENTED:** position 1 vs position 2 selection/recomputation behavior in flown LUMINARY 099.
- **DOCUMENTED:** LM-5 position-specific alpha/beta loads; profile adapter remains implementation work.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point rounding equivalence.
- **BLOCKED:** historical stochastic LR measurement generation.
- **UNRESOLVED:** controller-visible product timing/formatting.
