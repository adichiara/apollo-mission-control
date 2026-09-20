# Station research status — Apollo 11 landing-radar cadence and display boundary

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is constrained to one LR velocity component during each 2-second Average-G/PIPA interval, cycling `Vz`, `Vx`, `Vy`. Mission-specific MSK-1137 evidence constrains the controller-visible LR field family: GOOD/BAD range/velocity status, body-axis `VXB/VYB/VZB`, slant range, PGNS altitude, display masks, and separately ground-computed `ACT ΔV`.

Apollo 11 ground-system evidence constrains the intervening CCATS/RTCC and Display/Control layers. NASA TN D-8316 establishes buffered dynamic display updates independent of CRT refresh. PHO-FAM001 constrains the generic request transaction, and NASA TN D-7685 constrains Apollo-program display-request/channel-allocation behavior.

A renewed inspection of the Apollo-11-effective AC Electronics MSK-1137 format shows explicit `D/L` and `RTCC` source-category labeling on the display itself. Together with the field note identifying `ACT ΔV` as ground computed, this establishes that the controller product mixed spacecraft-downlink and ground/RTCC provenance. It does not establish the per-field routing table.

The Apollo 11 Mission Report now constrains the powered-descent **acceptance workflow** separately from the MCC display path. It states that, once LR data were available, the crew decided whether to incorporate them into PGNS using reasonability and precalculated limits, and verified convergence after incorporation. Because the AGS was not updated by LR, its data would then be in error and were no longer monitored closely. This is a useful player-visible state transition, but the source assigns the incorporation decision to the crew; it does not justify giving GUIDO a historical LR-accept/reject control.

PHO-TR515 remains useful only as a later primary-system baseline for how such provenance was formally represented: dynamic groups had source/external-name and downlist metadata. Its 1973 identifiers and plot update-rate fields are not back-projected into Apollo 11.

## Station boundary

`LR physical measurement/error → LGC estimator/update → crew reasonability/acceptance + convergence state → downlink/telemetry → CCATS/RTCC source/computation/logic → Display/Control dynamic-field formatting → TV-channel allocation/attach → controller-visible field`

Keep spacecraft acceptance, field provenance, dynamic-data update, CRT refresh, operator format request, TV-channel allocation, and station-specific controls separate.

## Maturity

No station maturity change. Mission-specific mixed provenance and the crew LR-acceptance/convergence workflow are now established, but Apollo-11-effective per-field source mapping is still required before claiming exact MSK-1137 routing or timing. GUIDO's historical interaction with the crew acceptance decision remains unresolved.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule and Apollo 11 MSK-1137 field semantics.
- **DOCUMENTED:** Apollo 11 MSK-1137 distinguishes `D/L` and `RTCC` provenance categories; `ACT ΔV` is ground computed.
- **DOCUMENTED:** Apollo 11 Mission Report assigns LR incorporation to the crew based on reasonability/precalculated limits and requires convergence verification after incorporation; AGS was not LR-updated.
- **DOCUMENTED:** Apollo MCC processing/display separation and buffered D/TV update behavior.
- **DOCUMENTED, APOLLO-PROGRAM EXPERIENCE:** TN D-7685 shared display-resource behavior.
- **DOCUMENTED, LATER SYSTEM BASELINE:** PHO-TR515 dynamic-field source/external-name and downlist metadata model; not Apollo 11 field mapping or tabular cadence.
- **BLOCKED:** direct PHO-TN401 inspection; flight-authentic numerical LR stochastic error generation.
- **UNRESOLVED:** per-field Apollo 11 MSK-1137 `D/L`/`RTCC` mapping, external-name/downlist/computation identifiers, GUIDO exact request controls and descent selection, GUIDO's role in the crew LR-acceptance decision, and numeric dynamic-data cadence/latency/freshness.
