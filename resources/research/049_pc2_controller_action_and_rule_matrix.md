# Apollo 13 PC+2 — controller action and rule matrix

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — sufficient to define the first nominal vertical-slice information model; exact console-format placement remains separate.**

## Purpose

Research note 048 selected Apollo 13 PC+2 preparation/execution as the best first vertical-slice candidate. This note converts the historical event into a controller-oriented action/rule matrix without requiring complete reconstruction of every Apollo 13 display.

The governing principle is scenario relevance: only information that can affect PC+2 preparation, execution, shutdown, or immediate post-burn verification is elevated to first-slice priority.

---

## 1. Historical sequence relevant to the playable slice

Mission Operations Report / revised flight-plan evidence establishes:

| GET | Event | First-slice significance |
|---|---|---|
| ~74:00 | AOT Sun check | verifies platform alignment before burn planning is finalized |
| ~76:00 | LM-burn Mission Rules review | establishes shutdown criteria before final preparation |
| 76:16 | PTC terminated; AOT star check satisfactory | alignment remains acceptable |
| 76:49 | maneuver toward burn attitude; AOT check satisfactory | confirms burn-attitude pointing knowledge |
| 77:09–77:34 | lunar LOS | temporary communications/telemetry interruption |
| 77:56 | S-IVB lunar impact | background mission event; not a control requirement for PC+2 |
| ~77:59 | final PC+2 maneuver PADs passed | final target data enters crew/ground workflow |
| 78:12 | LM power-up begins | vehicle enters burn configuration |
| 78–79:27 | external ΔV / state-vector / AGS-PGNS preparation | final guidance and readiness activity |
| 79:27:38.30 | ignition | start of monitored DPS burn |
| 79:32:02.12 | actual cutoff | guided shutdown, near prediction |
| 79:34 | LM power-down starts | immediate post-burn transition |

The first software slice can begin near 77:55–78:00 while treating earlier alignment/rule review as established historical state.

---

## 2. Core burn parameters

Mission Operations Report values:

- TIG: **79:27:38.30 GET**
- planned burn time: **4:23.69**
- actual burn time: **4:23.82**
- planned cutoff: **79:32:01.99**
- actual cutoff: **79:32:02.12**
- planned total ΔV: **861.5 ft/s**
- ullage: **2 jets / 10 seconds**
- propulsion: **LM DPS**
- primary guidance: **PGNS**
- AGS: backup / cross-check

GUIDO's postflight report records the maneuver as nominal and gives planned/executed guidance values. Those values should become nominal validation data rather than decorative historical text.

---

## 3. Documented shutdown criteria

The Mission Operations Report records the PC+2 Mission Rules review and the following shutdown criteria.

| Criterion | Historical threshold / condition | Strongest responsible discipline | Information-path implication |
|---|---|---|---|
| DPS thrust / chamber pressure | ground criterion approximately **85 psi**; onboard approximately **77% thrust** | CONTROL | ground telemetry and crew/onboard indication are distinct observations of the same engine-performance problem |
| DPS inlet pressure | ground approximately **150 psi**; onboard approximately **160 psi** | CONTROL | requires propulsion telemetry plus crew-side criterion; do not collapse them to one Boolean |
| fuel/oxidizer inlet ΔP | **>25 psi** | CONTROL → FLIGHT/CAPCOM | explicitly documented as a **ground callout only**; must exist in ground information even if not independently available to crew |
| attitude error | approximately **±10°**, excluding start transient | CONTROL / GUIDO boundary | needs attitude/guidance state; exact station display placement can remain unresolved initially |
| attitude rate | approximately **±10°/sec** | CONTROL | requires independently evolving vehicle-rate state |
| engine gimbal warning | warning present | CONTROL | warning/event path must be distinguishable from underlying gimbal physical state |
| ISS warning + program alarm | combined condition | GUIDO | onboard guidance/computer state delivered to ground/crew |
| LGC warning | warning present | GUIDO | onboard-computer health path |
| CES DC failure | failure present | CONTROL | control-electronics state, not generic LM electrical health |
| inverter warning after attempted switch | persistent warning | TELMU / CONTROL interface | electrical supply consequence affects control/guidance readiness; exact ownership during PC+2 should be checked before player-role locking |

### Important implementation rule

Do **not** precompute one historical `burn_abort` flag.

The simulator should expose the component measurements/events, allow the responsible controller(s) to interpret them, and let FLIGHT/CAPCOM/crew action follow from that interpretation.

---

## 4. Controller action matrix

### FLIGHT

Primary responsibilities in the slice:

- integrate readiness recommendations;
- decide whether to continue or shut down based on controller reports and mission rules;
- arbitrate conflicts between guidance, propulsion, trajectory and consumables constraints;
- communicate crew action through CAPCOM.

Required first-slice information:

- controller voice/reports;
- mission-rule reference;
- mission time / burn phase;
- no omniscient subsystem dashboard.

### FIDO

Primary responsibilities:

- maintain accepted trajectory solution;
- provide/validate maneuver targeting state;
- determine post-burn trajectory consequence.

Required first-slice information:

- current trajectory/state-vector product;
- PC+2 target/ΔV solution;
- post-burn tracking/trajectory residual sufficient for burn verification.

Exact historical FIDO CRT format remains non-blocking for the first nominal slice if the underlying product semantics are preserved.

### RETRO

Primary responsibilities:

- evaluate return-time / landing-area consequences of the accepted maneuver;
- maintain return/reentry plan built from the trajectory solution.

For a small first player count, FIDO/RETRO may eventually be aggregated, but the internal simulation products should remain separate.

### GUIDO

