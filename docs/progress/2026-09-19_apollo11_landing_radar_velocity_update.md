# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-20

## Completed

The Apollo-11-effective landing-radar velocity proof remains executable from source-controlled geometry through measurement-time propagation, beam projection, residual qualification, and weighted correction. Mission-specific MSK-1137 evidence controls known controller-visible LR field semantics and formatting.

Apollo 11 ground-system documentation separates spacecraft/downlink, CCATS/RTCC, Display/Control, and controller presentation. NASA TN D-8316 separates buffered dynamic-word update from CRT refresh and reference-slide access. PHO-FAM001 and NASA TN D-7685 constrain generic request and TV-channel allocation behavior without establishing Apollo 11 GUIDO controls.

The next unresolved per-field routing question was checked against the primary Philco-Ford PHO-TR515 *Display Formats Manual* (12 Jan 1973). For DTE formats, its Format Description Sheet data describes each dynamic group's source, coordinate location, and configuration. An external name may be a telemetry measurement number or a Data Processing Branch identifier for a computation, manual-entry datum, or special logic. The format metadata also carries a downlist indicator; if a display is updated from multiple downlists, that field is left blank. This establishes a concrete provenance model for controller fields rather than permitting direct authoritative-state aliasing.

PHO-TR515 is a 1973 system manual, not Apollo-11 mission-effectivity evidence. It does **not** identify the external names/downlists feeding Apollo 11 MSK-1137. Its explicit update-rate entry is described for plot formats; it is not evidence for MSK-1137 tabular update cadence.

## Implementation

No executable renderer changed. Existing source/sample, receive/process, and display-time separation remains correct. A future historical field profile should carry explicit source/provenance metadata rather than silently binding a displayed value to simulation state.

## Boundaries

No Apollo 11 MSK-1137 external-name mapping, downlist route, computed-field formula, numeric display timing, GUIDO control assignment, or powered-descent selection is invented. PHO-TN401 and flight-authentic stochastic LR generation remain **BLOCKED**. The next discriminating accessible target is Apollo-11-effective FDS/display-format or RTCC/CCATS documentation that names the MSK-1137 field sources.
