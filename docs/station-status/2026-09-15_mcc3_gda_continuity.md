# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/168_pc2_preignition_roll_gda_bound.md`

## CONTROL

**Improved.** CONTROL's `MCC-3` label is reconciled to its own contingency sequence: it denotes the 61:29 free-return DPS burn. Its later PC+2 rationale therefore points specifically to the GDA state produced by that burn's 40% compliance.

The primary controller loop also gives a numerical pre-burn checkout observation: CONTROL called the gimbal trim GO and said the observed result was "within about 0.3" and "plenty close." This constrains the 61:29 checkout but is not evidence for the later PC+2 mass-properties comparison tolerance.

CONTROL's PC+2 execution narrative now yields one approximate retained-state component: roll moved to about `-2°` at ignition by `-1.2°`, implying an immediately pre-ignition roll position of approximately `-0.8°`. This is derived arithmetic from approximate reported values, not an independently printed trim value.

Still unresolved: retained pitch GDA, exact post-61:29 cutoff state, and the calculation/comparison used to judge the retained state optimum for PC+2.

## FLIGHT / CAPCOM

**Improved.** Primary voice evidence before the 61:29 burn records CAPCOM's explicit disposition that the GDA settings were "go as they are." FLIGHT's immediate checkout questioning also establishes that controller acceptance involved an explicit closeness check rather than an unexamined state carryover.

## GUIDANCE

**Boundary retained.** Immediately after the 61:29 burn, the controller loop contains a `0.2` trim exchange. Because the record does not identify this as GDA angle trim, do not use it as the post-burn GDA state or as a PC+2 trim criterion without additional primary evidence.

## Flight Dynamics / RTCC

**Unchanged unresolved priority.** Need candidate/reference values, comparison criterion, run/job identity, and direct T+55 deck linkage. Neither the recovered `~0.3°` checkout observation nor the derived `~-0.8°` pre-ignition roll position supplies the missing mass-properties comparison criterion.

## Simulator constraint

Represent the 61:29 burn as a state-changing powered-flight compliance event in the provenance chain. Keep commanded trim, checkout agreement, powered-flight complied state, retained pre-ignition state, and later mass-properties candidate trim as distinct model concepts unless primary evidence explicitly equates them. If `~-0.8°` roll is used, label it as approximate and derived from CONTROL's ignition-motion report.