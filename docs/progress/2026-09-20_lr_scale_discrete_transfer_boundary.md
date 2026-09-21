# Progress — LR scale-discrete and transfer boundary

Date: 2026-09-20

## Completed

Primary-source review added an independent hardware/interface boundary around the unresolved Apollo 11 LR scale question.

AC Electronics ND-1021042 documents an LR-originated `Range low scale factor` discrete issued automatically at approximately 2,500 ft, plus digital LR data pulses and LGC readout/strobe/reset control. The LM-6 Apollo Operations Handbook, immediately post-Apollo-11 in configuration chronology, preserves the same automatic ~2,500-ft transition and documents conversion/counting into a 15-bit serial LGC transfer path.

This establishes strong continuity for the physical scale-state interface represented by LUMINARY 099 `ALTSCBIT`. It does not justify promoting the Luminary 1B 5.3950-ft/count value to a direct LM-5 hardware fact.

## Documentation synchronized

- `resources/research/503_lr_scale_discrete_and_serial_transfer_evidence.md`
- `docs/roadmap/2026-09-20_apollo11_lr_scale_selection.md`
- `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`
- `resources/APOLLO11_LR_SCALE_SELECTION_SOURCE_CATALOG_ADDENDUM.md`

## Remaining discriminating targets

1. LM-5/Luminary-1A-effective high-scale altitude bit weight.
2. Apollo 11 `SKALSKAL = 00000` prelaunch-load/run-time relationship.
3. LM-5 raw serial sign/bias/framing and rounding/truncation.
4. MCC/GUIDO visibility or procedural consequences of LR scale state.

Historical stochastic LR generation remains **BLOCKED**.