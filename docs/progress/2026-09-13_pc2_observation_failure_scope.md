# Progress — PC+2 observation-failure scope

Date: 2026-09-13

## Completed

- Researched open question 14 against primary Apollo/NASA instrumentation and communications sources.
- Added research note 104 defining the first-playable sensor/telemetry failure boundary.
- Added `PC2_OBSERVATION_FAILURE_SOURCES.md`.
- Distinguished source/sensor faults from instrumentation conditioning, telemetry/communications transport, and ground-processing faults.
- Recorded source-supported observation-integrity classes: unavailable measurement, biased/shifted measurement, nuisance/warning-path anomaly, and downstream path/product impairment.
- Determined that the nominal PC+2 first playable does **not** require an additional historical sensor failure.
- Preserved the existing synthetic ΔP branch as a synthetic scenario condition rather than retroactively inventing a failed pressure transducer.
- Prohibited random generic telemetry faults, unsupported failure probabilities, durations, bias/noise distributions, and recovery timing.

## Project consequence

Open question 14 is resolved for the current first playable. The model must support layered observation integrity, but failure modes enter a scenario only when a concrete sourced or explicitly synthetic case needs them.

This does not replace the physical live-play boundary. Seven-seat nominal, synthetic ΔP, and five-player compact human/device validation remain unclosed.