Primary responsibilities:

- verify LGC/PGNS readiness;
- support final state-vector / target-load workflow;
- monitor platform/alignment state;
- compare PGNS and AGS as required;
- monitor computer/guidance warnings;
- evaluate post-burn guidance residuals.

First-slice data priorities:

- LGC operating/program/alarm state;
- maneuver target / state vector;
- relevant alignment/attitude quantities;
- PGNS residuals / achieved guidance result;
- AGS cross-check quantities needed for PC+2.

This means complete MSK 1123 reconstruction is **not** required before GUIDO can be prototyped for PC+2.

### CONTROL

Primary responsibilities:

- DPS/RCS burn configuration;
- propulsion readiness;
- GDA/control readiness;
- thrust/chamber/inlet/ΔP monitoring;
- attitude/rate monitoring;
- propulsion/control shutdown recommendations;
- immediate post-burn control/power-down handoff support.

First-slice data priorities:

- DPS chamber/thrust indication;
- inlet pressures;
- fuel/oxidizer differential pressure;
- throttle / engine operating state;
- GDA/gimbal warning/state;
- attitude error / body rates;
- CES control-electronics status;
- RCS ullage status/consumption only to the degree it affects the burn.

This is the strongest station-specific rule set currently available for the first slice.

### TELMU

Primary responsibilities:

- verify LM electrical/environmental state can support burn configuration;
- monitor electrical load during power-up;
- protect the post-burn consumables/power-down plan;
- identify electrical/inverter conditions that make guidance/control operation unsafe.

First-slice data priorities:

- LM power/load state;
- battery/available energy state sufficient for the burn and immediate post-burn plan;
- inverter/electrical status relevant to the documented burn criteria;
- water/O2/thermal state only where it changes burn or power-down decisions.

Avoid implementing the entire TELMU consumables model solely because it exists in the historical mission.

### INCO

Primary responsibilities:

- maintain usable air-ground/telemetry/uplink path around lunar LOS/AOS and final updates;
- expose link state and command/telemetry availability rather than automatic success.

First-slice priorities:

- LOS/AOS state;
- telemetry availability;
- voice link availability;
- command/uplink availability and execution/verification behavior needed by maneuver-data updates.

Exact MSK 1475 layout is not required for the nominal PC+2 slice unless link geometry becomes an active player decision.

### CAPCOM

Primary responsibilities:

- transmit final procedures/rules/callouts to crew;
- receive crew readbacks and observations;
- relay FLIGHT-directed shutdown or continuation decisions.

Crew readback should be modeled as an information source separate from telemetry.

### FAO / PROCEDURES

Primary responsibilities:

- integrate revised activity sequence;
- stage burn/power-down procedure changes;
- maintain ground/crew procedure coherence.

Whether either is a dedicated first-slice player remains a later player-count decision.

---

## 5. First-slice information layers

The PC+2 scenario validates five distinct information classes:

1. **physical state** — actual thrust, pressures, attitude, electrical state;
2. **onboard state** — LGC/PGNS/AGS programs, targets, alarms, residuals;
3. **telemetry/link state** — what arrives at MCC and whether it is current/valid;
4. **ground-derived state** — trajectory solution, target products, comparisons;
5. **crew report** — onboard indications, readbacks, observations.

A nominal implementation should preserve those boundaries even if each physical subsystem begins with a deliberately limited model.

---

## 6. Historical validation targets

The nominal PC+2 run should reproduce at least:

- ignition at 79:27:38.30 GET;
- burn duration near 4:23.8;
- cutoff near 79:32:02.1;
- total commanded/achieved ΔV near the documented ~861 ft/s target;
- no triggered shutdown criteria in the nominal case;
- small PGNS residuals consistent with the postflight account;
- transition into power-down immediately after the burn.

The historical run is a validation case, not a scripted outcome: later nonnominal scenarios should be able to perturb the underlying state so the same rules lead to different controller decisions.

---

## 7. Research sufficiency / deferred gaps

The following are now **deferred rather than active blockers** unless the PC+2 implementation proves otherwise:

- exact non-critical MSK 1123 velocity-field routing;
- complete MSK 1137 field provenance;
- AEA/LGC/PCM header runtime semantics;
- complete EECOM console hardware;
- exact INCO look-angle screen layout;
- complete FIDO/RETRO CRT catalog;
- non-PC+2 telemetry calibrations;
- exact Staff Support Room representation.

The source that would resolve a deferred field should remain cataloged, but research effort should move to the scenario model/action path.

---

## 8. Next work

1. Define the authoritative PC+2 initialization state and parameter dictionary.
2. Build a nominal event/state timeline from ~77:55 through 80:00.
3. Map each first-slice parameter to source class: physical / onboard / telemetry / ground-derived / crew report.
4. Identify only the historical CRT/display fields necessary to expose those parameters to the relevant players.
5. Use the documented PC+2 planned/actual values as the first validation dataset.

---

## Primary sources

- *Mission Operations Report — Apollo 13*, 28 April 1970, Flight Director report and controller appendices.  
  https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- Apollo 13 Flight Journal, Day 4 PC+2 preparation/execution.  
  https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- Apollo 13 mission-document index.  
  https://apollojournals.org/afj/ap13fj/a13-documents.html
- Repository station specifications, especially `APOLLO13_CONTROL.md`, `APOLLO13_GUIDO.md`, `APOLLO13_FIDO.md`, `APOLLO13_RETRO.md`, `APOLLO13_TELMU.md`, `APOLLO13_INCO.md`, `APOLLO13_FLIGHT.md`, and `APOLLO13_CAPCOM.md`.
