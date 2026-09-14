# Stateful DPS domain proof

The user supplied a dps-numerical-v2 report for build
3bdcb13431378807eb05c20525e1b8597ad1684a on 2026-09-14 at
17:03:31.814Z–17:03:38.407Z: fourteen requests, sixteen PASS checks,
no errors, stable build identity. This is a summary, not a verbatim archive.

DPSTestSession adds retained state, separate command/advance operations,
revision checks, bounded work, atomic rejection, detached JSON export and
input-event replay. Tests cover changing direction after a burn, cutoff/coast,
replay, stale operations and rejected over-budget burns.

This is a domain-layer implementation only. It is not yet exposed in the
browser or HTTP API. Model time advances explicitly; no wall-clock pacing,
simulated crew, telemetry, gravity or live PC+2 integration is claimed.
Existing numerical assumptions remain in force. Exhaustion remains rejection.

Next: facilitator-protected per-run HTTP storage with serialized access,
bounded lifetime, browser controls and build-tagged exports. Existing /model-tests
continues to run the previously validated v2 suite unchanged.
