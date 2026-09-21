# Apollo 11 LR scale-selection source-catalog addendum

Date: 2026-09-20
Updated: 2026-09-21
Parent: `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| LUMINARY 099 `FLAGWORD_ASSIGNMENTS.agc` | `ALTSCALE` / `ALTSCBIT` identifies LR altitude scale state | Apollo-11-effective software state; not proof of controller visibility. |
| LUMINARY 099 `SERVICER.agc` | Tests `ALTSCBIT`; high-scale branch bypasses rescaling; low-scale path applies `SKALSKAL` | Apollo-11-effective estimator/interface logic. |
| LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc` | `SKALSKAL`: `LR ALT SCALE FACTOR RATIO: .2 NOM` | Apollo-11-effective software definition. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | Low-scale altitude = 1.079 ft/count; `LVELBIAS=-12288`, `LANDING RADAR BIAS FOR 153.6 KC.`; Vx/Vy/Vz component scales | Apollo-11-effective altitude conversion and raw velocity-bias constant. |
| LUMINARY 099 `P20-P25.agc` | `INITREAD`: Vx/Vy/Vz/range = octal `14/15/16/17`; velocity path masks `RNRAD` with `POSMAX` then adds `LVELBIAS` | Apollo-11-effective quantity selection and proof that raw velocity is count-biased at the LGC boundary. |
| MIT/IL LUMINARY Memo #85, *LUMINARY Revision 99*, 21 May 1969 | PCR 775; `SFR=5`; `SKALSKAL=0.2`; nonzero R12-compensation loads vs all-zero radar-compensation loads | Resolves Apollo 11 zero mission load and scale ratio. |
| Apollo 11 LUMINARY 99 prelaunch erasable-load table, LM5/4.5.1-1 | `SKALSKAL=00000`; `RADSKAL=00000,00000` | Mission-specific load; selects radar-performed compensation when read with Memo #85. |
| MIT/IL, *LEM PGNCS Guidance System Operations Plan*, Section 3 | `LR in "1"` / `LR in "0"` data flow separate from LR status discretes | Primary interface evidence. |
| AC Electronics ND-1021042, *LEM Primary Guidance, Navigation, and Control System* | LR digital pulses; LGC readout/reset and range/Vx/Vy/Vz selection; radar control stops sync and requests `RUPT9` after **15 received radar pulses** | Primary interface mechanism and independent 15-pulse corroboration. |
| Apollo 11 engineering note, LGC 520 alarm on DSKY-CB closure | Radar-read sequence = 80-ms gate, 5-ms delay, **15 readout pulses at 3200 pps**, then radar interrupt | **Mission-specific Apollo 11 word-length bridge.** |
| MIT/MSC R-700, Volume II, §5.4.5 | Selected radar measurement gate feeds a binary high-speed counter; counter accumulates the gated measurement and serially transfers the count; MSB first on complementary data lines | Primary hardware basis for integer gated-pulse model; does not specify sub-edge race behavior. |
| MIT/IL E-1982, *LEM PGNCS and Landing Radar Operations* | Selected LR velocity frequency accumulates in radar high-speed counter for an **80-ms count interval controlled by the LGC** | Primary independent evidence that measurement formation is pulse accumulation, not a documented arithmetic rounding operation. |
| MIT/IL HSI-208625, digital simulator description | LR self-test Vx/Vy/Vz/range values are specified as counts accumulated over an **80-ms sample period** | Primary functional corroboration of count-domain interface semantics; simulator document is not used to invent analog error statistics. |
| MIT/IL guidance-and-navigation functional description, §2.5.2.1.5 | SDC uses 15-bit counter and 15-bit shift register; range/velocity word shifts **MSB first** on two lines | Independent primary corroboration of MSB-first/two-line transfer. |
| NASA TN D-6849, *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar* | Velocity pulse train superimposed on 153.6-kHz reference to facilitate sign determination; SDC serializes velocity/range | Hardware explanation consistent with the flown `LVELBIAS` offset. |
| AC Electronics, *Apollo 11 Manual*, MSK-1137 definition | `LR RNG` and `VEL` status = `GOOD/BAD`; `VXB/VYB/VZB` = LR velocity in body axes; `RNG` = LR slant-range altitude | **Mission-specific controller-display evidence.** Establishes processed LR status/value visibility; does not establish raw downlink provenance and contains no PCR-775/scale-state field. |
| MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B* | LR altitude low/high scale 1.0790/5.3950 ft/count; DNLRVEL bias added with `K:LVELBIAS=-12288` | Near-mission primary corroboration of both derived altitude high scale and flown-code velocity-bias interpretation. |
| Grumman LMA790-3-LM, LM-6 *Apollo Operations Handbook* | Signal-data circuits count selected velocity PRF for 80 ms and serialize 15-bit words | Adjacent-effectivity corroboration only. |

