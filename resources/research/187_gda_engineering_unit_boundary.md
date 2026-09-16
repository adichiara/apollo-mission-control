# Research Note 187 — GDA engineering-unit boundary

Date: 2026-09-16

## Question

Does primary LM instrumentation documentation define the engineering-unit representation of the `GH1313V` / `GH1314V` GDA position telemetry family closely enough to improve the model without inventing an Apollo 13/LM-7 calibration?

## Primary source

**LM-10 and Subsequent Instrumentation Packet** (NASA/Grumman LM instrumentation documentation).

Public scan: https://www.ibiblio.org/apollo/Documents/LM-10_Instrumentation_Packet.pdf

This is a later LM configuration than Apollo 13's LM-7. It is therefore used only to establish documented continuity of the measurement family's engineering-unit representation, not as proof of LM-7 calibration constants.

## Finding

The instrumentation packet lists:

- `GH1313V` — **PITCH GDA POS** — engineering range `-6 6 DEG`;
- `GH1314V` — **ROLL GDA POS** — engineering range `-6 6 DEG`.

The same channel identifiers and Pitch/Roll functions already appear in the mission-block `LED-267-37C` LM-7/8/9 measurement index, where they are labeled voltage measurements with `(RET/EXT)` and `(EXT/RET)` direction metadata.

This materially narrows the representation question: at least in the documented LM-10-and-subsequent instrumentation system, the GDA position telemetry family was converted for engineering use into **degrees**, with a `-6°` to `+6°` range. The channel suffix `V` and the LM-7 index's `VOLT` label therefore do not mean that controller-facing engineering use must remain in raw volts.

## Boundary

Do **not** transfer the LM-10 numerical calibration to Apollo 13 as an exact LM-7 calibration without mission-block evidence. In particular, this source does not establish:

- that LM-7 used exactly the same telemetry conversion coefficients;
- which signed degree corresponds to EXT versus RET on each LM-7 axis;
- how the Apollo 13 Mission Report's actuator inches were derived from or related to these telemetry channels;
- the zero/reference convention of the crew-facing `5.86 / 6.75` trim numbers;
- that `5.86 / 6.75` are direct GH1313V/GH1314V telemetry readings.

The Mission Report's inch values and the crew-facing trim pair must remain separate representations until a mission-specific mapping is recovered.

## Simulation implication

The model may now represent `GH1313V` / `GH1314V` as a telemetry family whose later-LM engineering presentation is angular (`deg`) while keeping Apollo 13 conversion metadata explicitly unresolved. Do not force the four Apollo 13 postflight actuator positions through the LM-10 `-6..+6 DEG` calibration.

## Next target

The principal unresolved target remains the T+55 LM-burn deck -> RTCC/RTACF run -> `5.86 / 6.75` lineage. The parallel representation target is narrowed to a mission-block LM-7 instrumentation/calibration source establishing the GH1313V/GH1314V engineering conversion and polarity, plus a primary definition of the crew-facing trim-number reference.