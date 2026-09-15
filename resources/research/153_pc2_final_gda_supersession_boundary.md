# Research note 153 — Apollo 13 PC+2 final-GDA supersession boundary

Date: 2026-09-15

> **Correction (research note 155):** primary LM hardware documentation and the Apollo 13 FCD report establish that the LM CONTROL quantities below are angular GDA/engine-gimbal position in **degrees**. Research note 154 correctly identified the separate Mission Report telemetry table as actuator displacement in inches but overgeneralized that unit to this narrative. The pre-ignition roll-GDA angle is approximately `-0.8°`, followed by approximately `-2°` at ignition.

## Question

Can the surviving mission-specific primary record prove that the ~59-hour interim DPS gimbal trim was superseded before the actual PC+2 burn, even if the complete final trim pair and mass-properties job remain unrecovered?

## Primary source

NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, Appendix H (LM CONTROL), PC+2 — DPS 2.

NASA/Apollo Journal scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf

LM CONTROL reports that the crew powered up for PC+2 at GET 78:00, maneuvered to final burn attitude at 79:17, and ignited at 79:27:38. At ignition, the **roll GDA** moved to approximately `-2°`, described as a delta of `-1.2°` from its pre-ignition value. This implies a pre-ignition roll-GDA angle of approximately `-0.8°` (`-2.0 - (-1.2)`). The report treats the motion as an unexpected compliance response, not as a commanded trim update at ignition.

The same mission report's Flight Dynamics chronology states that the final PC+2 pad went to the crew at about GET 78 hours based on the GYM 289 vector.

## Finding

The ~59-hour trim pair cannot have survived unchanged into PC+2 ignition. The restored air-ground record at GET ~59:03 carried an interim pair of `5.86°` and `6.75°` and explicitly said the angles would be updated. The mission-specific LM CONTROL postflight report independently bounds the later roll-axis state: immediately before PC+2 ignition the roll GDA angle was approximately `-0.8°`, then moved to approximately `-2°` as the engine responded at ignition.

Therefore the historical product lifecycle contains at least:

`~59 h interim angular trim (update expected) -> later superseding trim/state -> ~79:27 pre-ignition roll GDA ≈ -0.8° -> ignition compliance response ≈ -2°`

The complete later commanded angular trim pair is still not recovered.

## Axis-label correction

Research note 152 and several derivative project documents called the second ~59-hour value a **yaw** trim. That is too strong. The air-ground exchange itself is confused: CAPCOM initially describes the values generically, Lovell suggests pitch/yaw, and Haise's final accepted readback gives pitch and roll. More importantly, the mission-specific LM CONTROL report describes the relevant DPS actuator as the **roll GDA**. Project documentation should therefore record the interim pair conservatively as `pitch 5.86° / roll 6.75°` (or simply the two DPS GDA angular values) rather than normalize the second value to yaw.

## Boundary retained

Do not infer:

- the final commanded pitch/roll angular trim pair;
- that the approximately `-0.8°` state was a pad-printed value;
- an exact degrees↔inches flight-unit conversion from generic hardware limits;
- which numbered mass-properties job produced the superseding trim;
- that the superseding trim came specifically from `T+55`;
- that the GYM 289 targeting vector itself encoded the GDA values;
- exact compliance mechanics beyond what LM CONTROL reports.

The `-0.8°` value is approximate arithmetic derived directly from the report's approximate `-2°` state and `-1.2°` delta.

## Simulation implication

Represent commanded angular trim separately from observed GDA/engine-gimbal angular position, linear actuator displacement, and engine-compliance response. Research note 155 establishes the generic hardware scale ±2 in ↔ ±6°, but it is not an exact LM-7 calibration.

## Next archival target

Recover the final ~78-hour P30/GDA pad or Flight Director/Flight Dynamics working sheet that gives the complete superseding PC+2 angular trim pair and its provenance. The mass-properties job number and explicit `T+55` relationship remain unresolved.