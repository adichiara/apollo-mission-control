# Progress Log

## 2026-09-11 — Foundation

### Repository

- Confirmed repository: `adichiara/apollo-mission-control`
- Repository was empty at initialization.
- Added project documentation structure.
- No implementation code added yet.

### Project principles recorded

- research/documentation before Apollo-specific design
- no silent invention of undocumented historical details
- simplification only after real complexity is understood
- simulator-style presentation rather than conventional game UI
- mission success first; safe crew return when objectives are lost
- central server with phone-based controller clients
- physical station documentation as part of play

### Initial historical research

Primary/near-primary NASA material identified for:

- Apollo 11 flight mission rules
- Apollo 11 flight plan
- Apollo 11 mission operations/support structure
- Apollo Mission Control organization and controller workflow
- Apollo program mission-control architecture
- MCC operational display-format standards
- flight-rule development and use
- integrated Apollo mission simulation/training

See `resources/PRIMARY_SOURCE_CATALOG.md` and research notes.

### Next work

1. Reconstruct controller organization/responsibilities.
2. Reconstruct MCC console/display architecture.
3. Determine candidate first mission interval from documentation quality and useful controller interaction.
4. Only then begin decisions about player-count aggregation and implementation scope.


## 2026-09-11 — Phase 1: Flight-control organization, pass 1

### Completed

- Reconstructed the documented three-group MOCR structure:
  - Mission Command and Control
  - Systems Operations
  - Flight Dynamics
- Documented the primary front-room responsibilities for FLIGHT, CAPCOM, EECOM, GNC, TELCOM, CONTROL, FIDO, RETRO, GUIDO, Booster, INCO, O&P, NETWORK, SURGEON, FAO, and related positions.
- Documented the major Staff Support Rooms and their functions.
- Documented the CCATS and RTCC support layers and their relationship to controller information.
- Checked the Apollo 11 official flight-control manning memorandum.
- Confirmed that Apollo 11 used the LM call sign **TELCOM** in its official manning list and actual EVA Flight Director loop.
- Recorded evidence that TELCOM later changed to TELMU rather than treating the labels as interchangeable.
- Identified a mission-specific staffing warning: Apollo 11's manning memorandum uses four shift columns, while the Apollo 13 baseline describes three 9-hour shifts.

### New documents

- `docs/FLIGHT_CONTROL_ORGANIZATION.md`
- `resources/research/003_mocr_positions_and_responsibilities.md`
- `resources/research/004_support_rooms_and_ground_processing.md`
- `resources/research/005_apollo11_manning_and_nomenclature.md`

### Architecture consequence

The documented MCC organization reinforces the existing separation between physical spacecraft state, instrumentation/telemetry, ground processing, and controller-visible information. RTCC explicitly generated displays/calculations and CCATS explicitly handled telemetry/command/tracking flow; controller clients should not bypass those logical boundaries where they matter operationally.

### Next research pass

1. Reconstruct physical console/display capabilities and controller display-request workflow.
2. Identify mission-specific display formats for the likely Apollo 11 LM activation/descent interval.
3. Begin mapping controller positions to actual displays, parameters, and support-room inputs.
4. Research voice-loop topology using primary Apollo documentation/audio.
5. Continue searching for integrated-simulation / SimSup scenario documentation.
