# Station status — PC+2 automatic GDA trim boundary

Date: 2026-09-16

## CONTROL

Evidence maturity improves for interpreting the GDA values already recovered from the 61:29 free-return sequence. NASA Apollo 13 mission material establishes that DPS gimbal trim compensates for changing center of gravity and can be automatically accomplished by PGNS or AGS. The Apollo 13 LM131 flight-software listing independently contains the powered-flight trim-gimbal control law.

### Supported

- CONTROL's preburn checkout role remains directly evidenced.
- `5.86 / 6.75` remains a sourced commanded/preburn GDA reference.
- Powered-flight gimbal trim is not necessarily static at the commanded starting values.

### Still unresolved

- exact T+55 mass-properties inputs and load/run lineage;
- CONTROL's alternative numerical trim;
- PC+2 ground-computation comparison criterion;
- exact powered-flight GDA history and post-61:29 actuator state.

No station maturity grade is raised solely by this finding.