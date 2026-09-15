# Apollo 13 PC+2 — Minimum Player-Facing Product Set

Status: **minimum first-slice presentation set implemented**  
Purpose: define the smallest historically defensible set of controller-facing information products required for the first PC+2 vertical slice.

## Principle

The first slice does not need a complete reconstruction of every station console.

A player-facing product is included only if it is needed to perform a documented PC+2 responsibility or apply a documented decision/shutdown rule.

Each product is classified as:

- **A — exact historical display/product substantially reconstructable now**;
- **B — historical product semantics documented, exact presentation incomplete**;
- **C — communication/report workflow documented, no dedicated display required for the slice**.

Where exact format evidence is incomplete, the first implementation uses a restrained project rendering of documented information rather than claiming an exact historical CRT transcription.

---

## FLIGHT

### Required products

| Product | Class | Purpose |
|---|---|---|
| Mission clock / phase reference | B | orient final preparation and burn sequence |
| Controller readiness reports | C | integrate GO/NO-GO |
| Mission Rules / PC+2 shutdown-rule reference | C | decision authority |
| CAPCOM/crew report stream | C | receive crew-side observations and confirmations |

### Implemented first-pass player view

The current FLIGHT project rendering contains:

- mission phase / scenario orientation;
- explicit GO-for-burn decision state.

FLIGHT does **not** receive an omniscient consolidated subsystem-health dashboard.

The common session layer now records controller readiness reports and blocks scenario progression at the historical final poll until the assigned FLIGHT player explicitly records GO. The readiness-report list itself is the next session-to-presentation integration item rather than a hidden calculated summary.

### Deferred

- direct rendering of readiness reports in the FLIGHT presentation;
- exact historical FLIGHT console layout;
- later discipline assessment/callout workflows not yet required by the first nominal integration run.

---

## FIDO / RETRO

### Required products

| Product | Class | Purpose |
|---|---|---|
| Accepted RTCC trajectory-solution status | B | establish current trajectory solution validity |
| Final PC+2 maneuver target/PAD product | B | target and maneuver verification |
| Return-plan product | B | landing area / return timing consequences |
| Post-burn trajectory solution status | B | determine whether burn achieved acceptable return state |

### Implemented first-pass player view

The current FIDO/RETRO project rendering contains:

- final target TIG;
- final LVLH delta-V vector/resultant;
- expected perigee;
- final PC+2 monitor-PAD return product with predicted landing coordinates, 0.05-g range-to-go, entry-interface velocity, and predicted 0.05-g GET;
- current ground-solution status.

The final maneuver values are tied to the approximately 77:52 GET P30 LM PAD, and the return values to the 78:00:58 GET monitor PAD. Earlier preliminary PC+2 alternatives are not mixed into the final first-slice product.

### Critical implementation gap

The executable model does not yet contain a propagated post-burn FIDO trajectory/landing solution. Therefore:

- `ground.postburn.propagated_trajectory` remains deferred;
- GUIDO post-burn residuals are not substituted for a FIDO trajectory assessment;
- physical burn completion does not automatically imply an acceptable return trajectory;
- no synthetic state vector or landing solution is created to fill the screen.

### Deferred

- exact historical FIDO/RETRO CRT layout;
- complete RTCC trajectory display catalog;
- exact Cartesian RTCC state vector until required by integrated trajectory behavior;
- post-burn propagated trajectory until gameplay requires the trajectory layer.

---

## GUIDO

### Required products

| Product | Class | Purpose |
|---|---|---|
| LM guidance/control real-time product | A/B | LGC/PGNS state, program/warnings, attitude/guidance monitoring |
| Final maneuver/load status product | B | state-vector and target-load verification |
| AGS backup/cross-check product | A/B | backup guidance availability and comparison |
| Post-burn residual product | A/B | assess guidance result |

### Historical display basis

MSK 1123 and 1137 are mission-specific Apollo 13 CRTs and supply much of the visual/terminology basis for GUIDO/CONTROL. R-567 LUMINARY 1C Section 2 independently establishes program-dependent LGC downlinks and update-verification behavior. Complete field routing is not required for the first slice.

### Implemented first-pass player view

The current GUIDO project rendering contains:

