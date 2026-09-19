# Research note 501 — Apollo 11 landing-radar composed estimator boundary

Date: 2026-09-19  
Research thread: `apollo11-landing-radar`

## Bounded question

Can the source-controlled Apollo 11 landing-radar velocity stages now be composed into one executable causal proof without inventing the remaining LM-5 measurement geometry or stochastic behavior?

## Primary-source check

The flown LUMINARY 099 listing keeps the geometry and estimator stages distinct. `SETPOS` loads `LRALPHA/LRBETA`, places the rotations in the AGC CDU-angle convention, transforms antenna `UNITY` and `UNITX` into navigation-base `VYBEAMNB` and `VXBEAMNB`, and forms `VZBEAMNB` by cross product. LUMINARY Memo #95 states that the LGC angles are antenna-to-navigation-base rotations, with beta then alpha, and are the negatives of the R-567 angles.

At velocity-update time, `RDGIMS` has already saved the measurement-time CDUs/PIPAs/time. `VELUPDAT` restores those CDUs, runs `QUICTRIG`, transforms the selected navigation-base velocity beam through `*NBSM*`, propagates the prior guidance velocity to `LRVTIME`, subtracts lunar-surface rotation, projects the estimate on that measurement-time beam, tests the measured-minus-reference residual, and passes accepted data to the weighting/update path.

`POWERED_FLIGHT_SUBROUTINES.agc` explicitly defines `TRG*NBSM` / `*NBSM*` as navigation-base-to-stable-member transforms using CDU angles in Y-Z-X order. This is enough to control the stage ordering and interfaces, but the repository does not yet contain an independently verified executable port of the AGC `AX*SR*T` rotation machinery.

The LM-5 prelaunch erasable load supplies the flown orientation values: `LRALPHA1=0.0163371759 rev`, `LRBETA1=0.0665287037 rev`, `LRALPHA2=0.0161680555 rev`, and `LRBETA2=0.0001361111 rev`. These values remain source data; this note does not turn an unverified modern rotation convention into historical code.

## Implementation decision

The next safe executable increment is therefore composition **from an explicit measurement-time selected beam**:

`prior guidance velocity + PIPA ΔV + previous-gravity Δt -> measurement-time velocity -> subtract lunar-surface velocity -> project on supplied measurement-time beam -> residual qualification -> historical weighting/correction`

This closes the executable composition of the estimator arithmetic while preserving the beam transform as a visible upstream dependency. It does not synthesize antenna/CDU geometry, radar measurements, radar noise, PIPA behavior, or a gravity field.

## Repository consequence

`landing_radar_velocity_chain.py` composes the existing propagation, reference projection, quality, and weighting/correction modules. Its result explicitly reports that the measurement-time beam is caller supplied. Tests prove accepted and rejected residual paths and Data Good persistence behavior.

This is a model-proof boundary, not a claim that the intermediate values were available on a Mission Control display.

## Remaining boundary

1. Implement and independently verify the Apollo-11-effective `SETPOS` antenna-to-NB and measurement-time `*NBSM*` transforms before a historical profile may synthesize the beam.
2. Keep historical stochastic LR measurement generation **BLOCKED** until a flight-effective numerical error model is recovered.
3. Keep controller-visible cadence/formatting separate pending Mission G downlink/ground/display evidence.

## Sources

- MIT/IL LUMINARY 099 final-program listing, `SERVICER.agc`, `SETPOS`, `RDGIMS`, `VELUPDAT`: https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- MIT/IL LUMINARY 099, `POWERED_FLIGHT_SUBROUTINES.agc`, `TRG*NBSM`, `*NBSM*`, `AX*SR*T`: https://www.ibiblio.org/apollo/listings/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc.html
- MIT/IL LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969: https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- Grumman/NASA, `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load: https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf

## Evidence status

- **DOCUMENTED:** flown stage ordering from antenna/NB geometry through measurement-time beam transform, propagation, residual qualification, and weighting/correction.
- **DOCUMENTED:** LM-5 `LRALPHA/LRBETA` orientation values and antenna-to-NB polarity/order convention.
- **IMPLEMENTED:** composed propagation -> explicit-beam projection -> residual qualification -> weighted correction proof.
- **PARTIALLY IMPLEMENTED:** historical beam production; source logic is controlled but the AGC transform is not yet ported and independently verified.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical stochastic landing-radar measurement-error model.
- **UNRESOLVED:** Mission Control-visible cadence, latency, synchronization, and formatting.
