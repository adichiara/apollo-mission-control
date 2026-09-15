# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Latest research note: `resources/research/169_post_mcc3_pc2_gda_as_is_readback.md`

## Roadmap refinement

The maneuver-label ambiguity is resolved sufficiently for research purposes. In LM CONTROL's contingency narrative, `MCC-3` is the 61:29 free-return DPS burn; mission-summary/trajectory sections call the same contingency maneuver MCC-4 while retaining the omitted pre-accident maneuver as MCC-3.

The historical chain has direct evidence that the GDA state was accepted before the 61:29 burn and that powered-flight compliance occurred. CONTROL later expected the state left by that maneuver to be optimum for PC+2.

Research note 167 adds a numerical bound to the **pre-burn checkout only**: during the 61:29 gimbal/throttle test, CONTROL judged the observed trim "within about 0.3" and "plenty close." Do not promote this into a formal RTCC or PC+2 trim-update tolerance. A separate immediate post-burn `0.2` guidance exchange is likewise not classified as a GDA residual absent explicit primary evidence.

Research note 168 recovers one approximate component of the **immediately pre-PC+2 execution state**. CONTROL reports the roll GDA moving to about `-2°` at ignition by `-1.2°`; arithmetic therefore constrains its pre-ignition roll position to approximately `-0.8°`. This is a derived approximate value, not a separately reported controller number.

Research note 169 adds a distinct **post-MCC-3 intended/retained reference readback**. In the NASA mission commentary after the 61:29 burn, the crew reads back that the PC+2 GDA should be "okay as is," "hopefully" pitch `5.85` and second axis `6.74` (transcribed as "Yaw"). Do not equate this pad/reference pair with measured actuator position; the primary wording itself is qualified and no controller artifact yet bridges it to the later ignition-state observation.

## Highest-priority unresolved artifact

Find the controller-side numerical comparison that validated no new PC+2 trim load:

1. PC+2 candidate trim angles from the applicable mass-properties calculation;
2. the reference values actually used in that comparison;
3. comparison delta and decision tolerance/criterion;
4. calculation time and RTCC/RTACF job/run identity;
5. direct link to the T+55 LM-burn mass-property deck family;
6. if available, telemetry/working-sheet evidence reconciling the `5.85 / 6.74` retained-reference readback with actual GDA actuator position.

Use the recovered `~0.3°` checkout acceptance only as a discriminator when classifying future evidence: hardware/gimbal checkout and mass-properties trim prediction remain separate provenance layers. Treat `5.85 / 6.74` as a post-MCC-3 PC+2 reference readback and `~-0.8°` roll as an approximate execution-state derivation; do not force them into one state without primary evidence.