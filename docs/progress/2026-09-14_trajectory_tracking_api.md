# Progress — trajectory-to-tracking validation API

Date: 2026-09-14

## Completed

- Added a facilitator-only API endpoint that runs the generic translational model and tracking-observation proof as one explicit chain.
- The request carries caller-supplied initial state, gravity, propulsion profile, station state, and observation delay/bias/quality inputs.
- The response keeps the translational result and downstream observation separate.
- Added API tests for normal coast/tracking behavior and unavailable observations.
- Preserved the existing DPS-only model-proof endpoint.

## Consequence

The validation harness can now exercise:

`propulsion profile → trajectory state → geometric tracking → delayed/biased/available observation`

without scenario-specific code or hidden historical constants.

This provides a reusable test surface for future scenario profiles before those models are wired into live player sessions.

## Boundary

The endpoint remains validation infrastructure. It does not create a player-visible product and does not claim Apollo/MSFN/RTCC historical behavior.
