# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-19

## Completed

The Apollo-11-effective landing-radar velocity proof is executable from source-controlled geometry inputs through measurement-time propagation, beam projection, residual qualification, and weighted correction. The LM-5 Mission G prelaunch load controls the position-specific geometry constants, and the mission-specific AC Electronics MSK-1137 definition controls the known controller-visible LR field semantics and formatting.

The next unresolved controller-product item was researched against primary NASA ground-system documentation. The Apollo 11 Mission Operation Report, M-932-69-11, describes MCC mission support as distinct CCATS, RTCC, Voice Communications, Display/Control, and MOCR/SSR elements; telemetry and operational data can be processed by CCATS/RTCC for flight-control evaluation. NASA TN D-8316 independently describes Apollo real-time display as an organized set of computer-input and display subsystems.

This closes the architecture-level question: an Apollo 11 controller CRT product is not a direct read of authoritative LGC/simulation state. The implementation must preserve spacecraft/downlink, ground receipt/processing, and display projection as separate layers.

The same sources do **not** establish the exact CCATS/RTCC transformation for each MSK-1137 landing-radar field, a numeric CRT refresh period, end-to-end latency, stale/freshness policy, or exact GUIDO request/key workflow. The documented 2-second onboard LR component cadence remains explicitly prohibited as a substitute display cadence.

## Implementation

No executable renderer changed in this pass. Existing controller-product timestamp/provenance architecture is consistent with the newly controlled boundary: source/sample, receive/process, and display times remain separable. Any zero-delay or caller-selected cadence remains a simulation simplification unless later mission-era evidence closes the timing gate.

## Boundaries

No continuous antenna motion, attitude history, radar noise distribution, per-field ground transform, or display timing is invented. Historical stochastic LR generation remains **BLOCKED**. The next useful retrieval target is a mission-era MCC Display/Control, RTCC program, CCATS, console/display handbook, or controller procedure that explicitly identifies MSK-1137 routing/update/request behavior.
