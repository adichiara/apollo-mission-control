# Apollo 13 PC+2 — scenario/failure injection architecture

Date: 2026-09-12  
Status: **IMPLEMENTED MINIMUM ARCHITECTURE — generic timed source-state injection is working for the first researched analog path; no undocumented Apollo SimSup command syntax is reconstructed.**

## Purpose

Define the smallest scenario-injection mechanism needed to create nonnominal PC+2 tests without scripting diagnoses, controller conclusions, or outcomes.

This is a software architecture contract, not a claim about the exact Apollo Simulation Supervisor console/interface.

## Primary-source evidence

### Apollo 13 simulator discrepancy report — hardware restart case

A contemporaneous Simulator Discrepancy Report for LUM 131 Rev. 8, test H20T-7.2 #1 dated 27 January 1970, states that the run tested the effects of a **hardware restart** on the closed-loop primary system.

The report records multiple dependent effects:

- drastically reduced P20 navigation-update frequency;
- changed P32 input data/resulting computations up to a trial solution;
- temporary control reversal in rate-command mode with pitch ACA out of detent, subsequently corrected;
- additional navigation/display effects still under investigation.

This is strong primary evidence for the architectural principle that an initiating simulator condition can propagate into several dependent onboard/control/display consequences rather than existing as one canned diagnosis.

Source: Apollo 13 Simulator Discrepancy Reports, `LM-LUM-31`, LUM 131 Rev. 8, 27 Jan 1970. Public scan: https://www.ibiblio.org/apollo/Documents/apollo_13_simulator_discrepencies.pdf

### Apollo 13 Mission Operations Report

The Mission Operations Report documents extensive premission simulation activity involving CMS, LMS, math-model, network, MCC/MSFN validation, abort, descent, ascent, reentry, and other mission-phase exercises. For PC+2 it also supplies the actual-flight shutdown criteria and controller responsibilities already implemented in research notes 049–055.

The project therefore evaluates injected conditions through the existing information/rule path rather than storing scenario-authored `abort`, `burn_bad`, or controller-diagnosis variables.

## Architecture decision

A scenario injection is a **change to a modeled source condition at a stated simulation time**.

It is not:

- a controller diagnosis;
- a FLIGHT decision;
- a shutdown command;
- a precomputed rule result;
- an automatically displayed message;
- a reconstruction of historical SimSup command syntax.

Conceptually:

```text
scenario injection
      ↓
authoritative/modelled source state
      ↓
instrumentation / onboard representation
      ↓
telemetry / ground processing
      ↓
station projection
      ↓
controller interpretation / rule application
      ↓
FLIGHT/CAPCOM/crew action
```

## Minimum injection contract

Each injection carries:

- stable `injection_id`;
- GET execution time;
- explicit target parameter;
- replacement value;
- evidence classification;
- provenance explaining whether the value is historical, source-bounded, or synthetic test data.

The implementation uses an explicit target whitelist. Arbitrary object-path mutation is rejected.

## Evidence classes

- `historical_event` — value/time directly support an actual historical event.
- `documented_simulation_case` — injection is supported by a reconstructable historical simulation case.
- `source_bounded_test` — affected parameter/rule is historical, but chosen test value/time are synthetic.
- `project_hypothetical` — reserved for future explicitly approved hypothetical scenarios.

The current nonnominal PC+2 test uses `source_bounded_test`: 80 psi is deliberately below the documented 85-psi ground criterion, but is **not** asserted as an Apollo 13 failure value.

## First whitelisted PC+2 target

The initial executable whitelist contains only:

- `dps_chamber_pressure_psi`.

This is intentionally narrower than the set of already projected warning states. Chamber pressure is the first path for which the project has both a researched LM-7-family measurement identity (`GQ6510P`) and a documented PC+2 ground threshold.

Warnings currently stored as nominal fixture values are **not yet** exposed through the generic injection layer. They should migrate to explicit runtime source state before becoming injection targets. This avoids mutating nominal historical fixture data to simulate failures.

Future candidates include engine-gimbal warning, CES DC failure, ISS warning/program alarm, LGC warning, and inverter-warning state after their runtime-source representations are separated from fixture constants.

## Timing semantics

Injection times are simulation GET values. If a scheduled historical event and an injection share the exact GET, the prototype applies the historical event first and the injection second. This is a deterministic software convention only, not historical SimSup behavior.

## No automatic diagnosis or action

After an injection:

- controller products are regenerated from changed state;
- the independent rule evaluator may return `TRIGGERED`;
- `PC2State.shutdown_rule_triggers` remains untouched;
- no engine cutoff, abort, GO/NO-GO, or CAPCOM call is generated automatically.

## First validation use

The low-chamber-pressure boundary path is now exercised as a timed injection:

1. run the PC+2 timeline to 79:29 GET;
2. inject synthetic chamber pressure = 80 psi;
3. project CONTROL products;
4. evaluate the documented 85-psi ground criterion;
5. verify the rule triggers while the engine remains running and no automatic shutdown/abort state is created.

Both the injection time and pressure are synthetic implementation-test choices.

## Deferred work

Do not yet implement:

- arbitrary nested-path mutation;
- duration/recovery curves;
- stochastic failure models;
- automatic causal propagation without sourced subsystem equations;
- historical SimSup operator UI;
- undocumented malfunction codes;
- compound narrative scenarios.

## Next step

Research and model the next PC+2 observation path whose runtime source state can be defensibly represented and perturbed—preferably inlet pressure, fuel/oxidizer differential pressure, onboard thrust indication, or inverter-after-switch state. Then add it to the injection whitelist and exercise its rule path without direct fixture editing.
