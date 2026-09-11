# Apollo 13 PROCEDURES Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Operations and Procedures Officer as the controller responsible for MCC/MSFN procedural interfaces, communications support procedures, playback/data-support coordination, and real-time procedural adaptation.

---

## 1. Position

**Call sign / position:** PROCEDURES  
**Title:** Operations and Procedures Officer

### Documented responsibility

Apollo Mission Control documentation assigns PROCEDURES responsibility for:

- detailed implementation of MCC/MSFN/GSFC/KSC mission-control interface procedures;
- communications inputs/changes to the ground support timeline;
- scheduling/directing telemetry and DSE voice playbacks;
- procedural coordination with INCO and ground-support organizations.

This is not primarily a spacecraft-systems position.

---

# 2. Flight Controllers Operations Handbook

The Apollo 13 PROCEDURES report states that the active **Flight Controllers Operations Handbook (FCOH)** was:

- basic document dated September 10, 1969;
- through Revision C dated April 1, 1970.

The report says the FCOH “procedurally worked very well” during Apollo 13.

### Simulation significance

PROCEDURES is a natural owner of cross-console/interface procedure state.

This differs from:

- Flight Mission Rules — decision criteria;
- controller console handbooks — personal station procedures;
- crew checklists — onboard execution.

---

# 3. Real-time ground-system procedure adaptation

Immediately before and during Apollo 13, PROCEDURES handled cases where normal documented procedures were missing or had to change.

Example: a request to modify PCM/ground-station DACS bit suppression so strip-chart recorder deflection could be made more useful.

The interim process was:

1. data user supplied the desired bit-suppression information to PROCEDURES;
2. PROCEDURES relayed it to CCATS telemetry personnel;
3. backup ground processing was configured;
4. PROCEDURES verified that normal configuration was restored after the HSD subformat work.

### Simulation significance

PROCEDURES can alter the **ground information-processing path** without owning the underlying spacecraft subsystem.

This role may affect what other controllers can see, record, or replay.

---

# 4. Instrumentation Support Plan

Apollo 13 used an Instrumentation Support Plan distributed before simulations.

It contained communications support for mission phases and was refined through simulations.

The report says simulations corrected:

- station configurations;
- uplink/downlink modes;
- DSE dump requirements;
- TV support requirements.

After the oxygen-tank accident changed the flight plan, subsequent site configurations were handled in real time and coordinated by:

- PROCEDURES;
- TRACK;
- TIC.

### Simulation significance

The ground network configuration itself changes with mission plan.

A future scenario engine should allow ground-support configuration to follow:

- mission phase;
- revised timeline;
- contingency needs.

---

# 5. Display / ground-support problems

Apollo 13 PROCEDURES documented specific operational issues.

## MSK 1503 — next station contact table

At about 00:20 GET, **MSK 1503** displayed outdated keyhole information for 30-foot stations.

The recommended fix was to update the display with current keyhole data.

This is a second mission-specific Apollo 13 display identifier now documented outside INCO.

## Site handovers

The report found that existing documentation did not clearly define who coordinated early site handovers.

A new procedure was recommended to establish a single point of contact so that handovers would not:

- break tracking-data continuity;
- interfere with INCO commanding;
- interfere with GUIDANCE commanding.

This is another example of ground operations affecting several controller disciplines.

---

# 6. Analog recorders / telemetry processing

During analog chart-recorder calibration, all PCM ground-station data was inhibited for roughly 20 minutes.

For Apollo 13 this affected:

- chart recorders;
- events;
- meters.

PROCEDURES recommended defining calibration procedures more carefully for later missions.

### Simulation significance

A ground-system maintenance/configuration action can temporarily remove controller data products even while spacecraft telemetry is physically being transmitted.

---

# 7. Delogs and Format 30 playback coordination

Apollo 13 required repeated historical-data requests.

Examples in the PROCEDURES report include:

- additional delog copies for Systems Engineers;
- extra Format 30 playback copy requested by GNC;
- coordination with telemetry personnel to produce multiple copies.

PROCEDURES therefore plays a role in historical/high-rate data retrieval alongside:

- INCO;
- telemetry processing;
- systems controllers.

This supports the project's distinction between live telemetry and replay/analysis products.

---

# 8. Simulation fidelity critique

The PROCEDURES postflight report contains a strong example of incorrect simulation.

During an ascent simulation, a CSM subcarrier failure was intended to remove telemetry, but two-way voice incorrectly remained available because the simulated antenna failure was implemented inconsistently.

PROCEDURES explicitly notes that malfunction procedures depend on the **actual failure dependency**.

The report recommends that failures be planned carefully so that the intended procedures can be exercised.

### Architecture consequence

Failure injection must occur at subsystem/interface level rather than by independently switching arbitrary symptoms.

---

# 9. Gradual communication degradation

The PROCEDURES report also criticizes simulations in which voice/data disappeared abruptly.

It recommends simulating progressive degradation so INCO and PROCEDURES have time to respond by actions such as:

- antenna recommendation;
- low-bit-rate commanding;
- down-voice backup configuration.

This provides direct evidence that **failure progression and timing** are part of the training scenario, not just final failed state.

---

# 10. Information families justified by evidence

## Procedures / documentation

- FCOH revision/state
- site-handover procedure
- communications support procedure
- playback/delog procedure
- ground-configuration procedure

## Network / instrumentation coordination

- next station contact
- site keyhole / acquisition limits
- ground-site configuration
- telemetry processing mode
- chart recorder/calibration state
- DSE/playback request state

## Cross-discipline requests

- requester
- required data/product
- priority
- copies/destination
- completion/restore-normal status

---

# 11. PROCEDURES versus INCO / NETWORK

## PROCEDURES

Owns detailed operational interface procedures and support coordination.

## INCO

Owns spacecraft communications/instrumentation state and communications commands.

## NETWORK

Owns MSFN/network operational status and site support.

Apollo 13 repeatedly required all three.

---

# 12. Implementation status

## DOCUMENTED

- FCOH ownership/use
- ground-interface procedural role
- Instrumentation Support Plan role
- site-handover procedural issues
- MSK 1503 problem
- data-recording/calibration effects
- delog / Format 30 coordination
- simulation-fidelity recommendations

## PARTIAL

- console information requirements
- request-tracking workflow
- exact coordination loops

## UNRESOLVED

- exact Apollo 13 PROCEDURES console layout
- complete display set
- DRK/MSK assignments beyond identified examples
- exact voice-loop panel
- exact request/document forms used in live operations

---

# 13. Research targets

1. Locate Apollo 13 FCOH Revision C.
2. Locate Apollo 13 Instrumentation Support Plan.
3. Reconstruct MSK 1503.
4. Identify PROCEDURES console display/control configuration.
5. Map playback/delog request workflow into CCATS/TIC/RTCC.
6. Identify real forms/logs used by PROCEDURES.

## Primary source

- Apollo 13 Mission Operations Report, Appendix J — Procedures Officer:
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
