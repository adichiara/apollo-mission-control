# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown using MSFN, onboard, and relative-tracking evidence. NASA TN D-6846 supplies a primary validation envelope of planned/postflight trajectory, guidance-command, radar-update, attitude, altitude-rate, and landing-phase products. Neither is promoted to a Mission-G live display or raw continuous truth stream.

The actual 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II; broad online discovery exhausted**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; PDI mass provenance further bounded.** Apollo 11 Mission Report §9.8 and fig. 9.8-1 document powered-descent duration/velocity change, throttle timing, the early telemetry dropout, and flight throttle/chamber/interface/regulator pressure histories.

The Apollo 11 Flight Plan supplies a 33,278.3-lb unmanned LM bookkeeping state and 436.7-lb CSM→LM lunar-orbit transfer, but neither is PDI mass. The primary source family remains **SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968, Volume III Mass Properties**.

The public digitization has now been provenance-audited: despite the 20 August 1969 Rev. 2 title date, surviving indexed pages include **Amendment 86 (9/10/70)** and **Amendment 110 (7/19/71)**; the latter's table 3.1-8 is for **LM-10**. The scan is therefore an amended working binder, not a pristine Mission-G snapshot. Section number alone is not evidence that a surviving row applies to LM-5.

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation* (September 1970), remains **BLOCKED ON NAMED SOURCE RECOVERY**.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this mass-properties provenance pass.

## Implementation boundary

The historical model may be validated against Apollo 11 flight throttle/pressure behavior, event timing, command relationships, and reconstructed trajectory/checkpoint products. PDI mass remains a model input until a Mission-G/LM-5 sequential mass-properties or consumables page is recovered with explicit mission identity and amendment/effective-date provenance. Do not derive it by adding transfer weights to an unmanned/launch state, borrowing another LM, or assuming an amendment-overwritten table retains its original Mission-G meaning.

## Evidence status

- underlying DPS parameter semantics: **DOCUMENTED**;
- LM-5 launch/unmanned configuration bookkeeping: **DOCUMENTED**;
- CSM→LM lunar-orbit transfer bookkeeping: **DOCUMENTED**;
- primary mission-specific PDI mass source family/table class: **DOCUMENTED / TARGET IDENTIFIED**;
- public Rev. 2 binder amendment-overwrite behavior: **DOCUMENTED**;
- exact LM-5 `LM PRE P.D.I.` sequential mass row: **UNRESOLVED — PROVENANCED PAGE REQUIRED**;
- Apollo 11 as-flown throttle/pressure telemetry relationships: **DOCUMENTED**;
- Apollo 11 DOI→touchdown reconstruction methodology: **DOCUMENTED AS RECONSTRUCTED**;
- source-backed descent validation/checkpoint envelope: **DOCUMENTED**;
- 45-day BET NAT state listing / exact state-series metadata: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 Mission Report Supplement 7, DPS Final Flight Evaluation: **BLOCKED ON NAMED SOURCE RECOVERY**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.