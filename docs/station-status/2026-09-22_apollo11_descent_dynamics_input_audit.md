# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; FTP control provenance improved.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents **33,683.5 lb at LM separation; 33,669.6 lb at DOI ignition; 33,401.6 lb at DOI cutoff; 16,153.2 lb at lunar landing**. It does not provide PDI mass.

The Apollo 11 Press Kit specifies **9,870 lbf** maximum-rated DPS thrust; NASA TN D-7143 records a **10,500-lbf maximum-rated design requirement**. The Mission Report confirms LM-5 throttle-up to FTP about 26 seconds after PDI.

NASA Apollo News Reference GN&C material describes the descent-engine throttle hard stop as **92.5 percent thrust** and the automatic-throttle integrating counter as **2.7 lb of thrust per pulse**. Separately, searchable LMA790-3-LM control material in the **15 December 1968 basic-date lineage**, on a page changed **15 March 1969**, states that the automatic-throttle counter ceiling combined with the fixed 10-percent TTCA output corresponds to **92.5 percent thrust**. This moves the 92.5-percent control-law evidence into the pre-Apollo-11 documentation lineage.

A NASA ALSJ-hosted primary excerpt directly demonstrates **LM-5-era Volume-I Subsystems Data** through explicit “On LM 5” versus “LM 6 and subsequent vehicles” language, but the excerpt is not DPS. The surviving later full handbook additionally describes **9,870 lbf nominal fixed-full-throttle thrust**, but that later force statement is not promoted to an LM-5 calibration.

Therefore the exact remaining CONTROL propulsion question is narrow: recover the **LM-5-era DPS performance/design pages or engine acceptance/final-flight-evaluation evidence** that establishes the force/performance mapping for Eagle itself. Apollo 11 DPS Supplement 7 remains **BLOCKED ON NAMED SOURCE RECOVERY**.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this source recovery.

## Implementation boundary

Use Mission Report masses only at their named events. Keep PDI mass modelled until explicitly recovered. Preserve 9,870 lbf as Apollo 11 preflight specification, FTP as an Apollo 11 flight control state, and 92.5 percent as a documented pre-Apollo-11 control-law ceiling. Do **not** numerically equate 92.5 percent with 9,870 lbf without LM-5-specific calibration evidence.

## Evidence status

- LM-5 postflight named-event masses: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- LM-5 FTP use/timing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- 92.5-percent FTP/control-law ceiling: **DOCUMENTED — PRE-APOLLO-11 HANDBOOK / NASA CONTROL DOCUMENTATION**;
- LM-5-era Volume-I Subsystems Data provenance: **DOCUMENTED — NASA-HOSTED PRIMARY EXCERPT**;
- LM-5 Volume-I **DPS performance/calibration pages**: **UNRESOLVED / TARGETED RECOVERY**;
- exact LM-5 FTP force/calibration: **UNRESOLVED**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7: **BLOCKED ON NAMED SOURCE RECOVERY**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.