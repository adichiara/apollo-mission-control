# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-19

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References `Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program`, Flight Software Branch, Flight Support Division, May 1969 | Primary mission-period evidence that this Luminary 1A equation document was part of the Mission G technical source set. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Page-change record states that it is a complete re-issue of MSC Internal Note `69-FS-3`, dated May 1969, updated for Luminary 1B | Primary bibliographic/change-control evidence identifying `69-FS-3`; comparative evidence, not automatic Apollo 11 equation authority. |
| LUMINARY 099 final-program listing, `SERVICER.agc` | `SETPOS` constructs antenna-to-navigation-base velocity beams from antenna `UNITY`/`UNITX` and cross product; `RDGIMS` stores measurement time, IMU CDU angles, and PIPA snapshot; `VELUPDAT` restores them, applies `*NBSM*`, propagates velocity to the LR epoch, subtracts lunar-surface rotation, qualifies the residual, and `VUPDAT` applies weighting/correction | Apollo-11-effective program authority for stage ordering and estimator semantics. Repository composition now mirrors propagation through correction while keeping the measurement-time beam explicit until the AGC transform is independently ported/verified. |
| LUMINARY 099 `POWERED_FLIGHT_SUBROUTINES.agc` | Defines `QUICTRIG`, CDU-angle order Y-Z-X, `TRG*NBSM` / `*NBSM*`, and their use of `AX*SR*T` | Apollo-11-effective authority for dynamic frame-transform semantics; source-controlled but not yet an independently verified executable repository transform. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | Defines fixed `HBEAMANT = (-.4687018041, 0, -.1741224271)` in LR antenna coordinates | Apollo-11-effective fixed range-beam geometry; do not normalize or substitute an invented vector. |
| LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969 | States that LGC `LRALPHA`/`LRBETA` are antenna-to-navigation-base Euler rotations, used beta then alpha, and are negatives of the R-567 angles | Primary Apollo-11-period authority for transform polarity/order. |
| `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load | Supplies `LRALPHA1=0.0163371759 rev`, `LRBETA1=0.0665287037 rev`, `LRALPHA2=0.0161680555 rev`, `LRBETA2=0.0001361111 rev`, plus `LRVMAX`, `LRVF`, `LRWV*`, `LRWVF*`, and `LRWVFF` | Mission/configuration authority for LM-5 orientation and velocity-update inputs. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | Average-G/PIPA processing occurs at 2-second intervals and LR velocity components are used one per interval; timeline cycles `Vz, Vx, Vy, Vz` | Primary Apollo-11 technical evidence for onboard LR component cadence; not MCC display or generic sensor/noise cadence. |
| NASA TN D-6849, *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar* | LM-5 functional verification found a one-count velocity bias from a logic race and records its corrective logic alteration; says a Gaussian Doppler-spectrum-simulator test-limit assumption was corrected because the approximation produced heavier tails; Apollo 11 flight data were within specification limits except low/near-zero-Doppler points where tracking was not expected | Primary LM-5/Apollo-11 hardware-history boundary. It does not provide a numerical flight-effective stochastic distribution. |
| MIT/IL E-1982, *LEM PGNCS and Landing Radar Operations During the Powered Lunar Landing Maneuver* | 1966 design study analyzes random and bias sensor errors and statistical LR weighting | Primary design-history evidence only; do not promote its assumed simulation error model to Apollo-11-effective without later effectivity evidence. |

## Current result

The landing-radar velocity estimator is source-controlled through measurement-time propagation, beam projection, residual qualification, and downstream correction. Those arithmetic stages are now composed in `landing_radar_velocity_chain.py` when the selected measurement-time beam is supplied explicitly.

The remaining geometry implementation boundary is narrower and explicit: `SETPOS` antenna-to-NB plus measurement-time `*NBSM*` are documented in the flown listing and Memo #95, and the LM-5 load values are recovered, but the repository does not yet contain an independently verified executable port of the AGC `AX*SR*T` transform. Do not choose a modern Euler convention merely to remove that explicit input.

The AC Electronics manual constrains onboard processing to one LR velocity component per 2-second Average-G/PIPA interval. This is an LGC estimator/input cadence, not evidence for an MCC/controller cadence.

The stochastic-error search remains **BLOCKED**: recovered LM-5/Apollo-11 evidence does not provide a numerical flight-effective error distribution and does not justify an arbitrary Gaussian model. Synthetic perturbations may be used only when labeled synthetic.

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

- **DOCUMENTED:** Apollo-11-effective static antenna geometry/position-transform semantics and LM-5 orientation loads.
- **DOCUMENTED:** measurement-time CDU/PIPA/time capture, NB-to-SM transform semantics, velocity propagation, residual qualification, and downstream weighting/correction.
- **DOCUMENTED / IMPLEMENTED:** composed explicit-beam propagation → projection → qualification → weighted correction proof.
- **PARTIALLY IMPLEMENTED:** historical beam synthesis; AGC transform not yet independently ported/verified.
- **DOCUMENTED:** onboard LR velocity-component update cadence of one component per 2-second Average-G/PIPA interval.
- **PARTIALLY DOCUMENTED:** qualitative Apollo 11 LR error boundary near zero Doppler.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical stochastic landing-radar velocity-error distribution.
- **UNRESOLVED:** controller-visible landing-radar/guidance product cadence and formatting.
