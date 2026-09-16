# Progress — LMS validation / acceptance source boundary

Date: 2026-09-16

## Completed

- Located NASA/JSC Record Group 255 series **E.155B1 — Project Files on the Lunar Module Simulator**, 1968–1970.
- Verified from the National Archives inventory that the series explicitly contains **acceptance test plans and procedures**, together with statements of work, progress/technical reports, operations manuals, correspondence, photographs, and drawings.
- Recorded archive locator **old accession 72A794 / A-23-16-6**.
- Preserved the contract boundary: the inventory says most correspondence concerns Kollsman Instrument Corporation and NAS9-8634, but the folder-level contents have not yet been inspected.
- Linked the acceptance-document target to the already identified LMS Instructor's Handbook Volume II Section 7 **Simulator Output Tables** (MSC accession *67-16127).
- Added research note 219 and updated the simulation-engine source catalog, roadmap, and causal-engine architecture.

## Evidence boundary

This pass establishes **existence and location of formal LMS acceptance documentation**, not the acceptance criteria themselves.

No numerical tolerance, correlation rule, timestep requirement, reference trajectory, or subsystem pass/fail threshold is promoted from this finding.

## Architecture consequence

Historical fidelity and modern software correctness remain separate validation layers. Numerical verification, historical source/profile validation, measurement/output validation, causal scenario validation, and live integration validation are tracked independently until primary LMS acceptance/correlation sources provide historical criteria.

## Next retrieval targets

1. RG 255 E.155B1 acceptance test plans/procedures and technical reports.
2. LMA-790-2-LMS Volume II Section 7 Simulator Output Tables, accession *67-16127.
3. LMS-specific model checkout/correlation reports referenced by those sources.
4. The 50 ms AACS integration-step study to determine whether it includes an explicit acceptance/error criterion.
