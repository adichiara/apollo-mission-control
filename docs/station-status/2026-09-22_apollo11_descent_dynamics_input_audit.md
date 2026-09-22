# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown using MSFN, onboard, and relative-tracking evidence. NASA TN D-6846 supplies a primary validation envelope of planned/postflight trajectory, guidance-command, radar-update, attitude, altitude-rate, and landing-phase products. Neither is promoted to a Mission-G live display or raw continuous truth stream.

The actual 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II; broad online discovery exhausted**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; as-flown propulsion validation strengthened.** Apollo 11 Mission Report §9.8 and fig. 9.8-1 document powered-descent duration/velocity change, 13% start throttle, throttle-up timing, the early telemetry dropout, and flight throttle/chamber/interface/regulator pressure histories. These can constrain model validation without inventing an exact thrust or Isp history.

A primary NASA supplement table identifies Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation* (September 1970). A targeted public recovery pass did not locate the document. It is **BLOCKED ON NAMED SOURCE RECOVERY** and is the preferred mission-specific propulsion follow-up.

LM-5 launch propellant loading is documented; PDI mass remains unresolved. Do not convert throttle position to exact force without a sourced calibration/performance relationship and do not substitute neighboring-mission supplement values.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this propulsion evidence pass.

## Implementation boundary

The historical model may be validated against Apollo 11 flight throttle/pressure behavior, event timing, command relationships, and reconstructed trajectory/checkpoint products. Exact PDI mass, exact delivered thrust/Isp, and missing BET states remain model/recovery boundaries rather than hidden historical constants.

## Evidence status

- underlying DPS parameter semantics: **DOCUMENTED**;
- LM-5 launch resource bookkeeping: **DOCUMENTED**;
- Apollo 11 as-flown throttle/pressure telemetry relationships: **DOCUMENTED**;
- Apollo 11 DOI→touchdown reconstruction methodology: **DOCUMENTED AS RECONSTRUCTED**;
- source-backed descent validation/checkpoint envelope: **DOCUMENTED**;
- 45-day BET NAT state listing / exact state-series metadata: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 Mission Report Supplement 7, DPS Final Flight Evaluation: **BLOCKED ON NAMED SOURCE RECOVERY**;
- Apollo 11 PDI mass and exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.