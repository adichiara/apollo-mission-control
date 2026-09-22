# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown using MSFN, onboard, and relative-tracking evidence. NASA TN D-6846 supplies a primary validation envelope of planned/postflight trajectory, guidance-command, radar-update, attitude, altitude-rate, and landing-phase products. Neither is promoted to a Mission-G live display or raw continuous truth stream.

The actual 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II; broad online discovery exhausted**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; postflight event masses now primary-source bounded.** Apollo 11 Mission Report §9.8 and fig. 9.8-1 document powered-descent duration/velocity change, throttle timing, the early telemetry dropout, and flight throttle/chamber/interface/regulator pressure histories.

The Mission Report Appendix A.6/table A-I additionally provides postflight LM mass properties derived from expendable usage/loading analysis and measured vehicle/stage weights: **33,683.5 lb at LM separation; 33,669.6 lb at DOI ignition; 33,401.6 lb at DOI cutoff; 16,153.2 lb at lunar landing**. It does not provide a PDI row.

The Apollo 11 Flight Plan's 33,278.3-lb unmanned LM bookkeeping state and 436.7-lb CSM→LM lunar-orbit transfer remain configuration anchors, not PDI mass. The public SNA-8-D-027(III) Rev. 2 mass-properties digitization remains amendment-overwritten and cannot safely supply Mission-G identity from section number alone.

NASA SP-4029, *Apollo by the Numbers*, was explicitly checked and is **not accepted for PDI closure**: its cross-mission table associates 33,669.6 lb with Apollo 11 PDI and 33,401.6 lb with DOI ignition, conflicting with the primary Mission Report's explicit DOI ignition/cutoff assignments. Preserve the primary event labels.

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation* (September 1970), remains **BLOCKED ON NAMED SOURCE RECOVERY**.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this mass-properties pass.

## Implementation boundary

The historical model may now use Mission Report table A-I masses as primary validation checkpoints at named events. PDI mass remains a model input until an explicitly labeled Mission-G/LM-5 PDI/pre-PDI source is recovered. Do not interpolate a historical truth value merely from DOI and landing masses, relabel DOI values from a secondary compilation, add transfer weights to an unmanned/launch state, or borrow another LM.

## Evidence status

- underlying DPS parameter semantics: **DOCUMENTED**;
- LM-5 launch/unmanned configuration bookkeeping: **DOCUMENTED**;
- CSM→LM lunar-orbit transfer bookkeeping: **DOCUMENTED**;
- LM-5 postflight mass at separation / DOI ignition / DOI cutoff / landing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- public Rev. 2 binder amendment-overwrite behavior: **DOCUMENTED**;
- SP-4029 Apollo 11 PDI/DOI event-label conflict: **DOCUMENTED — SECONDARY VALUE REJECTED FOR CLOSURE**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED — EXPLICITLY LABELED PROVENANCED SOURCE REQUIRED**;
- Apollo 11 as-flown throttle/pressure telemetry relationships: **DOCUMENTED**;
- Apollo 11 DOI→touchdown reconstruction methodology: **DOCUMENTED AS RECONSTRUCTED**;
- source-backed descent validation/checkpoint envelope: **DOCUMENTED**;
- 45-day BET NAT state listing / exact state-series metadata: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 Mission Report Supplement 7, DPS Final Flight Evaluation: **BLOCKED ON NAMED SOURCE RECOVERY**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.