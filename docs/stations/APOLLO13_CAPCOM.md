# Apollo 13 CAPCOM Station Specification

Status: **research specification — workflow strong, console/display details incomplete**

Purpose: reconstruct the Apollo 13 Spacecraft Communicator role as the controlled operational voice path between Mission Control and the flight crew.

---

## 1. Position

**Call sign / position:** CAPCOM  
**Title:** Spacecraft Communicator

### Documented responsibility

Apollo Mission Control documentation assigns CAPCOM responsibility for:

- voice communications with the flight crew;
- crew-procedure advice in coordination with Flight Activities / Mission Control.

CAPCOM was normally an astronaut, providing a communicator who understood both crew workload and technical procedure.

---

# 2. CAPCOM is a communication role, not a generic controller

CAPCOM does not replace the engineering disciplines.

A typical decision path is:

```text
technical controller
      ↓
FLIGHT
      ↓
CAPCOM
      ↓
crew
```

Crew observations and questions return:

```text
crew
  ↓
CAPCOM
  ↓
FLIGHT / relevant controller
```

The role's difficulty comes from maintaining a clean, concise, authoritative crew interface while many discussions are occurring internally.

---

# 3. Apollo 13 procedure transmission

Apollo 13 required Mission Control to develop and read up numerous nonstandard procedures, including:

- LM activation/power-down;
- CSM shutdown;
- guidance alignment;
- DPS burns;
- CO2/LiOH workaround;
- CM battery charging from LM power;
- water transfer;
- CSM reactivation;
- SM/LM jettison;
- entry preparation.

CAPCOM served as the crew-facing channel for this material.

### Simulation significance

Long procedures should not necessarily appear magically on the crew side.

Where the historical procedure was read verbally, CAPCOM may need to:

- receive a verified procedure;
- transmit it accurately;
- break it into manageable steps;
- obtain readback/confirmation;
- relay questions back to the appropriate controller.

---

# 4. Voice discipline

The value of CAPCOM is partly that the crew does **not** hear the entire Mission Control engineering discussion.

This protects the crew from:

- contradictory preliminary diagnoses;
- unfinished options;
- simultaneous controller chatter;
- unapproved procedure changes.

The simulator should preserve the distinction between:

- Flight loop discussion;
- CAPCOM/crew air-to-ground communication.

If crew audio is simulated, internal controller conversation should not leak automatically into the crew channel.

---

# 5. Crew observations as data

CAPCOM can obtain information that telemetry cannot provide or cannot reliably provide.

Examples include requests for:

- switch/talkback positions;
- visual observations;
- onboard gauge readings;
- crew perception of vehicle motion/noise;
- confirmation that procedures were completed.

These observations must then be routed back to FLIGHT/discipline controllers.

This can be particularly important when:

- telemetry is unavailable;
- instrumentation is suspect;
- the system is powered down;
- an onboard indication is not telemetered.

### Architecture implication

Crew reports are a separate information source from telemetry.

The central simulation should support a crew-state/observation layer rather than treating the crew as a passive voice soundtrack.

---

# 6. CAPCOM does not independently authorize technical actions

CAPCOM may clarify or communicate procedures, but the role is not intended to invent subsystem fixes.

The simulation should not give CAPCOM a generic menu of technical commands.

Crew-facing instructions should originate from:

- FLIGHT decisions;
- established procedures;
- appropriate controller recommendations;
- mission rules / flight-plan direction.

---

# 7. Timing and workload

CAPCOM must consider crew workload.

Apollo 13's Flight Director report explicitly notes that Mission Control delayed noncritical procedural items until the appropriate crew member was awake/available.

The mission also required coordination of:

- rest periods;
- meal periods;
- maneuver preparation;
- spacecraft power states;
- procedural read-ups.

Thus CAPCOM/FAO/FLIGHT interaction is part of the control problem.

---

# 8. Information requirements

A CAPCOM station ultimately needs:

## Voice

- air-to-ground transmit/receive
- Flight Director loop monitoring
- potentially CAPCOM/support coordination loops as documented

## Procedure state

- approved current procedure
- step/progress/readback status
- crew member responsible
- timing relative to mission event

## Crew context

- current crew member awake/available
- spacecraft occupied (CM/LM)
- ongoing maneuver/checklist
- pending questions/observations

## Mission context

- GET
- major upcoming event
- current approved plan

### Important limitation

Exact Apollo 13 CAPCOM CRT/display format assignments remain unresolved.

Do not create a modern chat/procedure dashboard and describe it as historical.

---

# 9. In-person simulation issue

Because the human players are sitting together, CAPCOM must still represent the crew boundary.

Controllers can speak to one another in the room, but they should not treat the simulated astronauts as if every controller can directly address them.

The normal operational convention should remain:

> crew communication goes through CAPCOM.

How strictly the software enforces this remains a later usability decision.

---

# 10. Implementation status

## DOCUMENTED

- crew voice responsibility
- Flight/discipline-to-CAPCOM communication structure
- procedure transmission
- crew observations/readbacks as operational information
- crew workload/timing relevance

## PARTIAL

- CAPCOM support-loop relationships
- working-document/process details

## UNRESOLVED

- exact Apollo 13 CAPCOM console layout
- exact CRT displays
- DRK/MSK configuration
- exact voice-panel configuration
- whether/how procedure text was physically staged at the console for specific Apollo 13 contingency sequences

---

# 11. Research targets

1. Extract CAPCOM channel audio from representative Apollo 13 periods.
2. Compare Flight loop decision → CAPCOM transmission → crew readback timing.
3. Inspect Flight Director log/procedure read-up documents.
4. Locate CAPCOM console handbook/console configuration.
5. Determine CAPCOM display access and voice-loop keying.

## Sources

- Apollo 13 Mission Control audio / CAPCOM channel:
  https://apolloinrealtime.org/13/
- Apollo 13 Mission Operations Report:
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- Apollo 13 Flight Director Logs / checklist read-up documents:
  https://apollojournals.org/afj/ap13fj/a13-documents.html
