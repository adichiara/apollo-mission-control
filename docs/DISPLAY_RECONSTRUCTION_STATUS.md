# Apollo Display Reconstruction Status

Status: **Phase 1 working index**

Purpose: separate displays that are mission-specifically documented from cross-mission continuity evidence and unresolved display assignments.

## Evidence labels

- **MISSION-SPECIFIC** — directly documented for the target mission.
- **CROSS-MISSION** — documented for another Apollo mission/configuration and useful as continuity evidence only.
- **LATER-APOLLO MAPPING** — later NASA telemetry/documentation links parameters to an MSK/display number.
- **UNRESOLVED** — identifier/content known only partially.

---

## Apollo 13 mission-specific identifiers currently established

| MSK / display | Function | Evidence |
|---:|---|---|
| 1475 | LM Look Angle Display | Apollo 13 INCO Post-Mission Report |
| 1503 | Next Station Contact Table | Apollo 13 PROCEDURES Post-Mission Report |
| CSM EPS HIGH DENSITY | EECOM electrical/fuel-cell display | Apollo 13 Review Board fig. B7-8 |
| CSM ECS-CRYO TAB | EECOM environmental/cryogenic display | Apollo 13 Review Board fig. B7-9 |

The Apollo 13 Review Board identifies the two EECOM pages as the station's two most frequently used formats and states they updated once per second.

---

## Guidance/control CRT family — cross-mission evidence

AC/Delco mission-summary material for Apollo 11 explicitly identifies the ASPO 45 CRT set:

- **MSK 683 (CM)**
- **MSK 966 (CM)**
- **MSK 1123 (LM)**
- **MSK 1137 (LM)**

An Apollo 13 AC Electronics *Guidance & Navigation Summary* survives and explicitly contains an **ASPO 45 CRT Displays** section, but the Apollo 13 pages have not yet been extracted.

Therefore the identifiers below are not yet promoted to Apollo 13 mission-specific status.

### MSK 683 — CSM GNC PRIMARY TAB — CROSS-MISSION

Earlier Apollo material identifies 0683 as:

**CSM GNC PRIMARY TAB**

Documented field families include:

- ground / CTE / CMC timing
- DSKY noun and registers
- DAP state
- deadband and rate
- vehicle acceleration
- VG X/Y/Z
- PIPA X/Y/Z
- TIG
- CSM RCS quad data
- SPS/control information
- gimbal / TVC information
- guidance/control status

This strongly matches Apollo 13 GNC's documented operational workload but is not proof that Apollo 13's page was unchanged.

### MSK 966 — CM guidance/navigation/rendezvous page — CROSS-MISSION

Earlier Apollo material includes computer, rendezvous, optics, state/targeting and maneuver quantities.

Exact title/layout still being transcribed.

### MSK 1123 — LM GUIDANCE, CONTROL AND PROPULSION REAL-TIME — CROSS-MISSION

Earlier Apollo material labels the page approximately:

**LM GUID, CONTROL AND PROP RT**

Documented fields include:

- GET
- AGS time
- LGC time
- downlink format identification
- receiving site
- time to engine cutoff
- time to end of descent phase
- DAP roll/pitch/yaw rates
- AGS rate gyro / ASA body rates
- LGC attitude commands
- local-vertical/body attitude quantities
- resolver/gimbal/CDU/IMU attitude
- AGS attitude
- PGNS error
- AGS error
- moment/offset terms
- AGS velocity
- LGC delta velocity
- AGS delta velocity
- propulsion/control information

This display clearly spans information relevant to GUIDO and CONTROL.

### MSK 1137 — LM powered-descent/control display — CROSS-MISSION

Earlier Apollo material explicitly documents fields including:

- GET / LGC clock / GMT
- site
- downlink ID
- throttle select status
- descent throttle command
- manual throttle
- automatic throttle
- total commanded throttle
- variable actuator position
- LGC-commanded thrust
- thrust-chamber pressure
- LGC/DAP attitude error
- AGS positional error
- desired body rates
- engine-generated angular acceleration/offset
- engine gimbal direction
- attitude-hold status
- automatic stabilization status
- cumulative commanded control torque

This page is particularly relevant to LM powered descent and CONTROL/GUIDO interaction.

---

## Later Apollo telemetry mapping evidence

Later NASA mission-evaluation/instrumentation documentation maps individual LM telemetry measurements to primary MSK numbers.

Examples include:

### MSK 1123

Mapped parameters include classes such as:

- APS helium pressures
- APS valve/low-level states
- APS fuel/oxidizer pressures
- ascent thrust-chamber pressure
- DPS regulator / helium pressures
- DPS propellant quantities/pressures
- RCS/control-system quantities
- guidance/control discretes and rates

### MSK 1137

Mapped parameters include examples such as:

- landing-radar bad/range/velocity states
- rendezvous-radar no-track
- radar antenna temperatures

This later mapping supports the functional continuity of 1123/1137 as LM guidance/control/propulsion displays.

It does **not** by itself prove the exact Apollo 13 field set or layout.

---

## Important continuity rule

For Apollo 13:

1. use the mission-specific Apollo 13 AC Electronics CRT section when extracted;
2. compare it against Apollo 11/12 ASPO 45 pages;
3. use later Apollo telemetry mappings as supporting continuity evidence;
4. do not fill missing Apollo 13 fields solely from later missions.

---

## Highest-value extraction target

**Apollo 13 Guidance & Navigation Summary — ASPO 45 CRT Displays**

The public high-resolution scan is indexed by the Apollo 13 Flight Journal and the same document is independently cataloged by Smithsonian NASM.

Extracting those few pages could potentially move:

- GNC
- GUIDO
- CONTROL

from workflow-level reconstruction to actual display reconstruction.

---

## Sources

- Apollo 13 Flight Journal, Mission Documents:
  https://apollojournals.org/afj/ap13fj/a13-documents.html
- AC Electronics Apollo 11 Guidance & Navigation Summary:
  https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- Apollo 17 Mission Evaluation Plan, NASA-TM-X-69530 / MSC-07361:
  https://ntrs.nasa.gov/citations/19730018126
- LM-10 Instrumentation Packet:
  https://www.ibiblio.org/apollo/Documents/LM-10_Instrumentation_Packet.pdf


## 2026-09-11 evidence update — mission-specific CRT pages inspected

The former size/extraction blocker is resolved. Direct inspection of the Apollo 13 scan confirms MSK 683, 966, 1123, and 1137 in ASPO-1–12 (PDF pages 179–190). Layouts are on PDF 180, 182, 186, and 188 respectively. These identifiers/layout references are now **MISSION-SPECIFIC**, superseding earlier unresolved identifier status in this document. Unchanged field-level continuity from Apollo 11 remains unproven.

See [direct inspection and page map](../resources/research/029_apollo13_aspo45_direct_inspection.md). Full transcription, refresh behavior, operational revisions, and station access remain open. No station maturity rating is raised by this update alone.
