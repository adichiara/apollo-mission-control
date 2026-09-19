# Apollo 11 / R-567 LUMINARY 1A source-catalog addendum

Date: 2026-09-19

## Controlled sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| MIT/IL Apollo Project Memo 7-69, George W. Cherry, *What is LUMINARY 1A? Some Results of the 28th Apollo Software Configuration Control Board Meeting*, 23 Jan 1969 | Identifies LUMINARY 1A as the Mission G program; records approved landing changes PCR 700 and PCR 670; gives proposed P66 changes and GSOP/program action assignments; records PCRs 704/705/706/723 as disapproved at that board state | Primary configuration-control intent. Strong crosswalk/retrieval evidence, but not by itself proof of final Rev. 099 implementation or flight behavior. |
| MIT/IL LUMINARY Memo #73, *LUMINARY Revisions 80-92*, 26 Mar 1969 | Revision 80 implemented PCR-700 P66 total-lag compensation; defines new pad-loaded `LAG/TAU` as total computation+engine-response lag divided by `TAUROD` | Primary implementation evidence. Does not by itself establish final Apollo 11 numerical load or all details of the January PCR proposal. |
| `SNA-8-D-027(II) REV 1`, LM Data Book Volume II, 11 Jun 1969, Mission G prelaunch erasable load | LUMINARY 99 load includes `LAG/TAU` at 2542/2543 with decimal value **0.413333** | Primary Apollo 11 mission/configuration evidence for the PCR-700 parameter. Do not convert this ratio into a physical lag without the controlled `TAUROD` value/interpretation chain. |
| MIT/IL LUMINARY Memo #85, *LUMINARY Revision 99*, 21 May 1969 | Revision 99 change record: LNY70 correction and PCR-775 landing-radar Doppler-compensation implementation | Primary Rev. 99 configuration-control context. Absence of PCR-700 from this memo is not independently proof that no intervening change affected it. |
| MIT/IL `R-567`, Section 2, *Data Links*, Revision 4, June 1969 | Revision-index cover explicitly names **LUMINARY 1A (Rev. 099)** and lists approved changes including PCR-670, PCR-700, PCN-765, and PCR-824 | Apollo 11-era primary effectivity/change-control evidence for Section 2. Change titles are not substitutes for technical pages. |
| MIT/IL `R-567`, Section 5, Revision 11, *Guidance Equations*, cumulative front matter | Preserves a historical revision-index sheet explicitly headed **Section 5 — Guidance Equations (Revision 4)**; visible first sheet includes PCR 636 (*November, 1968 GSOP Section 5 Corrections in Landing Program*) and other historical change identifiers | Primary-document recovery evidence for the existence/control history of Section 5 Revision 4. Does **not** establish that Revision 4 was Apollo 11 flight-effective or permit back-projection of Revision 11 equations. Complete Rev. 4 index/page effectivity still required. |
| Luminary 99/1 assembly listing, *Assembly and Operation Information* | Identifies the program as **LUMINARY 1A** and states that implementation details are specified in `R-567, as amended` | Primary program-to-GSOP relationship. Does not identify the complete section-by-section R-567 revision set effective at flight. |
| LUMINARY 99 program listing / Virtual AGC transcription | Exposes `LAG/TAU` in erasable assignments and its use in lunar-landing guidance | Strong implementation corroboration from the surviving program listing; preserve transcription/provenance labeling and do not substitute it for missing controlled GSOP equation pages. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Identifies `69-FS-3` (May 1969) as its LUMINARY 1A predecessor | Bibliographic/change-control route to the missing programmed-guidance-equation document; later equations remain comparative only. |

## Landing-change crosswalk

The January SCB memo and June Section 2 control sheet overlap on two high-value identifiers:

- PCR-670 — *Simplification of Landing Programs*. Memo 7-69 assigns program action to Don Eyles, Section 5 GSOP action to Allan Klumpp, and Section 4 GSOP action to Walker Kupfer.
- PCR-700 — *Improve the Rate of Descent Mode (P66) Performance*. Memo 7-69 describes intended changes including an erasable click scale factor, once-per-second ROD equations/commands, once-per-second DSKY HDOT updating, and preservation of clicks at P66 entry. Research note 329 closes one important part of the implementation chain: Memo #73 shows the P66 lag-compensation mechanism implemented in Revision 80, and the Apollo 11 Mission G LUMINARY 99 erasable-load document carries `LAG/TAU = 0.413333`. The once-per-second proposal details are still not promoted without final implementation evidence.

Research note 330 narrows the missing GSOP target to **Section 5 Revision 4** by recovering its historical index sheet inside the later cumulative Section 5 artifact. This is a retrieval lead, not a completed effectivity chain.

Additional June control-sheet identifiers remain useful retrieval keys:

- PCN-765 — *New Propulsion System Constants*
- PCR-824 — Section 2 documentation/detail update

Memo 7-69 also records PCR-704 (LR antenna rotation), PCR-705 (LR lateral velocity on downlink), PCR-706 (LR antenna-position discrete), and PCR-723 (two-segment LR altitude/velocity weighting) as **disapproved** in the 28th SCB state. Treat that as a dated negative boundary only; later approval would require separate evidence.

## Retrieval priority

1. Complete `R-567` Section 5 **Revision 4** revision-index pair and establish its LUMINARY 1A Rev. 099 effectivity.
2. Revision 4 landing-program/P63-P66 affected pages establishing exact final P66 equations and any explicit computation/command/display cadence.
3. Identify the PCR/PCN and final disposition for the P64 attitude-oscillation correction that Memo 7-69 still described as pending.
4. Affected landing-radar/update, estimator/filter, and propulsion-constant pages.
5. `69-FS-3`, retained as the preferred complete programmed-guidance-equation source when recoverable.
6. Controlled comparison with later LUMINARY revisions only after unchanged-page/effectivity boundaries are explicit.

PCR-700's presence in Apollo 11 no longer needs broad retrieval effort; the remaining question is exact final equation/cadence behavior and any sourced controller-facing consequence.

## Sources

- https://www.ibiblio.org/apollo/Documents/Memo-SCB28_text.pdf
- https://www.ibiblio.org/apollo/Documents/LUM73.pdf
- https://www.ibiblio.org/apollo/Documents/LUM85_text.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-R-567-SEC5-REV11_text.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
