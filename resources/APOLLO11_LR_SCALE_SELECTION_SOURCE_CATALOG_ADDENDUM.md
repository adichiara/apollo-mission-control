# Apollo 11 LR scale-selection source-catalog addendum

Date: 2026-09-20
Parent: `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| LUMINARY 099 `FLAGWORD_ASSIGNMENTS.agc` | `ALTSCALE` / `ALTSCBIT` identifies LR altitude scale state | Apollo-11-effective software state; not proof of controller visibility. |
| LUMINARY 099 `SERVICER.agc` | Tests `ALTSCBIT`; high-scale branch bypasses rescaling; low-scale path applies `SKALSKAL` | Apollo-11-effective estimator/interface logic. |
| LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc` | `SKALSKAL`: `LR ALT SCALE FACTOR RATIO: .2 NOM` | Apollo-11-effective software definition of nominal ratio; not alone a mission load. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` / assembly information | Low-scale LR altitude representation = 1.079 ft/count | Apollo-11-effective converted/stored scaling. |
| Apollo 11 LUMINARY 99 prelaunch erasable-load table, LM5/4.5.1-1 | `SKALSKAL` = `00000`; `RADSCALE` = `00000,00000` | Mission-specific load record; zero/run-time semantics unresolved. |
| AC Electronics ND-1021042, *LEM Primary Guidance, Navigation, and Control System*, Table 1-III (source data through 15 Jan 1966) | LR-originated `Range low scale factor` discrete issued automatically at approximately 2,500 ft; digital LR data pulses; LGC readout/gate-reset/range/velocity strobes | Primary pre-mission interface evidence. Establishes physical scale-state signaling and transfer architecture, not LM-5 numeric bit weights. |
| Grumman LMA790-3-LM, *Apollo Operations Handbook, Lunar Module, Subsystems Data*, LM-6, basic 15 Dec 1968 / change 15 Sep 1969 | At range PRF equivalent to 2,500 ft or less, altimeter mode changes and low-scale discrete is enabled; signal-data circuits convert/count radar data into 15-bit format and read shift-register data serially to LGC | Primary immediately post-Apollo-11 configuration evidence. Strong continuity; do not silently substitute LM-6 numeric implementation details for LM-5. |
| MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B* | `DNLRALT`: low scale 0.3288792 m = 1.0790 ft/count; high scale 1.64440 m = 5.3950 ft/count. `SKALSKAL` B0, unitless. | Primary MIT/MSC near-mission evidence. The exact low/high ratio is 0.2, explaining `.2 NOM`; do not silently back-project 5.3950 ft/count into LM-5 until Luminary 1A/hardware evidence confirms continuity. |

## Controlled conclusion

The semantic meaning of LUMINARY 099's `.2 NOM` is strongly bounded: the immediately succeeding Luminary 1B guidance equations define low/high LR altitude count values whose ratio is exactly 0.2. Independent hardware/interface documentation also shows that the LR itself originated an automatic low-scale indication near 2,500 ft and transferred digital radar data under LGC strobe/readout control, with the immediately post-Apollo-11 handbook explicitly describing a 15-bit serial path. The remaining question is no longer whether the high/low state had a physical interface basis, but whether the 5.3950-ft/count high-scale conversion and complete raw encoding are directly demonstrable for LM-5, and how the Apollo 11 `00000` prelaunch entry relates to run-time initialization.

## Sources

- https://www.ibiblio.org/apollo/listings/Luminary099/FLAGWORD_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/CONTROLLED_CONSTANTS.agc.html
- https://www.ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://www.ibiblio.org/apollo/Documents/apollolunarexcuracel_0.pdf
- LMA790-3-LM, LM-6 Apollo Operations Handbook, Subsystems Data (basic 15 Dec 1968; change 15 Sep 1969)
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** altitude scale-state branch, low-scale rescaling, and 1.079-ft/count low-scale representation.
- **DOCUMENTED, PRIMARY INTERFACE / STRONG CONTINUITY:** automatic LR-originated low-scale indication near 2,500 ft and digital pulse/strobe transfer architecture; 15-bit serial path explicitly documented immediately after Apollo 11.
- **DOCUMENTED, NEAR-MISSION PRIMARY:** 5.3950-ft/count high scale and exact 0.2 low/high ratio in Luminary 1B.
- **UNRESOLVED:** direct LM-5/Luminary 1A high-scale confirmation; mission zero-padload semantics; complete raw serial sign/bias/framing and rounding.