## Controlled conclusion

Revision-99 Memo #85 plus the Apollo 11 mission load resolve the `SKALSKAL` zero semantics: Apollo 11 selected radar-performed slant-range Doppler compensation. Flown LUMINARY 099 low scale × the Revision-99 factor of five gives 5.395 ft/count high scale.

The raw interface is constrained to a 15-bit, MSB-first serial transfer on complementary ones/zeros lines. Flown LUMINARY 099 further establishes the velocity numerical convention at the LGC boundary: the raw velocity count is masked as nonnegative and corrected by `LVELBIAS=-12288`. Signed velocity is therefore recovered from a 12,288-count offset representation rather than a serial sign bit/complement number. NASA's 153.6-kHz sign-reference description and MSC-69-FS-4 independently support this interpretation.

The former `SDC rounding/truncation` question should not be represented as a choice between software-style arithmetic operators. Primary hardware descriptions consistently define an integer pulse count accumulated during the selected 80-ms gate. A faithful implementation should therefore count admitted pulses. The sources recovered here do **not** establish the circuit-level convention for a pulse coincident with a gate edge, so that narrower timing detail remains unresolved.

The Apollo 11 MSK-1137 definition closes the controller-visibility question at the useful product boundary: LR range/velocity validity, body-axis velocity, and slant range were display products. It does not expose the onboard PCR-775 compensation choice, `RADSKAL`/`SKALSKAL`, `ALTSCBIT`, or scale/rescaling state. Those implementation details should remain internal unless a new primary source documents a controller-facing representation. The source/ground-processing chain for the displayed LR values remains unresolved.

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
- https://www.ibiblio.org/apollo/Documents/E-1982_LEM_PGNCS_and_Landing_Radar_Operations.pdf
- https://www.ibiblio.org/apollo/Documents/HSI-208625.pdf
- https://www.ibiblio.org/apollo/Documents/sundance_functional_description_vol1.pdf
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
- LMA790-3-LM, LM-6 Apollo Operations Handbook, Subsystems Data (basic 15 Dec 1968; change 15 Sep 1969)

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** altitude scale-state logic, 1.079-ft/count low scale, and flown quantity selection.
- **DOCUMENTED, REVISION-99 PRIMARY:** high/low ratio 5; `SKALSKAL=0.2`; compensation-load semantics.
- **DERIVED, APOLLO-11-EFFECTIVE:** 5.395-ft/count high scale.
- **RESOLVED, APOLLO-11 MISSION LOAD:** zero `RADSKAL`/`SKALSKAL` selects radar-performed compensation.
- **DOCUMENTED, APOLLO-11-SPECIFIC RAW WORD LENGTH:** 15 readout pulses/bits.
- **DOCUMENTED, PRIMARY APOLLO INTERFACE:** MSB-first serial transfer on complementary ones/zeros data lines.
- **RESOLVED, APOLLO-11-EFFECTIVE VELOCITY NUMERICAL REPRESENTATION:** raw LR velocity is a 12,288-count biased value; LUMINARY 099 removes the bias with `LVELBIAS=-12288`.
- **RESOLVED MODEL BOUNDARY, PRIMARY HARDWARE DESCRIPTION:** measurement formation is gated integer pulse accumulation; no separate arithmetic rounding/truncation operation is supported.
- **DOCUMENTED, APOLLO-11 CONTROLLER DISPLAY:** MSK-1137 exposes LR status, body-axis velocities, and slant range.
- **NOT DOCUMENTED AS CONTROLLER-VISIBLE:** PCR-775 compensation selection and onboard LR scale/rescaling state.
- **UNRESOLVED:** exact gate-edge pulse inclusion/phase behavior and ground-processing provenance of MSK-1137 LR values.
