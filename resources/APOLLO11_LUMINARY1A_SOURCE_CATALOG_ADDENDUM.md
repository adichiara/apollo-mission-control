# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-19

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References `Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program`, Flight Software Branch, Flight Support Division, May 1969 | Primary mission-period evidence that this Luminary 1A equation document was part of the Mission G technical source set. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Page-change record states that it is a **complete re-issue** of MSC Internal Note `69-FS-3`, *Programmed Guidance Equations for LUMINARY 1A Manned LM Earth Orbital and Lunar Program*, dated May 1969, updated for Luminary 1B | Primary bibliographic/change-control evidence identifying `69-FS-3`; `69-FS-4` is comparative evidence, not automatic Apollo 11 equation authority. |
| LUMINARY 099 final-program listing, `SERVICER.agc` | `SETPOS1`/`SETPOS2` select landing-radar position angles; `SETPOS` constructs antenna-to-navigation-base beam vectors; high-gate logic recomputes them after antenna repositioning; `RDGIMS` captures IMU CDU attitude data during velocity sampling | Apollo-11-effective program authority for the executable transform structure. Transcription derives from the MIT Museum LMY99 hardcopy; preserve the distinction between original listing content and later transcription metadata. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | Defines fixed `HBEAMANT` as the range beam in landing-radar antenna coordinates | Apollo-11-effective fixed program geometry; do not replace with an invented normalized vector. |
| LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969 | Clarifies that LGC `LRALPHA`/`LRBETA` are the negatives of the R-567 alpha/beta angles because the LGC performs antenna-to-navigation-base rotation; states beta/alpha usage order | Primary Apollo-11-period authority for transform polarity/order. |
| `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load | Supplies mission values for `LRALPHA1`, `LRBETA1`, `LRALPHA2`, `LRBETA2`; identifies stow and hover positions | Mission/configuration authority for LM-5 landing-radar orientation inputs. |

## Current retrieval target

The static antenna-position portion of the landing-radar beam transform is now documented by Apollo-11-effective sources; direct recovery of `69-FS-3` is no longer required merely to establish that transform.

The next bounded target is the **dynamic velocity-measurement attitude/reference-frame path**: trace the `RDGIMS` midpoint capture of `LRXCDU`, `LRYCDU`, `LRZCDU` through the transformation used by `VELUPDAT`, including time-tag semantics. After that, address the downstream estimator/filter and its cadence.

`69-FS-3` remains a preferred complete LUMINARY 1A equation source if recovered, especially for equation ancestry, descriptive cross-checks, and any dependency not directly closed by the flown listing/pad-load chain.

## Effectivity rule

Do not back-project `69-FS-4` (Luminary 1B), `70-FS-*`, R-567 Luminary 1C/1D/1E, or later terrain/radar changes into the Apollo 11 model without a controlled change comparison or independent Apollo 11-period corroboration.

## Sources

- https://ibiblio.org/apollo/Documents/Mission_G_Rendezvous.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/CONTROLLED_CONSTANTS.agc.html
- https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf

See research note `resources/research/405_apollo11_landing_radar_beam_transform.md`.
