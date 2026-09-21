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
| MIT/IL, *LEM PGNCS Guidance System Operations Plan*, Section 3 | `LR in "1"` / `LR in "0"` data flow separate from LR status discretes | Primary interface evidence. |
| AC Electronics ND-1021042, *LEM Primary Guidance, Navigation, and Control System* | LR digital pulses; LGC readout/reset and range/Vx/Vy/Vz selection; radar control stops sync and requests `RUPT9` after **15 received radar pulses** | Primary interface mechanism and independent 15-pulse corroboration. |
| Apollo 11 engineering note, LGC 520 alarm on DSKY-CB closure | Radar-read sequence = 80-ms gate, 5-ms delay, **15 readout pulses at 3200 pps**, then radar interrupt | **Mission-specific Apollo 11 word-length bridge.** |
| MIT/MSC R-700, Volume II | Radar shift-register contents transfer serially; `1` bits on ones bus, `0` bits on zeros bus; **most significant bit read first** | Primary Apollo interface evidence closing serial bit order; does not define signed-velocity numerical representation or conversion rounding. |
| MIT/IL guidance-and-navigation functional description, §2.5.2.1.5 | SDC uses 15-bit counter and 15-bit shift register; range/velocity word shifts **MSB first** on two lines | Independent primary corroboration of MSB-first/two-line transfer. |
| NASA TN D-6849, *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar* | Velocity sign determined from pulse trains before SDC; SDC serializes velocity/range for LGC | Establishes upstream sign determination, not serial signed-number representation. |
| Grumman LMA790-3-LM, LM-6 *Apollo Operations Handbook* | Signal-data circuits convert/count radar data into 15-bit format and read serially to LGC | Adjacent-effectivity corroboration only. |
| MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B* | LR altitude low/high scale 1.0790/5.3950 ft/count | Near-mission corroboration of Apollo-11-effective derived high scale. |

## Controlled conclusion

Revision-99 Memo #85 plus the Apollo 11 mission load resolve the `SKALSKAL` zero semantics: Apollo 11 selected radar-performed slant-range Doppler compensation. Flown LUMINARY 099 low scale × the Revision-99 factor of five gives 5.395 ft/count high scale.

The raw interface is now constrained further. Apollo-11-specific evidence establishes 15 readout pulses; R-700 Volume II establishes **MSB-first** serialization and complementary ones/zeros buses, independently corroborated by the MIT/IL functional description. NASA TN D-6849 places velocity-sign determination upstream of serialization.

Remaining raw-code questions are **signed-velocity numerical representation/integer bias and rounding/truncation**. Neither is inferred from word length, bit order, or the existence of complementary data lines.

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
- https://www.ibiblio.org/apollo/Documents/R-700-Volume-2.pdf
- https://www.ibiblio.org/apollo/Documents/sundance_functional_description_vol1.pdf
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- LMA790-3-LM, LM-6 Apollo Operations Handbook, Subsystems Data (basic 15 Dec 1968; change 15 Sep 1969)
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** altitude scale-state logic, 1.079-ft/count low scale, and flown quantity selection.
- **DOCUMENTED, REVISION-99 PRIMARY:** high/low ratio 5; `SKALSKAL=0.2`; compensation-load semantics.
- **DERIVED, APOLLO-11-EFFECTIVE:** 5.395-ft/count high scale.
- **RESOLVED, APOLLO-11 MISSION LOAD:** zero `RADSKAL`/`SKALSKAL` selects radar-performed compensation.
- **DOCUMENTED, APOLLO-11-SPECIFIC RAW WORD LENGTH:** 15 readout pulses/bits.
- **DOCUMENTED, PRIMARY APOLLO INTERFACE:** MSB-first serial transfer on complementary ones/zeros data lines; velocity sign exists before serialization.
- **UNRESOLVED:** signed-velocity representation/integer bias, rounding/truncation, and controller-visible consequences.
