# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-19

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References `Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program`, Flight Software Branch, Flight Support Division, May 1969 | Primary mission-period evidence that this Luminary 1A equation document was part of the Mission G technical source set. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Page-change record states that it is a **complete re-issue** of MSC Internal Note `69-FS-3`, *Programmed Guidance Equations for LUMINARY 1A Manned LM Earth Orbital and Lunar Program*, dated May 1969, updated for Luminary 1B | Primary bibliographic/change-control evidence identifying `69-FS-3`; `69-FS-4` is comparative evidence, not automatic Apollo 11 equation authority. |
| LUMINARY 099 final-program listing, `SERVICER.agc` | `SETPOS1`/`SETPOS2` select landing-radar position angles; `SETPOS` constructs antenna-to-navigation-base beam vectors; `LRVJOB` schedules `RDGIMS`; `RDGIMS` stores `LRVTIME`, IMU CDU angles, and PIPA snapshot; `VELUPDAT` restores those values, applies `*NBSM*`, advances the prior guidance velocity to the LR epoch using the saved PIPA increment and previous gravity contribution, subtracts lunar-rotation velocity, projects onto the selected beam, qualifies the residual, and `VUPDAT` applies the historical weighting/correction | Apollo-11-effective program authority for the executable measurement geometry, time-tag/propagation path, qualification, and velocity update. Transcription derives from the MIT Museum LMY99 hardcopy; preserve the distinction between original listing content and later transcription metadata. |
| LUMINARY 099 `POWERED_FLIGHT_SUBROUTINES.agc` | Defines `QUICTRIG`; states the CDU-angle order Y-Z-X; explicitly defines `*NBSM*` as the navigation-base-to-stable-member transformation using the already computed CDU sines/cosines | Apollo-11-effective authority for the dynamic frame-transform semantics used by `VELUPDAT`. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | Defines fixed `HBEAMANT` as the range beam in landing-radar antenna coordinates | Apollo-11-effective fixed program geometry; do not replace with an invented normalized vector. |
| LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969 | Clarifies that LGC `LRALPHA`/`LRBETA` are the negatives of the R-567 alpha/beta angles because the LGC performs antenna-to-navigation-base rotation; states beta/alpha usage order | Primary Apollo-11-period authority for transform polarity/order. |
| `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load | Supplies mission values for `LRALPHA1`, `LRBETA1`, `LRALPHA2`, `LRBETA2`; identifies stow and hover positions; supplies `LRVMAX`, `LRVF`, `LRWV*`, `LRWVF*`, and `LRWVFF` values | Mission/configuration authority for LM-5 landing-radar orientation and velocity-update inputs. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | Descent-state-vector material states that Average-G/PIPA processing occurs at 2-second intervals and that the three LR velocity components are used one per 2-second interval; the accompanying timeline shows the repeating velocity-component sequence `Vz, Vx, Vy, Vz` | Primary Apollo-11 training/technical evidence for the **onboard LR velocity-component update cadence**. This does not establish MCC display refresh, downlink freshness, controller-visible formatting, or a generic sensor/noise sample rate. |

## Current result

The landing-radar velocity estimator is now documented through the measurement-time propagation and downstream correction logic. `LRVJOB` schedules `RDGIMS` 170 ms after starting the five-sample velocity read; `RDGIMS` saves `TIME2,TIME1`, the three CDU angles, and PIPA values. `VELUPDAT` uses those saved values—not later current-time values—to reconstruct the LR measurement epoch.

The flown listing explicitly forms the measurement-time estimate as prior guidance velocity plus the PIPA-derived increment plus the previous gravity contribution over `LRVTIME - PIPTIME`, then subtracts the lunar-rotation velocity correction before projecting onto the measurement-time beam and testing the residual. This closes the earlier PIPA/gravity propagation research gap without inventing an independent gravity model.

The downstream velocity weighting/correction path is also controlled. LUMINARY 099 `VUPDAT` supplies the piecewise `LRVF/LRVMAX/LRW*` logic, update inhibit, P65/P66/P67 `LRWVFF` override, and weighted-residual vector correction; the LM-5 Mission G prelaunch erasable load supplies `LRVMAX=2000 ft/s`, `LRVF=200 ft/s`, `LRWVZ/Y/X=0.3`, `LRWVFZ/Y/X=0.2`, and `LRWVFF=0.1`. See research note 500.

The Apollo 11 AC Electronics manual now constrains one previously loose timing boundary: onboard descent-state-vector processing consumes one LR velocity component during each 2-second Average-G/PIPA interval, cycling the three components. A given component therefore recurs in the illustrated sequence after three such intervals. This is an LGC estimator/input cadence, not evidence for an MCC/controller product cadence.

The next bounded implementation target remains composition of the source-controlled propagation, beam transform, qualification, and weighting stages. Measurement/noise generation remains unresolved. For controller-visible timing, the new 2-second result may be used only as an upstream constraint; direct downlink/ground-display evidence is still required.

`69-FS-3` remains a preferred complete LUMINARY 1A equation source if recovered, especially for equation ancestry, descriptive cross-checks, and any dependency not directly closed by the flown listing/pad-load chain.

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

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static landing-radar antenna geometry and position transform.
- **DOCUMENTED:** measurement-time CDU/PIPA/time capture and NB-to-SM velocity-beam transform used by `VELUPDAT`.
- **DOCUMENTED:** Apollo-11-effective measurement-time velocity propagation through saved PIPA increment, previous gravity contribution, and lunar-rotation correction.
- **DOCUMENTED:** Apollo-11-effective residual qualification and downstream velocity weighting/correction logic and LM-5 weighting constants.
- **DOCUMENTED:** onboard LR velocity-component update cadence of one component per 2-second Average-G/PIPA interval; the source timeline cycles `Vz, Vx, Vy`.
- **PARTIALLY DOCUMENTED:** executable end-to-end composition of the controlled estimator stages.
- **UNRESOLVED:** landing-radar measurement error/noise generation.
- **UNRESOLVED:** controller-visible landing-radar/guidance product cadence and formatting; do not substitute the onboard 2-second component cadence for this separate ground-interface question.
