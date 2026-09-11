# Apollo 13 FLIGHT Station Specification

Status: **research specification — workflow strong, console/display details incomplete**

Purpose: reconstruct the Apollo 13 Flight Director position without turning FLIGHT into an omniscient game-master console.

---

## 1. Position

**Call sign:** FLIGHT  
**Position:** Flight Director

### Documented responsibility

Apollo Mission Control documentation assigns the Flight Director responsibility for MOCR decisions and actions concerning:

- vehicle systems;
- vehicle dynamics;
- MCC/MSFN operations.

The Flight Director is therefore the operational decision authority inside the control room, but the discipline controllers retain technical ownership of their systems.

---

# 2. FLIGHT does not replace specialist controllers

The Apollo 13 Flight Director loop repeatedly shows the operating pattern:

```text
controller detects / analyzes condition
        ↓
controller calls FLIGHT
        ↓
FLIGHT asks for status / recommendation / consequence
        ↓
other disciplines may be polled
        ↓
FLIGHT decides / coordinates
        ↓
CAPCOM or the responsible ground path executes the resulting action
```

FLIGHT frequently asks questions such as:

- status?
- recommendation?
- can we do this?
- what is the consequence?
- are we GO?
- how long do we have?
- who owns the next action?

The role is therefore primarily **integration, prioritization, authority, and timing**.

---

# 3. Flight Director loop

The Flight Director loop is the central front-room coordination channel.

Surviving Apollo 13 audio shows FLIGHT interacting directly with:

- EECOM
- GNC
- GUIDO
- FIDO
- RETRO
- TELMU
- CONTROL
- INCO
- PROCEDURES
- FAO
- NETWORK
- CAPCOM
- BOOSTER
- SURGEON / other support positions as required

Controllers generally call FLIGHT by discipline name and receive short directed exchanges.

### Simulation significance

A good FLIGHT player must:

- listen selectively;
- decide which problem is currently controlling;
- request missing information;
- distinguish diagnosis from recommendation;
- avoid allowing one discipline to optimize locally at the expense of the mission;
- maintain the decision sequence under incomplete/contradictory data.

No numerical “leadership score” is required.

---

# 4. Apollo 13 demonstrates changing mission priorities

The Flight Director's Report describes the mission shifting from nominal lunar landing toward:

1. stabilizing the CSM/LM systems situation;
2. regaining a viable Earth-return trajectory;
3. determining whether LM consumables could support that return;
4. executing the PC+2 maneuver;
5. developing nonstandard survival/reentry procedures;
6. reactivating the CM and preparing for entry.

FLIGHT therefore does not operate from one static objective list.

The controlling problem can shift among:

- EECOM/TELMU consumables;
- FIDO/RETRO trajectory;
- GUIDO alignment/computer state;
- CONTROL propulsion;
- INCO communications;
- PROCEDURES/FAO timeline.

---

# 5. Mission rules and judgment

Apollo flight rules were intended to predefine many decisions, but Apollo 13 required situations not fully captured by nominal rules.

FLIGHT must therefore have access to:

- mission rules;
- mission phase;
- controller recommendations;
- contingency procedures;
- current vehicle/crew capability;
- time-critical constraints.

The simulator should not automatically resolve a rule for FLIGHT.

A controller may cite the relevant rule or technical rationale; FLIGHT decides whether/how it applies to the current real-time situation.

---

# 6. Polling

Apollo Flight Directors routinely poll the room for GO/NO-GO or status before major events.

This is not merely ceremonial.

A poll:

- forces each discipline to own its readiness decision;
- exposes dissent quickly;
- creates a clear commitment point;
- gives FLIGHT a compact system-level picture.

The simulation should support this naturally through voice communication rather than through a software checklist that automatically collects GO votes.

A digital readiness summary may exist if historically documented for a given event, but the verbal poll itself is operational behavior.

---

# 7. CAPCOM relationship

FLIGHT does not normally speak directly to the crew.

After Mission Control reaches a decision, FLIGHT commonly directs CAPCOM to transmit:

- procedures;
- switch/configuration changes;
- maneuver instructions;
- status;
- requests for crew observations.

This preserves a deliberate boundary between:

- internal engineering discussion;
- approved crew-facing communication.

### Simulation significance

If a player acting as EECOM believes a switch should be moved, the normal path is not:

> EECOM speaks directly to the astronauts.

It is:

```text
EECOM → FLIGHT → CAPCOM → crew
```

unless a specific historical exception applies.

---

# 8. Conflict / cross-discipline arbitration

Apollo 13 repeatedly required choices in which one discipline's preferred action affected another.

Examples include:

- trajectory return time versus LM consumable lifetime;
- communications capability versus electrical load;
- guidance-system power versus consumables;
- thermal comfort versus water/electrical usage;
- RCS consumption versus attitude-control precision.

FLIGHT's station must expose the **recommendations and consequences**, not solve those tradeoffs automatically.

---

# 9. Information requirements

A historically grounded FLIGHT experience likely requires access to:

## Mission state

- GET / mission phase
- major planned events
- major active contingency plan
- current crew/vehicle configuration

## Controller/team status

- current calls/recommendations
- GO/NO-GO readiness
- unresolved technical questions
- action ownership

## Mission-level products

- flight plan/timeline
- mission rules
- maneuver/entry summary products
- consumables summary where historically available
- recovery/network status where required

### Important limitation

The exact Apollo 13 FLIGHT CRT display set remains unresolved.

Do not create a modern consolidated dashboard showing every subsystem simply because FLIGHT needs mission awareness.

Historically, much of FLIGHT's awareness came through controller calls and selected group/console displays.

---

# 10. Instructor/SimSup separation

FLIGHT is **not** SimSup.

FLIGHT should never receive:

- hidden physical truth;
- scenario trigger state;
- future failure schedule;
- “correct answer” information.

Those belong exclusively to the simulator/instructor layer.

---

# 11. Implementation status

## DOCUMENTED

- decision authority
- Flight Director loop coordination
- controller polling
- CAPCOM as crew communication path
- mission-priority integration
- discipline recommendation structure
- mission-rule use

## PARTIAL

- mission-level display/product use
- exact information shown directly at the Flight console

## UNRESOLVED

- exact Apollo 13 FLIGHT console layout
- exact CRT display IDs
- DRK/MSK configuration
- event/status indicators
- exact group-display dependence
- exact voice-panel loop selection

---

# 12. Research targets

1. Extract Apollo 13 Flight Director Log for console products and working documents.
2. Identify FLIGHT console CRT format assignments.
3. Map major-event polls from restored Flight Director loop audio.
4. Identify exact Flight Director voice-panel capabilities.
5. Determine which group displays FLIGHT routinely relied upon.

## Sources

- Apollo 13 Mission Operations Report, Flight Director's Report:
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- Apollo 13 restored Mission Control audio:
  https://apolloinrealtime.org/13/
- Apollo 13 Flight Director Logs index:
  https://apollojournals.org/afj/ap13fj/a13-documents.html
