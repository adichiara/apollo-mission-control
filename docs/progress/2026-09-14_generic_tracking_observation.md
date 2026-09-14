# Progress — generic tracking observation proof

Date: 2026-09-14

## Completed

- Added a mission-neutral geometric tracking layer deriving range, line-of-sight, and range rate from authoritative trajectory and station states.
- Added a separate observation layer with deterministic delay, range/range-rate bias, availability, validity, source, and provenance.
- Ensured unavailable observations withhold numerical values rather than leaking hidden truth.
- Allowed available-but-invalid values to remain visible with explicit validity state, supporting bad-processing/fault scenarios.
- Added synthetic tests for geometry, delay/bias separation, outages, invalid products, coincident geometry, and input validation.
- Added model documentation and architecture/roadmap integration.

## Architectural consequence

The causal chain now has a reusable numerical path:

`propulsion → trajectory truth → geometric tracking truth → observation`

without making controller-visible products aliases of authoritative state.

This supports many future scenarios, including maneuver evaluation, rendezvous, abort tracking, ground-processing discrepancies, and network outages, once historical station/network and processing details are sourced.

## Boundary

This is not an MSFN, radar, Doppler, CCATS, or RTCC implementation. Historical use still requires sourced station geometry, frames, measurement type, cadence, latency, processing, validity behavior, and presentation.
