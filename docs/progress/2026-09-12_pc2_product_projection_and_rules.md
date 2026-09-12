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

## 2026-09-12 continuation — DPS chamber-pressure observation path

### Primary-source finding

Research note `055_pc2_dps_chamber_pressure_observation_path.md` resolves the first analog propulsion shutdown-rule observation path.

The evidence chain is now strong enough for a bounded implementation:

1. the Apollo 13 Flight Control Division Mission Operations Report defines approximately **85 psi ground thrust-chamber pressure** as a PC+2 shutdown criterion, distinct from the crew/onboard approximately 77-percent-thrust criterion;
2. the **LM-7/8/9 Elementary Functional Diagrams** identify `GQ6510P` as **PRESS, THRUST CHAMBER**, giving mission-era vehicle-family measurement identity for Apollo 13's LM-7;
3. the Apollo 10 LM-4 DPS Final Flight Evaluation independently lists `GQ6510P` as engine thrust-chamber pressure and demonstrates its use as an actual propulsion flight measurement. Its LM-4 engineering range/sampling details are retained only as continuity evidence, not imported as Apollo 13 controller-display timing;
4. Apollo 13 mission/post-mission propulsion documentation supports the existence of recorded DPS flight data through the contingency burns without supplying a reviewed exact nominal GQ6510P trace for every instant of PC+2.

This is enough to represent a chamber-pressure measurement and rule observation without fabricating a historical normal reading.

### Implementation completed

- Added optional `PC2State.dps_chamber_pressure_psi`.
- `None` explicitly means **the project has not supplied a numerical value**; it does not mean Apollo telemetry is unavailable.
- CONTROL now receives `dps.chamber_pressure_psi` only when the simulation/test explicitly supplies a numerical observation.
- The product carries `psi` units and LM-7-family `GQ6510P` provenance.
- The shutdown-rule evaluator now handles the ground chamber-pressure criterion:
  - no modeled measurement → `NOT_EVALUABLE`;
  - modeled value >85 psi → `CLEAR`;
  - modeled value <=85 psi → `TRIGGERED`.
- Added a safe modeled-path test at 100 psi and a low-pressure rule-path test at 80 psi.
- The 80-psi value is explicitly **synthetic boundary-test data**, not an Apollo 13 historical malfunction or reconstructed pressure trace.
- A triggered chamber-pressure audit still does not stop the engine or mutate `state.shutdown_rule_triggers`.

### Documentation/source maintenance

- Added `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`.
- Updated `docs/scenarios/APOLLO13_PC2_PARAMETERS.md` to distinguish optional modeled GQ6510P observation from the intentionally unfrozen nominal PC+2 pressure trace.
- Updated `resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md` with the LM-7/8/9 diagrams, Apollo 10 DPS flight evaluation, Apollo 13 Mission Report, and Apollo 13 Panel 3 Addendum 1.
- Added `docs/station-status/2026-09-12_pc2_dps_chamber_pressure.md`.
- Updated `docs/ROADMAP.md` through the new analog CONTROL rule path.

### Station-status consequence

CONTROL remains maturity **B**. We now have a defensible measurement identity and an executable ground-rule path, but exact Apollo 13 GQ6510P PCM assignment, ground conversion, certified MSK 1137 `TCP` routing/update cadence, nominal PC+2 trace, and separate onboard 77-percent-thrust indication remain unresolved.

### Validation status

A new container-backed test run was attempted after the commits. The runtime again returned a transient client error before clone/test execution. The repository therefore records the tests as **committed but not freshly executed**; no passing result is claimed.

## Current documented stopping point

The project now has two qualitatively different source-backed nonnominal rule paths:

- a discrete conjunction: ISS warning + program alarm;
- an analog propulsion measurement: CONTROL chamber pressure against the 85-psi ground criterion.

That is sufficient to move the implementation boundary from hand-edited test observations toward a **minimal generic scenario/failure-injection object** that perturbs underlying modeled state/observations rather than setting diagnoses or rule outcomes directly.

The next implementation pass should therefore:

1. define the smallest generic injection structure needed to change an underlying observation/state at a specified mission time;
2. prove that the same controller-product and shutdown-rule layers respond without special-case scenario logic;
3. keep synthetic boundary fixtures explicitly labeled non-historical;
4. defer narrative Apollo training/failure scenarios until a historically documented malfunction mechanism is selected and sourced.

Additional rule-path research should be demand-driven from that architecture rather than performed merely to increase the number of implemented thresholds.
