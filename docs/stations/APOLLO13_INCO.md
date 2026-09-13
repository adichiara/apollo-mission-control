# Apollo 13 INCO Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Instrumentation and Communications Officer from mission-specific evidence and contemporary Apollo communications documentation.

INCO is not a generic “radio operator.” The position sits at the spacecraft/ground data-link boundary and has operational command responsibilities.

---

## 1. Position

**Call sign / position:** INCO  
**Apollo-era title:** Apollo Communications Engineer / Instrumentation and Communications Officer

### Documented responsibility

Apollo Mission Control documentation assigns INCO responsibility for monitoring and troubleshooting:

- CSM communications
- LM communications
- television
- PLSS communications where applicable
- erectable-antenna communications where applicable

INCO was also responsible for execution of commands associated with communications systems.

O&P / PROCEDURES shared the console/responsibility area but had a separate procedural/ground-interface function.

---

# 2. Communications state is multidimensional

Contemporary Apollo communications documentation shows that INCO did not work from a single “signal quality” value.

Operational cues included:

- digital uplink signal strength on a spacecraft telemetry TV display;
- calibrated uplink signal-strength meter;
- calibrated downlink signal-strength meter;
- telemetry dropouts;
- voice-subcarrier noise;
- spacecraft antenna look-angle display;
- site acquisition / two-way-lock status;
- high-bit-rate versus low-bit-rate telemetry mode;
- command-uplink margin;
- spacecraft antenna configuration.

A faithful station therefore needs separate physical/data-link state variables rather than a single connection meter.

---

# 3. PTC antenna management

During passive thermal control (PTC), the spacecraft continually rotated relative to Earth.

The contemporary paper *Telemetry and Communications to Apollo* describes INCO managing CSM omnidirectional antennas during PTC.

## Routine sequence

As the active omni rotated out of Earth view:

1. uplink/downlink signal decreased;
2. INCO watched signal strength and telemetry quality;
3. high-bit-rate telemetry could be changed to low-bit-rate before margins became too small;
4. just before command-uplink capability would be lost, INCO sent the antenna-switch command through the still-active antenna;
5. communications could disappear temporarily during the transition;
6. the newly visible antenna reacquired the link.

At lunar distance, loss of communications for one or two minutes during such antenna switching could occur.

### Simulation significance

A command can fail not because the command logic is wrong, but because:

- antenna geometry is poor;
- uplink margin is insufficient;
- the site has already lost two-way lock;
- a subcarrier has been removed;
- bitrate/mode is incompatible with current margins.

That is a genuine operational problem, not a random command-failure mechanic.

---

# 4. Signal-strength information

The contemporary communications paper identifies several distinct INCO cues.

## Digital telemetry value

Uplink signal strength was displayed digitally on the spacecraft telemetry TV display.

## Console meters

Uplink and downlink signal strengths from the active 85-foot site were available on calibrated percent-full-scale meters at the console.

## Telemetry data quality

As received strength fell, data dropouts appeared on the telemetry display.

## Voice cue

Noise on the voice subcarrier provided an additional subjective cue.

## Look-angle display

The spacecraft-antenna look-angle D/TV display used telemetered spacecraft attitude and MCC calculations to show antenna geometry relative to the active MSFN site.

The source describes both digital and graphical look-angle presentation, updated by MCC calculations.

This makes communications performance partly a geometry/navigation problem as well as an RF systems problem.

---

# 5. Apollo 13 LM Look Angle Display

Apollo 13 provides a specific mission-era display identifier:

**LM Look Angle Display — MSK 1475**

The INCO post-mission report states that this display failed to meet prior requirements.

## Documented deficiency

The LM Look Angle Display did not operate when the LM was transmitting low-bit-rate telemetry.

Apollo 13 spent much of the contingency with the LM active in low-bit-rate mode, so the deficiency compromised communications operations.

The issue had been discovered during simulations before flight.

Rather than undertake major RTCC reprogramming before Apollo 13, the deficiency was accepted for the mission.

INCO recommended correcting the display before Apollo 14.

### Simulation-profile significance

This is exactly the kind of historically documented defect the mission-profile system should preserve.

For an Apollo 13 profile:

> MSK 1475 should not silently behave as the corrected post-Apollo-13 system would when only LM low-bit-rate data are available.

This is a stronger fidelity target than merely reproducing the display’s visual appearance.

---

# 6. CLAD / LAD RTCC dependence

