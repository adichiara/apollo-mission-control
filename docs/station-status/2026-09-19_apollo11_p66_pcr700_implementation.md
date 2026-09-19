# Station-status addendum — Apollo 11 P66 / PCR-700

Date: 2026-09-19
Research: 400–404

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent reference.

## Supported vehicle/guidance facts

Apollo 11 LUMINARY 99 carried the PCR-700 P66 lag-compensation lineage. The Mission G prelaunch load supplies `LAG/TAU = 0.413333`; the LUMINARY 099 listing shows `P66VERTA` scheduling `RODTASK` with `1SEC`, with `RODTASK` dispatching `RODCOMP`; and Apollo Project Memo 9-69 identifies PCR-700A as a clarifying rewrite of PCR-700.

The closure challenge adds source provenance, not a station behavior: MSC `69-FS-4` explicitly says it completely re-issued May 1969 LUMINARY 1A `69-FS-3` and updated it for LUMINARY 1B.

## Station-facing boundary

None of these findings establishes a one-second station or crew display cadence. The listing demonstrates an internal guidance-task schedule and variable update, not Noun 63 DSKY servicing, LM downlink sampling/transmission, MCC display processing, or a controller-facing product. The 700/700A crosswalk establishes change-control ancestry, not Section 5 page effectivity. `69-FS-4` remains later comparison evidence unless unchanged ancestry is demonstrated.

Accordingly, no station maturity grade, controller display field, player-visible cadence, or executable station projection changes.

## Research state

The Apollo 11 P66/PCR-700 bounded question is **SUFFICIENT for current implementation**. Exact Section 5 descriptive-equation ancestry, direct `69-FS-3` contents, crew-visible Noun 63 timing, and station-visible timing are **DEFERRED** until a named implementation dependency requires them.

A future station-relevant question must establish the chain from LGC state through downlink/ground processing to a sourced controller-visible product before changing GUIDO/CONTROL/FLIGHT behavior.