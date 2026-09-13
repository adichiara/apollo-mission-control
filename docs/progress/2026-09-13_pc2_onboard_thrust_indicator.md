# Progress — PC+2 onboard thrust-indicator identification

Date: 2026-09-13

## Completed

- Reopened the bounded Apollo 13 PC+2 77-percent onboard-thrust gap left by research note 061.
- Verified the mission-specific wording: CAPCOM gave the crew a shutdown rule for a “thrust monitor readout, 77 percent or below,” and the Mission Operations Report separately records thrust <77 percent onboard.
- Identified the LM panel-1 dual-scale **CMD THRUST / ENG THRUST** indicator in primary LM operations documentation.
- Verified that the **ENG THRUST** scale represents actual engine thrust in percent and is driven from a combustion-chamber-pressure transducer.
- Verified Apollo 13 flight-data material uses the exact CMD THRUST / ENG THRUST indicator terminology in the mission configuration.
- Rejected P47, the T/W indicator, and direct ground `GQ6510P` aliasing as the PC+2 crew readout.

## Result

The onboard instrument identity is now constrained with high confidence to the panel-1 CMD/ENG THRUST instrument, with the **ENG THRUST** scale being the source-backed actual-thrust scale relevant to the 77-percent performance criterion.

The evidence does not contain a verbatim Apollo 13 statement saying “use the ENG pointer for the 77-percent rule,” so the mapping is documented as a strong functional inference rather than an exact quoted mission-rule label.

## Remaining boundary

The exact applicability gate remains unresolved. PC+2 intentionally passed through 12.6-percent and 40-percent commanded-thrust startup segments, so the 77-percent limit cannot be active indiscriminately from ignition.

The executable rule therefore remains `NOT_EVALUABLE` until a source-bounded crew observation/applicability state exists. No hidden-state-derived percent gauge or invented activation time is added.

## Documentation updated

- `resources/research/107_pc2_onboard_thrust_indicator_identification.md`
- `resources/source-catalog/PC2_THRUST_MONITOR_SOURCES.md`
- `resources/research/061_pc2_onboard_thrust_monitor_observation_path.md`
- `docs/ROADMAP.md`
- `docs/roadmap/2026-09-12_first_playable_integration.md`
- `resources/README.md`
- root `README.md`
- dated station-status addendum

## Next boundary

Physical seven-seat validation remains the primary project blocker. If repository-side archival work continues before that run, the next thrust-monitor question is the exact 77-percent rule applicability transition during the PC+2 startup-to-maximum-thrust sequence.
