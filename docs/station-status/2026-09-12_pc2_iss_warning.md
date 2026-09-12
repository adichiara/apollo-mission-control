# Station Research Status Addendum — PC+2 ISS Warning Path

Date: 2026-09-12  
Parent: `docs/STATION_RESEARCH_STATUS.md`

This addendum records the scenario-focused station-status change without destructively rewriting the large master status file through the current connector window.

## GUIDO

**Maturity remains B — Strong workflow.**

New evidence:

- Apollo 13 PC+2 Mission Rules require an inertial-reference / ISS warning **plus** computer program alarm as a shutdown criterion.
- Contemporary LM GN&CS handbook evidence shows **ISS WARNING SIGNAL** and **LGC WARNING SIGNAL** as distinct warning outputs with a path to the Instrumentation Subsystem.
- Contemporary LUMINARY functional-description material likewise treats ISS and LGC warning indications separately and describes ISS warning as being under LGC program control.

Implementation consequence:

- `pg_ns.iss.warning` is now a distinct GUIDO controller product with `onboard/telemetry` provenance.
- The ISS-warning + program-alarm rule is now evaluable as a conjunction and has the project's first source-backed nonnominal rule-path test.

Remaining gaps preventing maturity A:

- exact Apollo 13 LM-7 telemetry word/channel for ISS warning;
- exact ground-processing route;
- exact GUIDO CRT/MSK field and display placement during PC+2;
- complete console access/request workflow.

No other station maturity grade changes in this pass.

## CONTROL / TELMU

Unchanged at B. The next likely rule-path research candidates are:

- inverter warning persistence after inverter switching (TELMU/CONTROL interface); or
- a DPS pressure observation path (CONTROL) if mission-era telemetry/calibration documentation can establish the physical-to-ground measurement chain without fabricated nominal values.

## Source record

See:

- `resources/research/054_pc2_iss_warning_observation_path.md`
- `resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md`
- `resources/research/053_pc2_shutdown_rule_evaluation.md`
