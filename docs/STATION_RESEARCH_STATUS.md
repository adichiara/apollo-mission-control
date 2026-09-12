# Apollo 13 Station Research Status

Status: **Phase 1 working index**

Purpose: track how far each Apollo 13-era station has been reconstructed and prevent workflow evidence from being mistaken for display/console evidence.

## Evidence maturity scale

- **A — Station reference:** official console/display evidence plus mission-specific operational evidence.
- **B — Strong workflow:** mission-specific operational evidence is strong; exact display/console remains incomplete.
- **C — Role baseline:** responsibility is documented, but station-specific operational/display evidence remains limited.
- **D — Not yet reconstructed.**

| Station | Maturity | Detailed spec | Strongest current evidence | Main unresolved gap |
|---|---|---|---|---|
| FLIGHT | B | `APOLLO13_FLIGHT.md` | Flight Director report + restored Flight loop | exact FLIGHT displays/console |
| CAPCOM | B | `APOLLO13_CAPCOM.md` | official role + restored CAPCOM/air-ground audio | exact console/display/procedure staging |
| FIDO | B | `APOLLO13_FIDO.md` | FIDO postflight report, RTCC/vector operations | exact trajectory displays / MSK |
| RETRO | B | `APOLLO13_RETRO.md` | RETRO postflight report, RTE/entry products | exact return/entry displays / MSK |
| GUIDO | B | `APOLLO13_GUIDO.md` | GUIDO report + LUMINARY 1C + 1123/1137 provenance + FP7 DEDA/AEA telemetry evidence | exact telemetry-to-MSK selection / RTCC transforms + console access |
| EECOM | **A** | `APOLLO13_EECOM.md` | official console diagram + two real display formats | full display catalog / keyboard layouts |
| GNC | B | `APOLLO13_GNC.md` | GNC report + earlier CRT continuity lead | 683 field transcription / source mapping |
| TELMU | B | `APOLLO13_TELMU.md` | TELMU report, consumables/power chronology | exact LM systems displays |
| CONTROL | B | `APOLLO13_CONTROL.md` | CONTROL report + 1123/1137 layouts + LGC/PCM/AEA provenance | exact telemetry-to-MSK selection / RTCC transforms + console workflow |
| INCO | B | `APOLLO13_INCO.md` | INCO report + comms paper; MSK 1475 known | actual look-angle/command display layouts |
| PROCEDURES | B | `APOLLO13_PROCEDURES.md` | Procedures report; FCOH; MSK 1503 known | console/request/display workflow |
| FAO | B | `APOLLO13_FAO.md` | FAO postflight report + revised flight plan | exact FAO/Ground Timeline displays |
| SURGEON | C | — | organizational role + medical mission material | biomedical display/workflow reconstruction |
| NETWORK | C | — | Network Operations appendix + MCC architecture | console/site/network display reconstruction |
| BOOSTER/BSE | C | — | BSE appendix + Saturn mission data | three-seat console/display reconstruction |
| AFD | C | — | organizational role | working products/console |
| RECOVERY | C | — | Recovery Operations appendix | display/data products and player relevance |
| PAO | C | — | documented role | likely outside core simulation play |
| Mission Director/FOD | C | — | documented management roles | player relevance / operational interface |

## Current interpretation

### Best first station implementation candidate

**EECOM**

It is the only station currently at maturity A because the Apollo 13 Review Board preserves:

- console anatomy;
- two actual high-use CRT formats;
- telemetry labels/codes;
- update rate;
- event/limit behavior.

### Best next display-reconstruction targets

1. **GUIDO/GNC** — Apollo 13 Guidance & Navigation Summary contains a mission-specific CRT section and is now inspected; field-level transcription and mapping remain pending.
2. **INCO** — actual display ID MSK 1475 is known; layout still missing.
3. **PROCEDURES** — actual display ID MSK 1503 is known; layout still missing.
4. **TELMU/CONTROL** — simulator/output-table documentation may reveal LM telemetry and display structure.
5. **FIDO/RETRO** — need RTCC/flight-dynamics display-format sources.

## Phase 1 gap categories

Across stations, missing evidence now falls into a small number of repeated categories:

### Console hardware

- physical station layout;
- monitor count;
- DRK/MSK/key legends;
- status/event panels;
- meters/recorders;
- voice panels.

### Display catalog

- display/MSK numbers;
- field layout;
- labels and units;
- update cadence;
- channel/request behavior.

### Data provenance

- raw telemetry;
- ground-computed values;
- RTCC products;
- replay/delog products;
- support-room analysis.

### Action/command authority

- direct ground commands;
- crew-executed procedures through CAPCOM;
- CCATS/MSFN command chain;
- update verification.

### Communications

- exact loops monitored/transmitted;
- backroom loop topology;
- handoff between Flight loop and discipline loops.

## Phase 1 exit condition

Phase 1 should not require every station to reach maturity A.

A reasonable research exit condition is:

