# Research note 169 — post-MCC-3 PC+2 GDA “as is” readback

Date: 2026-09-15

## Question

Does a primary operational record recover any two-axis numerical reference for the GDA state intended to be retained for PC+2 after the 61:29 free-return DPS maneuver?

## Primary-source finding

Yes, but as a crew readback/reference rather than as measured post-compliance telemetry.

In the NASA Apollo 13 mission commentary / air-to-ground transcript after the 61:29 free-return burn, the crew reads back a revised PC+2 maneuver pad and states that the **GDA should be okay as is**, adding that this is “hopefully” pitch `5.85` and the second GDA axis `6.74`. The transcript labels that second axis “Yaw”; for the LM DPS GDA context, the operational pad elsewhere uses pitch/roll terminology. Preserve the transcript wording rather than silently rewriting the primary record.

Primary transcript:
- NASA, *Apollo 13 Mission Commentary / Air-to-Ground Transcript*, 14 April 1970, transcript page headed approximately GET 63:10:00.
- Searchable NASA result text preserves: `GDA should be okay as is, which hopefully is Pitch, 5.85 Yaw 6.74.`

## What this adds

This is the first recovered post-61:29 operational record that pairs the **“as is” PC+2 disposition with two numerical GDA values**.

It materially narrows the retained-reference question:

- pitch reference/readback: `5.85°`;
- second GDA-axis reference/readback: `6.74°` as transcribed;
- disposition: no new setting expected at that point — “GDA should be okay as is.”

The pair is only `0.01°` below the earlier `5.86° / 6.75°` interim pair passed near 59 GET. That numerical proximity is documented here as an observation only. It is **not** evidence that a `0.01°` PC+2 acceptance criterion was used, nor that the T+25 `0.01°` comparison rule applied to PC+2.

## Relationship to CONTROL’s ignition-motion report

Research note 168 derived an approximately `-0.8°` immediately pre-PC+2 roll-GDA position from CONTROL’s postflight statement that the roll GDA moved to about `-2°` at ignition by `-1.2°`.

The new `5.85 / 6.74` evidence does **not** justify replacing that execution-state derivation. The transcript wording is a crew pad readback — explicitly qualified by “hopefully” — and does not say these were measured GDA positions immediately before PC+2 ignition. The two records therefore belong to different evidence classes:

- `5.85 / 6.74`: operational intended/retained reference as read back after MCC-3;
- `~-0.8°` roll: approximate execution-state position derived from CONTROL’s later ignition-motion account.

Until a controller telemetry printout, working sheet, or RTCC product bridges them, do not force the two into a single numerical state.

## What remains unresolved

This finding does not recover:

- the RTCC/RTACF PC+2 candidate trim calculation;
- the candidate/reference comparison delta;
- the decision tolerance or criterion;
- calculation time or job/run identity;
- direct calculation-level linkage to the T+55 LM-burn mass-property deck;
- a measured two-axis GDA state at 61:29 cutoff or immediately before PC+2 ignition.

## Simulator implication

The model may now distinguish a source-backed **post-MCC-3 PC+2 retained-reference readback** (`5.85 / 6.74`, with transcript axis-label caveat) from the later observed/derived execution state. Do not use this pair as authoritative instantaneous actuator position, and do not infer a PC+2 comparison tolerance from its `0.01°` difference from the earlier interim pair.

## Next unresolved item

Prioritize controller/RTCC working artifacts that can connect the post-MCC-3 “as is” reference to the actual PC+2 mass-properties calculation: candidate trim, comparison delta/criterion, job identity, and T+55 deck provenance.