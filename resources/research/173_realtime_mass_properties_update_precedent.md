# Research note 173 — Apollo 13 real-time mass-properties update precedent

Date: 2026-09-15

## Question

Can the primary Apollo 13 Flight Control Division record further constrain how real-time mass-properties updates and trim-change decisions were handled, without inventing the still-missing PC+2 calculation chain?

## Primary source

NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970. NASA History scan: `https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf`; NTRS record/download: `19710010485`.

The report explicitly states that it tells the flight operation as seen in real time and that **no data is used except data available in real time**, even where later post-mission information showed the real-time data to be wrong. This makes the Flight Dynamics chronology unusually strong evidence for what information was operationally available to controllers.

## Findings

### 1. Apollo 13 had a documented real-time mass-properties rerun/update decision before the accident

In the Flight Dynamics chronology, after the T+24 telescope-data activity and before MCC-2, the report states that the **T+25 RTCC mass properties were run but an update was not needed because pitch/yaw trims were within 0.01 degree of T+6**.

This establishes, for Apollo 13 itself, a real-time workflow in which:

`time-tagged mass-properties set -> RTCC mass-properties run -> pitch/yaw trim comparison -> update/no-update decision`

It also proves that a numerical trim-difference criterion of `0.01°` was operationally relevant in at least this specific T+25-versus-T+6 update decision.

### 2. The later T+55 LM-burn deck update is also real-time evidence

In the same Flight Dynamics chronology, under MCC-2 through PC+2, the report states that **RTCC (LM burn) mass property decks were updated to T+55 decks**. Because of the report's explicit real-time-only evidence policy, this is not a postflight reconstruction: the T+55 deck family was operationally available in real time before the accident/abort calculations described immediately afterward.

### 3. This strengthens, but does not close, the ~59 GET PC+2 provenance chain

The same chronology later states that the DPS trim passed on the ~59 GET PC+2 abort pad was challenged by LM CONTROL, that CONTROL had used **premission mass properties**, and that CONTROL later agreed with Flight Dynamics' data because the premission basis was not the best data available.

The chronology therefore places all of the following in the same real-time Flight Dynamics record:

- T+55 LM-burn mass-property decks available before the accident;
- a ~59 GET Flight Dynamics PC+2 DPS trim passed to the crew;
- a competing CONTROL solution based on premission mass properties;
- subsequent CONTROL acceptance of Flight Dynamics' data.

This materially strengthens the hypothesis that the newer time-tagged LM-burn mass-properties context explains why Flight Dynamics' solution superseded CONTROL's premission calculation. **It still does not explicitly say that the `5.86° / 6.75°` pair was computed from a particular T+55 deck or identify the job/request that did so.** That link remains unresolved.

## Important boundary on the `0.01°` value

The T+25 entry is direct mission-specific evidence that `0.01°` mattered for one mass-properties trim-update comparison. It is **not evidence that `0.01°` was a universal RTCC rule or the criterion used for the later PC+2 dispute**. In particular, the `0.01°` per-axis difference between the ~59 GET `5.86 / 6.75` pair and the later `5.85 / 6.74` retained-reference readback must not be explained by importing the T+25 criterion without a source explicitly making that connection.

## Simulator implication

A source-backed generic workflow may now represent a controller mass-properties update cycle as producing pitch/yaw trim values that can be compared with a prior time-tagged solution before deciding whether an update is required. For the Apollo 13 PC+2 historical scenario, however, the comparison threshold must remain unknown unless the specific PC+2 artifact is recovered.

## Next archival target

Continue seeking the Apollo 13 real-time weight/c.g./mass-properties output or request sheet behind the ~59 GET PC+2 pad, with priority on:

1. explicit T+55 deck/job linkage;
2. Flight Dynamics computed trim output corresponding to `5.86 / 6.75`;
3. CONTROL's premission-mass-properties alternative values;
4. comparison delta and PC+2-specific acceptance criterion;
5. RTCC/RTACF job/request identifier and calculation time.

The T+25 `0.01°` precedent should be used as a search discriminator, not as a substituted PC+2 value.