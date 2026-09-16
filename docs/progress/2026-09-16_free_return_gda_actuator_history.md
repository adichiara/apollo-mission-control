# Progress — 61:29 free-return GDA actuator history

Date: 2026-09-16

## Completed

Recovered mission-specific GDA actuator values for the Apollo 13 61:29 free-return DPS maneuver from the primary *Apollo 13 Mission Report*, Table 6.4-I.

The table reports GDA position in inches:

- initial: pitch `-0.02`, roll `-0.34`;
- maximum excursion: pitch `+0.31`, roll `-0.27`;
- steady-state: pitch `+0.04`, roll `-0.51`;
- cutoff: pitch `+0.10`, roll `-0.31`.

Research Note 184 additionally recovers the generic NASA LM GDA mechanical range: ±2 inches actuator stroke corresponds to ±6° engine tilt, giving a nominal endpoint ratio of 3°/in. This is a mechanism-scale bound, not an Apollo 13/LM-7 calibration or a definition of the crew-facing `5.86 / 6.75` trim representation.

Research Note 185 recovers LM-7/8/9 engineering measurement semantics from `LED-267-37C`. The hardware documentation explicitly identifies analog `PITCH GDA POS (RET/EXT)` (`GH1313V`) and `ROLL GDA POS (EXT/RET)` (`GH1314V`) channels, plus separate LGC extend/retract trim-command discretes. This validates `Pitch` and `Roll` as the hardware axis labels and establishes that the two channels carry opposite extension/retraction notation. It does not by itself define the numerical sign or voltage-to-inch calibration.

This closes the exact-value actuator-history target at the resolution of the postflight summary and the generic mechanism-scale question, and narrows the mission-block telemetry semantics. It does not provide a continuous telemetry trace, the GH1313V/GH1314V engineering-unit calibration, or a sourced mapping from actuator inches to the preburn angular trim-number representation.

## Documentation impact

- added Research Notes 183–185;
- updated the PC+2 GDA roadmap;
- updated GDA trim source catalog;
- updated station-research status for CONTROL/GDA monitoring.

## Next unresolved item

Continue the main provenance target: recover a T+55 generation/load or downstream RTCC/RTACF run/request/output artifact tying the LM-burn mass-properties deck to `5.86 / 6.75`, ideally including weight/c.g., CONTROL's competing trim, and the comparison criterion. In parallel, seek the LM-7 instrumentation/calibration definition for `GH1313V` and `GH1314V` to map telemetry voltage/sign to actuator displacement and EXT/RET direction without assumption.
