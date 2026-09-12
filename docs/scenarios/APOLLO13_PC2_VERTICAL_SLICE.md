# Apollo 13 PC+2 Vertical Slice

Status: **Phase 2 working specification**  
Mission: Apollo 13  
Scenario: Pericynthion +2 hour return maneuver  
Decision basis: D-013 / research note 048

## 1. Purpose

This is the first implementation target for the Apollo Mission Control simulation.

The scenario reproduces the final preparation, execution, and immediate verification of Apollo 13's PC+2 maneuver using the docked CSM/LM stack and the LM Descent Propulsion System.

The vertical slice exists to validate the common simulation architecture and multiplayer controller workflow. It is not intended to reproduce every activity of Apollo 13 before the burn.

## 2. Historical event

Apollo 13 used a docked LM DPS burn after lunar pericynthion to shorten the return to Earth and move the landing area to the Pacific.

The Mission Operations Report gives the planned PC+2 parameters as approximately:

- TIG: **79:27:38.30 GET**
- burn duration: **4:23.69** planned; **4:23.82** actual
- cutoff: **79:32:01.99** planned; **79:32:02.12** actual
- total delta-V: approximately **861.5 ft/s** planned
- ullage: **two jets for 10 seconds**
- propulsion: LM DPS
- primary guidance/control: LM PGNS, with AGS backup/cross-check

The revised flight plan places PC+2 preparation across roughly 74:00–80:00 GET.

## 3. Recommended playable boundary

### Historical context window

**74:00–80:00 GET**

This captures the AOT alignment checks, mission-rule review, final maneuver updates, LM power-up, burn, and immediate power-down transition.

### Recommended first playable start

**Approximately 77:55–78:00 GET** is the current implementation recommendation, not yet a final decision.

Reason:

- the earlier Sun/star alignment verification and mission-rule review can be represented as established starting context;
- the final maneuver PADs, state-vector/target-load handling, LM power-up, AGS/PGNS preparation, burn readiness, burn monitoring and post-burn handoff remain live;
- this keeps the first session near a practical duration without inventing time compression before the project decides whether acceleration is allowed.

The exact start GET should be frozen only after the controller action sequence is mapped.

### Working endpoint

**Approximately 80:00 GET**, after burn verification and initiation of LM power-down.

The later establishment of PTC may be added after the core slice is working.

## 4. Historical preparation sequence

Primary mission documentation establishes the following sequence:

- ~74:00 — AOT Sun check used to assess LM platform alignment.
- 76:00 range — Mission Rules review for the LM burn.
- 76:16 — PTC terminated; AOT star check completed satisfactorily.
- 76:49 — maneuver toward burn attitude; AOT check at burn attitude satisfactory.
- 77:09–77:34 — loss of signal during lunar occultation.
- 77:56:27 — S-IVB lunar impact noted in the mission timeline.
- ~77:59 — final PC+2 maneuver PADs passed to the crew.
- 78:12 — LM power-up begun for burn configuration.
- before TIG — state-vector/target-load and guidance preparation; AGS aligned/cross-checked against PGNS.
- 79:27:38.30 — PC+2 ignition.
- 79:32:02.12 — actual guided cutoff.
- 79:34 — LM power-down initiated except functions required for subsequent attitude control/PTC.

Exact action ownership and uplink timing should be refined from the controller appendices and technical transcript before implementation is frozen.

## 5. Burn rules and monitoring requirements

The Mission Operations Report records a formal mission-rule review before PC+2. The documented shutdown criteria include:

- thrust/chamber-pressure criterion: ground and onboard indications had corresponding limits;
- DPS inlet-pressure criterion;
- fuel/oxidizer differential-pressure criterion, explicitly involving a **ground callout**;
- attitude error limit of approximately 10 degrees outside start transients;
- attitude-rate limit of approximately 10 degrees/second;
- engine-gimbal warning;
- inertial-reference warning combined with computer program alarm;
- LGC warning;
- CES DC power failure;
- persistent inverter warning after attempted inverter switching.

The exact station/source for each criterion must be mapped before the player information model is frozen.

The simulation should never present a generic `BURN GOOD/BAD` diagnosis. Controllers must see the measurements, warnings, crew reports, and guidance information from which the decision is made.

## 6. Core controller functions

### FLIGHT

- integrates station readiness;
- manages GO/NO-GO and shutdown decisions;
- receives discipline recommendations rather than omniscient simulation state.

### FIDO / RETRO

