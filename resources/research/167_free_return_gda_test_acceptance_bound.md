# Research note 167 — free-return GDA test acceptance bound

Date: 2026-09-15

## Question

Can the primary controller record recover any numerical acceptance criterion or state information around the 61:29 DPS maneuver that constrains the later PC+2 no-trim decision?

## Primary-source finding

Yes, but only for the **pre-61:29 gimbal trim/test check**, not for the later PC+2 candidate-vs-reference calculation.

In the Mission Control loop during the DPS gimbal/throttle test, CONTROL reports the gimbal driving to its stop and returning, then calls the trim GO and says it looks okay. CAPCOM asks what numbers were actually read out; FLIGHT asks, "How close were they?" CONTROL answers that they are **within about 0.3** and "plenty close."

Primary record/navigation source:
- Apollo 13 mission-control loop, GET ~61:08–61:12, preserved in the Apollo 13 real-time mission archive: https://apollo13realtime.org/
- Relevant sequence includes CONTROL at 61:10:57 (gimbal over against the stop and returning), 61:11:33/39 (GO / trim looks okay), and 61:12:07 ("within about 0.3 ... plenty close").

## Interpretation

This is direct numerical evidence that the controller team accepted the observed pre-burn gimbal trim/test result with an approximately `0.3°` discrepancy in the quantity being compared. It strengthens the state chain immediately before the 61:29 powered maneuver.

It does **not** establish that `0.3°` was the formal RTCC trim-update threshold, that the comparison was against a PC+2 candidate trim, or that the same criterion governed the later no-PC+2-trim decision. The loop context is the immediate gimbal/throttle checkout for the 61:29 burn.

The same controller record later shows FLIGHT asking after shutdown whether there is a requirement to trim; GUIDANCE answers `0.2`, which FLIGHT/GUIDANCE accept as good enough. Because that exchange occurs in the immediate post-burn guidance context and does not identify GDA angles, this project will **not** treat `0.2` as a GDA residual or PC+2 trim criterion without further primary evidence.

## Consequence

The provenance chain can now distinguish three numerical/decision layers:

1. earlier transmitted commanded GDA pair (`5.86° / 6.75°`);
2. pre-61:29 hardware/trim checkout accepted at roughly `0.3°` closeness;
3. post-61:29 powered-flight compliance state, still numerically unrecovered, later retained for PC+2.

This prevents incorrectly promoting the `0.3°` checkout observation into the missing PC+2 RTCC comparison tolerance.

## Next unresolved item

Continue searching for the **later controller-side PC+2 comparison**: numerical post-61:29 GDA reference state, PC+2 candidate trim, comparison delta/criterion, RTCC/RTACF job identity, and direct T+55 mass-property linkage. The `0.3°` checkout result is a useful discriminator: any archival artifact using it must be classified by whether it concerns hardware checkout versus mass-properties trim prediction.