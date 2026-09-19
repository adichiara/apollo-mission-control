# Progress — Apollo 11 landing-radar cadence and measurement boundary

Date: 2026-09-19

## Completed

Primary Apollo 11 technical documentation constrains powered-flight Average-G/state-vector processing to 2-second PIPA intervals and the LR velocity components to one per interval, cycling `Vz → Vx → Vy → Vz`. This remains an onboard estimator cadence, not an MCC display cadence.

The next unresolved measurement/noise gap was then tested against primary evidence. NASA TN D-6849 provides LM-5-specific history: a preflight one-count velocity bias caused by a logic race was corrected, and the Gaussian assumption used for Doppler-spectrum-simulator test limits had to be corrected because the test approximation produced more energy in the tails. Its Apollo 11 section reports flight data within specification limits except near zero Doppler, but does not provide a numerical flight-effective stochastic distribution.

The result is a useful negative constraint: an arbitrary Gaussian noise generator would be unsupported, and the corrected preflight one-count bias must not be reproduced as an Apollo 11 flight defect. The flight-authentic stochastic generator is **BLOCKED** pending numerical LM-5/Apollo-11-effective evidence.

## Repository consequence

- Roadmap now permits explicitly synthetic perturbations for testing while keeping them out of the historical profile.
- Source catalog and station status distinguish this sensor-model boundary from controller-visible timing.
- No executable behavior or station maturity changes in this research-only slice.

## Next bounded work

1. Implement the already source-controlled measurement-time propagation + beam transform + qualification + weighting composition.
2. Reopen historical stochastic LR generation only on recovery of LM-5/Apollo-11-effective numerical error evidence.
3. Pursue controller-facing timing separately through direct Mission G downlink/telemetry/display documentation.

## Sources

- AC Electronics, *Apollo 11 Guidance and Navigation System Manual*: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA / MSC, *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar*, NASA TN D-6849: https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- MIT/IL E-1982, *LEM PGNCS and Landing Radar Operations During the Powered Lunar Landing Maneuver*: https://www.ibiblio.org/apollo/Documents/E-1982_LEM_PGNCS_and_Landing_Radar_Operations.pdf

## Evidence status

- **DOCUMENTED:** one LR velocity component is used per 2-second Average-G/PIPA navigation interval, cycling `Vz`, `Vx`, `Vy`.
- **DOCUMENTED:** LM-5's preflight one-count velocity bias was corrected and the Doppler-simulator Gaussian test-limit assumption required correction for heavier tails.
- **PARTIALLY DOCUMENTED:** qualitative Apollo 11 LR error boundary near zero Doppler.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical stochastic LR velocity-error distribution.
- **UNRESOLVED:** controller-visible landing-radar/guidance product cadence and formatting.
