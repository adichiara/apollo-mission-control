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

## 3. Playable boundary

### Historical context window

**74:00–80:00 GET**

This captures the AOT alignment checks, mission-rule review, final maneuver updates, LM power-up, burn, and immediate power-down transition.

### First implementation start

**77:55:00 GET** is the frozen nominal vertical-slice start.

This is a source-backed operational boundary rather than an arbitrary round time:

- communications have just been reacquired after lunar occultation and are weak;
- the final P30 LM maneuver PAD begins at 77:55:24;
- the weak link interferes with the initial readback;
- the crew raises S-band power and the link becomes strong enough to complete the exchange;
- final targeting, burn-configuration power-up, ranging/uplink activity, readiness polling, burn execution, and post-burn verification all remain live.

Earlier Sun/star alignment verification and the Mission Rules review are initialized as established historical context rather than replayed.

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
- **77:55:00 — nominal vertical-slice start; communications weak after AOS.**
- **77:55:24 — final P30 LM maneuver PAD read-up begins in the air-ground record.**
- 77:56:27 — S-IVB lunar impact noted in the mission timeline.
- **77:59:17 — communications become loud and clear after the S-band power-amplifier change.**
- The Flight Director report summarizes the final maneuver PADs as passed at approximately 77:59; this is consistent with the read-up beginning earlier and completing around that time.
- 78:12 — LM power-up begun for burn configuration, with approximately 38–40 A required.
- ~78:21–78:23 — ranging and final ground/uplink computer activity are completed sufficiently for computer control to return to the crew.
- ~79:17 — Flight performs the final GO/NO-GO poll; the team is GO.
- ~79:23 — LM is in P40 / final burn program state.
- 79:27:38.30 — PC+2 ignition.
- 79:32:02.12 — actual guided cutoff.
- ~79:32:41 onward — post-burn residuals reviewed.
- 79:34 — LM power-down initiated except functions required for subsequent attitude control/PTC.

The exact second for every internal switch transition is not frozen unless a controller procedure or failure case requires it.

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

The exact station/source for each criterion is tracked in research note 049 and the PC+2 parameter specification.

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

The stable implementation-oriented parameter set is maintained in:

- `docs/scenarios/APOLLO13_PC2_PARAMETERS.md`
- `resources/research/050_pc2_initialization_and_nominal_validation.md`

### Trajectory/navigation

- mission time;
- current trajectory state sufficient for the PC+2 target and post-burn verification;
- maneuver target in its documented coordinate representation;
- PGNS state vector / loaded target state;
- relevant AGS backup/cross-check state;
- alignment/attitude-error state.

The exact Cartesian RTCC state vector at 77:55 is deliberately deferred until the trajectory propagator requires it; it will not be reverse-engineered from the PAD.

### Propulsion/control

- DPS operating state;
- commanded/actual thrust or chamber-pressure representation;
- inlet/propellant pressure state needed for burn rules;
- fuel/oxidizer differential pressure;
- throttle profile;
- RCS ullage availability;
- attitude/rates;
- engine/gimbal/control warnings relevant to documented shutdown criteria.

Exact nominal pressure values are not invented from shutdown thresholds. They are added only when a source or implementation dependency justifies them.

### Guidance/computers

- LGC operating state and program/alarm state;
- PGNS guidance progression and cutoff;
- AGS monitoring/backup state;
- guidance residuals;
- separation between LVLH maneuver-PAD components and IMU-coordinate PGNS velocity-to-be-gained values.

### Electrical/consumables

- LM electrical load/power availability sufficient to support burn configuration;
- burn-configuration current around the documented 38–40 A level;
- consumable state only where it can alter readiness or immediate post-burn power-down decisions.

### Communications/data path

- initially weak air-ground link;
- S-band power-amplifier state;
- command/uplink availability;
- ranging availability;
- telemetry availability/validity/age;
- crew voice/readback as an information channel separate from telemetry.

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

## 9. Nominal validation targets

The first deterministic nominal fixture should reproduce at least:

- TIG: **79:27:38.30 GET**;
- planned burn duration: **263.69 s**;
- actual burn duration: **263.82 s**;
- actual cutoff: **79:32:02.12 GET**;
- target resultant ΔV: **861.5 ft/s**;
- executed PGNS IMU-coordinate Vg values approximately **+742.21, -425.88, +91.04 ft/s**;
- post-burn PGNS residuals approximately **+1.0, +0.3, 0.0 ft/s**;
- no shutdown-rule trigger in the nominal run;
- transition into LM power-down after burn verification.

Mission Operations Report computed event times are authoritative for physical/guidance validation; voice timestamps represent communication events and may lag the underlying spacecraft event.

## 10. Deferred research that is not a blocker

Unless a PC+2 implementation dependency emerges, defer:

- complete MSK 1123/1137 parameter reconstruction outside burn-critical fields;
- exact AGS ULL versus ACT VEL ground algorithm if those fields are not needed for player decisions in this slice;
- exact Cartesian RTCC state vector before the trajectory model requires it;
- exact nominal values for propulsion measurements for which only shutdown thresholds are currently documented;
- full EECOM keyboard/panel reconstruction;
- complete INCO MSK 1475 layout;
- complete FIDO/RETRO display catalog;
- every Staff Support Room position;
- every voice-loop assignment;
- exact historical behavior outside the selected interval.

These remain documented gaps, not permission to invent behavior.

## 11. Immediate next work

1. Define the nominal event/state transition model from 77:55 through 79:34 using the new parameter specification.
2. Identify the smallest player-facing historical display/product set actually required by GUIDO, CONTROL, FIDO/RETRO, TELMU, INCO, FLIGHT, and CAPCOM.
3. Map those required products to the parameter/source layers without reconstructing unrelated display fields.
4. Use the historical nominal run as the first deterministic validation fixture.
5. Only then begin the implementation schema and simulation code.

## Primary sources

- *Mission Operations Report — Apollo 13*, 28 April 1970.  
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- Apollo 13 Technical Air-to-Ground Voice Transcription, mission-document collection.  
  https://apollojournals.org/afj/ap13fj/a13-documents.html
- Apollo 13 Flight Journal, Day 4 Part 2, used to navigate the underlying air-ground chronology.  
  https://www.apollojournals.org/afj/ap13fj/13day4-leaving-moon.html
- Apollo Mission Techniques, Mission H-2 and Subsequent series.  
  https://www.ibiblio.org/apollo/Documents/