The Apollo 13 INCO report says manual MED inputs to the communications look-angle displays identified as **CLAD** and **LAD** had to be made by “Computer Dynamics” personnel in the RTCC area.

Communications SSR personnel had to coordinate these inputs on the RTCC Dynamics loop.

FIDO also used that loop, producing documented coordination difficulty.

### What is established

- the look-angle displays depended partly on RTCC/computer-dynamics processing;
- Communications SSR did not independently control every required input;
- the data/product workflow crossed organizational boundaries;
- communication-display support could be delayed by loop/access contention.

### Unresolved

The exact expansion/name of CLAD should not be guessed until a primary source establishes it.

LAD is explicitly identified in the mission report as the LM Look Angle Display.

---

# 7. Apollo 13 command-uplink anomaly during PTC

Apollo 13 INCO documented a case where a routine antenna command did not get through as expected.

Operational factors included:

- impending loss of two-way lock;
- site handling of the 70-kHz command subcarrier;
- limited command margin;
- antenna switching timing.

After two-way lock was lost, Madrid removed the command subcarrier to reacquire the spacecraft.

INCO then needed a command-only uplink mode with better margin to complete the command.

The post-mission report notes that some other sites delayed removing the uplink after two-way-lock loss, which sometimes gave INCO another opportunity to get a command into the spacecraft.

INCO recommended formalizing such behavior in a Network Operations Directive.

### Simulation significance

The ground network is part of INCO’s playable environment.

A future simulation may need to represent:

- active station;
- uplink carrier/subcarrier state;
- two-way lock;
- command margin;
- bitrate;
- antenna geometry;
- site procedure.

Exactly how much of that is surfaced to the player remains a later design decision.

---

# 8. High Gain Antenna anomaly

Apollo 13 experienced an early CSM high-gain antenna acquisition anomaly.

The ground supplied predicted HGA pitch/yaw angles.

The crew checked:

- primary and secondary HGA electronics;
- AUTO and REACQ modes;
- circuit breakers;
- onboard angle indications.

The antenna would not initially achieve narrow-beam lock.

During a maneuver toward the PTC attitude it subsequently acquired and operated normally.

### Station information implied

INCO needs some representation of:

- predicted look angles;
- antenna pitch/yaw;
- track mode;
- acquisition/lock state;
- beam state;
- signal strength;
- spacecraft attitude/geometry.

The exact Apollo 13 CRT used for this work remains unresolved.

---

# 9. Low-power communications configuration

After the CSM oxygen-tank accident, communications configuration was changed to reduce electrical load.

The INCO report documents deliberate power/communications tradeoffs involving equipment such as:

- S-band power amplifier modes;
- telemetry bitrate;
- tape/DSE functions;
- VHF;
- antenna equipment.

Communications quality, telemetry capability and spacecraft power consumption were therefore coupled.

This makes EECOM/TELMU–INCO coordination historically meaningful.

---

# 10. S-IVB / LM downlink interference

Apollo 13 encountered interference between the S-IVB Instrument Unit and LM downlinks.

One procedure separated their frequencies by offsets.

That improved communications separation but caused RTCC to consider some LM tracking data unusable.

A revised approach changed which vehicle was offset.

Postflight analysis concluded that RTCC could manually correct for the frequency offset.

### Simulation significance

A communications configuration can affect another discipline’s data quality.

This is a concrete INCO/FIDO/BOOSTER/RTCC interaction:

```text
communications frequency configuration
        ↓
tracking-data usability
        ↓
RTCC trajectory input
        ↓
FIDO state quality
```

The project should preserve such cross-discipline effects where a documented scenario uses them.

---

# 11. Entry communications anomaly

During CSM reactivation near entry, Mission Control initially suspected the S-band power amplifier was not operating because signal strength and electrical-current indications did not match expectations.

The LM Look Angle Display showed geometry placing the LM roughly along the ground-to-CM line.

Postflight analysis concluded that the docked LM structure was attenuating the CSM antenna path.

### Simulation lesson

Again:

> weak signal ≠ failed radio.

INCO must reason from:

- spacecraft configuration;
- antenna geometry;
- expected gain;
- measured strength;
- power state;
- bitrate/lock behavior.

---

# 12. Data retrieval / DSE

The CSM Data Storage Equipment could record information during periods when live downlink was unavailable or undesirable.

Contemporary documentation states that recorded information was later dumped to selected S-band stations by **INCO-executed commands**.

