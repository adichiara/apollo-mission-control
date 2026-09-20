# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-20

## Completed

The Apollo-11-effective landing-radar velocity proof is executable from source-controlled geometry inputs through measurement-time propagation, beam projection, residual qualification, and weighted correction. The LM-5 Mission G prelaunch load controls position-specific geometry constants, and the mission-specific AC Electronics MSK-1137 definition controls known controller-visible LR field semantics and formatting.

Primary NASA ground-system documentation closes the architecture-level controller-product question. The Apollo 11 Mission Operation Report separates CCATS, RTCC, Voice Communications, Display/Control, and MOCR/SSR functions; NASA TN D-8316 independently constrains buffered display generation. A controller CRT product therefore cannot be modeled as a direct read of authoritative LGC/simulation state.

Costis, Ortolani, and Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401 (24 Dec 1969), is cited by HAER TX-109-C to Box 078-65/66 of the JSC History Collection at University of Houston-Clear Lake. No public digital copy was located, so direct inspection is **BLOCKED**.

NASA TN D-8316 establishes that D/TV generators could update displays independently of CRT refresh and could update complete instruction lists or single data words. Its four-second requirement concerns reference-slide access, not dynamic telemetry cadence.

The next request-workflow question was checked against a primary NASA Apollo 12 Saturn V Flight Manual. It states that the DRK requested specific RTCC display formats through labeled PBIs and provided the same capability as the MSK in display-request mode, with faster callup because no thumbwheel selection was required. This is useful adjacent-effectivity evidence for the MCC request architecture, but it is deliberately **not** treated as proof of Apollo 11 GUIDO console equipment or the MSK-1137 descent request sequence.

## Implementation

No executable renderer changed. Existing controller-product timestamp/provenance separation remains correct. A future interface may distinguish MSK-style coded selection from DRK-style direct format PBIs only after Apollo-11-effective station evidence establishes which mechanism belongs at GUIDO.

## Boundaries

No continuous antenna motion, attitude history, radar noise distribution, per-field ground transform, numeric display timing, Apollo 11 GUIDO DRK assignment, or request-key sequence is invented. Historical stochastic LR generation remains **BLOCKED**. Exact Apollo 11 per-field routing, dynamic-data cadence/latency/freshness, powered-descent format selection, and GUIDO request workflow remain unresolved; PHO-TN401 inspection is **BLOCKED** pending archival retrieval or an authenticated scan.
