# Roadmap addendum — Apollo 11 P66 / PCR-700

Date: 2026-09-19
Parent: `docs/ROADMAP.md`
Research: 329–330

The active D-024 Apollo 11 powered-descent item is narrowed again. PCR-700 implementation itself is no longer an unresolved gate: MIT LUMINARY Memo #73 establishes implementation in Revision 80, and the Apollo 11 Mission G LUMINARY 99 erasable-load document carries the resulting `LAG/TAU` parameter.

Research 330 adds a document-control lead: the surviving R-567 Section 5 Revision 11 artifact preserves a historical revision-index sheet explicitly headed **Guidance Equations (Revision 4)**. Direct reinspection also establishes that the sheet is cumulative: its dagger legend identifies additional material added in Revision 7. PCR 636 is unmarked; dagger-marked rows must not be attributed to Revision 4 merely because they appear on that sheet. Combined with the June 1969 Section 2 Revision 4 sheet explicitly naming LUMINARY 1A Rev. 099, Section 5 Revision 4 remains the strongest current retrieval target, but it is not yet proven flight effectivity.

## Revised next work

1. Recover/inspect the complete R-567 Section 5 **Revision 4 revision-index pair**, preserving the Revision-7 later-addition markings when assigning change ancestry.
2. Recover the Revision 4 P63-P66 affected pages and establish their LUMINARY 1A Rev. 099 effectivity/page state before using equations.
3. Inspect final P63-P66 technical material for the exact P66 equation form and any explicit computation/command/display cadence.
4. Keep the January 1969 SCB once-per-second details classified as proposal/change-intent until final implementation evidence confirms them.
5. Recover `69-FS-3` in parallel as the preferred complete LUMINARY 1A programmed-guidance-equation source.
6. Only after the equation/effectivity chain closes, evaluate whether any new numerical dependency belongs in `apollo11_g_descent_partial` and whether a site-facing causal proof should change.

Do not back-project Revision 7/8/11 changes or equations merely because the later cumulative R-567 artifact preserves the Revision 4 index.