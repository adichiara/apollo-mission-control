# Research Note 185 — LM-7 GDA measurement-channel semantics

Date: 2026-09-16

## Question

Can a primary LM-7 engineering artifact narrow the unresolved axis/sign semantics behind Apollo 13 GDA telemetry without inventing a conversion between the crew-facing `5.86 / 6.75` trim pair and the postflight actuator values in inches?

## Primary source recovered

**Lunar Module 7, 8, & 9 Elementary Functional Diagrams**, document `LED-267-37C`.

Public scan: https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf

This is an LM-7/8/9 engineering document, directly applicable to Apollo 13's LM-7 hardware block.

The measurement index identifies the mission-block instrumentation channels:

- `GH1313V` — `VOLT, PITCH GDA POS (RET/EXT)`;
- `GH1314V` — `VOLT, ROLL GDA POS (EXT/RET)`;
- `GH1318X` — `PITCH TRIM EXTEND FROM LGC`;
- `GH1319X` — `PITCH TRIM RETRACT FROM LGC`;
- `GH1320X` — `PITCH GDA (EXT/RET)`;
- `GH1343X` — `ROLL TRIM EXTEND FROM LGC`;
- `GH1344X` — `ROLL TRIM RETRACT FROM LGC`;
- `GH1345X` — `ROLL GDA (RET/EXT)`.

## What this establishes

1. **Pitch and roll are the engineering-document axis names for the two LM-7 GDA channels.** The Apollo 13 Mission Report's `Pitch` and `Roll` labels therefore agree with the LM-7/8/9 hardware documentation; there is no need to relabel the second postflight actuator channel as yaw.

2. **The two axes do not share identical extension/retraction notation.** The analog position entries are explicitly `PITCH ... (RET/EXT)` and `ROLL ... (EXT/RET)`. The associated discrete GDA entries likewise use opposite parenthetical ordering. This is a real hardware/instrumentation polarity distinction and should be preserved in any telemetry model.

3. **Separate LGC trim-command discretes existed for extend and retract on each axis.** That supports modeling commanded trim direction separately from measured analog GDA position.

## What this does not establish

The measurement index does **not** provide enough information by itself to assert:

- the engineering-unit calibration of `GH1313V` or `GH1314V` from telemetry voltage to inches;
- which sign in the Apollo 13 Mission Report's inch values corresponds to EXT versus RET;
- a mapping from actuator inches to the crew-facing `5.86 / 6.75` angular trim numbers;
- the zero/reference convention for those crew-facing numbers;
- the T+55 mass-properties-to-trim computational lineage.

The opposite `RET/EXT` versus `EXT/RET` labels are therefore recorded as channel semantics, not converted into a guessed numerical sign rule.

## Simulation implication

For a station-facing CONTROL/GDA telemetry implementation:

- preserve `Pitch` and `Roll` as the two GDA actuator axes;
- preserve separate measured-position and trim-command concepts;
- retain the source's axis-specific extension/retraction polarity metadata;
- do not translate the Mission Report's signed inch values into EXT/RET state until the measurement calibration/sign definition is recovered;
- do not use the generic 3°/in mechanism ratio to derive the crew-facing trim numbers.

## Next archival target

The main priority remains the T+55 LM-burn deck -> RTCC/RTACF run -> `5.86 / 6.75` lineage. For the parallel representation target, seek the LM-7 instrumentation/calibration definition for `GH1313V` and `GH1314V` (or equivalent PCM/measurement-definition material) that maps telemetry voltage/sign to actuator displacement and EXT/RET direction.
