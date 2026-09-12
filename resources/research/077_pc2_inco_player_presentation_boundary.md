# Apollo 13 PC+2 — first-pass INCO player presentation boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — minimum project-rendered INCO view defined from mission-specific communications evidence; exact historical CRT reconstruction remains unclaimed**

## Question

What is the minimum historically defensible player-facing INCO information needed for the first PC+2 slice?

## Primary-source findings

### PC+2 chronology / technical air-ground communications

The live slice begins with weak air-ground communications during the final maneuver-PAD exchange and later improves to a clear link after communications reconfiguration.

At **78:21:54 GET**, CAPCOM requested verification that the LM **Ranging Function** switch was in **Ranging** because the ground needed ranging support for the upcoming burn. The crew confirmed the requested state at approximately **78:22:14**. At **78:23:05**, CAPCOM returned the computer to the crew.

This establishes that communications quality and ranging configuration were operational dependencies of final PC+2 support rather than cosmetic status fields.

### Apollo 13 Mission Report — Communications Equipment

The mission report documents LM S-band communications as the primary Earth link during LM operations and states that:

- low-power and low-bit-rate configurations were used extensively to conserve electrical power;
- voice and telemetry configuration could differ;
- the updata/uplink path was used when required and performed nominally;
- communications quality depended on vehicle/configuration conditions rather than a single global communications-health state.

The report is sufficient to justify separate voice, telemetry, uplink, ranging, and overall link-quality products. It does not establish an exact first-pass INCO CRT layout for this slice.

## Presentation decision

The first INCO screen is a **project rendering of documented communications information**, not an Apollo CRT reconstruction.

It contains only the products already represented in the controller projection:

### AIR-GROUND LINK

- link quality;
- voice availability;
- telemetry availability.

### NAV / COMMAND SUPPORT

- ranging enabled;
- uplink state.

## Important boundaries

### Link quality is not a hidden diagnosis

`comm.air_ground_quality` is a controller-facing communications condition. It does not expose hidden simulator integrity or automatically identify which antenna/amplifier/site condition caused degradation.

### Voice and telemetry remain separate

A future sourced failure may affect voice, telemetry, or both. The first presentation therefore does not collapse them into a single communications `GO` flag.

### Ranging is explicit

The 78:21:54 request shows that ranging configuration had to be verified for final burn support. The player view therefore exposes the ranging state independently.

### Uplink is configuration-dependent

The nominal fixture presently carries the uplink path as `configuration_dependent`. The presentation preserves that value rather than simplifying it to a fabricated binary `GO` state.

## Deferred

Do not invent for this first slice:

- exact INCO CRT numbers or field coordinates;
- antenna look angles or detailed RF geometry;
- S-band amplifier switch state unless promoted into the common product model;
- exact site/network routing;
- detailed modulation/bit-rate controls;
- a generic communications-health score.

## Code

- `src/apollo_mission_control/inco_presentation.py`
- `tests/test_inco_presentation.py`

## Sources

Primary / mission-specific:

- Apollo 13 Technical Air-to-Ground / Flight Journal chronology around 77:55–78:23 GET.
- NASA, *Apollo 13 Mission Report*, Section 6.3, Communications Equipment.
- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, INCO/communications chronology where applicable.

Repository context:

- `docs/stations/APOLLO13_INCO.md`
- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`
- `src/apollo_mission_control/controller_products.py`

## Stop condition / next work

The minimum INCO presentation is sufficient for initial play. Additional antenna/network reconstruction should be demand-driven by a concrete communications failure scenario.

Next build the minimum **FLIGHT** and **CAPCOM** views, then stop expanding station presentation research and begin integrated playable PC+2 session orchestration.
