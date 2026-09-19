# Apollo 11 / R-567 LUMINARY 1A source-catalog addendum

Date: 2026-09-19

## Controlled sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| MIT/IL Apollo Project Memo 7-69, George W. Cherry, *What is LUMINARY 1A? Some Results of the 28th Apollo Software Configuration Control Board Meeting*, 23 Jan 1969 | Identifies LUMINARY 1A as the Mission G program; approved PCR 700 and PCR 670 | Primary configuration-control intent; not alone proof of final Rev. 099 behavior. |
| MIT/IL LUMINARY Memo #67, *LUMINARY Revisions 70-79* | Revision 72 implemented PCR-700 and PCR-670; PCR-700 added `RODSCALE` and `TAUROD` | Primary program implementation ancestry; does not establish final Apollo 11 equation/page state. |
| MIT/IL LUMINARY Memo #73, *LUMINARY Revisions 80-92*, 26 Mar 1969 | Revision 80 modified P66 for total-lag compensation and added `LAG/TAU` under PCR-700 | Primary later implementation evidence. |
| `SNA-8-D-027(II) REV 1`, LM Data Book Volume II, 11 Jun 1969 | Mission G LUMINARY 99 load includes `LAG/TAU = 0.413333` | Apollo 11 mission/configuration evidence; do not convert ratio to physical lag without controlled `TAUROD`. |
| MIT/IL `R-567`, Section 2, Revision 4, June 1969 | Explicitly names **LUMINARY 1A (Rev. 099)** and lists PCR-670/PCR-700 | Section-2-specific effectivity evidence; does not establish Section 5 revision state. |
| MIT/IL `R-567`, Section 5, Revision 8, front matter | Preserves an **Incorporated in Rev. 4 of GSOP** inventory lacking PCR-670/PCR-700; also explicitly controls LUMINARY 1C and lists later P66 changes PCR-988/PCR-1013 with affected pages; notes some unchanged pages were republished for convenience | Primary Section-5 history and later-change boundary. Later surviving P66 pages cannot be back-projected merely because they appear in this artifact. |
| MIT/IL `R-567`, Section 5, Revision 11, cumulative front matter | Preserves historical **Guidance Equations (Revision 5)** index listing PCR-670 and PCR-700A without later-revision dagger marks | Earliest directly recovered Section-5 control state in the inspected chain containing both landing-change identifiers; does not by itself prove first historical incorporation or Apollo 11 effectivity. |
| Luminary 99/1 assembly listing | Identifies LUMINARY 1A and states implementation details are specified in `R-567, as amended` | Program-to-GSOP relationship; no complete section revision set. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Identifies `69-FS-3` (May 1969) as its LUMINARY 1A predecessor; contains explicit later P66 definitions including `VBIAS`, `VDGVERT`, and `WCHVERT` | Primary later programmed-equation comparison endpoint. Do not back-project 1B equation text/cadence into Apollo 11 without unchanged ancestry. |
| Virtual AGC document-library PCR catalog | Describes PCR-700A as a rewritten clarification of PCR-700 | Secondary retrieval aid only; seek the primary PCR/change-control artifact before treating 700A wording as technically identical to 700. |

## Effectivity lesson from research 331–332

R-567 revision numbers are section-specific. The recovered Section 5 Revision-4 inventory lacks PCR-670/PCR-700, while the historical Section 5 Revision-5 index contains PCR-670/PCR-700A. Revision 5 is therefore the current concrete landing-equation retrieval target. Later LUMINARY 1B/1C sources preserve useful P66 detail, but the documented later P66 changes mean they are comparison endpoints until page-level unchanged ancestry is demonstrated.

## Retrieval priority

1. Recover Section 5 Revision 5 landing-program/P63-P66 affected pages and page-level change markings.
2. Establish LUMINARY 1A Rev. 099/Apollo 11 effectivity or a controlled unchanged-page chain.
3. Use later `69-FS-4` / R-567 states to test that chain while excluding documented later P66 changes.
4. Recover a primary PCR-700/PCR-700A crosswalk.
5. Recover `69-FS-3` as the preferred complete LUMINARY 1A programmed-guidance-equation source.
6. Only then evaluate exact P66 equations/cadence and controller-facing consequences.

## Sources

- https://www.ibiblio.org/apollo/Documents/Memo-SCB28_text.pdf
- https://www.ibiblio.org/apollo/Documents/LUM67_text.pdf
- https://www.ibiblio.org/apollo/Documents/LUM73.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- https://www.ibiblio.org/apollo/NARA-SW/R-567-sec5-rev8-5.1-5.2.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-R-567-SEC5-REV11_text.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc.html
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
- https://www.ibiblio.org/apollo/links2.html