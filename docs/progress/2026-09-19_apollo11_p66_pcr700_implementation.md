# Progress — Apollo 11 P66 / PCR-700 implementation

Date: 2026-09-19
Research: 329–333

## Completed

- Direct MIT implementation evidence establishes PCR-700 ancestry in LUMINARY: Memo #67 records PCR-700 and PCR-670 implemented in Revision 72; Memo #73 records the later P66 total-lag compensation in Revision 80 and introduction of `LAG/TAU`.
- Apollo 11 mission/configuration evidence from `SNA-8-D-027(II) REV 1` shows the LM-5 Mission G LUMINARY 99 prelaunch load containing `LAG/TAU = 0.413333`.
- The surviving cumulative R-567 artifact preserves a Section 5 Revision 5 index listing PCR-670 and PCR-700A; later 1B/1C equation documents remain comparison evidence because later P66-specific changes are documented.
- Research 333 inspected the LUMINARY 099 assembly listing itself. In the P66 path, `P66VERTA` loads `1SEC`, calls `TWIDDLE`, and schedules `RODTASK`; `RODTASK` dispatches `RODCOMP`.
- `RODCOMP` updates `VDGVERT`, updates `HDOTDISP`, and uses `LAG/TAU` in the P66 computation. The Apollo 11 P66 ROD computation cadence is therefore directly documented as **one second**.
- MIT/IL Apollo Project Memo 9-69 now supplies the previously missing primary crosswalk: **PCR-700A, “Improve the Rate-of-Descent Mode (P66) Performance,” is explicitly described as a clarifying rewrite of PCR-700**, with the action already assigned. This reconciles the PCR-700 identifier in Apollo 11-effective Section 2 Revision 4 with PCR-700A in the recovered Section 5 Revision 5 control index without assuming a separate technical change.

## Boundary retained

The January SCB once-per-second **computation** detail is confirmed in the final LUMINARY 099 program path. Do not extend that conclusion to a one-second DSKY/Noun 63 refresh, telemetry cadence, MCC display cadence, or controller-facing product. `HDOTDISP` is updated in the one-second computation path, but display-service timing is a separate question.

The PCR-700/700A identity is now primary-source documented, but this does not establish that every Section 5 Revision 5 equation page is Apollo 11-effective. LUMINARY 1B/1C descriptive equations remain comparison evidence unless unchanged ancestry is demonstrated.

## Model effect

The cadence fact and change-control crosswalk are eligible as historical evidence if a future model dependency requires them. No current station projection or player-visible product depends on these facts, so no executable behavior, DSKY behavior, controller product, or station maturity changes in this step.

## Next

Stop treating exact P66 ROD computation cadence and the PCR-700/PCR-700A crosswalk as unresolved. Continue only the remaining bounded questions: Section 5 Revision 5 descriptive-equation ancestry/effectivity, `69-FS-3` retrieval, and any separately named crew- or station-visible timing dependency.