# Research note 179 — preburn GDA checkout acceptance bound

Date: 2026-09-16

## Question

Does the surviving 61-hour Flight Director loop recover an operational tolerance or acceptance statement for the GDA trim before the 61:29 free-return DPS burn, and can that value be used as the missing PC+2 computational comparison criterion?

## Mission-control voice evidence

The recovered Flight Director loop around 61:03–61:11 GET shows CONTROL actively directing the LM gimbal-trim checkout. CONTROL tells FLIGHT that the crew needs to trim the **gimbal, not the throttle**, and recommends using the DAP-set gimbal/throttle-test procedure. After the checkout, CONTROL reports:

- `61:11:39` — **"Trim looks okay."**
- FLIGHT asks how close the observed values were.
- `61:12:07` — CONTROL answers **"We're within about 0.3. We're - plenty close."**
- CONTROL then reports the configuration ready.

The loop therefore supplies a mission-specific operational acceptance statement associated with the actual preburn GDA checkout.

## Finding

`~0.3°` is now source-backed as an **observed preburn gimbal-trim checkout closeness** that CONTROL judged "plenty close" for proceeding with the 61:29 maneuver.

This improves the earlier classification of the `within about 0.3` exchange: it is not merely generic hardware-checkout evidence. The surrounding loop explicitly ties it to CONTROL's gimbal-trim procedure and readiness decision immediately before the free-return DPS burn.

## Critical boundary

This does **not** recover the missing PC+2 computational acceptance criterion.

The `~0.3` statement concerns the observed/checked gimbal trim immediately before executing the 61:29 maneuver. It does not describe:

- the earlier Flight Dynamics-versus-LM-CONTROL comparison at ~59 GET;
- a mass-properties trim-calculation delta;
- the T+55 RTCC deck;
- a rule for deciding whether two independently computed pitch/yaw trim solutions agree;
- the later PC+2 `5.85 / 6.74` retained-reference decision.

Accordingly, do not substitute `0.3°` for the still-unrecovered PC+2 calculation/comparison criterion, just as the earlier T+25 `0.01°` no-update result must remain scoped to T+25.

## Station implication

CONTROL's operational role is now more concrete: the station not only challenged the earlier ground-computed trim on mass-properties grounds, but also directed the spacecraft gimbal-trim checkout and judged the resulting preburn trim sufficiently close to proceed.

For simulator design, distinguish at least:

1. **ground computation/comparison acceptance** — unresolved for the ~59 GET disagreement;
2. **spacecraft preburn gimbal checkout acceptance** — `within about 0.3`, judged "plenty close" here;
3. **powered-flight compliance/resulting actuator state** — exact two-axis post-61:29 state unrecovered.

## Source

Apollo 13 Flight Director loop, approximately 61:03–61:12 GET, recovered mission-control audio/transcription. The transcript records CONTROL's gimbal-trim instructions and the `within about 0.3` / `plenty close` readiness exchange.

The Apollo 13 Real-time presentation credits NASA for the mission audio/transcription source and NASA Johnson for making the audio available. This note uses the loop as mission-control voice evidence; it does not elevate editorial annotations on the presentation site to primary evidence.

## Next archival target

Continue searching for the separate real-time T+55 generation/load or downstream RTCC/RTACF LM-burn run/request/output artifact that can connect the mass-properties deck to the ~59 GET `5.86 / 6.75` calculation. CONTROL's alternative numerical trim and the computational comparison rule remain unresolved.