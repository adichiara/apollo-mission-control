# Roadmap addendum — PC+2 TELMU player presentation

Date: 2026-09-12  
Status: **CURRENT — records the latest completed presentation boundary and next integration priority**

## Completed boundary

The first-pass TELMU player presentation now exposes only the controller-facing PC+2 products already supported by the source/model boundary:

- LM power/configuration mode;
- documented 38–40 A burn-configuration current **reference**;
- inverter warning;
- inverter-switch action and action GET;
- post-burn power-down transition.

The presentation is explicitly labeled a project rendering. It does not claim an exact Apollo TELMU CRT, does not expose hidden integrity metadata, and does not treat deferred measured current as failed telemetry.

Implementation/research:

- `src/apollo_mission_control/telmu_presentation.py`
- `tests/test_telmu_presentation.py`
- `resources/research/075_pc2_telmu_player_presentation_boundary.md`
- `resources/source-catalog/PC2_TELMU_PRESENTATION_SOURCES.md`

## Immediate next work

Build the **first-pass FIDO/RETRO player presentation** from the existing PC+2 target/return projection.

Prioritize:

1. final maneuver target/PAD;
2. TIG and LVLH ΔV components;
3. expected perigee / return consequences;
4. current ground solution status;
5. post-burn trajectory assessment state.

Do not invent a complete RTCC Cartesian state vector, historical CRT coordinates, or a synthetic post-burn trajectory solution merely to fill the screen.

## Project-direction rule

Once FIDO/RETRO and the remaining minimum INCO / FLIGHT / CAPCOM views exist, shift directly to **integrated playable-session orchestration**. Additional display archaeology or subsystem expansion must be justified by a concrete player decision or validation need.
