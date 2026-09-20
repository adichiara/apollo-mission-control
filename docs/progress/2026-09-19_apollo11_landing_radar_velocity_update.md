# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-20

## Completed

The Apollo-11-effective landing-radar velocity proof remains executable from source-controlled geometry through measurement-time propagation, beam projection, residual qualification, and weighted correction. Mission-specific MSK-1137 evidence controls known controller-visible LR field semantics and formatting.

Apollo 11 ground-system documentation separates spacecraft/downlink, CCATS/RTCC, Display/Control, and controller presentation. NASA TN D-8316 separates buffered dynamic-word update from CRT refresh and reference-slide access. PHO-FAM001 and NASA TN D-7685 constrain generic request and TV-channel allocation behavior without establishing Apollo 11 GUIDO controls.

PHO-TR515 supplies a later-system field-provenance schema but not Apollo 11 identifiers. A renewed primary-source inspection of the AC Electronics Apollo 11 MSK-1137 sheet now establishes a mission-effective boundary that is stronger than that generic schema alone: the format visibly distinguishes `D/L` and `RTCC` provenance categories, and its notes identify `ACT ΔV` as ground computed. MSK-1137 was therefore a mixed-source controller product rather than a direct rendering of a single spacecraft downlist.

This does **not** establish which `D/L` or RTCC source fed every displayed field, nor an external-name/downlist identifier or computation formula. Those remain intentionally unassigned.

## Implementation

No executable renderer changed. Existing source/sample, receive/process, and display-time separation remains correct. A future historical field profile must preserve the mission-specific `D/L` versus RTCC provenance distinction and must not silently bind a displayed value to similarly named simulation state.

## Boundaries

No Apollo 11 per-field external-name mapping, exact downlist route, RTCC computation formula, numeric display timing, GUIDO control assignment, or powered-descent selection is invented. PHO-TN401 and flight-authentic stochastic LR generation remain **BLOCKED**. The next discriminating accessible target is Apollo-11-effective FDS/RTCC/CCATS documentation that maps individual MSK-1137 fields to the already documented `D/L`/`RTCC` source categories.
