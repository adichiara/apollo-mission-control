# Apollo 13 PC+2 RTCC mass-properties sources

## NASA — Flight Control Division, Mission Operations Report — Apollo 13

- Date: 1970-04-28
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- Source class: primary / mission-specific Flight Control Division report

### Supports

- lift-off (`T-6`) mass properties were generated and loaded into RTCC by `T-2:46`, proving `T±N` is not generation/loading time;
- a `T+25` run was compared against `T+6` trims;
- LM-burn mass-property decks were updated to `T+55` before abort work;
- at ~59 hours GET, LM Control challenged a PC+2 DPS trim, then accepted Flight Dynamics data after having used inferior premission mass properties.

### Boundary

The report establishes a mission-relative mass-properties reference-state/epoch lineage and operational provenance/reconciliation behavior. It does not define exact `T+55` epoch semantics, deck fields, or explicitly identify the accepted ~59-hour basis as the `T+55` deck.

## NASA MSC — Apollo 13 Mission Report

- Date: 1970-09
- Report: `MSC-02680`
- NTRS: https://ntrs.nasa.gov/citations/19710003598
- NTRS scan: https://ntrs.nasa.gov/api/citations/19710003598/downloads/19710003598.pdf
- Source class: primary / mission-specific postflight mission report

### Supports

Appendix A §A.5 explicitly defines the table's mass properties as conditions **determined from postflight analyses of expendable loadings and usage during flight**. Expendables usage is based on reported real-time and postflight data; preflight measured module/stage weights and CG, calculated inertias, and monitored post-weighing changes were used to update the spacecraft mass properties.

Table A-I gives event-indexed weight, CG, moments of inertia, and products of inertia. Relevant post-accident rows include:

- second midcourse correction: `95,959.9 lb` ignition / `95,647.1 lb` cutoff;
- transearth injection (PC+2): **`95,424.0 lb` ignition / `87,456.0 lb` cutoff**;
- third midcourse correction: `87,325.3 lb` ignition / `87,263.3 lb` cutoff;
- fourth midcourse correction: `87,132.1 lb` ignition / `87,101.8 lb` cutoff.

Footnote `b` states that mass properties for these post-accident maneuver phases are referenced to the lunar-module coordinate system because the LM provided spacecraft dynamic control.

The PC+2/TEI ignition event mass is `508.0 lb` below the independently documented final P30 module-weight sum of `95,932 lb` (`62,480 + 33,452`).

### Boundary

`95,424.0 lb` is an official **postflight reconstructed event mass-property value**. The mission report does not establish that it was loaded into RTCC or used as the final targeting input. The `508 lb` difference is therefore a reconciliation between distinct historical product classes, not an error to normalize away. Do not attribute it to a particular consumable, vent, module-accounting rule, epoch, or deck without direct evidence.

## NASA MSC Internal Note 71-FM-214 — Skylab RTCC Mass Properties System Requirements

- Date: 1971-06-14
- Author: E. Ray Hischke
- Identifiers: `MSC-04378`, `MSC-IN-71-FM-214`, `NASA-TM-X-67442`
- NTRS: https://ntrs.nasa.gov/citations/19720006192
- Source class: primary NASA RTCC requirements documentation; explicitly describes Skylab as a carryover of the then-current Apollo RTCC Mass Properties System

### Supports

- module summation into total weight/CG state;
- engine-trim calculations driven by spacecraft weight/center of mass;
- temporary/permanent propellant depletion tables and associated weight calculations.

### Boundary

Architectural semantics only; not H-2 deck contents or `T+55` definition.

## Apollo 10/11 operational support material

Primary Apollo-era RTACF/mission-operations documentation establishes that mass-properties products were operational inputs to trajectory, trim, DAP/control, entry-aerodynamics, and propellant-support calculations and were updated as vehicle configuration/propellant state changed. These sources do not define Apollo 13 deck values.

## Project rule

For PC+2 validation keep separate:

1. hidden physical spacecraft mass/CG;
2. official postflight reconstructed event-indexed mass properties;
3. mission-control RTCC mass-properties state/deck;
4. module/depletion state;
5. reference-epoch label;
6. generation/update/load timestamp;
7. provenance/version of calculation basis;
8. P30 targeting/module weights;
9. controller-visible trim/trajectory products.

Do not label the P30 `62480 + 33452 = 95932 lb` as exact physical ignition mass. Do not retroactively use the mission report's `95424.0 lb` reconstructed PC+2/TEI ignition event mass as an operational targeting input.

## Next archival targets

Highest value is now H-2 RTCC/Flight Dynamics documentation, mass-property deck listings, processor descriptions, or maneuver worksheets that expose the **operational** module/depletion accounting behind the `T+55` state and final P30 module weights. Search terms should include `Apollo 13`, `H-2`, `RTCC`, `mass properties`, `T+55`, `PC+2`, `transearth injection`, `95932`, `P30`, `weight-CG`, `depletion table`, and `deck`.