# Station research status — Apollo 11 landing-radar estimator chain

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

Apollo 11's onboard landing-radar velocity path is executable at equation level from the LM-5 source-controlled position geometry plus explicit measurement-time attitude inputs through propagation, residual qualification, and weighted correction. The profile supplies the documented stow/hover `LRALPHA/LRBETA` pairs directly.

Flown LUMINARY 099 constrains antenna-position behavior: beam geometry is recomputed for discrete position 2 after the repositioning job reports success; no continuous slew geometry is inferred.

This improves spacecraft-model completeness only. It does not change GUIDO station maturity or authorize an exact station display. No source here establishes that beam vectors, saved CDUs, or estimator intermediates were controller-visible, nor their ground cadence or formatting.

GAEC master end-item specification LSP-470-2D, reproduced in NASA primary material, supplies the quantitative 3-sigma LR performance envelope. It remains a validation/acceptance envelope, not evidence that historical measurement error was Gaussian.

The Apollo 11 Mission Report supplies mission-event timing for the two expected zero-Doppler tracking losses during manual maneuvering. Table 5-I records `Landing radar data not good` at 102:44:11 and `data good` at 102:44:21, then `data not good` at 102:44:59 and `data good` at 102:45:03. At the table's one-second event resolution, the recorded not-good intervals are therefore 10 seconds and 4 seconds. These replace the prior open-ended statement that no duration evidence existed; they do not establish sub-second transition times or a generalized dropout probability.

The Apollo 11 AC Electronics guidance manual adds a separate qualification rule: LR `DATA GOOD` must have been present for at least four seconds before the range/velocity measurement tests permit state-vector updating. A historical replay must therefore distinguish the sensor's recorded good/not-good discrete from the LGC's later eligibility to consume reacquired LR data. Do not resume LR-aided state updates merely because the Mission Report event table has changed back to `DATA GOOD`.

NASA TN D-6849 independently records generally in-spec LM-5 behavior except near zero Doppler and warns against treating its Doppler-spectrum-simulator test distribution as simply Gaussian. Dyer's F-mission test memorandum remains adjacent-effectivity evidence with uninspected numerical contents.

NASA-CR-92466 / TRW-11176-H059-R0-00 (25 Oct 1968) is now identified as a mission-period primary contractor source whose stated purpose is LR altimeter beam-bandwidth and Doppler equations for mathematical-model use. It may strengthen physical-model verification after inspection, but does not establish LM-5 flight residual statistics.

A later LM10-and-subsequent Apollo Operations Handbook documents selectable LR range/velocity quantities at the LGC radar interface and describes the LR digital quantities as 15-bit binary words. This is an adjacent architecture cross-check only. Its later effectivity does not authorize an Apollo 11 bit weighting, quantization step, display cadence, or noise model.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, or stochastic measurement rule is established. The timed not-good intervals are spacecraft/sensor history unless separate evidence establishes a controller-visible product or callout.

## Player-facing boundary

Do not expose estimator internals or precursor test requirements as controller-visible telemetry without separate mission-effective evidence. Do not present the 3-sigma limits as a controller alarm/redline. Do not invent controller-visible symptoms for the two documented tracking losses. The 10-second and 4-second intervals are event-table timing anchors, not random-dropout parameters. Do not render a 15-bit Apollo 11 quantizer merely from the later LM10 handbook.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** source-controlled LM-5 position geometry + SETPOS + measurement-time NBSM beam path through the velocity estimator proof.
- **DOCUMENTED:** landing-radar 3-sigma performance envelope from GAEC LSP-470-2D as reproduced in NASA primary material.
- **DOCUMENTED, APOLLO 11 FLIGHT:** range/velocity acquisition at ~44,000/~28,000-ft slant range; recorded `DATA NOT GOOD` intervals 102:44:11–:21 and 102:44:59–102:45:03, attributed by the Mission Report to expected zero-Doppler effects during manual maneuvering.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** at least four continuous seconds of `DATA GOOD` are required before LR measurement tests permit state-vector updating.
- **DOCUMENTED:** TN D-6849 cautions against a simple Gaussian simulator-error assumption.
- **DOCUMENTED, MISSION-PERIOD MODEL SOURCE:** NASA-CR-92466 concerns verified LR beam-bandwidth/Doppler equations for mathematical-model use; not flight-error statistics.
- **ADJACENT EFFECTIVITY:** LM10-and-subsequent handbook documents selectable LR digital quantities/15-bit interface architecture; no Apollo 11 quantization constant is inferred.
- **NOT CLAIMED:** sub-second dropout transition timing, random dropout probability, controller-visible symptom, Apollo-11-effective LR bit weighting, or bit-for-bit AGC fixed-point equivalence.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective stochastic LR measurement-error distribution/process beyond the documented performance envelope and discrete flight events.
- **UNRESOLVED:** controller-visible radar/guidance cadence, synchronization, formatting, and symptoms of the documented tracking losses.

No station maturity grade changes.
