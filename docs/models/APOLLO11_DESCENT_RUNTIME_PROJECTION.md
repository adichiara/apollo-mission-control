# Apollo 11 Descent Runtime Projection

Status: **implemented read-only architecture composition; not yet an executable historical scenario**

## Purpose

Compose the Apollo 11 powered-descent architecture reference from existing source-bounded domains without creating a second event system or converting hidden model state into controller decisions.

Implementation:

- `src/apollo_mission_control/apollo11_descent_runtime_projection.py`
- `src/apollo_mission_control/apollo11_descent_runtime_probe.py`
- `tests/test_apollo11_descent_runtime_projection.py`
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

## Deliberately not done

This projection is not yet:

- an executable selectable Apollo 11 scenario;
- a new runtime adapter;
- a continuous trajectory/thrust simulation;
- a historical reconstruction of station timing;
- a source of automatic GO/NO-GO, abort, or landing decisions;
- a substitute for unresolved Mission-G ground-product routing.

## Next

Use this projection as the read-only boundary for an Apollo 11 descent runtime adapter/fixture. The adapter should reuse `GenericScenarioSession` mechanics and existing causal domains, expose only source-backed/controller-supplied products, and keep the scenario non-executable until its required model/readiness gates are explicitly satisfied.
