# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents a mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The actual 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; FTP provenance tightened.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents **33,683.5 lb at LM separation; 33,669.6 lb at DOI ignition; 33,401.6 lb at DOI cutoff; 16,153.2 lb at lunar landing**. It does not provide PDI mass.

The contemporary NASA **Apollo 11 Press Kit** specifies **9,870 lbf** as the DPS mission-facing maximum-rated thrust. NASA TN D-7143 records a **10,500-lbf maximum-rated design requirement**. The Apollo 11 Mission Report confirms LM-5 throttle-up to FTP about 26 seconds after PDI.

A follow-up provenance check prevents overclaiming the operations-handbook evidence. The searchable LMA790-3-LM Subsystems Data copy that describes the automatic ceiling as a **92.5-percent FTP** and states **9,870 lbf nominal thrust at fixed full throttle** belongs to a later LM handbook family. Smithsonian catalogs the 1 February 1970 Volume I as **LM-7 and subsequent**; NTRS identifies a later handbook as **LM-11 and subsequent**. Those passages therefore document mature-LM control semantics, not a recovered LM-5 calibration.

The mission-specific evidence remains strong but bounded: Apollo 11 documentation gives the 9,870-lbf preflight specification and confirms use of FTP in flight. Exact LM-5 FTP force/calibration and delivered thrust remain unresolved until an LM-5 configuration-controlled source or postflight propulsion evaluation is recovered.

NASA SP-4029 and NASA 20080013635 remain rejected for PDI closure because their event/value assignments do not establish the missing Mission-G PDI state.

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation*, is independently documented by later NASA mission-report supplement tables as published in **September 1970**, but its contents remain **BLOCKED ON NAMED SOURCE RECOVERY**. No identifier or performance value is inferred from neighboring mission supplements.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this propulsion-source audit.

## Implementation boundary

Use primary Mission Report masses only at their named events. PDI mass remains a model input until an explicitly labeled Mission-G/LM-5 PDI/pre-PDI source is recovered. Preserve 9,870 lbf as an Apollo 11 preflight DPS specification and FTP as an Apollo 11 flight control state. Treat later-handbook 9,870-lbf fixed-full-throttle semantics as configuration-qualified corroboration only. Do not convert flight throttle percentage to exact LM-5 force without LM-5-specific calibration/performance evidence.

## Evidence status

- LM-5 postflight mass at separation / DOI ignition / DOI cutoff / landing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf mission-facing preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- LM-5 use/timing of fixed throttle point: **DOCUMENTED — PRIMARY APOLLO 11 MISSION REPORT**;
- 92.5-percent FTP and 9,870-lbf nominal fixed-full-throttle semantics: **DOCUMENTED — LATER-LM PRIMARY OPERATIONS HANDBOOK; NOT LM-5 CALIBRATION**;
- D-7143 10,500-lbf maximum-rated value: **DOCUMENTED — PROGRAM/DESIGN REQUIREMENT, NOT LM-5 DELIVERED THRUST**;
- exact LM-5 FTP force/calibration: **UNRESOLVED**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED**;
- Apollo 11 as-flown throttle/pressure relationships: **DOCUMENTED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7: **BLOCKED ON NAMED SOURCE RECOVERY; PUBLICATION CONFIRMED SEPTEMBER 1970**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.