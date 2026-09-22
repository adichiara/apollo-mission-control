# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown using MSFN, onboard, and relative-tracking evidence. NASA TN D-6846 supplies a primary validation envelope of planned/postflight trajectory, guidance-command, radar-update, attitude, altitude-rate, and landing-phase products. Neither is promoted to a Mission-G live display or raw continuous truth stream.

The actual 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II; broad online discovery exhausted**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; PDI mass provenance narrowed.** Apollo 11 Mission Report §9.8 and fig. 9.8-1 document powered-descent duration/velocity change, throttle timing, the early telemetry dropout, and flight throttle/chamber/interface/regulator pressure histories.

The Apollo 11 Flight Plan supplies a 33,278.3-lb unmanned LM bookkeeping state and 436.7-lb CSM→LM lunar-orbit transfer, but neither is PDI mass. The primary source family that should contain the event-specific answer is now identified: **SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968, Volume III Mass Properties**. Its mission-specific sequential mass-properties/consumables structure is independently verified in repository Apollo 13 research, where later LM-7 pages contain an explicit `LM PRE P.D.I.` row. No LM-7 value is transferred to LM-5.

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation* (September 1970), remains **BLOCKED ON NAMED SOURCE RECOVERY**.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this mass-properties provenance pass.

## Implementation boundary

The historical model may be validated against Apollo 11 flight throttle/pressure behavior, event timing, command relationships, and reconstructed trajectory/checkpoint products. PDI mass remains a model input until the Mission-G/LM-5 sequential mass-properties row is actually recovered and its amendment provenance checked. Do not derive it by adding transfer weights to an unmanned/launch state or by borrowing Apollo 13 values.

## Evidence status

- underlying DPS parameter semantics: **DOCUMENTED**;
- LM-5 launch/unmanned configuration bookkeeping: **DOCUMENTED**;
- CSM→LM lunar-orbit transfer bookkeeping: **DOCUMENTED**;
- primary mission-specific PDI mass source family/table class: **DOCUMENTED / TARGET IDENTIFIED**;
- exact LM-5 `LM PRE P.D.I.` sequential mass row: **UNRESOLVED — EXTRACTION TARGET**;
- Apollo 11 as-flown throttle/pressure telemetry relationships: **DOCUMENTED**;
- Apollo 11 DOI→touchdown reconstruction methodology: **DOCUMENTED AS RECONSTRUCTED**;
- source-backed descent validation/checkpoint envelope: **DOCUMENTED**;
- 45-day BET NAT state listing / exact state-series metadata: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 Mission Report Supplement 7, DPS Final Flight Evaluation: **BLOCKED ON NAMED SOURCE RECOVERY**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.