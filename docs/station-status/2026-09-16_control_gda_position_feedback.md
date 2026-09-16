# Station status — CONTROL GDA position feedback

Date: 2026-09-16
Station: CONTROL

## Newly established

Primary LM documentation supports treating the Pitch and Roll GDA position channels as physical actuator-position feedback, not as aliases for LGC trim commands. `LED-267-37C` identifies the LM-7/8/9 channels as `GH1313V` Pitch GDA Position and `GH1314V` Roll GDA Position, with separate LGC extend/retract command discretes. The LM Operations Handbook DECA trim-control diagram independently shows actuator-position feedback returning from the GDA into the control electronics.

Research note 187 adds a further representation constraint from the primary LM-10-and-subsequent Instrumentation Packet: the same `GH1313V` / `GH1314V` measurement family is presented there as Pitch/Roll GDA position over `-6..+6 DEG`. This demonstrates a documented angular engineering-unit presentation for the later LM configuration. It does not establish that LM-7 used identical conversion coefficients or signed polarity.

## CONTROL modeling consequence

A CONTROL-facing implementation should keep at least these concepts separate:

- commanded/preburn GDA trim reference;
- LGC extend/retract trim commands;
- measured physical Pitch/Roll GDA actuator position;
- telemetry engineering-unit presentation;
- powered-flight attitude response/outcome.

The telemetry family may be annotated as angular in later-LM instrumentation (`-6..+6 DEG`), but do not transfer that calibration to Apollo 13, convert the Mission Report's signed actuator inches to degrees/EXT/RET, or equate those measurements with the crew-facing `5.86 / 6.75` pair until LM-7 calibration/reference evidence is recovered.

## Remaining status

The station's PC+2 trim provenance remains incomplete. Highest priority is still the T+55 mass-properties deck -> RTCC/RTACF trim computation lineage, including CONTROL's competing numerical solution and the comparison/acceptance basis. The representation subproblem is now specifically LM-7 engineering conversion/polarity plus the crew-facing trim-number reference, rather than an unconstrained raw-voltage question.