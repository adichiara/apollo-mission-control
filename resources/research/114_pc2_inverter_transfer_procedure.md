# Apollo 13 PC+2 — inverter transfer procedure after an inverter warning

Date: 2026-09-13  
Status: **RESOLVED for first-playable cockpit transfer sequence; no numeric persistence dwell or crew-member assignment recovered.**

## Question

Research notes 112–113 established that Apollo 13's mission-specific PC+2 configuration retained **inverter 2**, and that the shutdown rule required trying the other inverter before treating a continuing inverter light as a shutdown condition. The remaining first-playable question was the exact cockpit transfer sequence from inverter 2 to inverter 1.

## Primary evidence

### Apollo 13 LM Malfunction Procedures

A surviving Apollo 13 *LM Malfunction Procedures* handbook scan, LMA790-3-LM, contains the INVERTER caution flowchart. The flowchart is written with inverter 2 as the operating source and states that, if inverter 1 is operating, references to inverter 2 are to be exchanged accordingly.

For the `Select alt inverter` action with inverter 2 operating, the procedure gives the sequence:

1. `CB(11) EPS: INV 1 — close`
2. `INVERTER — 1`
3. `CB(16) EPS: INV 2 — open`
4. re-observe whether the `INVERTER` caution light is off

This is directly compatible with the mission-specific PC+2 starting state established in note 112.

The same flowchart then branches on whether the inverter light has cleared. It does **not** provide a numeric dwell/persistence interval before that re-observation.

Public scan: https://www.ibiblio.org/apollo/Documents/Apollo%2013%20Malfunction%20Procedures.pdf

### LM electrical architecture cross-check

The Apollo Operations Handbook — Lunar Module, Subsystems Data (§2.5.3.3) independently documents the two-inverter architecture, the panel-11 inverter-1 feeder breaker, panel-16 inverter-2 feeder breaker, and the INVERTER selector. This corroborates the controls named in the Apollo 13 malfunction procedure.

Public scan: https://web.mit.edu/digitalapollo/Documents/Chapter8/lemhandbook.pdf

## Canonical first-playable interpretation

For a PC+2 inverter caution while operating on inverter 2:

```text
INVERTER caution
      ↓
CB(11) EPS: INV 1 — CLOSE
      ↓
INVERTER selector — 1
      ↓
CB(16) EPS: INV 2 — OPEN
      ↓
re-observe INVERTER caution
      ↓
light remains → PC+2 shutdown criterion satisfied
light clears   → criterion not satisfied on this evidence
```

This replaces the previous generic `switch to inverter 1` placeholder with a directly sourced Apollo 13-era cockpit sequence.

## What remains unresolved

This source does **not** establish:

- a numeric wait/dwell time before judging whether the caution remains;
- which astronaut would execute the transfer during the hypothetical PC+2 failure;
- exact controller-to-CAPCOM wording for commanding the transfer;
- whether TELMU/CONTROL independently saw the selector position or only electrical/caution consequences;
- the exact telemetry word or CRT field used by TELMU/CONTROL;
- whether a MASTER ALARM reset would be operationally relevant to the PC+2 shutdown decision beyond the separate INVERTER caution state.

No such details should be invented.

## First-playable consequence

The first playable may now represent the crew transfer action as the ordered three-control sequence above. The sequence remains a **crew action** downstream of CAPCOM communication and must not become an automatic controller-side state mutation.

The post-transfer shutdown decision still depends on a **fresh observation that the INVERTER caution remains**. No fixed persistence timer is authorized.

## Relationship to earlier notes

- Note 112 remains canonical for the mission-specific **initial inverter 2** selection.
- Note 113 remains canonical for the **alternate inverter 1 identity**.
- This note closes the previously preserved uncertainty about the exact inverter-2-to-inverter-1 cockpit transfer chronology.
- Notes 059–060 remain applicable for warning semantics and the action/report/re-observation loop, subject to this now-sourced control sequence.
