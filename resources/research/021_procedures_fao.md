# Research Note 021 — Apollo 13 PROCEDURES / FAO

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Core distinction

Apollo 13 documents two coordination positions that become especially important in contingency operations.

### PROCEDURES

Owns the **ground/MCC/network procedural interface**.

Examples:

- FCOH
- communications support configuration
- site handovers
- telemetry/playback support
- data-processing configuration
- ground-support procedures

### FAO

Owns the **crew/mission activity timeline**.

Examples:

- flight-plan updates
- activity deletion/rescheduling
- rest/eat periods
- procedure placement in timeline
- TV/navigation/photography scheduling
- contingency return timeline

## Mission-specific display evidence

PROCEDURES identifies:

- **MSK 1503 — next station contact table**

The Apollo 13 report notes that its keyhole information was out of date.

This is another documented example where a real MCC display could itself contain imperfect/outdated ground-configuration data.

## Simulation-fidelity evidence

PROCEDURES criticizes simulation failures that violated real communications dependencies and recommends progressive degradation rather than instantaneous arbitrary loss.

This reinforces subsystem-level fault injection.

## Sources

- Apollo 13 Mission Operations Report, Appendices J and K:
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
