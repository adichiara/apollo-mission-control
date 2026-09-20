# Progress — Apollo 11 landing-radar digital-interface boundary

Date: 2026-09-20

## Question

Can the unresolved Apollo-11-effective LR quantization/error process be narrowed from primary or primary-contractor evidence without inventing a flight noise model?

## Research result

Two useful sources were identified, but neither closes the LM-5 stochastic-error question.

1. TRW report NASA-CR-92466 / TRW-11176-H059-R0-00, *Apollo Spacecraft Systems Analysis Program: Landing Radar Altimeter Beam Bandwidth and Doppler Equations for Mathematical Model Use* (25 Oct 1968), is a mission-period NASA contractor report. NTRS describes its lunar-reflectivity, acquisition-altitude, beam-bandwidth, and Doppler equations as verified for mathematical-model use. This makes it a strong target for physical/signal-model verification, not evidence for Apollo 11 flight residual statistics.
2. The later Grumman *Apollo Operations Handbook, Lunar Module LM10 and Subsequent*, LMA790-3-LM, documents selectable LR velocity/range quantities at the LGC radar interface and states that LR velocity/range data are supplied to the LGC as 15-bit binary words. Its effectivity is later than LM-5. It therefore corroborates digital-interface architecture but cannot set Apollo 11 bit weighting, quantization, cadence, or noise parameters.

## Decision

Historical stochastic LR generation remains **BLOCKED**. Do not derive a quantization step by dividing a performance range by 15 bits, and do not treat the later LM10 word format as Apollo-11-effective without an LM-5/effectivity bridge.

NASA-CR-92466 is added to the model-verification research path. Direct inspection should extract only supported beam/Doppler equations and assumptions. Any use as an Apollo 11 flight-error model requires separate LM-5 applicability evidence.

## Documentation synchronized

- focused Apollo 11 landing-radar roadmap;
- landing-radar station research status;
- Apollo 11 / Luminary 1A source catalog;
- this progress record.

## Next discriminating evidence

The highest-value unresolved targets remain: Apollo-11-effective FDS/RTCC/CCATS per-field routing for MSK-1137; LM-5 qualification/acceptance or Apollo 11 flight-data reduction containing actual LR residual/quantization/bias/correlation evidence; and direct retrieval of the F-mission test memorandum with an explicit LM-5 applicability bridge.

## Evidence status

- **DOCUMENTED, MISSION-PERIOD MODEL SOURCE:** NASA-CR-92466 exists and is specifically scoped to LR beam-bandwidth/Doppler mathematical-model verification.
- **ADJACENT EFFECTIVITY:** LM10-and-subsequent handbook documents selectable LR digital quantities and a 15-bit LR/LGC interface.
- **NOT ESTABLISHED:** Apollo-11-effective bit weighting, quantization step, stochastic distribution, correlation, bias process, or MCC display timing.
- **BLOCKED:** historical stochastic LR measurement generation pending flight-effective numerical evidence.
