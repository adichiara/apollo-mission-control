# Landing Radar Guidance-Update Gate Model Proof

Status: **implemented reusable velocity-reference projection + measurement-quality + eligibility boundary; not a complete radar or state-estimator simulation**

## Purpose

Represent the decision boundary:

`radar measurement + data quality + update enablement + guidance-state condition -> channels eligible for estimator processing`

The implementation deliberately stops before state-vector correction.

Files:

- `src/apollo_mission_control/landing_radar_reference.py`
- `src/apollo_mission_control/landing_radar_quality.py`
- `src/apollo_mission_control/landing_radar_model.py`

## Why this boundary matters

Apollo 11 descent distinguishes several events that must not be collapsed:

- landing-radar data become good;
- the crew/guidance path enables radar updates;
- altitude updates can be admitted;
- velocity updates are gated by guidance-state conditions;
- downstream guidance processing uses accepted measurements.

A scenario script should not equate "radar good" with "state vector immediately becomes radar truth."

## Inputs

- measurement time;
- upstream radar data-good state;
- optional altitude measurement;
- optional velocity measurement;
- whether radar updates are enabled;
- current estimated guidance velocity;
- optional caller-supplied speed threshold for velocity-update eligibility;
- provenance/applicability.

## Outputs

- altitude measurement present/eligible;
- velocity measurement present/eligible;
- estimated speed;
- explicit blocking reasons;
- assumptions/provenance.

## Velocity-reference layer

`src/apollo_mission_control/landing_radar_reference.py` implements the source-backed velocity-reference boundary used before the velocity residual test:

`estimated vehicle velocity - lunar-surface velocity -> surface-relative velocity -> dot(selected radar-beam unit vector)`

The model requires the vehicle/surface vectors and selected beam unit vector to be supplied in one common frame at the measurement epoch. It rejects a non-unit beam instead of silently normalizing it.

This matches the flown Luminary 099 architecture in `SERVICER.agc`: the state estimate is advanced to the radar measurement time, the lunar-rotation correction `DELVS` is subtracted, and the result is dotted with the selected velocity-beam vector before the measured-minus-estimated residual is tested. Later R-567 guidance documentation independently describes the selected velocity-component unit vector and vehicle-to-platform transformation.

The model deliberately does **not** synthesize the LM-5 beam vector from antenna position, vehicle attitude, or platform attitude. That transform remains a separate historical geometry dependency.

## Upstream quality layer

`src/apollo_mission_control/landing_radar_quality.py` represents Data Good persistence, optional range-scale stability, channel validity, and caller-supplied affine residual reasonableness tests. These remain separate from the update gate so raw measurement qualification is not conflated with permission to enter the estimator.

Apollo 11 historical values are recorded in `data/landing_radar_profiles/apollo11_lm5_landing_radar_partial.json`; no Apollo constants are embedded in either model.

## Deliberately deferred

- LM-5 antenna-position + vehicle/platform attitude transform that produces the selected beam unit vector;
- surface intersection/terrain model;
- measurement noise/bias generation;
- antenna state;
- weighting/filter equations;
- state-vector correction;
- program-specific guidance-cycle cadence;
- controller display/downlink generation.

Those are separate layers.

## Apollo 11 applicability boundary

The Apollo 11 Mission Report documents:

- landing-radar data good at 102:37:51;
- radar updates enabled at 102:38:45;
- landing-radar velocity updating begins when estimated velocity falls below 2000 ft/s at 102:38:50.

Apollo guidance documentation further describes altitude updating after radar incorporation is allowed and velocity use below a preselected speed threshold.

The reusable models contain none of those mission values. The Apollo 11 profile now records the sourced 4-second Data Good persistence, 1-second range-scale stability, 50,000-ft range-update altitude boundary, 2,000-ft/s velocity-update boundary, astronaut approval requirement, and affine reasonableness-rule constants. Historical execution now has the reusable surface-relative selected-beam reference projection, but still requires the mission-specific LM-5 beam/attitude transform and downstream estimator pieces described below.

## Validation

Synthetic tests verify surface-relative selected-beam projection, strict unit-vector validation, independent quality, enablement, channel-presence, and velocity-threshold gates. The Causal Model Lab exposes the projection as a separate stage before the residual test.

This model does not authorize an `apollo11_descent_v1` runtime by itself.
