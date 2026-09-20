# Progress — Apollo 11 landing-radar DATA GOOD replay

Date: 2026-09-20

## Roadmap slice

Implement the source-backed historical landing-radar tracking interruptions without inventing a stochastic dropout process.

## Source-controlled behavior

Apollo 11 Mission Report Table 5-I records four one-second-resolution transitions:

- 102:44:11 — landing radar DATA NOT GOOD;
- 102:44:21 — DATA GOOD;
- 102:44:59 — DATA NOT GOOD;
- 102:45:03 — DATA GOOD.

The Apollo 11 AC Electronics guidance manual independently requires DATA GOOD to have been continuously present for at least four seconds before landing-radar measurement tests permit state-vector updating.

These are different states:

`raw DATA GOOD → persistence qualification → measurement reasonableness → estimator update`

A historical replay must therefore allow reacquisition without immediately reopening the estimator.

## Implementation

Added a mission-neutral discrete-transition replay model:

- caller supplies the initial DATA GOOD state and initial good-since time;
- the historical profile supplies only documented transitions;
- transitions retain their one-second source resolution;
- the replay computes current raw state, good-since time, duration, qualification state, applied transitions, and next documented transition;
- no state outside the source-bounded sequence is inferred automatically.

The Apollo 11 LM-5 landing-radar profile now contains the four Mission Report transitions and its existing four-second qualification duration.

Added facilitator proof endpoint:

`/api/admin/model-proof/landing-radar-data-good-replay`

The Causal Model Lab now provides explicit checks for:

- first reacquisition at 102:44:21 — raw DATA GOOD but not qualified;
- 102:44:25 — four seconds continuous DATA GOOD and qualified again.

Unit/profile/API/browser-contract tests cover both historical intervals and the qualification boundary.

## Guardrails

This does not establish:

- stochastic dropout probability;
- a random duration distribution;
- sub-second transition timing;
- maneuver kinematics producing either zero-Doppler loss;
- controller-visible symptoms or callouts;
- MCC display cadence.

Historical stochastic landing-radar generation remains BLOCKED under D-024.

## Next

The onboard landing-radar estimator is now executable/composed enough for the current architecture pressure test. The next high-value Apollo 11 gap is the controller-product boundary: per-field MSK-1137 D/L-versus-RTCC routing, external-name/downlist or computation identifiers, and controller-visible timing/workflow where mission-effective evidence exists.
