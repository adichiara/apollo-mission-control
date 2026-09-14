# Apollo 13 PC+2 — Mission H-2 TDFCB Revision 4 configuration boundary

Date: 2026-09-14  
Status: **REVIEWED / PARTIALLY RESOLVED — contemporaneous Philco documentation identifies a mission-specific Mission H-2 Telemetry Data Format Control Book (TDFCB), Revision 4, delivered before flight and checked against PHO-TR155. The surviving report does not expose the TDFCB contents, so exact Apollo 13 TELMU loading/cadence remains unresolved.**

## Question

Research notes 123–124 established that PHO-TR155 Revision C governed the Mission H-2 Display System, but the exact TELMU electrical display/loading remained unrecovered.

The next question is:

> Is there a mission-specific Apollo 13 telemetry-configuration authority, separate from PHO-TR155, that can constrain which LM measurements and format products were prepared for the MCC?

## Primary source finding

### Philco-Ford PHO-TR474 — TO-3900, Data Format Control Book

Philco-Ford's quarterly report dated 10 April 1970 identifies the **Telemetry Data Format Control Book (TDFCB)** as an active Mission H-2 configuration-control product.

For Mission H-2 it reports that:

- a **Mission H-2 TDFCB, Revision 4** was prepared and delivered on **28 January 1970** (ahead of its 4 February due date);
- the delivery included a master and two copies, tape copies, a tape-discrepancy letter, **high-speed and wideband requirements**, a **special LM Flight Control listing**, Flight Control listing and compare, index listing, and master compare;
- Philco checked **all required LM measurements** for processing problems on **26 January 1970**;
- the Mission H-2 Rev. 4 master tape received an associated-vehicle/downlink-vehicle or RTCC-buffer field;
- on **10 February 1970**, the **Mission H-2 Rev. 4 TDFCB PCM Ground Station (PCMGS)** material was checked against **PHO-TR155**;
- on **12 February 1970**, the MCC Master Measurement Number List was checked against Mission H-2 Rev. 4 and Mission H-3 Rev. 1;
- on **18 March 1970**, Philco prepared a **Format 30** and master compare between Mission H-2 Rev. 4 and Mission H-3 Rev. 1 for RSDP.

Primary source:

- Philco-Ford / Houston Operations, **PHO-TR474**, 10 April 1970, NASA NTRS 19700016172, sections 3.2.6 / pp. 3-10 through 3-12.
  https://ntrs.nasa.gov/api/citations/19700016172/downloads/19700016172.pdf

## What this resolves

1. Apollo 13/H-2 had a **mission-specific telemetry-format configuration baseline**: TDFCB Revision 4.
2. The TDFCB was not merely a generic telemetry handbook. The reported deliverables included LM-specific Flight Control listings, high-speed/wideband requirements, index/compare products, and a mission master tape.
3. PHO-TR155 and the TDFCB were explicitly cross-checked: Philco records checking the H-2 Rev. 4 **PCMGS against PHO-TR155**. This makes TDFCB Rev. 4 a high-value companion authority for reconstructing the telemetry side of H-2 display products.
4. The H-2 telemetry baseline was mature before flight: Revision 4 was delivered in January and remained the H-2 revision used in documented February and March compare/check work.

## What this does **not** resolve

The reviewed source does **not** reproduce TDFCB Revision 4 itself. Therefore it does not establish:

- that `GC0071V` or `GC0155F` appeared in a particular H-2 Flight Control listing;
- their exact H-2 PCM format/sample cadence;
- an H-2 MSK, display request, CRT coordinate, or operational-indicator position;
- a TELMU versus CONTROL routing decision for a specific display;
- display refresh/latency;
- exact Format-30 subformat membership for these parameters.

Do not infer those details from the existence of the TDFCB.

## Relationship to PHO-TR155

The evidence now supports a two-document reconstruction target:

```text
Mission H-2 TDFCB Rev. 4
    → telemetry measurement / format / Flight Control configuration
    → PCMGS material cross-checked against PHO-TR155

PHO-TR155 Mission H-2 Rev. C
    → MCC operational/display configuration
```

The surviving PHO-TR474 report proves that these configuration domains were checked against one another, but it does not expose the parameter-to-console details that the project still seeks.

## First-playable consequence

No existing PC+2 implementation assumption needs to change.

The project should continue to render source-backed inverter electrical evidence as a **project TELMU product**, while treating the exact Apollo 13 display/loading and cadence as unresolved. The new result improves provenance: the next archival search should target **Mission H-2 TDFCB Revision 4 and its special LM Flight Control/PCMGS listings**, not only PHO-TR155 Revision C.

## Next archival targets

Priority order:

1. **Mission H-2 TDFCB Revision 4** (delivered 1970-01-28);
2. its **special LM Flight Control listing** and Flight Control listing/compare;
3. its **PCMGS** listing/material checked against PHO-TR155 on 1970-02-10;
4. its high-speed/wideband requirements and March Format-30 compare material;
5. PHO-TR155 Mission H-2 Revision C;
6. Mission H-2 data-pack Revision N.

## Project consequence

No station maturity grade changes and no implementation PASS state changes.

The historical boundary is tighter: **Apollo 13/H-2 telemetry configuration was controlled by Mission H-2 TDFCB Revision 4, and Philco explicitly checked its PCM ground-station configuration against PHO-TR155. Exact parameter loading remains an archival gap, not a license to copy adjacent-mission values.**