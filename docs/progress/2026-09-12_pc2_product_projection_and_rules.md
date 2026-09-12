# Progress Log — 2026-09-12 — PC+2 product projection and shutdown rules

This is a continuation of `docs/PROGRESS.md`. The master file is preserved unchanged because its full contents exceed the current connector read window; this dated continuation avoids a destructive whole-file rewrite.

## Research completed

- Reviewed the Apollo 13-era MCC/MSFN information path and Apollo real-time display architecture to confirm that controller products should remain downstream of spacecraft/onboard state, communications/telemetry, and ground processing.
- Created `resources/research/052_pc2_controller_product_projection.md` defining the first station-specific projection boundary.
- Preserved a critical distinction between **historical data validity** and **project implementation completeness**: historically required measurements whose nominal values are not yet modeled are tracked as deferred implementation fields, not falsely shown as unavailable telemetry.
- Reviewed the PC+2 Mission Rules and crew readback using the Mission Operations Report and technical air-ground record.
- Created `resources/research/053_pc2_shutdown_rule_evaluation.md` defining `clear`, `triggered`, `not_evaluable`, and `not_applicable` rule states.
- Logged, rather than resolved, a primary-source wording conflict: the Mission Operations Report associates the startup-transient exception with the attitude-rate criterion, while the crew readback associates it with attitude error.

## Implementation completed

- Added `source_layer` to the common `Product` metadata contract.
- Added `src/apollo_mission_control/controller_products.py` with station-specific projection sets for CONTROL, GUIDO, FIDO/RETRO, TELMU, INCO, FLIGHT, and CAPCOM.
- Added explicit `deferred_fields` so missing implementation values cannot masquerade as Apollo telemetry failures.
- Added `src/apollo_mission_control/shutdown_rules.py` with a partial, source-backed shutdown-rule audit evaluator.
- The evaluator does **not** create or command a generic `burn_abort` state.
- Modeled discrete warnings can evaluate as clear/triggered; unsupported analog criteria remain `not_evaluable` until their observation paths are modeled.
- Added tests for station information boundaries, metadata, deferred-field behavior, post-burn residual availability, partial rule evaluation, and positive warning cases.

## Source catalog maintenance

- Added `resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md` as an active implementation-specific supplement to the master source catalog.
- Updated `resources/README.md` to document scenario/source-catalog supplements and the expectation that they be folded into the master catalog during comprehensive maintenance.
- Added NASA TN D-8316, *Apollo Experience Report: Real-Time Display System*, as architecture support only; it is not used to invent PC+2 display layout or refresh cadence.

## Station-status consequence

No maturity grades changed. This work implements already documented information boundaries; it does not provide new exact console/display evidence. CONTROL, GUIDO, FIDO, RETRO, TELMU, INCO, FLIGHT, and CAPCOM remain maturity **B**.

## Validation status

The expanded tests are committed, but the container/Python execution runtime returned a transient client error during this pass. The repository therefore does **not** claim that the new tests have executed successfully.

## Documented stopping point

The next implementation work should be driven by one of two source-backed needs:

1. model the first currently deferred shutdown-rule observation path for which a defensible measurement/state source can be established; or
2. select the first nonnominal validation case only when its underlying condition and observation path are documented strongly enough to avoid a scripted diagnosis.

The minimum numerical trajectory state remains deferred until the propagating trajectory implementation requires it.
