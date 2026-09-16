# Station status — PC+2 automatic GDA trim boundary

Date: 2026-09-16

## CONTROL

Evidence maturity improves for interpreting the GDA values already recovered from the 61:29 free-return sequence. NASA Apollo 13 mission material establishes that DPS gimbal trim compensates for changing center of gravity and can be automatically accomplished by PGNS or AGS. The Apollo 13 LM131 flight-software listing independently contains the powered-flight trim-gimbal control law.

Mission-specific postflight evidence now also establishes that the 61:29 maneuver was flown with primary guidance/AUTO, guidance performance was nominal, no vehicle attitude excursions were reported, and firing time was as predicted. The propulsion report records a 34.3-second firing at minimum throttle (12% reported postflight) for 5 seconds followed by approximately 37% throttle.

Mission Report Table 6.4-I provides a separate maneuver-outcome quantity: velocity residual after trim of `+0.2 / 0.0 / +0.3 ft/s` (X/Y/Z). Research Note 182 classifies these strictly as translational velocity residuals. They are not GDA angles, gimbal errors, or a trim-acceptance tolerance.

### Supported

- CONTROL's preburn checkout role remains directly evidenced.
- `5.86 / 6.75` remains a sourced commanded/preburn GDA reference.
- Powered-flight gimbal trim is not necessarily static at the commanded starting values.
- The 61:29 vehicle attitude response can be represented as nominal/stable at the mission-report level; this does not establish exact actuator position.
- Post-trim maneuver residual may be represented as approximately `[+0.2, 0.0, +0.3] ft/s`.
- Executed throttle behavior should be distinguished from the nominal 10%/40% preburn pad.
- CONTROL's preburn `within about 0.3` checkout statement must remain separate from the postburn `+0.3 ft/s` velocity residual.

### Still unresolved

- exact T+55 mass-properties inputs and load/run lineage;
- CONTROL's alternative numerical trim;
- PC+2 ground-computation comparison criterion;
- exact powered-flight GDA history and post-61:29 actuator state.

The Apollo 13 GN&C performance-analysis supplement (`NTRS 19730017939`) remains a priority primary-source target for the last item. No station maturity grade is raised solely by these findings.