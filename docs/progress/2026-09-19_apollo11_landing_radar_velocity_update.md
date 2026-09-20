# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-20

## Completed

The Apollo-11-effective landing-radar velocity proof is executable from source-controlled geometry inputs through measurement-time propagation, beam projection, residual qualification, and weighted correction. The LM-5 Mission G prelaunch load controls position-specific geometry constants, and the mission-specific AC Electronics MSK-1137 definition controls known controller-visible LR field semantics and formatting.

Primary NASA ground-system documentation closes the architecture-level controller-product question. The Apollo 11 Mission Operation Report separates CCATS, RTCC, Voice Communications, Display/Control, and MOCR/SSR functions; NASA TN D-8316 independently constrains buffered display generation. A controller CRT product therefore cannot be modeled as a direct read of authoritative LGC/simulation state.

Costis, Ortolani, and Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401 (24 Dec 1969), is cited by HAER TX-109-C to Box 078-65/66 of the JSC History Collection at University of Houston-Clear Lake. No public digital copy was located, so direct inspection is **BLOCKED**.

NASA TN D-8316 establishes that D/TV generators could update displays independently of CRT refresh and could update complete instruction lists or single data words. Its four-second requirement concerns reference-slide access, not dynamic telemetry cadence.

Philco `PHO-FAM001` (30 Jun 1967) documents the Computer Display/Control Interface request transaction: display-request keyboards/encoders could select among up to 384 stored displays, with the operator pressing the desired-display switch and then the desired-display-device switch. This narrows the generic interaction sequence before Apollo 11. It does not establish GUIDO's Apollo 11 keyboard installation, labels, MSK-1137 mapping, or descent-time selection.

NASA TN D-7685, an Apollo Experience Report written from the flight-control user-organization perspective, adds the operational channel-allocation layer. It states that lunar-landing missions required 36 computer-driven TV channels rather than the 28 sufficient for Earth-orbital Apollo flights. In display-request mode, a console request caused the computer to generate and format the display, place it on the next available computer-driven TV channel, and automatically connect that channel to the requesting console. Allocation was first-come/first-served. Channel-attach mode instead connected a console to an already active channel. When capacity became constrained, a display showing the format and requesting console for each channel allowed the flight-control team to determine which formats to release. These are Apollo-program operational semantics; they do not prove a GUIDO-specific Apollo 11 control map or refresh cadence.

The Apollo 12 Saturn V Flight Manual independently states that the DRK requested specific RTCC display formats through labeled PBIs and provided the same capability as the MSK in display-request mode, with faster callup because no thumbwheel selection was required. That remains adjacent-effectivity evidence only.

## Implementation

No executable renderer changed. Existing controller-product timestamp/provenance separation remains correct. The display service may eventually model requested-format allocation, channel sharing/attach, and release as separate state from the format's dynamic data, but GUIDO-specific controls remain gated on Apollo-11-effective station evidence.

## Boundaries

No continuous antenna motion, attitude history, radar noise distribution, per-field ground transform, numeric display timing, Apollo 11 GUIDO DRK assignment, button/format mapping, or powered-descent selection is invented. Historical stochastic LR generation remains **BLOCKED**. Exact Apollo 11 per-field routing and dynamic-data cadence/latency/freshness remain unresolved; PHO-TN401 inspection is **BLOCKED** pending archival retrieval or an authenticated scan.
