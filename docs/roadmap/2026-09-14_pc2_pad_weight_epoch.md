# PC+2 numerical-validation roadmap — pad-weight epoch

Date: 2026-09-14
Research notes: `resources/research/137_pc2_pad_weight_epoch_boundary.md`, `resources/research/138_pc2_rtcc_mass_property_deck_boundary.md`, `resources/research/139_pc2_dps_performance_boundary.md`

## Resolved this pass

Research-note-130 target 5 is narrowed substantially. The final Apollo 13 PC+2 P30 LM maneuver PAD explicitly carried `62480 lb` CSM and `33452 lb` LM at GET 077:55:24 for TIG 079:27:38.30, and the pair survived crew readback/ground confirmation.

The Flight Control Division Mission Operations Report further establishes that:

- RTCC **LM-burn mass-property decks were updated to T+55 decks** before the abort maneuver work; and
- a PC+2 DPS trim disagreement was resolved because LM Control had used **premission mass properties**, which were not the best data then available.

These values are therefore safe to use as **historical final-PAD / targeting regression inputs with an in-flight updated RTCC mass-properties lineage**.

## Boundary retained

Neither reviewed source defines the `62480 + 33452 = 95932 lb` pair as exact physical ignition mass or exposes the RTCC mass-accounting/propagation convention. The causal model must therefore keep PAD/targeting mass reference distinct from hidden physical mass.

## Propulsion boundary now partially resolved

Research note 139 establishes mission-specific PC+2 burn duration, staged throttle-command behavior, terminal blowdown, and the Apollo 13 configuration's nominal full-thrust value. It also shows why an instantaneous piecewise-constant-thrust history is not yet a historical reconstruction: startup buildup was operationally material, and the final portion of PC+2 was a distinct blowdown condition.

General DPS design values remain separate from LM-7 PC+2 calibration. In particular, the Apollo 13 `9870 lbf` nominal full-thrust baseline must not be silently equated with the general design report's `10,500 lbf` maximum rated thrust, and the design `305 s` specific impulse is not yet frozen as the PC+2 effective Isp.

## Next unresolved numerical inputs

Priority order is now:

1. recover Apollo 13/LM-7-specific DPS thrust, mass-flow, Isp, startup, and blowdown performance data suitable for numerical validation;
2. recover the Apollo RTCC mass-properties/T+55 deck semantics and how that deck fed the docked PC+2 DPS solution;
3. extract original LMS/FMES equations/integration assumptions beyond the current public handbook boundary;
4. recover sufficient state-vector/trajectory information for postburn propagation and regression.

## Integration rule

Do not force a numerical DPS model to reproduce `861.5 ft/s` by assuming `95932 lb` is exact ignition mass. Treat exact agreement as a validation target only after the mass convention, delivered-thrust / mass-flow history (including transient and blowdown treatment), propellant consumption, and integration assumptions are source-bounded.
