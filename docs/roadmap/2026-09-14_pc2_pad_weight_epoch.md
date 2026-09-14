# PC+2 numerical-validation roadmap — pad-weight epoch

Date: 2026-09-14
Research note: `resources/research/137_pc2_pad_weight_epoch_boundary.md`

## Resolved this pass

Research-note-130 target 5 is narrowed substantially. The final Apollo 13 PC+2 P30 LM maneuver PAD explicitly carried `62480 lb` CSM and `33452 lb` LM at GET 077:55:24 for TIG 079:27:38.30, and the pair survived crew readback/ground confirmation.

These values are now safe to use as **historical final-PAD / targeting regression inputs**.

## Boundary retained

The reviewed transcript does not define the pair as exact physical ignition mass or expose the RTCC mass-accounting convention. The causal model must therefore keep PAD/targeting mass reference distinct from hidden physical mass until a computation/weight-accounting source closes that gap.

## Next unresolved numerical inputs

Priority order remains:

1. recover the RTCC/Flight Dynamics weight convention and epoch for the docked PC+2 P30 solution;
2. recover Apollo 13/LM-7 DPS thrust/throttle and propellant-performance material suitable for numerical validation;
3. extract original LMS/FMES equations/integration assumptions beyond the current public handbook boundary;
4. recover sufficient state-vector/trajectory information for postburn propagation and regression.

## Integration rule

Do not force a numerical DPS model to reproduce `861.5 ft/s` by assuming `95932 lb` is exact ignition mass. Treat exact agreement as a validation target only after the weight epoch, thrust convention, propellant consumption, and integration assumptions are source-bounded.