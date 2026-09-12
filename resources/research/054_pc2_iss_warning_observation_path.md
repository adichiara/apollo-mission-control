# Apollo 13 PC+2 — ISS warning observation path

Date: 2026-09-12  
Status: **REVIEWED — sufficient to model the ISS-warning observation and evaluate the documented ISS-warning + program-alarm shutdown criterion; exact PC+2 CRT field placement remains unresolved**

## Purpose

Resolve the first deferred positive shutdown-rule observation path from research note 053 without inventing an analog measurement or unsupported failure value.

The selected path is the PC+2 criterion:

> inertial-reference / ISS warning **plus** computer program alarm.

The question for implementation is whether the ISS warning can be represented as a distinct onboard/telemetry observation rather than as a generic guidance-health flag.

## Primary evidence

### 1. Apollo 13 Mission Operations Report

The Flight Director report records the PC+2 Mission Rules review at approximately 76:00 GET. One mandatory shutdown condition was an inertial-reference-system warning light combined with a computer program alarm.

This establishes that the rule is conjunctive: neither observation should be silently replaced by one generic Boolean.

Source: NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, p. III-25.

### 2. Apollo Operations Handbook — Lunar Module, GN&CS subsystem

The contemporary LM operations-handbook GN&CS material shows the DSKY/display-and-keyboard assembly with separate warning paths. Figure 2.1-33 identifies an **ISS WARNING SIGNAL** and an **LGC WARNING SIGNAL** as distinct outputs to the **Instrumentation Subsystem**.

The same figure shows the DSKY caution/status indications and the surrounding condition-indicator circuitry. This is direct systems evidence that ISS warning is a discrete onboard warning signal and that it has an instrumentation path; it is not merely a prose diagnosis produced by the ground.

Source family: Grumman, *Apollo Operations Handbook, Lunar Module, Volume I — Subsystems Data*, LMA790-3-LM, GN&CS section, Figure 2.1-33, p. 2.1-78. The searchable LM-10-and-subsequent edition has Basic Date 1 February 1970.

Configuration caution: the searchable public copy is LM-10-and-subsequent, while Apollo 13 flew LM-7. The project has already documented this handbook chronology difference. This source is used here only for the signal-path architecture that is also consistent with mission-specific Apollo 13 rule language. It is not used to assert a mission-specific CRT layout or exact LM-7 wiring revision without further evidence.

### 3. Contemporary LUMINARY functional-description material

LM PGNCS functional-description material describes separate LGC and ISS warning indications in the crew caution/warning system and states that the ISS warning is under LGC program control. This supports treating `iss_warning` as a discrete onboard guidance warning state rather than deriving it from alignment error or from a program alarm.

The detailed logic identifies multiple possible inertial-system failure contributors. Those individual failure mechanisms are **not required** for the first PC+2 rule-path test and are not frozen into the scenario model here.

## Implementation consequence

The minimum model may now include:

- `pg_ns.iss_warning` — Boolean onboard warning state;
- `pg_ns.lgc.program_alarm` — existing optional program-alarm observation/code;
- a controller projection carrying ISS warning through an `onboard/telemetry` source layer;
- rule evaluation requiring **both** observations to be active.

The rule evaluator should behave as follows when both observations are modeled:

| ISS warning | program alarm | rule result |
|---|---|---|
| false | absent | `clear` |
| true | absent | `clear` |
| false | present | `clear` |
| true | present | `triggered` |

This replaces the earlier `not_evaluable` positive-program-alarm branch, because the missing observation path is now modeled.

## First nonnominal validation case

The first source-backed nonnominal rule test should inject only the **observations required by the documented criterion**:

- ISS warning = true;
- program alarm = present.

It should then verify that the derived audit rule is `triggered` while the authoritative mission state does **not** automatically issue an abort/shutdown command.

The test should not invent:

- a specific PC+2 failure mechanism;
- a specific program-alarm number;
- a specific historical Apollo 13 occurrence;
- exact ground CRT placement.

This is therefore a rule-path validation case, not a claim that this malfunction actually occurred during PC+2.

## Remaining uncertainty

- exact Apollo 13/LM-7 telemetry channel/word for ISS warning;
- exact GUIDO CRT field or display used to see the warning during PC+2;
- exact individual failure mechanism for the first future narrative/non-nominal scenario.

These do not block the rule-path model because the existence of the distinct warning and instrumentation path is established.

## Sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, p. III-25.  
  https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- Grumman, *Apollo Operations Handbook, Lunar Module, Volume I — Subsystems Data*, LMA790-3-LM, GN&CS Figure 2.1-33.  
  https://www.ibiblio.org/apollo/Documents/LMA790-3-LM10-ApolloOperationsHandbookLunarModuleLM10AndSubsequent-Volume1-SubsystemsData-SearchableText.pdf
- Contemporary LUMINARY functional-description material, PGNCS caution/warning discussion.  
  https://www.ibiblio.org/apollo/Documents/sundance_functional_description_vol1.pdf
