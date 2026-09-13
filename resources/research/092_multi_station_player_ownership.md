# 092 — Multi-station player ownership implementation boundary

Date: 2026-09-12  
Status: **IMPLEMENTED — domain ownership generalized; transport/UI wiring still pending**

## Question

When compact mode gives one human player responsibility for more than one controller position, what may be combined in software without erasing the historically distinct station responsibilities documented for Apollo 13?

## Primary-source check

The implementation rechecked the same primary-source organizational evidence used for research note 091 before changing the domain model.

### Apollo 13 Press Kit

NASA's Apollo 13 Press Kit describes the Mission Control positions as separate responsibilities inside larger functional groups:

- TELMU/TELCOM and CONTROL are separate LM specialties within Systems Operations;
- FIDO, RETRO, and GUIDO are separate Flight Dynamics specialties;
- CAPCOM is the voice contact with the crew;
- FLIGHT is responsible for operational decisions/actions in the MOCR.

The source supports organizational affinity between some technical positions, but it does not say that one Apollo 13 controller performed the proposed compact-mode pairings.

### Apollo 13 Mission Operations Report

The 28 April 1970 Mission Operations Report retains separate controller appendices for FIDO, RETRO, GUIDO, TELMU, CONTROL, and INCO. This reinforces the implementation rule that a compact player may own several original stations while the software must continue to represent those stations separately.

### Apollo 13 Review Board material

The Review Board material separately identifies controller responsibilities and records the INCO/O&P shared-console arrangement. That demonstrates selected sharing existed historically, but it does not authorize arbitrary consolidation or establish the project's five-player arrangement as historical staffing.

## Implementation decision

`PC2Session` now supports **one player owning one or more original station identities**.

The domain model does **not** introduce `LM_SYSTEMS` or `FLIGHT_DYNAMICS` as historical stations. Those remain modern player-role labels only.

Implemented semantics:

- `assign_stations(player_id, stations)` assigns an ordered set of existing station identities;
- an original station can still belong to only one player at a time;
- `stations_for()` and `owns_station()` expose station ownership explicitly;
- station-specific actions authorize against the original station identity;
- station-specific audit actors remain `CONTROL`, `TELMU`, `GUIDO`, `FIDO_RETRO`, etc.;
- multi-station readiness requires the caller to identify which original station is reporting;
- bundled snapshots are a collection of separate station presentations keyed by original station name;
- the existing single-station API remains available for the seven-seat baseline.

## Approved compact configuration

The five-player mapping from note 091 is now encoded as project configuration:

- FLIGHT → `FLIGHT`
- CAPCOM → `CAPCOM`
- LM SYSTEMS → `TELMU`, `CONTROL`
- FLIGHT DYNAMICS → `GUIDO`, `FIDO_RETRO`
- INCO → `INCO`

These labels are explicitly simulator conveniences. They are not added to the authoritative station list.

## Information-boundary rule

Owning two stations does not fuse their information models.

A bundled player receives two station-scoped presentations. Data present in one presentation is not copied into the other, and an action remains authorized/audited under the station that owns it.

This is important because the historical sources establish separate controller responsibilities even where the positions belonged to the same functional group.

## Compatibility boundary

The legacy `station_assignments` mapping is retained as a one-station compatibility projection for existing callers. Authoritative compact-mode ownership is stored in `player_station_sets`.

Code that needs compact-mode semantics must use `stations_for()`, `owns_station()`, station-qualified readiness, or `bundled_player_snapshot()` rather than assuming every player has exactly one station.

## What remains unresolved

This change closes the framework-neutral domain boundary only.

Still pending:

1. HTTP join/rejoin support for station sets rather than one station string;
2. browser persistence of a compact role/station set;
3. bundled player UI navigation that keeps substation identity visible;
4. live five-player playtest after the seven-seat baseline is exercised;
5. any four-player-or-smaller configuration.

No new historical procedure, staffing claim, information-sharing rule, or controller authority was invented to implement compact mode.

## Sources

1. *Apollo 13 Press Kit*, NASA, 1970.  
   https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_PressKit.pdf
2. *Report of Apollo 13 Review Board — Appendix A / Baseline Data*, NASA, 1970, NTRS `19700078804`.  
   https://ntrs.nasa.gov/citations/19700078804
3. *Mission Operations Report — Apollo 13*, Manned Spacecraft Center, 28 April 1970.  
   https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf

See `resources/source-catalog/PC2_LOW_PLAYER_COUNT_SOURCES.md`.
