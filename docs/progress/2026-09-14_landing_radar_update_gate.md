# Progress — landing-radar update gate

Date: 2026-09-14

## Completed

- Added a mission-neutral landing-radar guidance-update eligibility model.
- Kept radar measurement quality upstream of the gate.
- Kept crew/guidance update enablement separate from data quality.
- Separated altitude and velocity channel eligibility.
- Added optional caller-supplied estimated-speed threshold for velocity updates.
- Explicitly stopped before state-vector correction/filtering.
- Added synthetic tests and model documentation.
- Updated Apollo 11 model readiness and architecture documentation.

## Apollo 11 source pressure

The actual-flight chronology distinguishes radar-good, update-enable, and velocity-update-start events. The model therefore does not collapse those into one boolean.

## Remaining boundary

The Apollo 11 landing-radar domain remains partial. Still required:

- physical radar measurement generation/error behavior;
- reasonability/validity logic;
- weighting/filter/state-vector correction;
- exact processing cadence;
- controller/downlink presentation.

No Apollo 11 threshold or measurement constant is embedded in the generic model.
