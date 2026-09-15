# Apollo 13 PC+2 — inverter contingency action/report loop

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED BOUNDARY — sufficient to define the decision/action/re-observation loop. Research notes 113–114 subsequently resolve alternate inverter 1 and the inverter-2 → inverter-1 cockpit transfer sequence. Numeric post-transfer dwell, crew-member assignment, and exact hypothetical controller voice routing remain unresolved.**

## Purpose

Research note 059 established that the PC+2 inverter criterion is not a simple warning-light shutdown condition. The crew-facing rule requires an inverter switch attempt before the warning can become a positive shutdown criterion.

This note asks the next implementation question:

> What minimum controller/CAPCOM/crew exchange preserves the sourced inverter contingency while keeping crew action, completion report, and fresh post-transfer observation distinct?

## 1. Mission-specific rule wording

At approximately 76:30 GET, CAPCOM read the PC+2 burn rules to the crew. The air-ground record states that shutdown is required for an inverter light **after switching inverters**.

The crew readback at approximately 76:37 GET restates the condition more explicitly: an inverter light **if it is still on after we've tried switching inverters**.

This establishes the operational order:

1. inverter warning/light is observed;
2. switching inverters is attempted;
3. the warning is observed again after the switch;
4. if the warning remains, the shutdown criterion is satisfied.

Primary mission-specific sources:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970, PC+2 Mission Rules review.
- Apollo 13 technical/PAO air-ground transcript at approximately 76:30–76:38 GET.

## 2. CAPCOM/crew communication boundary

The rule itself was transmitted by CAPCOM and read back by the crew. This supports the existing project architecture in which crew-facing procedural instructions and confirmations use the CAPCOM/air-ground path rather than appearing directly at every controller station.

For a nonnominal inverter event during the burn, the minimum defensible simulation loop is therefore:

```text
inverter warning observation
        ↓
TELMU/CONTROL interpretation/recommendation
        ↓
FLIGHT decision/authorization
        ↓
CAPCOM crew-facing instruction
        ↓
crew inverter-switch attempt
        ↓
crew completion/report event
        ↓
post-switch warning observation
        ↓
TELMU/CONTROL rule interpretation
        ↓
FLIGHT/CAPCOM shutdown decision path
```

The exact historical speaker sequence for a hypothetical PC+2 inverter failure is not documented because the nominal mission did not encounter this failure. The chain above therefore represents documented role boundaries plus the explicit rule ordering, not a claim that a particular failure actually occurred.

## 3. What may be implemented now

The project may represent three distinct event classes:

### A. Crew-facing instruction

A timestamped CAPCOM communication event authorizing/requesting the already-documented contingency action.

This event should record:

- GET;
- sender (`CAPCOM`);
- recipient (`CREW`);
- action requested (`switch_lm_inverter`);
- provenance/reference.

Research notes 113–114 now supply the mission-specific identity and transfer sequence. Current implementation may encode inverter 2 → inverter 1 and the three sourced controls, while still avoiding invented controller wording or response timing.

### B. Crew operational action

The existing `switch_lm_inverter` operational action remains appropriate.

It records only that an inverter-switch attempt occurred and when. It must not automatically clear the warning or generate a diagnosis.

### C. Crew completion/report event

A separate crew-report event may record that the requested action was performed. This is distinct from telemetry and distinct from the resulting inverter-warning state.

The report need not claim an exact historical phrase.

## 4. Post-switch observation

The inverter-warning observation after the switch must remain an independent onboard/telemetry product.

Therefore:

```text
crew says switch completed
```

must not imply:

```text
warning cleared
```

or:

```text
warning remains
```

The electrical/source-condition model or scenario injection determines the subsequent warning state. Rule evaluation then uses that post-action observation.

## 5. No invented persistence timer

Neither the Mission Operations Report nor the reviewed air-ground record establishes a numeric delay such as 1, 2, or 5 seconds before judging the post-switch warning.

The LM-5-and-later inverter-caution circuitry already included selection-transient inhibition while valid voltage/frequency processing was established (research note 059). That supports waiting for a meaningful post-switch observation, but does not justify an arbitrary software timer.

Implementation should therefore evaluate the positive rule only from an observation whose timestamp is later than or equal to the recorded switch attempt and which is explicitly marked as post-switch/current.

## 6. Unresolved procedure details

The current primary-source record still does **not** establish for this PC+2 contingency:

- exact crew member performing the action;
- exact controller who would first call the warning;
- exact delay before the warning is judged again;
- whether the ground could independently confirm the switch position or relied on crew report/procedure execution.

Subsequent research recovered the Apollo 13 LM Malfunction Procedures INVERTER caution flowchart and resolved the transfer controls; see research note 114. The remaining items above stay unfrozen.

## 7. Implementation consequence

The first end-to-end nonnominal loop should test information/action separation rather than inventing a historical failure:

1. inject a synthetic inverter-warning observation during the burn;
2. confirm the rule is not yet positive;
3. record a CAPCOM contingency instruction;
4. record crew execution of `switch_lm_inverter`;
5. record a crew completion report;
6. supply a post-switch warning observation that remains on;
7. confirm the rule becomes `TRIGGERED`;
8. confirm no engine cutoff or generic abort occurs automatically.

The warning values/times in such a test are implementation fixtures, not reconstructed Apollo 13 events.

## 8. Next research boundary

After this loop is implemented, the next high-value unresolved item should be selected from:

- exact crew/onboard thrust-monitor observation path for the 77-percent criterion;
- attitude/rate shutdown observation paths and the start-transient wording conflict;
- singular 150-psi inlet-pressure ground-product aggregation if a direct CONTROL source becomes available.

Selection should again follow strongest accessible primary evidence rather than convenience.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- Apollo 13 Flight Journal / underlying air-ground record, 076:30:31–076:38 GET, PC+2 burn-rule read-up and crew readback.
- NASA, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA report 19720018206, inverter-caution processing.
- Apollo 13, *LM Malfunction Procedures*, LMA790-3-LM, INVERTER caution flowchart; see research note 114.