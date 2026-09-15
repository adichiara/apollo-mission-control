# Apollo 13 PC+2 — inverter warning after switching inverters

Date: 2026-09-12  
Status: **REVIEWED / SUPERSEDED IN PART — the caution/action separation remains valid. Research notes 112–114 subsequently resolve initial inverter 2, alternate inverter 1, and the three-control transfer sequence. Numeric post-transfer dwell and exact controller display/routing remain unresolved.**

## Purpose

This note asks what the Apollo 13 phrase “inverter light after switching inverters” constrains and how to represent it without inventing a persistence delay or crew procedure.

## 1. Apollo 13 mission-specific rule

The Apollo 13 Flight Control Division *Mission Operations Report* lists an inverter-warning condition among the PC+2 shutdown criteria. The air-ground rule read-up around 76:30 GET expresses the crew-facing rule as an **inverter light after switching inverters**; Haise reads it back as an inverter light still on after they have tried switching inverters.

This establishes that the criterion is not simply:

`inverter caution light on → shutdown`

The switch action is part of the criterion.

## 2. What the LM inverter caution represented

The NASA *Apollo Experience Report — Lunar Module Instrumentation Subsystem* documents the electrical-power inverter caution path. It identifies inverter bus frequency (`GC0155`) and voltage (`GC0071`) measurements and shows caution logic responding to out-of-limit inverter AC quality.

The indication is therefore tied to inverter output voltage/frequency quality rather than being a generic “inverter failed” Boolean.

## 3. LM-5-and-later selection-transient handling

The same report describes an LM-5-and-later hardware change applicable to Apollo 13 LM-7: removal of the inverter-caution inhibit during selection was delayed until valid processed inverter data were established. A normal selection transient should therefore not be represented as the positive post-switch shutdown condition.

The source does **not** justify inventing a 1 s, 2 s, 5 s, or other persistence timer.

## 4. Corrected mission-specific initial selection

Research note 112 revisits the actual Apollo 13 PC+2 read-up. At the -4 minute configuration step CAPCOM directed:

- `CB(16) INVERTER 2, CLOSE`; and
- **scratch `Select Inverter 1`.**

That direct mission-specific instruction overrides the generic LM handbook convention used in the earlier note-111 synthesis. The current first-playable initial source is therefore **inverter 2**, not inverter 1.

Later primary-source work closes this boundary. Research note 113 identifies inverter 1 as the only alternate in the mission-specific inverter-2 starting state, and research note 114 recovers the Apollo 13 LM Malfunction Procedures transfer sequence: close the inverter-1 feeder breaker, select inverter 1, then open the inverter-2 feeder breaker.

## 5. Implementation boundary

Safely distinguish:

1. `lm.inverter_warning` — onboard caution state from the documented voltage/frequency monitoring path;
2. `lm.inverter_switch_attempted` — crew/procedural action that a redundant-inverter switch was actually attempted.

Positive criterion:

```text
inverter warning present
AND
inverter switch attempt has occurred
AND
warning remains present after that switch
```

without inventing a fixed delay.

Initial PC+2 configuration is inverter 2. The sourced alternate action is the inverter-2 → inverter-1 transfer recovered in research note 114. The post-transfer caution remains a separate fresh observation; no numeric dwell is invented.

## 6. What remains unresolved

- any required waiting interval before judging the post-switch light;
- exact telemetry word / TELMU or CONTROL display field used to observe the warning;
- whether the switch action was independently visible to the ground or known only from crew report/procedure execution.

## 7. Architecture consequence

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
crew redundant-inverter switch attempt
        ↓
post-switch warning observation
        ↓
rule interpretation
```

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970.
- NASA Apollo 13 technical/PAO air-ground transcript, ~72:48–73:15, ~74:55–75:15, and ~76:30–76:38 GET.
- NASA, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA report 19720018206.
- Research note 112 for the mission-specific PC+2 selection correction.
- Research note 113 for alternate inverter 1 identity.
- Research note 114 for the sourced inverter-2 → inverter-1 cockpit transfer sequence.
