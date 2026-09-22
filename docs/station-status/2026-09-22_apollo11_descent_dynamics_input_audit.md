# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The actual 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; FTP/design-rating distinction narrowed.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents **33,683.5 lb at LM separation; 33,669.6 lb at DOI ignition; 33,401.6 lb at DOI cutoff; 16,153.2 lb at lunar landing**. It does not provide PDI mass.

The contemporary NASA **Apollo 11 Press Kit** specifies **9,870 lbf** as the DPS mission-facing maximum-rated thrust. NASA TN D-7143 records a **10,500-lbf maximum-rated design requirement**. Primary Apollo Operations Handbook control documentation now supplies the conceptual bridge: automatic descent-engine throttle control tops out at the **fixed-throttle point (FTP), described as 92.5 percent thrust**, rather than continuously commanding the maximum-rated design point. The Apollo 11 Mission Report confirms throttle-up to FTP about 26 seconds after PDI.

This does not close an exact LM-5 throttle-to-force conversion. The recovered sources do not establish a configuration-controlled calibration making 9,870 lbf a direct 92.5-percent conversion of 10,500 lbf, and the arithmetic does not match exactly. Preserve the source-specific numbers and semantics rather than normalizing them.

NASA SP-4029 and NASA 20080013635 remain rejected for PDI closure because their event/value assignments do not establish the missing Mission-G PDI state.

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation*, is independently documented by later NASA mission-report supplement tables as published in **September 1970**, but its contents remain **BLOCKED ON NAMED SOURCE RECOVERY**. No identifier or performance value is inferred from neighboring mission supplements.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this propulsion-source audit.

## Implementation boundary

Use primary Mission Report masses only at their named events. PDI mass remains a model input until an explicitly labeled Mission-G/LM-5 PDI/pre-PDI source is recovered. Model **FTP/operational full throttle** separately from **maximum-rated design thrust**. Do not convert flight throttle percentage to exact force without LM-5-specific calibration/performance evidence.

## Evidence status

- LM-5 postflight mass at separation / DOI ignition / DOI cutoff / landing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf mission-facing preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- automatic throttle ceiling at 92.5-percent FTP: **DOCUMENTED — PRIMARY OPERATIONS HANDBOOK**;
- D-7143 10,500-lbf maximum-rated value: **DOCUMENTED — PROGRAM/DESIGN REQUIREMENT, NOT LM-5 DELIVERED THRUST**;
- exact LM-5 FTP force/calibration: **UNRESOLVED**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED**;
- Apollo 11 as-flown throttle/pressure relationships: **DOCUMENTED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7: **BLOCKED ON NAMED SOURCE RECOVERY; PUBLICATION CONFIRMED SEPTEMBER 1970**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.