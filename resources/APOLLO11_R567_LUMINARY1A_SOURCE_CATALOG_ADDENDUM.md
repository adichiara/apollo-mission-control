# Apollo 11 / R-567 LUMINARY 1A source-catalog addendum

Date: 2026-09-19

## Controlled sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| MIT/IL Apollo Project Memo 7-69, George W. Cherry, *What is LUMINARY 1A? Some Results of the 28th Apollo Software Configuration Control Board Meeting*, 23 Jan 1969 | Identifies LUMINARY 1A as the Mission G program; approved PCR 700 and PCR 670 | Primary configuration-control intent; not alone proof of final Rev. 099 behavior. |
| MIT/IL LUMINARY Memo #73, *LUMINARY Revisions 80-92*, 26 Mar 1969 | Revision 80 implemented PCR-700 P66 total-lag compensation; defines `LAG/TAU` | Primary implementation evidence. |
| `SNA-8-D-027(II) REV 1`, LM Data Book Volume II, 11 Jun 1969 | Mission G LUMINARY 99 load includes `LAG/TAU = 0.413333` | Apollo 11 mission/configuration evidence; do not convert ratio to physical lag without controlled `TAUROD`. |
| MIT/IL `R-567`, Section 2, Revision 4, June 1969 | Explicitly names **LUMINARY 1A (Rev. 099)** and lists PCR-670/PCR-700 | Section-2-specific effectivity evidence; does not establish Section 5 revision state. |
| MIT/IL `R-567`, Section 5, Revision 8, front matter | Preserves an **Incorporated in Rev. 4 of GSOP** inventory running through PCN 755 and including PCR 636; PCR-670/PCR-700 are absent from the recovered Rev.-4 inventory | Primary section-history evidence. Demonstrates that Section 2 Rev. 4 cannot be used to infer Section 5 Rev. 4 content/effectivity. |
| MIT/IL `R-567`, Section 5, Revision 11, cumulative front matter | Preserves historical Section 5 Rev. 4 sheet with Revision-7 dagger annotations | Use to reconcile ancestry; do not back-project later equations. |
| Luminary 99/1 assembly listing | Identifies LUMINARY 1A and states implementation details are specified in `R-567, as amended` | Program-to-GSOP relationship; no complete section revision set. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Identifies `69-FS-3` (May 1969) as its LUMINARY 1A predecessor | Bibliographic route to missing Apollo 11 equation document. |

## Effectivity lesson from research 331

The repository must treat R-567 revision numbers as **section-specific** unless a source explicitly establishes synchronization. Section 2 Revision 4 is a June 1969 LUMINARY 1A Rev. 099 state containing PCR-670/PCR-700. The recovered Section 5 Revision-4 inventory does not contain those identifiers. Section 5 Revision 4 therefore remains a historical anchor, not the presumed final Apollo 11 equation state.

## Retrieval priority

1. Identify the Section 5 revision/change state that first documents PCR-670 and/or PCR-700.
2. Recover its landing-program/P63-P66 affected pages and establish LUMINARY 1A Rev. 099 effectivity.
3. Reconcile Revision 8 and Revision 11 cumulative front-matter annotations and page ancestry.
4. Recover `69-FS-3` as the preferred complete LUMINARY 1A programmed-guidance-equation source.
5. Only then evaluate exact P66 equations/cadence and controller-facing consequences.

## Sources

- https://www.ibiblio.org/apollo/Documents/Memo-SCB28_text.pdf
- https://www.ibiblio.org/apollo/Documents/LUM73.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- https://www.ibiblio.org/apollo/NARA-SW/R-567-sec5-rev8-5.1-5.2.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-R-567-SEC5-REV11_text.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc.html
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf