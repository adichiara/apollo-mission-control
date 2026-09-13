# Progress — low-player-count station aggregation research

Date: 2026-09-12

## Completed

- Researched the deferred low-player-count station-aggregation question using Apollo 13/NASA primary sources first.
- Confirmed the historical organizational grouping of FIDO/RETRO/GUIDO under Flight Dynamics and TELMU/CONTROL under Systems Operations.
- Confirmed FLIGHT and CAPCOM as distinct decision/crew-voice functions that should remain independent in the first compact mode.
- Confirmed a real Apollo example of selective console/function sharing: INCO + O&P.
- Defined a **five-player compact PC+2 configuration** as a project adaptation:
  - FLIGHT
  - CAPCOM
  - LM SYSTEMS = TELMU + CONTROL
  - FLIGHT DYNAMICS = GUIDO + FIDO/RETRO
  - INCO
- Explicitly rejected any implication that Apollo historically manned PC+2 with those five bundled roles.
- Defined the implementation invariant that bundled players must retain the original station-scoped products, actions, readiness judgments, and audit identities underneath the combined UI.
- Left four-player-or-smaller configurations unresolved.

## Repository changes

- Added `resources/research/091_low_player_count_station_aggregation_boundary.md`.
- Added `resources/source-catalog/PC2_LOW_PLAYER_COUNT_SOURCES.md`.
- Added station-status addendum `docs/station-status/2026-09-12_low_player_count_aggregation.md`.
- Updated decision, roadmap, and research-resource documentation to remove the prior blanket statement that low-player-count aggregation was entirely undesigned.

## Current boundary

The research/design boundary is now closed for the first compact configuration. Code implementation remains intentionally separate from the historical claim:

```text
player -> assigned set of original stations -> bundled presentation
```

The full seven-seat configuration remains the preferred fidelity baseline and the existing live-device protocol still needs physical execution.

## Next implementation target

When compact-mode implementation begins, generalize station assignment to allow one player to own multiple original stations while preserving existing station authorization and information boundaries. Do not introduce synthetic domain stations that erase TELMU/CONTROL/GUIDO/FIDO/RETRO ownership.
