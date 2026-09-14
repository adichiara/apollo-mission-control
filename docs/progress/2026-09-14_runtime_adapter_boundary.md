# Progress — shared runtime adapter boundary

Date: 2026-09-14

## Completed

- Extracted `SessionStatus` and the minimum shared session contract into `session_runtime.py`.
- Removed the realtime clock's direct dependency on `PC2Session`.
- Added a runtime-adapter registry:
  - `pc2_v1` remains the only implemented adapter;
  - scenario creation dispatches through the registry;
  - unsupported adapters are rejected explicitly.
- Added runtime capability metadata.
- Marked PC+2-only operations separately:
  - `pc2_delta_p`;
  - `pc2_dps_shutdown`.
- Moved exact-set join/rejoin semantics into the runtime contract rather than the HTTP transport.
- Session status now exposes the active runtime adapter and capability set.
- Added tests for:
  - runtime construction through the registry;
  - structural conformance of PC2Session to the shared contract;
  - unsupported adapter rejection;
  - explicit PC+2 capability boundaries;
  - realtime-clock operation against a minimal non-PC2 runtime object.

## Shared contract

The generic runtime boundary currently covers only behavior already justified across the project direction:

- authoritative state with GET/phase;
- lifecycle status;
- timed-event advancement;
- station assignment/ownership and exact-set rejoin;
- player snapshots;
- readiness reporting;
- FLIGHT decision and CAPCOM queue/transmission;
- audit history;
- explicit scenario-state injection.

It does **not** include PC+2 shutdown rules, ΔP interpretation, DPS crew shutdown choreography, PC+2 products, or PC+2 event names.

## Consequence

A future Apollo 11 descent runtime can implement the same lifecycle/session contract while supplying its own guidance/radar/trajectory state and procedures. The web transport and realtime clock no longer need to import or construct PC2Session directly.

## Next

1. Validate this refactor through full CI/network smoke.
2. Define the minimum Apollo 11 descent state/observation model from research note 141.
3. Implement the first scenario-neutral guidance/observation primitives only where both the existing engine architecture and the second reference require them.
