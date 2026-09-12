# 081 — Apollo 13 PC+2 mission-clock and decision-gate semantics

Date: 2026-09-12  
Status: **IMPLEMENTATION BOUNDARY RESOLVED**

## Question

When a playable controller decision is pending, should Apollo Ground Elapsed Time (GET) stop, should later timed events continue past the unresolved decision, or should the simulator represent the hold explicitly as a simulation pause?

## Primary-source findings

### Apollo 13 Mission Operations Report — Flight Control Division, 28 April 1970

The PC+2 chronology is expressed in GET and treats the sequence as a timed operational timeline. Relevant points include:

- LM power-up begins around **78+12 GET**;
- the crew is specifically advised that the **PC+2 maneuver ignition time was not time critical**;
- the LM is at final burn attitude and a **GO** is given around **79:17 GET**;
- actual PC+2 ignition occurs at **79:27:38.30 GET**;
- LM power-down begins around **79+34 GET**.

The source therefore separates the readiness/GO event from TIG and also explicitly says TIG was not time-critical. It does **not** define a numerical allowable delay, nor does it say GET stops while a decision is pending.

Primary source:

- NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, NTRS document 19710010485.
- https://ntrs.nasa.gov/citations/19710010485

### Apollo GET definition / clock practice

NASA Apollo documentation defines mission events relative to Ground Elapsed Time from range zero. Apollo-era documentation also distinguishes the mission time reference from later planned clock updates; this is evidence that GET is a mission time coordinate, not a controller-decision semaphore.

Supporting NASA technical source:

- NASA Apollo 13 GNC retrospective technical paper, NTRS 20090026451: GET starts at the integral second before liftoff/range zero.
- https://ntrs.nasa.gov/citations/20090026451

## What the sources do **not** establish

The reviewed sources do not establish:

- that Mission Control stopped or froze GET for a pending GO/NO-GO decision;
- an Apollo simulator policy for pausing player deliberation;
- a numerical amount by which PC+2 could be delayed without retargeting;
- that downstream events should be applied retroactively after a delayed player decision;
- a generic rule that every controller decision should pause a simulation.

The statement that PC+2 ignition time was not time critical must therefore **not** be converted into an invented delay tolerance.

## Project decision

For the first playable deterministic PC+2 slice, a blocking controller decision gate is represented as an **explicit simulation pause**.

This means:

1. historical/source-backed GET advances only while session status is `RUNNING`;
2. reaching the final FLIGHT GO/NO-GO gate sets session status to `PAUSED`;
3. the pause carries an explicit machine-readable reason (`decision_gate:flight_go`);
4. the player may continue to submit readiness information and make the required decision while paused;
5. manual resume cannot bypass an unresolved decision gate;
6. FLIGHT `GO` clears the gate and automatically returns the session to `RUNNING`;
7. `NO-GO` keeps the gate and pause active;
8. later historical events are not silently applied while the gate is unresolved.

This is a **simulation/playability policy**, not a claim that historical Apollo GET stopped.

## Why this is the minimum-safe policy

Allowing GET to continue while the gate blocks event execution immediately creates a second unresolved question: what should happen when nominal timed events such as P40, ullage, and TIG become overdue before FLIGHT clears the gate?

The primary sources support neither automatic retroactive execution nor a specific retiming rule. Explicit simulation pause therefore preserves the source-backed nominal sequence without inventing a delay model.

A later realtime/nonnominal timing model may replace this with separate wall-clock, mission-time, and event-eligibility clocks, but that should be introduced only when gameplay actually requires delayed execution rather than deliberation pause.

## Implementation

- `src/apollo_mission_control/pc2_session.py`
  - adds `pause_reason`;
  - final GO poll opens an explicit decision pause;
  - manual resume is blocked while a gate is pending;
  - GO automatically resumes the decision pause;
  - NO-GO remains paused.
- `src/apollo_mission_control/web_app.py`
  - exposes `pause_reason` through status responses.
- `tests/test_pc2_session.py`
- `tests/test_web_app.py`

## Next boundary

With clock/gate semantics explicit, the next integration task is browser-side rejoin persistence followed by a runnable HTTP/mobile smoke test and then one already-modeled nonnominal branch through the same session/API path.
