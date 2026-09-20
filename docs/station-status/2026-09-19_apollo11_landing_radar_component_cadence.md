# Station research status — Apollo 11 landing-radar cadence and display boundary

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is constrained to one LR velocity component during each 2-second Average-G/PIPA interval, cycling `Vz`, `Vx`, `Vy`. Mission-specific MSK-1137 evidence constrains the controller-visible LR field family: GOOD/BAD range/velocity status, body-axis `VXB/VYB/VZB`, slant range, PGNS altitude, display masks, and separately ground-computed `ACT ΔV`.

Apollo 11 ground-system evidence constrains the intervening CCATS/RTCC and Display/Control layers. NASA TN D-8316 establishes buffered dynamic display updates independent of CRT refresh. PHO-FAM001 constrains the generic request transaction, and NASA TN D-7685 constrains Apollo-program display-request/channel-allocation behavior.

PHO-TR515 now supplies a later primary system baseline for field provenance. A DTE format's dynamic groups were specified with source, coordinate, and configuration metadata. The source external name could identify a telemetry measurement or a Data Processing Branch computation, manual-entry datum, or special-logic result. Format metadata could also identify a downlist, with a defined blank case when multiple downlists fed the display. This means a historically reconstructed GUIDO field needs an explicit provenance route; a matching semantic name alone is insufficient.

Because PHO-TR515 is dated 1973, it does not establish Apollo 11 MSK-1137 external names or downlists. Its explicit update-rate field is associated with plot formats and is not used here as a tabular-display cadence.

## Station boundary

`LR physical measurement/error → LGC estimator/update → downlink/telemetry → CCATS/RTCC source/computation/logic → Display/Control dynamic-field formatting → TV-channel allocation/attach → controller-visible field`

Keep field provenance, dynamic-data update, CRT refresh, operator format request, TV-channel allocation, and station-specific controls separate.

## Maturity

No station maturity change. The generic provenance schema is better constrained, but Apollo-11-effective field-source mapping is still required before claiming exact MSK-1137 routing or timing.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule and Apollo 11 MSK-1137 field semantics.
- **DOCUMENTED:** Apollo MCC processing/display separation and buffered D/TV update behavior.
- **DOCUMENTED, APOLLO-PROGRAM EXPERIENCE:** TN D-7685 shared display-resource behavior.
- **DOCUMENTED, LATER SYSTEM BASELINE:** PHO-TR515 dynamic-field source/external-name and downlist metadata model; not Apollo 11 field mapping or tabular cadence.
- **BLOCKED:** direct PHO-TN401 inspection; flight-authentic numerical LR stochastic error generation.
- **UNRESOLVED:** Apollo 11 MSK-1137 external-name/downlist/computation mapping, GUIDO exact request controls and descent selection, and numeric dynamic-data cadence/latency/freshness.
