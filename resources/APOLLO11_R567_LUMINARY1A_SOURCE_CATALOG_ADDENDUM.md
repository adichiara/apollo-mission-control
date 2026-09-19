# Apollo 11 / R-567 LUMINARY 1A source-catalog addendum

Date: 2026-09-18

## Controlled sources

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| MIT/IL Apollo Project Memo 7-69, George W. Cherry, *What is LUMINARY 1A? Some Results of the 28th Apollo Software Configuration Control Board Meeting*, 23 Jan 1969 | Identifies LUMINARY 1A as the Mission G program; records approved landing changes PCR 700 and PCR 670; gives proposed P66 changes and GSOP/program action assignments; records PCRs 704/705/706/723 as disapproved at that board state | Primary configuration-control intent. Strong crosswalk/retrieval evidence, but not by itself proof of final Rev. 099 implementation or flight behavior. |
| MIT/IL `R-567`, Section 2, *Data Links*, Revision 4, June 1969 | Revision-index cover explicitly names **LUMINARY 1A (Rev. 099)** and lists approved changes including PCR-670, PCR-700, PCN-765, and PCR-824 | Apollo 11-era primary effectivity/change-control evidence for Section 2. Change titles are not substitutes for technical pages. |
| Luminary 99/1 assembly listing, *Assembly and Operation Information* | Identifies the program as **LUMINARY 1A** and states that implementation details are specified in `R-567, as amended` | Primary program-to-GSOP relationship. Does not identify the complete section-by-section R-567 revision set effective at flight. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Identifies `69-FS-3` (May 1969) as its LUMINARY 1A predecessor | Bibliographic/change-control route to the missing programmed-guidance-equation document; later equations remain comparative only. |

## Landing-change crosswalk

The January SCB memo and June Section 2 control sheet overlap on two high-value identifiers:

- PCR-670 — *Simplification of Landing Programs*. Memo 7-69 assigns program action to Don Eyles, Section 5 GSOP action to Allan Klumpp, and Section 4 GSOP action to Walker Kupfer.
- PCR-700 — *Improve the Rate of Descent Mode (P66) Performance*. Memo 7-69 describes intended changes including an erasable click scale factor, once-per-second ROD equations/commands, once-per-second DSKY HDOT updating, and preservation of clicks at P66 entry. The June Section 2 Rev. 4 index confirms PCR-700 in the LUMINARY 1A Rev. 099 document state, but does not prove those implementation details remained unchanged through flight.

Additional June control-sheet identifiers remain useful retrieval keys:

- PCN-765 — *New Propulsion System Constants*
- PCR-824 — Section 2 documentation/detail update

Memo 7-69 also records PCR-704 (LR antenna rotation), PCR-705 (LR lateral velocity on downlink), PCR-706 (LR antenna-position discrete), and PCR-723 (two-segment LR altitude/velocity weighting) as **disapproved** in the 28th SCB state. Treat that as a dated negative boundary only; later approval would require separate evidence.

## Retrieval priority

1. `R-567` Section 5 **Guidance Equations** control/revision pages effective for LUMINARY 1A Rev. 099.
2. Section 5 landing-program/P63-P66 pages associated with PCR-670 and any controlled change pages establishing PCR-700's final implementation.
3. Identify the PCR/PCN and final disposition for the P64 attitude-oscillation correction that Memo 7-69 still described as pending.
4. Affected landing-radar/update, estimator/filter, and propulsion-constant pages.
5. `69-FS-3`, retained as the preferred complete programmed-guidance-equation source when recoverable.
6. Controlled comparison with later LUMINARY revisions only after effectivity/change boundaries are explicit.

## Sources

- https://www.ibiblio.org/apollo/Documents/Memo-SCB28_text.pdf
- https://ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc.html
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
