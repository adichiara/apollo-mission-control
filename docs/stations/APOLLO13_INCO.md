# Apollo 13 INCO Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Instrumentation and Communications Officer from mission-specific evidence and contemporary Apollo communications documentation.

INCO is not a generic “radio operator.” The position sits at the spacecraft/ground data-link boundary and has operational command responsibilities.

---

## 1. Position

**Call sign / position:** INCO  
**Apollo-era title:** Apollo Communications Engineer / Instrumentation and Communications Officer

### Documented responsibility

Apollo Mission Control documentation assigns INCO responsibility for monitoring and troubleshooting CSM/LM communications, television, PLSS/erectable-antenna communications where applicable, and communications-system commands. O&P / PROCEDURES shared the console/responsibility area but had a separate procedural/ground-interface function.

---

# 2. Communications state is multidimensional

Contemporary Apollo communications documentation shows that INCO did not work from a single “signal quality” value. Operational cues included digital and metered uplink/downlink strength, telemetry dropouts, voice-subcarrier noise, spacecraft antenna look angle, site acquisition/two-way-lock status, telemetry bitrate, command-uplink margin, and spacecraft antenna configuration.

A faithful station therefore needs separate physical/data-link state variables rather than a single connection meter.

---

# 3. PTC antenna management

During passive thermal control (PTC), the spacecraft continually rotated relative to Earth.

The contemporary paper *Telemetry and Communications to Apollo Flight Controllers* describes INCO managing CSM omnidirectional antennas during PTC. As the active omni rotated out of Earth view, INCO monitored signal/telemetry, could change telemetry rate, and sent antenna-switch commands before uplink capability was lost. Temporary communications loss could occur during the transition.

### Simulation significance

A command can fail because antenna geometry is poor, uplink margin is insufficient, the site has lost two-way lock, a subcarrier has been removed, or bitrate/mode is incompatible with current margins. That is an operational dependency, not a random command-failure mechanic.

---

# 4. Signal-strength information

The same paper identifies digital uplink signal strength, calibrated uplink/downlink console meters, telemetry dropouts, voice noise, and spacecraft-antenna look-angle presentation as distinct INCO cues. The look-angle product combined telemetered attitude with MCC calculations, making communications performance partly a geometry/navigation problem as well as an RF problem.

---

# 5. Apollo 13 LM Look Angle Display

Apollo 13 provides a specific mission-era display identifier: **LM Look Angle Display — MSK 1475**. The INCO post-mission report states that it failed to meet prior requirements because it did not operate with LM low-bit-rate telemetry. The deficiency had been found in simulations and accepted for Apollo 13 rather than prompting major RTCC reprogramming.

For an Apollo 13 profile, MSK 1475 must not silently behave like a corrected post-Apollo-13 system.

---

# 6. CLAD / LAD RTCC dependence

The Apollo 13 INCO report says manual MED inputs to communications look-angle displays identified as **CLAD** and **LAD** had to be made by “Computer Dynamics” personnel in the RTCC area. Communications SSR coordinated these inputs on the RTCC Dynamics loop, also used by FIDO. The exact expansion/name of CLAD remains unresolved; LAD is explicitly identified as the LM Look Angle Display.

---

# 7. Apollo 13 command-uplink anomaly during PTC

Apollo 13 INCO documented a routine antenna command that did not get through as expected, involving impending loss of two-way lock, site handling of the 70-kHz command subcarrier, limited command margin, and antenna-switch timing. After two-way lock was lost, Madrid removed the command subcarrier to reacquire the spacecraft; INCO then needed a command-only uplink mode with better margin.

A future simulation may therefore need active station, uplink carrier/subcarrier state, two-way lock, command margin, bitrate, antenna geometry, and site procedure where a sourced scenario depends on them.

---

# 8. High Gain Antenna anomaly

Apollo 13 experienced an early CSM high-gain antenna acquisition anomaly. Ground-predicted look angles, crew checks of electronics/modes/breakers/indications, spacecraft attitude, acquisition/lock state, and signal strength all contributed to diagnosis. The antenna later acquired during a maneuver toward PTC attitude.

---

