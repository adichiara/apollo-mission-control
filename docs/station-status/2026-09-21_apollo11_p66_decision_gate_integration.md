# Station research status — Apollo 11 P66 decision-gate integration

Date: 2026-09-21

## GUIDANCE

**Status: sufficient for current P66 authority boundary.**

Ground guidance/navigation observations and comparisons remain available after crew takeover. The reusable gate therefore retains its controller-visible LR state and GUIDANCE readiness. Flight Mission Rule 5-11 prevents trajectory/guidance constraint violations after takeover from being promoted by this layer into an abort cause.

Still unresolved: exact Mission-G display/keying used to recognize P66 and any dedicated GUIDANCE voice call. Neither is required by the current domain contract.

## FLIGHT

**Status: sufficient for current P66 authority boundary.**

FLIGHT remains a separate explicit human decision state. Manual takeover changes applicability of trajectory/guidance abort constraints; it does not synthesize a GO, NO-GO, or abort decision.

## CONTROL

**Status unchanged.**

The P66 transition does not disable independently sourced systems/propellant monitoring or the previously documented propellant-countdown path. `control_readiness` remains independent of the new control-mode state.

## CAPCOM

**Status unchanged.**

No new P66-specific CAPCOM call is introduced. Relay remains a separate communication state and must be sourced independently.

## Implementation boundary

The reusable decision gate now supports:

`automatic → manual`

as an authority transition while retaining the same observations. Exact detection/annunciation of that transition belongs upstream in scenario/controller-product evidence and is not inferred here.

## Evidence status

- **GUIDANCE:** SUFFICIENT for observation-continuity/rule-authority behavior; exact P66 indication DEFERRED.
- **FLIGHT:** SUFFICIENT for explicit human-decision separation.
- **CONTROL:** SUFFICIENT; unaffected independent criteria remain separate.
- **CAPCOM:** SUFFICIENT for existing relay boundary; no P66-specific call claimed.