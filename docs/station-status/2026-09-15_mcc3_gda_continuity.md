# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/169_post_mcc3_pc2_gda_as_is_readback.md`

## CONTROL

**Improved.** CONTROL's `MCC-3` label is reconciled to its own contingency sequence: it denotes the 61:29 free-return DPS burn. Its later PC+2 rationale therefore points specifically to the GDA state left by that burn's 40% compliance.

The primary controller loop gives a numerical pre-burn checkout observation: CONTROL called the gimbal trim GO and said the observed result was "within about 0.3" and "plenty close." This constrains the 61:29 checkout but is not evidence for the later PC+2 mass-properties comparison tolerance.

CONTROL's PC+2 execution narrative yields one approximate execution-state component: roll moved to about `-2°` at ignition by `-1.2°`, implying an immediately pre-ignition roll position of approximately `-0.8°`. This is derived arithmetic from approximate reported values, not an independently printed trim value.

Still unresolved: the controller/RTCC candidate-reference calculation and evidence reconciling pad/reference settings with actual actuator state.

## FLIGHT / CAPCOM

**Improved.** Primary voice evidence before the 61:29 burn records CAPCOM's explicit disposition that the GDA settings were "go as they are." A later NASA mission-commentary readback after the burn says the PC+2 GDA should be "okay as is," with the crew adding "hopefully" pitch `5.85` and second axis `6.74` (transcribed as "Yaw"). This supplies a two-axis intended/retained reference after MCC-3, but not measured GDA telemetry.

## GUIDANCE

**Boundary retained.** Immediately after the 61:29 burn, the controller loop contains a `0.2` trim exchange. Because the record does not identify this as GDA angle trim, do not use it as the post-burn GDA state or as a PC+2 trim criterion without additional primary evidence.

## Flight Dynamics / RTCC

**Unchanged unresolved priority, now narrower.** Need the PC+2 candidate trim, reference values used for comparison, comparison criterion, run/job identity, and direct T+55 deck linkage. The `5.85 / 6.74` post-MCC-3 readback gives a reference candidate for archival discrimination but does not prove that those were the values used in the RTCC comparison. Neither the `~0.3°` checkout observation nor the `0.01°` difference from the earlier `5.86 / 6.75` pair may be promoted into a PC+2 tolerance.

## Simulator constraint

Keep commanded/pad trim, checkout agreement, powered-flight complied state, retained-reference readback, actual actuator state, and later mass-properties candidate trim as distinct model concepts unless primary evidence explicitly equates them. `5.85 / 6.74` may be represented only as the source-backed post-MCC-3 PC+2 "as is" reference/readback; `~-0.8°` roll remains approximate execution-state arithmetic from CONTROL's ignition-motion report.