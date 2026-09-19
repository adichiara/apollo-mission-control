# Roadmap addendum — Apollo 11 R-567 Luminary 1A control

Date: 2026-09-18  
Parent: `docs/ROADMAP.md`

## Newly resolved

A directly readable primary GSOP control sheet supplies an Apollo 11-specific source path that does not depend on recovering MSC Internal Note `69-FS-3` first.

`R-567`, Section 2, **Data Links (Revision 4)** identifies itself as applying to **LUMINARY 1A (Rev. 099)** and is dated **June 1969**. Its revision index records approved changes including PCR-670, *Simplification of Landing Programs*; PCR-700, *Improve the Rate of Descent Mode (P66) Performance*; PCN-765, *New Propulsion System Constants*; and PCR-824, a Section 2 documentation update.

The surviving Luminary 99/1 assembly listing independently states that the LGC program is LUMINARY 1A and that implementation details are specified in `R-567, as amended`.

## Roadmap consequence

Keep `69-FS-3` as the preferred programmed-guidance-equation target, but add **mission-effective R-567 LUMINARY 1A revisions/change pages** as a parallel primary-source route. Prioritize recovery of Apollo 11-effective Section 5 guidance-equation pages and their revision/change control before borrowing equations from Luminary 1B/1C.

The June 1969 Section 2 control sheet may establish change identity/effectivity and data-link behavior, but it does **not** by itself supply the underlying landing-guidance equations or prove the technical content of the listed PCR/PCN changes.

## Next bounded retrieval

1. Locate the R-567 Section 5 revision/change state effective for LUMINARY 1A Rev. 099.
2. Recover the control/revision pages first.
3. Compare powered-descent, landing-radar/update, estimator/filter, P63–P66, and propulsion-constant pages against later revisions only where change control supports the comparison.
4. Do not back-project later R-567 Rev. 8 / LUMINARY 1C equations into Apollo 11.

## Primary sources

- `R-567`, Section 2, Data Links (Rev. 4), June 1969, LUMINARY 1A (Rev. 099): https://ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- Luminary 99/1 assembly listing, Assembly and Operation Information: https://www.ibiblio.org/apollo/listings/Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc.html
