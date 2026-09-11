# Research Note 025 — Apollo 13 FSRR / FMES Test Evidence

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Sources

Apollo 13 Flight Software Readiness Review material:

- FSRR minutes:
  https://www.ibiblio.org/apollo/Documents/apollo_13_fsrr_minutes.pdf
- FMES test material:
  https://www.ibiblio.org/apollo/Documents/apollo_13_fmes_tests.pdf

These documents concern the H-2 / Apollo 13 LM software/simulator configuration around **LUMINARY 131**.

## FMES/FCI functional architecture

The FSRR material shows a closed-loop engineering/simulation chain involving:

- flight table
- IMU
- Abort Sensor Assembly
- rate gyro assembly
- LGC / AEA
- accelerations
- radar
- attitude
- simulated cockpit controls:
  - ACA
  - TTCA
  - DSKY
  - DEDA
  - switches/displays
- flight-type hardware:
  - ATCA
  - CWEA
  - DECA
  - GDA
  - throttle servo
  - RCS jet simulator
- FMES math models:
  - vehicle dynamics
  - radar
  - accelerometers
  - propulsion
  - RCS/engine response

### Project significance

NASA/Grumman were validating Apollo 13 guidance software against a closed-loop hardware/simulator model, not merely checking isolated program outputs.

This gives us a historically grounded subsystem boundary for the LM simulation.

## Documented nominal mission tests

The FSRR lists tests including:

- CSM circular-orbit guidance cases (P52, P76, P20);
- PDI auto landing (P63/P64/P65-66);
- PDI rate-of-descent landing (P63/P64/P66);
- automatic P66 with ROD;
- ascent through MCC-1 using P12, P20, P32, P33, P34, P35, P41;
- auto landing using P27;
- landing-point-designator / ROD landing;
- deorbit using P30/P42.

## Documented software checks

Explicit checks include:

- touchdown-loss / TLOSS behavior in auto landing;
- TLOSS behavior in ROD landing;
- powered ascent;
- early and late aborts;
- restarts during:
  - auto landing;
  - ROD landing;
  - ascent through MCC-1;
- automatic P66;
- P22;
- early/late abort cases.

## Documented redline / boundary tests

The FSRR identifies tests for:

- PDI with landing radar locked in position 1;
- PDI with landing radar locked in position 2;
- landing-radar reasonableness check;
- landing-radar capability errors during auto landing;
- P20 rendezvous-radar boresight error;
- slow engine start;
- transients in P63, P12, P40, P42.

These are highly valuable test-case families because they are tied directly to Apollo 13's guidance/simulator configuration.

## Duty-cycle testing

The FSRR also records LGC duty-cycle effects of operational actions.

Examples reported include increased duty cycle from:

- monitor activity;
- DSKY verb/noun input;
- PRO;
- KEY REL.

And decreased duty cycle from configurations such as:

- ATT HOLD;
- DAP OFF;
- landing-radar no-read;
- selected verbs/modes;
- manual throttle.

This is evidence that operational workload could influence computer computational margin.

## Simulator/software discrepancy summary

For the period roughly January 6 to March 10, 1970, the FSRR summarizes discrepancies in categories including:

- software;
- simulator;
- hardware.

It reports both closed and open items.

The conclusion states that a successful nominal or abort **LM-7 mission could be flown with the tested software using appropriate workaround procedures**.

That is an important historical point:

> readiness did not mean “zero known anomalies.” It meant known anomalies were understood and acceptable/workaround-able.

## Listed problem areas

The FSRR summary includes problem areas such as:

- P66 horizontal-velocity displays;
- TLOSS effects in P63/P64;
- alarm behavior;
- hardware restarts affecting rendezvous-radar/P20 updates;
- X-axis override altitude quantization;
- step in throttle recovery;
- AZBIAS polarity error.

Some were accepted because symptoms were not unsafe or workarounds existed.

## Scenario / simulation consequence

These documents give us three different uses:

1. **vehicle/software model validation** — how the LM guidance simulation should behave;
2. **known Apollo 13 configuration defects** — mission-profile quirks that may need preservation;
3. **test-case families** — documented cases that can later become research-backed training/simulation scenarios if enough detail is recovered.

Do not automatically turn every FSRR test into a Mission Control scenario; many were engineering/software qualification tests rather than integrated flight-controller simulations.

## Research targets

1. Transcribe each test case/run ID and expected/observed outcome.
2. Cross-reference FSRR issues with:
   - Apollo 13 program notes;
   - postflight AGC report;
   - Simulation Discrepancy Reports.
3. Determine which anomalies affected telemetry/displays visible to Mission Control.
4. Determine which issues were fixed before flight versus flown with workaround.
5. Use FMES architecture to constrain LM math-model implementation.

## Sources

- https://www.ibiblio.org/apollo/Documents/apollo_13_fsrr_minutes.pdf
- https://www.ibiblio.org/apollo/Documents/apollo_13_fmes_tests.pdf
