# Station research status — Apollo 11 LR scale selection

Date: 2026-09-20
Updated: 2026-09-21
Parent: `docs/station-status/2026-09-19_apollo11_landing_radar_beam_transform.md`

## GUIDO / guidance-monitoring consequence

Flown LUMINARY 099 establishes that the onboard landing-radar altitude path explicitly tracked high/low scale state and conditionally rescaled the low-scale path before altitude residual/update logic. The Apollo 11 LUMINARY 99 prelaunch pad-load table records `SKALSKAL` at erasable address 1356 as octal `00000`; `RADSKAL` occupies 1354–1355 and is also zero. Earlier repository references to 3461/3462 and `RADSCALE` were transcription errors and have been corrected.

MIT Instrumentation Laboratory LUMINARY Memo #85 (21 May 1969) resolves the zero-load semantics for Revision 99 / PCR 775. It defines `SFR = High Scale Factor / Low Scale Factor = 5` and `SKALSKAL = 1/SFR = 0.2`. R12 slant-range Doppler compensation uses nonzero `RADSKAL`/`SKALSKAL`; radar-performed compensation sets all three registers to zero. Apollo 11's mission load therefore selects radar-performed compensation, not a zero physical scale ratio.

Flown LUMINARY 099 supplies 1.079 ft/count low scale and Memo #85 supplies the factor of 5, directly deriving 5.395 ft/count high scale. MSC-69-FS-4 independently corroborates 5.3950 ft/count.

The MIT/IL *LEM PGNCS Guidance System Operations Plan*, Section 3, identifies `LR in "1"` and `LR in "0"` binary data-flow inputs separately from LR validity, antenna-position, and range-low-scale discretes. AC Electronics ND-1021042 identifies complementary LGC readout/reset and quantity-selection behavior. NASA's *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar* states that velocity sign is determined in the measurement pulse-train path before the Signal Data Converter assembles serial binary output.

A mission-specific Apollo 11 engineering note on the LGC 520 alarm closes raw transfer length: an 80-ms gate, a 5-ms delay, **15 readout pulses at 3200 pps**, then radar interrupt. ND-1021042 independently terminates sync and requests `RUPT9` after 15 received radar pulses. MIT/MSC R-700 Volume II now closes serial bit order: the radar shift-register contents are read out **most-significant-bit first**, with `1` bits on the ones bus and `0` bits on the zeros bus. An MIT/IL functional description independently describes the resulting 15-bit range/velocity word as MSB-first on two lines. This does not establish signed-velocity numerical representation/integer bias or Signal Data Converter rounding/truncation.

Flown LUMINARY 099 also closes software-side quantity selection. `P20-P25.agc` invokes `INITREAD` with octal `14` for `LRVELX`, `15` for `LRVELY`, `16` for `LRVELZ`, and `17` for `LRALT`. These are read-selection commands, not returned-data encoding.

No recovered source establishes that `ALTSCBIT`, raw scale state, PCR-775 compensation selection, transfer encoding, or rescaling was exposed directly to GUIDO, CONTROL, or FLIGHT. No station display, alarm, callout, or procedure is added from this evidence.

## Player-facing boundary

A spacecraft model may preserve LR altitude scale state internally; use 1.079 ft/count low scale and derived 5.395 ft/count high scale; encode the mission load as radar-performed slant-range Doppler compensation; preserve the flown quantity-selection mapping (`Vx/Vy/Vz/range` = octal `14/15/16/17`); preserve that velocity sign is determined before Signal Data Converter serialization; and model the Apollo 11 LR/LGC transfer as a 15-bit serial readout, **MSB first**, over complementary ones/zeros data lines. Do not invent signed-velocity representation/integer bias, rounding/truncation, controller-visible controls, or an exact invariant 2,500-ft switching altitude.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** `ALTSCBIT` selects high/low LR altitude treatment; low scale invokes `SKALSKAL` rescaling.
- **DOCUMENTED, APOLLO-11-EFFECTIVE LOW SCALE:** 1.079 ft/count stored representation.
- **DOCUMENTED, REVISION-99 PRIMARY:** high/low ratio 5, `SKALSKAL = 0.2`, and PCR-775 compensation-selection pad semantics.
- **DERIVED, APOLLO-11-EFFECTIVE HIGH SCALE:** 5.395 ft/count = 1.079 × 5; independently corroborated by Luminary 1B.
- **RESOLVED, APOLLO-11 PRELAUNCH LOAD:** zero `RADSKAL`/`SKALSKAL` selects radar-performed Doppler compensation.
- **DOCUMENTED, APOLLO-11-SPECIFIC RAW TRANSFER LENGTH:** 15 readout pulses at 3200 pps followed by radar interrupt; corroborated by ND-1021042's 15-pulse radar-control description.
- **DOCUMENTED, PRIMARY APOLLO INTERFACE:** MSB-first serial binary transfer on complementary ones/zeros lines; separate readout/reset/quantity selection; upstream velocity-sign determination.
- **DOCUMENTED, APOLLO-11-EFFECTIVE QUANTITY SELECTION:** `LRVELX=14`, `LRVELY=15`, `LRVELZ=16`, `LRALT=17` (octal).
- **NO STATION MATURITY CHANGE:** controller visibility/routing remains unestablished.
- **UNRESOLVED:** signed-velocity representation/integer bias, rounding/truncation, and controller-visible compensation/scale-state consequences.