- all likely core player positions at B or better;
- at least one systems station, one flight-dynamics/guidance station, and one communications/coordination station with enough display evidence to validate the common station architecture;
- major mission-era nomenclature/configuration differences documented;
- known source conflicts logged;
- no player-count aggregation decisions made from role titles alone.

The project is approaching that point for Apollo 13, but exact display reconstruction remains the largest gap.


## 2026-09-11 — Source extraction and comparison status

ASPO 45 pages are accessible and inspected. MSK 1137 has a normalized Apollo 13 definition-group inventory and verified differences from Apollo 11. See research notes 029–031. This advances display evidence without resolving full console configuration, access, refresh behavior, or operational revisions; maturity ratings remain unchanged.


## 2026-09-11 — LM CRT provenance pass

R-567 Rev. 8 has now been mapped against the Apollo 13 LM CRT evidence. This establishes direct LGC origins for many MSK 1123/1137 field families and, equally importantly, identifies fields that must be ground-derived or sourced from non-LGC telemetry.

The strongest new result is the landing-radar chain: the LGC downlink sends time-tagged antenna-axis data one velocity component at a time, while MSK 1137 presents stable-member velocity components and guidance-comparison residuals. Exact RTCC/ground transformation logic is therefore now a high-priority research target.

See research note 032. Maturity ratings remain unchanged at B because display access, ground transforms, non-LGC telemetry provenance, and console workflow are not yet fully reconstructed.


## 2026-09-11 — MSK 1137 non-LGC telemetry pass

Vehicle-specific sources now identify several physical/PCM measurements behind the Apollo 13 MSK 1137 hardware fields:

- GQ6510P — DPS thrust-chamber pressure;
- GQ6806H — variable-injector actuator position;
- GN7563T — LM-7 landing-radar antenna temperature;
- GN7723T — rendezvous-radar antenna temperature.

Apollo-wide NASA telemetry tables independently route GQ6806H, GN7563T, GN7723T, several PGNCS electrical measurements, and PIPA temperature to MSK 1137. Because those routing tables are retrospective, the Apollo 13 profile still requires mission-era confirmation where possible.

CONTROL remains maturity B: the provenance picture is materially better, but exact Apollo 13 display loading, engineering conversions, refresh behavior, and complete console workflow are not yet reconstructed.

See research note 034.


## 2026-09-11 — MSK 1123 provenance pass

Research note 035 begins the same field-provenance treatment for Apollo 13 MSK 1123 that notes 032–034 established for 1137.

The key result is that 1123 is also a composite Mission Control product. It combines LGC/PGNS downlink values, PCM control measurements, AGS/AEA information, radar data, propulsion state, and ground context. Apollo telemetry routing tables explicitly tie RGA rate channels, attitude-error channels, and selected APS/RCS measurements to 1123.

GUIDO and CONTROL remain at B: the display's source architecture is substantially clearer, but mission-specific AGS Flight Program 7 mapping, exact LM-7 PCM routing/calibration, ground transformations, station access, and refresh behavior remain unresolved.


## 2026-09-11 — AGS Flight Program 7 operational pass

Research note 036 adds directly inspected Flight Program 7 DEDA address evidence and, crucially, Apollo 13 in-flight validation.

Actual Apollo 13 contingency-burn procedures used:
- 400+5 body-axis alignment;
- 400+0 attitude hold;
- 404/405/406 reset;
- DEDA 470 burn monitoring.

This narrows the AGS gap from “what did Flight Program 7 expose?” to the more specific **AEA telemetry → ground decoding → MSK 1123 field** path.

GUIDO and CONTROL remain maturity B because that telemetry/display path, station access, and update behavior are still incomplete.


## 2026-09-11 — AGS telemetry / RTCC processing pass

Research note 037 separates the AEA's ground telemetry stream from the crew DEDA interface and documents the mission-era LM-7 handbook's dedicated AEA telemetry-word-list table.

General AGS documentation establishes a 50-word digital telemetry block repeated once per second, but the exact Flight Program 7 word-to-memory assignments are still being extracted rather than copied from Flight Program 6.

The Apollo 13 Mission Operations Report adds a particularly important real-world validation case: after MCC-5 the **RTCC incorrectly processed AGS body angles**. Mission Control rejected the bad ground readout and used the independent FDAI reference, which showed PTC was actually correct.

This confirms that ground-processing validity must be modeled separately from spacecraft/telemetry validity. Station maturity remains unchanged.


## 2026-09-11 — FP7 telemetry continuity matrix

Research notes 038–039 now constrain the missing Apollo 13 AEA telemetry list much more tightly.

The surviving FP6 and FP8 source listings both place their 50-word telemetry block at octal addresses **0325–0406**. Their symbols agree at 49 of 50 positions; address 0371 differs. The Apollo 13 G&N Dictionary independently supplies direct or partial mission-specific meaning for 25 of those 50 candidate addresses, including navigation vectors, time, velocity, selector state, and delta-V monitor words.

