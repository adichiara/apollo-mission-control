# Progress — Apollo 11 descent decision gate model-lab integration

Date: 2026-09-21

## Result

Projected the research-502 descent decision-gate contract into the existing
site-facing Causal Model Lab.

The new model-proof endpoint and page preserve the same non-automation boundary as
the domain model:

- LR range/velocity validity and antenna position remain independent;
- Guidance and CONTROL readiness are explicit controller states;
- FLIGHT remains an explicit decision even when both modeled station calls are GO;
- CAPCOM relay remains a separate communication state;
- contradictory relay/FLIGHT combinations are exposed rather than repaired.

The browser surface includes explicit demonstrations for:

- a caller-configured decision chain;
- Guidance/CONTROL GO with FLIGHT still undecided;
- a contradictory CAPCOM GO relay after a FLIGHT NO-GO.

## Files

- `src/apollo_mission_control/web_app.py`
- `web/model_tests.html`
- `tests/test_web_model_proof.py`
- `tests/test_model_test_runner.py`

## Guardrail

This remains a model/test surface, not scenario automation. It does not compute
Delta-H, infer LR convergence, derive Guidance readiness from telemetry, or decide
whether FLIGHT should land.

## Next

After CI, merge this vertical slice and continue the Apollo 11 powered-descent
reference by connecting explicit controller events to the reusable decision-gate
state, while preserving the current BLOCKED/DEFERRED research boundaries.

## Evidence status

- **DOCUMENTED:** controller-visible inputs and front-room FLIGHT -> CAPCOM topology.
- **PARTIALLY DOCUMENTED:** exact field-to-rule mapping.
- **BLOCKED:** Mission-G per-field LR provenance/engineering conversion.
- **DEFERRED:** exact GUIDO/back-room phraseology and timing.
