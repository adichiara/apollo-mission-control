# 127 — PC+2 PHO-TR155 data-pack process boundary

Date: 2026-09-14

## Question

What can the surviving Apollo-era documentation establish about the relationship between PHO-TR155 and the Mission H-2 “data-pack Revision N” entry, without inventing the contents of Revision N or expanding undocumented pack abbreviations?

## Primary sources

### PHO-TR515 — MCC operational display-format standards/procedures

Philco’s display-format manual states that when an MCC user required a display, the Requirements and Configuration Section gathered the needed data through **data-pack circulation** and then prepared **PHO-TR155, Configuration and Control Document**, with computer listings. The same manual describes preliminary PHO-TR155 working lists as inputs to production work such as module overlays.

Primary source:

- Philco-Ford, **PHO-TR515**, MCC operational display-format standards/procedures manual, NASA NTRS 19730010501: https://ntrs.nasa.gov/api/citations/19730010501/downloads/19730010501.pdf

### PHO-TR460 — earlier H-2 configuration work

The earlier Philco progress report lists multiple individually named H-2 PHO-TR155 data-pack products (`FDB`, `CSB`, `FCOB`, `LSB`, `SLV`, `FSB`, `ESB`, `MOD`, `PCB`, `OSB`) and records a preliminary card deck/listing issued to IBM.

Primary source:

- Philco-Ford, **PHO-TR460**, NASA NTRS 19690029816: https://ntrs.nasa.gov/api/citations/19690029816/downloads/19690029816.pdf?attachment=true

### PHO-TR474 — final preflight H-2 revision history

The April 1970 Philco report separately records:

- PHO-TR155 Revision C issued 1970-03-06;
- H-2 data-pack Revision N issued 1970-03-06;
- implementation of the H-2 Display System in accordance with PHO-TR155 Revision C.

Primary source:

- Philco-Ford, **PHO-TR474**, 10 April 1970, NASA NTRS 19700016172: https://ntrs.nasa.gov/api/citations/19700016172/downloads/19700016172.pdf

## Finding

The documentation now supports a stronger process distinction than research note 126 could make alone:

`display/user requirement → Requirements & Configuration data-pack circulation → PHO-TR155 configuration/control output → working lists / display-production implementation`

Therefore, the surviving **Mission H-2 data-pack Revision N** entry should be treated as a revision state in the configuration-input/control workflow associated with PHO-TR155, not as a synonym for PHO-TR155 Revision C and not as proof of a single TELMU console-loading package.

PHO-TR460 remains important because it shows that the H-2 data-pack workflow previously consisted of multiple individually named pack products. PHO-TR515 explains how that class of material fit the configuration process: data-pack circulation supplied the Requirements and Configuration Section, which prepared PHO-TR155. PHO-TR474 then shows the final preflight revision chronology but does not enumerate Revision N’s internal contents.

## Historical boundary

The repository may now state that:

- PHO-TR155 was prepared from requirements/configuration information gathered through data-pack circulation;
- preliminary PHO-TR155 working lists were then used in downstream display-production work;
- the H-2 data-pack family was therefore upstream/supporting configuration material rather than merely another title for PHO-TR155 itself;
- H-2 data-pack Revision N and PHO-TR155 Revision C share the same 1970-03-06 date in PHO-TR474 but remain distinct documented products/states;
- Revision N remains a valid archival target because its contents may reveal which H-2 configuration inputs changed at the Revision-C milestone.

The repository must not state, absent additional primary evidence, that:

- Revision N was specifically the TELMU console-09 loading package;
- Revision N contained `GC0071V`, `GC0155F`, or any named measurement;
- any unsupported expansion of `FDB`, `CSB`, `FCOB`, `LSB`, `SLV`, `FSB`, `ESB`, `MOD`, `PCB`, or `OSB` is correct;
- the matching 1970-03-06 dates prove a one-to-one contents mapping between Revision N and PHO-TR155 Revision C.

## First-playable consequence

No simulation or UI change is justified by this finding. It is a provenance correction: the project may continue using a source-bounded TELMU inverter evidence product, but exact Apollo 13 module/indicator loading, display request, sampling cadence, precision, and latency remain unresolved.

## Next archival target

Highest value now shifts from a generic “pack key” alone to any primary artifact that connects one of the named data-pack products to PHO-TR155 contents, especially:

1. Mission H-2 data-pack Revision N or its transmittal/index;
2. PHO-TR155 H-2 Revision C contents/front matter;
3. a Requirements and Configuration data-pack definition/key identifying the named pack abbreviations;
4. Mission H-2 TELMU console-09 working list or operational-configuration sheet;
5. H-2 TDFCB Revision 4 LM Flight Control / PCMGS listings.

## Related research

- `resources/research/123_pc2_pho_tr155_h2_revision_c_provenance_boundary.md`
- `resources/research/124_pc2_pho_tr155_h2_display_system_implementation_boundary.md`
- `resources/research/125_pc2_h2_tdfcb_rev4_configuration_boundary.md`
- `resources/research/126_pc2_h2_photr155_data_pack_lineage_boundary.md`
