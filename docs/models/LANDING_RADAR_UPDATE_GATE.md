# Landing Radar Guidance-Update Gate Model Proof

Status: **implemented reusable eligibility model; not a radar or state-estimator simulation**

## Purpose

Represent the decision boundary:

`radar measurement + data quality + update enablement + guidance-state condition -> channels eligible for estimator processing`

The implementation deliberately stops before state-vector correction.

File:

`src/apollo_mission_control/landing_radar_model.py`

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

## Deliberately deferred

- radar beam geometry;
- surface intersection/terrain model;
- measurement noise/bias generation;
- antenna state;
- reasonability tests;
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

The reusable model contains none of those mission values. A future Apollo 11 runtime/profile may supply them only with explicit source provenance.

## Validation

Synthetic tests verify independent quality, enablement, channel-presence, and velocity-threshold gates.

This model does not authorize an `apollo11_descent_v1` runtime by itself.
