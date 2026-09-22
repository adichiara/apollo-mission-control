# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The actual 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; propulsion provenance improved.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents **33,683.5 lb at LM separation; 33,669.6 lb at DOI ignition; 33,401.6 lb at DOI cutoff; 16,153.2 lb at lunar landing**. It does not provide PDI mass.

The contemporary NASA **Apollo 11 Press Kit** specifies the DPS at **9,870 lbf maximum rated thrust**, throttleable between **1,050 and 6,300 lbf**, with ±6° gimbal capability. NASA TN D-7143 later records a **10,500-lbf maximum-rated design requirement**. These are retained as differently scoped primary specifications; they are not merged into an as-flown range and neither is treated as delivered LM-5 thrust.

NASA SP-4029 and NASA 20080013635 remain rejected for PDI closure because their event/value assignments do not establish the missing Mission-G PDI state.

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation*, is independently documented by later NASA mission-report supplement tables as published in **September 1970**, but its contents remain **BLOCKED ON NAMED SOURCE RECOVERY**. No identifier or performance value is inferred from neighboring mission supplements.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this propulsion-source audit.

## Implementation boundary

Use primary Mission Report masses only at their named events. PDI mass remains a model input until an explicitly labeled Mission-G/LM-5 PDI/pre-PDI source is recovered. Use the Apollo 11 Press Kit thrust values as preflight specification evidence only; do not convert Mission Report throttle percentage to exact thrust without a mission-specific documented relationship.

## Evidence status

- LM-5 postflight mass at separation / DOI ignition / DOI cutoff / landing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf maximum rated / 1,050–6,300-lbf throttleable preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- D-7143 10,500-lbf maximum-rated value: **DOCUMENTED — PROGRAM/DESIGN REQUIREMENT, NOT LM-5 DELIVERED THRUST**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED**;
- Apollo 11 as-flown throttle/pressure relationships: **DOCUMENTED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7: **BLOCKED ON NAMED SOURCE RECOVERY; PUBLICATION CONFIRMED SEPTEMBER 1970**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.