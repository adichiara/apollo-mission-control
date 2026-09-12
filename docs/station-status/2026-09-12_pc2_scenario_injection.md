# Station Status Addendum — PC+2 scenario injection layer

Date: 2026-09-12

## Result

The new generic timed scenario-injection layer does **not** change any station maturity grade.

It changes how nonnominal conditions enter the simulation, not what has been historically reconstructed for a controller console.

## CONTROL

Maturity remains **B**.

The first injectable source state is `dps_chamber_pressure_psi`, backed by the LM-7-family `GQ6510P` thrust-chamber-pressure measurement identity and the documented PC+2 ground shutdown criterion.

The timed-injection test now demonstrates the complete implemented path:

```text
synthetic source-bounded state change
    → modeled chamber-pressure observation
    → CONTROL product
    → independent 85-psi rule evaluation
```

This is an implementation advance but does not resolve CONTROL's principal historical gaps:

- exact Apollo 13 PCM assignment and engineering conversion;
- certified MSK 1137 `TCP` routing;
- exact update cadence;
- nominal PC+2 pressure trace;
- separate onboard 77-percent-thrust indication;
- full console/request workflow.

## GUIDO / TELMU / other PC+2 stations

Maturity remains unchanged.

Although several warning states are already represented in nominal fixtures/projections, they are **not yet** generic injection targets. They should first be migrated into explicit runtime source state rather than mutating nominal fixture constants.

This preserves the distinction between:

- historical nominal initialization data;
- runtime authoritative/source state;
- scenario injection;
- controller-visible products.

## Research consequence

Future station-specific nonnominal work should add an injectable parameter only after its source-state/measurement path is sufficiently documented. The injection layer itself is not evidence for a display field, telemetry channel, console control, or controller authority.

See `resources/research/056_pc2_scenario_injection_architecture.md`.
