# Apollo 13 FIDO Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Flight Dynamics Officer from mission-specific real-time operations evidence.

FIDO owns the ground trajectory solution and trajectory-data quality. This position is distinct from GUIDO, GNC, and RETRO.

---

## 1. Position

**Call sign / position:** FIDO  
**Apollo 13 Mission Operations Report:** Flight Dynamics Officer

### Documented responsibility

Apollo Mission Control documentation assigns FIDO responsibility for:

- powered-flight trajectory monitoring;
- mission-feasibility assessment from the trajectory standpoint;
- reentry trajectory monitoring;
- impact-point updates;
- trajectory support during launch, translunar, lunar, transearth, and entry phases.

The Apollo 13 postflight report shows that FIDO's work was not "read current position from a screen." It involved deciding which tracking data and which RTCC trajectory representation were trustworthy.

---

# 2. Tracking-data quality is part of the job

Apollo 13 provides several direct examples.

## Prelaunch / launch

During the T-5 hour trajectory run:

- VAN produced no valid data because of a CDP problem.
- A separate ALDS-interface problem was traced to a procedure/workaround used for simulation support.

At launch:

- VAN still could not send high-speed data to Houston.
- During the States pass, TEX tracking data was rejected because of a header-coding error.

### Simulation significance

FIDO must eventually distinguish:

- data unavailable;
- data received but invalid;
- data received but questionable;
- data accepted for trajectory processing.

A player should not receive a single perfect state vector whenever the spacecraft physically exists.

---

# 3. RTCC ephemeris / model state matters

During the early translunar phase, a sequence of operations accidentally re-anchored the RTCC ephemeris on a pre-TLI vector and also re-enabled a pre-TLI vent model.

That incorrect model state later contaminated impact-point comparisons.

FIDO eventually corrected the ephemeris by deleting the bad TLI event and re-anchoring on the intended post-TLI vector.

### Simulation significance

The ground trajectory solution has its own state.

A trajectory error can originate in:

- tracking data;
- event/model inputs;
- wrong vector selection;
- incorrect RTCC configuration.

This is distinct from any actual spacecraft navigation error.

---

# 4. Multiple competing vectors

Apollo 13 repeatedly used several independent trajectory/vector sources.

The FIDO report documents:

- IU vectors;
- CMC vectors;
- high-speed cutoff vectors;
- Select-generated tracking vectors;
- MSFC estimates;
- RTCC ephemeris vectors.

Example after TLI:

- IU vector available;
- CMC vector available;
- high-speed trajectory source available;
- residual comparisons were used to decide which best represented TLI cutoff;
- the chosen vector then became the ephemeris reference.

The report preserves vector identifiers such as:

- ICHU01 / ICHU06 / ICHU08
- CCHU08
- BDAX36
- LLHU01
- GWMX53
- MILX99
- GWMX307

These identifiers are operational evidence and should be retained in research data rather than replaced by generic labels.

### Station requirement

FIDO eventually needs the ability to compare:

- vector source;
- time tag;
- residuals / fit quality;
- maneuver prediction from each vector;
- current RTCC ephemeris reference.

---

# 5. Tracking anomalies can mimic physical maneuvers

The Apollo 13 FIDO report records unexplained tracking "glitches."

One event produced a pre/post vector difference of several feet per second.

The team considered whether the difference represented:

- a real vehicle event / vent;
- bad tracking;
- another data-processing issue.

This is a recurring Apollo pattern:

> trajectory change in the ground solution does not automatically equal real spacecraft ΔV.

The simulation should preserve that ambiguity.

---

# 6. CSM / LM / IU tracking interference

After the accident, the LM was powered up while the S-IVB Instrument Unit remained active.

Because of communications/frequency conflicts, valid LM tracking data could not initially be obtained at the same time as IU data.

A premission contingency plan was used with modifications.

The FIDO report states it took roughly **four hours** to obtain satisfactory LM tracking data.

### Cross-discipline consequence

