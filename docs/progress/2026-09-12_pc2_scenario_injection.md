# Progress Log — 2026-09-12 — PC+2 timed scenario injection

Continuation of `docs/PROGRESS.md` and `docs/progress/2026-09-12_pc2_product_projection_and_rules.md`.

## Research completed

- Reviewed the contemporaneous Apollo 13 Simulator Discrepancy Reports for LUM 131 Rev. 8.
- Research note `056_pc2_scenario_injection_architecture.md` records the relevant primary-source case: test H20T-7.2 #1 (27 Jan 1970) intentionally tested a hardware restart and documented several dependent consequences rather than one canned failure indication.
- Preserved the distinction between simulator engineering evidence and an integrated historical SimSup scenario. No undocumented malfunction code, operator UI, or exact injection command syntax is inferred.
- Reconfirmed from the Apollo 13 Mission Operations Report that the selected PC+2 rule/product path should remain the downstream decision mechanism for nonnominal conditions.

## Implementation completed

- Added `src/apollo_mission_control/scenario_injection.py`.
- Added `EvidenceClass` metadata:
  - `historical_event`;
  - `documented_simulation_case`;
  - `source_bounded_test`;
  - `project_hypothetical`.
- Added immutable `StateInjection` records carrying ID, GET, target, value, evidence class, and provenance.
- Added explicit target whitelisting rather than arbitrary nested-object mutation.
- Initial executable target is deliberately limited to `dps_chamber_pressure_psi`, the first observation with both a researched LM-7-family measurement identity and a documented PC+2 threshold.
- Added deterministic event/injection ordering: historical timeline event first, injection second at identical GET. This is documented as a project convention, not historical SimSup behavior.
- Added `run_with_injections(...)` with optional stop GET for deterministic validation snapshots.

## Validation fixture added

`tests/test_scenario_injection.py` now expresses the existing low-chamber-pressure boundary path as a timed scenario injection rather than direct state mutation:

- injection GET: 79:29:00;
- injected chamber pressure: 80 psi;
- classification: `source_bounded_test`;
- expected CONTROL result: chamber-pressure product = 80 psi;
- expected rule result: documented ground criterion triggers;
- engine remains running at the snapshot;
- no cutoff/abort or `shutdown_rule_triggers` mutation is created by the injection mechanism.

Both the selected time and 80-psi value are explicitly synthetic implementation-test choices. They are not presented as a historical Apollo 13 failure.

Additional tests reject unsupported injection targets and verify that future injections are not applied before their GET.

## Source/catalog maintenance

- Added the Apollo 13 Simulator Discrepancy Reports to `resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md`.
- Updated `docs/ROADMAP.md` through the first generic timed nonnominal injection.
- Added `docs/station-status/2026-09-12_pc2_scenario_injection.md`.
- Updated README current status and source/status links.

## Station-status consequence

No maturity grade changes.

CONTROL remains **B**. The injection layer proves that the researched chamber-pressure source state can be perturbed and naturally flow into CONTROL/rule evaluation, but does not resolve exact Apollo 13 PCM assignment, ground conversion, MSK 1137 routing, update cadence, or nominal PC+2 pressure trace.

GUIDO, TELMU, and other PC+2 positions are unchanged. Their already-modeled warning constants are not yet generic injection targets because those observations should first be migrated into explicit runtime source state instead of mutating nominal fixture constants.

## Validation execution status

A clean repository clone/test run was attempted again in the execution environment after these commits. The container runtime returned a client error before the repository could be cloned, so the new test files are **committed but not freshly executed in this run**. No passing result is claimed.

## Current documented stopping point

The generic injection architecture is no longer the blocker.

Next work should research and model **one additional PC+2 runtime observation path** that can be defensibly perturbed through the same interface. Candidate priority remains:

1. DPS inlet pressure;
2. fuel/oxidizer differential pressure;
3. separate onboard thrust indication;
4. inverter warning plus inverter-switch-attempt state.

Selection should be based on strongest accessible primary-source evidence, not on convenience. Once the next source state is established, migrate it into runtime state, add it to the explicit injection whitelist, and prove that the existing station-product/rule path reacts without scenario-specific diagnosis logic.
