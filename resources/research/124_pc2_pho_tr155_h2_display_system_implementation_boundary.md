# Apollo 13 PC+2 — PHO-TR155 H-2 display-system implementation boundary

Date: 2026-09-14  
Status: **REVIEWED / PARTIALLY RESOLVED — contemporaneous Philco documentation confirms that the Mission H-2 Display System was configured in accordance with PHO-TR155 Revision C during March 1970 and that no equipment configuration changes were required. Exact H-2 TELMU display contents remain unresolved.**

## Question

Research note 123 established the existence and issue date of Mission H-2 PHO-TR155 Revision C but did not establish whether Revision C implied physical console/equipment changes, display-software/configuration changes, or both.

The next question is:

> What does contemporaneous Mission H-2 implementation reporting say about how PHO-TR155 Revision C affected the MCC Display System, and what may safely be inferred for the Apollo 13 TELMU reconstruction?

## Primary source finding

### Philco Houston Operations Progress Report PHO-TR474

Philco-Ford's report for the quarter ending 10 April 1970 states in its MCC reconfiguration section that:

- the **Display System Mission H-2 configuration was in accordance with PHO-TR155 Revision C**;
- **Revision C was implemented in March 1970**;
- **no equipment configuration changes were necessary** for that implementation;
- the same quarter also included implementation of Revision B and two MRR connect changes plus **1126 console label changes**.

Primary source:

- Philco-Ford / Houston Operations, **PHO-TR474**, 10 April 1970, NASA NTRS 19700016172:
  https://ntrs.nasa.gov/api/citations/19700016172/downloads/19700016172.pdf

This is mission-specific, contemporaneous evidence about the implementation state of the H-2 MCC Display System shortly before Apollo 13 flight.

## What this resolves

1. **Revision C was not merely a paper configuration artifact.** Philco explicitly states that the Mission H-2 Display System was configured in accordance with it and that the revision was implemented in March.
2. **Revision C did not require equipment configuration changes.** Therefore the project should not infer new physical display hardware, added TELMU modules, different monitor counts, or other hardware alterations merely because Revision C existed.
3. The H-2 configuration could change through software/data/configuration/connection/label work without changing equipment hardware. This is consistent with Apollo MCC's configurable display architecture.

## Important limit on the label-change count

PHO-TR474 reports 1126 console label changes in the same quarterly MCC-reconfiguration discussion, but the reviewed passage does **not** establish that all 1126 changes were caused by PHO-TR155 Revision C, nor that they belonged to TELMU, nor that they concerned PC+2 inverter monitoring.

Therefore do not use that number to reconstruct TELMU panel labels or to claim a specific H-2 console labeling change.

## Consequence for TELMU reconstruction

The strongest source-backed first-playable interpretation is now:

```text
Mission H-2 physical display-system hardware
    → no Revision-C equipment change required

Mission H-2 operational/display configuration
    → implemented in accordance with PHO-TR155 Revision C
    → exact TELMU loading still unrecovered
```

For the PC+2 inverter path, the project may continue to render a **project TELMU electrical product** carrying source-backed `GC0071V` / `GC0155F` evidence, but it must not claim that the rendering reproduces the exact H-2 module, CRT format, indicator coordinates, DRK/MSK selection, or console labeling.

## What remains unresolved

The source does not expose:

- exact TELMU console-09 loading for Apollo 13;
- exact `GC0071V` / `GC0155F` indicator or CRT placement;
- exact display request or MSK identity;
- exact selector/key workflow;
- live sampling/display refresh cadence or latency;
- whether these values were normally watched on operational indicators, CRT, strip chart, or a combination during PC+2;
- exact Revision-C change pages or the H-2 Revision N data-pack contents.

## Archival search result

A targeted public-web search again recovered PHO-TR474 and adjacent Apollo documentation, but not a digitized copy of PHO-TR155 Mission H-2 Revision C or data-pack Revision N. This remains a bounded search result, not evidence that the documents no longer survive.

## Next archival target

Priority remains:

1. **PHO-TR155 Mission H-2 Revision C**;
2. **Mission H-2 data-pack Revision N**;
3. H-2 TELMU console-09 loading/configuration sheets;
4. H-2 display-request or MSK inventories;
5. controller console handbooks/logs that expose TELMU electrical-display use.

## Project consequence

No station maturity grade changes and no implementation PASS state changes.

The historical boundary becomes more precise: **Apollo 13's H-2 display configuration was implemented under Revision C without requiring equipment reconfiguration.** Any exact physical-console reconstruction still requires separate evidence.