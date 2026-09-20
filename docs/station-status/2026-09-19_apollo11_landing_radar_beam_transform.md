# Station research status — Apollo 11 landing-radar estimator chain

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

Apollo 11's onboard landing-radar velocity path is executable at equation level from the LM-5 source-controlled position geometry plus explicit measurement-time attitude inputs through propagation, residual qualification, and weighted correction. The profile supplies the documented stow/hover `LRALPHA/LRBETA` pairs directly.

Flown LUMINARY 099 constrains antenna-position behavior: beam geometry is recomputed for discrete position 2 after the repositioning job reports success; no continuous slew geometry is inferred.

This improves spacecraft-model completeness only. It does not change GUIDO station maturity or authorize an exact station display. No source here establishes that beam vectors, saved CDUs, or estimator intermediates were controller-visible, nor their ground cadence or formatting.

GAEC master end-item specification LSP-470-2D, reproduced in NASA primary material, supplies the quantitative 3-sigma LR performance envelope. It remains a validation/acceptance envelope, not evidence that historical measurement error was Gaussian.

The Apollo 11 Mission Report supplies mission-event timing for the two expected zero-Doppler tracking losses during manual maneuvering. Table 5-I records `Landing radar data not good` at 102:44:11 and `data good` at 102:44:21, then `data not good` at 102:44:59 and `data good` at 102:45:03. At the table's one-second event resolution, the recorded not-good intervals are therefore 10 seconds and 4 seconds. These replace the prior open-ended statement that no duration evidence existed; they do not establish sub-second transition times or a generalized dropout probability.

The Apollo 11 AC Electronics guidance manual adds a separate qualification rule: LR `DATA GOOD` must have been present for at least four seconds before the range/velocity measurement tests permit state-vector updating. A historical replay must therefore distinguish the sensor's recorded good/not-good discrete from the LGC's later eligibility to consume reacquired LR data.

NASA TN D-6849 independently records generally in-spec LM-5 behavior except near zero Doppler and warns against treating its Doppler-spectrum-simulator test distribution as simply Gaussian. Dyer's F-mission test memorandum remains adjacent-effectivity evidence with uninspected numerical contents.

NASA-CR-92466 / TRW-11176-H059-R0-00 (25 Oct 1968) is a mission-period primary contractor source for LR altimeter beam-bandwidth and Doppler equations. It may strengthen physical-model verification after inspection, but does not establish LM-5 flight residual statistics.

The flown Apollo 11 LUMINARY 099 listing now narrows the interface/scaling gap directly. `ASSEMBLY_AND_OPERATION_INFORMATION.agc` gives low-scale LR altitude a low-order bit weight of `1.079 ft`, with X/Y/Z LR velocity low-order bit weights of `-0.6440`, `+1.212`, and `+0.8668 ft/s`. `PINBALL_NOUN_TABLES.agc` contains the corresponding constants, and `SERVICER.agc` independently marks stored `HMEAS` as `1.079 FT/BIT`. These are Apollo-11-effective onboard converted/stored measurement scales, not proof of the complete LM-5 serial-transfer encoding.

A later LM10-and-subsequent Apollo Operations Handbook and later R-567 revisions document 15-bit raw LR/LGC words and raw conversion details. They remain adjacent architecture cross-checks for unresolved serial-interface details; they are not needed to establish the flown LUMINARY-side scales above.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, or stochastic measurement rule is established. The timed not-good intervals are spacecraft/sensor history unless separate evidence establishes a controller-visible product or callout.

## Player-facing boundary

Do not expose estimator internals or precursor test requirements as controller-visible telemetry without separate mission-effective evidence. Do not present the 3-sigma limits as a controller alarm/redline. Do not invent controller-visible symptoms for the two documented tracking losses. The 10-second and 4-second intervals are event-table timing anchors, not random-dropout parameters. The flown LUMINARY bit weights may constrain onboard converted values, but do not render a claimed bit-for-bit LM-5 serial quantizer until raw encoding/rounding evidence is recovered.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** source-controlled LM-5 position geometry + SETPOS + measurement-time NBSM beam path through the velocity estimator proof.
- **DOCUMENTED:** landing-radar 3-sigma performance envelope from GAEC LSP-470-2D as reproduced in NASA primary material.
- **DOCUMENTED, APOLLO 11 FLIGHT:** range/velocity acquisition at ~44,000/~28,000-ft slant range; recorded `DATA NOT GOOD` intervals 102:44:11–:21 and 102:44:59–102:45:03, attributed by the Mission Report to expected zero-Doppler effects during manual maneuvering.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** at least four continuous seconds of `DATA GOOD` are required before LR measurement tests permit state-vector updating.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD SCALING:** low-scale altitude `1.079 ft/bit`; X/Y/Z velocity low-order bit weights `-0.6440/+1.212/+0.8668 ft/s` in the converted/stored LUMINARY representation.
- **DOCUMENTED:** TN D-6849 cautions against a simple Gaussian simulator-error assumption and establishes a serial-binary LGC path separate from local display outputs.
- **DOCUMENTED, MISSION-PERIOD MODEL SOURCE:** NASA-CR-92466 concerns verified LR beam-bandwidth/Doppler equations for mathematical-model use; not flight-error statistics.
- **ADJACENT EFFECTIVITY:** later LM10/R-567 material documents 15-bit raw interface architecture/conversions; complete Apollo 11 serial encoding is not inferred.
- **NOT CLAIMED:** sub-second dropout transition timing, random dropout probability, controller-visible symptom, complete LM-5 serial encoding/rounding/framing, or bit-for-bit radar-electronics equivalence.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective stochastic LR measurement-error distribution/process beyond the documented performance envelope and discrete flight events.
- **UNRESOLVED:** controller-visible radar/guidance cadence, synchronization, formatting, and symptoms of the documented tracking losses.

No station maturity grade changes.
