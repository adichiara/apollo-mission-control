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

## Apollo 11 simulation evidence — keep distinct

Two source threads must not be treated as one proven event.

### Harold Miller / Jay Honeycutt recollection

Miller recalls Jay Honeycutt running a lunar-landing simulation involving the **computer failure light**. That recollection establishes a Honeycutt-run computer-indication case, but the current source does not establish that it was the same run as the later-described 1201/1202 program-alarm exercise.

### Richard Koos / Gene Kranz program-alarm account

Separate NASA oral-history evidence identifies a final Apollo 11 landing simulation in which SimSup **Richard (Dick) Koos** inserted a **1201/1202 program alarm**. Steve Bales called for an abort; the debrief concluded that the team should not have aborted solely on that alarm, and follow-up training/rule development addressed program-alarm response.

Kranz's oral history independently describes the same training lesson: the team aborted for computer program alarms, Koos challenged the decision in debrief, and Bales was tasked to develop rules for handling the alarms.

### Evidence boundary

The repository therefore treats these as **distinct evidence threads unless a stronger source explicitly links them**:

1. Honeycutt / computer-failure-light recollection;
2. Koos / program-alarm simulation and abort/debrief sequence.

Do not infer identical indications, identical scenario scripting, or a shared run merely because both concern the LM computer.

The Koos program-alarm case is the stronger candidate for a specifically reconstructed historical SimSup case because its operational consequence and debrief lesson are more directly documented. Exact scripting, timing, and telemetry-injection details still require stronger source support before reconstruction.

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

- Apollo 13 Mission Operations Report: https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- Harold G. Miller, *The Early Days of Simulation and Operations*: https://www.nasa.gov/wp-content/uploads/2025/08/millerhg-paper.pdf
- Richard H. Koos NASA Oral History, 24 August 2023: https://www.nasa.gov/wp-content/uploads/2025/08/koosrh-8-24-23.pdf
- Eugene F. Kranz NASA Oral History, 8 January 1999: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/KranzEF/EFK_1-8-99.pdf
