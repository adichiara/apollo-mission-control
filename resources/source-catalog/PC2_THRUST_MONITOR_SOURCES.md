# PC+2 Onboard Thrust-Monitor Source Addendum

Status: **active supplement to `PC2_IMPLEMENTATION_SOURCES.md`**

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 28 Apr 1970
- **Status:** PRIMARY / REVIEWED
- **Use:** establishes distinct PC+2 thrust criteria: approximately 85-psi ground chamber pressure and approximately 77-percent onboard thrust.
- **Constraint:** does not itself name the onboard instrument pointer.

## Apollo 13 technical/PAO air-ground transcript

- **Interval:** approximately 76:30–76:38 GET
- **Status:** PRIMARY / REVIEWED
- **Use:** CAPCOM calls the crew-side criterion a “thrust monitor readout, 77 percent or below”; crew readback repeats the thrust-monitor threshold.
- **Constraint:** transcript wording alone does not identify the exact pointer, but it establishes a crew-visible percent-thrust readout.

## Apollo Operations Handbook — Lunar Module, Subsystems Data

- **Organization:** Grumman/NASA Apollo LM program documentation
- **Status:** PRIMARY TECHNICAL / REVIEWED
- **Use:** identifies the panel-1 dual-scale **CMD THRUST / ENG THRUST** indicator. CMD displays commanded thrust; ENG displays actual engine thrust. ENG input is derived from a descent-engine combustion-chamber pressure transducer because thrust is proportional to chamber pressure. The ENG scale is expressed in percent thrust and reads approximately 92.5 percent at the fixed full-throttle position.
- **Implementation relevance:** this is the first reviewed primary technical source that directly matches the Apollo 13 rule's required onboard percent-thrust indication.

## Apollo 13 LM Malfunction Procedures

- **Document type:** Flight Data File / mission-specific LM malfunction procedures
- **Status:** PRIMARY / REVIEWED-PARTIAL
- **Use:** Apollo 13 CES/MPS malfunction material explicitly uses **ENG THRUST** and **CMD THRUST** indicator terminology and treats disagreement between them as a propulsion/control symptom.
- **Implementation relevance:** confirms the indicator family was part of Apollo 13 operational crew vocabulary, rather than only a generic earlier LM design description.

## LM guidance program documentation

- **Status:** PRIMARY TECHNICAL / REVIEWED-PARTIAL
- **Use:** distinguishes LM P40 (DPS powered flight) from P47 (Thrust Monitor).
- **Key constraint:** PC+2 was executed in P40; the existence of P47 does not justify mapping the 77-percent rule to P47.

## LM thrust-to-weight indicator technical material

- **Status:** PRIMARY TECHNICAL / REVIEWED-PARTIAL
- **Use:** establishes the separate T/W indicator as an accelerometer/thrust-to-weight display calibrated in lunar-gravity terms.
- **Key constraint:** it is not the percent-thrust instrument identified for this rule.

## Research records

- `resources/research/061_pc2_onboard_thrust_monitor_observation_path.md` — original bounded gap.
- `resources/research/107_pc2_onboard_thrust_indicator_identification.md` — follow-up identification pass.

## Current interpretation

The historical instrument family is now identified with high confidence:

```text
Apollo 13 “thrust monitor readout”
    -> panel-1 CMD THRUST / ENG THRUST indicator
    -> ENG THRUST scale for actual engine thrust
```

This is a source-backed functional inference rather than a verbatim Apollo 13 sentence naming the ENG pointer. The distinction remains documented.

The executable rule remains `NOT_EVALUABLE` for a narrower reason: the first playable does not yet contain a source-bounded crew ENG THRUST observation/applicability state, and the exact point at which the 77-percent limit becomes active after the commanded 12.6-percent/40-percent startup segments remains unresolved.

Do not alias the crew indication to ground `GQ6510P`, synthesize a percent gauge from hidden engine state, or invent a startup activation time.
