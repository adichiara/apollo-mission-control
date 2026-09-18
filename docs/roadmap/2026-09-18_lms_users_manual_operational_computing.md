# Roadmap update — LMS User's Manual operational-computing source

Date: 2026-09-18

## Closed this pass

A distinct mature-LMS computing/operator source is now under direct retrieval control: the public `LMS User's Manual`, Volume 1, Update #34, dated 22 October 1971.

The source is complementary to, not a substitute for, the 1967 `LMA-790-2-LMS` Volume I simulator description and the 1971 LMS Console Directory.

Research 313 independently confirms from NASA/MSC `MSC-IN-CF-P-69-5` (1969) that `LMA790-2-LMS`, Volume II, Sections II and III were cited as an engineering reference dated April 1, 1967. Research 315 reconciles that with the earlier Avitabile archival recovery in note 220: Section 2 is **Malfunction Data** (3 folders) and Section 3 is **Lunar-landing Mission Procedures** (4 folders). Their MSC accession identifiers and technical contents remain unrecovered.

Research 316 narrows the handbook date discrepancy: the original NASA/MSC Corporate Author Index dates `67-14186`, `67-14187`, and `67-14188` to **1 April 1967**, while the Corporate Author Index Supplement gives **15 May 1967** for `67-14186` and `67-14187`. No source recovered yet explains the difference, so both dates are retained as retrieval keys and neither is assigned an unsupported administrative or revision meaning.

## Open gates, in order

1. Page-extract the 1967 Volume I candidate and verify its title/revision/effectivity against `LMA-790-2-LMS` / `67-14186`, explicitly checking both the 1 April and 15 May date controls.
2. Page-extract the 1971 User's Manual and search for explicit program loading, initialization, DDP-224/machine identifiers, common-memory use, and LMS-specific peripheral operation.
3. Retrieve `67-16127` Section 7 for simulator-output ownership/interface mapping.
4. Recover Volume II Section 2 — **Malfunction Data** — from the three Avitabile folders and extract only explicit malfunction/model/insertion relationships.
5. Recover Volume II Section 3 — **Lunar-landing Mission Procedures** — from the four Avitabile folders.
6. Retrieve `67-14187` / `67-14188` operating sections if machine/program allocation remains unresolved.
7. Cross-check any machine/program claim against TN D-7112 and Apollo 13-period configuration/change records before historical-profile use.
8. Keep NASA Release `66-254`/Honeywell procurement and RG 255 E.155B1 acceptance/configuration retrieval as parallel provenance threads.

## Guardrail

Neither the 1971 User's Manual nor the newly identified 1967 Sections 2/3 reference authorizes Apollo 13 processor assignments, software revisions, loading procedures, telemetry routing, numerical cadence, acceptance tolerances, station-product changes, or executable constants. The April/May catalog discrepancy likewise authorizes no technical inference.

The existing causal-engine measurement/output layer and Causal Model Lab already satisfy the architectural consequence of the recovered output-dictionary evidence. Do not add duplicate runtime abstractions merely because another historical source now supports the same separation.
