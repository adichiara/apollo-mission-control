# Apollo 13 PC+2 — DPS restart physical response boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — restartable engine-on path established; exact Apollo 13 restart transient remains unresolved**

## Question

After an unexplained premature DPS shutdown has been classified as restart-eligible and the crew performs the pre-briefed restart sequence, what physical response can the simulator represent without assuming that command execution automatically succeeds?

## Primary / contemporary evidence

### Apollo 13 Mission Operations Report

The PC+2 Mission Rules Review states that an early shutdown for reasons other than the listed shutdown criteria was to be restarted by ullaging, depressing Engine Start, and turning on Descent Engine Command Override.

This establishes that a successful DPS restart was an intended contingency for PC+2, but does not define its transient or guarantee success.

### Apollo 13 mission transcript

The contemporaneous air-ground exchange gives the same crew-facing restart sequence for an in-burn stop associated with flashing Noun 97: PRO, ullage, Engine Start, Descent Engine Override on.

### Apollo Operations Handbook — Lunar Module LM10 and Subsequent, Volume I

Contemporary LMA790-3-LM subsystem documentation states that:

- the descent engine can be shut down and restarted within operational limitations;
- manual start is accomplished by arming the descent engine and pressing START;
- an engine-on command causes the four pilot valves to open;
- actuation fuel then opens the fuel and oxidizer propellant shutoff valves;
- opening those valves routes propellant to the injector/combustion chamber;
- the Descent Engine Command Override provides an alternate voltage path to keep the engine firing if DECA power fails.

The handbook therefore supports the physical chain:

```text
eligible restart + crew restart sequence
        ↓
engine-on command
        ↓
pilot valves commanded open
        ↓
propellant shutoff valves commanded open
        ↓
propellant flow / combustion
        ↓
engine thrusting
```

## What is not supported precisely

The reviewed sources do not justify inventing:

- the exact command-to-reignition delay for LM-7;
- the exact thrust level immediately following this contingency restart;
- a chamber-pressure rise curve;
- exact GQ6510P restart values;
- restart success probability;
- a guaranteed successful response merely because the crew performed the procedure.

## Implementation consequence

A new explicit physical-response helper, `apply_pc2_restart_response(...)`, may set the engine physically running only when:

1. the restart decision is `RESTART_ELIGIBLE`; and
2. the modeled restart action sequence has been completed.

The crew actions themselves still do not start the engine.

On a successful physical-response event the model records:

- engine-on command received;
- pilot valves commanded open;
- propellant shutoff valves commanded open;
- `engine_running=True`.

Because the exact restart thrust command is unresolved, the state uses the explicit internal label `restart_thrust_unspecified` rather than aliasing the response to minimum, 40-percent, or maximum thrust.

No fresh chamber-pressure observation is generated. Controller confirmation remains an independent telemetry/communication problem.

## Architectural value

This preserves four separable concepts:

`restart eligibility ≠ crew procedure ≠ physical restart response ≠ controller confirmation`

That structure permits future sourced cases in which a crew executes the correct restart procedure but the engine fails to restart, or restarts abnormally, without changing the historical rule model.

## Sources

Primary / contemporary:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, PC+2 Mission Rules Review.
- NASA Apollo 13 mission commentary / air-ground transcript, approximately 76:31–76:37 GET.
- Grumman / NASA, *Apollo Operations Handbook — Lunar Module LM10 and Subsequent, Volume I — Subsystems Data*, LMA790-3-LM, 1 February 1970, DPS interface and functional-description sections.

Repository context:

- `resources/research/067_pc2_premature_shutdown_restart_branch.md`
- `resources/research/069_pc2_dps_shutdown_command_and_physical_response.md`
- `resources/research/070_pc2_dps_shutdown_confirmation_evidence.md`

## Research stop condition

The restart command/physical-response boundary is sufficiently documented for the current simulation architecture. Do not pursue a detailed restart transient unless a later scenario requires one.

The next useful PC+2 dependency should be selected from unresolved controller-facing behavior rather than deeper propulsion transients.