- LGC operating state;
- active program / P40 state;
- program alarm;
- ISS warning;
- LGC warning/status;
- alignment accepted assessment;
- state-vector load status;
- target-load status;
- planned PGNS Vg;
- post-burn residual product when available.

`PROGRAM` and alarm/status information have direct Apollo display/downlink analogues. Alignment/load verification, planned Vg, LGC-operating boolean, and the postburn residual product are not claimed to be verbatim CRT literals where exact routing/format remains incomplete.

### Deferred

- `vg_remaining` / `dv_gained` until their modeled source paths are justified;
- AGS backup/cross-check presentation until the required PC+2 value path is modeled;
- exact attitude/rate duplication at the GUIDO boundary where CONTROL already owns the operational shutdown observation;
- noncritical MSK 1123 velocity rows;
- exact AGS ULL / ACT VEL routing unless a later failure case requires them;
- full DEDA-status reproduction;
- exact CRT coordinates/request behavior/refresh cadence.

Deferred project fields are not shown as failed historical telemetry.

---

## CONTROL

### Required products

| Product | Class | Purpose |
|---|---|---|
| LM guidance/control/propulsion real-time display family | A/B | principal burn monitoring |
| Propulsion-rule monitor | B | apply shutdown limits |
| Attitude/rate monitor | A/B | detect shutdown criteria |
| Warning/event indications | B | gimbal/CES/control failures |

### Implemented first-pass player view

The current CONTROL project rendering groups modeled products into burn/propulsion, attitude/control, and ullage information. It preserves source/provenance/validity and does not expose hidden integrity metadata.

Apollo 13 MSK 1137 `TCP` is chamber pressure expressed in percent. The modeled `GQ6510P` path is in psi, so it is shown as project `CHAMBER P` rather than falsely relabeled or converted to `TCP`.

### Critical historical distinction

The fuel/oxidizer ΔP rule is a **ground callout only**. The CONTROL product therefore exposes that ground measurement independently of crew indications when modeled.

For the implemented nonnominal branch, a threshold exceedance produces a CONTROL callout decision, followed by a distinct CAPCOM→crew communication event and a distinct crew shutdown command. The exact hypothetical CONTROL→FLIGHT→CAPCOM internal voice-loop sequence is not asserted because the reviewed PC+2 sources do not document it.

### Deferred

- singular ground inlet-pressure product until its selection/aggregation semantics are sourced;
- complete propulsion telemetry catalog;
- exact normal numeric pressure baselines where surviving evidence currently provides only shutdown thresholds;
- exact CRT routing/coordinates/refresh cadence.

---

## TELMU

### Required products

| Product | Class | Purpose |
|---|---|---|
| LM electrical-load/configuration product | B | verify burn power-up and post-burn power-down |
| Inverter-bus electrical evidence / crew caution report | B | shutdown-rule support without assuming direct caution telemetry |
| Limited consumables context | B | ensure burn configuration does not compromise return plan |

### Implemented first-pass player view

The current TELMU project rendering contains:

- LM power/configuration mode;
- documented **38–40 A burn-configuration current reference**;
- inverter-switch action state and action GET;
- no direct TELMU INVERTER-caution telemetry field; the caution state is represented to the ground through crew reporting;
- post-burn power-down transition.

The 38–40 A figure is explicitly rendered as **BURN CONFIG CURRENT REF**. It is a documented expected/required configuration load from the Mission Operations Report, not live measured current telemetry.

The onboard INVERTER caution and inverter-switch action remain distinct. Reviewed primary schematics do not establish a direct ground telemetry tap for the derived caution. Ground rule evaluation therefore uses explicit crew reporting, while source-backed `GC0071V` / `GC0155F` electrical measurements remain a separate telemetry path whose exact H-2 loading/display is unresolved.

### Deferred

- actual measured burn current until its source/value path is modeled;
- exact TELMU CRT/display layout and field labels;
- complete consumables dashboard;
- water/O2/CO2/LiOH lifetime presentation;
- detailed battery and thermal state unless required by a later scenario branch.

Deferred project fields are omitted rather than shown as failed historical telemetry.

---

## INCO

### Required products

| Product | Class | Purpose |
|---|---|---|
| Air-ground link status | B | manage weak post-AOS communication |
| Telemetry availability/quality | B | determine whether controller data are current |
| Uplink/command path state | B | support final guidance updates |
| Ranging state | B | support FIDO/trajectory solution |

