# Research Note 023 — Apollo 13 Simulator Discrepancy Reports

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Source

A small collection of contemporaneous **Simulation Discrepancy Reports** survives in the Virtual AGC document library:

https://www.ibiblio.org/apollo/Documents/apollo_13_simulator_discrepencies.pdf

The reports reference **LUM 131 Rev. 1**, the Apollo 13 LM guidance-computer software configuration.

## Why this source matters

This is not a retrospective description of simulation.

It records actual discrepancies discovered while testing/simulating the Apollo 13 guidance software and hardware/simulator environment.

This gives the project evidence for:

- how simulator test runs were identified;
- what effects were being exercised;
- what simulator/program behavior was considered discrepant;
- how NASA/contractor teams investigated those discrepancies.

## Example: hardware restart test

One discrepancy report describes a run intended to test the effects of a **hardware restart** on the loaded/closed-loop primary guidance system.

Observed effects included changes to:

- navigation-update frequency;
- P32 data/computations up to trial solution;
- temporary control reversal in a rate-command mode after restart;
- other navigation/display consequences still under investigation.

The report then recommends additional fixed-memory load verification.

### Simulation significance

A "computer restart" should not be authored as one simple boolean fault with a canned alarm.

The actual software/hardware state transition can affect:

- guidance computation;
- navigation state;
- control response;
- display behavior;
- recovery/restart verification.

This is precisely the kind of failure dependency the scenario engine needs to preserve.

## Configuration-testing detail

The reports discuss:

- PAC/LGC loading;
- fixed-memory bank content;
- verification tables;
- checksums;
- restart behavior after load changes.

This reinforces the project rule that simulator software configuration must be treated as explicit mission configuration.

## Evidence status

The eight-page scan is difficult to OCR cleanly.

Therefore only clearly legible findings are being recorded at this stage.

Do not turn individual discrepancy reports into playable scenarios until:

- the report is legible enough to define the setup;
- the expected simulator behavior is understood;
- the mission phase and player-visible consequences can be reconstructed.

## Research value

These reports create a new scenario/source class:

**documented simulator discrepancy/test cases**

They differ from:

- Flight Director integrated simulations;
- SimSup malfunction cases;
- actual mission anomalies.

All three may be useful, but their provenance and purpose are different.

## Next steps

1. Transcribe the discrepancy reports from higher-quality page images if available.
2. Identify every test ID/date.
3. Map each report to LUMINARY 131 Rev. 1 program behavior.
4. Determine which were software defects, simulator defects, or expected spacecraft-computer behavior.
5. Cross-reference Apollo 13 FSRR/program notes and postflight AGC report.
