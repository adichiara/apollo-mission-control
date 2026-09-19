# Station-status addendum — Apollo 11 P66 / PCR-700

Date: 2026-09-19
Research: 329–333

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent reference.

## Supported vehicle/guidance facts

Apollo 11 LUMINARY 99 carried the PCR-700 P66 lag-compensation lineage: MIT implementation records identify the program changes, and the Mission G prelaunch erasable load supplies `LAG/TAU = 0.413333`.

Research 333 adds direct final-program timing evidence. In the LUMINARY 099 assembly listing, `P66VERTA` schedules `RODTASK` using `1SEC`; `RODTASK` dispatches `RODCOMP`. `RODCOMP` updates `VDGVERT` and `HDOTDISP` and consumes `LAG/TAU`. The P66 rate-of-descent computation task is therefore documented on a one-second schedule.

## Station-facing boundary

This does not establish a one-second station or crew display cadence. The listing demonstrates an internal guidance-task schedule and variable update. It does not by itself establish the timing of Noun 63 DSKY servicing, LM downlink sampling/transmission, MCC display processing, or any controller-facing product.

Accordingly:

- no station maturity grade changes;
- no controller display field is added;
- no player-visible cadence is frozen;
- no executable station projection changes.

The previous unresolved item “exact Apollo 11 P66 computation cadence” is closed. Any future station-relevant question must name a separate dependency in the chain from LGC state through downlink/ground processing to a sourced controller-visible product. Later LUMINARY 1B/1C material remains comparison evidence unless unchanged ancestry is demonstrated.