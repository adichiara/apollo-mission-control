# Progress Log — 2026-09-12 — PC+2 product projection and shutdown rules

This is a continuation of `docs/PROGRESS.md`. The master file is preserved unchanged because its full contents exceed the current connector read window; this dated continuation avoids a destructive whole-file rewrite.

## Research completed

- Reviewed the Apollo 13-era MCC/MSFN information path and Apollo real-time display architecture to confirm that controller products should remain downstream of spacecraft/onboard state, communications/telemetry, and ground processing.
- Created `resources/research/052_pc2_controller_product_projection.md` defining the first station-specific projection boundary.
- Preserved a critical distinction between **historical data validity** and **project implementation completeness**: historically required measurements whose nominal values are not yet modeled are tracked as deferred implementation fields, not falsely shown as unavailable telemetry.
- Reviewed the PC+2 Mission Rules and crew readback using the Mission Operations Report and technical air-ground record.
- Created `resources/research/053_pc2_shutdown_rule_evaluation.md` defining `clear`, `triggered`, `not_evaluable`, and `not_applicable` rule states.
- Logged, rather than resolved, a primary-source wording conflict: the Mission Operations Report associates the startup-transient exception with the attitude-rate criterion, while the crew readback associates it with attitude error.

## Implementation completed — product/rule baseline

- Added `source_layer` to the common `Product` metadata contract.
- Added `src/apollo_mission_control/controller_products.py` with station-specific projection sets for CONTROL, GUIDO, FIDO/RETRO, TELMU, INCO, FLIGHT, and CAPCOM.
- Added explicit `deferred_fields` so missing implementation values cannot masquerade as Apollo telemetry failures.
- Added `src/apollo_mission_control/shutdown_rules.py` with a partial, source-backed shutdown-rule audit evaluator.
- The evaluator does **not** create or command a generic `burn_abort` state.
- Modeled discrete warnings can evaluate as clear/triggered; unsupported analog criteria remain `not_evaluable` until their observation paths are modeled.

## 2026-09-12 continuation — ISS warning observation path

### Primary-source finding

Research note `054_pc2_iss_warning_observation_path.md` resolves the first deferred positive shutdown-rule observation path.

The Apollo 13 Mission Operations Report defines a mandatory PC+2 shutdown criterion requiring **inertial-reference/ISS warning plus a computer program alarm**. The LM Operations Handbook GN&CS block diagram independently shows a distinct **ISS WARNING SIGNAL** and **LGC WARNING SIGNAL** routed to the Instrumentation Subsystem. Contemporary LUMINARY functional-description material likewise treats ISS and LGC warnings as distinct onboard caution/warning indications and describes ISS warning as being under LGC program control.

The project therefore now has sufficient evidence to model ISS warning as its own onboard/telemetry observation. The source does **not** establish the exact Apollo 13 LM-7 telemetry word or GUIDO CRT field, so those remain explicit gaps.

### Implementation completed

- Advanced the nominal fixture to schema `0.3-research-fixture` and added nominal `pgns.iss_warning = false`.
- Added `pg_ns.iss.warning` to GUIDO's controller-product projection with `onboard/telemetry` provenance.
- Updated the shutdown evaluator so the ISS/program-alarm criterion is truly conjunctive:
  - warning false + no alarm → clear;
  - warning true + no alarm → clear;
  - warning false + alarm present → clear;
  - warning true + alarm present → triggered.
- Added the first source-backed nonnominal **rule-path** validation case by injecting only the documented observations: ISS warning present plus program alarm present.
- The test deliberately uses a non-historical test sentinel for “program alarm present”; it does not invent a PC+2 alarm number or malfunction mechanism.
- The triggered audit result still does not mutate `state.shutdown_rule_triggers` or automatically command a shutdown. Controller/FLIGHT/CAPCOM action remains a separate decision path.

### Validation status

The updated tests are committed. A fresh container-backed test execution attempt again failed with a transient client/runtime error before the repository could be cloned/run. The project therefore does **not** claim that this test suite has executed successfully in this pass.

## Source catalog maintenance

- `resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md` now includes the LM Operations Handbook GN&CS source and contemporary LUMINARY functional-description source used for the ISS warning path.
- The configuration caveat is explicit: the searchable handbook is LM-10-and-subsequent, while Apollo 13 flew LM-7. It is used only for warning/instrumentation-path architecture consistent with the Apollo 13 mission-rule evidence, not to claim exact LM-7 CRT/word routing.

## Station-status consequence

GUIDO remains maturity **B**. Evidence improved from “rule requires an ISS warning” to “ISS warning is a distinct onboard warning with an instrumentation path,” but exact Apollo 13 LM-7 telemetry word, ground routing, and GUIDO CRT placement remain unresolved. No other station maturity grade changes.

## Documented stopping point

The first source-backed nonnominal rule path is now complete at the information/audit level. The next useful branch should be chosen by evidence value rather than convenience:

1. research the **inverter-warning-after-switch** path if the LM electrical documentation can establish switch-attempt and warning-persistence state cleanly; or
2. research one **DPS pressure** observation path if mission-era telemetry/calibration documentation can provide a defensible physical-to-ground measurement model without inventing nominal values.

Do not add a narrative failure scenario until the underlying malfunction state and observation path are both documented strongly enough to avoid a scripted diagnosis.
