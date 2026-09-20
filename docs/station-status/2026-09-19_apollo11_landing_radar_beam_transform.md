# Station research status — Apollo 11 landing-radar estimator chain

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

Apollo 11's onboard landing-radar velocity path is executable at equation level from the LM-5 source-controlled position geometry plus explicit measurement-time attitude inputs through propagation, residual qualification, and weighted correction. The profile now supplies the documented stow/hover `LRALPHA/LRBETA` pairs directly; callers no longer transcribe those constants.

Flown LUMINARY 099 constrains antenna-position behavior: beam geometry is recomputed for discrete position 2 after the repositioning job reports success; no continuous slew geometry is inferred. The LM-5 prelaunch erasable load independently supplies the position-specific values in revolutions.

This improves spacecraft-model completeness only. It does not change GUIDO station maturity or authorize an exact station display. No source here establishes that beam vectors, saved CDUs, or estimator intermediates were controller-visible, nor their ground cadence or formatting.

A NASA primary-source table reproducing GAEC master end-item specification **LSP-470-2D** supplies the quantitative landing-radar performance envelope. Range accuracy is 3 sigma `1.4% + 15 ft` at 2,000–25,000 ft and `1.4% + 5 ft` at 10–2,000 ft. Velocity accuracy to the LGC is also 3 sigma: 25,000–2,000 ft — Vx `1.5% or 1.5 ft/s`, Vy `2.0% or 2.0 ft/s`, Vz `2.0% or 2.0 ft/s`; 2,000–200 ft — Vx `1.5% or 1.5 ft/s`, Vy `3.5% or 3.5 ft/s`, Vz `3.0% or 3.0 ft/s`; 200–5 ft — Vx `1.5% or 1.5 ft/s`, Vy `2.0% or 1.5 ft/s`, Vz `2.0% or 1.5 ft/s`. The source says use percentage or ft/s, whichever is greater, with percentages referenced to vector velocity. This is useful for validation and scenario-bound checks, but it is **not** evidence that historical measurement error was Gaussian. NASA TN D-6849 records that a Gaussian assumption used in Doppler-spectrum-simulator test limits had to be corrected because the simulator approximation put more energy in the tails. Accordingly, no stochastic generator is authorized from the 3-sigma table alone.

D. A. Dyer's *LM landing radar test for the F mission — Project Apollo* (MSC-69-EG-14 / NASA-TM-X-64374, 11 Mar 1969; NTRS 19700025433) remains a plausible adjacent-effectivity source for additional test/error detail. Its numerical contents remain uninspected and cannot silently override or specialize the Mission-G boundary.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, timing rule, or stochastic measurement rule is established.

## Player-facing boundary

Do not expose beam vectors, CDU/PIPA snapshots, `LRVTIME`, gravity terms, lunar-rotation correction, estimator internals, or precursor F-mission test requirements as Apollo-11 controller-visible telemetry/behavior without separate mission-effective evidence. Do not present the LSP-470-2D 3-sigma limits as a controller alarm/redline unless controller-facing evidence is found.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** source-controlled LM-5 position geometry + SETPOS + measurement-time NBSM beam path through the velocity estimator proof.
- **DOCUMENTED:** discrete position-1/position-2 recomputation behavior.
- **DOCUMENTED:** landing-radar 3-sigma range and altitude-banded component velocity performance envelope from GAEC LSP-470-2D as reproduced in NASA primary material.
- **DOCUMENTED:** TN D-6849 warns against treating its Doppler-spectrum-simulator test distribution as simply Gaussian.
- **DOCUMENTED, ADJACENT EFFECTIVITY / CONTENT NOT YET INSPECTED:** MSC-69-EG-14 / NASA-TM-X-64374 is an F-mission LR test-requirements memorandum.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point arithmetic equivalence.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective stochastic landing-radar measurement-error distribution/process beyond the documented performance envelope.
- **UNRESOLVED:** controller-visible radar/guidance product cadence, synchronization, and formatting.

No station maturity grade changes.
