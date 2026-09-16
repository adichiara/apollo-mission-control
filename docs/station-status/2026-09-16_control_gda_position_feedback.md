# Station status — CONTROL GDA position feedback

Date: 2026-09-16
Station: CONTROL

## Newly established

Primary LM documentation now supports treating the Pitch and Roll GDA position channels as physical actuator-position feedback, not as aliases for LGC trim commands. `LED-267-37C` identifies the LM-7/8/9 channels as `GH1313V` Pitch GDA Position and `GH1314V` Roll GDA Position, with separate LGC extend/retract command discretes. The LM Operations Handbook DECA trim-control diagram independently shows actuator-position feedback returning from the GDA into the control electronics and places the GDA-position measurements on that feedback side.

## CONTROL modeling consequence

A CONTROL-facing implementation should keep at least these concepts separate:

- commanded/preburn GDA trim reference;
- LGC extend/retract trim commands;
- measured physical Pitch/Roll GDA actuator position;
- powered-flight attitude response/outcome.

Do not convert the Apollo 13 Mission Report's signed actuator inches to EXT/RET direction or to the crew-facing `5.86 / 6.75` pair until LM-7 calibration/reference evidence is recovered.

## Remaining status

The station's PC+2 trim provenance remains incomplete. Highest priority is still the T+55 mass-properties deck -> RTCC/RTACF trim computation lineage, including CONTROL's competing numerical solution and the comparison/acceptance basis.