# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Latest research note: `resources/research/167_free_return_gda_test_acceptance_bound.md`

## Roadmap refinement

The maneuver-label ambiguity is resolved sufficiently for research purposes. In LM CONTROL's contingency narrative, `MCC-3` is the 61:29 free-return DPS burn; mission-summary/trajectory sections call the same contingency maneuver MCC-4 while retaining the omitted pre-accident maneuver as MCC-3.

The historical chain has direct evidence that the GDA state was accepted before the 61:29 burn and then changed/complied under 40% powered flight. CONTROL later expected that resulting state to be optimum for PC+2.

Research note 167 adds a numerical bound to the **pre-burn checkout only**: during the 61:29 gimbal/throttle test, CONTROL judged the observed trim "within about 0.3" and "plenty close." Do not promote this into a formal RTCC or PC+2 trim-update tolerance. A separate immediate post-burn `0.2` guidance exchange is likewise not classified as a GDA residual absent explicit primary evidence.

## Highest-priority unresolved artifact

Find the controller-side numerical comparison that validated retaining the post-61:29 complied state for PC+2:

1. post-61:29 reference GDA angles;
2. PC+2 candidate trim angles;
3. comparison delta and decision tolerance/criterion;
4. calculation time and RTCC/RTACF job/run identity;
5. direct link to the T+55 LM-burn mass-property deck family.

Use the recovered `~0.3°` checkout acceptance only as a discriminator when classifying future evidence: hardware/gimbal checkout and mass-properties trim prediction remain separate provenance layers. Do not reconstruct missing numerical values from the earlier commanded pair, the checkout discrepancy, or PC+2 ignition motion.