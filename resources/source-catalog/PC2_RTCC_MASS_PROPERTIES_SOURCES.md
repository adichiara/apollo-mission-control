# Apollo 13 PC+2 RTCC mass-properties sources

## NASA — Flight Control Division, Mission Operations Report — Apollo 13

- Date: 1970-04-28
- NASA/Apollo Journal scan: https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- Source class: primary / mission-specific Flight Control Division report

### Supports

- LM-burn mass-property decks were updated to `T+55` decks before abort-maneuver work;
- LM Control initially challenged the PC+2 DPS trim after using premission mass properties;
- Flight Dynamics considered better in-flight mass-properties data available for the maneuver solution.

### Boundary

The report does not define the exact `T+55` naming convention, deck fields, mass/CG values, or derivation of the final P30 weights.

## Apollo 10 — Operational Support Plan for the Real-Time Auxiliary Computing Facility, Flight Annex

- Archival scan: https://www.ibiblio.org/apollo/Documents/Operational%20Support%20Plan%20for%20the%20Real-Time%20Auxiliary%20Computing%20Facility%20Apollo%2010%20Flight%20Annex.pdf
- Source class: primary Apollo-era operational support documentation

### Supports

- mass properties and spacecraft weight were operational inputs to RCS/SPS support calculations;
- the MRS program accepted updated mass-properties information as propellant was expended and vehicle configuration changed;
- mass-properties products supported maneuver/control quantities including trim and DAP-related work.

### Boundary

Apollo 10 documentation establishes functional semantics only. It does not define Apollo 13/H-2 `T+55` deck structure or values.

## Apollo 11 — Mission Operations Report

- Mission-document index: https://www.apollojournals.org/afj/ap11fj/a11-documents.html
- Source class: primary / mission operations report

### Supports

- RTACF mass-properties computations produced weight-CG tables;
- those tables were used by RTACF and RTCC trajectory processors for pitch/yaw trim calculations;
- mass-properties capability also supported entry-aerodynamics and DAP-load products.

### Boundary

These are Apollo 11 operational semantics, not Apollo 13 deck definitions.

## Project rule

For historical PC+2 validation, keep separate:

1. physical spacecraft mass/CG;
2. mission-control mass-properties state/deck;
3. maneuver targeting/P30 weight values;
4. controller-visible trim/trajectory products.

Do not label the documented `62480 lb` CSM and `33452 lb` LM P30 values as exact physical ignition masses until H-2-specific deck semantics or equivalent calculation records establish that relationship.

## Next archival targets

Prioritize mission-specific sources matching combinations of:

`Apollo 13`, `H-2`, `RTCC`, `RTACF`, `ACF`, `mass properties`, `LM burn`, `T+55`, `trim`, `P30`, `weight-CG`, `deck`.

Highest-value recoveries would be H-2 RTCC/Flight Dynamics requirements, mass-property deck definitions/listings, processor input descriptions, or maneuver-support worksheets that bridge the deck to the final PC+2 P30 solution.