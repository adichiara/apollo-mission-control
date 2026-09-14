# Progress — reusable scenario catalog boundary

Date: 2026-09-14

## Completed

- Added a framework-neutral scenario catalog that discovers JSON fixtures from `data/scenarios`.
- Defined a small cross-scenario metadata contract:
  - scenario ID and title;
  - mission;
  - status/provenance class;
  - scenario class;
  - runtime-adapter identifier;
  - start/end mission-time metadata;
  - vehicle configuration;
  - source count.
- Added explicit metadata to the Apollo 13 PC+2 fixture:
  - `historical_flight_reconstruction`;
  - runtime adapter `pc2_v1`.
- Added `GET /api/scenarios` for scenario discovery.
- Extended session creation so `POST /api/session/create?scenario_id=...` selects a cataloged scenario.
- Preserved existing behavior: omitting the scenario ID still creates `apollo13_pc2_nominal`.
- Session status now identifies the active scenario.
- Added unit and HTTP tests for discovery, metadata validation, duplicate IDs, explicit selection, and unknown IDs.

## Boundary retained

The catalog is **not** a claim that multiple scenarios are already playable.

Only the `pc2_v1` runtime adapter is implemented. A fixture using another adapter may be cataloged later but must remain non-executable until its domain/runtime implementation exists.

This deliberately avoids forcing PC+2's state model to become the universal Apollo state schema before a second scenario gives us evidence for the correct shared abstraction.

## Next

1. Validate catalog/selection behavior through CI and deployed API smoke.
2. Define the first reusable mission-profile boundary (mission-era MCC/station/configuration metadata) separately from scenario events.
3. Select a second, materially different reference scenario to pressure-test what belongs in common engine state versus a scenario-specific adapter.
