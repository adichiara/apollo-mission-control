# Apollo 13 PC+2 — controller evidence after DPS restart

Date: 2026-09-12  
Status: **REVIEWED — no new restart-confirmation product justified; reuse common chamber-pressure observation path**

## Question

After an eligible premature-shutdown contingency physically restarts the DPS, does the current source base justify a special controller-visible `restart confirmed` indication, or should Mission Control continue to reason from the existing propulsion observations?

## Primary-source findings

### Apollo 13 PC+2 ground chamber-pressure rule

The Apollo 13 Flight Control Division *Mission Operations Report* treats thrust chamber pressure as a ground-observed PC+2 quantity and gives the ground shutdown criterion at approximately 85 psi.

This establishes that CONTROL had a chamber-pressure observation path during the burn. It does not define a separate post-restart confirmation flag or a restart-specific pressure threshold.

### LM-7-family measurement identity

The *Lunar Module 7, 8 & 9 Elementary Functional Diagrams* identify `GQ6510P` as `PRESS, THRUST CHAMBER`.

This is sufficient to keep a fresh post-restart chamber-pressure sample on the same measurement → telemetry/ground processing → CONTROL product path already implemented for nominal and shutdown-rule monitoring.

### Contemporary DPS behavior

The Apollo 10 LM-4 DPS flight-evaluation material records `GQ6510P` as the engine thrust-chamber-pressure measurement used in propulsion analysis. Contemporary LM operations documentation establishes that a successful engine-on command opens the pilot/propellant valve path and produces combustion/thrust.

These sources support treating a new post-restart chamber-pressure observation as relevant propulsion evidence. Apollo 10 timing/numerical traces are not imported into Apollo 13.

## Negative finding

This pass found no primary/contemporary support for adding any of the following to the Apollo 13 PC+2 model:

- a dedicated ground `RESTART CONFIRMED` discrete;
- a special restart-only CONTROL CRT field;
- a numerical chamber-pressure threshold meaning `restart successful`;
- a required crew restart-success callout;
- a fixed confirmation latency after pressing Engine Start or enabling command override.

Absence of evidence is not proof that no display/discrete existed somewhere in the ground system; it means the current model should not invent one.

## Implementation consequence

**No new runtime code is required.**

The existing architecture already carries the needed minimum evidence:

```text
physical successful restart
        ↓
new GQ6510P thrust-chamber-pressure observation (when supplied)
        ↓
common CONTROL product projection
        ↓
controller interpretation
```

Important rules:

- physical restart must not fabricate a fresh GQ6510P sample;
- a pre-restart pressure sample must not be reused as fresh evidence;
- the chamber-pressure value remains an observation, not an omniscient engine-state flag;
- the existing <=85 psi shutdown rule remains a shutdown criterion during engine operation, not a restart-success threshold.

## Architectural result

The same controller product should be reused across nominal burn monitoring, shutdown-rule evaluation, shutdown evidence, and post-restart observation. This avoids creating scenario-specific duplicate products that Apollo documentation does not support.

The simulation therefore retains:

`physical state ≠ measurement ≠ controller product ≠ controller conclusion`

## Sources

Primary / contemporary:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, PC+2 Mission Rules Review.
- *Lunar Module 7, 8 & 9 Elementary Functional Diagrams*, `GQ6510P — PRESS, THRUST CHAMBER`.
- TRW / NASA MSC, *Apollo 10 LM-4 Descent Propulsion System Final Flight Evaluation*, 8 August 1969, for contemporary `GQ6510P` instrumentation continuity only.
- Grumman / NASA, *Apollo Operations Handbook — Lunar Module LM10 and Subsequent, Volume I*, DPS functional description.

Repository context:

- `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`
- `resources/research/070_pc2_dps_shutdown_confirmation_evidence.md`
- `resources/research/071_pc2_dps_restart_physical_response.md`

## Stop condition

The restart-confirmation question is sufficiently bounded. Do not create a special restart-confirmation product unless a later primary source explicitly establishes one.

The next useful work should move away from DPS transient detail and toward the first-pass player-facing CONTROL information presentation using already-researched products, while preserving unresolved exact CRT routing where necessary.