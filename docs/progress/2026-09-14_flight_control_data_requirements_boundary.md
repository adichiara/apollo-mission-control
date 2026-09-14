# Progress — Flight Control data-requirements boundary

Date: 2026-09-14

Continued the H-2 TELMU archival track after research note 128.

Primary PHO-TR515 documentation identifies a more specific source class for recorder-side telemetry presentation. Flight Control Division branch requirements for pen recorders carried user console numbers and telemetry measurement numbers. The Flight Control Data Requirements Document carried high-speed format/subformat titles, measurement numbers, and pen locations; corresponding LBO requirements also used console numbers, subformat numbers, mission identifiers, and Flight Control branch designators.

Research note 129 records the resulting boundary: an H-2 Flight Control Data Requirements Document, branch requirement letter, or recorder cross-reference could materially narrow TELMU presentation, but PHO-TR515 does not establish that any PHO-TR460 abbreviated data pack is identical to that document and does not place `GC0071V` / `GC0155F` on any Apollo 13 recorder.

No simulation/UI behavior change is justified. Exact H-2 TELMU loading, live cadence, CRT/indicator routing, recorder assignment, precision, and latency remain unresolved.

Next archival targets now include the Mission H-2 Flight Control Data Requirements Document and H-2 recorder cross-reference/overlay requirement material alongside Revision N, PHO-TR155 Revision C, and TDFCB Revision 4.