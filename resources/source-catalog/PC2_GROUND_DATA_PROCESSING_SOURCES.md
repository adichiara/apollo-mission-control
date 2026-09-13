# PC+2 ground data-processing sources

Date: 2026-09-13  
Scope: MSFN / CCATS / RTCC functions material to the Apollo 13 PC+2 first playable

## Primary sources

### Report of Apollo 13 Review Board — Appendix A

- **Title:** Report of Apollo 13 Review Board. Appendix A — Baseline Data: Apollo 13 Flight Systems and Operations
- **Report:** NASA-TM-X-66473
- **Date:** June 1970
- **NTRS:** https://ntrs.nasa.gov/citations/19700078804
- **Status:** REVIEWED-PARTIAL / IMPLEMENTATION-SOURCE
- **Relevant pages:** A-133–A-137 (mission support areas, CCATS, RTCC)
- **Supports:**
  - CCATS as MCC↔MSFN interface;
  - telemetry/command/tracking routing and processing;
  - command support from RTCC load generation/transfer through spacecraft acceptance verification;
  - RTCC telemetry processing, limit sensing, trajectory/ephemeris calculation, command-load generation, and display generation;
  - tracking-data selection/data-quality reporting to Flight Dynamics;
  - trajectory-computation support and requested command-load generation/review/transfer.

### Apollo MCC/MSFN Mission Configuration — Command, Communication, Telemetry, Tracking

- **Report:** NASA-TM-X-64290
- **Date:** March 1970
- **Author:** E. H. Clark
- **NTRS:** https://ntrs.nasa.gov/citations/19700024253
- **Status:** REVIEWED-PARTIAL / IMPLEMENTATION-SOURCE
- **Supports:**
  - main-line Apollo MCC/MSFN architecture;
  - RTCC controller-display support;
  - RTCC load-data generation/transfer toward CCATS;
  - redundancy/implementation context showing that these were support-computing functions rather than front-room station responsibilities.

### Apollo 13 Mission Report

- **Report:** MSC-02680 / NASA-TM-X-66449
- **Date:** September 1970
- **NTRS:** https://ntrs.nasa.gov/citations/19710003598
- **Status:** REVIEWED-PARTIAL
- **Use here:** mission-specific context for Apollo 13 trajectory, communications, and post-accident operations; detailed PC+2 load/ranging use is already cataloged under `PC2_FINAL_LOAD_UPLINK_SOURCES.md`.

## Implementation boundary supported by these sources

For the PC+2 first playable, model ground systems as decision-relevant functional services:

`MSFN observation/communications → CCATS reception/routing/processing → RTCC processing/product generation → front-room controller product/action`

and, for uplink:

`front-room request/solution → RTCC load generation/review → CCATS command path → spacecraft/crew acceptance evidence`

Do **not** infer exact internal keying, software execution, data formats, site scheduling, tracking geometry, processing delays, or failure rates unless a stronger source and concrete scenario dependency require them.
