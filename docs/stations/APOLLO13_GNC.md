# Apollo 13 CSM GNC Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Command/Service Module Guidance, Navigation & Control systems controller from mission-specific evidence without assuming undocumented display or console details.

This position is distinct from GUIDO.

---

## 1. Position

**Call sign / position:** GNC  
**Apollo 13 Mission Operations Report:** CSM Guidance and Navigation Officer

### Documented responsibility

Apollo MCC organizational documentation assigns CSM GNC responsibility for monitoring and troubleshooting CSM:

- guidance/navigation/control hardware
- stabilization/control hardware
- reaction control
- service propulsion

The operational record shows that GNC's real-time work centered heavily on the *hardware and propulsion/control-system state* that made spacecraft attitude and maneuvering possible.

GUIDO, by contrast, handled onboard guidance/computer/navigation-state monitoring and updates.

---

# 2. Apollo 13 real-time GNC workload

The Apollo 13 GNC post-mission report is the strongest current mission-specific source.

## 2.1 SM reaction control system

Prior to the accident, the only documented SM RCS anomaly was **Quad D P/T ratio instrumentation**, which remained full-scale high after transposition/docking/extraction and later returned to correct indication.

The controller attributed this to the transducer being unable to follow the high-use period.

This is important simulator evidence:

> an abnormal instrument indication did not necessarily mean the underlying propulsion system had failed.

## 2.2 Electrical-system effects on control authority

When Main Bus B and AC Bus 2 were lost, selected RCS automatic-control coils lost enable power.

The vehicle rates produced by oxygen venting caused many thruster commands, but available control authority was reduced.

The crew used direct RCS through RHC 2 to assist vehicle control.

Thus GNC's information domain crosses several systems:

- electrical power availability
- RCS enable circuitry
- commanded jets
- achieved vehicle control

This does **not** make GNC the electrical-systems controller; it means GNC must know the electrical dependencies of its own hardware.

## 2.3 Quad D diagnosis

After the accident:

- Quad D fuel manifold pressure decreased
- Quad D oxidizer manifold pressure decreased
- the crew was asked to open the Quad D helium valves
- manifold pressures returned to normal

GNC concluded that the helium isolation valves had been closed by the shock of the oxygen-tank rupture.

This is a good example of controller reasoning from several telemetry values plus a crew action.

## 2.4 Quad C ambiguity

The crew continued to have difficulty damping vehicle rates.

The post-mission report states that:

- the DAP had A/C roll selected
- thruster A1 had been turned off
- the resulting configuration provided only limited axis authority
- there was no indication of Quad C propellant usage

Possible explanations included:

- Quad C propellant isolation valves closed
- Quad C damaged/inoperable

But the propellant valves **and their talkback indicators depended on Main Bus B power**, which had been lost.

Therefore the actual valve state could not immediately be determined.

This is a highly relevant information-quality pattern:

```text
physical state
   ↓
sensor / talkback requires electrical power
   ↓
indication unavailable/ambiguous
   ↓
controller must infer from other telemetry and vehicle response
```

The eventual GNC station must be capable of such ambiguity rather than converting unavailable indication into known state.

## 2.5 DAP / jet-selection recovery

The crew later:

- selected B/D roll in the DAP
- selected Main Bus A on the RCS jet selects

to regain automatic control.

Therefore an Apollo 13 GNC simulation needs sufficient representation of:

- DAP configuration
- jet/quad selection
- electrical enable state
- commanded jet behavior
- actual control response

## 2.6 CM RCS entry preparation

Before command-module RCS operation near entry, instrumented injector temperatures were below minimum operating temperature.

A roughly 20-minute preheat was required before hot-fire checks.

Later, before LM jettison, injector temperatures were checked again and selected jets were fired when temperatures were below the 28 °F limit.

This establishes temperature/thermal state as part of GNC's RCS responsibility.

---

# 3. Parameter families established by mission evidence

The following information families are directly justified for GNC even though the exact Apollo 13 CRT format containing them remains unresolved.

## 3.1 SM RCS

- quad identification A/B/C/D
- propellant quantity/usage
- fuel manifold pressure
- oxidizer manifold pressure
- helium/isolation state where observable
- jet/thruster commands
- jet availability/enabling
- electrical-bus dependency
- P/T ratio instrumentation
- control authority by axis

## 3.2 CM RCS

- injector temperature
- heater/preheat state
- jet firing/check state
- propellant/system status relevant to entry and separation

## 3.3 Digital Autopilot / control configuration

- selected DAP configuration
- quad pair selection
- roll/pitch/yaw control availability
- attitude deadband/rate settings where historically available
- commanded versus achieved vehicle response

## 3.4 Vehicle motion

- attitude rates
- attitude/control behavior
- control-system response to venting/external disturbance

## 3.5 SPS

The broader GNC role includes Service Propulsion System monitoring.

Apollo 13 Flight Director reporting shows GNC noting expected SPS oxidizer-tank pressure decay during translunar coast.

A complete GNC station therefore also requires SPS pressure/propulsion/control data.

Exact field set remains to be reconstructed.

---

# 4. Candidate historical display — CSM GNC PRIMARY TAB

A strong cross-mission candidate exists:

**CSM GNC PRIMARY TAB — display/MSK 0683 / 683**

AC/Delco documentation for Apollo 11 and Apollo 12 explicitly preserves this display.

The page includes field families consistent with GNC's documented Apollo 13 responsibilities, including:

- mission/ground/computer time
- CMC/DSKY registers
- quad information
- RCS and SPS pressure/temperature data
- DAP
- deadband/rate
- attitude error
- CMC/SCS status
- vehicle acceleration
- velocity-to-go components
- PIPA values
- gimbal commands
- SPS gimbal/TVC information
- TIG

