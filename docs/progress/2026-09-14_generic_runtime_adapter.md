# Progress — generic runtime adapter

Date: 2026-09-14

## Completed

- Added a second runtime adapter, `generic_v1`, independent of `PC2Session`.
- Added shared runtime behavior for:
  - lifecycle and continuous GET advancement;
  - station assignment/rejoin;
  - station-scoped projections;
  - readiness reporting;
  - FLIGHT decision gates;
  - CAPCOM queue/transmission;
  - audit history;
  - controlled source-state injection;
  - timed external/discrete scenario events.
- Added a test-only synthetic fixture rather than publishing a fake historical scenario in the production scenario catalog.
- Added tests proving the generic runtime satisfies the shared `SessionRuntime` contract while not advertising PC+2-specific capabilities.

## Architecture boundary

The generic runtime is exercise infrastructure, not a generic physics engine.

Timed scenario updates may represent genuinely external/discrete exercise inputs. They must not be used to script downstream physical consequences that should emerge from propulsion, guidance, electrical, trajectory, observation, crew, or other causal models.

Station projections are explicit allowlists so generic runtime state is not automatically exposed to players.

## Consequence

The repository now proves two separate executable runtime implementations:

- `pc2_v1` — historical Apollo 13 PC+2 reference adapter;
- `generic_v1` — scenario-neutral validation adapter.

This closes the architectural dependency where all executable session behavior previously required `PC2Session`. The next historically grounded scenario can now either use the generic shared mechanics plus new causal domains or introduce a specialized adapter only for behavior that is truly scenario-specific.
