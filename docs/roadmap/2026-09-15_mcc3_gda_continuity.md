# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Research note: `resources/research/166_mcc3_nomenclature_and_gda_state_continuity.md`

## Roadmap refinement

The maneuver-label ambiguity is resolved sufficiently for research purposes. In LM CONTROL's contingency narrative, `MCC-3` is the 61:29 free-return DPS burn; mission-summary/trajectory sections call the same contingency maneuver MCC-4 while retaining the omitted pre-accident maneuver as MCC-3.

The historical chain now has direct evidence that the GDA state was accepted before the 61:29 burn and then changed/complied under 40% powered flight. CONTROL later expected that resulting state to be optimum for PC+2.

## Highest-priority unresolved artifact

Find the controller-side numerical comparison that validated retaining the post-61:29 complied state for PC+2:

1. post-61:29 reference GDA angles;
2. PC+2 candidate trim angles;
3. comparison delta and decision tolerance/criterion;
4. calculation time and RTCC/RTACF job/run identity;
5. direct link to the T+55 LM-burn mass-property deck family.

Do not reconstruct missing numerical values from the earlier commanded pair or from PC+2 ignition motion.