# Progress — Apollo 11 landing-radar output-interface boundary

Date: 2026-09-20

## Work completed

The next unresolved landing-radar item was checked against primary NASA Apollo experience evidence rather than using the later LM10 handbook to infer Apollo-11 quantization.

NASA TN D-6849 / MSC-S-311, *Apollo Experience Report: Lunar Module Landing Radar and Rendezvous Radar*, explicitly describes the landing-radar output architecture. LR velocity and slant-range information was processed and supplied to the LM guidance computer in **serial binary form**, while the same radar information was supplied to LM displays through **pulse trains and dc analog voltages**.

This is useful because it is mission-family hardware evidence tied by the same report to LM-5/Apollo 11 flight experience. It establishes that the LGC digital measurement path and the crew-display electrical path were distinct outputs of the radar subsystem. It therefore strengthens the interface model without importing the later LM10 15-bit word description into LM-5.

## What this does not establish

TN D-6849 does not, in the recovered passage, specify Apollo-11-effective serial word length, bit weighting, least-significant-bit size, transfer cadence, rounding/truncation behavior, or a stochastic error distribution. It also does not establish MCC/GUIDO display routing. No quantization constant is inferred.

The later LM10-and-subsequent handbook remains only an adjacent-effectivity cross-check for a 15-bit LR/LGC interface. Historical stochastic LR generation remains **BLOCKED** pending LM-5/Apollo-11-effective numerical residual/quantization evidence.

## Documentation synchronized

- focused landing-radar roadmap;
- station research status;
- Apollo 11 / Luminary 1A source catalog;
- this progress record.

## Evidence status

- **DOCUMENTED, APOLLO-PROGRAM HARDWARE / LM-5 EXPERIENCE SOURCE:** LR provides processed velocity/range to the LGC in serial binary form and separately to LM displays as pulse trains/dc analog voltages.
- **ADJACENT EFFECTIVITY ONLY:** LM10-and-subsequent handbook identifies 15-bit LR/LGC words.
- **UNRESOLVED:** LM-5 serial word length/bit weighting/quantization, transfer cadence, rounding behavior, and numerical residual process.
- **BLOCKED:** historical stochastic Apollo-11-effective LR measurement generation.

## Primary source

Rozas, M. F., and Cunningham, J. A., NASA TN D-6849 / MSC-S-311, *Apollo Experience Report: Lunar Module Landing Radar and Rendezvous Radar*, June 1972, NTRS 19720016521.