# Progress — generic resource inventory model

Date: 2026-09-14

## Completed

- Added a mission-neutral finite-resource inventory model.
- Supports multiple resources with independent units/bounds.
- Supports piecewise-constant consumption and replenishment.
- Reports consumed/replenished quantities, unsatisfied consumption, overflow, and exact boundary-hit times.
- Clamps inventories at configured bounds rather than allowing negative or impossible quantities.
- Added synthetic tests for multi-resource depletion, exact depletion timing, replenishment/overflow, unbounded resources, zero-flow segments, and invalid configuration.

## Architecture consequence

The simulator can now represent time-evolving finite resources without embedding scenario outcomes:

`configuration-dependent flow -> inventory state -> downstream subsystem availability/observation`

The next integration step is to connect selected resource state to other reusable models only where a sourced scenario dependency exists; for example, remaining battery energy may determine whether an electrical source remains available.

## Boundary

No battery chemistry, pressure, tank, transfer, or mission-specific rate model is implied.
