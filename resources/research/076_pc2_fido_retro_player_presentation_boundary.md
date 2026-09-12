# Apollo 13 PC+2 — first-pass FIDO/RETRO player presentation boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — final maneuver target and return-plan products presented without inventing a complete RTCC trajectory solution or historical CRT layout**

## Question

What is the smallest player-facing FIDO/RETRO presentation needed for the PC+2 slice so players understand the maneuver objective and return consequences without receiving an omniscient trajectory state?

## Primary-source findings

### Final PC+2 maneuver PAD

The Apollo 13 air-to-ground record at approximately 77:52 GET gives the final P30 LM maneuver PAD for PC+2:

- TIG: 79:27:38.30 GET;
- LVLH delta-V: X +833.0 fps, Y -50.9 fps, Z -213.9 fps;
- resultant delta-V: 861.5 fps;
- expected perigee: 20.5 nmi;
- burn duration: 4:24.

These values define the final maneuver target for the selected vertical slice and supersede earlier preliminary PC+2 alternatives.

### Final PC+2 monitor PAD

At 78:00:58 GET, CAPCOM read a monitor PAD beginning at Noun 61. The final values were:

- landing latitude: -21.65 deg;
- landing longitude: -165.00 deg;
- range to go at 0.05 g: 1163.5 nmi;
- velocity at entry interface: 36,292 fps;
- 0.05-g GET: 142:39:22.

The crew read these values back and CAPCOM confirmed them. These are the final return-plan values already frozen in the PC+2 nominal fixture.

### FIDO / RETRO responsibility split

The Apollo 13 Mission Operations Report establishes that FIDO owned the ground trajectory solution and trajectory-data quality, while RETRO used the accepted trajectory to maintain return/reentry options, landing-area consequences, and recovery planning.

For the first player presentation, the project combines them into one `FIDO_RETRO` projection because low-player-count aggregation has not yet been finalized. The information semantics remain distinct:

- FIDO side: ground solution status / maneuver trajectory;
- RETRO side: practical return plan and landing consequences.

## Presentation decision

The first FIDO/RETRO view is a **project rendering**, not an Apollo CRT reconstruction.

It contains three sections:

### MANEUVER TARGET

- TIG;
- PAD delta-V in LVLH;
- expected perigee.

### RETURN PLAN

- final PC+2 monitor PAD as a single sourced return-plan product containing landing coordinates, 0.05-g range-to-go, entry-interface velocity, and predicted 0.05-g GET.

### GROUND SOLUTION

- current project ground-solution status.

The solution-status product should not be interpreted as a universal statement that all trajectory products are correct. FIDO historically had to evaluate tracking and RTCC data quality, and the project already supports hidden ground-product integrity failures independently of visible validity/status.

## Critical omission: post-burn trajectory assessment

The minimum product definition ultimately requires a post-burn ground trajectory assessment. The current executable model does **not** yet have a propagated post-burn FIDO trajectory solution.

Therefore:

- `ground.postburn.propagated_trajectory` remains deferred;
- GUIDO's post-burn residual must **not** be substituted for a FIDO trajectory solution;
- physical burn completion must **not** automatically mark the return trajectory satisfactory;
- no synthetic state vector or impact/landing solution is manufactured merely to fill the screen.

This omission is visible in project documentation, not presented to the player as a historical telemetry outage.

## Exact display boundary

Still unresolved and intentionally not blocking:

- exact Apollo 13 FIDO CRT/display IDs during PC+2;
- exact RETRO return-plan CRT layout;
- CRT coordinates/request behavior/update cadence;
- exact RTCC Cartesian state vector at scenario start;
- post-burn propagated trajectory until a trajectory implementation is warranted.

## Implementation

- `src/apollo_mission_control/fido_retro_presentation.py`
- `tests/test_fido_retro_presentation.py`

The presentation preserves product value, units, validity, source layer, and provenance. Hidden integrity metadata is not exposed, and deferred trajectory products are omitted rather than presented as failed telemetry.

## Sources

Primary / mission-specific:

- Apollo 13 Technical Air-to-Ground / Flight Journal, Day 4 Part 2, final P30 LM maneuver PAD around 77:52 GET and monitor PAD at 78:00:58 GET.
- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, FIDO and RETRO post-mission reports.
- NASA, *Apollo 13 Mission Report*, September 1970, for the mission-level consequence that PC+2 shortened transearth time and moved landing from the Indian Ocean to the South Pacific.

Repository context:

- `docs/stations/APOLLO13_FIDO.md`
- `docs/stations/APOLLO13_RETRO.md`
- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`
- `data/scenarios/apollo13_pc2_nominal.json`

## Stop condition / next work

The minimum target/return presentation is sufficient for initial play. Do not implement a trajectory propagator merely to make this screen more complete.

Next build the **INCO** minimum view because the first minutes of the live slice deliberately begin with weak communications, then move to FLIGHT and CAPCOM. Once those minimum views exist, shift to integrated playable-session orchestration.
