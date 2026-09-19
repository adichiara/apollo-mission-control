# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-19

## Completed

Closed the source logic for the Apollo-11-effective landing-radar measurement-time velocity estimate and downstream weighting/correction stage, and now composed those executable stages through residual qualification.

The flown LUMINARY 099 `RDGIMS` / `VELUPDAT` path constrains the propagation leg: during the five-sample LR velocity read, `RDGIMS` saves `LRVTIME`, IMU CDUs, and the PIPA snapshot; `VELUPDAT` forms the measurement-time estimate from prior guidance velocity, the saved PIPA-derived increment, and previous gravity contribution, then subtracts lunar-surface rotation before beam projection and residual testing. The same flown path plus the LM-5 Mission G prelaunch load constrain the downstream weighting/correction. Research note 500 records that controlled estimator chain.

A fresh primary-source check before composition confirmed the geometry interface rather than filling it by assumption. LUMINARY 099 `SETPOS` constructs the navigation-base velocity beams from antenna axes; Memo #95 fixes antenna-to-NB polarity/order; `VELUPDAT` restores measurement-time CDUs and applies `*NBSM*`; and `POWERED_FLIGHT_SUBROUTINES.agc` identifies `*NBSM*` as the NB-to-SM transform implemented through `AX*SR*T` with Y-Z-X CDU ordering.

## Implementation

The repository now contains:

- `landing_radar_propagation.py` — explicit-input measurement-time propagation;
- `landing_radar_reference.py` — surface-relative selected-beam projection;
- `landing_radar_velocity_update.py` — weighting/correction;
- `landing_radar_velocity_chain.py` — composed propagation → projection → residual qualification → weighting/correction proof;
- `landing_radar_profiles.py` — historical profile loader and Apollo 11 LM-5 weighting metadata;
- tests covering successful composition, reasonableness rejection, and Data Good persistence rejection.

The composed proof deliberately requires the measurement-time selected beam as an explicit input. It does not synthesize the LM-5 antenna/CDU transform, gravity field, PIPA behavior, radar measurement, or noise. This makes the current executable boundary narrower than the full source-controlled historical chain, but avoids substituting an unverified modern Euler convention for the AGC transform.

## Next implementation boundary

Implement and independently verify the Apollo-11-effective `SETPOS` antenna-to-navigation-base transform and the measurement-time `*NBSM*` transform, then replace the explicit-beam input in the historical proof with source-derived beam production. The LM-5 load values are already recovered; the remaining requirement is a verified executable port of the transform semantics.

Landing-radar measurement generation/error behavior remains **BLOCKED** on a flight-effective numerical error model. Controller-visible product cadence/formatting remains a separate unresolved evidence problem.
