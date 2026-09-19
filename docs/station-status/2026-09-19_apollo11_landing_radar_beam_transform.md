# Station research status — Apollo 11 landing-radar estimator chain

Date: 2026-09-19

## GUIDO / guidance-monitoring consequence

Apollo 11's onboard landing-radar velocity path is source-controlled from antenna geometry through measurement-time propagation, residual qualification, and weighted correction. The source-derived SM/NB and antenna/NB transforms are now executable at equation level and verified against a separately coded literal `Sunburst37 AXISROT` oracle plus inverse/basis invariants.

This improves spacecraft-model completeness only. It does not change GUIDO station maturity or authorize an exact station display. No source here establishes that beam vectors, saved CDUs, or estimator intermediates were controller-visible, nor does it establish their ground cadence or formatting.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, or timing rule is established.

## Player-facing boundary

Do not expose beam vectors, CDU/PIPA snapshots, `LRVTIME`, gravity terms, lunar-rotation correction, or estimator internals as controller-visible telemetry without separate station-product evidence.

## Evidence status

- **DOCUMENTED / IMPLEMENTED:** Apollo-11-effective transform direction/order and equation-level floating-point SM/NB + antenna/NB transform.
- **VERIFIED:** production transform against literal source-equation oracle, identity, inverse, norm, and orthogonality checks.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point arithmetic equivalence.
- **DOCUMENTED / IMPLEMENTED:** explicit-input propagation, qualification, weighting/correction, and composed estimator proof with supplied beam.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical landing-radar measurement-error/noise model.
- **UNRESOLVED:** controller-visible radar/guidance product cadence, synchronization, and formatting.

No station maturity grade changes.