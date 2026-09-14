# Apollo 13 PC+2 RTCC mass-properties sources

## NASA — Flight Control Division, Mission Operations Report — Apollo 13

- Date: 1970-04-28
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- Source class: primary / mission-specific Flight Control Division report

### Supports

- prelaunch lift-off (`T-6`) mass properties — weights, centers of gravity, and aerodynamic data — were generated and loaded into the RTCC;
- a `T+25` RTCC mass-properties run was compared against `T+6` pitch/yaw trims and did not require an update;
- LM-burn mass-property decks were later updated to `T+55` decks before abort-maneuver work;
- LM Control initially challenged the PC+2 DPS trim after using premission mass properties;
- Flight Dynamics considered better in-flight mass-properties data available for the maneuver solution;
- taken together, the repeated `T-6`, `T+6`, `T+25`, and `T+55` usage establishes a mission-relative time-tagged mass-properties lineage rather than an opaque revision-letter convention.

### Boundary

The report supports interpreting `T+55` as a mass-properties basis associated with approximately mission time +55 hours. It does not define whether that label means an exact 55:00:00 GET state, a nominal calculation epoch, deck-generation time, or a propagated state referenced to that mission time. It also does not provide the deck fields, mass/CG values, or derivation of the final P30 weights.

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
3. mission-relative deck epoch label and any separately documented generation/update timestamp;
4. maneuver targeting/P30 weight values;
5. controller-visible trim/trajectory products.

Do not label the documented `62480 lb` CSM and `33452 lb` LM P30 values as exact physical ignition masses until H-2-specific deck semantics or equivalent calculation records establish that relationship.

## Next archival targets

The broad question of whether `T+55` is time-related is now closed by the Apollo 13 Flight Dynamics narrative. Prioritize mission-specific sources matching combinations of:

`Apollo 13`, `H-2`, `RTCC`, `RTACF`, `ACF`, `mass properties`, `LM burn`, `T+55`, `T+25`, `T+6`, `trim`, `P30`, `weight-CG`, `deck`.

Highest-value recoveries would be H-2 RTCC/Flight Dynamics requirements, mass-property deck definitions/listings, processor input descriptions, or maneuver-support worksheets that define the precise T+N epoch convention and bridge the `T+55` deck to the final PC+2 solution.