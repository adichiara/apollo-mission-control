# Research Note 010 — Apollo 13 Controller Station Evidence

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Objective

Move from general controller responsibility descriptions toward evidence for the actual information and reasoning required at individual Apollo 13 stations.

## Source: Apollo 13 Mission Operations Report

The report is unusually valuable because it states that it tells the mission story **as seen in real time**, using only information available in real time even where later postflight evidence showed that information to be wrong.

That makes it directly relevant to simulator design: the player should receive the controller's historical information state, not retrospective truth.

## Station findings

### EECOM

Postflight operations comments explicitly praise the EECOM Staff Support Room, especially EPS personnel, because the oxygen-tank anomaly became a power-management problem during the event and entry planning.

The report also states that **HSD Format 30** was available for the first time on Apollo 13 and was used extensively for data playback associated with the oxygen-tank anomaly.

This means playback/historical telemetry could be operationally important, not only current telemetry.

### GNC

The report demonstrates diagnosis through relationships among:

- manifold pressures
- helium-valve state
- spacecraft electrical-bus state
- thruster commands
- DAP jet selections
- vehicle-rate behavior

The controller inferred whether RCS subsystems were operable from these combined observations.

### TELMU

After CSM failure, TELMU tracked LM power transition, heater current, bus voltage, and LM data acquisition. Once the return trajectory was chosen, total LM lifetime became the immediate systems concern.

Thus trajectory decisions and systems/consumables decisions were coupled across controller disciplines.

### CONTROL

Before the accident, CONTROL already had a live issue involving DPS supercritical-helium pressure. The team had predetermined action branches based on pressure ranges and projected PDI pressure.

This is an excellent example of authentic simulator gameplay arising directly from flight rules/procedure thresholds rather than a game-generated alert.

### INCO

The report shows INCO:

- commanding antenna changes
- timing commands against expected loss of two-way lock
- coordinating around ground-site behavior
- dealing with communications modes needed for TV/DSE functions

Ground communications must therefore have enough state to support command success/failure and acquisition effects.

### GUIDO

The report shows GUIDO checking CMC vector, clock, and REFSMMAT after a computer restart and developing alternate alignment/maneuver techniques when normal guidance capability was powered down.

### FIDO

The report shows FIDO dealing with validity of tracking data and RTCC vector/model state, not just reading a single trajectory solution.

## EECOM console benchmark from Apollo 13 Review Board

Figure B7-7 identifies actual console components.

Figures B7-8 and B7-9 preserve two frequently used EECOM display formats and provide real parameter labels/codes and example values.

This provides enough evidence to begin an authentic EECOM prototype without inventing a generic display.

Important caveat: the reproduced formats are snapshots from the Apollo 13 accident investigation, not a complete EECOM display catalog.

## Design consequence

Controller phone interfaces should eventually be generated from **station profiles** containing:

- historically available display formats
- parameter definitions
- request/access method
- update cadence
- event/limit indications
- station commands
- mission-era naming/configuration

The project should not define those fields generically and then populate them with invented data. Each field is a research target.

## Sources

- https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-review-report-app-b-c-d-e-19700078726.pdf
- https://ntrs.nasa.gov/citations/19700024253
