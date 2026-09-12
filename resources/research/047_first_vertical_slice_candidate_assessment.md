# First vertical-slice candidate assessment

Date: 2026-09-11  
Status: **REVIEWED — recommends Apollo 13 PC+2 preparation/execution as the first vertical slice.**

## Purpose

Phase 1 has reconstructed enough of the Apollo 13 control-room organization, controller responsibilities, data paths, and several key display families to begin choosing a bounded first playable scenario.

This assessment deliberately applies the project's research-sufficiency rule. It does not require every display field or console key to be resolved before scenario selection.

The first vertical slice should maximize:

- surviving primary-source detail;
- meaningful interaction among several controller disciplines;
- compatibility with the Apollo 13-era technical baseline;
- bounded physical/model scope;
- clear mission objectives and failure/decision criteria;
- opportunity to validate the historical information-flow architecture.

---

## Candidate A — Apollo 13 oxygen-tank accident and immediate stabilization

Approximate interval: **55:54:53 GET through the free-return DPS maneuver at 61:29:43 GET**.

### Strengths

- exceptionally rich documentation;
- iconic real-time systems diagnosis;
- strong EECOM evidence, including actual displays;
- major interaction among FLIGHT, EECOM, GNC, TELMU, CONTROL, GUIDO, FIDO/RETRO, INCO, CAPCOM, PROCEDURES and FAO;
- demonstrates imperfect telemetry, failed instrumentation, configuration uncertainty, consumables reasoning and contingency decision-making.

### Weaknesses for the first implementation

- starts with a compound CSM cryogenic/electrical failure whose physical propagation is comparatively complex;
- quickly requires simultaneous CSM shutdown, LM activation, trajectory planning, communications, consumables and crew-procedure modeling;
- the scenario boundary expands naturally rather than remaining compact;
- reproducing the accident convincingly risks implementing a large fraction of the eventual spacecraft model before the common station architecture has been validated.

### Assessment

**High-value later scenario; too broad for the first vertical slice.**

---

## Candidate B — Apollo 13 PC+2 preparation and burn

Recommended working interval: approximately **74:00 GET through 80:00 GET**, with the core burn at **79:27:38–79:32:03 GET**.

Apollo 13 Mission Operations documentation records that the flight-control team converged on a descent-engine PC+2 maneuver of roughly 850–860 ft/s to shorten the return and move landing to the Pacific. The final preparation included an LM platform/alignment check, maneuver PAD/state-vector/target-load updates, a Mission Rules review, explicit shutdown criteria, AGS backup/cross-check functions, and the DPS burn itself.

### Primary-source anchors

The Apollo 13 Mission Operations Report documents:

- management/flight-control selection of the PC+2 return plan;
- the AOT Sun check and ±1-degree alignment criterion;
- FIDO/RETRO return-time and trajectory tradeoffs;
- updated state vector and target load;
- formal PC+2 Mission Rules review around 76:00 GET;
- shutdown criteria involving thrust, inlet pressure, fuel/oxidizer differential pressure, attitude/rate, warning lights and guidance/control state;
- the executed burn and planned-versus-executed guidance quantities;
- controller-specific postflight accounts for GUIDO, CONTROL, TELMU, FIDO/RETRO and others.

The Apollo 13 Flight Journal preserves the air-ground sequence, including the maneuver PAD, burn rules and crew readbacks.

### Strong controller interaction

The interval naturally exercises:

- **FLIGHT** — integrates the return plan and GO/NO-GO decision;
- **FIDO/RETRO** — trajectory, return target and maneuver solution;
- **GUIDO** — LGC state, uplink, alignment, PGNS/AGS comparison;
- **CONTROL** — DPS/RCS configuration, thrust/pressure criteria and burn monitoring;
- **TELMU** — consumables and post-burn power-down constraints;
- **INCO** — communications/command path and tracking-site support;
- **FAO/PROCEDURES** — maneuver timeline and procedural integration;
- **CAPCOM** — crew communication and readback path.

