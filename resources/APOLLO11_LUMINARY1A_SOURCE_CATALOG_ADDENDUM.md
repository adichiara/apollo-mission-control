# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-19

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References `Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program`, Flight Software Branch, Flight Support Division, May 1969 | Primary mission-period evidence for the Luminary 1A equation document. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Complete re-issue of `69-FS-3` updated for Luminary 1B | Bibliographic/change-control evidence; not automatic Apollo 11 equation authority. |
| LUMINARY 099 `SERVICER.agc` | `SETPOS1` selects position-1 alpha/beta; `SETPOS2` selects position-2; `HIGATJOB` waits for physical position-2 success, recomputes beams, then enables LR reads. `SETPOS` transforms antenna UNITY/UNITX to NB and cross-products the third velocity beam. `RDGIMS` captures measurement epoch/CDUs/PIPAs; `VELUPDAT` applies measurement-time `*NBSM*`, propagation, qualification, and update. | Apollo-11-effective stage order, discrete antenna-position behavior, and transform-interface authority. Does not support a continuous slew model. |
| LUMINARY 099 `POWERED_FLIGHT_SUBROUTINES.agc` | `AX*SR*T` consumes sine/cosine state in Y-Z-X order; `-3` selects SM→NB and `+3` NB→SM; `*NBSM*` reuses prepared trig state | Apollo-11-effective transform contract. |
| MIT Apollo `Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc` | Primary predecessor `SMNB` rotates Y→Z→X; `NBSM` reverses X→Z→Y; `AXISROT` gives explicit arithmetic | Algorithmic lineage/sign oracle only; not Apollo-11 constant authority. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | `HBEAMANT = (-.4687018041, 0, -.1741224271)` | Apollo-11-effective fixed range-beam geometry. |
| LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969 | `LRALPHA/LRBETA` are antenna→NB rotations, beta then alpha, negatives of R-567 angles | Primary Apollo-11-period polarity/order authority. |
| `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load | Position-1/2 alpha/beta values plus `LRVMAX`, `LRVF`, `LRWV*`, `LRWVF*`, `LRWVFF` | Mission/configuration authority. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | Average-G/PIPA 2-second intervals; one LR velocity component per interval, cycling `Vz, Vx, Vy, Vz` | Onboard cadence only; not MCC display cadence. |
| NASA TN D-6849 | LM-5 bias correction and qualitative non-Gaussian/near-zero-Doppler error boundary | No numerical flight-effective stochastic distribution. |
| MIT/IL E-1982 | 1966 design-study statistical LR error/weighting assumptions | Design-history only. |

## Current result

`landing_radar_transform.py` provides equation-level SETPOS and SM/NB transforms. `landing_radar_velocity_chain.py` now composes them: callers may provide alpha/beta plus saved measurement-time CDU angles, select X/Y/Z, and continue through propagation, projection, qualification, and weighted correction. An explicit-beam path remains for synthetic/unit work.

No LM-5 load number is invented or silently embedded in this composition. A provenance-bearing profile adapter for the recovered position-1/position-2 load values is the next implementation step. Historical stochastic LR generation remains **BLOCKED**. Controller-visible cadence/formatting remains separate.

## Effectivity rule

Do not back-project Luminary 1B/1C or later behavior into Apollo 11 without controlled comparison. `Sunburst37` is used only as an algorithmic lineage/sign cross-check; Apollo-11-effective interfaces and constants remain controlled by LUMINARY 099, Memo #95, and LM-5 sources.

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

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** equation-level SETPOS + measurement-time NBSM velocity-beam path through the estimator.
- **DOCUMENTED:** discrete position-1/position-2 selection and recomputation behavior; LM-5 position-specific loads.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point equivalence.
- **DOCUMENTED:** one LR velocity component per 2-second Average-G/PIPA interval.
- **UNRESOLVED / BLOCKED:** numerical stochastic Apollo-11-effective LR error distribution.
- **UNRESOLVED:** controller-visible LR/guidance product cadence and formatting.
