# Apollo 13 FAO Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Flight Activities Officer as the Mission Control owner/coordinator of the operational flight plan and crew activity timeline.

FAO is not merely an administrative scheduler. Apollo 13 shows FAO continuously integrating technical constraints into what the crew should do, when, and in what order.

---

## 1. Position

**Call sign / position:** FAO  
**Title:** Flight Activities Officer

### Documented responsibility

Apollo Mission Control documentation assigns FAO responsibility for:

- developing and coordinating the flight plan;
- detailed implementation of crew activities;
- coordination of timeline changes with controllers and Flight Plan Support.

---

# 2. Nominal mission workload

Before the accident, FAO coordinated routine changes such as:

- purge scheduling with EECOM;
- launch-vehicle debriefing questions;
- photography opportunities;
- P23/navigation activities;
- TV scheduling;
- LM early-entry planning;
- PTC activities;
- flight-plan deletions.

This means FAO has active workload even when no emergency exists.

---

# 3. Cross-discipline timeline integration

The Apollo 13 report shows FAO repeatedly coordinating with other disciplines.

Examples:

- **EECOM:** rearranged a purge schedule;
- **G&C/GNC:** allowed additional star marks based on RCS status;
- **NETWORK:** rescheduled longlines for earlier TV;
- **Flight Plan Support:** calculated attitudes/optics for photography and navigation;
- **GUIDO / CONTROL / FIDO:** developed no-communications and midcourse procedures later in the mission;
- **SPAN / technical teams:** received procedure/activity products for insertion into the timeline;
- **CAPCOM:** received flight-plan deletions/updates for crew transmission.

FAO therefore integrates the consequences of technical decisions into a coherent crew sequence.

---

# 4. Flight-plan changes are operational products

The postflight report records physical/operational handling of flight-plan changes.

Examples include:

- copies of deletions passed to FLIGHT, Mission Director, and CAPCOM;
- CSM Solo Book and flight-plan bootstrap pages marked with changes;
- explicit flight-plan updates sent to the crew;
- activities deleted to relieve a tight timeline.

### Simulation significance

A scenario need not formalize paper transfer, but the **flight plan must be a mutable operational object**.

A contingency changes:

- which tasks remain;
- which tasks are deleted;
- task timing;
- responsible crew member;
- prerequisites;
- communications windows;
- rest/eat periods;
- maneuver preparation.

---

# 5. Apollo 13 contingency timeline

After the accident, the original lunar mission timeline became irrelevant.

Mission Control constructed a new survival/return timeline containing activities such as:

- LM power-up;
- CSM power-down;
- docked alignment;
- free-return maneuver;
- LM power-down;
- PC+2 preparation/burn;
- crew rest/eat cycles;
- rendezvous-radar procedure update;
- LiOH procedure;
- LM power to CM;
- midcourse corrections;
- CSM reactivation;
- SM/LM jettison;
- entry.

The Mission Operations Report preserves the revised summary flight plan.

### Station implication

FAO should not simply show "next objective."

The role requires managing a timeline with:

- dependencies;
- durations;
- technical readiness;
- crew availability;
- communication/read-up time;
- rest constraints.

---

# 6. Crew workload and rest

Apollo 13's Flight Director report explicitly notes that Mission Control held noncritical procedural items until the correct crew member was awake/available.

FAO's timeline therefore interacts with:

- crew sleep;
- meals;
- workload;
- maneuver preparation;
- procedure read-up.

This is a real operational constraint, not a game stamina bar.

---

# 7. Procedures versus schedule

FAO and PROCEDURES overlap but have different responsibilities.

## PROCEDURES

How the ground/MCC/network/support procedure works.

## FAO

When mission/crew activities occur and how they fit together.

## CAPCOM

How approved crew-facing instructions are transmitted.

## FLIGHT

Which plan/procedure is approved and what has priority.

---

# 8. Mission-phase information requirements

A future FAO station needs, at minimum:

## Timeline

- GET
- current activity
- next activities
- duration
- responsible crew member
- prerequisites / constraints
- deleted/deferred activities

## Crew status

- awake/resting
- current spacecraft/location (CM/LM)
- current checklist/procedure
- pending read-up

## Mission events

- maneuver TIGs
- communications windows
- acquisition/loss of signal
- planned updates
- entry milestones

## Technical dependencies

- GO/NO-GO from relevant controllers
- required power/configuration state
- trajectory event status
- procedure readiness

Exact Apollo 13 CRT format remains unresolved.

---

# 9. Flight-plan support

The FAO report repeatedly refers to **Flight Plan Support** performing detailed calculation/preparation work.

Examples include:

- star/attitude checks;
- photography geometry;
- PTC/optics planning;
- revised activity preparation.

This is another front-room/backroom relationship that must be understood before deciding whether support is explicitly simulated.

---

# 10. Implementation status

## DOCUMENTED

- flight-plan coordination
- mission activity/deletion/update handling
- cross-discipline schedule integration
- crew workload/rest considerations
- contingency timeline rebuilding
- Flight Plan Support relationship

## PARTIAL

- exact products/displays used by FAO
- exact workflow for distributing updates

## UNRESOLVED

- exact Apollo 13 FAO console layout
- CRT display IDs
- DRK/MSK assignments
- Ground Timeline / Flight Plan display interaction
- exact support-room workflow
- exact voice loops

---

# 11. Research targets

1. Extract Apollo 13 Flight Director Log/flight-plan working sheets.
2. Identify FAO CRT/display products.
3. Identify Ground Timeline and Flight Plan TV channel use.
4. Locate FAO console handbook.
5. Reconstruct post-accident timeline-change workflow.
6. Map CAPCOM procedure read-ups to FAO timeline state.

## Primary source

- Apollo 13 Mission Operations Report, Appendix K — Flight Activities Officer:
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
