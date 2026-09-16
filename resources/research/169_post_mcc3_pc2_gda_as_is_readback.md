# Research note 169 — post-MCC-3 PC+2 GDA “as is” reference

Date: 2026-09-15

> **2026-09-16 correction:** Research note 188 recovered a clearer NASA transcript rendering. The `5.85 / 6.74` pair is a CAPCOM-issued PC+2 GDA reference on a new P30 pad, not a crew-originated `hopefully` readback. The axis wording is pitch/roll. The historical finding below is retained with that correction incorporated.

## Question

Does a primary operational record recover any two-axis numerical reference for the GDA state intended to be retained for PC+2 after the 61:29 free-return DPS maneuver?

## Primary-source finding

Yes, as a ground-issued desired/reference pair rather than measured post-compliance telemetry.

In the NASA Apollo 13 mission commentary / air-to-ground transcript after the 61:29 free-return burn, CAPCOM introduces a new PC+2 P30 maneuver pad and states:

> `Your GDA ought to be okay as it is from the last burn but pitch ought to be at 5.85, in roll it's 6.74.`

Primary transcript:
- NASA, *Apollo 13 Mission Commentary / Air-to-Ground Transcript*, 14 April 1970, transcript page headed GET 63:00:00.

## What this adds

This is a recovered post-61:29 operational record pairing the **“okay as it is from the last burn” PC+2 disposition with two ground-passed numerical GDA values**.

- pitch reference: `5.85°`;
- roll reference: `6.74°`;
- disposition: no new GDA setting expected at that point — `okay as it is from the last burn`.

The pair is only `0.01°` below the earlier `5.86° / 6.75°` interim pair passed near 59 GET. That numerical proximity is an observation only. It is **not** evidence that a `0.01°` PC+2 acceptance criterion was used, nor that the T+25 `0.01°` comparison context applied to PC+2.

## Relationship to CONTROL’s ignition-motion report

Research note 168 derived an approximately `-0.8°` immediately pre-PC+2 roll-GDA position from CONTROL’s postflight statement that the roll GDA moved to about `-2°` at ignition by `-1.2°`.

The `5.85 / 6.74` evidence does **not** justify replacing that execution-state derivation. CAPCOM states what the GDA `ought to be` on the PC+2 pad and says it should already be okay from the previous burn; the transcript does not identify these numbers as measured actuator positions immediately before PC+2 ignition. The two records therefore remain different evidence classes:

- `5.85 / 6.74`: ground-issued PC+2 desired/reference pair;
- `~-0.8°` roll: approximate execution-state position derived from CONTROL’s later ignition-motion account.

Until a controller telemetry printout, working sheet, or RTCC product bridges them, do not force the two into a single numerical state.

## What remains unresolved

This finding does not recover:

- the RTCC/RTACF PC+2 candidate trim calculation;
- the candidate/reference comparison delta;
- the decision tolerance or criterion;
- calculation time or job/run identity;
- direct calculation-level linkage to the T+55 LM-burn mass-property deck;
- a measured two-axis GDA state immediately before PC+2 ignition.

## Simulator implication

The model may distinguish a source-backed **post-free-return PC+2 ground-issued GDA reference** (`5.85 / 6.74`, pitch/roll) from observed/derived execution state. Do not use this pair as authoritative instantaneous actuator position, and do not infer a PC+2 comparison tolerance from its `0.01°` difference from the earlier interim pair.

## Next unresolved item

Prioritize controller/RTCC working artifacts that can connect the post-free-return “okay as it is” reference to the actual PC+2 mass-properties calculation: candidate trim, comparison delta/criterion, job identity, and T+55 deck provenance.