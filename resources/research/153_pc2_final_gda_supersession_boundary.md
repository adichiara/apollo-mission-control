# Research note 153 — Apollo 13 PC+2 final-GDA supersession boundary

Date: 2026-09-15

> **Correction (research note 154):** the LM CONTROL GDA quantities cited below are **actuator displacement in inches, not degrees**. The supersession conclusion remains valid, but the physical quantity must not be represented as an angular trim. The corrected pre-ignition roll-GDA displacement is approximately `-0.8 in`, followed by approximately `-2 in` at ignition.

## Question

Can the surviving mission-specific primary record prove that the ~59-hour interim DPS gimbal trim was superseded before the actual PC+2 burn, even if the complete final trim pair and mass-properties job remain unrecovered?

## Primary source

NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, Appendix H (LM CONTROL), PC+2 — DPS 2.

NASA/Apollo Journal scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf

LM CONTROL reports that the crew powered up for PC+2 at GET 78:00, maneuvered to final burn attitude at 79:17, and ignited at 79:27:38. At ignition, the **roll GDA actuator displacement** moved to approximately `-2 in`, described as a delta of `-1.2 in` from its pre-ignition value. This implies a pre-ignition roll-GDA displacement of approximately `-0.8 in` (`-2.0 - (-1.2)`). The report treats the motion as an unexpected compliance response, not as a commanded trim update at ignition.

The same mission report's Flight Dynamics chronology states that the final PC+2 pad went to the crew at about GET 78 hours based on the GYM 289 vector.

## Finding

The ~59-hour trim pair cannot have survived unchanged into PC+2 ignition. The restored air-ground record at GET ~59:03 carried an interim pair of `5.86°` and `6.75°` and explicitly said the angles would be updated. The mission-specific LM CONTROL postflight report independently bounds the later roll-axis actuator state: immediately before PC+2 ignition the roll GDA displacement was approximately `-0.8 in`, then moved to approximately `-2 in` as the engine responded at ignition.

Therefore the historical product lifecycle contains at least:

`~59 h interim angular trim (update expected) -> later superseding trim/state -> ~79:27 pre-ignition roll GDA actuator ≈ -0.8 in -> ignition compliance response ≈ -2 in`

The complete later commanded angular trim pair is still not recovered.

## Axis-label correction

Research note 152 and several derivative project documents called the second ~59-hour value a **yaw** trim. That is too strong. The air-ground exchange itself is confused: CAPCOM initially describes the values generically, Lovell suggests pitch/yaw, and Haise's final accepted readback gives pitch and roll. More importantly, the mission-specific LM CONTROL report describes the relevant DPS actuator as the **roll GDA**. Project documentation should therefore record the interim pair conservatively as `pitch 5.86° / roll 6.75°` (or simply the two DPS GDA angular values) rather than normalize the second value to yaw.

## Boundary retained

Do not infer:

- the final commanded pitch/roll angular trim pair;
- that the approximately `-0.8 in` actuator displacement was a pad-printed value;
- a degrees↔inches conversion without sourced GDA geometry/calibration;
- which numbered mass-properties job produced the superseding trim;
- that the superseding trim came specifically from `T+55`;
- that the GYM 289 targeting vector itself encoded the GDA values;
- exact compliance mechanics beyond what LM CONTROL reports.

The `-0.8 in` value is approximate arithmetic derived directly from the report's approximate `-2 in` state and `-1.2 in` delta.

## Simulation implication

Represent commanded angular trim separately from observed actuator displacement and engine-compliance response. A maneuver product may be superseded before execution, and ignition can produce a further physical GDA displacement without implying a new targeting product.

## Next archival target

Recover the final ~78-hour P30/GDA pad or Flight Director/Flight Dynamics working sheet that gives the complete superseding PC+2 angular trim pair and its provenance. The mass-properties job number and explicit `T+55` relationship remain unresolved.