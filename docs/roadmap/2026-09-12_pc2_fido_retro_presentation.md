# Roadmap addendum — PC+2 FIDO/RETRO player presentation

Date: 2026-09-12  
Status: **CURRENT — records the latest completed presentation boundary and next integration priority**

## Completed boundary

The first-pass FIDO/RETRO presentation now exposes the final historical PC+2 maneuver target and return-plan products already supported by the nominal fixture:

- TIG;
- final LVLH delta-V vector/resultant;
- expected perigee;
- final monitor-PAD landing/entry values;
- current ground-solution status.

The presentation remains a project rendering. It does not invent an RTCC Cartesian state vector, exact historical CRT layout, or post-burn trajectory solution.

Implementation/research:

- `src/apollo_mission_control/fido_retro_presentation.py`
- `tests/test_fido_retro_presentation.py`
- `resources/research/076_pc2_fido_retro_player_presentation_boundary.md`
- `resources/source-catalog/PC2_FIDO_RETRO_PRESENTATION_SOURCES.md`

## Important gap preserved

A real post-burn FIDO trajectory/landing assessment is not yet modeled. GUIDO residuals must not be used as a substitute, and physical burn completion must not automatically imply a satisfactory return trajectory.

## Immediate next work

Build the minimum **INCO** player view from the already-modeled communications products:

1. air-ground quality;
2. voice availability;
3. telemetry availability;
4. ranging state;
5. uplink configuration/state.

Then build minimum FLIGHT and CAPCOM views and shift directly to **integrated playable-session orchestration**.

## Project-direction rule

Do not reopen broad subsystem/display research before integration unless a concrete player decision or validation problem requires it.
