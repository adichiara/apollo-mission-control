# Research Note 017 — TELMU / CONTROL Responsibility Source Conflict

**Date:** 2026-09-11  
**Status:** SOURCE CONFLICT DOCUMENTED

## Issue

One section of the Apollo 13 Review Board Appendix B contains text that appears to reverse the established TELMU and CONTROL responsibility descriptions.

Its extracted text says, in effect:

- TELMU → LM guidance/propulsion/control systems
- CONTROL → LM electrical/environmental/communications systems

That conflicts with multiple mission-specific sources.

## Contrary mission-specific evidence

### Apollo 13 Mission Operations Report

Its contents and acronym list identify:

- **TELMU** — LM Electrical, Environmental, and EMU Officer; acronym expansion: Electrical, Environmental, Extra Vehicular Systems Engineer for the LM.
- **CONTROL** — Guidance, Control, and Propulsion Officer for the LM.

The postflight appendices themselves confirm this through their actual subject matter:

- TELMU Appendix G focuses on LM electrical power, water, oxygen, CO2/LiOH, thermal state and consumables.
- CONTROL Appendix H focuses on DPS, RCS, control configuration, GDA, rates/attitude and propulsion constraints.

### Apollo 11 operational material

Apollo 11 landing commentary likewise identifies:

- TELMU/TELCOM as LM electrical/environmental;
- CONTROL as LM control systems.

### Apollo 13 real-time communications

Actual Flight Director loop exchanges align with the Mission Operations Report division:

- TELMU discusses power, oxygen and electrical/environmental configuration;
- CONTROL discusses attitude control, guidance/control hardware and propulsion configuration.

## Current project treatment

The Apollo 13 Mission Operations Report plus the controller postflight reports are used for the operational division:

### TELMU
LM electrical, environmental, consumables, EMU/life-support systems.

### CONTROL
LM guidance/control/propulsion hardware.

The conflicting Review Board passage is retained as a source anomaly and is **not silently corrected or ignored**.

## Possible explanations

Not yet established:

- drafting/editing error in the Review Board appendix;
- transposed paragraph labels;
- source/OCR issue.

Do not claim which explanation is correct until the original page image or another authoritative explanation is located.

## Project lesson

Even official NASA documents can conflict.

For implementation facts:

1. record the conflict;
2. compare independent primary/mission-specific evidence;
3. prefer evidence closest to actual operational use when it is internally consistent;
4. retain the contradictory source in the provenance record.

## Sources

- Apollo 13 Mission Operations Report:
  https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- Apollo 13 Review Board Appendix B:
  https://ntrs.nasa.gov/citations/19700078726
