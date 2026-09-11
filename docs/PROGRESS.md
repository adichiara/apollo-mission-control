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
