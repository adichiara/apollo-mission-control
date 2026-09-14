# Progress — independent guidance cross-check model

Date: 2026-09-14

## Completed

- Added a mission-neutral independent-guidance observation comparison model.
- Added caller-defined comparison fields, tolerances, and freshness window.
- Added validity/missing-field handling that produces an indeterminate result rather than a false comparison.
- Kept both sources symmetric: neither is treated as hidden truth.
- Kept mission decisions outside the model.
- Added synthetic tests and documentation.
- Updated Apollo 11 `backup_guidance` readiness to record that generic machinery exists while historical fields/tolerances remain unresolved.

## Consequence

The simulator can now represent the evidence relationship between independent guidance systems without collapsing that relationship into a pre-authored outcome.

This is reusable for Apollo 11 powered descent, Apollo 13 PGNS/AGS checks, and future rendezvous/abort scenarios.

## Apollo 11 profile advance

Research note 146 and `data/guidance_monitoring_profiles/apollo11_g_powered_descent_monitoring_partial.json` now source-bound part of the Apollo 11 configuration:

- AGS-PGNS in-plane problem-detection limits: 10 fps radial / 10 fps downrange;
- powered-flight-processor/PGNS isolation limits: 10 fps radial / 10 fps downrange;
- powered-flight-processor/PGNS PGNS-failure limits: 35 fps radial / 30 fps downrange;
- AGS-PGNS crossrange problem-detection limit: 20 fps.

Freshness/update cadence remains unresolved. The profile loader therefore refuses to generate an executable historical `GuidanceCrosscheckConfig` until a source-backed timing value is supplied.
