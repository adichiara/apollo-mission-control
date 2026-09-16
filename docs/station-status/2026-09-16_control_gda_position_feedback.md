# Station status — CONTROL GDA position feedback

Date: 2026-09-16
Station: CONTROL

## Newly established

Primary LM documentation supports treating the Pitch and Roll GDA position channels as physical actuator-position feedback, not as aliases for LGC trim commands. `LED-267-37C` identifies the LM-7/8/9 channels as `GH1313V` Pitch GDA Position and `GH1314V` Roll GDA Position, with separate LGC extend/retract command discretes. The LM Operations Handbook DECA trim-control diagram independently shows actuator-position feedback returning from the GDA into the control electronics.

Research note 187 adds a further representation constraint from the primary LM-10-and-subsequent Instrumentation Packet: the same `GH1313V` / `GH1314V` measurement family is presented there as Pitch/Roll GDA position over `-6..+6 DEG`. This demonstrates a documented angular engineering-unit presentation for the later LM configuration. It does not establish that LM-7 used identical conversion coefficients or signed polarity.

Research note 188 clarifies the post-free-return PC+2 operational instruction from the NASA transcript. CAPCOM, while issuing a new PC+2 P30 pad, says the GDA `ought to be okay as it is from the last burn` and specifies pitch `5.85`, roll `6.74`. This is a ground-issued desired/reference pair with a no-action disposition, not a crew estimate and not measured GDA telemetry.

## CONTROL modeling consequence

A CONTROL-facing implementation should keep at least these concepts separate:

- computed/ground-issued GDA trim reference;
- disposition (`load/change` versus `okay as it is`);
- LGC extend/retract trim commands;
- measured physical Pitch/Roll GDA actuator position;
- telemetry engineering-unit presentation;
- powered-flight attitude response/outcome.

The telemetry family may be annotated as angular in later-LM instrumentation (`-6..+6 DEG`), but do not transfer that calibration to Apollo 13, convert the Mission Report's signed actuator inches to degrees/EXT/RET, or equate those measurements with the crew-facing `5.86 / 6.75` or `5.85 / 6.74` references until LM-7 calibration/reference evidence is recovered. The `5.85 / 6.74` pair should carry the explicit historical disposition `okay as it is from the last burn` without being treated as proof of a new computation.

## Remaining status

The station's PC+2 trim provenance remains incomplete. Highest priority is still the T+55 mass-properties deck -> RTCC/RTACF trim computation lineage, including CONTROL's competing numerical solution and the comparison/acceptance basis. The representation subproblem is now specifically LM-7 engineering conversion/polarity plus the crew-facing trim-number reference, rather than an unconstrained raw-voltage question.