This links:

- INCO communications configuration;
- NETWORK/MSFN site behavior;
- RTCC tracking-data processing;
- FIDO trajectory confidence.

The FIDO client therefore should not own communications controls, but it must be able to experience their trajectory-data consequences.

---

# 7. Modeling small nongravitational effects

During transearth coast, the LM supercritical-helium vent disturbed spacecraft attitude.

FIDO observed little immediate Doppler-residual effect.

Later a small equivalent maneuver was inserted into the Mission Planning Table to model the vent and improve trajectory processing.

### Simulation significance

The ground model may need explicit non-impulsive effects or equivalent modeled maneuvers when real spacecraft behavior does not fit the nominal propagation model.

---

# 8. Entry vector selection

Near entry, the final entry PAD was generated from a specific post-MCC-7 vector:

**GWMX307**

The vector used only data collected after MCC-7 and indicated an entry flight-path angle around -6.2 degrees.

Tracking was interrupted before LM separation, so the final entry solution was based on the last accepted data plus the known CM/LM separation maneuver.

### Station implication

FIDO's entry workload includes:

- deciding the acceptable tracking arc;
- selecting the trajectory vector;
- accounting for executed separation/midcourse maneuvers;
- monitoring entry flight-path angle trends;
- handing the accepted trajectory to RETRO/GUIDO/entry processing.

---

# 9. Information families justified by Apollo 13 evidence

## Tracking inputs

- station/source
- data availability
- data acceptance/rejection
- residuals
- time tag
- known site/data-quality problems

## Trajectory vectors

- vector identifier
- vehicle represented
- source type
- epoch
- position/velocity
- fit/residual quality
- vector comparison

## RTCC model/configuration

- active ephemeris anchor
- maneuver/event history
- vent/mass/propulsion model inputs
- spacecraft/launch-vehicle vehicle identity
- accepted maneuver updates

## Derived trajectory products

- perigee/apogee
- free-return status
- lunar/flyby geometry
- impact point
- entry flight-path angle
- predicted landing point
- maneuver ΔV / TIG / burn consequences

Exact CRT pages and display numbers remain unresolved.

---

# 10. FIDO versus GUIDO versus RETRO

## FIDO

Answers:

- What trajectory does the ground solution say we are on?
- Which data/vector should we trust?
- What will this maneuver do to the trajectory?
- Where/when will the vehicle arrive or impact?

## GUIDO

Answers:

- What does the onboard computer know?
- Is its state/alignment valid?
- What onboard update should be loaded?

## RETRO

Answers:

- Given the accepted trajectory and mission constraints, what return/reentry plan should be maintained?
- What abort/return opportunity, landing area, entry target and backup plan are appropriate?

This separation is a core architecture requirement.

---

# 11. Implementation status

## DOCUMENTED

- tracking-data quality responsibility
- use of multiple competing vectors
- RTCC ephemeris/model state
- vector selection and comparison
- tracking/communications interference
- trajectory-model correction
- entry-vector selection
- impact/trajectory monitoring

## PARTIAL

- exact data products passed between Selects/RTCC/FIDO
- exact maneuver-planning displays
- FIDO interaction with FDS/SSR support

## UNRESOLVED

- exact Apollo 13 FIDO console layout
- exact display IDs / MSK assignments
- DRK/MSK controls
- exact tracking-data-selection display
- exact vector comparison display
- exact Mission Planning Table interface
- voice-loop selection

---

# 12. Research targets

1. Locate Apollo 13 Flight Dynamics CRT/display-format documentation.
2. Identify Selects/FIDO/RTCC tracking-data selection displays.
3. Identify Mission Planning Table displays used by FIDO.
4. Locate FIDO console handbook.
5. Map vector identifiers and RTCC naming conventions.
6. Reconstruct FIDO SSR/backroom products.

## Primary source

- *Mission Operations Report — Apollo 13*, Appendix C: Flight Dynamics Officer.
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
