# Progress — generic electrical power model

Date: 2026-09-14

## Completed

- Added a mission-neutral coarse electrical bus/load model.
- Added caller-defined source capacities and equipment loads.
- Added explicit source availability, bus enablement, and load command state.
- Added deterministic priority-based supply under insufficient capacity.
- Equal-priority loads are all-or-none so the engine does not silently invent an ordering.
- Added per-load reason codes and explicit model assumptions/provenance.
- Added synthetic tests for normal supply, source loss, overload/load shedding, bus disablement, commanded-off loads, and invalid configuration.

## Architecture consequence

The simulator now has reusable causal machinery for:

`electrical source/configuration -> bus capacity -> equipment powered/unpowered`

This is intentionally separate from historical Apollo bus topology and detailed electrical physics.

## Next

Add energy/consumable depletion as a separate reusable state model, then connect historically sourced mission profiles only where controller decisions require those dependencies.
