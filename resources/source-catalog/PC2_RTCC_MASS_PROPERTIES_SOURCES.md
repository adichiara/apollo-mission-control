# Apollo 13 PC+2 RTCC mass-properties sources

## NASA — Flight Control Division, Mission Operations Report — Apollo 13

- Date: 1970-04-28
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- Source class: primary / mission-specific Flight Control Division report

### Supports

- lift-off (`T-6`) mass properties were generated and loaded into RTCC by `T-2:46`, proving `T±N` is not generation/loading time;
- a `T+25` run was compared against `T+6` trims;
- LM-burn mass-property decks were updated to `T+55` before abort work;
- at ~59 hours GET, LM Control challenged a PC+2 DPS trim, then accepted Flight Dynamics data after having used inferior premission mass properties;
- the final PC+2 pad was sent at about GET 78 hours based on the GYM 289 vector;
- in the later return/entry chronology, final stowage definitions were used to compute entry aerodynamics at approximately GET 122 hours, and those EOM aerodynamics were loaded into RTCC **based on mass properties job 27** (`L/D = .29052`).

### Boundary

The report establishes a mission-relative mass-properties reference-state/epoch lineage, operational provenance/reconciliation behavior, and direct H-2 evidence that a mass-properties computation could have a separately referencable **numbered job identity** preserved into a downstream operational product. It does not define exact `T+55` epoch semantics, deck fields, or explicitly identify the accepted ~59-hour basis as the `T+55` deck. **Job 27 is a late entry-aerodynamics job around GET 122 hours and must not be assigned to PC+2.** The PC+2 job number remains unknown.

## Apollo 13 restored mission-audio transcript — GET ~59:01–59:05

- Presentation: https://apollo13realtime.org/
- Source class: restored/edited transcript of mission audio; corroborating operational evidence, not a substitute for the Flight Control Division primary report

### Supports

At GET 59:01–59:05 CAPCOM reads a P30 pad for a PC+2 DPS abort and gives DPS gimbal trim values:

- pitch `5.86°`;
- yaw `6.75°`.

CAPCOM explicitly says these two angles **will be updated**, and the crew confirms them as DPS gimbal angles/GDAs.

### Boundary

These are recovered **interim/update-expected** trim values associated with the ~59-hour PC+2 product. Do not treat them as the final PC+2 trim, assign them specifically to the `T+55` deck, infer a job number, or assume they survived unchanged into the final ~78-hour GYM 289/P30 solution.

## NASA MSC — Apollo 12 Flight Control Division postflight report, RETRO

- Mission: Apollo 12
- Archival scan: https://www.ibiblio.org/apollo/Documents/Apollo_12_Postflight_Report_RETRO.pdf
- Relevant section: RETRO, General item 1
- Source class: primary / immediately preceding Apollo mission Flight Control Division postflight report

### Supports

- mass properties were computed by **RTCC controllers in an offline computer in lieu of RTACF**;
- mass properties were **run prior to each maneuver**;
- resulting SPS trim values agreed within **0.1 degree** with onboard postburn values for both CSM-alone and docked configurations.

This establishes that, by Apollo 12, operational mass properties could be a controller-initiated, pre-maneuver computational product in the RTCC support workflow rather than a static table value.

### Boundary

Do not infer that Apollo 13 used the identical Apollo 12 offline program, staffing procedure, run cadence, constants, or table layout. This source does not identify `T+55`, the accepted H-2 PC+2 trim basis, or the final P30 module-weight calculation. It strengthens the workflow model only.

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

## NASA MSC Mission Planning and Analysis Division — Apollo 11 Mission Support Section

- Mission: Apollo 11
- Archival scan: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- Relevant section: Mission Support Section, pp. 2-79 ff.
- Source class: primary NASA MSC Apollo operational-support documentation; architectural evidence, not Apollo 13 mission-specific values

### Supports

The RTACF computational-capability description explicitly states that mass-properties **weight-c.g. tables** were used by **RTACF and RTCC trajectory processors to compute pitch and yaw trim angles**. It also lists entry-aerodynamics and DAP-load mass-properties products. The separate constants-update capability included updates to mass-properties tables, aerodynamic tables, and thrust parameters.

This establishes a documented Apollo operational data-flow boundary:

`mass-properties weight/CG tables -> RTACF/RTCC trajectory processors -> pitch/yaw trim angles`

### Boundary

Do not infer that Apollo 13 used unchanged Apollo 11 software, constants, table layouts, or values. This source does not identify the H-2 `T+55` deck, accepted ~59-hour PC+2 trim basis, or final P30 module-weight calculation. It supports the architecture and provenance model only.

## Project rule

For PC+2 validation keep separate:

1. hidden physical spacecraft mass/CG;
2. official postflight reconstructed event-indexed mass properties;
3. mission-control RTCC mass-properties state/deck;
4. module/depletion state;
5. reference-epoch label;
6. generation/update/load timestamp;
7. provenance/version of calculation basis;
8. controller-initiated mass-properties calculation run and computational venue/version;
9. optional sourced mass-properties job identity/number;
10. weight/CG table or equivalent processor input product;
11. trajectory/trim processor invocation and pitch/yaw trim output;
12. P30 targeting/module weights;
13. controller-visible trim/trajectory products, including lifecycle/finality and reconciliation state.

Do not label the P30 `62480 + 33452 = 95932 lb` as exact physical ignition mass. Do not retroactively use the mission report's `95424.0 lb` reconstructed PC+2/TEI ignition event mass as an operational targeting input. Do not assign the documented late-entry mass properties job 27 to PC+2. Do not treat the ~59-hour `5.86° / 6.75°` pair as final.

## Next archival targets

Highest value is now the Apollo 13 Flight Director Log plus H-2 RTCC controller procedures, mass-property run sheets/listings, Flight Dynamics/RETRO worksheets, processor descriptions, weight/CG tables, or maneuver worksheets spanning **GET 55–59 and 77–78 hours**. Seek the numbered job/run and `T+55` basis behind the interim `5.86° / 6.75°` trim and any later replacement trim, plus an explicit connection to the final GYM 289/P30 product and `62480 / 33452 lb` module weights. Search terms should include `Apollo 13`, `H-2`, `RTCC`, `RTACF`, `mass properties`, `mass properties job`, `job 27`, `job number`, `T+55`, `PC+2`, `transearth injection`, `95932`, `P30`, `5.86`, `6.75`, `GDA`, `GYM 289`, `weight-CG`, `weight c.g.`, `trim`, `depletion table`, `offline computer`, `run`, and `deck`.