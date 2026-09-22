# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; LM-5 Volume-I provenance improved.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents **33,683.5 lb at LM separation; 33,669.6 lb at DOI ignition; 33,401.6 lb at DOI cutoff; 16,153.2 lb at lunar landing**. It does not provide PDI mass.

The Apollo 11 Press Kit specifies **9,870 lbf** maximum-rated DPS thrust; NASA TN D-7143 records a **10,500-lbf maximum-rated design requirement**. The Mission Report confirms LM-5 throttle-up to FTP about 26 seconds after PDI.

The later searchable LMA790-3-LM Volume-I copy describes **92.5-percent FTP** and **9,870 lbf nominal fixed-full-throttle thrust**, but its surviving full-handbook provenance is LM-7-and-subsequent or later; it remains mature-LM semantics, not LM-5 calibration.

A NASA ALSJ-hosted primary excerpt now directly demonstrates **LM-5-era Volume-I Subsystems Data**: pages carry **Basic Date 15 December 1968**, explicitly describe hardware **“On LM 5,”** and contrast it with **“LM 6 and subsequent vehicles.”** This materially closes the prior provenance question for LM-5 Volume I. However, the recovered excerpt concerns waste-management/crew equipment, not DPS, and contains no FTP/thrust/Isp calibration. The exact propulsion target is therefore narrowed to the **DPS section/pages from this LM-5-era Volume-I change state**.

LM-5-and-subsequent Volume II Operational Procedures is also recovered but supplies no force calibration. Apollo 11 DPS Supplement 7 remains **BLOCKED ON NAMED SOURCE RECOVERY**.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this source recovery.

## Implementation boundary

Use Mission Report masses only at their named events. Keep PDI mass modelled until explicitly recovered. Preserve 9,870 lbf as Apollo 11 preflight specification and FTP as an Apollo 11 flight control state. The newly recovered LM-5 Volume-I excerpt establishes configuration provenance only; do not infer DPS calibration from unrelated subsystem pages.

## Evidence status

- LM-5 postflight named-event masses: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- LM-5 FTP use/timing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- LM-5-era Volume-I Subsystems Data provenance: **DOCUMENTED — NASA-HOSTED PRIMARY EXCERPT, BASIC DATE 15 DECEMBER 1968**;
- LM-5 Volume-I **DPS section/calibration pages**: **UNRESOLVED / TARGETED RECOVERY**;
- later-LM 92.5-percent FTP / 9,870-lbf fixed-full-throttle semantics: **DOCUMENTED — NOT LM-5 CALIBRATION**;
- exact LM-5 FTP force/calibration: **UNRESOLVED**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7: **BLOCKED ON NAMED SOURCE RECOVERY**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.