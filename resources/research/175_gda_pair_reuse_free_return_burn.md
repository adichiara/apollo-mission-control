# Research note 175 — 5.86 / 6.75 GDA pair reused for the 61:29 free-return burn

Date: 2026-09-16

## Question

Did the `5.86° / 6.75°` pair passed with the ~59 GET PC+2 abort pad remain merely a provisional PC+2 planning value, or can primary mission voice trace the same pair into the intervening 61:29 free-return DPS maneuver that CONTROL later identified as the state-setting event for PC+2?

## Primary sources

1. NASA Apollo 13 Technical Air-to-Ground Voice Transmission transcript, tape 41/9–41/10, around 60:52–60:56 GET (`as13-tec.pdf`).
2. NASA Apollo 13 mission voice at ~59:03 GET, where CAPCOM passes the PC+2 DPS trim pair and explicitly says the gimbal trim angles "will be updated" but that the crew should use `5.86 / 6.75` for the moment.
3. NASA/MSC Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, LM CONTROL narrative, which later says the GDA settings resulting from the 61:29 maneuver's 40% powered-flight compliance were expected to provide optimum alignment for PC+2.

## Finding

At 60:53:09 GET, CAPCOM reads the crew the P30 pad for the 61:29:42.84 free-return midcourse correction. The same read-up explicitly gives the LM GDA angles as:

- pitch `5.86°`
- roll `6.75°`

Haise reads those same values back at 60:54:57 and CAPCOM accepts the pad readback.

This is the same numerical pair that had been passed roughly two hours earlier with the provisional PC+2 abort pad. The earlier read-up explicitly warned that those gimbal trim angles "will be updated" while instructing the crew to use them for the moment.

The primary record therefore supports a stronger continuity chain than previously documented:

`~59 GET provisional PC+2 DPS trim 5.86 / 6.75 -> same commanded GDA pair on the 61:29 free-return DPS pad -> powered-flight compliance during the 61:29 maneuver -> resulting GDA state expected by CONTROL to be optimum for PC+2 -> later PC+2 GDA disposition "okay as is"`.

## What this closes

The `5.86 / 6.75` pair is no longer best described only as a PC+2 planning solution. It is also directly documented as the **commanded GDA pair for the intervening 61:29 free-return DPS burn**. This supplies the missing numerical bridge into the maneuver that CONTROL later identified as setting the GDA state relevant to PC+2.

## Evidence boundary

Do not infer:

- that the actual post-compliance actuator state remained exactly `5.86 / 6.75`;
- that the later `5.85 / 6.74` readback is measured GDA telemetry;
- that the `0.01°` difference between those pairs is a PC+2 tolerance;
- that the same RTCC/RTACF job generated both the ~59 PC+2 pad and the 61:29 free-return pad;
- that the T+55 deck directly generated `5.86 / 6.75`;
- CONTROL's competing premission-mass-properties numerical trim.

The 61:29 burn's 40% compliance is explicitly important precisely because powered flight could move the gimbals away from the commanded starting pair. The commanded pair and resulting complied state must remain separate data fields.

## Simulator implication

Represent at least three distinct GDA concepts:

1. ground-computed/commanded initial trim pair;
2. commanded pair actually loaded/carried into a burn;
3. post-powered-flight complied actuator/reference state.

For this Apollo 13 sequence, `5.86 / 6.75` is source-backed for items 1 and 2; the exact numerical two-axis value for item 3 remains unrecovered.

## Next archival target

The highest-value unresolved artifact remains upstream: recover the real-time weight/c.g./mass-properties output and RTCC/RTACF request/output that produced or validated the `5.86 / 6.75` solution, including CONTROL's competing values and explicit T+55 provenance. Downstream, seek telemetry or a controller working sheet that numerically records the post-61:29 complied two-axis GDA state.