### Implemented first-pass player view

The current INCO project rendering contains:

- air-ground link quality;
- voice availability;
- telemetry availability;
- ranging enabled/confirmed state;
- uplink state.

These are kept separate rather than collapsed into one communications `GO` flag. The 78:21:54 ranging-verification request is preserved as an explicit operational dependency.

### Deferred

- exact MSK 1475/look-angle layout;
- detailed antenna geometry;
- detailed RF/S-band configuration unless a future communications failure case requires it.

---

## CAPCOM

### Required products

| Product | Class | Purpose |
|---|---|---|
| Air-ground voice channel | C | sole normal operational crew communication path |
| Maneuver PAD / procedure text | C | transmit final target and rules |
| Crew readback/response stream | C | verify transfer and receive onboard observations |
| Ground/FLIGHT callout queue | C | communicate GO/shutdown/procedure decisions whose crew-facing transmission is required |

### Implemented first-pass player view

The current CAPCOM project rendering contains:

- air-ground quality;
- final PC+2 maneuver/procedure PAD;
- crew-report stream.

CAPCOM has no direct authoritative subsystem dashboard.

The new session layer also contains an explicit FLIGHT-approved CAPCOM queue and a separate CAPCOM transmission event. Surfacing that queue directly in the CAPCOM presentation is the next integration step.

### Deferred

- queue UI/presentation;
- explicit readback-state UI;
- exact historical CAPCOM console layout;
- unsourced internal controller-loop routing.

---

## FAO / PROCEDURES

These functions are historically relevant but do not yet require dedicated player stations in the minimum vertical slice.

### Required system functions

- maintain the updated activity sequence;
- make the correct burn/power-down procedure available;
- preserve procedural ordering and dependencies;
- support FLIGHT/CAPCOM with procedure context.

Initial implementation may represent these as documented support products rather than separate player interfaces until player-count design is addressed.

---

## Cross-product metadata

Every controller-facing dynamic datum should be capable of carrying:

- sample time;
- receive time;
- validity;
- stale/unavailable state;
- source layer;
- provenance identifier.

This is required even when the first nominal run uses perfect communications after the initial weak-link period.

---

## Minimum presentation checkpoint

### Implemented

1. CONTROL burn-monitor product.
2. GUIDO guidance/load/residual product.
3. TELMU power/configuration product.
4. FIDO/RETRO target and return product.
5. INCO link/ranging product.
6. FLIGHT decision view.
7. CAPCOM PAD/voice/report view.

The minimum first-slice presentation set is therefore **complete enough for integrated playtesting**.

### Active priority — integration

Do not add more display fields simply because historical material exists. Current implementation priority is:

1. session/player snapshot serialization;
2. readiness reports visible to FLIGHT;
3. CAPCOM pending/transmitted queue visible to CAPCOM;
4. scripted multi-station nominal playthrough;
5. transport/mobile shell.

### Add only if required by usability/validation

- additional MSK 1123/1137 fields;
- secondary trajectory displays;
- detailed consumables pages;
- antenna look-angle page;
- full DEDA/status panels;
- exact console coordinates/format reconstruction.

---

## Historical-presentation rule

For an exact historical display, preserve its documented layout and labeling.

For a product whose semantics are known but exact screen is not, use a neutral project rendering that:

- uses historical terminology and units only where equivalence is justified;
- does not add diagnosis or modern alert semantics;
- does not claim to be an exact Apollo screen;
- preserves source/validity distinctions;
- can later be replaced by an exact historical format without changing the underlying parameter model.

This permits implementation to proceed without inventing archival details.

## Sources / repository basis

- Apollo 13 *Mission Operations Report*, controller appendices and PC+2 chronology.
- Apollo 13 Technical Air-to-Ground Voice Transcription / Flight Journal.
- Apollo 13 Mission Report communications sections.
- Apollo 13 AC Electronics *Guidance & Navigation Summary*, MSK 1123/1137.
- Apollo 13 TELMU Post Mission Report.
- Apollo 13 FIDO and RETRO post-mission reports.
- Apollo 13 Review Board Appendix B.
- MIT R-567 LUMINARY 1C Section 2 — Data Links, Rev. 8.
- Existing station specifications under `docs/stations/`.
- Research notes 029–079.
