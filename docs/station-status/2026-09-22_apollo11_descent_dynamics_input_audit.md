# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; exact DPS delivered-performance evidence remains blocked.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents named event masses but no PDI mass.

The Apollo 11 Press Kit specifies **9,870 lbf** maximum-rated DPS thrust; NASA TN D-7143 records a **10,500-lbf maximum-rated design requirement**. The Mission Report confirms LM-5 throttle-up to FTP about 26 seconds after PDI. LMA790-3-LM page 2.2-215, **Change Date 15 June 1969**, directly documents the **92.5% THRUST** TTCA hard stop in the LM-5 handbook state.

The handbook target remains **LMA790-3-LM §2.3.5, page 2.3-25, Table 2.3-1** and is **BLOCKED ON LEGIBLE PAGE-IMAGE / LEP RECOVERY**. Apollo 11 Mission Report Supplement 7 remains blocked on content/identifier recovery.

The highest-priority force-calibration lead has a primary bibliographic identity. A NASA/MSC mission-techniques reference list cites the exact Purdue MSA 5 title as **John P. Mayer, MSC Mission Planning and Analysis Division, memorandum 69-FMZ2-149, 5 June 1969, “Effect of Fixed Throttle Point Thrust on the Time from Loss of Radial Guidance Control to DPS Throttle-down.”** The OCR rendering `FMZ2` is preserved pending recovery of the clean memo title page. This supplies an actionable memo number but no numerical FTP result.

A primary NASA-MSC **26 Oct 1971 records-transmittal index** now adds a concrete archival trail for neighboring Apollo 11 MPAD material: page 17 lists **MSC-69-FM-156** and the Apollo 11 Vol. IV descent/ascent dispersion-analysis sequence under **box 3751-33 / WRCS 25 Item 1a**. Memo 69-FMZ2-149 is not visible in the scanned index, so no box assignment is inferred for it. This lead is for document recovery only.

The source trail also preserves two states of 69-FM-156: a later primary reference cites a **10 Jun 1969 “G Mission Lunar Descent Dispersion Analysis,”** while Purdue catalogs a **2 Jul 1969 Apollo 11 Vol. IV Part 1 Lunar Descent addendum** under the same internal-note number. Treat these as base/addendum states pending recovery rather than merging their dates or contents.

Two related **8 July 1969** Purdue records remain active recovery targets: **“Effects of DPS engine dispersions and LM weight on throttle-down time”** (File 2, Item 20) and **“Effects of known dispersions at PDI on throttle-down time”** (File 2, Item 21). No force, weight, mass, or dispersion value is inferred from their titles.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from bibliographic/archival recovery alone.

## Implementation boundary

Keep PDI mass modelled until explicitly recovered. Preserve 9,870 lbf as Apollo 11 preflight specification, FTP as an Apollo 11 flight control state, and 92.5 percent as an LM-5-effective documented control hard stop. Do **not** numerically equate 92.5 percent with 9,870 lbf without LM-5-specific force-calibration evidence.

## Evidence status

- LM-5 postflight named-event masses: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- LM-5 FTP use/timing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- 92.5-percent throttle hard stop: **DOCUMENTED — LM-5-EFFECTIVE HANDBOOK PAGE, 15 JUNE 1969**;
- 5 June 1969 FTP study identity: **DOCUMENTED — PURDUE MSA 5 + PRIMARY NASA/MSC REFERENCE LIST; JOHN P. MAYER; MEMO 69-FMZ2-149**;
- neighboring Apollo 11 MPAD FM archival series: **DOCUMENTED — PRIMARY NASA-MSC RECORDS TRANSMITTAL; BOX 3751-33 / WRCS 25 ITEM 1a FOR LISTED RECORDS**;
- 5 June FTP study contents/numerical result: **BLOCKED ON DOCUMENT RECOVERY; NEXT ACTIVE CONTROL TARGET**;
- 69-FM-156 June base / July addendum relationship: **PARTIALLY DOCUMENTED; BLOCKED ON TITLE-PAGE/CONTENT RECOVERY**;
- two 8 July throttle-down studies: **DOCUMENTED AS ARCHIVAL RECORDS; CONTENT BLOCKED ON ITEM RECOVERY**;
- DPS performance table location: **DOCUMENTED — §2.3.5 / PAGE 2.3-25 / TABLE 2.3-1**;
- page 2.3-25 LM-5 effective date/table values: **BLOCKED ON LEGIBLE PRIMARY PAGE-IMAGE / LEP RECOVERY**;
- exact LM-5 FTP force/calibration: **UNRESOLVED**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7 existence/title/date: **DOCUMENTED — LATER NASA SUPPLEMENT TABLES**;
- Apollo 11 underlying LM-5 DPS project-report identifier/content: **BLOCKED ON BIBLIOGRAPHIC / ARCHIVAL RECOVERY**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.