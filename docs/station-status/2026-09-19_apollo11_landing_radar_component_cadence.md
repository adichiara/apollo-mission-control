# Station research status — Apollo 11 landing-radar cadence and display boundary

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is constrained to one LR velocity component during each 2-second Average-G/PIPA interval, cycling `Vz`, `Vx`, `Vy`. Mission-specific MSK-1137 evidence constrains the controller-visible LR field family: GOOD/BAD range/velocity status, body-axis `VXB/VYB/VZB`, slant range, PGNS altitude, display masks, and separately ground-computed `ACT ΔV`.

Apollo 11 ground-system evidence constrains the intervening CCATS/RTCC and Display/Control layers. NASA TN D-8316 establishes buffered dynamic display updates independent of CRT refresh and separates reference-slide access from dynamic-word update.

Philco `PHO-FAM001` (30 Jun 1967) provides a direct pre-Apollo-11 MCC baseline for the request interaction: Display/Control request keyboards/encoders could select up to 384 stored displays, and a request consisted of selecting the desired display and then the desired display device. This supports a generic request transaction, not a GUIDO-specific control layout.

NASA TN D-7685 adds Apollo-program flight-control experience for what happened after a display request. Lunar-landing missions used a 36-channel computer-driven TV pool. In display-request mode the computer generated/formatted the requested display, assigned the next available channel, and automatically connected that channel to the requesting console on a first-come/first-served basis. In channel-attach mode a console received an already active channel. A channel-usage display identified each channel's format and requesting console so channels could be released when needed. This constrains shared display-resource behavior but not Apollo 11 GUIDO's button legends, MSK-1137 request key, or display-data refresh rate.

A primary Apollo 12 flight manual provides adjacent-effectivity evidence that a DRK could request a specific RTCC display format directly by labeled PBI and had the same capability as MSK display-request mode except that DRK callup avoided thumbwheel selection. Neither source establishes which Apollo 11 GUIDO buttons mapped to MSK-1137 or when the descent display was selected.

## Station boundary

`LR physical measurement/error → LGC estimator/update → downlink/telemetry → CCATS/RTCC ground processing → Display/Control format generation/dynamic-word update → TV-channel allocation/attach → controller-visible field`

Keep display content, display-data update, CRT refresh, operator format request, TV-channel allocation/attach/release, and station-specific button mapping as separate concepts. Do not expose a specific DRK/MSK control map on Apollo 11 GUIDO until mission-effective evidence supports it.

## Maturity

No station maturity change. Generic request and channel-allocation behavior is substantially better constrained, but Apollo-11-effective evidence is still required before implementing GUIDO's exact controls or powered-descent display-selection workflow.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting at the recorded level.
- **DOCUMENTED:** Apollo MCC separates CCATS/RTCC processing from Display/Control/controller operations.
- **DOCUMENTED:** D/TV dynamic updates were buffered and independent of CRT refresh requirements; the four-second TN D-8316 figure concerns reference-slide access.
- **DOCUMENTED, APOLLO-PROGRAM EXPERIENCE:** TN D-7685 defines the lunar-landing 36-channel computer-driven TV pool, first-come/first-served display-request allocation, automatic monitor connection, channel attach, and channel-usage/release mechanism.
- **DOCUMENTED, PRE-APOLLO-11 BASELINE:** PHO-FAM001 defines the generic display/device request transaction and up-to-384-display keyboard/encoder capability.
- **DOCUMENTED, ADJACENT EFFECTIVITY:** Apollo 12 flight manual defines DRK direct-PBI request behavior and equivalence to MSK display-request mode.
- **DOCUMENTED:** PHO-TN401 identity and physical archival location.
- **BLOCKED:** direct PHO-TN401 inspection; flight-authentic numerical LR stochastic error generation.
- **UNRESOLVED:** Apollo 11 GUIDO DRK/MSK equipment, exact button/format mapping and powered-descent selection, exact per-field CCATS/RTCC routing/transformation, and numeric dynamic-data cadence/latency/freshness.