EECOM/GNC remain relevant to the docked CSM/LM configuration and CSM state, but need not carry the full accident-diagnosis workload that would be required in Candidate A.

### Why it is a good vertical slice

- bounded six-hour interval with a very clear climax;
- one major propulsion event rather than a continuously spreading failure;
- uses the Apollo 13 LM guidance/control architecture already heavily researched;
- exposes the distinction between spacecraft telemetry, onboard computers, RTCC products, controller judgment and crew communication;
- includes historically documented abort/shutdown rules that can be tested objectively;
- supports a meaningful nominal success condition without an artificial score;
- can validate multiplayer station synchronization before the accident's full systems complexity is implemented.

### Important scope control

The first implementation does **not** need to recreate every activity between 74:00 and 80:00 continuously at maximum fidelity.

The scenario can initialize the historical state at a selected preparation point and model only the state needed to support:

1. alignment verification;
2. maneuver targeting/uplink;
3. consumables/configuration readiness;
4. GO/NO-GO and shutdown-rule monitoring;
5. DPS burn execution;
6. immediate post-burn verification/power-down handoff.

### Assessment

**Best first vertical-slice candidate.**

---

## Candidate C — Apollo 11 powered descent / PDI to landing

Core interval: powered descent beginning near **102:33 GET**, ending at lunar landing around **102:45 GET**.

### Strengths

- exceptionally compelling operational scenario;
- strong surviving mission techniques, transcript/audio, flight rules and guidance documentation;
- natural interaction among FLIGHT, FIDO, GUIDO, CONTROL/TELCOM, CAPCOM and supporting positions;
- documented program-alarm decision history is directly relevant to the descent team.

### Weaknesses for the first implementation

- requires a mission-profile step back from the Apollo 13 baseline;
- demands a more complete lunar-descent guidance, radar, propulsion and trajectory model immediately;
- precise timing and rapidly changing vehicle dynamics make weak simulation shortcuts more visible;
- exact Apollo 11 controller display/console configuration remains less complete than the Apollo 13 technical baseline.

### Assessment

**Excellent second major scenario after the common platform is proven.**

---

## Recommendation

Select **Apollo 13 PC+2 preparation/execution** as the first vertical slice.

This is not because it is the most famous Apollo event. It is the best current intersection of:

- source availability;
- station coverage already reconstructed;
- bounded model scope;
- authentic team interaction;
- historically explicit decision criteria;
- compatibility with the project's Apollo 13-era baseline.

The oxygen-tank accident remains a priority expansion scenario, while Apollo 11 powered descent is the strongest early test of mission-profile portability.

---

## Research sufficiency boundary

Selection of PC+2 does **not** require resolving every outstanding MSK 1123/1137 field transformation before implementation begins.

Before implementation, research should focus only on gaps that materially affect PC+2 player decisions:

- which PC+2-critical values must appear at GUIDO/CONTROL/TELMU/FIDO stations;
- exact mission-rule/shutdown criteria and their information source;
- maneuver state-vector/target/uplink workflow;
- alignment-verification information;
- DPS/RCS configuration and burn-monitor quantities;
- communications and crew-readback path;
- post-burn verification and immediate power-down handoff.

Other unresolved display fields can remain deferred unless implementation proves they are required.

---

## Primary sources

- *Mission Operations Report — Apollo 13*, 28 April 1970, especially Flight Director report and controller appendices.  
  https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- Apollo 13 Flight Journal, Day 4, PC+2 preparation/burn chronology.  
  https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- Apollo 13 mission document index, including Final Flight Mission Rules, Mission Operations Report, technical air-to-ground transcript and navigation procedures.  
  https://apollojournals.org/afj/ap13fj/a13-documents.html
- Mission H-2 Apollo Mission Techniques series, contemporary approved guidance/control/data-flow/decision-logic documentation.  
  https://www.ibiblio.org/apollo/Documents/
