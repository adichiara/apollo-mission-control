# Progress — Apollo 11 landing-radar flown scaling boundary

Date: 2026-09-20

## Question

Can the unresolved Apollo-11 landing-radar quantization/bit-weighting thread be narrowed without back-projecting the later LM10 handbook?

## Primary evidence recovered

The flown LUMINARY 099 assembly listing provides Apollo-11-effective numerical scaling evidence directly:

- `ASSEMBLY_AND_OPERATION_INFORMATION.agc` identifies landing-radar altitude scale type `W` with a low-order bit weight of **1.079 ft**.
- The same flown listing identifies landing-radar velocity scale types `X/Y/Z` with low-order bit weights of **-0.6440, +1.212, and +0.8668 ft/s** respectively.
- `PINBALL_NOUN_TABLES.agc` contains the corresponding Apollo-11 constants for LR altitude and the three LR velocity components.
- `SERVICER.agc` independently comments the accepted/stored `HMEAS` altitude measurement as **1.079 ft/bit**.

This is stronger than the prior later-LM10 cross-check because the source is the Apollo 11 LUMINARY 099 listing assembled 14 July 1969.

## What this closes

Apollo 11 onboard converted/stored LR measurement resolution is now source-controlled for:

- low-scale altitude: 1.079 ft per low-order bit;
- velocity X: -0.6440 ft/s per low-order bit;
- velocity Y: +1.212 ft/s per low-order bit;
- velocity Z: +0.8668 ft/s per low-order bit.

The signs are part of the component conversion convention and must not be reinterpreted as error polarity.

## What remains unresolved

This evidence does **not** by itself establish the complete LM-5 radar-to-LGC serial transfer encoding. In particular, do not infer from these internal scale constants:

- serial word length;
- raw serial integer offset/bias;
- high-range altitude bit weight;
- rounding/truncation behavior in the radar electronics;
- transfer-bit order or electrical framing;
- a stochastic quantization-error distribution.

Later R-567 revisions describe a 15-bit raw-data representation and high/low range conversion, but remain later-effectivity evidence unless an Apollo-11-effective bridge is recovered. The later LM10 handbook likewise remains adjacent-effectivity for word length.

## Simulation consequence

A historical Apollo 11 model may now represent the documented **onboard converted measurement resolution** at the LUMINARY boundary. It should not claim bit-for-bit LM-5 serial-interface emulation or synthesize uniform quantization noise from this evidence alone.

Historical stochastic LR generation remains **BLOCKED** pending flight-effective residual/bias/correlation evidence. The serial-interface encoding thread is narrowed but not closed.

## Primary sources

- Apollo 11 LUMINARY 099, `ASSEMBLY_AND_OPERATION_INFORMATION.agc`, MIT Instrumentation Laboratory/NASA, assembled 14 Jul 1969.
- Apollo 11 LUMINARY 099, `PINBALL_NOUN_TABLES.agc`, MIT Instrumentation Laboratory/NASA.
- Apollo 11 LUMINARY 099, `SERVICER.agc`, MIT Instrumentation Laboratory/NASA.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** onboard converted/stored low-scale LR altitude and X/Y/Z velocity bit weights.
- **UNRESOLVED:** complete LM-5 raw serial encoding, high-range altitude conversion at the hardware interface, rounding/truncation, and serial framing.
- **BLOCKED:** historical stochastic LR error generation beyond documented performance envelopes and flight events.
