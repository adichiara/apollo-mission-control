# Station research status — CONTROL / 61:29 GDA

Date: 2026-09-16

## Newly documented

Primary postflight evidence provides mission-specific GDA actuator positions for the 61:29 free-return DPS burn. *Apollo 13 Mission Report* Table 6.4-I reports, in inches:

| Phase | Pitch | Roll |
|---|---:|---:|
| Initial | -0.02 | -0.34 |
| Maximum excursion | +0.31 | -0.27 |
| Steady-state | +0.04 | -0.51 |
| Cutoff | +0.10 | -0.31 |

NASA LM reference material also establishes the generic GDA mechanism range: each actuator extends/retracts 2 inches from mid-position for a maximum 6° engine tilt on its axis; published specifications give ±2 in stroke and ±6° gimbal position, each with ±5% tolerance. The nominal endpoint ratio is therefore 3°/in.

LM-7/8/9 Elementary Functional Diagrams (`LED-267-37C`) now provide mission-block measurement semantics. The measurement index identifies `GH1313V` as `VOLT, PITCH GDA POS (RET/EXT)` and `GH1314V` as `VOLT, ROLL GDA POS (EXT/RET)`, with separate pitch and roll LGC extend/retract trim-command discretes (`GH1318X`, `GH1319X`, `GH1343X`, `GH1344X`). The associated discrete GDA indications likewise preserve opposite axis-specific RET/EXT ordering.

This strengthens CONTROL's documented `GDA position/trim` information family with actual maneuver-specific postflight values, a sourced generic mechanical scale, and LM-7-specific channel/axis semantics.

## Fidelity boundary

The Mission Report reports actuator displacement in inches, while the crew-facing preburn trim was communicated in degrees. The generic 3°/in endpoint ratio is not an LM-7-specific calibration and does not define the zero/reference or sign convention of the crew-facing `5.86 / 6.75` numbers. `LED-267-37C` confirms the Pitch/Roll channel names and opposite extension/retraction notation, but the recovered measurement index alone does not establish which Mission Report numerical sign means EXT or RET, nor the voltage-to-inch calibration. Do not infer either mapping. The four postflight values are summary points, not a continuous trace.

## Still unresolved

- exact Apollo 13 CONTROL CRT field calibration/precision for GDA position;
- exact live values seen by CONTROL during the burn versus the later postflight reconstruction;
- `GH1313V` / `GH1314V` telemetry voltage/sign-to-inch and EXT/RET calibration;
- crew-facing GDA trim-number zero/reference and mapping to actuator position;
- T+55 mass-properties computational lineage to the `5.86 / 6.75` preburn trim;
- CONTROL's competing numerical trim and comparison criterion.
