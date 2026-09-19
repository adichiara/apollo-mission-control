# Apollo 11 / R-567 LUMINARY 1A source-catalog addendum

Date: 2026-09-19

## Controlled sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| MIT/IL Apollo Project Memo 7-69, George W. Cherry, *What is LUMINARY 1A? Some Results of the 28th Apollo Software Configuration Control Board Meeting*, 23 Jan 1969 | Identifies LUMINARY 1A as the Mission G program; approved PCR 700 and PCR 670 | Primary configuration-control intent; not alone proof of final Rev. 099 behavior. |
| MIT/IL Apollo Project Memo 9-69, *Results of the 29th Apollo Software Configuration Control Board Meeting* | Lists PCR-700A under the P66-performance title and explicitly states it is a clarifying rewrite of PCR-700, with action already assigned; discusses the lag-compensation idea being implemented | Primary PCR-700→700A change-control crosswalk. Does not by itself establish Section 5 page effectivity. |
| MIT/IL LUMINARY Memo #67, *LUMINARY Revisions 70-79* | Revision 72 implemented PCR-700 and PCR-670; PCR-700 added `RODSCALE` and `TAUROD` | Primary program implementation ancestry. |
| MIT/IL LUMINARY Memo #73, *LUMINARY Revisions 80-92*, 26 Mar 1969 | Revision 80 modified P66 for total-lag compensation and added `LAG/TAU` under PCR-700 | Primary later implementation evidence. |
| `SNA-8-D-027(II) REV 1`, LM Data Book Volume II, 11 Jun 1969 | Mission G LUMINARY 99 load includes `LAG/TAU = 0.413333` | Apollo 11 mission/configuration evidence; do not convert ratio to physical lag without controlled `TAUROD`. |
| MIT/IL LUMINARY 099 assembly listing, `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc` | `P66VERTA` schedules `RODTASK` with `1SEC`; `RODTASK` dispatches `RODCOMP`; `RODCOMP` updates `VDGVERT`/`HDOTDISP` and consumes `LAG/TAU` | Direct Apollo 11 program evidence for one-second P66 ROD computation scheduling. Does not establish DSKY, downlink, MCC, or controller-visible refresh cadence. |
| MIT/IL `R-567`, Section 2, Revision 4, June 1969 | Explicitly names **LUMINARY 1A (Rev. 099)** and lists PCR-670/PCR-700 | Section-2-specific effectivity evidence; do not transfer its revision number to Section 5. Memo 9-69 now explains why Section 5 can identify the same P66 change as PCR-700A. |
| MIT/IL `R-567`, Section 5, Revision 8, front matter | Preserves an **Incorporated in Rev. 4 of GSOP** inventory lacking PCR-670/PCR-700; also explicitly controls LUMINARY 1C and lists later P66 changes PCR-988/PCR-1013; notes some unchanged pages were republished | Primary Section-5 history and later-change boundary. |
| MIT/IL `R-567`, Section 5, Revision 11, cumulative front matter | Preserves historical **Guidance Equations (Revision 5)** index listing PCR-670 and PCR-700A without later-revision dagger marks | Earliest directly recovered Section-5 control state in the inspected chain containing both landing-change identifiers; does not by itself prove first historical incorporation or Apollo 11 page effectivity. |
| Luminary 99/1 assembly listing, assembly/operation information | Identifies LUMINARY 1A and states implementation details are specified in `R-567, as amended` | Program-to-GSOP relationship. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Identifies `69-FS-3` (May 1969) as its LUMINARY 1A predecessor; contains explicit later P66 definitions including `VBIAS`, `VDGVERT`, and `WCHVERT` | Primary later programmed-equation comparison endpoint. Do not back-project later descriptive equations into Apollo 11 without unchanged ancestry. |
| Virtual AGC document-library PCR catalog | Lists PCR-700A and its title | Retrieval/index aid only; its former role as the sole 700→700A crosswalk is superseded by primary Apollo Project Memo 9-69. |

## Effectivity lesson from research 331–333

R-567 revision numbers are section-specific. Section 5 Revision 5 remains the concrete descriptive-equation retrieval target, while later LUMINARY 1B/1C sources are comparison endpoints. The LUMINARY 099 assembly listing independently closes the exact P66 ROD computation interval: the final program schedules `RODTASK` at `1SEC`. Apollo Project Memo 9-69 independently closes the PCR-number mismatch by identifying PCR-700A as a clarifying rewrite of PCR-700. Neither result makes later descriptive equation pages Apollo 11-effective without a controlled page/effectivity chain.

## Retrieval priority

1. Recover Section 5 Revision 5 landing-program/P63-P66 affected pages when needed for descriptive equation/page ancestry/effectivity.
2. Recover `69-FS-3` as the preferred complete LUMINARY 1A programmed-guidance-equation source.
3. If crew-visible Noun 63 timing becomes material, research the DSKY display-service path separately.
4. If station-visible timing becomes material, establish downlink and ground-display ancestry separately before changing controller products.
5. Do not spend further research effort reconfirming the one-second P66 ROD computation cadence or the PCR-700/PCR-700A crosswalk absent contradictory primary evidence.

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