- owns trajectory/return solution and landing-target consequences;
- provides the accepted maneuver solution and post-burn trajectory assessment;
- preserves the distinction between trajectory-state determination and return/reentry planning even if later player scaling combines the roles.

### GUIDO

- monitors LGC/PGNS state and maneuver data;
- supports state-vector/target-load/uplink workflow;
- monitors alignment and PGNS/AGS consistency;
- verifies guidance residuals after cutoff.

### CONTROL

- monitors DPS/RCS configuration and propulsion/control readiness;
- owns propulsion-related shutdown criteria and relevant ground callouts;
- monitors attitude/control behavior and DPS performance during the burn.

### TELMU

- monitors LM electrical/environmental/consumables state;
- confirms the vehicle can support burn configuration and the planned post-burn power-down;
- should not be reduced to a single remaining-lifetime value.

### INCO

- maintains the communications/command path needed for updates and crew communication;
- exposes communications state rather than guaranteeing command delivery.

### CAPCOM

- communicates procedures, maneuver information, GO/NO-GO decisions and callouts to the crew;
- crew responses/readbacks are a separate information source from telemetry.

### FAO / PROCEDURES

- supports the updated activity sequence and ground/crew procedure coordination;
- exact first-slice player representation remains to be decided.

## 7. Minimum authoritative simulation state

The first slice should model only the state that can materially alter PC+2 decisions or observations.

### Trajectory/navigation

- mission time;
- current trajectory state sufficient for the PC+2 target and post-burn verification;
- maneuver target/vector;
- PGNS state vector;
- relevant AGS backup/cross-check state;
- alignment/attitude-error state.

### Propulsion/control

- DPS operating state;
- commanded/actual thrust or chamber-pressure representation;
- inlet/propellant pressure state needed for burn rules;
- fuel/oxidizer differential pressure;
- throttle profile;
- RCS ullage availability;
- attitude/rates;
- engine/gimbal/control warnings relevant to documented shutdown criteria.

### Guidance/computers

- LGC operating state and program/alarm state;
- PGNS guidance progression and cutoff;
- AGS monitoring/backup state;
- guidance residuals.

### Electrical/consumables

- LM electrical load/power availability sufficient to support burn configuration;
- consumable state required for readiness and post-burn power-down decisions;
- only dependencies that can affect this interval need full behavior initially.

### Communications/data path

- command/uplink availability;
- air-ground voice availability;
- telemetry availability/validity sufficient to allow historically meaningful data loss or stale-state variants later.

## 8. Information-path requirements

The first slice must preserve these separations even if the physical models are initially simple:

```text
physical spacecraft state
    ↓
sensors / onboard computers
    ↓
telemetry / communications
    ↓
ground processing / RTCC products
    ↓
controller displays and indications
    ↓
controller judgment
    ↓
FLIGHT / CAPCOM / crew action
```

A future failure may occur at any of these layers. The first nominal run should therefore not wire all displayed values directly to perfect authoritative state.

## 9. Deferred research that is not a blocker

Unless a PC+2 implementation dependency emerges, defer:

- complete MSK 1123/1137 parameter reconstruction outside burn-critical fields;
- exact AGS ULL versus ACT VEL ground algorithm if those fields are not needed for player decisions in this slice;
- full EECOM keyboard/panel reconstruction;
- complete INCO MSK 1475 layout;
- complete FIDO/RETRO display catalog;
- every Staff Support Room position;
- every voice-loop assignment;
- exact historical behavior outside the selected interval.

These remain documented gaps, not permission to invent behavior.

## 10. Immediate next work

1. Build a PC+2 event/action matrix by controller from 77:55 through 80:00.
2. Map every documented shutdown criterion to:
   - responsible controller;
   - physical quantity/event;
   - onboard/telemetry/ground source;
   - player-facing display or crew report.
3. Define the initial-state parameter set at the selected start GET.
4. Identify the smallest set of historical CRT fields/products actually required for the nominal PC+2 run.
5. Produce a nominal-state validation table using the historical planned/actual burn values.
6. Only then begin the implementation schema and simulation code.

## Primary sources

- *Mission Operations Report — Apollo 13*, 28 April 1970.  
  https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- Apollo 13 Flight Journal, Day 4 PC+2 preparation and execution.  
  https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- Apollo 13 mission-document index, including Final Flight Mission Rules, technical air-to-ground transcript, Navigation Procedures and revised mission timeline.  
  https://apollojournals.org/afj/ap13fj/a13-documents.html
- Apollo Mission Techniques, Mission H-2 and Subsequent series.  
  https://www.ibiblio.org/apollo/Documents/
