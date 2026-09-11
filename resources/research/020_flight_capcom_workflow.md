# Research Note 020 — FLIGHT / CAPCOM Workflow

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Core finding

Apollo 13 audio and official Mission Control organization support a deliberate two-stage communication architecture:

```text
technical disciplines ↔ FLIGHT ↔ CAPCOM ↔ crew
```

This should remain visible in the simulation.

## FLIGHT

The Flight Director loop shows FLIGHT as:

- decision authority;
- poller/integrator;
- conflict resolver;
- mission-priority manager.

FLIGHT does not replace EECOM, FIDO, GUIDO, etc. with a master systems display.

## CAPCOM

CAPCOM is the operational crew-voice interface.

The crew receives a much cleaner stream than the internal Flight loop:

- approved instructions;
- concise status;
- requests for observations;
- procedural read-ups.

Crew replies become a separate data source that CAPCOM routes back into Mission Control.

## Apollo 13 relevance

The accident required many procedures to be developed on the ground and transmitted to the crew.

The Flight Director report also documents deliberate management of crew rest/work cycles, including holding noncritical procedures until the required crew member was available.

Thus voice communication is linked to procedure state and timeline—not merely roleplaying style.

## Source value

The restored Apollo 13 Mission Control collection now contains 50 synchronized audio channels and more than 7,200 hours of audio.

This creates a future path for empirical analysis of:

- call cadence;
- controller-to-FLIGHT exchanges;
- FLIGHT-to-CAPCOM delay;
- CAPCOM read-up lengths;
- crew readbacks;
- loop usage by mission phase.

## Sources

- Apollo 13 in Real Time:
  https://apolloinrealtime.org/13/
- Apollo 13 Mission Operations Report:
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
