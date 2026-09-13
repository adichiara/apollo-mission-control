# Apollo 13 PC+2 — inverter warning after switching inverters

Date: 2026-09-12  
Status: **REVIEWED-PARTIAL — sufficient to separate the inverter caution indication from the switch action and to identify the LM-5-and-later caution-generation path. Research note 111 subsequently resolves the first-playable inverter identities as normal DPS-burn inverter 1 and contingency alternate inverter 2; exact post-warning switch chronology/timing and controller information path remain unresolved.**

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

The project may safely distinguish at least two states/events:

1. `lm.inverter_warning` — the inverter caution indication resulting from the documented voltage/frequency monitoring path;
2. `lm.inverter_switch_attempted` — a crew/procedural action indicating that an inverter switch was actually attempted.

These are not the same information class:

- the warning is an onboard electrical/caution state that can reach Mission Control through instrumentation/telemetry;
- the switch attempt is a crew/procedure action and should not be silently inferred from the warning itself.

Therefore the positive rule should be:

```text
inverter warning present
AND
inverter switch attempt has occurred
AND
warning remains present after that switch
```

without inventing a fixed time delay.

## 5. Current executable decision

Do **not** treat an inverter warning alone as an automatic shutdown command.

The shutdown evaluator behavior remains conservative:

- warning absent → rule clear;
- warning present without represented switch action → `NOT_EVALUABLE`;
- represented switch attempt followed by a continuing warning → eligible to evaluate the sourced shutdown criterion.

Research note 111 now narrows the first-playable action identity to a **normal inverter 1 → contingency inverter 2** transfer. That identity does not authorize inventing the detailed cockpit switch sequence or a post-switch timer.

## 6. What remains unresolved

Research note 111 closes the earlier gaps for:

- normal burn-time inverter identity: **inverter 1**;
- contingency alternate identity: **inverter 2**.

The following remain unresolved:

- exact cockpit switch/breaker chronology after the warning;
- any required waiting interval before judging the post-switch light;
- exact telemetry word / TELMU or CONTROL display field used to observe the warning;
- whether the switch action was independently visible to the ground or known only from crew report/procedure execution.

These should remain explicit gaps.

## 7. Architecture consequence

This rule exposes a useful distinction for the simulator:

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
crew switch action (PC+2 first playable: inverter 1 → inverter 2)
        ↓
post-switch warning observation
        ↓
rule interpretation
```

The generic scenario-injection layer should continue to inject source conditions/observations, while operational actions such as switching an inverter belong to a separate action/event path.

## 8. Follow-on work

The minimal controller/crew action-event contract developed after this note remains the correct abstraction. Research note 111 adds the source-bounded inverter-number mapping; it does not create a need for another malfunction field or a detailed electrical simulator.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- Apollo 13 technical/PAO air-ground transcript, ~76:30 GET.
- NASA, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA report 19720018206, inverter caution discussion/Figure 27.
  https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- See research note 111 for the LM Operations Handbook and Apollo 13 PC+2 configuration evidence establishing the first-playable inverter 1 → inverter 2 identity.
