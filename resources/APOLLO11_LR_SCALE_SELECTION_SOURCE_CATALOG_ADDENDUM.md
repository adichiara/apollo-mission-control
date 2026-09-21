# Apollo 11 LR scale-selection source-catalog addendum

Date: 2026-09-20
Updated: 2026-09-21
Parent: `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| LUMINARY 099 `FLAGWORD_ASSIGNMENTS.agc` | `ALTSCALE` / `ALTSCBIT` identifies LR altitude scale state | Apollo-11-effective software state; not proof of controller visibility. |
| LUMINARY 099 `SERVICER.agc` | Tests `ALTSCBIT`; high-scale branch bypasses rescaling; low-scale path applies `SKALSKAL` | Apollo-11-effective estimator/interface logic. |
| LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc` | `SKALSKAL`: `LR ALT SCALE FACTOR RATIO: .2 NOM` | Apollo-11-effective software definition of nominal ratio. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` / assembly information | Low-scale LR altitude representation = 1.079 ft/count | Apollo-11-effective converted/stored scaling. Combined with Revision-99 `SFR = 5`, directly implies 5.395 ft/count high scale. |
| LUMINARY 099 `P20-P25.agc` | Flown radar lead-ins call `INITREAD`: `LRVELX` octal `14`, `LRVELY` `15`, `LRVELZ` `16`, `LRALT` `17`; `LRALT` is annotated one sample per reading | **Apollo-11-effective quantity-selection evidence.** Closes software-side LR read command mapping; does not define returned-data bit order, sign/bias, word length, or rounding. |
| MIT Instrumentation Laboratory LUMINARY Memo #85, *LUMINARY Revision 99*, 21 May 1969 | PCR 775 creates `RADSKAL` and `SKALSKAL`; `SFR = High Scale Factor / Low Scale Factor = 5`; `SKALSKAL = 1/SFR = 0.2` B-0. R12 Doppler compensation requires `RADSKAL` 1354–1355 = `00023,37462` and `SKALSKAL` 1356 = `06315`; radar-performed compensation requires all three registers zero. | Primary Revision-99 design evidence. Directly resolves the Apollo 11 zero mission load and establishes the 5:1 scale ratio. Does not prove controller visibility or raw serial encoding. |
| Apollo 11 LUMINARY 99 prelaunch erasable-load table, LM5/4.5.1-1 | `SKALSKAL` = `00000`; `RADSKAL` = `00000,00000` | Mission-specific load record. Read with Memo #85, selects radar-performed Doppler compensation; not a zero scale ratio. |
| MIT/IL, *LEM PGNCS Guidance System Operations Plan*, Section 3, LGC/LEM interface | LR inputs include `LR in "1" (Data Flow)` and `LR in "0" (Data Flow)` separately from range/velocity-good, antenna-position, and range-low-scale discretes | Primary Apollo-era interface evidence. Establishes two binary data-flow inputs and separation of data from status discretes; does not define bit order, sign/bias, word length, or rounding. |
| AC Electronics ND-1021042, *LEM Primary Guidance, Navigation, and Control System*, Table 1-III | LR-originated `Range low scale factor` discrete issued automatically at approximately 2,500 ft; `LR in "0"`/`LR in "1"` digital data pulses; LGC `Readout command`, continuous 3,200-cps `Gate reset`, and separate range/Vx/Vy/Vz strobes enabling LR transfer gates | Primary pre-mission interface evidence. Together with the GSOP, constrains framing architecture: binary data value is separate from LGC-controlled quantity selection/timing. Not LM-5 numeric bit encoding. |
| Grumman LMA790-3-LM, *Apollo Operations Handbook, Lunar Module, Subsystems Data*, LM-6, basic 15 Dec 1968 / change 15 Sep 1969 | At range PRF equivalent to 2,500 ft or less, altimeter mode changes and low-scale discrete is enabled; signal-data circuits convert/count radar data into 15-bit format and read shift-register data serially to LGC | Primary immediately post-Apollo-11 configuration evidence. Strong continuity; do not silently substitute LM-6 word length or raw encoding details for LM-5. |
| MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B* | `DNLRALT`: low scale 0.3288792 m = 1.0790 ft/count; high scale 1.64440 m = 5.3950 ft/count. `SKALSKAL` B0, unitless. | Primary MIT/MSC near-mission evidence. Independently corroborates the Apollo-11-effective 5.395-ft/count value derived from flown LUMINARY 099 low scale × Revision-99 ratio; it is not needed to back-project that value. |

## Controlled conclusion

LUMINARY Memo #85 closes the prior `SKALSKAL = 00000` ambiguity. Revision 99/PCR 775 deliberately allowed slant-range Doppler compensation either in R12 or in the landing radar. Nonzero `RADSKAL`/`SKALSKAL` values selected the R12 calculation; zeroing all three registers selected radar-performed compensation. The Apollo 11 prelaunch table contains exactly those zero values. Memo #85 also directly defines the Revision-99 high/low scale-factor ratio as 5 and its reciprocal `SKALSKAL` as 0.2. Therefore the zero mission load must not be interpreted as a zero physical altitude scale ratio.

The absolute high-scale conversion no longer needs an independent LM-5 quotation to be usable at the documented precision: flown LUMINARY 099 supplies 1.079 ft/count low scale and Revision-99 Memo #85 supplies the factor of 5, so high scale is 5.395 ft/count by direct arithmetic. The later Luminary 1B equations independently corroborate that result as 5.3950 ft/count. This is explicitly a derived Apollo-11-effective value, not evidence for otherwise unknown raw LR serial coding.

The GSOP plus ND-1021042 close one portion of the former generic `framing` question. The LR/LGC interface has two binary data-flow inputs and separate LGC readout/reset and quantity-specific range/Vx/Vy/Vz strobes. Flown LUMINARY 099 now closes the software side of quantity selection as octal `14/15/16/17` for Vx/Vy/Vz/range respectively. Data-bit value, quantity selection, and transfer timing must therefore remain distinct concepts in the simulator. The remaining raw-code questions are LM-5 word length, bit order, sign convention/integer bias, and rounding/truncation. The later LM-6 15-bit description remains corroborative only.

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
- LMA790-3-LM, LM-6 Apollo Operations Handbook, Subsystems Data (basic 15 Dec 1968; change 15 Sep 1969)
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** altitude scale-state branch, low-scale rescaling, and 1.079-ft/count low-scale representation.
- **DOCUMENTED, REVISION-99 PRIMARY:** high/low scale ratio 5; `SKALSKAL = 0.2`; R12-vs-radar Doppler compensation pad-load semantics.
- **DERIVED, APOLLO-11-EFFECTIVE:** 5.395-ft/count high scale from 1.079 × 5; independently corroborated by Luminary 1B's explicit 5.3950-ft/count value.
- **RESOLVED, APOLLO-11 MISSION LOAD:** zero `RADSKAL`/`SKALSKAL` selects radar-performed Doppler compensation.
- **DOCUMENTED, PRIMARY INTERFACE:** two binary LR data-flow inputs plus separate LGC readout/reset and range/Vx/Vy/Vz strobes constrain transfer framing architecture.
- **DOCUMENTED, APOLLO-11-EFFECTIVE QUANTITY SELECTION:** Vx/Vy/Vz/range read commands = octal `14/15/16/17` in flown LUMINARY 099.
- **ADJACENT EFFECTIVITY:** LM-6 explicitly documents 15-bit serial transfer; no LM-5 word length is inferred solely from it.
- **UNRESOLVED:** LM-5 raw word length, bit order, sign/bias, rounding/truncation, and controller-visible consequences.
