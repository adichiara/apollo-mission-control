# Apollo 13 PC+2 — alternate inverter identity after an inverter warning

Date: 2026-09-13  
Status: **RESOLVED for alternate inverter identity; transfer chronology subsequently resolved by research note 114.**

## Question

Research note 112 established that the Apollo 13 PC+2 burn configuration deliberately retained **inverter 2**, while the contemporaneous shutdown rule told the crew to shut down if an inverter light remained after they had tried **switching inverters**. The remaining question was whether the first playable may name inverter 1 as the alternate without inventing a mission-specific procedure.

## Primary evidence

### 1. Apollo 13 mission-specific configuration

The Apollo 13 air-ground procedure read-up at approximately 75:11–75:15 GET directed:

- `CB(16) INVERTER 2, CLOSE`; and
- deletion of the stock `Select Inverter 1` step.

This fixes the active PC+2 inverter as **inverter 2**. See note 112.

### 2. Apollo 13 shutdown-rule wording

At approximately 76:30–76:38 GET, CAPCOM read and Haise read back the inverter criterion as a shutdown condition when the inverter light remained **after switching / trying to switch inverters**.

The rule does not spell out a numbered alternate.

### 3. LM electrical architecture

The Apollo Operations Handbook — Lunar Module, Subsystems Data documents the LM AC section as using **two identical redundant inverters**. The same handbook identifies inverter 2 as the normal subsystem-activation source and inverter 1 as the other redundant unit, normally used for DPS/APS burns under the generic configuration.

Thus, in the mission-specific PC+2 state where inverter 2 is the selected source, the instruction to **switch inverters** has only one redundant inverter identity available: **inverter 1**.

## Interpretation

This note closes the **identity** question. Research note 114 subsequently recovers the Apollo 13 LM Malfunction Procedures sequence for the transfer itself.

Canonical first-playable mapping:

```text
PC+2 AC source = inverter 2
        ↓
inverter caution/light
        ↓
crew switches to the other redundant inverter = inverter 1
        ↓
observe whether inverter caution/light remains
        ↓
if it remains, shutdown criterion satisfied
```

The mapping `inverter 2 → inverter 1` is therefore an **architecture-constrained consequence of the mission-specific starting state plus the contemporaneous “switch inverters” rule**, not a verbatim recovered Apollo 13 sentence saying “select inverter 1.”

## What remains unresolved

This note does **not** establish:

- whether a MASTER ALARM reset is operationally relevant to the PC+2 shutdown decision beyond the separate INVERTER caution state;
- which crew member would execute the action;
- any dwell/persistence time before judging the warning;
- whether TELMU/CONTROL could independently observe the selected inverter position;
- the exact telemetry word or console display field used by TELMU/CONTROL;
- exact controller-to-CAPCOM wording for a failure that never occurred historically.

Those details remain unfrozen unless a direct procedural source is recovered or a later implementation dependency makes them necessary.

## First-playable consequence

It is acceptable to label the alternate inverter identity as **inverter 1**. Research note 114 additionally authorizes the sourced sequence `CB(11) EPS: INV 1 — close` → `INVERTER — 1` → `CB(16) EPS: INV 2 — open`.

No automatic transfer, numeric dwell, crew-member assignment, or hidden-state shortcut is authorized.

## Sources

1. NASA Apollo 13 Mission Commentary / air-ground transcript, approximately 74:55–75:15 and 76:30–76:38 GET. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
2. Grumman/NASA, *Apollo Operations Handbook — Lunar Module, Subsystems Data*, LMA790-3-LM, §2.5.3.3 A-C Section. Public scan: https://web.mit.edu/digitalapollo/Documents/Chapter8/lemhandbook.pdf
3. Apollo 13 Flight Journal, Day 4 Part 1, transcript presentation used as a navigation aid to the NASA transcript. https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html

## Relationship to earlier notes

- Note 111 remains superseded on its initial PC+2 inverter-selection synthesis.
- Note 112 remains canonical for the mission-specific **initial inverter 2** selection.
- This note resolves the remaining **alternate identity** question.
- Note 114 is canonical for the exact inverter-2 → inverter-1 transfer procedure.
