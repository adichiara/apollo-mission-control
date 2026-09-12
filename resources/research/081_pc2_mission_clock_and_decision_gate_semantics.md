# 081 — Apollo 13 PC+2 mission-clock and decision-gate semantics

Date: 2026-09-12  
Status: **SOURCE FINDINGS RETAINED / IMPLEMENTATION POLICY SUPERSEDED BY D-016**

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

## Superseded project policy

An earlier implementation decision used an explicit simulation pause at blocking controller gates. That policy was provisional and has been superseded by **D-016** after project review.

The source findings above remain valid. What changed is the simulator architecture chosen in response to them.

## Current policy

See `082_continuous_mission_clock_architecture.md`.

The current rule is:

- GET advances continuously while the session is running;
- controller decisions do not stop time;
- only an explicit game/session pause stops GET;
- nominal timed events whose prerequisites are absent are missed rather than automatically executed or replayed later.

This makes the mission clock independent of controller-decision state and establishes the engine as a continuously evolving simulation rather than a sequence of gated scenes.
