# Station research status — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## GUIDANCE / FIDO

**Status: PARTIALLY DOCUMENTED, bounded.** TRW Note 70-FMT-819 Volume I documents mission-specific postflight continuous LM trajectory reconstruction from DOI through touchdown. NASA TN D-6846 supplies a primary validation envelope. The 45-day BET NAT listing remains **BLOCKED ON NAMED SOURCE RECOVERY — Volume II**.

## CONTROL

**Status: PARTIALLY DOCUMENTED; DPS page target blocked on legible primary-page recovery.** Apollo 11 Mission Report §9.8/fig. 9.8-1 document powered-descent timing and flight throttle/pressure histories. Appendix A.6/table A-I documents named event masses but no PDI mass.

The Apollo 11 Press Kit specifies **9,870 lbf** maximum-rated DPS thrust; NASA TN D-7143 records a **10,500-lbf maximum-rated design requirement**. The Mission Report confirms LM-5 throttle-up to FTP about 26 seconds after PDI. LMA790-3-LM page 2.2-215, **Change Date 15 June 1969**, directly documents the **92.5% THRUST** TTCA hard stop in the LM-5 handbook state.

The exact handbook target remains **LMA790-3-LM §2.3.5, page 2.3-25, Table 2.3-1 — Descent Propulsion Section Performance and Design Data**. A follow-on recovery pass reached the September 1969 issue's primary **List of Effective Pages** and confirmed that the relevant handbook uses individual page revision states. The available indexed rendering is too OCR-corrupted around the 2.3 ranges to read page 2.3-25's own issue date defensibly, and it does not expose the table body reliably. The page is therefore **BLOCKED ON LEGIBLE PAGE-IMAGE / LEP RECOVERY**, not configuration-qualified.

A later NASA-hosted handbook preserves the same section/table/page structure but remains a locator cross-check only. Its values must not be back-projected onto Eagle.

## FLIGHT / CAPCOM

**Status: unchanged.** No new GO/NO-GO criterion or crew-facing call follows from this source recovery.

## Implementation boundary

Keep PDI mass modelled until explicitly recovered. Preserve 9,870 lbf as Apollo 11 preflight specification, FTP as an Apollo 11 flight control state, and 92.5 percent as an LM-5-effective documented control hard stop. Do **not** numerically equate 92.5 percent with 9,870 lbf without LM-5-specific force-calibration evidence.

## Evidence status

- LM-5 postflight named-event masses: **DOCUMENTED — PRIMARY MISSION REPORT**;
- Apollo 11 DPS 9,870-lbf preflight specification: **DOCUMENTED — CONTEMPORARY PRIMARY MISSION SOURCE**;
- LM-5 FTP use/timing: **DOCUMENTED — PRIMARY MISSION REPORT**;
- 92.5-percent throttle hard stop: **DOCUMENTED — LM-5-EFFECTIVE HANDBOOK PAGE, 15 JUNE 1969**;
- DPS performance table location: **DOCUMENTED — §2.3.5 / PAGE 2.3-25 / TABLE 2.3-1**;
- page 2.3-25 LM-5 effective date/table values: **BLOCKED ON LEGIBLE PRIMARY PAGE-IMAGE / LEP RECOVERY**;
- exact LM-5 FTP force/calibration: **UNRESOLVED**;
- exact LM-5 PDI/pre-PDI mass: **UNRESOLVED**;
- 45-day BET NAT state listing: **BLOCKED ON NAMED SOURCE RECOVERY — VOLUME II**;
- Apollo 11 DPS Supplement 7: **BLOCKED ON NAMED SOURCE RECOVERY; NEXT ACTIVE PROPULSION TARGET**;
- exact delivered thrust/Isp history: **UNRESOLVED**;
- new player-visible station products: **NONE CLAIMED**.