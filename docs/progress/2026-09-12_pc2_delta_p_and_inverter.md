# Progress Log — 2026-09-12 — PC+2 delta-P and inverter rule paths

This is a continuation of the main project progress log.

## Inlet-pressure stop condition honored

Research note 057 had established two LM-7-family interface-pressure measurements (`GQ3611P` fuel and `GQ4111P` oxidizer) but not the selection/aggregation semantics behind the singular PC+2 150-psi ground inlet-pressure criterion.

A further bounded search did not recover defensible direct CONTROL/procedure evidence for that mapping. The project therefore did **not** infer either-side/minimum/average logic. The 150-psi ground rule remains `NOT_EVALUABLE`.

## Fuel/oxidizer differential-pressure path

Added `resources/research/058_pc2_fuel_oxidizer_delta_p_observation_path.md`.

Mission-specific sources establish:

- fuel/oxidizer ΔP greater than 25 psi as a PC+2 shutdown criterion;
- the criterion as a ground-only callout;
- separation from chamber-pressure and singular inlet-pressure criteria.

The exact ground transformation from LM pressure measurements remains unresolved. The implementation therefore models an optional ground-derived `dps_fuel_oxidizer_delta_p_psi` product without defining it as `GQ3611P - GQ4111P` or inventing sign/absolute-value semantics.

Implementation:

- added optional runtime ΔP state;
- added CONTROL projection with ground-derived provenance;
- added rule evaluation (`>25` triggered, `<=25` clear, missing value `NOT_EVALUABLE`);
- allowed source-bounded ΔP scenario injections;
- added synthetic tests at 26 psi and exactly 25 psi;
- retained no automatic engine cutoff/abort behavior.

## Inverter-warning-after-switch path

Added `resources/research/059_pc2_inverter_warning_after_switch.md`.

Primary technical evidence narrows the criterion:

- Apollo 13 PC+2 requires an inverter warning/light after switching inverters;
- LM instrumentation documentation ties the caution to inverter AC voltage/frequency quality;
- LM-5-and-subsequent hardware, including Apollo 13 LM-7, suppresses the normal inverter-selection transient until processed inverter data are valid.

No arbitrary persistence timer is therefore introduced.

Implementation now separates:

- runtime inverter warning observation;
- crew/procedural inverter-switch action;
- post-switch rule interpretation.

Added `src/apollo_mission_control/operational_actions.py` with the first minimal operational action: `switch_lm_inverter`. The action records only that a switch attempt occurred and its GET; it does not invent the inverter identity or cause/clear an electrical fault.

The shutdown evaluator now gives:

- no warning → `CLEAR`;
- warning present but no represented switch action → `NOT_EVALUABLE`;
- warning still present after represented switch action → `TRIGGERED`.

A new test exercises the positive rule path during the live burn at 79:29 GET and confirms that rule evaluation does not command cutoff or mutate the generic shutdown state.

## Station/source maintenance

Added:

- `docs/station-status/2026-09-12_pc2_delta_p.md`;
- `docs/station-status/2026-09-12_pc2_inverter_warning.md`;
- `resources/source-catalog/PC2_INVERTER_WARNING_SOURCES.md`.

CONTROL and TELMU remain maturity **B** because exact display/telemetry routing and some procedure details remain unresolved.

## Validation status

A container-backed test execution was attempted during this run but again failed with a transient runtime `ClientError` before the suite could execute. Tests are committed but are **not** recorded as freshly passing.

## Current stopping point

The project now distinguishes three different event classes that should remain separate:

1. historical/nominal mission events;
2. scenario/failure source-state injections;
3. controller/crew operational actions.

The next implementation/research pass should use this separation to model a small end-to-end decision/action loop rather than adding thresholds for their own sake. The strongest candidate is the inverter contingency itself: recover enough primary procedure evidence to determine what action/report sequence Mission Control and crew would follow after an inverter caution, without inventing exact switch identity or timing if the source does not supply it.
