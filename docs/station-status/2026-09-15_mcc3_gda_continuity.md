# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/167_free_return_gda_test_acceptance_bound.md`

## CONTROL

**Improved.** CONTROL's `MCC-3` label is reconciled to its own contingency sequence: it denotes the 61:29 free-return DPS burn. Its later PC+2 rationale therefore points specifically to the GDA state produced by that burn's 40% compliance.

The primary controller loop now also gives a numerical pre-burn checkout observation: CONTROL called the gimbal trim GO and said the observed result was "within about 0.3" and "plenty close." This constrains the 61:29 checkout but is not evidence for the later PC+2 mass-properties comparison tolerance.

Still unresolved: numerical post-burn GDA state and the calculation/comparison used to judge it optimum for PC+2.

## FLIGHT / CAPCOM

**Improved.** Primary voice evidence before the 61:29 burn records CAPCOM's explicit disposition that the GDA settings were "go as they are." FLIGHT's immediate checkout questioning also establishes that controller acceptance involved an explicit closeness check rather than an unexamined state carryover.

## GUIDANCE

**Boundary added.** Immediately after the 61:29 burn, the controller loop contains a `0.2` trim exchange. Because the record does not identify this as GDA angle trim, do not use it as the post-burn GDA state or as a PC+2 trim criterion without additional primary evidence.

## Flight Dynamics / RTCC

**Unchanged unresolved priority.** Need candidate/reference values, comparison criterion, run/job identity, and direct T+55 deck linkage. The recovered `~0.3°` checkout observation must not be substituted for this missing criterion.

## Simulator constraint

Represent the 61:29 burn as a state-changing powered-flight compliance event in the provenance chain. Keep commanded trim, checkout agreement, powered-flight complied state, and later mass-properties candidate trim as distinct model concepts unless primary evidence explicitly equates them.