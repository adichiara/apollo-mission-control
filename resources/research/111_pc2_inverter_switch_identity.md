# Apollo 13 PC+2 — inverter-switch identity

Date: 2026-09-13  
Status: **RESOLVED FOR FIRST-PLAYABLE IDENTITY — normal DPS-burn inverter 1; contingency alternate inverter 2. Exact cockpit switch chronology and post-switch judgement timing remain unresolved.**

## Purpose

Research notes 059–060 established the PC+2 rule semantics:

> an inverter light is a shutdown criterion only if it remains after the crew has tried switching inverters.

They intentionally left two questions open: which inverter was expected to be operating during the burn, and which inverter was the alternate.

## 1. LM design rule for powered descent/ascent burns

The Apollo LM Operations Handbook, subsystem data, electrical power section states that the two inverters are redundant and that the INVERTER switch selects which inverter feeds the AC buses. It further states that inverter 2 is normally used when LM subsystems are first activated, while **inverter 1 is the operating inverter during DPS and APS engine burns**.

Primary technical source:

- Grumman/NASA, *Apollo Operations Handbook — Lunar Module, Subsystems Data*, LMA790-3-LM, §2.5.3.3 A-C Section.
- Public scan: https://web.mit.edu/digitalapollo/Documents/Chapter8/lemhandbook.pdf

This is direct subsystem documentation for the LM design/operational convention and is applicable to the DPS-powered PC+2 maneuver.

## 2. Apollo 13 PC+2 preparation is consistent with inverter 2 as the alternate

The mission-specific PC+2 contingency-checklist read-up provides the relevant configuration evidence.

At about 74:55 GET, CAPCOM instructed Haise to perform the AC-bus power/temperature check in the order **inverter 2, then inverter 1**, and to leave the **EPS INVERTER 2 circuit breaker OPEN** after the check.

At about 75:15 GET, CAPCOM corrected the checklist reference and explicitly had the crew **CLOSE CB(16) INVERTER 2** before the burn procedure continued.

Primary mission-specific source:

- NASA Apollo 13 air-to-ground/mission commentary, approximately 74:55–75:15 GET.
- NASA PAO transcript: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- Transcript presentation preserving the same air-ground exchange: https://apollo13.spacelog.org/03%3A02%3A56%3A30/

The mission-specific sequence does not itself contain a sentence saying “operate on inverter 1, switch to inverter 2 on an inverter light.” It does, however, prepare inverter 2 and is consistent with the handbook rule that inverter 1 is the operating inverter for DPS burns.

## 3. Crew-facing shutdown rule

At about 76:30 GET, CAPCOM told the crew to shut down for an inverter light **after switching inverters**. Haise read the rule back as an inverter light that is still on after they have tried switching inverters.

Primary mission-specific source:

- NASA Apollo 13 mission commentary / air-ground transcript, approximately 76:30–76:38 GET.
- NASA PAO transcript: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf

This confirms that the contingency requires an attempted transfer to the redundant inverter before the inverter-light condition becomes a positive shutdown criterion.

## 4. First-playable interpretation

For the PC+2 first playable, represent the sourced configuration as:

```text
normal DPS-burn AC source: inverter 1
          ↓
INVERTER caution/light
          ↓
crew contingency action: select/switch to inverter 2
          ↓
post-switch inverter-light observation
          ↓
light remains present → shutdown criterion satisfied
```

The identity mapping is a **source-bounded synthesis** of:

1. the LM handbook’s explicit DPS-burn operating-inverter rule; and
2. Apollo 13’s mission-specific preparation of inverter 2 plus the contemporaneous “switch inverters” shutdown rule.

It is stronger than leaving the inverter numbers anonymous, but it is not presented as a verbatim Apollo 13 rule sentence.

## 5. What this does not authorize

Do not invent:

- an exact elapsed time the crew must wait after selecting inverter 2;
- a fixed persistence timer for the light;
- an exact switch-toggle/circuit-breaker chronology beyond the sourced preparation steps;
- automatic engine cutoff when the warning appears;
- automatic knowledge on the ground that the switch occurred unless represented by crew report/procedure state;
- an exact TELMU/CONTROL CRT field or telemetry word not otherwise sourced.

The LM-5-and-later caution-inhibit design documented in the LM instrumentation experience report still means a normal selection transient should not be treated as the positive post-switch warning condition.

## 6. Consequence for prior notes

Research note 059's unresolved bullets for **initial inverter selection** and **alternate-inverter identity** are closed for the current PC+2 first playable by this note.

Research note 060's generic action/report contract remains valid. Its action can now be represented specifically as an **inverter 1 → inverter 2** contingency transfer, while exact switch timing and post-switch persistence remain unresolved.

## Sources

1. Grumman/NASA, *Apollo Operations Handbook — Lunar Module, Subsystems Data*, LMA790-3-LM, §2.5.3.3 A-C Section. https://web.mit.edu/digitalapollo/Documents/Chapter8/lemhandbook.pdf
2. NASA Apollo 13 Mission Commentary / air-ground transcript, ~74:55–75:15 GET and ~76:30–76:38 GET. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
3. NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970, PC+2 shutdown-rule summary. https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
4. NASA, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA report 19720018206, inverter caution logic and LM-5-and-later selection-transient inhibit discussion. https://www.ibiblio.org/apollo/Documents/19720018206.pdf
