# Progress — deterministic simulated flight-crew actor

Date: 2026-09-14

## Completed

- Added a mission-neutral `SimulatedCrew` actor.
- Added caller-supplied instruction rules mapping supported CAPCOM actions to:
  - bounded acknowledgement text;
  - one supported crew operational action;
  - an allowlist of forwarded parameters;
  - provenance.
- Kept receipt and crew action as separate explicit stages.
- Added temporal-order checks without generating response delay.
- Kept physical/subsystem effects outside the actor.
- Added tests for unsupported/untransmitted instructions, duplicate handling, parameter allowlisting, timing order, and receipt/action separation.
- Bridged the Apollo 13 PC+2 DPS shutdown-call path onto the generic actor while retaining the existing `OperationalAction` and later physical engine-off response boundary.

## Consequence

The simulator no longer needs a PC+2-specific concept of "crew receipt" as the architectural model. PC+2 is now one configuration of a reusable non-player crew actor.

Future Apollo 11 and other scenarios can reuse the same actor once their CAPCOM/crew action mappings and any response timing are source-bounded.

## Boundary

The crew actor is deterministic exercise infrastructure, not crew AI. It does not diagnose, choose procedures, decide abort/continue, invent timing, or assert physical success.
