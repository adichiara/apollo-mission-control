# Roadmap addendum — Apollo 11 P66 / PCR-700

Date: 2026-09-19
Parent: `docs/ROADMAP.md`
Research: 329

The active D-024 Apollo 11 powered-descent item is narrowed again. PCR-700 implementation itself is no longer an unresolved gate: MIT LUMINARY Memo #73 establishes implementation in Revision 80, and the Apollo 11 Mission G LUMINARY 99 erasable-load document carries the resulting `LAG/TAU` parameter.

## Revised next work

1. Recover the LUMINARY 1A Rev. 099-effective R-567 Section 5 control/revision pages.
2. Inspect the final P63-P66 technical pages for the exact P66 equation form and any explicit computation/command/display cadence.
3. Keep the January 1969 SCB once-per-second details classified as proposal/change-intent until final implementation evidence confirms them.
4. Recover `69-FS-3` in parallel as the preferred complete LUMINARY 1A programmed-guidance-equation source.
5. Only after the equation/effectivity chain closes, evaluate whether any new numerical dependency belongs in `apollo11_g_descent_partial` and whether a site-facing causal proof should change.

Do not spend further research effort merely proving that PCR-700 reached Apollo 11; that question is sufficiently closed for current architecture work.