## Evidence for Apollo 13 continuity

A mission-specific **AC Electronics Apollo 13 Guidance and Navigation Summary** survives in the Smithsonian National Air and Space Museum Archives.

Independent catalog/auction descriptions state that the Apollo 13 manual contains a section titled:

**ASPO 45 CRT Displays**

which is the same section title under which the Apollo 11/12 manuals present CSM GNC PRIMARY TAB.

### Current evidence status

**PARTIALLY DOCUMENTED / CONTINUITY CANDIDATE**

What is established:

- CSM GNC PRIMARY TAB 0683 existed for Apollo 11 and Apollo 12.
- An Apollo 13 AC Electronics Guidance and Navigation Summary exists.
- The Apollo 13 manual includes an ASPO 45 CRT Displays section.
- The 0683 field families align with Apollo 13 GNC's documented real-time duties.

What is **not** yet established:

- that Apollo 13 retained display 0683 unchanged,
- that its field layout was identical,
- that the same MSK number was used,
- what revisions may have occurred.

Therefore:

> Do not implement 0683 as the Apollo 13 GNC display until the Apollo 13 manual or H-2 operational-configuration documentation confirms it.

It can be used now as a research template for what to look for.

---

# 5. CSM GNC PRIMARY TAB 0683 — known earlier-mission structure

The Apollo 11/12 AC/Delco source provides these major field groups.

This is **reference evidence only**, not yet the Apollo 13 station specification.

## Time / site / computer timing

- GMT
- SITE
- GETA — Ground Elapsed Time Actual
- CTE — Central Timing Equipment time
- CMC — Command Module Computer clock
- GETC — Ground Elapsed Time Computed
- CMC-ΔT — difference between computed GET and CMC time

## Computer / DSKY state

- CMC noun
- Register 1
- Register 2
- Register 3

## Guidance/control state

- ISS
- optics
- CMC
- DAP
- deadband
- rate
- attitude error
- CMC/SCS mode/status

## Propulsion/control hardware

- Quad A/B/C/D information
- RCS helium / manifold data
- SPS tank/regulator/manifold values
- temperature/pressure groups

## Dynamic flight/control quantities

- vehicle acceleration
- VG X / Y / Z
- PIP X / Y / Z
- gimbal command
- OCDU data
- SPS gimbal
- automatic/manual TVC
- TIG

The exact labels, units, scaling, status encoding, and Apollo 13 applicability remain to be verified.

---

# 6. GNC versus GUIDO boundary

A fundamental station-design rule emerges from the records.

## GNC

Concerned with whether the *physical CSM control and propulsion systems* can execute the required motion:

- RCS
- SPS
- SCS
- control electronics
- jet/valve/propellant state
- hardware dependencies
- achieved vehicle behavior

## GUIDO

Concerned with what the *onboard guidance/navigation/computer system* knows and is commanding:

- CMC/LGC state
- guidance programs
- navigation state vectors
- platform alignment
- REFSMMAT
- DSKY/computer monitoring
- ground updates/uplinks

There is overlap because the systems interact, but the jobs are not interchangeable.

This distinction should be preserved when later considering low-player-count role aggregation.

---

# 7. Playback and reconstruction

The GNC post-mission report states that the control-system event sequence was reconstructed using:

- playback data
- delogs
- chart-recorder information

This suggests that real-time diagnosis and later detailed reconstruction used different information products.

Do not assume the GNC player has all retrospective information available live.

---

# 8. Source-quality / implementation status

## DOCUMENTED for Apollo 13

- role responsibilities
- detailed RCS accident response
- DAP/quad-selection reasoning
- electrical dependencies affecting control
- ambiguous/unavailable indications
- CM RCS thermal/preheat concern
- SPS monitoring as a GNC duty
- real-time versus playback distinction

## PARTIAL

- likely display information families
- continuity of CSM GNC PRIMARY TAB from Apollo 11/12

## UNRESOLVED

- Apollo 13 exact GNC console layout
- Apollo 13 exact display IDs
- Apollo 13 version of CSM GNC PRIMARY TAB
- DRK/MSK configuration
- event/limit indicators
- complete SPS display set
- exact command/control authority at the ground console
- voice-loop selections

---

# 9. Research targets

1. Obtain/digitally inspect **AC Electronics, Apollo 13 Guidance and Navigation Summary**.
2. Locate H-2 **PHO-TR155 Revision C**.
3. Confirm whether **CSM GNC PRIMARY TAB 0683** was retained for Apollo 13.
4. Identify other Apollo 13 GNC CRT formats.
5. Identify Apollo 13 GNC console hardware/panel layout.
6. Map GNC telemetry fields to spacecraft instrumentation and units.
7. Locate Apollo 13 GNC console handbook/procedures.

---

## Primary sources

1. *GNC Apollo 13 Post-Mission Report*, Flight Control Division, Appendix F of Apollo 13 Mission Operations Report.  
   NASA/NTRS document 19710010485; also contained in the full Mission Operations Report.

2. *Mission Operations Report — Apollo 13*, 28 April 1970.

3. *Guidance, Navigation, and Control Systems Performance Analysis: Apollo 13 Mission Report Supplement 1*, MSC-02680-SUPPL-1 / NASA-TM-X-69528, September 1970.

4. AC/Delco Electronics Apollo 11 and Apollo 12 Guidance and Navigation Summary material documenting CSM GNC PRIMARY TAB 0683.

## Archival source target

- AC Electronics, *Apollo 13 Guidance and Navigation Summary*, circa 1970, Smithsonian National Air and Space Museum Archives, Apollo Flight Guidance Computer Software Collection [Hamilton], Box 2, Folder 10.
