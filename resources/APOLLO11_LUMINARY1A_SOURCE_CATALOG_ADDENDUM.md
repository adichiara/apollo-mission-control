# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-19

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References `Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program`, Flight Software Branch, Flight Support Division, May 1969 | Primary mission-period evidence for the Luminary 1A equation document. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Complete re-issue of `69-FS-3` updated for Luminary 1B | Bibliographic/change-control evidence; not automatic Apollo 11 equation authority. |
| LUMINARY 099 `SERVICER.agc` | `SETPOS` places beta/Y, zero/Z, alpha/X; constructs antenna→NB beams; `RDGIMS` captures measurement epoch/CDUs/PIPAs; `VELUPDAT` applies measurement-time `*NBSM*`, propagation, qualification, and update | Apollo-11-effective stage-order and transform-interface authority. |
| LUMINARY 099 `POWERED_FLIGHT_SUBROUTINES.agc` | `AX*SR*T` consumes sine/cosine state in Y-Z-X order; `-3` selects SM→NB and `+3` NB→SM; `*NBSM*` reuses prepared trig state; `FLESHPOT` independently constructs the CDU transformation matrix | Apollo-11-effective transform contract and in-program matrix cross-check. |
| MIT Apollo `Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc` | Earlier primary `SMNB` performs Y→Z→X axis rotations; `NBSM` reverses them X→Z→Y; `AXISROT` changes arithmetic sense under `NBSMBIT` | Independent primary-software corroboration only; not Apollo-11 effectivity authority for constants. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | `HBEAMANT = (-.4687018041, 0, -.1741224271)` | Apollo-11-effective fixed range-beam geometry. |
| LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969 | `LRALPHA/LRBETA` are antenna→NB rotations, beta then alpha, negatives of R-567 angles | Primary Apollo-11-period polarity/order authority. |
| `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load | Position-1/2 alpha/beta values plus `LRVMAX`, `LRVF`, `LRWV*`, `LRWVF*`, `LRWVFF` | Mission/configuration authority. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | Average-G/PIPA 2-second intervals; one LR velocity component per interval, cycling `Vz, Vx, Vy, Vz` | Onboard cadence only; not MCC display cadence. |
| NASA TN D-6849 | LM-5 bias correction and qualitative non-Gaussian/near-zero-Doppler error boundary | No numerical flight-effective stochastic distribution. |
| MIT/IL E-1982 | 1966 design-study statistical LR error/weighting assumptions | Design-history only. |

## Current result

The estimator arithmetic is executable through propagation → explicit-beam projection → qualification → weighted correction. The current verification pass independently closes the former transform-convention ambiguity: flown LUMINARY 099, predecessor primary Apollo software, Memo #95, and the LUMINARY 099 matrix construction agree on controlled axis ordering/direction semantics.

The remaining geometry implementation gate is numerical equivalence between a modern floating-point implementation and original AGC transform behavior. Do not choose a library Euler convention by name alone.

Historical stochastic LR generation remains **BLOCKED**. Controller-visible cadence/formatting remains separate.

## Effectivity rule

Do not back-project Luminary 1B/1C or later behavior into Apollo 11 without controlled comparison. `Sunburst37` is used only as an algorithmic lineage cross-check; Apollo-11-effective behavior remains controlled by LUMINARY 099 and LM-5 sources.

## Sources

- https://ibiblio.org/apollo/Documents/Mission_G_Rendezvous.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc.html
- https://www.ibiblio.org/apollo/listings/Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/CONTROLLED_CONSTANTS.agc.html
- https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- https://www.ibiblio.org/apollo/Documents/E-1982_LEM_PGNCS_and_Landing_Radar_Operations.pdf

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static geometry, angle placement, Y-Z-X order, transform direction, propagation, qualification, and weighting/correction.
- **CORROBORATED:** transform sequence from independent primary Apollo software and LUMINARY 099 matrix construction.
- **DOCUMENTED / IMPLEMENTED:** composed explicit-beam estimator proof.
- **PARTIALLY IMPLEMENTED:** historical beam synthesis; numerical-equivalence fixture remains.
- **DOCUMENTED:** one LR velocity component per 2-second Average-G/PIPA interval.
- **UNRESOLVED / BLOCKED:** numerical stochastic Apollo-11-effective LR error distribution.
- **UNRESOLVED:** controller-visible LR/guidance product cadence and formatting.