# 9. Low-power communications configuration

After the oxygen-tank accident, communications configuration was deliberately changed to reduce electrical load, coupling communications quality/telemetry capability to spacecraft power consumption and making EECOM/TELMU–INCO coordination meaningful.

---

# 10. S-IVB / LM downlink interference

Apollo 13 encountered interference between S-IVB Instrument Unit and LM downlinks. Frequency-offset procedures affected RTCC tracking-data usability, establishing a concrete communications-configuration → tracking-quality → RTCC/FIDO dependency.

---

# 11. Entry communications anomaly

During CSM reactivation near entry, weak S-band indications were initially suspected as an equipment problem. Postflight analysis instead attributed attenuation to docked-LM geometry. This reinforces that weak signal does not itself diagnose a failed radio.

---

# 12. Data retrieval / DSE

The CSM Data Storage Equipment could record information for later dump to selected S-band stations by INCO-executed commands. O&P/PROCEDURES also had playback scheduling/direction responsibilities, so the exact workflow crossed positions.

---

# 13. Commands and verification

Apollo 13’s INCO post-mission critique indicates that command execution required real-time monitoring to verify command receipt and that poor simulator behavior sometimes forced unrealistic repeats. Command execution should therefore distinguish request/preparation, ground-path availability, transmission, spacecraft receipt/decode, and observed acknowledgement/state change.

---

# 14. INCO information families justified by evidence

These include spacecraft communications hardware state, link state, antenna/spacecraft geometry, command-path state, recorded-data state, and television configuration where relevant to a sourced scenario.

---

# 15. INCO versus NETWORK versus PROCEDURES

**INCO:** spacecraft-side communications/instrumentation behavior and communications-system commands.  
**NETWORK:** MSFN network status, sites, and MCC/network operational availability.  
**PROCEDURES / O&P:** detailed MCC/MSFN/GSFC/KSC interface procedures, playback scheduling, and ground-support-timeline communications changes.

Do not merge them conceptually before player-count simplification is studied.

---

# 16. Simulator-training evidence

INCO’s Apollo 13 post-mission report criticizes communications simulations for incorrectly represented dependent channels, long gaps, wrong mission/month data, and unrealistic command execution. It explicitly describes such errors as negative training. Failure injection must therefore operate through subsystem dependencies, not independent scripted symptoms.

---

# 17. Implementation status

## DOCUMENTED for Apollo 13

- role and communications-command responsibility
- signal-strength and antenna-management task
- command-uplink timing/margin behavior
- HGA acquisition anomaly
- LM Look Angle Display MSK 1475 and low-bit-rate deficiency
- CLAD/LAD dependency on RTCC Computer Dynamics
- low-power communications configuration
- S-IVB/LM interference
- entry geometry/attenuation anomaly
- DSE data-retrieval command role
- simulation-training deficiencies

## PARTIAL / UNRESOLVED

Exact display structures, console layout, complete DRK/MSK assignments, CLAD title/number, signal-strength scales, voice-loop selections, complete command repertoire, and detailed CCATS/MSFN handoffs remain research questions.

---

# 18. Research targets

1. Locate Apollo 13 communications display-format specifications, especially MSK 1475.
2. Identify CLAD exact title and display number.
3. Locate INCO console handbook / DRK and MSK assignments.
4. Extract command-system workflow from AS-508 MCC/MSFN configuration.
5. Identify CCATS/remote-site command acknowledgements available to INCO.
6. Map CSM/LM communications telemetry parameter codes.
7. Reconstruct PTC antenna-switching state machine from spacecraft antenna patterns and MSFN geometry.
8. Locate the high-speed-printer command-verification product.

## Primary / contemporary sources

1. Apollo 13 Mission Operations Report, Appendix I — INCO.
2. AS-508 MCC/MSFN Mission Configuration/System Description, March 1970.
3. Alan Glines and Joseph A. Lazzaro, *Telemetry and Communications to Apollo Flight Controllers*, International Telemetering Conference, 1970; NTRS 19710030221: https://ntrs.nasa.gov/citations/19710030221
4. Apollo 13 Technical Air-to-Ground Voice Transcript.
