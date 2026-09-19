# Roadmap addendum — Apollo 11 P66 / PCR-700

Date: 2026-09-19
Parent: `docs/ROADMAP.md`
Research: 329–333

The active D-024 Apollo 11 powered-descent item is narrowed again. PCR-700 implementation itself is no longer an unresolved gate. Program revision records establish PCR-700/PCR-670 implementation ancestry, and the Apollo 11 Mission G LUMINARY 99 erasable-load document carries the resulting `LAG/TAU` parameter.

Research 331 recovered the historical **Guidance Equations (Revision 5)** index listing PCR-670 and PCR-700A. Research 332 established that later LUMINARY 1B/1C equation material is comparison evidence only unless unchanged ancestry is demonstrated.

Research 333 now closes a narrower implementation question directly from the LUMINARY 099 assembly listing: `P66VERTA` schedules `RODTASK` with the constant `1SEC`; `RODTASK` dispatches `RODCOMP`, which updates `VDGVERT`, updates `HDOTDISP`, and consumes `LAG/TAU` in the P66 computation. The Apollo 11 P66 ROD computation task therefore runs on a one-second schedule. This does not establish DSKY, telemetry, MCC, or other player-visible refresh cadence.

## Revised next work

1. Treat the **one-second P66 ROD computation cadence as documented**; do not continue searching merely to reconfirm it.
2. Recover R-567 Section 5 Revision 5 P63-P66 affected pages only to resolve descriptive equation/page ancestry or another named implementation dependency.
3. Recover `69-FS-3` in parallel as the preferred complete LUMINARY 1A programmed-guidance-equation source, but no longer as a prerequisite for the ROD computation interval.
4. Seek a primary PCR-700/PCR-700A crosswalk; do not promote the secondary catalog's “rewritten clarification” description into technical equivalence.
5. If crew-visible Noun 63 timing becomes implementation-relevant, research the display-service path separately; `HDOTDISP` update inside `RODCOMP` does not establish DSKY refresh timing.
6. If a station-visible dependency is named, establish the downlink/display chain separately before changing GUIDO/CONTROL/FLIGHT products.
7. Only add numerical dependencies to `apollo11_g_descent_partial` or change a site-facing causal proof when the recovered behavior materially affects a player-visible or model-visible product.

No station maturity or controller-facing cadence changes from research 333.