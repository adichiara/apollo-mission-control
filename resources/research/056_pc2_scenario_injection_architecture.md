# Apollo 13 PC+2 — scenario/failure injection architecture

Date: 2026-09-12  
Status: **IMPLEMENTATION-READY ARCHITECTURE NOTE — generic injection semantics are justified; no undocumented Apollo SimSup command syntax is reconstructed.**

## Purpose

Define the smallest scenario-injection mechanism needed to create nonnominal PC+2 tests without scripting diagnoses, controller conclusions, or outcomes.

This note addresses a software architecture question, not a claim about the exact Apollo Simulation Supervisor console/interface.

## Primary-source evidence

### 1. Apollo 13 simulator discrepancy report — hardware restart case

A contemporaneous Simulator Discrepancy Report for LUM 131 Rev. 8, test H20T-7.2 #1 dated 27 January 1970, states that the run tested the effects of a **hardware restart** on the closed-loop primary system.

The report records multiple resulting effects, including:

- drastically reduced P20 navigation-update frequency;
- changed P32 input data/resulting computations up to a trial solution;
- a temporary control reversal in rate-command mode with pitch ACA out of detent, subsequently corrected;
- additional navigation/display effects still under investigation.

The important implementation implication is not the exact restart behavior itself. It is that a simulated initiating condition propagated into multiple dependent onboard/control/display consequences. The project should therefore inject conditions at their modeled source and allow subsystem, telemetry, ground-processing, and controller-product layers to carry the consequences.

Source: Apollo 13 Simulator Discrepancy Reports, `LM-LUM-31`, LUM 131 Rev. 8, 27 Jan 1970. Public scan: https://www.ibiblio.org/apollo/Documents/apollo_13_simulator_discrepencies.pdf

### 2. Apollo 13 Mission Operations Report

The Apollo 13 Mission Operations Report documents extensive premission simulation activity involving CMS, LMS, math-model, network, MCC/MSFN validation, abort, descent, ascent, reentry, and other mission-phase exercises.

For the selected PC+2 slice, the same report supplies the actual flight shutdown criteria and controller responsibilities already implemented in notes 049–055.

This supports using the historical rule/product path to evaluate injected conditions rather than putting a scenario-authored `abort`, `burn_bad`, or controller diagnosis into the simulation state.

## Architecture decision

A scenario injection is a **change to an authoritative modeled condition or observation source at a stated simulation time**.

It is not:

- a controller diagnosis;
- a FLIGHT decision;
- a shutdown command;
- a precomputed rule result;
- an automatically displayed message;
- a claim that the exact injection command existed on an Apollo SimSup console.

Conceptually:

```text
scenario injection
      ↓
authoritative/modelled state
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

Each injection should carry:

- stable `injection_id`;
- GET execution time;
- explicit target parameter;
- replacement value;
- evidence classification;
- provenance/note explaining whether the injected value is historical, source-bounded, or synthetic test data.

The first implementation supports only an explicit whitelist of modeled state fields. It must reject arbitrary object paths so scenario files cannot silently mutate unrelated internal state.

## Evidence classes

### `historical_event`

Value/time are directly supported as an actual historical event.

### `documented_simulation_case`

Injection is supported by a reconstructable historical simulation case.

### `source_bounded_test`

The affected parameter and decision threshold are historical, but the chosen test value/time are synthetic and exist only to exercise the implementation.

Example: setting modeled chamber pressure to 80 psi to test the documented 85-psi ground criterion. This does **not** assert that Apollo 13 experienced an 80-psi PC+2 failure.

### `project_hypothetical`

Reserved for future explicitly approved hypothetical scenarios. Not used by the initial PC+2 nonnominal validation set.

## First whitelisted PC+2 targets

The generic mechanism initially exposes only observations/state already modeled and researched:

- `dps_chamber_pressure_psi`;
- `engine_gimbal_warning`;
- `ces_dc_failure`;
- `iss_warning`;
- `program_alarm`;
- `lgc_warning`;
- `inverter_warning`.

This list is an implementation boundary, not a claim that these were the only failures Apollo simulations could inject.

## Timing semantics

Injection times are simulation GET values.

If a scheduled historical event and an injection share the exact same GET, the prototype processes the historical event first and the injected condition second. This is a deterministic software ordering rule only; it is not asserted as historical SimSup behavior.

## No automatic diagnosis or action

After an injection:

- controller products are regenerated from the changed state;
- the independent rule evaluator may report a criterion `TRIGGERED`;
- `PC2State.shutdown_rule_triggers` remains untouched by the injection mechanism;
- no engine cutoff, abort, GO/NO-GO, or CAPCOM call is generated automatically.

Those later actions belong to controller/player logic and subsequent simulation layers.

## First validation use

The existing low-chamber-pressure boundary test can now be expressed as a timed source-bounded injection rather than direct test mutation:

1. run the nominal PC+2 event sequence to a selected burn time;
2. inject a synthetic chamber-pressure observation of 80 psi;
3. project CONTROL products;
4. evaluate the documented ground chamber-pressure rule;
5. verify that the rule triggers while no automatic shutdown command is created.

The test time/value remain clearly marked as synthetic.

## Deferred work

Do not yet implement:

- arbitrary nested-path mutation;
- duration/recovery curves;
- stochastic failure models;
- automatic causal propagation not supported by subsystem equations;
- historical SimSup operator UI;
- undocumented malfunction codes;
- compound narrative scenarios.

Add these only when a source-backed scenario or subsystem model requires them.

## Next step

After this generic layer is working, the next high-value branch is to model another PC+2 observation path whose underlying measurement/state can be defensibly perturbed—likely inlet pressure, fuel/oxidizer differential pressure, onboard thrust indication, or inverter-after-switch state—then express its nonnominal case through this injection interface rather than direct fixture editing.
