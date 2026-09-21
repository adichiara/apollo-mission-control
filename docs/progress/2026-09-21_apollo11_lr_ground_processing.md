# Apollo 11 LR ground-processing provenance — progress

Date: 2026-09-21

## Question

What Apollo-11-specific primary evidence constrains the ground-processing layer between the LGC landing-radar downlink words and controller-visible LR products?

## Primary evidence recovered

TRW Systems Group, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume 1* (16 March 1970; NASA-CR-108349 / TRW-11176-H508-R0-00; NTRS 19700014995) contains a dedicated §7.4, **LANDING RADAR DATA ANALYSIS**.

Section 7.4 states that landing-radar data were obtained by **processing the downlink telemetry data with a special-purpose computer program**, whose output was onboard observations on punched cards in a HOPE-compatible format. HOPE then computed simulated LR observables from selected LM trajectories and auxiliary information including REFSMAT, gimbal angles, and radar operating mode; residuals were formed from computed versus actual observable values.

The same section separately identifies an **RTCC** descent trajectory as a vector obtained in the RTCC in real time. That separation matters: this source does not support collapsing "LR telemetry processing" and "RTCC trajectory generation" into one undocumented step.

## Controlled conclusion

This closes another part of the provenance boundary: Apollo 11 LR observables demonstrably existed as products derived from **downlink telemetry processing**, and the mission's postflight analysis treated those observables separately from an RTCC real-time trajectory product.

It does **not** identify the special-purpose postflight program as the real-time MCC path, and it does not map `DNLRVELX/Y/Z/DNLRALT` to MSK-1137 `VXB/VYB/VZB/RNG`. It therefore cannot justify claiming that RTCC generated, converted, or directly routed the MSK-1137 LR fields. Preserve the real-time telemetry/display routing as unresolved.

## Simulation consequence

Keep the ground model layered:

`LGC LR downlink words → telemetry/engineering processing → controller LR display products`

Do not insert an RTCC transform into the LR display path without mission-effective real-time documentation. RTCC may remain a separate source of trajectory/state products.

## Source

- TRW Systems Group, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume 1*, 16 March 1970, NASA-CR-108349 / TRW-11176-H508-R0-00, NTRS 19700014995, §7.4, especially §7.4.1. https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19700014995.pdf

## Next target

Seek Apollo-11-effective real-time telemetry/FDS/CCATS/display-database documentation giving engineering-unit parameter identifiers or routing for the LR downlink words and MSK-1137 fields. Search specifically for the telemetry measurement definitions underlying `VXB/VYB/VZB/RNG`, rather than assuming RTCC ownership from the display context.

## Evidence status

- **DOCUMENTED, APOLLO-11-SPECIFIC:** postflight LR observables were obtained by processing downlink telemetry with a special-purpose computer program.
- **DOCUMENTED, APOLLO-11-SPECIFIC:** HOPE consumed those observations plus trajectory/attitude/radar-mode inputs for residual analysis.
- **DOCUMENTED, APOLLO-11-SPECIFIC:** an RTCC real-time descent trajectory is described as a separate analysis input/product.
- **UNRESOLVED:** real-time telemetry engineering conversion and per-field routing to MSK-1137.
- **NOT ESTABLISHED:** that RTCC generated or transformed MSK-1137 `VXB/VYB/VZB/RNG`.
