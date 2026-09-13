# Progress — PC+2 inverter selection correction

Date: 2026-09-13

## Research target

Recheck the unresolved inverter contingency chronology from research note 111 against mission-specific Apollo 13 procedure evidence before refining the post-warning action.

## Finding

The review exposed a correction to the prior synthesis. During the PC+2 read-up, CAPCOM explicitly directed `CB(16) INVERTER 2, CLOSE` and **deleted the stock checklist line `Select Inverter 1`**. Earlier in the same mission sequence, the crew had explicitly selected inverter 2 for LM AC use.

The generic LM handbook convention that inverter 1 normally operates during DPS/APS burns therefore cannot be used as the Apollo 13 PC+2 first-playable state. Apollo 13 deliberately modified that stock procedure.

## Repository consequence

- added research note 112 as the canonical correction;
- marked note 111 superseded in part;
- corrected note 059's implementation boundary;
- corrected the inverter source catalog;
- corrected the dated inverter roadmap addendum;
- added a station-status correction record;
- PR documentation should treat note 112, not note 111's earlier synthesis, as canonical.

## First-playable state

`PC+2 selected inverter 2 → inverter warning → crew tries switching to redundant inverter → warning remains → shutdown criterion`

A named post-warning inverter-2-to-inverter-1 transfer remains intentionally unfrozen until direct Apollo 13 procedural evidence is recovered.

## Priority

Physical seven-seat nominal, synthetic ΔP, and approved five-player compact validation remain the main PASS boundaries. This archival correction prevents an unsupported configuration from entering those runs; it does not create a new required scenario.
