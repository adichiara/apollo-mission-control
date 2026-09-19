# Roadmap addendum — Apollo 11 P66 / PCR-700

Date: 2026-09-19
Parent: `docs/ROADMAP.md`
Research: 329–332

The active D-024 Apollo 11 powered-descent item is narrowed again. PCR-700 implementation itself is no longer an unresolved gate. Program revision records establish PCR-700/PCR-670 implementation ancestry, and the Apollo 11 Mission G LUMINARY 99 erasable-load document carries the resulting `LAG/TAU` parameter.

Research 331 recovered the next Section 5 control state: the historical **Guidance Equations (Revision 5)** index lists PCR-670 and PCR-700A without the sheet's later-revision dagger marks. Revision 5 is the earliest directly recovered Section 5 state in the inspected chain containing them, but its Apollo 11 effectivity and affected equation pages remain open.

Research 332 establishes the later-document boundary. MSC `69-FS-4` preserves detailed P66 programmed-equation definitions for LUMINARY 1B, but R-567 Revision 8 explicitly records later P66-specific changes (PCR-988 Auto P66 and PCR-1013 Multiple Servicers Avoidance in P66). Revision 8 also republishes some unchanged pages for convenience. Later 1B/1C material is therefore a comparison endpoint only, not an Apollo 11 substitute, unless page-level unchanged ancestry is demonstrated.

## Revised next work

1. Recover R-567 **Section 5 Revision 5 P63-P66 affected pages** and their page/change markings.
2. Establish LUMINARY 1A Rev. 099/Apollo 11 effectivity directly, or construct a controlled unchanged-page ancestry into an explicitly effective state.
3. Use `69-FS-4` and later R-567 pages only as comparison endpoints while reconstructing ancestry; explicitly screen out later P66 changes such as PCR-988/PCR-1013.
4. Seek a primary PCR-700/PCR-700A crosswalk; do not promote the secondary catalog's “rewritten clarification” description into technical equivalence.
5. Keep the January 1969 SCB once-per-second details classified as proposal/change-intent until final implementation evidence confirms them.
6. Recover `69-FS-3` in parallel as the preferred complete LUMINARY 1A programmed-guidance-equation source.
7. Only after the equation/effectivity chain closes, evaluate whether any new numerical dependency belongs in `apollo11_g_descent_partial` and whether a site-facing causal proof should change.

No executable behavior changes from the later-equation comparison finding alone.