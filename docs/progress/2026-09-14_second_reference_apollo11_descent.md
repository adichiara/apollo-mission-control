# Progress — second reference case selection

Date: 2026-09-14

## Completed

- Evaluated Apollo 11 powered descent as a materially different architecture reference from PC+2.
- Used the Apollo 11 Mission Report to establish an exact actual-flight chronology for landing-radar state, 1201/1202 alarms, P64/P66 transitions, redesignation, and landing.
- Used Richard Koos's NASA oral history to strengthen the documented preflight simulation boundary:
  - a program alarm was deliberately injected;
  - Bales called abort;
  - PGNS/AGS cues agreed and were normal;
  - alarm handling was not yet in the flight rules;
  - the debrief triggered alarm-specific rule work.
- Preserved Koos's uncertainty about whether the injected alarm was 1201 or 1202.
- Selected the actual-flight 102:37:30–102:43:22 interval as the **second engineering reference case**, not yet as an executable runtime.
- Kept the preflight SimSup case separate so missing injection details are not reconstructed from the actual flight.

## Consequence

The second reference forces reusable support for guidance-computer alarm/restart state, PGNS/AGS cross-checks, landing radar and measurement acceptance, continuously evolving powered-descent trajectory, and continue/abort decisions based on controller evidence.

This provides a concrete basis for the next software abstraction: a runtime adapter interface shared by PC+2 and future scenario-specific runtimes.

## Next

Define the minimum runtime-adapter/session contract without moving PC+2-specific methods into the generic interface.
