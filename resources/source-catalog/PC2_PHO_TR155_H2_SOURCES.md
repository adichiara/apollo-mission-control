# PC+2 PHO-TR155 / Mission H-2 source catalog

Date: 2026-09-14

Purpose: track primary evidence for the missing Apollo 13/H-2 MCC Operational Configuration and prevent adjacent-mission configuration details from being promoted into the Apollo 13 first playable without mission-specific support.

## A. Primary mission-era provenance

### A1. PHO-TR474 — Houston Operations progress report

**Organization:** Philco-Ford / Houston Operations  
**Date:** 10 April 1970  
**NASA NTRS:** 19700016172  
**URL:** https://ntrs.nasa.gov/api/citations/19700016172/downloads/19700016172.pdf  
**Authority:** primary contemporaneous contractor record.

Relevant section: **Operational Configuration Documentation (PHO-TR155)**.

Mission H-2 entries establish:

- PHO-TR155 Revision A issued 1970-01-23;
- Revision B issued 1970-02-13;
- Revision C issued **1970-03-06**;
- H-2 data-pack Revision N dated **1970-03-06**;
- additional PHO-TR155 revision material continued through March 1970.

**Use:** authoritative for existence, issue date, and configuration-control lineage of H-2 PHO-TR155 Revision C.  
**Do not use for:** console contents not reproduced in PHO-TR474.

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

1. **PHO-TR155, Mission H-2, Revision C**, issued 1970-03-06;
2. **Mission H-2 data pack Revision N**, dated 1970-03-06;
3. H-2 TELMU console-09 operational-configuration/loading sheets;
4. H-2 TELMU console handbook or controller log;
5. H-2 display-request/MSK inventory naming `GC0071V` and/or `GC0155F`.

## D. Current historical boundary

The repository may state that:

- H-2 PHO-TR155 Revision C existed and was issued on 1970-03-06;
- `GC0071V` and `GC0155F` are source-backed LM inverter-bus electrical measurements;
- cross-mission evidence supports TELMU station-family ownership.

The repository must **not** state as Apollo 13 fact, absent recovered H-2 configuration evidence:

- exact TELMU indicator/module position;
- exact CRT/display-request number;
- exact MSK/DRK action;
- exact live sampling/display cadence;
- exact field precision or latency;
- exact CONTROL equivalent presentation.

## Related research

- `resources/research/116_pc2_inverter_ground_observation_path.md`
- `resources/research/118_pc2_inverter_mcc_display_routing_boundary.md`
- `resources/research/119_pc2_inverter_telemetry_sample_display_continuity.md`
- `resources/research/120_pc2_inverter_as508_format30_boundary.md`
- `resources/research/121_pc2_inverter_telmu_indicator_continuity_boundary.md`
- `resources/research/122_pc2_inverter_onboard_ground_monitoring_boundary.md`
- `resources/research/123_pc2_pho_tr155_h2_revision_c_provenance_boundary.md`