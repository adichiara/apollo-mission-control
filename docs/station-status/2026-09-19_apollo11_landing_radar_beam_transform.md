# Station research status — Apollo 11 landing-radar estimator chain

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

Apollo 11's onboard landing-radar velocity path is executable at equation level from the LM-5 source-controlled position geometry plus explicit measurement-time attitude inputs through propagation, residual qualification, and weighted correction. The profile now supplies the documented stow/hover `LRALPHA/LRBETA` pairs directly; callers no longer transcribe those constants.

Flown LUMINARY 099 constrains antenna-position behavior: beam geometry is recomputed for discrete position 2 after the repositioning job reports success; no continuous slew geometry is inferred. The LM-5 prelaunch erasable load independently supplies the position-specific values in revolutions.

This improves spacecraft-model completeness only. It does not change GUIDO station maturity or authorize an exact station display. No source here establishes that beam vectors, saved CDUs, or estimator intermediates were controller-visible, nor their ground cadence or formatting.

A newly cataloged primary NASA memorandum, D. A. Dyer's *LM landing radar test for the F mission — Project Apollo* (MSC-69-EG-14 / NASA-TM-X-64374, 11 Mar 1969; NTRS 19700025433), is a plausible precursor source for the unresolved LR numerical-error thread. The accessible NTRS record establishes that it concerns F-mission LR test requirements, but its PDF contents were not retrievable in this pass. No numerical requirement is therefore imported. Because it is F-mission evidence, any recovered value will still require an explicit Mission-G/LM-5 applicability bridge before controlling Apollo 11 simulation behavior.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, timing rule, or stochastic measurement rule is established.

## Player-facing boundary

Do not expose beam vectors, CDU/PIPA snapshots, `LRVTIME`, gravity terms, lunar-rotation correction, estimator internals, or precursor F-mission test requirements as Apollo-11 controller-visible telemetry/behavior without separate mission-effective evidence.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** source-controlled LM-5 position geometry + SETPOS + measurement-time NBSM beam path through the velocity estimator proof.
- **DOCUMENTED:** discrete position-1/position-2 recomputation behavior.
- **DOCUMENTED, ADJACENT EFFECTIVITY / CONTENT NOT YET INSPECTED:** MSC-69-EG-14 / NASA-TM-X-64374 is an F-mission LR test-requirements memorandum and a retrieval target for quantitative error evidence.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point arithmetic equivalence.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical landing-radar measurement-error/noise model; F-mission evidence alone cannot close it.
- **UNRESOLVED:** controller-visible radar/guidance product cadence, synchronization, and formatting.

No station maturity grade changes.
