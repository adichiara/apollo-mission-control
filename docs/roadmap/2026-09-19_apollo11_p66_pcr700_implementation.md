# Roadmap addendum — Apollo 11 P66 / PCR-700

Date: 2026-09-19
Parent: `docs/ROADMAP.md`
Research: 329–331

The active D-024 Apollo 11 powered-descent item is narrowed again. PCR-700 implementation itself is no longer an unresolved gate: MIT LUMINARY Memo #73 establishes implementation in Revision 80, and the Apollo 11 Mission G LUMINARY 99 erasable-load document carries the resulting `LAG/TAU` parameter.

Research 330 recovered a historical R-567 Section 5 **Guidance Equations (Revision 4)** control state and its later cumulative annotations. Research 331 adds a necessary section-effectivity correction: the surviving Section 5 Revision 8 front matter groups the recovered 254.2–755 change inventory, including PCR 636, under **Incorporated in Rev. 4 of GSOP**, but PCR-670 and PCR-700 are absent from that inventory. By contrast, Section 2 Revision 4 explicitly names LUMINARY 1A Rev. 099 and lists both changes. Revision numbers therefore cannot be assumed synchronized across R-567 sections.

## Revised next work

1. Identify the R-567 **Section 5 revision/change state that first documents PCR-670 and/or PCR-700**, rather than presuming Section 5 Revision 4 is the final Apollo 11 equation set.
2. Tie the resulting P63-P66 page state to LUMINARY 1A Rev. 099 before using equations or cadence statements.
3. Reconcile Revision 8 and Revision 11 cumulative front-matter annotations so later additions are not projected backward.
4. Keep the January 1969 SCB once-per-second details classified as proposal/change-intent until final implementation evidence confirms them.
5. Recover `69-FS-3` in parallel as the preferred complete LUMINARY 1A programmed-guidance-equation source.
6. Only after the equation/effectivity chain closes, evaluate whether any new numerical dependency belongs in `apollo11_g_descent_partial` and whether a site-facing causal proof should change.

Section 5 Revision 4 remains a useful historical anchor, but is no longer the presumed final Apollo 11 technical target.