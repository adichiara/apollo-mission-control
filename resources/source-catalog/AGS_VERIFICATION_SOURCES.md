# Abort Guidance System verification / validation sources

Status: **primary verification methodology recovered; exact radar-filter bounds/curves and Apollo 9 configuration crosswalk remain retrieval targets**

## NASA TN D-7990 — Apollo Experience Report: Guidance and Control Systems: Lunar Module Abort Guidance System

- Author: Pat M. Kurten
- Organization: Lyndon B. Johnson Space Center
- Publication: July 1975
- NASA Technical Note: `NASA TN D-7990`
- JSC report: `JSC S-424`
- NTRS document ID: `19750018954`
- NTRS record: https://ntrs.nasa.gov/citations/19750018954
- Public PDF mirror used for page inspection: https://apollojournals.org/alsj/19750018954_tnD7990LM_AGS.pdf

### Verification layers directly supported

The report documents:

- equation testing / closed-loop engineering simulation under nominal and 3σ vehicle, sensor, or trajectory dispersions;
- bit-by-bit interpretive computer simulation (ICS) to verify coded-program implementation against equations;
- closed-loop ICS flight simulator (FS) combining AEA program and vehicle flight characteristics;
- special ICS driver routines;
- 600-cycle Monte Carlo performance analysis against mission requirements;
- independent MSC hybrid-computer testing with actual ASA and DEDA hardware;
- mission-specific six-degree-of-freedom simulation incorporating AGS and other LM flight-control hardware.

### Operational simulated-flight criteria

The report states that simulated-flight procedures tested:

- initialization;
- CSM acquisition;
- radar filter;
- abort from powered descent;
- abort from lunar surface;
- CSI;
- CDH;
- TPI; and
- external delta-V guidance.

Test criteria were derived from interpretive computer simulations and represented as **value bounds or bounded curves** for AEA/display parameters.

This is primary evidence for Apollo-era operational validation using parameter-level criteria rather than only qualitative GO/NO-GO judgments.

### Numerical/cadence boundary

A later simulated-flight discrepancy in the report describes roundoff during transformation of compensated velocity in a **20-millisecond computing cycle**. The report says the buildup was evaluated and found negligible in the dynamic flight environment.

Use: AGS/AEA computing-context evidence only.

Do not use as:

- a global LMS integration timestep;
- a generic Apollo simulator update rate;
- a PC+2 timestep;
- proof that every AGS function updated independently at 20 ms.

### Configuration/effectivity boundary

The report describes a mission-specific software development/release process involving requirements/reference trajectories, verification plans/results, performance analyses, updated constants, readiness reviews, and final program loading.

Therefore criteria should be treated as tied to program/configuration/effectivity unless continuity is explicitly established.

Research record: `resources/research/237_ags_verification_validation_architecture.md`.

## Apollo 9 Mission Report / Supplement 3 crosswalk target

Research note 236 records the flight-derived mismatch: AGS range/range-rate information degraded much faster in flight than in the simulator after radar updates, with flight-side solution variation reported up to approximately ±3 ft/s about the mean.

TN D-7990 establishes that radar-filter simulated-flight tests and bounded parameter criteria existed, but the exact applicable radar-filter bound/curve has not yet been recovered or tied to Apollo 9's simulator configuration.

Required future crosswalk:

`Apollo 9 AGS/software configuration`
→ `preflight radar-filter simulated-flight procedure`
→ `criterion/bounded curve`
→ `simulator result`
→ `Apollo 9 flight result / Supplement 3 postflight analysis`

Do not substitute later generic capability tables or 3σ input dispersions for that missing comparison.
