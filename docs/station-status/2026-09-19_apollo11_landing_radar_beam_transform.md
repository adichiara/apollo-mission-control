# Station research status — Apollo 11 landing-radar estimator chain

Date: 2026-09-19

## GUIDO / guidance-monitoring consequence

Apollo 11's onboard landing-radar velocity path is source-controlled from antenna geometry through measurement-time propagation, residual qualification, and weighted correction. The executable proof currently composes those arithmetic stages while requiring the selected measurement-time beam explicitly.

Research 501 removes the remaining rotation-order ambiguity without inventing a modern convention. LUMINARY 099 controls Y-Z-X input order and SM→NB/NB→SM direction; the earlier primary MIT `Sunburst37` implementation independently gives the corresponding Y→Z→X and inverse X→Z→Y axis sequences; LUMINARY 099 `FLESHPOT` provides a same-program matrix cross-check.

The remaining historical beam-synthesis gate is numerical verification of a floating-point port against original AGC behavior. Until that fixture passes, the explicit beam dependency remains correct.

This does not change GUIDO station maturity or authorize an exact station display. No source here establishes which onboard intermediate values were presented to Mission Control, their ground cadence, or formatting.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, or timing rule is established.

## Player-facing boundary

Do not expose beam vectors, CDU/PIPA snapshots, `LRVTIME`, gravity terms, lunar-rotation correction, or estimator internals as controller-visible telemetry without separate station-product evidence.

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static geometry and transform-direction/order semantics.
- **CORROBORATED:** transform sequence by independent primary Apollo software and LUMINARY 099 matrix construction.
- **DOCUMENTED / IMPLEMENTED:** explicit-input propagation, qualification, weighting/correction, and composed estimator proof with supplied beam.
- **PARTIALLY IMPLEMENTED:** historical beam synthesis; numerical-equivalence fixture remains required.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical landing-radar measurement-error/noise model.
- **UNRESOLVED:** controller-visible radar/guidance product cadence, synchronization, and formatting.

No station maturity grade changes.