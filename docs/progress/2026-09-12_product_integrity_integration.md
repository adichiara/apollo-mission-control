# Progress — product integrity integration and controller rejection

Date: 2026-09-12

## Completed

- Integrated hidden product-integrity annotations into the common `ProjectionSet` station object.
- Kept integrity metadata outside the normal controller-visible `products` dictionary.
- Added `controller_decisions.py` with explicit decision/audit events.
- Added explicit `reject_product(...)` event creation rather than auto-rejecting products marked internally incorrect.
- Added integration tests showing:
  - a product may remain `Validity.VALID` and visible while hidden integrity is `INCORRECT`;
  - controller rejection is a separate event with its own basis and optional independent reference.
- Added research note `066_controller_product_rejection_decision_event.md`.

## Architectural result

The data path now distinguishes:

`source/physical state → processing → visible product → hidden integrity metadata → controller interpretation/decision`

No hidden integrity flag is exposed automatically to players.

## Historical boundary

The post-MCC-5 AGS/RTCC case remains outside the PC+2 historical interval. It validates reusable architecture only.

## Test status

New tests are committed. No successful execution is recorded in this pass.

## Next work

Return to PC+2-specific nonnominal behavior. Prefer a source-backed path that uses already-modeled controller products and produces a real decision/communication problem without requiring speculative display reconstruction.
