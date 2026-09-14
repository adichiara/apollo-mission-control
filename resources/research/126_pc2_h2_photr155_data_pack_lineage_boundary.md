# Apollo 13 PC+2 — Mission H-2 PHO-TR155 data-pack lineage boundary

Date: 2026-09-14  
Status: **REVIEWED / PARTIALLY RESOLVED — contemporaneous Philco reporting shows that H-2 PHO-TR155 configuration work used multiple named data-pack products and a preliminary card deck/listing before the later report's generic reference to H-2 data-pack Revision N. Revision N must not be treated as a TELMU-specific loading artifact without the pack itself or an authoritative pack key.**

## Question

Research notes 123–125 identified PHO-TR155 Revision C, H-2 data-pack Revision N, and Mission H-2 TDFCB Revision 4 as the strongest remaining mission-specific configuration targets.

The next unresolved issue is:

> Does the surviving primary record justify treating “Mission H-2 data-pack Revision N” as a TELMU console-loading package, or does PHO-TR155 use a broader family of data-pack products?

## Primary-source finding

### Philco-Ford PHO-TR460 — earlier H-2 configuration work

An earlier Philco-Ford Houston Operations progress report, **PHO-TR460** (NASA NTRS 19690029816), describes Mission H-2 PHO-TR155 work as updates to multiple individually identified data packs. The surviving report text lists H-2 updates including:

- `FDB-I`;
- `CSB-Rev. E`;
- `FCOB-Rev. E`;
- `LSB-Rev. E`;
- `SLV-1`;
- `FDB-Rev. E`;
- `FSB-Rev. E`;
- and a later group including `CSB`, `ESB`, `FCOB`, `LSB`, `FDB`, `MOD`, `PCB`, `FSB`, and `OSB` at Revision F.

The same H-2 entry states that a **preliminary card deck and listing were issued to IBM**.

Primary source:

- Philco-Ford / Houston Operations, **PHO-TR460**, NASA NTRS 19690029816, section 2.4, “MCC Operational Configuration Documentation and Testing (ORACT).”
  https://ntrs.nasa.gov/api/citations/19690029816/downloads/19690029816.pdf?attachment=true

### Philco-Ford PHO-TR474 — later H-2 state

PHO-TR474 later reports H-2 PHO-TR155 Revision A/B/C issuance and says that **data-pack Revision N** was provided on **6 March 1970**, the same date as PHO-TR155 Revision C.

PHO-TR474 does not, in the reviewed passage, identify Revision N as a TELMU-only pack or provide the meaning of the earlier pack abbreviations.

Primary source:

- Philco-Ford / Houston Operations, **PHO-TR474**, 10 April 1970, NASA NTRS 19700016172, section 2.4.1.1.
  https://ntrs.nasa.gov/api/citations/19700016172/downloads/19700016172.pdf

## What this resolves

1. **PHO-TR155 configuration data was not represented by one obviously TELMU-specific artifact.** Earlier H-2 work explicitly involved a family of named data-pack products.
2. The surviving record shows a configuration lineage from multiple H-2 data-pack revisions and a preliminary IBM card deck/listing to the later Revision C / Revision N baseline.
3. Therefore, **“data-pack Revision N” is an archival identifier, not evidence by itself of TELMU console-09 loading**.
4. The next archival search should seek either:
   - the actual H-2 Revision N package;
   - a PHO-TR155 data-pack contents/key/index that maps the pack abbreviations and Revision N scope;
   - or the exact H-2 TELMU operational-configuration/loading sheets directly.

## What this does **not** resolve

The reviewed primary sources do not establish:

- what each pack abbreviation means in PHO-TR155;
- which pack, if any, contains TELMU console-09 loading;
- whether Revision N was a consolidated package label, a publication state, or another packaging convention;
- exact `GC0071V` / `GC0155F` indicator/module placement, CRT request, cadence, precision, or latency;
- exact IBM processing or card-deck semantics.

Do **not** expand the pack abbreviations from generic acronym lists or infer their contents from the names alone.

## Relationship to the TDFCB trail

The mission-specific reconstruction target is now better separated into three evidence families:

```text
Mission H-2 TDFCB Rev. 4
    → telemetry measurement / format / Flight Control configuration

PHO-TR155 Mission H-2 Rev. C
    → MCC operational/display configuration

PHO-TR155 data-pack family / Rev. N
    → supporting configuration products, exact pack scope still unresolved
```

PHO-TR474 documents a TDFCB-to-PHO-TR155 cross-check; PHO-TR460 shows that PHO-TR155 implementation itself used multiple configuration data-pack products.

## First-playable consequence

No simulation behavior changes.

Continue to render `GC0071V` / `GC0155F` as a source-backed project TELMU electrical product while leaving exact H-2 presentation unresolved. Do not cite “Revision N” as though it were the recovered TELMU loading sheet.

## Next archival targets

Priority order:

1. **Mission H-2 TDFCB Revision 4**, especially special LM Flight Control and PCMGS listings;
2. **PHO-TR155 Mission H-2 Revision C**;
3. a **PHO-TR155 data-pack key/index/contents list** that identifies the H-2 pack abbreviations and Revision N scope;
4. **Mission H-2 data-pack Revision N** itself;
5. H-2 TELMU console-09 operational-configuration/loading sheets or controller handbook.

## Project consequence

No station maturity grade changes and no implementation PASS state changes.

The historical boundary is tighter: **H-2 PHO-TR155 used a family of configuration data-pack products, so Revision N is not safely interpretable as TELMU-specific without the actual package or an authoritative contents key.**