# Landing Radar Guidance-Update Gate Model Proof

Status: **implemented reusable propagation + velocity-reference + measurement-quality + eligibility + weighted velocity-correction proof; historical beam synthesis and sensor generation remain incomplete**

## Purpose

Represent the bounded chain:

`prior guidance state + explicit measurement-time inputs -> radar-axis reference -> measurement qualification -> update eligibility -> weighted velocity correction`

Files:

- `src/apollo_mission_control/landing_radar_propagation.py`
- `src/apollo_mission_control/landing_radar_reference.py`
- `src/apollo_mission_control/landing_radar_quality.py`
- `src/apollo_mission_control/landing_radar_model.py`
- `src/apollo_mission_control/landing_radar_velocity_update.py`
- `src/apollo_mission_control/landing_radar_velocity_chain.py`

## Why this boundary matters

Apollo 11 descent distinguishes radar Data Good, update enablement, measurement qualification, estimator admission, and state-vector correction. A scenario must not equate "radar good" with "state vector immediately becomes radar truth."

## Measurement-time propagation

`landing_radar_propagation.py` mirrors the source-controlled `VELUPDAT` arithmetic boundary using explicit caller inputs for prior guidance velocity, PIPA-derived delta-V, previous gravity, elapsed time, and lunar-surface velocity. It does not synthesize a gravity field, PIPA behavior, measurement, or noise.

## Velocity-reference layer

`landing_radar_reference.py` implements:

`measurement-time estimated velocity - lunar-surface velocity -> dot(selected measurement-time radar-beam unit vector)`

The selected beam is explicit and must be unit length. This matches the flown LUMINARY 099 stage ordering without pretending that the repository has already ported the complete LM-5 antenna/CDU transform.

Primary-source reinspection constrains that remaining transform: `SETPOS` constructs NB velocity beams from antenna axes; LUMINARY Memo #95 fixes antenna-to-NB polarity/order; `VELUPDAT` restores measurement-time CDUs and applies `*NBSM*`; `POWERED_FLIGHT_SUBROUTINES.agc` implements that transform through `AX*SR*T` with Y-Z-X CDU ordering. The source logic is controlled, but the executable port is not yet independently verified.

## Measurement-quality layer

`landing_radar_quality.py` represents Data Good persistence, optional range-scale stability, channel validity, and caller-supplied affine residual reasonableness tests. Raw qualification remains separate from permission to update guidance state.

## Downstream velocity weighting / correction

`landing_radar_velocity_update.py` applies a qualified scalar residual along the selected measurement-time beam using caller/profile-supplied weighting. The Apollo 11 profile supplies the LM-5 `LRVMAX`, `LRVF`, component weights, and P65/P66/P67 `LRWVFF` override recovered in research note 500.

`updated velocity = prior velocity + weight * scalar residual * selected beam`

## Composed proof

`landing_radar_velocity_chain.py` now composes:

`propagation -> surface-relative selected-beam projection -> residual qualification -> weighted correction`

The result preserves each intermediate stage and explicitly reports that the measurement-time beam is caller supplied. Tests cover accepted correction, reasonableness rejection, and Data Good persistence rejection.

This composition is historical in stage semantics only where the supplied inputs/profile are source-controlled. Synthetic test vectors remain synthetic.

## Deliberately deferred

- executable and independently verified LM-5 `SETPOS` antenna-to-NB + measurement-time `*NBSM*` beam synthesis;
- surface intersection/terrain measurement generation;
- flight-effective measurement noise/bias generation;
- complete antenna hardware state;
- controller display/downlink generation and cadence.

Historical stochastic LR measurement generation is **BLOCKED** pending numerical LM-5/Apollo-11-effective evidence.

## Apollo 11 applicability boundary

The Apollo 11 Mission Report documents landing-radar Data Good, update enablement, and the velocity-update start below the 2000 ft/s threshold. Apollo guidance documentation constrains the onboard update logic. None of that establishes an MCC display cadence or exposes onboard intermediate variables as controller telemetry.

## Validation

Synthetic tests verify propagation composition, surface-relative projection, strict unit-vector validation, quality rejection, piecewise weighting, program override, inhibit behavior, and vector correction. The composed proof does not authorize an `apollo11_descent_v1` runtime by itself.
