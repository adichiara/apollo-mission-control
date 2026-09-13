# Research Note 011 — Apollo Simulation Cases

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Apollo 13 premission simulation schedule

The Apollo 13 Mission Operations Report preserves a detailed premission MCC/MSFN support schedule.

Named simulation activities include:

- LOI
- LM activation/descent
- TLI
- ascent
- descent aborts
- launch aborts
- reentry
- lunar surface
- DOI
- TEI
- FIDO/BSE math-model work
- lunar impact
- combined CSM/LM ascent/descent
- network simulation
- tracking/data-flow and communications validation

### What this proves

NASA trained discrete mission phases and contingency classes repeatedly rather than treating "Apollo mission simulation" as one monolithic exercise.

### What it does not prove

The schedule does not tell us the malfunction set injected into each run.

Therefore these are scenario-family evidence, not finished scenarios.

## Simulation-design philosophy evidence

Harold Miller's retrospective NASA paper says:

- simulations were normally segmented by mission phase;
- they existed to develop teamwork and procedures;
- simulation designers inserted failures to exercise procedures, ground rules, and communications;
- Apollo simulations closed the command loop so real controller procedures could be exercised;
- simulated spacecraft data was routed through control-center systems rather than bypassing them.

This strongly supports the project's existing architecture.

## Program-alarm example

Miller recalls Jay Honeycutt running a lunar-landing simulation involving the computer failure light.

The better-known Apollo 11 historical accounts identify the case as a preflight program-alarm simulation that resulted in an unnecessary abort call and subsequent development of alarm-response guidance.

This is currently the strongest candidate for a specifically reconstructed historical SimSup case.

## Archive question

Miller states that simulations were documented more systematically after Mercury-Atlas 7 but that he did not know whether the material had survived.

This suggests an archival search target:

- JSC History Collection
- University of Houston-Clear Lake
- National Archives holdings
- individual flight-controller papers/collections

Search specifically for:

- simulation case sheets
- SimSup scripts
- malfunction lists
- post-simulation debriefs
- integrated simulation schedules
- Simulation Design Section material

## Sources

- https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- https://www.nasa.gov/wp-content/uploads/2025/08/millerhg-paper.pdf
