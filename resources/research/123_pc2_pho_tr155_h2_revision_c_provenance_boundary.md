# Apollo 13 PC+2 — PHO-TR155 H-2 Revision C provenance boundary

Date: 2026-09-14  
Status: **REVIEWED / PARTIALLY RESOLVED — contemporaneous Philco documentation confirms that Mission H-2 PHO-TR155 Revision C was issued on 1970-03-06; the actual Revision C content was not recovered in this research pass, so Apollo 13 TELMU loading remains unresolved.**

## Question

Research note 122 left the exact Apollo 13 TELMU presentation of inverter-bus measurements `GC0071V` and `GC0155F` unresolved and identified **PHO-TR155 Revision C / Mission H-2 MCC Operational Configuration** as the highest-value archival target.

The next question is:

> Can the existence, revision date, and configuration-control lineage of that mission-specific document be established from primary sources, and does any indexed copy currently expose its TELMU console loading?

## Primary source finding

### Philco Houston Operations Progress Report PHO-TR474

Philco's contemporaneous progress report for the period ending 10 April 1970 contains a section titled **Operational Configuration Documentation (PHO-TR155)**. For **Mission H-2**, it records:

- PHO-TR155 revisions delivered to Data Control for publication on **6 February, 27 February, and 20 March 1970**;
- published H-2 PHO-TR155 outputs:
  - Revision A — **23 January 1970**;
  - Revision B — **13 February 1970**;
  - Revision C — **6 March 1970**;
- associated H-2 data-pack revisions culminating in **Revision N — 6 March 1970**.

Primary source:

- Philco-Ford / Houston Operations, **PHO-TR474**, progress report, 10 April 1970, NASA NTRS 19700016172:
  https://ntrs.nasa.gov/api/citations/19700016172/downloads/19700016172.pdf

This is direct contemporaneous evidence that the Apollo 13/H-2 Revision C configuration document existed and had been formally issued before flight.

## Archival availability finding

A targeted search of indexed NASA/Apollo document collections in this pass did **not** recover a digitized copy of the H-2 PHO-TR155 Revision C itself or its Revision N data pack.

That is a **bounded search result only**. It does not establish that no surviving paper, microfilm, institutional, or unindexed digital copy exists.

## Adjacent-mission evidence and its limits

Earlier and later LM records remain useful for continuity but cannot fill the Apollo 13 configuration gap:

- the LM-1 Data Evaluation Guide lists `GC0071V` and `GC0155F` as ground-display/telemetry measurements and supplies LM-1 display-request identifiers;
- later Apollo operational material supports TELMU ownership of the same electrical measurements;
- later LM instrumentation material gives format-dependent sampling information.

Those records support continuity of the **measurement identities and station family**, not Apollo 13-specific display-request numbers, indicator coordinates, MSK assignments, sample rates, or console geometry.

Therefore do **not** transplant:

- LM-1 display-request numbers;
- Apollo 15 TELMU module/indicator locations;
- LM-10 sample rates or MSK assignments;
- any later console layout

into the Apollo 13 first playable as historical fact.

## What this resolves

- `PHO-TR155` for Mission H-2 is a documented, real configuration-control product rather than a speculative archival target.
- Revision C was issued **1970-03-06**.
- H-2 data-pack Revision N was also dated **1970-03-06**, providing a second precise archival target.
- The remaining TELMU presentation gap is now tied to a specific missing mission configuration artifact rather than to uncertainty over whether such a document existed.

## What remains unresolved

Until Revision C, Revision N, or equivalent H-2 console-loading material is recovered, do not claim exact Apollo 13 values for:

- TELMU console-09 operational-indicator/module positions for `GC0071V` / `GC0155F`;
- CRT format/display-request identity;
- MSK/DRK action or field placement;
- normal live sample cadence, display refresh, field precision, or latency;
- physical indicator versus CRT versus strip-chart use during PC+2;
- direct CONTROL presentation of the same measurements.

## First-playable consequence

No first-playable product changes are required.

The conservative boundary remains:

```text
crew-local path
AC bus / inverter state
    → onboard Power/Temp Monitor and caution/warning
    → crew observation/report

separate from

ground path
GC0071V / GC0155F
    → PCM / MSFN / MCC processing
    → TELMU electrical evidence
    → project-rendered presentation
      [exact H-2 console format unresolved]
```

A project-rendered TELMU product may expose source-backed inverter voltage/frequency evidence, but it must not be labeled or drawn as an exact H-2 historical console reconstruction until mission-specific configuration evidence is recovered.

## Next archival target

Priority order:

1. **PHO-TR155 Mission H-2 Revision C**, issued 1970-03-06;
2. **Mission H-2 data pack Revision N**, dated 1970-03-06;
3. surviving H-2 TELMU console-09 loading sheets, console handbook, MOC change pages, or controller logs;
4. display-request inventories that explicitly associate `GC0071V` / `GC0155F` with H-2 TELMU presentation.

## Project consequence

This pass strengthens source provenance without increasing station maturity or changing any physical-validation PASS state. The absence of the Revision C content remains an explicit historical-configuration gap rather than an invitation to copy adjacent-mission display details.