# Apollo 11 / R-567 LUMINARY 1A source-catalog addendum

Date: 2026-09-19

## Controlled sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| MIT/IL Apollo Project Memo 7-69, George W. Cherry, *What is LUMINARY 1A? Some Results of the 28th Apollo Software Configuration Control Board Meeting*, 23 Jan 1969 | Identifies LUMINARY 1A as the Mission G program; approved PCR 700 and PCR 670 | Primary configuration-control intent; not alone proof of final Rev. 099 behavior. |
| MIT/IL Apollo Project Memo 9-69, *Results of the 29th Apollo Software Configuration Control Board Meeting* | Lists PCR-700A under the P66-performance title and explicitly states it is a clarifying rewrite of PCR-700, with action already assigned | Primary PCR-700→700A change-control crosswalk; not Section 5 page effectivity. |
| MIT/IL LUMINARY Memo #67, *LUMINARY Revisions 70-79* | Revision 72 implemented PCR-700 and PCR-670 | Primary program implementation ancestry. |
| MIT/IL LUMINARY Memo #73, *LUMINARY Revisions 80-92*, 26 Mar 1969 | Revision 80 modified P66 for total-lag compensation and added `LAG/TAU` under PCR-700 | Primary later implementation evidence. |
| `SNA-8-D-027(II) REV 1`, LM Data Book Volume II, 11 Jun 1969 | Mission G LUMINARY 99 load includes `LAG/TAU = 0.413333` | Apollo 11 mission/configuration evidence. |
| MIT/IL LUMINARY 099 assembly listing, `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc` | `P66VERTA` schedules `RODTASK` with `1SEC`; `RODTASK` dispatches `RODCOMP`; `RODCOMP` updates `VDGVERT`/`HDOTDISP` and consumes `LAG/TAU` | Direct Apollo 11 program evidence for one-second P66 ROD computation scheduling; not DSKY/downlink/MCC cadence. |
| MIT/IL `R-567`, Section 2, Revision 4, June 1969 | Explicitly names **LUMINARY 1A (Rev. 099)** and lists PCR-670/PCR-700 | Section-2-specific effectivity evidence; do not transfer revision number to Section 5. |
| MIT/IL `R-567`, Section 5, Revision 8, front matter | Preserves an **Incorporated in Rev. 4 of GSOP** inventory lacking PCR-670/PCR-700; lists later P66 changes | Primary Section-5 history and later-change boundary. |
| MIT/IL `R-567`, Section 5, Revision 11, cumulative front matter | Preserves historical **Guidance Equations (Revision 5)** index listing PCR-670 and PCR-700A without later-revision dagger marks | Earliest directly recovered Section-5 control state inspected containing both identifiers; not by itself Apollo 11 page effectivity. |
| Luminary 99/1 assembly listing, assembly/operation information | Identifies LUMINARY 1A and states implementation details are specified in `R-567, as amended` | Program-to-GSOP relationship. |
| MSC `69-FS-4`, *Programmed Guidance Equations for LUMINARY 1B* | Page-change record states it is a **complete re-issue** of May 1969 MSC Internal Note `69-FS-3`, *Programmed Guidance Equations for LUMINARY 1A Manned LM Earth Orbital and Lunar Program*, updated for LUMINARY 1B; contains later P66 definitions | Primary provenance for the missing 1A note and later programmed-equation comparison endpoint. Do not back-project 1B equations without unchanged ancestry. |
| Virtual AGC document-library PCR catalog | Lists PCR-700A and its title | Retrieval/index aid only; superseded as crosswalk evidence by primary Memo 9-69. |

## D-024 state after research 400–404

The bounded Apollo 11 P66/PCR-700 question is **SUFFICIENT for current implementation**. The final LUMINARY 099 program closes the P66 ROD computation interval at one second, and Apollo Project Memo 9-69 closes the PCR-700/PCR-700A identity question. The closure challenge confirms from `69-FS-4` that May 1969 `69-FS-3` is the LUMINARY 1A predecessor, but does not supply enough unchanged-page evidence to promote later equations backward.

Section 5 Revision 5 descriptive-equation ancestry/effectivity and direct `69-FS-3` contents are therefore **DEFERRED**, not active retrieval priorities, until a named implementation dependency or reopen trigger exists.

## Reopen priority

1. Direct recovery of `69-FS-3` or Apollo-11-effective Section 5 P63–P66 pages.
2. Contradictory mission-specific primary evidence.
3. Implementation requiring exact descriptive P63–P66 equations.
4. Crew-visible Noun 63 timing requirement, triggering separate DSKY display-service research.
5. Station-visible timing requirement, triggering separate downlink/ground-display research.

Do not spend further effort reconfirming the one-second computation cadence, PCR-700/PCR-700A crosswalk, or descriptive-page ancestry absent one of these triggers.

## Sources

- https://www.ibiblio.org/apollo/Documents/Memo-SCB28_text.pdf
- https://www.ibiblio.org/apollo/Documents/Memo-SCB29_text.pdf
- https://www.ibiblio.org/apollo/Documents/LUM67_text.pdf
- https://www.ibiblio.org/apollo/Documents/LUM73.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc.html
- https://ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- https://www.ibiblio.org/apollo/NARA-SW/R-567-sec5-rev8-5.1-5.2.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-R-567-SEC5-REV11_text.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc.html
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
- https://www.ibiblio.org/apollo/links2.html