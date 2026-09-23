# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; exact DPS delivered-performance evidence remains blocked.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents named event masses but no PDI mass.

The Apollo 11 Press Kit specifies **9,870 lbf** maximum-rated DPS thrust; NASA TN D-7143 records a **10,500-lbf maximum-rated design requirement**. The Mission Report confirms LM-5 throttle-up to FTP about 26 seconds after PDI. LMA790-3-LM page 2.2-215, **Change Date 15 June 1969**, directly documents the **92.5% THRUST** TTCA hard stop in the LM-5 handbook state.

A primary NASA-MSC records-transmittal listing identifies **Operational Calibration Curves, Vol. II — Calibration Curves for LM-5**, dated **12 June 1969**, in the Apollo 11 launch-data holdings. Direct page-image inspection supplies a concrete recovery key: **FRC accession 72-A-1116 / Record Group 255 / agency box 71**. The FRC-only field also bears `3751-30`, but it is struck/annotated on the form and is retained only as a legacy locator. The index does not expose the volume's curves or channel coverage, so it does **not** establish a DPS thrust curve, FTP-force mapping, or telemetry conversion.

A separate primary NASA-MSC/NARA launch-data listing for **Apollo 12** establishes the same vehicle-specific calibration-series structure, with **Vol. II assigned to LM-6**. It strengthens the archival interpretation but does not reveal LM-5 curve names or values.

Official NARA **Record Group 255** guidance now independently places **Manned Spacecraft Center / Johnson Space Center textual records in Fort Worth**. An official NARA Apollo-history article likewise identifies the National Archives Southwest Region, Fort Worth, as the repository for more than 8,600 cubic feet of transferred JSC RG 255 records. This makes **NARA Fort Worth / RG 255 / accession 72-A-1116 / agency box 71** the evidence-supported next recovery route. It does not independently prove the current shelf location of box 71. A fresh public-web/NASA/NTRS search did not recover a digitized copy, so the volume remains **BLOCKED ON DOCUMENT RECOVERY**.

The handbook target remains **LMA790-3-LM §2.3.5, page 2.3-25, Table 2.3-1** and is **BLOCKED ON LEGIBLE PAGE-IMAGE / LEP RECOVERY**. Apollo 11 Mission Report Supplement 7 remains blocked on content/identifier recovery.

The FTP-force lead also has a primary bibliographic identity: **John P. Mayer, MSC Mission Planning and Analysis Division, memorandum 69-FMZ2-149, 5 June 1969, “Effect of Fixed Throttle Point Thrust on the Time from Loss of Radial Guidance Control to DPS Throttle-down.”** This supplies an actionable memo number but no numerical FTP result.

The same 26 Oct 1971 NASA-MSC transmittal lists **MSC-69-FM-156** and the Apollo 11 Vol. IV descent/ascent dispersion-analysis sequence under **box 3751-33 / WRCS 25 Item 1a**. Memo 69-FMZ2-149 is not visible in the scanned index, so no box assignment is inferred for it.

The source trail preserves two states of 69-FM-156: a later primary reference cites a **10 Jun 1969 “G Mission Lunar Descent Dispersion Analysis,”** while Purdue catalogs a **2 Jul 1969 Apollo 11 Vol. IV Part 1 Lunar Descent addendum** under the same internal-note number. Treat these as base/addendum states pending recovery.

Two related **8 July 1969** Purdue records remain active recovery targets: **“Effects of DPS engine dispersions and LM weight on throttle-down time”** and **“Effects of known dispersions at PDI on throttle-down time.”** No force, weight, mass, or dispersion value is inferred from their titles.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from bibliographic/archival recovery alone.

## Implementation boundary

Keep PDI mass modelled until explicitly recovered. Preserve 9,870 lbf as Apollo 11 preflight specification, FTP as an Apollo 11 flight control state, and 92.5 percent as an LM-5-effective documented control hard stop. Do **not** numerically equate 92.5 percent with 9,870 lbf without LM-5-specific force-calibration evidence. Do not assume the located LM-5 calibration volume contains a DPS force mapping until its pages are recovered.

## Evidence status

- LM-5 postflight named-event masses: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- LM-5 FTP use/timing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- 92.5-percent throttle hard stop: **DOCUMENTED — LM-5-EFFECTIVE HANDBOOK PAGE, 15 JUNE 1969**;
- LM-5 Operational Calibration Curves Volume II identity/date: **DOCUMENTED — PRIMARY NASA-MSC RECORDS TRANSMITTAL; 12 JUNE 1969**;
- LM-5 Operational Calibration Curves archival locator: **DOCUMENTED — FRC ACCESSION 72-A-1116 / RG 255 / AGENCY BOX 71; `3751-30` RETAINED ONLY AS STRUCK/ANNOTATED LEGACY FRC LOCATOR**;
- MSC/JSC RG 255 repository route: **DOCUMENTED — OFFICIAL NARA RG 255 GUIDE; TEXTUAL RECORDS IN FORT WORTH**;
- LM-5 Operational Calibration Curves contents/DPS applicability: **BLOCKED ON DOCUMENT RECOVERY; NARA FORT WORTH REFERENCE REQUEST IS NEXT ACTIVE CONTROL ACTION**;
- 5 June 1969 FTP study identity: **DOCUMENTED — PURDUE MSA 5 + PRIMARY NASA/MSC REFERENCE LIST; JOHN P. MAYER; MEMO 69-FMZ2-149**;
- 5 June FTP study contents/numerical result: **BLOCKED ON DOCUMENT RECOVERY**;
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