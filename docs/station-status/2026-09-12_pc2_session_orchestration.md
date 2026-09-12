# Station research-status addendum — PC+2 session orchestration transition

Date: 2026-09-12

## Presentation checkpoint

The minimum first-slice player-facing views now exist for:

- CONTROL
- GUIDO
- TELMU
- FIDO/RETRO
- INCO
- FLIGHT
- CAPCOM

This satisfies the documented stop condition for broad display expansion before integrated play.

## FLIGHT

**Maturity remains B.**

Improved:

- the session layer now has a first-class per-station readiness-report concept;
- FLIGHT GO/NO-GO is an explicit controller decision rather than a hidden-health calculation;
- the audit trail can preserve the room-poll -> decision sequence.

Still unresolved:

- exact Apollo 13 FLIGHT console layout;
- exact wording/order of every individual readiness response in the PC+2 poll;
- exact internal voice-loop routing.

These are not blockers for first integrated play.

## CAPCOM

**Maturity remains B.**

Improved:

- controller/FLIGHT callouts can now be queued separately from crew transmission;
- CAPCOM transmission is a distinct auditable event;
- the architecture prevents a controller decision from silently appearing to the crew.

Still unresolved:

- exact CAPCOM console layout;
- detailed procedure staging/queue hardware;
- exact internal callout handoff topology.

## Other PC+2 stations

CONTROL, GUIDO, TELMU, FIDO/RETRO, and INCO remain at their existing maturity levels. No additional display research is required before session integration unless a concrete player decision exposes a missing product.

## Research stop condition

Station-by-station display expansion is paused for the PC+2 vertical slice.

## Next project boundary

Integrate the session orchestration state with station products/presentations, then move to transport/reconnect/client delivery. New historical station research should be demand-driven by an integration or gameplay dependency.
