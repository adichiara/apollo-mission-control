# Research note 160 — Apollo 13 RTCC mass-properties no-update precedent

Date: 2026-09-15

## Question

Is there mission-specific primary evidence for how Flight Dynamics decided whether a newly run mass-properties solution required a trim update, even if the exact PC+2 working sheet remains unrecovered?

## Primary evidence

### Flight Control Division Mission Operations Report — Apollo 13

The Flight Dynamics/RETRO postflight narrative records, before MCC-2:

- the **T+25 RTCC mass properties were run**;
- **an update was not needed**;
- the stated reason was that the resulting pitch/yaw trims were **within 0.01° of T+6**.

Source: NASA Manned Spacecraft Center, MSC-02680, *Flight Control Division Mission Operations Report — Apollo 13*, 28 April 1970, Flight Dynamics/RETRO appendix, launch-through-MCC-2 chronology.

Primary scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf

The same report later states that RTCC LM-burn mass-property decks were updated to T+55 decks and that the ~59-hour PC+2 DPS trim disagreement arose because LM CONTROL had used premission mass properties rather than the better available data; CONTROL later agreed with Flight Dynamics.

## Finding

Apollo 13 therefore directly documents a controller-side **run -> compare -> update/no-update** workflow for mass-properties-derived trim. At T+25, a new RTCC mass-properties run did not automatically produce a crew/product update: Flight Dynamics compared its trims with the earlier T+6 reference and explicitly retained the prior values because the differences were within 0.01°.

This is the strongest mission-specific procedural precedent yet recovered for the unresolved PC+2 no-update decision.

## Critical boundary

Do **not** transfer the `0.01°` criterion to PC+2. The source states it for the T+25-versus-T+6 CSM/SPS context. PC+2 involved the docked CSM/LM stack, DPS, different mass-property decks, and an emergency operating context. No recovered source says CONTROL used the same tolerance at PC+2.

Likewise, this evidence does not prove:

- the numerical candidate PC+2 trim;
- the exact retained PC+2 two-axis gimbal state;
- a numbered PC+2 mass-properties job;
- that the 5.86°/6.75° free-return trim was generated directly from T+55;
- the numerical threshold used when the PC+2 Verb 48 sequence was terminated after Noun 47.

## Simulation implication

Represent mass-properties trim handling as an explicit decision process rather than assuming every calculation overwrites the active trim:

`reference mass-properties state -> new RTCC mass-properties run -> candidate trim -> comparison to current/reference trim -> controller update/no-update decision -> operational product state`

The comparison criterion must be scenario/source specific. For the documented Apollo 13 T+25 case, `<= 0.01° difference from T+6` is historically supported. For PC+2, leave the threshold unknown until directly sourced.

## Next archival target

Continue searching H-2 CONTROL/Flight Dynamics working records for the corresponding PC+2 comparison: candidate trim, retained/current trim, comparison delta/tolerance, mass-properties run/job identity, or an explicit controller note explaining why the Noun 48 update was unnecessary.