# Progress — Apollo 11 P66 site-facing authority proof

Date: 2026-09-22

## Completed

Closed the remaining site-facing implementation item from the 2026-09-21 P66
decision-gate integration.

The existing Apollo 11 descent decision-gate API now accepts explicit
`control_mode`:

- `automatic`;
- `manual`.

The Causal Model Lab exposes the same selector and adds an
**Automatic / manual authority comparison** action.

## Paired proof

The paired case intentionally keeps these values unchanged:

- landing-radar controller-visible state;
- Guidance readiness;
- CONTROL readiness;
- FLIGHT decision;
- CAPCOM relay.

It changes only `control_mode`.

Expected result:

- automatic control → trajectory/guidance abort constraints remain applicable;
- manual/P66 takeover → those trajectory/guidance constraints are not themselves
  abort causes.

The landing-radar/controller observation remains visible in both cases.

## Guardrail

The proof does not detect P66 automatically and does not generate:

- an abort;
- a continue/landing decision;
- a FLIGHT GO/NO-GO;
- a CAPCOM transmission.

It is an authority/rule-applicability proof, not a mission-decision algorithm.

## Tests

Added API regression coverage proving observation and human-decision-state continuity
across the automatic→manual transition, and browser-contract coverage for the paired
site-facing proof.

## Next

Return to the unresolved Apollo 11 controller-product boundary identified in the
main roadmap. Exact Mission-G P66 annunciation/keying/voice detail remains deferred
unless a player-facing dependency reopens it.
