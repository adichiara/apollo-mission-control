# 129 — PC+2 Flight Control data-requirements boundary

Date: 2026-09-14

## Question

Can primary MCC display-production documentation narrow what kind of source would contain mission-specific console/recorder assignment for telemetry measurements, without treating the unrecovered H-2 PHO-TR155 data-pack abbreviations as solved?

## Primary evidence

### PHO-TR515 — Flight Control requirements for telemetry recorders

Philco-Ford's MCC display-format standards/procedures manual describes the production of pen-recorder and light-beam-oscillograph overlays from Flight Control requirements.

For pen recorders it states that Flight Control Division approved branch requirements identified **user console numbers** and **telemetry measurement numbers**. It further states that the **Flight Control Data Requirements Document** listed high-speed format, subformat alphanumeric titles, measurement numbers, and pen locations for all four stripchart recorders.

For LBO overlays the same manual states that branch requirements identified **console numbers and telemetry subformat numbers**, and that the Flight Control Data Requirements Document listed the high-speed format, subformat titles, measurement numbers, and pen locations for all four LBOs. LBO overlays were identified with a Flight Control branch designator as well as format/subformat and mission identifiers.

Primary source:

- Philco-Ford, **PHO-TR515**, MCC operational display-format standards/procedures manual, NASA NTRS 19730010501, especially sections 5.2–5.7 and 6.2–6.5: https://ntrs.nasa.gov/api/citations/19730010501/downloads/19730010501.pdf

## Finding

This does **not** recover Apollo 13 TELMU console-09 loading, but it identifies a more specific source class for mission/controller telemetry presentation than the generic PHO-TR155 data-pack label alone:

`Flight Control branch requirement → console / measurement or subformat assignment → Flight Control Data Requirements Document → recorder/overlay production`

The manual therefore establishes that mission-era Flight Control requirements documentation could carry exactly the kinds of fields now missing for H-2 recorder presentation: console number, measurement number, high-speed format/subformat, title, and pen position.

It also clarifies a terminology trap. PHO-TR515 uses **Flight Control data pack** in the recorder-production workflow, but this wording does not by itself prove that PHO-TR460's H-2 pack label `FCOB` or any other abbreviated PHO-TR155 pack is identical to the Flight Control Data Requirements Document or to a specific recorder package.

## Historical boundary

The repository may now state that:

- Flight Control branch requirements were explicit inputs to MCC recorder-display production;
- for pen recorders those requirements included user console numbers and telemetry measurement numbers;
- the Flight Control Data Requirements Document carried format/subformat, titles, measurement numbers, and pen positions for stripchart and LBO recorders;
- recorder overlays were mission- and console-associated products and LBO overlays also carried a Flight Control branch designator;
- an H-2 Flight Control Data Requirements Document, branch requirement letter, recorder cross-reference, or equivalent could therefore materially narrow the Apollo 13 TELMU presentation path.

The repository must not state, absent H-2 material, that:

- `GC0071V` or `GC0155F` was assigned to a particular Apollo 13 stripchart/LBO pen;
- TELMU console 09 necessarily used a recorder rather than another display path for those measurements;
- any PHO-TR460 abbreviated data-pack product is proven to be the Flight Control Data Requirements Document;
- recorder format/subformat identifiers establish the live CRT/indicator cadence or routing.

## First-playable consequence

No simulator/UI change is justified. Existing TELMU inverter evidence remains a project rendering bounded by measurement identity and station-family continuity. Exact H-2 presentation remains unresolved.

## Next archival target

Add to the existing H-2 targets:

1. Mission H-2 **Flight Control Data Requirements Document** or branch requirement letters;
2. H-2 pen-recorder/LBO cross-reference lists keyed by mission, console, and measurement number;
3. H-2 recorder overlay requirements tied to LM Systems/TELMU;
4. Mission H-2 data-pack Revision N/transmittal and PHO-TR155 Revision C;
5. Mission H-2 TDFCB Revision 4 special LM Flight Control / PCMGS listings.

These targets are complementary: the Flight Control requirements source class may expose console/measurement/format/pen assignment even if the full PHO-TR155 package remains unrecovered.

## Related research

- `resources/research/125_pc2_h2_tdfcb_rev4_configuration_boundary.md`
- `resources/research/126_pc2_h2_photr155_data_pack_lineage_boundary.md`
- `resources/research/127_pc2_photr155_data_pack_process_boundary.md`
- `resources/research/128_pc2_h2_data_pack_organizational_acronym_boundary.md`