This is still **not** treated as a certified Apollo 13 Table 2.1-7. The remaining authority target is the February 1970 LM-7 handbook telemetry table. GUIDO/CONTROL maturity remains B.


## 2026-09-11 — AGS direction-cosine attitude path

Research note 040 documents the attitude representation behind the AGS telemetry architecture.

FP6 and FP8 source listings both show six telemetered direction cosines (X-body and Z-body rows) snapshotted for telemetry, rather than final body Euler angles. This fits Apollo 13's documented RTCC body-angle-processing failure and gives the project a concrete ground-transform boundary for MSK 1123 AGS ATT.

The exact FP7 Table 2.1-7 identifiers and RTCC conversion equations remain unresolved. GUIDO/CONTROL maturity remains B.


## 2026-09-11 — AGS delta-V interface pass

Research note 041 separates the AEA's telemetered delta-V accumulation from the crew DEDA readout path.

The telemetry block carries VD1X/Y/Z at 0404–0406, while Apollo 13 DEDA 470–472 represents separate 2-second navigation-update values. Apollo 13 used 404–406 zeroing and 470 monitoring operationally during contingency burns.

This removes another potential false simplification: MSK 1123 AGS DEL VEL must not be implemented as a mirror of the crew's current DEDA display. Exact CRT routing remains unresolved; maturity stays B.


## 2026-09-11 — AGS ullage provenance pass

Research note 042 separates the AGS ullage measurement, threshold test, consecutive-cycle counter, completion criterion, and controller-visible field.

This removes another ambiguity in MSK 1123: its AGS ULL field is in velocity units and therefore is not simply the MU8 counter or an ullage-acquired Boolean. Exact field calculation/routing remains unresolved; GUIDO/CONTROL maturity stays B.


## 2026-09-11 — MSK 1123 DEDA telemetry pass

Research note 043 ties the DEDA portion of MSK 1123 to explicit AEA telemetry variables: readout-mode flag, DEDA data, clear-mode flag, and DEDA address.

This is another piece of the 1123 page that can now be implemented from a historically separated source path rather than by mirroring a crew display. Exact Apollo 13 masks/formatting and FP7 telemetry IDs remain unresolved; GUIDO/CONTROL remain maturity B.


## 2026-09-11 — consolidated MSK 1123 AGS field matrix

Research note 044 consolidates the AGS portion of MSK 1123 into source-path confidence classes.

Several rows now have strong provenance (AGS time, RGA rates, AGS attitude, AGS attitude error, DEDA state), while ASA rate, AGS velocity, AGS delta velocity, and AGS ullage have constrained but not yet certified source mappings.

The main research bottleneck has shifted from “what does the page contain?” to **exact FP7 telemetry membership and RTCC/display transformation rules**. GUIDO/CONTROL remain at B.


## 2026-09-11 — MSK 1123 velocity-row semantics and ground-format context

Research note 045 separates five adjacent velocity-related rows using the Apollo 11/12 AC/Delco display definitions: **AGS VEL** (indicated velocity), **LGC DEL VEL** (two-second PIPA output), **AGS DEL VEL** (measured velocity), **AGS ULL** (ullage measurement), and **ACT VEL** (accumulated velocity along thrust). The older display definitions also constrain their historical precision without proving that the Apollo 13 masks were unchanged.

A January 1970 MIT Instrumentation Laboratory report independently reproduces the 1123-style page as a **Typical Data Format for Ground Consoles**, including the AEA/LGC/PCM header and the same velocity rows. This strengthens the evidence that the page is a composite ground-monitoring product rather than a direct mirror of a single onboard source.

The new evidence does **not** identify the exact Apollo 13 FP7 telemetry word or RTCC transformation feeding AGS VEL / DEL VEL / ULL, nor does it establish that the AEA/LGC/PCM header boxes were dynamic validity indicators. GUIDO and CONTROL therefore remain at maturity B.


## 2026-09-11 — AEA telemetry-word-list recovery

Research note 046 recovers Table 2.1-7's telemetry structure and engineering descriptions from a contemporary LMA790-3-LM copy sharing the Apollo 13 handbook's **1 February 1970 basic date**, while retaining its later **15 June 1970 change date** as an explicit continuity limitation.

The telemetry list now independently confirms distinct products for present LM inertial velocity, compensated 20-ms body-axis incremental velocity, a dimensionless ullage counter, and a separate three-word sensed body-axis velocity-increment family. It also confirms DEDA-state and attitude-direction-cosine telemetry families.

This removes “what velocity products are actually available in the AEA telemetry stream?” as the main uncertainty. The remaining high-value problem is **which telemetry product and ground transformation feeds each MSK 1123 row**. The exact LM-7 page still needs direct comparison with the June-changed searchable table. GUIDO and CONTROL remain maturity **B** because controller-facing selection, RTCC transformation, station access, and refresh behavior remain incomplete.
