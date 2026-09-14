# Deterministic Simulated Flight-Crew Actor

Status: **implemented generic actor model; scenario integration staged**

## Purpose

Represent the non-player spacecraft crew without turning the crew into an AI decision-maker or allowing CAPCOM transmission to mutate spacecraft state directly.

The reusable chain is:

`CAPCOM transmission -> crew receipt/acknowledgement -> supported crew action -> subsystem/physical response -> later observation/report`

Implementation:

`src/apollo_mission_control/simulated_crew.py`

## Generic boundary

A scenario/runtime supplies `CrewInstructionRule` records mapping:

- a supported CAPCOM action;
- a bounded/canned acknowledgement;
- a supported crew operational action;
- an allowlist of CAPCOM parameters forwarded into that action;
- provenance.

The actor records two independent stages:

1. `receive_instruction(...)`
2. `perform_supported_action(...)`

Neither method applies a vehicle/subsystem consequence.

## Timing rule

The actor does not invent crew-response latency.

The caller supplies authoritative GET for receipt and action. The actor checks temporal ordering only:

- receipt cannot precede transmission;
- action cannot precede receipt.

A scenario with source-backed timing may schedule those times. A scenario without source-backed timing may keep them explicit/manual in the validation harness.

## Information rule

Only parameters explicitly allowlisted by the rule are forwarded from a CAPCOM item to a crew operational action. This prevents arbitrary instruction metadata from becoming cockpit state.

## Deliberate exclusions

The actor does not:

- choose between competing procedures;
- infer a diagnosis;
- decide GO/NO-GO or abort/continue;
- generate unsourced delays;
- mutate propulsion/electrical/guidance state;
- assert that a commanded action physically succeeded;
- synthesize crew reports from hidden truth.

Those remain separate scenario, subsystem, observation, and controller layers.

## Integration direction

Apollo 13 PC+2 already has a source-bounded shutdown-call path whose existing helper keeps receipt, STOP command, and physical engine-off response separate. That path should migrate onto this actor while preserving its current evidence boundary.

Apollo 11 powered descent can reuse the same actor for source-bounded crew actions once the applicable CAPCOM/crew mappings and timing are established.
