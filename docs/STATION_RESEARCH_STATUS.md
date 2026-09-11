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
| GUIDO | B | `APOLLO13_GUIDO.md` | GUIDO report + LUMINARY 1C data-link spec + LM CRT provenance map | ground transformation/display routing; exact console access |
| EECOM | **A** | `APOLLO13_EECOM.md` | official console diagram + two real display formats | full display catalog / keyboard layouts |
| GNC | B | `APOLLO13_GNC.md` | GNC report + earlier CRT continuity lead | 683 field transcription / source mapping |
| TELMU | B | `APOLLO13_TELMU.md` | TELMU report, consumables/power chronology | exact LM systems displays |
| CONTROL | B | `APOLLO13_CONTROL.md` | CONTROL report + 1137 layout + LGC and selected LM-7 PCM provenance | remaining PCM routing/conversions + RTCC transforms + console workflow |
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
