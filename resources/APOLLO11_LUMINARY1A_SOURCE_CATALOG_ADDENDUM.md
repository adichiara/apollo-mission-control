# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-19

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References `Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program`, Flight Software Branch, Flight Support Division, May 1969 | Primary mission-period evidence that this Luminary 1A equation document was part of the Mission G technical source set. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Page-change record states that it is a **complete re-issue** of MSC Internal Note `69-FS-3`, *Programmed Guidance Equations for LUMINARY 1A Manned LM Earth Orbital and Lunar Program*, dated May 1969, updated for Luminary 1B | Primary bibliographic/change-control evidence identifying `69-FS-3`; `69-FS-4` is comparative evidence, not automatic Apollo 11 equation authority. |
| LUMINARY 099 final-program listing, `SERVICER.agc` | `SETPOS1`/`SETPOS2` select landing-radar position angles; `SETPOS` constructs antenna-to-navigation-base beam vectors; `LRVJOB` schedules `RDGIMS`; `RDGIMS` stores `LRVTIME`, IMU CDU angles, and PIPA snapshot; `VELUPDAT` restores the saved CDUs, calls `QUICTRIG`, and applies `*NBSM*` to the selected velocity beam | Apollo-11-effective program authority for the executable measurement geometry and time-tag path. Transcription derives from the MIT Museum LMY99 hardcopy; preserve the distinction between original listing content and later transcription metadata. |
| LUMINARY 099 `POWERED_FLIGHT_SUBROUTINES.agc` | Defines `QUICTRIG`; states the CDU-angle order Y-Z-X; explicitly defines `*NBSM*` as the navigation-base-to-stable-member transformation using the already computed CDU sines/cosines | Apollo-11-effective authority for the dynamic frame-transform semantics used by `VELUPDAT`. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | Defines fixed `HBEAMANT` as the range beam in landing-radar antenna coordinates | Apollo-11-effective fixed program geometry; do not replace with an invented normalized vector. |
| LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969 | Clarifies that LGC `LRALPHA`/`LRBETA` are the negatives of the R-567 alpha/beta angles because the LGC performs antenna-to-navigation-base rotation; states beta/alpha usage order | Primary Apollo-11-period authority for transform polarity/order. |
| `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load | Supplies mission values for `LRALPHA1`, `LRBETA1`, `LRALPHA2`, `LRBETA2`; identifies stow and hover positions | Mission/configuration authority for LM-5 landing-radar orientation inputs. |

## Current result

The landing-radar velocity-beam geometry is now documented through the measurement-time stable-member transform. `LRVJOB` schedules `RDGIMS` 170 ms after starting the five-sample velocity read; `RDGIMS` saves `TIME2,TIME1`, the three CDU angles, and PIPA values. `VELUPDAT` uses those saved CDUs—not a later current-attitude read—to transform the selected navigation-base velocity beam with `*NBSM*`.

The downstream **velocity weighting/correction path** is now also controlled. LUMINARY 099 `VUPDAT` supplies the piecewise `LRVF/LRVMAX/LRW*` logic, update inhibit, P65/P66/P67 `LRWVFF` override, and weighted-residual vector correction; the LM-5 Mission G prelaunch erasable load supplies `LRVMAX=2000 ft/s`, `LRVF=200 ft/s`, `LRWVZ/Y/X=0.3`, `LRWVFZ/Y/X=0.2`, and `LRWVFF=0.1`. See research note 500. The next bounded estimator target is the upstream PIPA/gravity propagation into the estimate at landing-radar measurement time and executable composition with the source-controlled beam transform.

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

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static landing-radar antenna geometry and position transform.
- **DOCUMENTED:** measurement-time CDU/time capture and NB-to-SM velocity-beam transform used by `VELUPDAT`.
- **DOCUMENTED:** Apollo-11-effective downstream velocity weighting/correction logic and LM-5 weighting constants.
- **PARTIALLY DOCUMENTED:** complete end-to-end measurement-time estimator composition, including PIPA/gravity propagation.
- **UNRESOLVED:** controller-visible product cadence and formatting.
