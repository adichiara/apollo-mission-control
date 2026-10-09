# Apollo 11 Descent Runtime Projection

Status: **implemented read-only architecture composition and runtime adapter; live historical scenario execution remains model-readiness gated**

## Purpose

Compose the Apollo 11 powered-descent architecture reference from existing source-bounded domains without creating a second event system or converting hidden model state into controller decisions.

Implementation:

- `src/apollo_mission_control/apollo11_descent_runtime_projection.py`
- `src/apollo_mission_control/apollo11_descent_runtime_probe.py`
- `src/apollo_mission_control/apollo11_descent_session.py`
- `data/scenarios/apollo11_descent_program_alarm_reference.json`
- `tests/test_apollo11_descent_runtime_projection.py`
- `tests/test_runtime_adapters.py`
- `tests/test_apollo11_descent_runtime_probe.py`

## Reused domains

The projection reuses rather than duplicates:

- `GenericScenarioSession` for station ownership, readiness, FLIGHT decisions, CAPCOM queue/transmission, GET, and audit history;
- the Apollo 11 nominal powered-descent phase profile;
- the Apollo 11 controller-product schema;
- the generic-runtime descent decision projection;
- explicit landing-radar controller state;
- explicit guidance-computer alarm/restart state.

## Non-automation invariants

The composed snapshot explicitly reports:

- `human_decision_generated = false`;
- `controller_products_derived_from_hidden_state = false`;
- `session_mutated = false`.

These are implementation contracts, not historical claims.

A Guidance/CONTROL GO pair remains compatible with FLIGHT being undecided. A FLIGHT GO remains separate from a CAPCOM relay. An active onboard program-alarm state does not populate the controller-visible alarm field unless that product value is explicitly supplied through the controller-product boundary.

## Manual-control authority

The generic-runtime descent projection now accepts the explicit `DescentControlMode`.

Changing from automatic to manual/P66:

- does not remove landing-radar observations;
- does not change the nominal phase state;
- does not create a FLIGHT decision;
- changes only the already sourced trajectory/guidance abort-rule applicability represented by the decision-gate contract.

## Time/phase boundary

The projection calculates TFI from:

`session GET - supplied PDI GET`

and evaluates the nominal phase skeleton. It does not infer PDI from hidden state and does not reconcile nominal phase anchors with postflight flown-duration observations.

## Controller-product boundary

Only values explicitly supplied to `project_apollo11_descent_products` become available controller products.

For example, the reference probe demonstrates both:

1. onboard guidance state contains active alarm `1202`, but the controller alarm product is unavailable because it was not supplied;
2. the same onboard state with an explicitly supplied `program.alarm_latest = 1202` produces an available controller product.

This prevents a future runtime adapter from using convenient internal state as a substitute for unresolved Mission-G routing.

## Site-facing proof

Facilitator endpoint:

`GET /api/admin/model-proof/apollo11-descent-runtime-projection`

The Causal Model Lab shows five architecture cases:

- high-gate station GO / FLIGHT undecided;
- explicit FLIGHT GO + separate CAPCOM relay;
- manual-control rule-authority transition;
- active alarm not back-filled into controller product;
- active alarm explicitly supplied to controller product.

Probe values and event timings are synthetic. The proof is not an Apollo 11 historical replay.

## Runtime-adapter boundary

The cataloged `apollo11_descent_v1` adapter is now implemented as an `Apollo11DescentSession` layered on `GenericScenarioSession`.

It binds:

- source-controlled PDI GET;
- the nominal powered-descent phase profile;
- the explicit `landing_go` decision-gate identifier;
- GUIDO as the player/station identity for the bounded Guidance-readiness input;
- CONTROL as the CONTROL readiness input;
- explicit CAPCOM GO/NO-GO action identifiers.

The fixture keeps station views empty. Internal reference-event variables therefore do not become controller-visible products automatically. The bound `project_descent()` method still requires landing-radar state, controller-product values, and guidance-computer state as separate explicit inputs.

The nominal high-gate anchor opens `landing_go` for architecture testing. That scheduling is a project integration anchor, not a claim that the historical FLIGHT decision occurred at exactly nominal high gate.

The scenario catalog also separates adapter availability from execution approval. Apollo 11 advertises the adapter but requires validated historical model domains before the live session API will create it. PC+2 retains its separately accepted partial-model prototype policy.

## Deliberately not done

This projection/adapter is not yet:

- an executable selectable Apollo 11 historical session;
- a continuous trajectory/thrust simulation;
- a historical reconstruction of station timing;
- a source of automatic GO/NO-GO, abort, or landing decisions;
- a substitute for unresolved Mission-G ground-product routing.

## Next

Treat the adapter/fixture integration question as complete. Use D-024 to bound the remaining execution-readiness dependencies rather than broadening the adapter. Live execution remains blocked by the scenario's validated-model gate, while unresolved Mission-G controller-product routing remains separate from onboard/vehicle model readiness.
