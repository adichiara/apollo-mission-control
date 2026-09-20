# Station research status — Apollo 11 landing-radar estimator chain

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

Apollo 11's onboard landing-radar velocity path is executable at equation level from the LM-5 source-controlled position geometry plus explicit measurement-time attitude inputs through propagation, residual qualification, and weighted correction. The profile now supplies the documented stow/hover `LRALPHA/LRBETA` pairs directly; callers no longer transcribe those constants.

Flown LUMINARY 099 constrains antenna-position behavior: beam geometry is recomputed for discrete position 2 after the repositioning job reports success; no continuous slew geometry is inferred. The LM-5 prelaunch erasable load independently supplies the position-specific values in revolutions.

This improves spacecraft-model completeness only. It does not change GUIDO station maturity or authorize an exact station display. No source here establishes that beam vectors, saved CDUs, or estimator intermediates were controller-visible, nor their ground cadence or formatting.

A NASA primary-source table reproducing GAEC master end-item specification **LSP-470-2D** supplies the quantitative landing-radar performance envelope. Range accuracy is 3 sigma `1.4% + 15 ft` at 2,000–25,000 ft and `1.4% + 5 ft` at 10–2,000 ft. Velocity accuracy to the LGC is also 3 sigma: 25,000–2,000 ft — Vx `1.5% or 1.5 ft/s`, Vy `2.0% or 2.0 ft/s`, Vz `2.0% or 2.0 ft/s`; 2,000–200 ft — Vx `1.5% or 1.5 ft/s`, Vy `3.5% or 3.5 ft/s`, Vz `3.0% or 3.0 ft/s`; 200–5 ft — Vx `1.5% or 1.5 ft/s`, Vy `2.0% or 1.5 ft/s`, Vz `2.0% or 1.5 ft/s`. The source says use percentage or ft/s, whichever is greater, with percentages referenced to vector velocity. This is useful for validation and scenario-bound checks, but it is **not** evidence that historical measurement error was Gaussian.

The Apollo 11 Mission Report supplies a stronger mission-event boundary than the later experience-report summary: range and velocity were acquired at slant ranges of approximately 44,000 and 28,000 ft; tracking was then lost briefly at altitudes of 240 and 75 ft. The report explicitly says those losses were expected and attributes them to zero-Doppler effects associated with manual maneuvering. These are source-controlled Apollo 11 events suitable for historical scenario validation. They do **not** authorize a generalized dropout probability, invented loss duration, or zero-Doppler stochastic algorithm.

NASA TN D-6849 independently records generally in-spec LM-5 behavior except near zero Doppler and warns against treating its Doppler-spectrum-simulator test distribution as simply Gaussian. D. A. Dyer's *LM landing radar test for the F mission — Project Apollo* (MSC-69-EG-14 / NASA-TM-X-64374, 11 Mar 1969; NTRS 19700025433) remains a plausible adjacent-effectivity source for additional test/error detail. Its numerical contents remain uninspected and cannot silently override or specialize the Mission-G boundary.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, timing rule, or stochastic measurement rule is established. The 240-ft and 75-ft tracking-loss events are spacecraft/sensor history unless separate evidence establishes a controller-visible product or callout.

## Player-facing boundary

Do not expose beam vectors, CDU/PIPA snapshots, `LRVTIME`, gravity terms, lunar-rotation correction, estimator internals, or precursor F-mission test requirements as Apollo-11 controller-visible telemetry/behavior without separate mission-effective evidence. Do not present the LSP-470-2D 3-sigma limits as a controller alarm/redline unless controller-facing evidence is found. Do not invent controller-visible symptoms for the documented 240-ft/75-ft tracking losses.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** source-controlled LM-5 position geometry + SETPOS + measurement-time NBSM beam path through the velocity estimator proof.
- **DOCUMENTED:** discrete position-1/position-2 recomputation behavior.
- **DOCUMENTED:** landing-radar 3-sigma range and altitude-banded component velocity performance envelope from GAEC LSP-470-2D as reproduced in NASA primary material.
- **DOCUMENTED, APOLLO 11 FLIGHT:** range/velocity acquisition at approximately 44,000/28,000-ft slant range; brief expected tracking losses at 240/75-ft altitude attributed to zero-Doppler effects during manual maneuvering.
- **DOCUMENTED:** TN D-6849 warns against treating its Doppler-spectrum-simulator test distribution as simply Gaussian.
- **DOCUMENTED, ADJACENT EFFECTIVITY / CONTENT NOT YET INSPECTED:** MSC-69-EG-14 / NASA-TM-X-64374 is an F-mission LR test-requirements memorandum.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point arithmetic equivalence.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective stochastic landing-radar measurement-error distribution/process beyond the documented performance envelope and discrete flight events.
- **UNRESOLVED:** controller-visible radar/guidance product cadence, synchronization, formatting, and symptoms of the documented tracking losses.

No station maturity grade changes.
