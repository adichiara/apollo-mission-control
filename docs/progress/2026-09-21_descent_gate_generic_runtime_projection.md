# Progress — descent gate generic-runtime projection

Date: 2026-09-21

## Architectural finding

The existing generic runtime already contains the human-event primitives needed by
the Apollo 11 descent decision gate:

- explicit station readiness reports;
- a gate-scoped FLIGHT decision audit event;
- CAPCOM queue items with a distinct transmitted state and transmission GET.

A second controller-event framework would duplicate these semantics and create an
unnecessary parallel path.

## Implemented

Added a narrow adapter that projects those existing runtime artifacts into the
reusable descent decision-gate contract.

The adapter:

- selects the latest Guidance and CONTROL readiness reports at or before the
  requested GET;
- selects the latest FLIGHT decision for one explicitly configured gate id;
- recognizes only explicitly configured CAPCOM GO/NO-GO action identifiers;
- treats queued-but-not-transmitted CAPCOM items as **not relayed**;
- preserves contradictory FLIGHT/CAPCOM states rather than correcting them;
- receives controller-visible landing-radar state separately and never derives
  readiness from it.

## Files

- `src/apollo_mission_control/descent_decision_projection.py`
- `tests/test_descent_decision_projection.py`

## Guardrail

The action identifiers are software integration identifiers, not claims about exact
Apollo phraseology. Exact GUIDO/back-room words remain DEFERRED. Mission-G ground
Delta-H computation and per-field LR provenance remain unresolved/BLOCKED as already
recorded.

## Next

Use this adapter only when an Apollo 11 powered-descent runtime fixture is created
with an explicit landing decision gate. Do not make the generic runtime itself
Apollo-specific.
