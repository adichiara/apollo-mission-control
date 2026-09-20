# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-20

## Completed

The Apollo-11-effective landing-radar velocity proof is executable from source-controlled geometry inputs through measurement-time propagation, beam projection, residual qualification, and weighted correction. The LM-5 Mission G prelaunch load controls position-specific geometry constants, and the mission-specific AC Electronics MSK-1137 definition controls known controller-visible LR field semantics and formatting.

Primary NASA ground-system documentation closes the architecture-level controller-product question. The Apollo 11 Mission Operation Report separates CCATS, RTCC, Voice Communications, Display/Control, and MOCR/SSR functions; NASA TN D-8316 independently describes Apollo real-time display as computer-input and output subsystems. A controller CRT product therefore cannot be modeled as a direct read of authoritative LGC/simulation state.

Costis, Ortolani, and Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401 (24 Dec 1969), is cited by HAER TX-109-C to Box 078-65/66 of the JSC History Collection at University of Houston-Clear Lake. No public digital copy was located, so direct inspection is **BLOCKED** rather than replaced by inference from HAER aggregate statistics.

A renewed primary-source check of NASA TN D-8316 narrows the timing problem. Its D/TV generators used random-access buffer memories, allowing the computer to update displays independently of CRT refresh requirements and to update either complete instruction lists or single data words. Its four-second timing requirement concerns electromechanical reference-slide access, not dynamic telemetry cadence. Thus CRT refresh, dynamic-word update, operator display request, and reference-slide access are distinct mechanisms.

## Implementation

No executable renderer changed. Existing controller-product timestamp/provenance separation remains correct. The documented two-second onboard LR component cadence and the four-second reference-slide access requirement are both explicitly prohibited as substitutes for an unsupported Apollo 11 dynamic controller-display update rate.

## Boundaries

No continuous antenna motion, attitude history, radar noise distribution, per-field ground transform, or numeric display timing is invented. Historical stochastic LR generation remains **BLOCKED**. Exact Apollo 11 GUIDO request/key workflow, per-field routing, dynamic-data cadence/latency/freshness, and powered-descent format selection remain unresolved; PHO-TN401 inspection is **BLOCKED** pending archival retrieval or an authenticated scan.