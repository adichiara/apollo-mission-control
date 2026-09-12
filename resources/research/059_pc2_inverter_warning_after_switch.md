# Apollo 13 PC+2 — inverter warning after switching inverters

Date: 2026-09-12  
Status: **REVIEWED-PARTIAL — sufficient to separate the inverter caution indication from the switch action and to identify the LM-5-and-later caution-generation path; exact PC+2 switch procedure/timing and controller information path remain unresolved.**

## Purpose

Research note 058 made the fuel/oxidizer differential-pressure rule executable without inventing its internal ground transformation. The next unresolved PC+2 shutdown criterion is the inverter warning condition.

Question:

> What does the Apollo 13 phrase “inverter light after switching inverters” actually constrain, and can it be represented without inventing a persistence delay or crew procedure?

## 1. Apollo 13 mission-specific rule

The Apollo 13 Flight Control Division *Mission Operations Report* lists a persistent inverter-warning condition among the PC+2 shutdown criteria. The air-ground rule read-up around 76:30 GET expresses the crew-facing rule as an **inverter light after switching inverters**.

This wording establishes that the criterion is not simply:

> inverter caution light on → shutdown

The switch action is part of the criterion.

Primary mission-specific sources:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- Apollo 13 technical/PAO air-ground transcript near 76:30 GET.

## 2. What the LM inverter caution represented

The NASA *Apollo Experience Report — Lunar Module Instrumentation Subsystem* documents the electrical-power inverter caution path.

The report identifies inverter AC quality measurements including:

- inverter bus frequency, measurement `GC0155`;
- inverter bus voltage, measurement `GC0071`.

The caution logic shown in the report responds to out-of-limit inverter output, including approximately:

- frequency above 402 Hz;
- frequency below 398 Hz;
- voltage below 112 Vac.

The caution indication is therefore tied to inverter output voltage/frequency quality rather than being a generic “inverter failed” Boolean.

Primary source:

- NASA, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA technical report 19720018206, inverter caution discussion and Figure 27.
  https://www.ibiblio.org/apollo/Documents/19720018206.pdf

## 3. LM-5-and-later selection-transient handling

The same report describes an important hardware change for **LM-5 and subsequent vehicles**. Apollo 13 flew LM-7, so this applicability includes the mission vehicle.

For these vehicles, removal of the inverter-caution inhibit during inverter selection was delayed until the selected inverter voltage had been processed by the Signal Conditioning Electronics Assembly / Caution and Warning Electronics Assembly path. The purpose was to prevent a normal inverter-selection transient from producing a misleading caution indication before valid voltage/frequency information existed.

This matters for PC+2 interpretation:

- a momentary selection transient should not be modeled as the documented positive shutdown criterion;
- the mission-rule wording “after switching inverters” is consistent with asking whether the alternate inverter still produces an out-of-limit caution after the switch;
- the source does **not** justify inventing an arbitrary persistence timer such as 1 s, 2 s, or 5 s.

## 4. Implementation boundary

The project may now safely distinguish at least two states/events:

1. `lm.inverter_warning` — the inverter caution indication resulting from the documented voltage/frequency monitoring path;
2. `lm.inverter_switch_attempted` — a crew/procedural action indicating that an inverter switch was actually attempted.

However, these are not the same information class:

- the warning is an onboard electrical/caution state that can reach Mission Control through instrumentation/telemetry;
- the switch attempt is a crew/procedure action and should not be silently inferred from the warning itself.

Therefore the positive rule should eventually be:

```text
inverter warning present
AND
inverter switch attempt has occurred
AND
warning remains present after that switch
```

without inventing a fixed time delay.

## 5. Current executable decision

Do **not** yet add `lm_inverter_switch_attempted` as a generic failure-injection target. A switch is an operational action, not a malfunction source condition.

The present shutdown evaluator behavior remains conservative:

- warning absent → rule clear;
- warning present without represented switch action → `NOT_EVALUABLE`.

The next implementation dependency is therefore an explicit crew/controller action/event path that can record an inverter switch attempt separately from fault injection.

Once that action path exists, a test may represent:

- warning present before switch;
- crew switches inverter;
- warning remains present afterward;
- rule evaluates `TRIGGERED`;
- no automatic engine cutoff or generic abort state is created.

## 6. What remains unresolved

The reviewed sources do not yet establish, for the PC+2 slice:

- exact initial inverter selection at the relevant instant;
- which alternate inverter would be selected by the contingency procedure;
- exact cockpit switch chronology;
- any required waiting interval before judging the post-switch light;
- exact telemetry word / TELMU or CONTROL display field used to observe the warning;
- whether the switch action was independently visible to the ground or known only from crew report/procedure execution.

These should remain explicit gaps.

## 7. Architecture consequence

This rule exposes a useful new distinction for the simulator:

```text
source failure / electrical condition
        ↓
inverter voltage & frequency
        ↓
caution/warning processing
        ↓
inverter warning

crew/controller decision
        ↓
crew switch action
        ↓
post-switch warning observation
        ↓
rule interpretation
```

The generic scenario-injection layer should continue to inject source conditions/observations, while operational actions such as switching an inverter belong to a separate action/event path.

## 8. Next work

The highest-value next implementation item is therefore **the minimal controller/crew action-event contract**, not another arbitrary malfunction field. It should be just large enough to represent an action such as an inverter switch, preserve its time/source/provenance, and let rule evaluation depend on the resulting observations.

This action layer should be implemented generically enough to support later CAPCOM/crew procedural actions, but should not yet imply a full crew simulator or command language.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- Apollo 13 technical/PAO air-ground transcript, ~76:30 GET.
- NASA, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA report 19720018206, inverter caution discussion/Figure 27.
  https://www.ibiblio.org/apollo/Documents/19720018206.pdf
