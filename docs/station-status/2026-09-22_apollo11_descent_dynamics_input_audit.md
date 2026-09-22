# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The actual 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; event provenance gate tightened.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents **33,683.5 lb at LM separation; 33,669.6 lb at DOI ignition; 33,401.6 lb at DOI cutoff; 16,153.2 lb at lunar landing**. It does not provide PDI mass.

NASA SP-4029 is rejected for PDI closure because its Apollo 11 event assignments conflict with the primary Mission Report. A second conflict is now recorded: NASA technical paper **20080013635** uses **33,683.5 lb as a simulated PDI weight**, exactly matching the Mission Report's separation mass. Because that paper describes an approximate simulation and does not supply contemporaneous Mission-G mass-ledger provenance, its value is classified **MODELLED / NOT HISTORICAL PDI EVIDENCE**.

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation* (September 1970), remains **BLOCKED ON NAMED SOURCE RECOVERY**.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this source-conflict audit.

## Implementation boundary

Use primary Mission Report masses only at their named events. PDI mass remains a model input until an explicitly labeled Mission-G/LM-5 PDI/pre-PDI source is recovered. Do not adopt a later NASA simulation value merely because it uses an authentic Apollo 11 mass number.

## Evidence status

- LM-5 postflight mass at separation / DOI ignition / DOI cutoff / landing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- SP-4029 event-label conflict: **DOCUMENTED — REJECTED FOR CLOSURE**;
- NASA 20080013635 simulated PDI assignment of 33,683.5 lb: **DOCUMENTED AS MODEL INPUT — REJECTED AS HISTORICAL PDI EVIDENCE**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED — EXPLICITLY LABELED PROVENANCED SOURCE REQUIRED**;
- Apollo 11 as-flown throttle/pressure relationships: **DOCUMENTED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7: **BLOCKED ON NAMED SOURCE RECOVERY**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.