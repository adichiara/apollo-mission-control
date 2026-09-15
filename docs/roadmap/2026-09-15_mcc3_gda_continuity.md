# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Latest research note: `resources/research/168_pc2_preignition_roll_gda_bound.md`

## Roadmap refinement

The maneuver-label ambiguity is resolved sufficiently for research purposes. In LM CONTROL's contingency narrative, `MCC-3` is the 61:29 free-return DPS burn; mission-summary/trajectory sections call the same contingency maneuver MCC-4 while retaining the omitted pre-accident maneuver as MCC-3.

The historical chain has direct evidence that the GDA state was accepted before the 61:29 burn and then changed/complied under 40% powered flight. CONTROL later expected that resulting state to be optimum for PC+2.

Research note 167 adds a numerical bound to the **pre-burn checkout only**: during the 61:29 gimbal/throttle test, CONTROL judged the observed trim "within about 0.3" and "plenty close." Do not promote this into a formal RTCC or PC+2 trim-update tolerance. A separate immediate post-burn `0.2` guidance exchange is likewise not classified as a GDA residual absent explicit primary evidence.

Research note 168 now recovers one approximate component of the **immediately pre-PC+2 retained state**. CONTROL reports the roll GDA moving to about `-2°` at ignition by `-1.2°`; arithmetic therefore constrains its pre-ignition roll position to approximately `-0.8°`. This is a derived approximate value, not a separately reported controller number, and it does not establish the exact state at 61:29 cutoff.

## Highest-priority unresolved artifact

Find the controller-side numerical comparison that validated retaining the complied state for PC+2:

1. retained/reference pitch GDA angle and any more precise roll evidence;
2. PC+2 candidate trim angles;
3. comparison delta and decision tolerance/criterion;
4. calculation time and RTCC/RTACF job/run identity;
5. direct link to the T+55 LM-burn mass-property deck family.

Use the recovered `~0.3°` checkout acceptance only as a discriminator when classifying future evidence: hardware/gimbal checkout and mass-properties trim prediction remain separate provenance layers. Treat `~-0.8°` roll as an approximate pre-ignition state derived from CONTROL's reported motion, not as the missing candidate trim or tolerance. Do not reconstruct the pitch axis or missing comparison from the earlier commanded pair.