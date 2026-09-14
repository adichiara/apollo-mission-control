# Progress — PC+2 DPS performance boundary

Date: 2026-09-14

## Completed

- Continued the numerical-validation queue after closing the RTCC mass-property lineage boundary in research note 138.
- Recovered mission-specific Apollo 13 DPS constraints for the PC+2 burn:
  - Flight Dynamics actual duration `263.82 s`;
  - staged minimum/40-percent/maximum-thrust command profile;
  - terminal regulator isolation and blowdown;
  - Apollo 13 vehicle-baseline nominal full thrust `9870 lbf`.
- Separated those mission-specific facts from general DPS design values such as `10,500 lbf` maximum rated thrust and `305 s` design specific impulse.
- Recorded startup transient behavior as an explicit historical-model boundary because Apollo 13 high-speed data showed thrust buildup timing could matter operationally.

## Consequence

The current Level-1 piecewise-constant-thrust / constant-Isp engine remains a valid synthetic model proof, but it is not yet a historically validated PC+2 propulsion model.

The next historical propulsion implementation must be able to admit start transient and blowdown behavior or an equivalent source-backed thrust history. No unsupported transient curve or Isp has been added.

## Next

Search for LM-7/Apollo 13-specific postflight DPS performance or acceptance/calibration data. In parallel, retain the unresolved RTCC T+55 mass/depletion convention as a separate validation gap.
