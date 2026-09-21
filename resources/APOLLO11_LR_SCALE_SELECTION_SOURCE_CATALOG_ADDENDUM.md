# Apollo 11 LR scale-selection source-catalog addendum

Date: 2026-09-20
Updated: 2026-09-21
Parent: `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| LUMINARY 099 `FLAGWORD_ASSIGNMENTS.agc` | `ALTSCALE` / `ALTSCBIT` identifies LR altitude scale state | Apollo-11-effective software state; not proof of controller visibility. |
| LUMINARY 099 `SERVICER.agc` | Tests `ALTSCBIT`; high-scale branch bypasses rescaling; low-scale path applies `SKALSKAL` | Apollo-11-effective estimator/interface logic. |
| LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc` | `SKALSKAL`: `LR ALT SCALE FACTOR RATIO: .2 NOM` | Apollo-11-effective software definition. |
| LUMINARY 099 controlled constants / assembly information | Low-scale LR altitude representation = 1.079 ft/count | With Revision-99 `SFR = 5`, implies 5.395 ft/count high scale. |
| LUMINARY 099 `P20-P25.agc` | `INITREAD`: Vx/Vy/Vz/range = octal `14/15/16/17` | Apollo-11-effective quantity selection; not returned-data encoding. |
| MIT/IL LUMINARY Memo #85, *LUMINARY Revision 99*, 21 May 1969 | PCR 775; `SFR=5`; `SKALSKAL=0.2`; nonzero R12-compensation loads vs all-zero radar-compensation loads | Resolves Apollo 11 zero mission load and scale ratio. |
| Apollo 11 LUMINARY 99 prelaunch erasable-load table, LM5/4.5.1-1 | `SKALSKAL=00000`; `RADSKAL=00000,00000` | Mission-specific load; selects radar-performed compensation when read with Memo #85. |
| MIT/IL, *LEM PGNCS Guidance System Operations Plan*, Section 3 | `LR in "1"` / `LR in "0"` data flow separate from LR status discretes | Primary interface evidence; does not by itself define bit order/sign/bias/rounding. |
| AC Electronics ND-1021042, *LEM Primary Guidance, Navigation, and Control System* | LR digital pulses; LGC readout/reset and range/Vx/Vy/Vz selection; radar control stops sync and requests `RUPT9` after **15 received radar pulses** | Primary interface mechanism and independent 15-pulse corroboration. |
| Apollo 11 engineering note, LGC 520 alarm on DSKY-CB closure | Radar-read sequence = 80-ms gate, 5-ms delay, **15 readout pulses at 3200 pps**, then radar interrupt; explains `SAMPLIN` handling | **Mission-specific Apollo 11 word-length bridge.** Establishes 15-pulse raw radar readout for Apollo 11; does not establish bit order/sign/bias/rounding. |
| NASA TN D-6849, *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar* | Velocity sign determined from pulse trains before SDC; SDC serializes velocity/range for LGC | Establishes upstream sign determination, not serial sign representation. |
| Grumman LMA790-3-LM, LM-6 *Apollo Operations Handbook* | Signal-data circuits convert/count radar data into 15-bit format and read serially to LGC | Adjacent-effectivity corroboration only; no longer needed as sole basis for Apollo 11 word length. |
| MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B* | LR altitude low/high scale 1.0790/5.3950 ft/count | Near-mission corroboration of Apollo-11-effective derived high scale. |

## Controlled conclusion

Revision-99 Memo #85 plus the Apollo 11 mission load resolve the `SKALSKAL` zero semantics: Apollo 11 selected radar-performed slant-range Doppler compensation. Flown LUMINARY 099 low scale × the Revision-99 factor of five gives 5.395 ft/count high scale.

The interface chain is now constrained further. GSOP/ND-1021042 separate binary data value from LGC-controlled transfer/selection; LUMINARY 099 supplies the flown quantity-select commands; NASA TN D-6849 places velocity-sign determination upstream of serialization. Most importantly, the mission-specific Apollo 11 520-alarm engineering note describes **15 readout pulses at 3200 pps followed by radar interrupt**, while ND-1021042 independently terminates radar sync after 15 received pulses. The Apollo 11 raw LR/LGC transfer length can therefore be treated as 15 bits/pulses rather than adjacent-effectivity inference.

Remaining raw-code questions are **serial bit order, sign representation/integer bias, and rounding/truncation**. These must not be inferred from the 15-pulse result.

## Sources

- https://www.ibiblio.org/apollo/listings/Luminary099/FLAGWORD_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/CONTROLLED_CONSTANTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/P20-P25.agc.html
- https://www.ibiblio.org/apollo/Documents/LUM85_text.pdf
- https://www.ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://www.ibiblio.org/apollo/Documents/as278_gsop_section3_lm.pdf
- https://www.ibiblio.org/apollo/Documents/apollolunarexcuracel_0.pdf
- https://www.ibiblio.org/apollo/Documents/apollo_11_520_alarm.pdf
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- LMA790-3-LM, LM-6 Apollo Operations Handbook, Subsystems Data (basic 15 Dec 1968; change 15 Sep 1969)
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** altitude scale-state logic, 1.079-ft/count low scale, and flown quantity selection.
- **DOCUMENTED, REVISION-99 PRIMARY:** high/low ratio 5; `SKALSKAL=0.2`; compensation-load semantics.
- **DERIVED, APOLLO-11-EFFECTIVE:** 5.395-ft/count high scale.
- **RESOLVED, APOLLO-11 MISSION LOAD:** zero `RADSKAL`/`SKALSKAL` selects radar-performed compensation.
- **DOCUMENTED, APOLLO-11-SPECIFIC RAW WORD LENGTH:** 15 readout pulses/bits.
- **DOCUMENTED, PRIMARY INTERFACE:** binary data and transfer/selection are distinct; velocity sign exists before serialization.
- **UNRESOLVED:** serial bit order, sign representation/bias, rounding/truncation, and controller-visible consequences.
