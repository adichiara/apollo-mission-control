# Station research status — Flight Control data-requirements boundary

Date: 2026-09-14

## TELMU / Mission H-2 configuration status

**Status:** still partial; no exact Apollo 13 console-loading reconstruction justified.

Research note 129 adds a new primary-source route to mission-specific presentation detail. PHO-TR515 shows that Flight Control branch recorder requirements identified console and telemetry assignments, while the Flight Control Data Requirements Document carried format/subformat, measurement-number, title, and pen-location information used to produce recorder overlays.

### Newly constrained

- mission/controller recorder presentation was requirements-driven rather than arbitrary;
- console number and measurement number were explicit pen-recorder requirement fields;
- high-speed format/subformat, measurement number, and pen position were explicit Flight Control Data Requirements fields;
- LBO products also carried mission and Flight Control branch identity.

### Still unresolved for TELMU

- whether `GC0071V` / `GC0155F` appeared on Apollo 13 TELMU stripchart/LBO recorders;
- exact H-2 console-09 module/indicator loading;
- exact CRT/display-request and MSK/DRK workflow;
- exact H-2 live cadence, precision, and latency;
- exact recorder pen/format/subformat assignment;
- Mission H-2 data-pack Revision N contents and pack-label definitions.

### Implementation consequence

Keep the current TELMU inverter evidence product source-bounded and explicitly non-exact. No software change is warranted from this archival finding alone.

### Next TELMU archival targets

Prioritize an H-2 Flight Control Data Requirements Document, Flight Control branch requirement letter, or recorder cross-reference/overlay requirement keyed by console and measurement number, in parallel with PHO-TR155 Revision C, Revision N, and TDFCB Revision 4.