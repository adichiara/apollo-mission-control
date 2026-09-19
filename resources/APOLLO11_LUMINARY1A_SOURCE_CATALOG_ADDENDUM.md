# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-19

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References `Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program`, Flight Software Branch, Flight Support Division, May 1969 | Primary mission-period evidence that this Luminary 1A equation document was part of the Mission G technical source set. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Page-change record states that it is a **complete re-issue** of MSC Internal Note `69-FS-3`, *Programmed Guidance Equations for LUMINARY 1A Manned LM Earth Orbital and Lunar Program*, dated May 1969, updated for Luminary 1B | Primary bibliographic/change-control evidence identifying `69-FS-3`; `69-FS-4` is comparative evidence, not automatic Apollo 11 equation authority. |
| LUMINARY 099 final-program listing, `SERVICER.agc` | `SETPOS` constructs antenna-to-navigation-base beam vectors; `RDGIMS` stores measurement time, IMU CDU angles, and PIPA snapshot; `VELUPDAT` restores them, applies `*NBSM*`, propagates velocity to the LR epoch, subtracts lunar-rotation velocity, qualifies the residual, and `VUPDAT` applies weighting/correction | Apollo-11-effective program authority for executable measurement geometry, time-tag/propagation, qualification, and velocity update. |
| LUMINARY 099 `POWERED_FLIGHT_SUBROUTINES.agc` | Defines `QUICTRIG`, CDU-angle order Y-Z-X, and `*NBSM*` as navigation-base-to-stable-member transformation | Apollo-11-effective authority for dynamic frame-transform semantics. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | Defines fixed `HBEAMANT` | Apollo-11-effective fixed program geometry. |
| LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969 | Clarifies LGC `LRALPHA`/`LRBETA` polarity and beta/alpha usage order | Primary Apollo-11-period authority for transform polarity/order. |
| `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load | Supplies mission `LRALPHA*`, `LRBETA*`, `LRVMAX`, `LRVF`, `LRWV*`, `LRWVF*`, and `LRWVFF` values | Mission/configuration authority for LM-5 orientation and velocity-update inputs. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | Average-G/PIPA processing occurs at 2-second intervals and LR velocity components are used one per interval; timeline cycles `Vz, Vx, Vy, Vz` | Primary Apollo-11 technical evidence for onboard LR component cadence; not MCC display or generic sensor/noise cadence. |
| NASA TN D-6849, *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar* | LM-5 functional verification found a one-count velocity bias from a logic race and records its corrective logic alteration; says a Gaussian Doppler-spectrum-simulator test-limit assumption was corrected because the approximation produced heavier tails; Apollo 11 flight data were within specification limits except low/near-zero-Doppler points where tracking was not expected | Primary LM-5/Apollo-11 hardware-history boundary. It does **not** provide a numerical flight-effective stochastic distribution; do not turn the preflight bias into a flown defect or use an arbitrary Gaussian noise model. |
| MIT/IL E-1982, *LEM PGNCS and Landing Radar Operations During the Powered Lunar Landing Maneuver* | 1966 design study explicitly analyzes random and bias sensor errors and statistical LR weighting | Primary design-history evidence only. Do not promote its assumed simulation error model to Apollo-11-effective without later effectivity evidence. |

## Current result

The landing-radar velocity estimator is documented through measurement-time propagation and downstream correction logic. The flown listing reconstructs the LR measurement epoch and forms the measurement-time velocity estimate from prior guidance velocity, PIPA-derived increment, previous gravity contribution, and lunar-rotation correction. `VUPDAT` supplies the piecewise weighting/correction logic; the LM-5 load supplies Apollo-11-effective thresholds and weights. See research note 500.

The AC Electronics manual constrains onboard processing to one LR velocity component per 2-second Average-G/PIPA interval. This is an LGC estimator/input cadence, not evidence for an MCC/controller cadence.

The stochastic-error search is now **BLOCKED**: LM-5/Apollo-11 primary evidence constrains known preflight and near-zero-Doppler behavior, and specifically warns against an unqualified Gaussian assumption, but the recovered sources do not provide a numerical flight-effective error distribution. Synthetic perturbations may be used only when labeled synthetic.

The next bounded implementation target is composition of the source-controlled propagation, beam transform, qualification, and weighting stages. Controller-visible timing remains a separate evidence problem.

`69-FS-3` remains a preferred complete LUMINARY 1A equation source if recovered, especially for equation ancestry, descriptive cross-checks, and dependencies not directly closed by the flown listing/pad-load chain.

## Effectivity rule

Do not back-project `69-FS-4` (Luminary 1B), `70-FS-*`, R-567 Luminary 1C/1D/1E, or later terrain/radar changes into the Apollo 11 model without a controlled change comparison or independent Apollo 11-period corroboration.

## Sources

- https://ibiblio.org/apollo/Documents/Mission_G_Rendezvous.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/CONTROLLED_CONSTANTS.agc.html
- https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- https://www.ibiblio.org/apollo/Documents/E-1982_LEM_PGNCS_and_Landing_Radar_Operations.pdf

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static landing-radar antenna geometry and position transform.
- **DOCUMENTED:** measurement-time CDU/PIPA/time capture, velocity propagation, residual qualification, and downstream weighting/correction.
- **DOCUMENTED:** onboard LR velocity-component update cadence of one component per 2-second Average-G/PIPA interval.
- **DOCUMENTED:** LM-5 preflight one-count velocity bias was corrected; the cited Gaussian simulator test-limit assumption required correction for heavier tails.
- **PARTIALLY DOCUMENTED:** qualitative Apollo 11 LR error boundary near zero Doppler.
- **PARTIALLY DOCUMENTED:** executable end-to-end composition of the controlled estimator stages.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical stochastic landing-radar velocity-error distribution.
- **UNRESOLVED:** controller-visible landing-radar/guidance product cadence and formatting.
