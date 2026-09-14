# PC+2 PHO-TR155 / Mission H-2 source catalog

Date: 2026-09-14

Purpose: track primary evidence for the missing Apollo 13/H-2 MCC Operational Configuration and related mission-specific telemetry configuration, and prevent adjacent-mission configuration details from being promoted into the Apollo 13 first playable without mission-specific support.

## A. Primary mission-era provenance

### A1. PHO-TR474 — Houston Operations progress report

**Organization:** Philco-Ford / Houston Operations  
**Date:** 10 April 1970  
**NASA NTRS:** 19700016172  
**URL:** https://ntrs.nasa.gov/api/citations/19700016172/downloads/19700016172.pdf  
**Authority:** primary contemporaneous contractor record.

Relevant sections include **Operational Configuration Documentation (PHO-TR155)**, **MCC Reconfiguration**, and **TO-3900, Data Format Control Book**.

Mission H-2 PHO-TR155 entries establish:

- PHO-TR155 Revision A issued 1970-01-23;
- Revision B issued 1970-02-13;
- Revision C issued **1970-03-06**;
- H-2 data-pack Revision N dated **1970-03-06**;
- additional PHO-TR155 revision material continued through March 1970;
- the **Mission H-2 Display System configuration was in accordance with PHO-TR155 Revision C**;
- Revision C was **implemented in March 1970**;
- **no equipment configuration changes were necessary** for that implementation;
- the same quarterly MCC-reconfiguration discussion also records two MRR connect changes and **1126 console label changes**.

Mission H-2 telemetry-format entries establish:

- **Mission H-2 TDFCB Revision 4** was delivered **1970-01-28**;
- its deliverables included master/tape copies, a tape-discrepancy letter, **high-speed and wideband requirements**, a **special LM Flight Control listing**, Flight Control listing and compare, index listing, and master compare;
- all required LM measurements were checked for processing problems on **1970-01-26**;
- the H-2 Rev. 4 master tape was updated with an associated-vehicle/downlink-vehicle or RTCC-buffer field;
- the **Mission H-2 Rev. 4 TDFCB PCMGS was checked against PHO-TR155 on 1970-02-10**;
- the MCC Master Measurement Number List was checked against H-2 Rev. 4 and H-3 Rev. 1 on 1970-02-12;
- a Format-30/master comparison between H-2 Rev. 4 and H-3 Rev. 1 was prepared on 1970-03-18.

**Use:** authoritative for existence, dates, implementation state, and the relationship between H-2 telemetry-format configuration and PHO-TR155.  
**Do not use for:** exact TELMU console contents, exact parameter sample rates/loading, or to attribute all 1126 label changes specifically to Revision C, TELMU, or PC+2 inverter monitoring.

### A2. Mission H-2 TDFCB Revision 4 — identified, not yet recovered

**Title family:** Telemetry Data Format Control Book (TDFCB)  
**Mission/revision:** Mission H-2, Revision 4  
**Delivered:** 28 January 1970  
**Status:** primary mission-specific configuration authority identified through PHO-TR474; full document/listings not recovered in this pass.

The surviving Philco report shows that TDFCB Rev. 4 carried mission-specific telemetry-format and Flight Control products and that its PCMGS material was explicitly checked against PHO-TR155.

**Highest-value components to recover:**

- special LM Flight Control listing;
- Flight Control listing and compare;
- PCMGS listing/material;
- high-speed/wideband requirements;
- index/master compare;
- March 1970 Format-30 compare material.

**Use if recovered:** establish Apollo 13/H-2 measurement membership, telemetry formats/cadence, Flight Control routing products, and possibly the exact ground-side evidence path for `GC0071V` / `GC0155F`.

## B. Adjacent-mission continuity evidence

### B1. LM-1 Data Evaluation Guide

Primary Apollo-era documentation lists `GC0071V` and `GC0155F` as LM inverter-bus voltage/frequency ground-display telemetry measurements and provides LM-1-specific display-request identifiers.

**Use:** measurement identity and early program continuity.  
**Do not import:** LM-1 display-request numbers into Apollo 13.

### B2. Later Apollo TELMU operational-configuration evidence

Later Apollo operational material places `GC0071V` and `GC0155F` on TELMU operational indicators.

**Use:** continuity supporting TELMU as the station family for these measurements.  
**Do not import:** later module/indicator coordinates into H-2.

### B3. Later LM instrumentation packet

Later LM instrumentation documentation preserves the same measurements and gives format-dependent sample rates.

**Use:** continuity and warning that cadence is format-dependent.  
**Do not import:** later sample rates, MSK assignments, or loading into Apollo 13.

## C. Mission-specific material still sought

Highest priority:

1. **Mission H-2 TDFCB Revision 4**, delivered 1970-01-28, especially its special LM Flight Control and PCMGS listings;
2. **PHO-TR155, Mission H-2, Revision C**, issued 1970-03-06;
3. **Mission H-2 data pack Revision N**, dated 1970-03-06;
4. H-2 TELMU console-09 operational-configuration/loading sheets;
5. H-2 TELMU console handbook or controller log;
6. H-2 display-request/MSK inventory naming `GC0071V` and/or `GC0155F`.

## D. Current historical boundary

The repository may state that:

- H-2 PHO-TR155 Revision C existed and was issued on 1970-03-06;
- the Mission H-2 Display System was implemented in accordance with Revision C during March 1970;
- Revision C implementation required **no equipment configuration changes**;
- Mission H-2 telemetry-format configuration was controlled by **TDFCB Revision 4**, delivered 1970-01-28;
- its mission-specific products included LM Flight Control, PCMGS, high-speed/wideband, index, and compare material;
- Philco explicitly checked the H-2 Rev. 4 TDFCB PCMGS against PHO-TR155;
- `GC0071V` and `GC0155F` are source-backed LM inverter-bus electrical measurements;
- cross-mission evidence supports TELMU station-family ownership.

The repository must **not** state as Apollo 13 fact, absent recovered H-2 configuration evidence:

- exact TELMU indicator/module position;
- exact CRT/display-request number;
- exact MSK/DRK action;
- exact live sampling/display cadence;
- exact field precision or latency;
- exact CONTROL equivalent presentation;
- that `GC0071V` / `GC0155F` are definitely present in a specific unrecovered H-2 TDFCB listing;
- that the 1126 quarterly console-label changes were specifically TELMU or Revision-C inverter-display changes.

## Related research

- `resources/research/116_pc2_inverter_ground_observation_path.md`
- `resources/research/118_pc2_inverter_mcc_display_routing_boundary.md`
- `resources/research/119_pc2_inverter_telemetry_sample_display_continuity.md`
- `resources/research/120_pc2_inverter_as508_format30_boundary.md`
- `resources/research/121_pc2_inverter_telmu_indicator_continuity_boundary.md`
- `resources/research/122_pc2_inverter_onboard_ground_monitoring_boundary.md`
- `resources/research/123_pc2_pho_tr155_h2_revision_c_provenance_boundary.md`
- `resources/research/124_pc2_pho_tr155_h2_display_system_implementation_boundary.md`
- `resources/research/125_pc2_h2_tdfcb_rev4_configuration_boundary.md`