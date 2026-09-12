# Apollo 13 PC+2 — DPS shutdown command and physical response boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — crew STOP command and valve-response architecture established; exact LM-7 timing and controller confirmation trace remain unresolved**

## Question

Once the crew receives a valid PC+2 shutdown callout, what cockpit action actually commands descent-engine shutdown, and what physical response can the simulator represent without inventing a shutdown delay or chamber-pressure decay curve?

## Primary-source / contemporary LM evidence

### Apollo Operations Handbook — Lunar Module LM10 and subsequent, Volume I

Contemporary LMA790-3-LM material states that:

- the descent engine remains on until an engine-off discrete is initiated;
- either crew STOP pushbutton (panels 5 and 6) can initiate the engine-off command;
- the astronauts can manually command the engine on or off with the START/STOP pushbuttons;
- engine on/off commands are routed through the descent-engine control electronics to actuate the engine pilot valves;
- those commands hydraulically open or close the fuel and oxidizer shutoff valves.

Relevant pages in the searchable handbook include 2.1-19 and 2.1-35/37 family material.

### Configuration-continuity support

The same manual STOP-pushbutton architecture appears in earlier LM handbook material and in contemporary LM familiarization documentation. This brackets LM-7 with a consistent control architecture, but the exact Apollo 13 LM-7 handbook page has not been line-by-line recovered in this pass.

Therefore the implementation treats the STOP pushbutton → engine-off discrete → pilot/shutoff-valve closure path as sufficiently established for common LM control behavior, while retaining an LM-7-specific documentation caveat.

## What is supported

The following distinction is now defensible:

```text
crew presses ENGINE STOP
        ↓
engine-off command/discrete enters CES/DECA control path
        ↓
pilot valves commanded to engine-off state
        ↓
fuel/oxidizer shutoff valves commanded closed
        ↓
descent engine ceases thrusting
```

The crew action and physical response should remain separate simulation events even though the hardware response is causally linked.

## What is not yet supported precisely

The reviewed sources do not justify inventing:

- the exact milliseconds/seconds between STOP pushbutton press and zero thrust for LM-7;
- a PC+2-specific chamber-pressure tailoff curve;
- exact GQ6510P values during shutdown;
- an exact controller-visible engine-off discrete field;
- the exact delay from crew action to CONTROL confirmation;
- which crew member would have pressed STOP in the hypothetical ΔP case.

## Implementation consequence

Operational action:

- `press_engine_stop`

records the crew input and sets only the crew shutdown-command state.

Vehicle response:

- `apply_engine_off_response(...)`

is a distinct physical event that:

- sets `engine_running=False`;
- sets throttle phase to `off`;
- records that an engine-off discrete was received;
- records pilot-valve and propellant-shutoff-valve closure commands.

The helper deliberately does **not** alter chamber pressure or manufacture a telemetry confirmation. A later measurement update must provide any controller-observable confirmation.

## Architectural value

This closes a previously collapsed boundary:

`crew instruction/action ≠ physical engine response ≠ controller confirmation`

That distinction is necessary for failure scenarios in which:

- the crew issues the correct command but the engine does not respond;
- the engine shuts down but the ground has delayed/ambiguous confirmation;
- a valve/control failure produces a partial or abnormal response.

No such failure is invented here; the architecture merely permits them later when sourced.

## Sources

Primary/contemporary:

- Grumman / NASA, *Apollo Operations Handbook — Lunar Module LM10 and Subsequent, Volume I — Subsystems Data*, LMA790-3-LM, basic date 1 February 1970, searchable copy: https://ibiblio.org/apollo/Documents/LMA790-3-LM10-ApolloOperationsHandbookLunarModuleLM10AndSubsequent-Volume1-SubsystemsData-SearchableText.pdf
- Contemporary LM familiarization documentation, LMA790-2 family, for propulsion-control continuity.

Repository context:

- `resources/research/068_pc2_delta_p_ground_callout_shutdown_loop.md`
- `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`

## Research stop condition

The control/response boundary is sufficiently documented for implementation. Do not pursue exact shutdown transient timing or pressure decay unless a specific scenario requires it. The next useful step is to decide which **controller-observable confirmation** should close the loop, prioritizing already-documented GQ6510P chamber pressure or another directly sourced engine-thrusting indication if one can be recovered cheaply.
