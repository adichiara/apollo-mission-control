# Progress — Apollo 11 descent decision-gate contract

Date: 2026-09-21

Continued from research note 502 and the closed Apollo 11 LR controller-workflow thread.

## Result

Implemented a bounded decision-gate contract that preserves the documented station
and communication chain without creating an automatic landing decision.

The contract keeps LR range/velocity validity, antenna position, LR body-axis
velocity, LR slant range, PGNS altitude, TGO, Guidance readiness, CONTROL readiness,
FLIGHT decision, and CAPCOM relay as separate states.

Two deliberately non-decision derived checks are provided:

- whether the currently modeled Guidance and CONTROL readiness inputs are explicit;
- whether a recorded CAPCOM relay is consistent with a recorded FLIGHT decision.

## Guardrails

The implementation does **not**:

- treat CONTROL's LR position-2 call as LR acceptance or convergence;
- infer Guidance readiness from LR data;
- infer FLIGHT GO from station GO calls;
- infer CAPCOM relay from FLIGHT's decision;
- implement an unsourced ground `RNG - ALT` / Delta-H algorithm;
- change spacecraft state when a controller decision or CAPCOM relay is recorded.

## Files

- `src/apollo_mission_control/descent_decision_gate.py`
- `tests/test_descent_decision_gate.py`
- `docs/models/APOLLO11_DESCENT_DECISION_GATE.md`

## Next

Integrate the contract with the existing Apollo 11 landing-radar/guidance model
projection and the site-facing model/test page. Keep controller calls explicit so
wrong, delayed, omitted, or conflicting decisions remain possible.

## Evidence status

- **DOCUMENTED:** station-product ingredients and FLIGHT -> CAPCOM landing-poll topology.
- **PARTIAL:** exact field-to-rule mapping.
- **BLOCKED:** Mission-G LR per-field provenance/engineering conversion.
- **DEFERRED:** exact GUIDO/back-room phraseology and timing.