Therefore INCO’s job includes data recovery, not only live communications.

O&P/PROCEDURES also had responsibility for scheduling/direction of telemetry and DSE voice playbacks, so exact workflow crosses positions.

---

# 13. Commands and verification

Apollo 13’s INCO post-mission critique of simulations contains a particularly useful operational detail.

The report says INCO command execution apparently required **real-time monitoring via high-speed printer** to verify that commands were properly received by the CMS, LMS or simulation/math model.

Poor simulation behavior sometimes forced controllers to repeat commands an unrealistic number of times.

### Simulation significance

Command execution should eventually distinguish:

1. command requested/prepared;
2. ground path available;
3. command transmitted;
4. spacecraft receives/decodes it;
5. acknowledgement/state change is observed.

Do not collapse these into a generic button whose success is instant and certain.

---

# 14. INCO information families justified by evidence

## Spacecraft communications hardware

- CSM/LM transponder state
- power amplifier state/mode
- S-band configuration
- VHF transmitter/receiver state
- high-gain/steerable antenna state
- omni antenna selection
- track/acquisition mode

## Link state

- uplink signal strength
- downlink signal strength
- telemetry bitrate
- telemetry dropouts/quality
- two-way lock
- voice mode / quality
- command-uplink margin
- active MSFN station

## Geometry

- spacecraft attitude
- active antenna
- antenna look angle
- HGA/steerable antenna pitch/yaw
- antenna gain/obstruction effects where applicable

## Command path

- uplink subcarrier/mode
- command transmission
- receipt/verification
- site/CCATS/RTCC dependencies

## Recorded data

- DSE record/playback/dump state
- playback schedule/availability

## Television

- TV downlink/transmitter configuration
- interaction between TV/FM modes and other communications functions

---

# 15. INCO versus NETWORK versus PROCEDURES

## INCO

Spacecraft-side communications/instrumentation behavior and communication-system commands.

## NETWORK

MSFN network status, sites and MCC/network operational availability.

## PROCEDURES / O&P

Detailed MCC/MSFN/GSFC/KSC interface procedures, playback scheduling, and ground-support-timeline communications changes.

Real operational problems cross all three positions.

Do not merge them conceptually before player-count simplification is studied.

---

# 16. Simulator-training evidence

INCO’s Apollo 13 post-mission report criticizes communications simulations for:

- incorrectly simulating complete USB downlink failures while leaving crew downlink voice unaffected;
- long gaps between simulations;
- using the wrong mission/month data;
- unrealistic command execution requiring excessive repeats.

The report states that such errors gave INCO **negative training** and reduced Flight Director confidence.

This is direct evidence for the project’s simulator philosophy:

> A malfunction scenario must preserve the actual dependencies of the communications system. A failure labeled “USB downlink failure” cannot selectively leave dependent channels working simply because that is convenient for scenario scripting.

---

# 17. Implementation status

## DOCUMENTED for Apollo 13

- role and communications-command responsibility
- signal-strength and antenna-management task
- command-uplink timing/margin behavior
- HGA acquisition anomaly
- LM Look Angle Display MSK 1475
- low-bit-rate deficiency of MSK 1475
- CLAD/LAD dependency on RTCC Computer Dynamics
- low-power communications configuration
- S-IVB/LM downlink interference
- entry geometry/attenuation anomaly
- DSE data-retrieval command role
- simulation-training deficiencies

## PARTIAL

- exact structure of communications TV displays
- console meter configuration
- exact command verification/high-speed-printer workflow
- command handoff among INCO/CCATS/MSFN/site/spacecraft

## UNRESOLVED

- exact Apollo 13 INCO console physical layout
- complete INCO DRK/MSK assignments
- exact CLAD display name/number
- exact LAD screen layout
- other INCO display numbers
- exact signal-strength meter scales
- precise voice-loop selections
- complete command repertoire available from INCO
- communications SSR console/data-product details

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
3. R. W. Winkelman et al., *Telemetry and Communications to Apollo*, 1970.
4. Apollo 13 Technical Air-to-Ground Voice Transcript.

## Mission-report evidence

- LM Look Angle Display MSK 1475 deficiency
- RTCC CLAD/LAD interface deficiency
- command-uplink/network timing anomaly
- HGA anomaly
- low-power configuration
- S-IVB/LM interference
- entry communications anomaly
- simulation critique
