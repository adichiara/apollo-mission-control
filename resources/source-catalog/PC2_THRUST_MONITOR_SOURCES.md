# PC+2 Onboard Thrust-Monitor Source Addendum

Status: **active supplement to `PC2_IMPLEMENTATION_SOURCES.md`**

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 28 Apr 1970
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- **Status:** PRIMARY / REVIEWED
- **Use:** establishes distinct PC+2 thrust criteria: approximately 85-psi ground chamber pressure and approximately 77-percent onboard thrust; independently records the staged throttle profile of about 5 seconds at 12.6 percent, 21 seconds at 40 percent, then maximum thrust.
- **Constraint:** does not itself name the onboard instrument pointer or state the exact 77-percent applicability gate.

## Apollo 13 Technical Crew Debriefing

- **Organization:** NASA Manned Spacecraft Center, Flight Crew Support Division
- **Date:** 24 Apr 1970
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/a13-techdebrief.pdf
- **Relevant section:** 9, p. 9-2
- **Status:** PRIMARY / REVIEWED
- **Use:** Lovell states that PC+2 used 5 seconds at idle/low thrust, 21 seconds at 40-percent throttle, and the remainder at full throttle; he further states that the configured transition to full throttle occurred at **26 seconds** after engine start. Haise states that ENGINE THRUST gauge observation was the clear cue that the engine was lit.
- **Implementation relevance:** supplies a mission-specific, crew-observed phase boundary that can gate the 77-percent criterion without inventing an arbitrary activation delay.

## Apollo 13 technical/PAO air-ground transcript

- **Interval:** approximately 76:30–76:38 GET
- **URL:** https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- **Status:** PRIMARY / REVIEWED
- **Use:** CAPCOM calls the crew-side criterion a “thrust monitor readout, 77 percent or below”; crew readback repeats the thrust-monitor threshold. The surrounding rule discussion ties PC+2 to the LOI Mode I abort-rule family.
- **Constraint:** transcript wording alone does not identify the exact pointer or throttle-regime qualifier.

## Apollo Operations Handbook — Lunar Module, Subsystems Data

- **Organization:** Grumman/NASA Apollo LM program documentation
- **Status:** PRIMARY TECHNICAL / REVIEWED
- **Use:** identifies the panel-1 dual-scale **CMD THRUST / ENG THRUST** indicator. CMD displays commanded thrust; ENG displays actual engine thrust. ENG input is derived from a descent-engine combustion-chamber pressure transducer because thrust is proportional to chamber pressure. The ENG scale is expressed in percent thrust and reads approximately 92.5 percent at the fixed full-throttle position.
- **Implementation relevance:** directly matches the Apollo 13 rule's required onboard percent-thrust indication.

## Apollo 13 LM Malfunction Procedures

- **Document type:** Flight Data File / mission-specific LM malfunction procedures
- **Status:** PRIMARY / REVIEWED-PARTIAL
- **Use:** Apollo 13 CES/MPS malfunction material explicitly uses **ENG THRUST** and **CMD THRUST** indicator terminology and treats disagreement between them as a propulsion/control symptom.
- **Implementation relevance:** confirms the indicator family was part of Apollo 13 operational crew vocabulary, rather than only a generic earlier LM design description.

## Apollo 10 Mission Rules — DPS lineage

- **Organization:** NASA Manned Spacecraft Center
- **Relevant item:** section 3, item 3-77, reviewed page dated 23 Apr 1969
- **Status:** PRIMARY / LINEAGE EVIDENCE
- **Use:** surviving DPS rule material conditions the fuel-inlet-pressure limit by throttle regime, including a >65-percent-throttle branch. Apollo 13's PC+2 rules were explicitly related to LOI Mode I abort rules.
- **Constraint:** this does **not** prove that Apollo 13 copied the Apollo 10 throttle qualifier verbatim. It supports the narrower conclusion that DPS abort criteria historically distinguished commanded low-thrust startup from high-throttle operation.

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
- `resources/research/107_pc2_onboard_thrust_indicator_identification.md` — instrument-identification pass.
- `resources/research/108_pc2_thrust_rule_applicability_gate.md` — bounded first-playable applicability resolution.

## Current interpretation

The historical instrument family is identified with high confidence:

```text
Apollo 13 “thrust monitor readout”
    -> panel-1 CMD THRUST / ENG THRUST indicator
    -> ENG THRUST scale for actual engine thrust
```

For the current first playable, the applicability gate is now bounded as:

```text
commanded 12.6% / 40% startup
    -> criterion inactive
commanded maximum/full-throttle segment
    -> ENG THRUST <=77% criterion applicable
```

The Apollo 13 crew debrief fixes the nominal full-throttle transition at **burn +26 seconds**. The final applicability mapping is a source-bounded lineage inference, not a recovered Apollo 13 sentence stating the qualifier verbatim.

The gate does not itself make the rule evaluable from hidden engine state. A scenario still needs an explicit crew-visible ENG THRUST observation; do not alias the crew indication to ground `GQ6510P` or synthesize a percent gauge directly from hidden physical truth.
