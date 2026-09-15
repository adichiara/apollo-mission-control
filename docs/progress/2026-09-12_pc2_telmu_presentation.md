# Progress — PC+2 TELMU player presentation

Date: 2026-09-12

## Completed

- Confirmed the true current repository stopping point after reconciling already-completed restart-response and CONTROL/GUIDO presentation work.
- Researched the TELMU presentation boundary from mission-specific primary sources.
- Confirmed PC+2 LM power-up began around 78:12 GET and the documented burn configuration required approximately 38–40 A.
- Confirmed immediate post-burn LM power-down began around 79:34 GET.
- Preserved the documented inverter-warning-after-switch shutdown rule as a separate warning/action/re-observation path.
- Added `resources/research/075_pc2_telmu_player_presentation_boundary.md`.
- Added `resources/source-catalog/PC2_TELMU_PRESENTATION_SOURCES.md`.
- Added `src/apollo_mission_control/telmu_presentation.py`.
- Added `tests/test_telmu_presentation.py`.
- Defined the first TELMU player view as an explicitly labeled project rendering rather than a claimed historical CRT transcription.
- Labeled the documented 38–40 A figure as **BURN CONFIG CURRENT REF**, not live current telemetry.
- Originally kept inverter warning, switch action, and switch timestamp distinct.
- **Correction (2026-09-15):** the direct inverter-warning field was removed from TELMU after research note 117 bounded the derived caution as crew-side unless a stronger direct telemetry source is recovered. Source-backed inverter-bus voltage/frequency remain separate future TELMU electrical products once H-2 loading/presentation is sufficiently sourced.
- Omitted deferred actual current (`lm.power.current_a`) rather than presenting it as failed/unavailable historical telemetry.
- Kept hidden product-integrity metadata outside the player presentation.

## Scope boundary

The first TELMU screen does not expand into the full Apollo 13 lifeboat consumables problem. Water, oxygen, CO2/LiOH, detailed battery state, cabin temperature, and projected lifetime remain deferred because they are not required for the bounded PC+2 maneuver slice.

## Test status

Tests are committed. No successful full-suite execution is recorded in this pass.

## Next work

Build the first-pass **FIDO/RETRO** player presentation from the existing target/return products. Prioritize maneuver target, expected return consequences, solution status, and later post-burn trajectory assessment without inventing a full RTCC state vector or exact CRT layout.
