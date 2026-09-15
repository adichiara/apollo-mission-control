# Progress — PC+2 inverter action/report loop

Date: 2026-09-12

## Research completed

Added `resources/research/060_pc2_inverter_contingency_action_report_loop.md`.

Primary mission-specific evidence from the Apollo 13 PC+2 burn-rule read-up and crew readback establishes the operational order:

1. inverter warning/light observed;
2. crew tries switching inverters;
3. warning is judged again after the switch;
4. if still on, the shutdown criterion is satisfied.

The reviewed primary material does **not** establish which alternate inverter would be selected, exact switch/circuit-breaker positions, a numeric dwell time, or the precise controller call sequence for a hypothetical failure that did not occur.

The Museum of Flight catalog confirms that the flown Apollo 13 LM-7 Contingency Checklist survives, but the accessible record reviewed in this pass does not expose the specific inverter contingency details. It is retained as a future source target rather than used to fill gaps by inference.

## Implementation completed

Added `src/apollo_mission_control/procedural_exchange.py` with a minimal procedural communication ledger. It currently supports:

- CAPCOM crew-facing `instruction` events;
- crew `completion_report` events;
- generic `readback` event class support.

For the inverter rule, the exchange records only the sourced action name `switch_lm_inverter`; it rejects the temptation to invent an inverter number.

Expanded scenario injection initially to support an `lm_inverter_warning` observation target.

**Correction (2026-09-15):** research note 117 subsequently established a stronger information boundary. The reviewed primary schematics do not establish direct ground telemetry of the derived INVERTER caution. The implementation now keeps `lm_inverter_warning` as onboard state and uses a separate `crew_inverter_warning_report` observation for ground rule evaluation. A hidden onboard caution alone cannot authorize the transfer or satisfy the rule.

The shutdown-rule evaluator requires a distinct later post-switch **crew report** before the positive rule can trigger. No persistence timer is introduced.

Added `tests/test_inverter_contingency_loop.py` covering the first small end-to-end source-bounded loop:

```text
synthetic crew warning report
    -> rule NOT_EVALUABLE
CAPCOM instruction
    -> crew switch action
    -> crew completion report
unchanged pre-switch warning only
    -> rule still NOT_EVALUABLE
distinct post-switch crew warning report
    -> rule TRIGGERED
```

The test also confirms the rule evaluator still does not issue engine cutoff, create a generic abort state, or modify `shutdown_rule_triggers` automatically.

Updated the earlier operational-action tests to require the same distinct post-switch observation.

## Documentation updated

- `docs/ROADMAP.md`
- `docs/station-status/2026-09-12_pc2_inverter_warning.md`
- `resources/source-catalog/PC2_INVERTER_WARNING_SOURCES.md`
- `resources/research/060_pc2_inverter_contingency_action_report_loop.md`

## Current research boundary

The inverter contingency is now sufficiently represented for the first vertical slice without unsupported historical details. Remaining inverter gaps are display/procedure-detail gaps rather than blockers for the architecture.

The next research target is the **onboard thrust-monitor observation path behind the 77-percent PC+2 criterion**. This should begin with primary LM crew/display and propulsion documentation. If that path cannot be resolved efficiently, the next fallback is the attitude/rate shutdown path and its startup-transient wording conflict.

The singular 150-psi ground inlet-pressure aggregation remains deliberately deferred unless a direct CONTROL/procedure/display source becomes readily available.

## Test execution status

The new and revised tests are committed. No passing test claim is recorded in this entry unless the suite is successfully executed in the available runtime.
