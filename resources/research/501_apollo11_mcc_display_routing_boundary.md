# Apollo 11 MCC display-routing boundary

Date: 2026-09-19  
Status: **REVIEWED — architecture controlled; field-level routing/cadence unresolved**

## Question

What can primary NASA sources establish about the path between Apollo 11 spacecraft telemetry and the controller-visible MSK-1137 landing-radar fields, without inventing an exact CRT refresh rate or unsupported field transformation?

## Primary-source result

### Apollo 11 Mission Operation Report — M-932-69-11

The mission-specific Mission Operation Report describes MCC mission support as an integrated set of distinct systems: the Communications, Command, and Telemetry System (CCATS), Real-Time Computer Complex (RTCC), Voice Communications System, Display/Control System, and the MOCR/SSR flight-control organization. It states that spacecraft telemetry and operational data are received and can be processed by CCATS and RTCC for flight-control evaluation.

This establishes an Apollo-11-effective architectural boundary: a controller CRT product is not evidence of a direct read from LGC state. Spacecraft/downlink data, ground receipt/processing, and controller presentation must remain separate simulator layers.

Source: NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11, Mission Support section.

### Apollo Experience Report — Real-Time Display System

NASA TN D-8316 / JSC-S-461 retrospectively describes the Apollo real-time display system as separate subsystems serving distinct requirements, including a computer-input multiplexer, plotting-display subsystem, digital-display subsystem, and digital-television subsystem.

This independently supports the separation between ground-computer output and controller presentation. Because the report is Apollo-program retrospective rather than an Apollo-11 MSK-1137 field-routing specification, it is not used to assign an exact Apollo 11 landing-radar field path or refresh cadence.

Source: C. J. Sullivan and L. W. Burbank, *Apollo Experience Report: Real-Time Display System*, NASA-TN-D-8316 / JSC-S-461, 1976, NTRS 19760024152.

### Mission-specific MSK-1137 definition

The already controlled AC Electronics Apollo 11 guidance/navigation summary defines the landing-radar field identities, coordinate frame, engineering units, display masks, GOOD/BAD status fields, and the ground-computed identity of `ACT ΔV`. It does not identify the complete CCATS/RTCC program chain, per-field request/key workflow, or refresh timing.

## Implementation consequence

The Apollo 11 controller-product model may now treat this layer ordering as source-controlled:

`spacecraft/onboard quantity → downlink/telemetry → CCATS/RTCC ground processing → Display/Control System → controller-visible field`

The model must not collapse those stages merely because the final MSK-1137 field definition is known.

For implementation, retain independent provenance/timestamps for source/sample, ground receipt/processing, and display projection. A zero-delay or caller-selected cadence may be used only when explicitly labeled as a simulation simplification; it is not an Apollo 11 historical timing claim.

## What remains unresolved

No reviewed primary source in this pass establishes:

- the exact Apollo 11 CCATS/RTCC transformation or routing for each MSK-1137 landing-radar field;
- a numeric CRT refresh period for MSK-1137;
- end-to-end telemetry-to-display latency;
- a source-backed stale/freshness threshold for these fields; or
- the exact GUIDO request/key workflow used to summon or refresh this display.

The documented 2-second LGC landing-radar component-update schedule remains onboard estimator timing only and must not be reused as the CRT refresh period.

## Research stop condition

Do not infer field-level timing from the architecture documents. Re-open exact timing/routing when a mission-era Apollo MCC Display/Control, RTCC program, CCATS, console/display handbook, or controller procedure directly identifies MSK-1137 routing, update behavior, or request semantics.

## Sources

- NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11, Mission Support. https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionOpReport.pdf
- C. J. Sullivan and L. W. Burbank, *Apollo Experience Report: Real-Time Display System*, NASA-TN-D-8316 / JSC-S-461, NTRS 19760024152. https://ntrs.nasa.gov/citations/19760024152
- AC Electronics, *Apollo 11 Guidance and Navigation System Manual*, ASPO 45 CRT display definitions. https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf

## Evidence status

- **DOCUMENTED:** Apollo 11 MCC separates CCATS, RTCC, Display/Control, and MOCR/SSR functions; telemetry/operational data can be processed by CCATS/RTCC for flight-control use.
- **DOCUMENTED:** Apollo real-time display architecture uses distinct input/display subsystems rather than direct authoritative-state presentation.
- **DOCUMENTED:** Apollo 11 MSK-1137 landing-radar field semantics/formatting at the previously recorded level.
- **UNRESOLVED:** exact per-field Apollo 11 CCATS/RTCC routing and transformation.
- **UNRESOLVED:** exact CRT refresh cadence, end-to-end latency, freshness policy, and request/key workflow.
- **NOT PERMITTED:** substituting the onboard 2-second LGC component cadence for controller-display cadence.