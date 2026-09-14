# Generic Tracking Observation Proof

Status: **implemented validation model; not historically validated**

## Purpose

This model proves the next information-path boundary:

`authoritative trajectory state -> geometric tracking truth -> controller-eligible observation`

It exists specifically to prevent later station products from becoming direct aliases of hidden vehicle state.

Implementation:

`src/apollo_mission_control/tracking_observation.py`

## Scope

The proof computes geometric:

- range;
- line-of-sight unit vector;
- range rate.

It then applies caller-supplied observation effects:

- receive delay / age;
- deterministic range bias;
- deterministic range-rate bias;
- availability;
- validity;
- source/provenance metadata.

No Apollo, MSFN, RTCC, station-location, Earth, Moon, or mission constants are embedded.

## Truth versus observation

The model intentionally uses two separate objects.

### Geometric truth

Derived from authoritative vehicle and station position/velocity states.

This is simulation-internal state and should not be exposed directly to a controller presentation.

### Tracking observation

The downstream product carries only what the observation path makes available, plus explicit quality metadata.

An observation may therefore be:

- available and valid;
- available but invalid;
- unavailable;
- delayed/stale;
- biased.

This supports the project rule that valid physical state, instrumentation/telemetry availability, and ground-product correctness are independent concepts.

## Deliberate omissions

The proof does not yet model:

- signal light time;
- Doppler/radar hardware;
- station visibility/horizon;
- antenna geometry;
- atmosphere/ionosphere;
- measurement noise;
- clock error;
- station handover;
- MSFN routing;
- CCATS/RTCC transformation;
- historical sample cadence or display latency.

Those require scenario- and system-specific source support.

## Validation coverage

Synthetic tests verify:

- geometric range and range rate;
- observation delay and bias without mutating truth;
- unavailable values being withheld;
- available-but-invalid values remaining visible and flagged;
- coincident-geometry rejection;
- invalid delay rejection.

## Historical-use gate

A historical scenario must source, as applicable:

- station/network geometry;
- station/spacecraft reference frames;
- measurement type and equipment;
- measurement availability;
- delays/cadence;
- processing transformations;
- validity/failure behavior;
- controller-visible precision and presentation.

This proof supplies only the reusable causal separation.


## Facilitator validation API

The combined proof endpoint is:

`POST /api/admin/model-proof/trajectory-tracking`

The endpoint deliberately returns the translational result and the downstream tracking observation as separate objects. This makes the truth/observation boundary inspectable during model development while preserving the rule that player-facing products must consume only the observation side.
