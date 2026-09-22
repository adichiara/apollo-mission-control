# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; LM-5 control-limit provenance now direct.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents **33,683.5 lb at LM separation; 33,669.6 lb at DOI ignition; 33,401.6 lb at DOI cutoff; 16,153.2 lb at lunar landing**. It does not provide PDI mass.

The Apollo 11 Press Kit specifies **9,870 lbf** maximum-rated DPS thrust; NASA TN D-7143 records a **10,500-lbf maximum-rated design requirement**. The Mission Report confirms LM-5 throttle-up to FTP about 26 seconds after PDI.

NASA Apollo News Reference GN&C material describes the descent-engine throttle hard stop as **92.5 percent thrust** and the automatic-throttle integrating counter as **2.7 lb of thrust per pulse**. LMA790-3-LM page 2.2-222, changed 15 March 1969, independently gives the 92.5-percent automatic ceiling.

The stronger recovery is **LMA790-3-LM page 2.2-215, Change Date 15 June 1969**, retained in the September LM-6-and-subsequent Volume-I scan. Figure 2.2-62, *Thrust/Translation Controller Assembly — Angular Displacements*, labels the throttle hard-stop position **92.5% THRUST**. The September issue explicitly supersedes **LM-5 and Subsequent dated 15 June 1969**, so this page is directly effective in the LM-5 handbook state. The 92.5-percent control-limit configuration question is therefore closed.

The surviving later full handbook describes **9,870 lbf nominal fixed-full-throttle thrust**, but that later force statement is not promoted to an LM-5 calibration. Exact LM-5 force at the 92.5-percent control point remains unresolved.

The next CONTROL target is the **DPS §2.3 performance/design pages with individual effective dates of 15 June 1969 or earlier**, followed by Apollo 11 DPS Supplement 7 or LM-5 acceptance/performance records for delivered performance.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this source recovery.

## Implementation boundary

Use Mission Report masses only at their named events. Keep PDI mass modelled until explicitly recovered. Preserve 9,870 lbf as Apollo 11 preflight specification, FTP as an Apollo 11 flight control state, and **92.5 percent as an LM-5-effective documented control hard stop**. Do **not** numerically equate 92.5 percent with 9,870 lbf without LM-5-specific force-calibration evidence.

## Evidence status

- LM-5 postflight named-event masses: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- LM-5 FTP use/timing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- 92.5-percent throttle hard stop: **DOCUMENTED — LM-5-EFFECTIVE HANDBOOK PAGE, 15 JUNE 1969**;
- LM-5 Volume-I **DPS performance/calibration pages**: **UNRESOLVED / TARGETED RECOVERY**;
- exact LM-5 FTP force/calibration: **UNRESOLVED**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7: **BLOCKED ON NAMED SOURCE RECOVERY**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.