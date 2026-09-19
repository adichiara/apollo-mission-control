# Progress — Apollo 11 P66 / PCR-700 implementation

Date: 2026-09-19
Research: 400–404

## Completed

- MIT implementation evidence establishes PCR-700 ancestry: Memo #67 records PCR-700/PCR-670 implemented in Revision 72; Memo #73 records later P66 total-lag compensation in Revision 80 and `LAG/TAU`.
- Apollo 11 Mission G LUMINARY 99 prelaunch data carry `LAG/TAU = 0.413333`.
- The recovered R-567 Section 5 Revision 5 index lists PCR-670 and PCR-700A; later 1B/1C equations remain comparison evidence.
- LUMINARY 099 final-program evidence shows `P66VERTA` scheduling `RODTASK` with `1SEC`; `RODTASK` dispatches `RODCOMP`, which updates `VDGVERT`/`HDOTDISP` and uses `LAG/TAU`.
- Apollo Project Memo 9-69 explicitly identifies PCR-700A as a clarifying rewrite of PCR-700.
- The D-024 closure challenge targeted the remaining equation/effectivity gap. MSC `69-FS-4` states that it is a complete re-issue of May 1969 `69-FS-3`, *Programmed Guidance Equations for LUMINARY 1A*, updated for LUMINARY 1B. This confirms the missing source's provenance but does not establish safe 1B→1A equation back-projection.

## Closure

The bounded P66/PCR-700 question is **SUFFICIENT for current implementation**. Exact Section 5 Revision 5 P63–P66 descriptive-page ancestry/effectivity and direct `69-FS-3` contents remain unresolved but are **DEFERRED**: no current player-visible, station-visible, causal-model, or validation behavior depends on those descriptive pages.

Crew-visible Noun 63 timing and station-visible timing remain separate deferred questions until a named feature requires them.

## Model effect

No executable behavior, DSKY behavior, controller product, station projection, or station maturity changes. The historical cadence and change-control crosswalk remain available if a future model dependency requires them.

## Reopen triggers

Reopen on direct recovery of `69-FS-3` or Apollo-11-effective Section 5 pages, contradictory mission-specific primary evidence, implementation requiring exact P63–P66 descriptive equations, a crew-display timing dependency, or a controller-product timing dependency. Otherwise move to the next OPEN roadmap item.