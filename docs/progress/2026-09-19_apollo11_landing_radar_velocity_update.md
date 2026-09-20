# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-19

## Completed

The Apollo-11-effective landing-radar velocity proof is executable from source-controlled geometry inputs through measurement-time propagation, beam projection, residual qualification, and weighted correction. The LM-5 Mission G prelaunch load controls the position-specific geometry constants, and the mission-specific AC Electronics MSK-1137 definition controls the known controller-visible LR field semantics and formatting.

Primary NASA ground-system documentation closes the architecture-level controller-product question. The Apollo 11 Mission Operation Report describes MCC mission support as distinct CCATS, RTCC, Voice Communications, Display/Control, and MOCR/SSR elements; telemetry and operational data can be processed by CCATS/RTCC for flight-control evaluation. NASA TN D-8316 independently describes Apollo real-time display as an organized set of computer-input and display subsystems. An Apollo 11 controller CRT product therefore cannot be modeled as a direct read of authoritative LGC/simulation state.

The next mission-specific retrieval target was then pursued. Costis, Ortolani, and Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401 (24 Dec 1969), is cited by HAER TX-109-C to Box 078-65/66, Mission Documents: Apollo 11, Johnson Space Center History Collection, University of Houston-Clear Lake. A targeted public-web retrieval found no digital copy. Direct inspection is now classified **BLOCKED** rather than merely unresolved. HAER's aggregate Apollo 11 display-use statistics remain useful secondary evidence but cannot establish exact GUIDO request keys, per-field routing, refresh cadence, latency, freshness, or powered-descent format selection.

The documented 2-second onboard LR component cadence remains explicitly prohibited as a substitute display cadence.

## Implementation

No executable renderer changed in this pass. Existing controller-product timestamp/provenance architecture remains correct: source/sample, receive/process, and display times stay separable. Any zero-delay or caller-selected cadence remains a simulation simplification unless later mission-era evidence closes the timing gate.

## Boundaries

No continuous antenna motion, attitude history, radar noise distribution, per-field ground transform, or display timing is invented. Historical stochastic LR generation remains **BLOCKED**. Direct PHO-TN401 inspection is also **BLOCKED** pending archival retrieval or an authenticated scan. Accessible mission-era Display/Control, RTCC, CCATS, console, and controller-procedure sources remain valid next targets because they may close narrower routing/timing questions independently.