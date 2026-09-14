# Progress — PC+2 inverter onboard/ground monitoring boundary

Date: 2026-09-14

## Completed

- Continued from research note 121's unresolved question about actual PC+2 inverter evidence use.
- Reviewed the mission-specific Apollo 13 mission commentary / air-to-ground transcript rather than inferring behavior from later console layouts.
- Confirmed that the PC+2 activation read-up explicitly closed the EPS display and directed the crew to compare the Power/Temp Monitor AC-bus indication on **inverter 2, then inverter 1**.
- Confirmed that caution-and-warning power was deliberately retained through the immediate post-burn transition until PTC was established.
- Confirmed that low-bit-rate telemetry remained available during the later reduced-power configuration while local display functions were being removed.
- Added `resources/research/122_pc2_inverter_onboard_ground_monitoring_boundary.md`.
- Updated the inverter telemetry-presentation source catalog.

## Result

The first-playable information boundary is now more explicit:

```text
crew-local inverter evidence
    = Power/Temp Monitor + caution/warning + crew observation/report

TELMU ground evidence
    = GC0071V / GC0155F telemetry through MCC processing
```

These are separate evidence paths. The first playable should not treat inverter verification as an exclusively ground/TELMU event, nor should it convert crew-local indication automatically into direct ground telemetry.

## Still unresolved

- Apollo 13 / AS-508 TELMU console-09 loading for `GC0071V` / `GC0155F`;
- exact CRT/MSK/display-request use and live sample cadence;
- field precision, refresh, latency, and actual PC+2 TELMU presentation selection;
- any direct CONTROL presentation;
- direct caution/selector telemetry beyond the documented voltage/frequency path.

## Validation

Research/documentation-only change. No station-maturity grade, scenario PASS state, or physical-play validation claim changes.
