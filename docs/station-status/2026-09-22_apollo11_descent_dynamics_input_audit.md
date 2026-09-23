# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; exact DPS delivered-performance evidence remains blocked.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents named event masses but no PDI mass.

The Apollo 11 Press Kit specifies **9,870 lbf** maximum-rated DPS thrust; NASA TN D-7143 records a **10,500-lbf maximum-rated design requirement**. The Mission Report confirms LM-5 throttle-up to FTP about 26 seconds after PDI. LMA790-3-LM page 2.2-215, **Change Date 15 June 1969**, directly documents the **92.5% THRUST** TTCA hard stop in the LM-5 handbook state.

The handbook target remains **LMA790-3-LM §2.3.5, page 2.3-25, Table 2.3-1** and is **BLOCKED ON LEGIBLE PAGE-IMAGE / LEP RECOVERY**.

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation*, is primary-documented by later NASA supplement tables as published in **September 1970**, but its public catalog record/content remains unrecovered. Apollo 10 primary evidence shows its corresponding supplement wraps TRW **11176-H314-R0-00**, so the underlying LM-5 contractor report remains an active target; no Apollo 11 number is interpolated.

The highest-priority force-calibration lead remains the **5 June 1969** Armstrong MSA 5 planning item, **“Effect of fixed throttle point thrust on the time from loss of radial guidance control to DPS throttle-down.”** A follow-on Purdue catalog pass adds two closely related **8 July 1969** records in the same Mission Planning subgroup:

- **“Effects of DPS engine dispersions and LM weight on throttle-down time”** — File 2, Item 20 (Box 54, Folder 5, Item 14).
- **“Effects of known dispersions at PDI on throttle-down time”** — File 2, Item 21 (Box 54, Folder 5, Item 15).

These archive records establish that Apollo 11 planning explicitly treated engine dispersion, LM weight, and PDI dispersions as throttle-down-time variables. They do **not** expose the underlying numerical inputs. No force, weight, mass, or dispersion value is inferred from catalog titles. Recovering all three items is now the active CONTROL archival package.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from locator recovery alone.

## Implementation boundary

Keep PDI mass modelled until explicitly recovered. Preserve 9,870 lbf as Apollo 11 preflight specification, FTP as an Apollo 11 flight control state, and 92.5 percent as an LM-5-effective documented control hard stop. Do **not** numerically equate 92.5 percent with 9,870 lbf without LM-5-specific force-calibration evidence. Do not derive a nominal PDI mass from the existence of a PDI-dispersion study.

## Evidence status

- LM-5 postflight named-event masses: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- LM-5 FTP use/timing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- 92.5-percent throttle hard stop: **DOCUMENTED — LM-5-EFFECTIVE HANDBOOK PAGE, 15 JUNE 1969**;
- 5 June 1969 Apollo 11 fixed-throttle-point-thrust planning item existence/title/date: **DOCUMENTED — OFFICIAL PURDUE MSA 5 FINDING AID**;
- 8 July 1969 DPS-engine-dispersion/LM-weight throttle-down study existence/title/date/identifier: **DOCUMENTED — OFFICIAL PURDUE ARCHIVAL CATALOG**;
- 8 July 1969 PDI-dispersion throttle-down study existence/title/date/identifier: **DOCUMENTED — OFFICIAL PURDUE ARCHIVAL CATALOG**;
- contents/numerical evidence of those three MSA 5 items: **BLOCKED ON ARCHIVAL ITEM RECOVERY; NEXT ACTIVE CONTROL TARGETS**;
- DPS performance table location: **DOCUMENTED — §2.3.5 / PAGE 2.3-25 / TABLE 2.3-1**;
- page 2.3-25 LM-5 effective date/table values: **BLOCKED ON LEGIBLE PRIMARY PAGE-IMAGE / LEP RECOVERY**;
- exact LM-5 FTP force/calibration: **UNRESOLVED**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7 existence/title/date: **DOCUMENTED — LATER NASA SUPPLEMENT TABLES**;
- Apollo 11 underlying LM-5 DPS project-report identifier/content: **BLOCKED ON BIBLIOGRAPHIC / ARCHIVAL RECOVERY**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.