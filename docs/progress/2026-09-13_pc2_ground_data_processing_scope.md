# Progress — PC+2 ground data-processing scope

Date: 2026-09-13  
Status: **RESOLVED FOR FIRST PLAYABLE**

## Completed

- Reopened open question 13 using Apollo 13 primary sources first.
- Reviewed the Apollo 13 Review Board Appendix A mission-support descriptions for CCATS and RTCC.
- Cross-checked against the March 1970 Apollo MCC/MSFN configuration description.
- Defined the first-playable boundary as functional ground-data services rather than IBM/UNIVAC/software emulation.
- Preserved the staged PC+2 load path already established in notes 098–099.
- Kept tracking/ranging data quality distinct from trajectory products and from hidden spacecraft truth.
- Explicitly rejected unsupported internal keying, message formats, site-routing logic, delays, failure rates, and new playable ground-support positions.
- Added research note 103 and `PC2_GROUND_DATA_PROCESSING_SOURCES.md`.

## Project consequence

The simulator may represent source-backed availability/quality/readiness states for tracking, telemetry processing, trajectory solutions, and command/load transfer where those states affect controller decisions. Internal MSFN/CCATS/RTCC machinery remains deferred until a selected scenario requires a particular mechanism.

## Next boundary

Physical seven-seat and compact five-player execution remain the unclosed validation boundary. Additional historical research should be reopened only for a concrete dependency exposed by playtesting or a selected failure branch.
