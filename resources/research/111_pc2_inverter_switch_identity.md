# Apollo 13 PC+2 — inverter-switch identity

Date: 2026-09-13  
Status: **SUPERSEDED IN PART BY RESEARCH NOTE 112.** The generic LM handbook evidence below remains valid, but the earlier first-playable conclusion that PC+2 operated on inverter 1 is withdrawn. Mission-specific Apollo 13 procedure evidence explicitly deleted `Select Inverter 1` and restored the inverter-2 feed for PC+2; note 112 is canonical for first-playable identity.

## Purpose

This note originally attempted to resolve which inverter was expected to be operating during the burn and which inverter was the alternate. The underlying generic handbook evidence was correctly recorded, but the synthesis did not give sufficient priority to the mission-specific Apollo 13 PC+2 modification.

## 1. Generic LM design convention

The Apollo LM Operations Handbook, subsystem data, electrical power section states that the two inverters are redundant and that the INVERTER switch selects which inverter feeds the AC buses. It further states that inverter 2 is normally used when LM subsystems are first activated, while **inverter 1 is the normal operating inverter during DPS and APS engine burns**.

Primary technical source:

- Grumman/NASA, *Apollo Operations Handbook — Lunar Module, Subsystems Data*, LMA790-3-LM, §2.5.3.3 A-C Section.
- Public scan: https://web.mit.edu/digitalapollo/Documents/Chapter8/lemhandbook.pdf

This documents the stock LM convention. It does **not** establish the Apollo 13 emergency PC+2 configuration.

## 2. Apollo 13 mission-specific evidence overrides the stock convention

The PC+2 contingency-checklist read-up instructed the crew to close `CB(16) INVERTER 2` and explicitly **scratch out `Select Inverter 1`** on page 17. Earlier in the same mission sequence, inverter 2 had been explicitly selected for LM AC use.

That mission-specific modification is direct evidence that the stock burn procedure's inverter-1 selection was intentionally not followed for PC+2.

See research note 112 for the corrected first-playable interpretation and complete source chain.

## 3. Crew-facing shutdown rule remains valid

At about 76:30 GET, CAPCOM told the crew to shut down for an inverter light **after switching inverters**. Haise read the rule back as an inverter light that is still on after they have tried switching inverters.

Primary mission-specific source:

- NASA Apollo 13 mission commentary / air-ground transcript, approximately 76:30–76:38 GET.

The criterion therefore still requires an attempted redundant-inverter transfer before a continuing inverter warning becomes a positive shutdown condition.

## 4. Corrected first-playable boundary

Canonical interpretation after note 112:

```text
PC+2 pre-burn selected source: inverter 2
          ↓
INVERTER caution/light
          ↓
crew attempts switch to redundant inverter
          ↓
post-switch inverter-light observation
          ↓
light remains present → shutdown criterion satisfied
```

This restriction was later closed by research notes 113–114. The current canonical action is the sourced inverter 2 → inverter 1 transfer using the Apollo 13 LM Malfunction Procedures sequence.

## 5. What remains unresolved

Do not invent:

- a fixed persistence timer for the light;
- automatic engine cutoff when the warning appears;
- automatic ground knowledge that the switch occurred unless represented by crew report/procedure state;
- an exact TELMU/CONTROL CRT field or telemetry word not otherwise sourced.

The LM-5-and-later caution-inhibit design documented in the LM instrumentation experience report still means a normal selection transient should not be treated as the positive post-switch warning condition.

## Sources

1. Grumman/NASA, *Apollo Operations Handbook — Lunar Module, Subsystems Data*, LMA790-3-LM, §2.5.3.3 A-C Section. https://web.mit.edu/digitalapollo/Documents/Chapter8/lemhandbook.pdf
2. NASA Apollo 13 Mission Commentary / air-ground transcript, ~72:48–73:15, ~74:55–75:15, and ~76:30–76:38 GET. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
3. NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970. https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
4. NASA, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA report 19720018206. https://www.ibiblio.org/apollo/Documents/19720018206.pdf

## Later resolution

Research note 113 resolves alternate inverter 1 identity. Research note 114 recovers the inverter-2 → inverter-1 cockpit transfer sequence. Those later notes are canonical for the post-warning action.
