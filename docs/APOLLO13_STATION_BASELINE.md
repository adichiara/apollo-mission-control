# Apollo 13 Controller Station Baseline

Status: **Phase 1 working baseline**

Purpose: translate the Apollo 13-era historical record into controller-by-controller station requirements without yet simplifying them into game roles.

This is not yet a UI specification. It records what each position must ultimately be able to observe, reason about, communicate, and influence if the Apollo 13-era configuration is used as the common technical baseline.

## Evidence classes

- **DOCUMENTED** — directly supported by mission-era or official NASA material.
- **PARTIAL** — responsibility/workflow is documented, but exact console data/display implementation is not yet reconstructed.
- **UNRESOLVED** — source needed before implementation.

---

## FLIGHT — Flight Director

### Core responsibility — DOCUMENTED

Responsible for MOCR decisions and actions concerning:

- vehicle systems
- vehicle dynamics
- MCC/MSFN operations

FLIGHT receives recommendations from the discipline controllers rather than replacing their detailed monitoring role.

### Station requirements

**Documented / partial:**

- shared awareness of discipline calls
- mission-phase status
- ability to issue/coordinate decisions through the Flight Director loop
- access to group/mission displays and supporting status products

**Unresolved:**

- exact Apollo 13 FLIGHT console display menu
- exact console controls and indicator set
- which direct telemetry products FLIGHT routinely monitored versus relying on discipline calls

---

## CAPCOM — Spacecraft Communicator

### Core responsibility — DOCUMENTED

Responsible for voice communications with the flight crew and served with FAO as a crew-procedures adviser.

### Station requirements

- air-to-ground communications path
- access to current approved procedures/instructions
- Flight loop monitoring
- mission timeline/crew activity awareness

### Unresolved

- exact display set used at the Apollo 13 CAPCOM console
- exact voice-panel configuration

---

## FIDO — Flight Dynamics Officer

### Core responsibility — DOCUMENTED

Responsible for trajectory aspects of the mission, including powered flight trajectory, orbital trajectory, abort/reentry trajectory work, and mission feasibility from a trajectory standpoint.

### Apollo 13 operational evidence

The Apollo 13 FIDO postflight appendix records direct work with:

- tracking-site data quality
- RTCC trajectory state/vector handling
- launch and TLI trajectory
- S-IVB trajectory/impact prediction
- free-return and post-accident return trajectory
- midcourse corrections
- landing-area consequences

The report shows that trajectory conclusions depended not only on spacecraft physics but also on which ground tracking data were considered valid and how the RTCC state was anchored.

### Station requirement implication

A faithful FIDO station cannot simply show a perfect authoritative position vector. It eventually needs a distinction among:

- tracking observations
- accepted/rejected data
- ground-computed state vectors
- predicted trajectory
- maneuver solutions
- landing/entry consequences

### Unresolved

- exact display-format numbers
- exact tracking-data-selection workflow between FIDO and RTCC support
- precise FIDO/RETRO division by mission phase in each target scenario

---

## RETRO — Retrofire Officer

### Core responsibility — DOCUMENTED

Maintained an updated reentry/return plan throughout the mission and supported abort/deorbit/landing-point planning.

### Station requirement implication

Likely information families include:

- return/entry opportunities
- burn timing
- entry corridor
- landing point
- recovery-area implications

### Unresolved

Detailed Apollo 13 RETRO display inventory and console controls remain to be reconstructed from Appendix B and related trajectory documentation.

---

## GUIDO — Guidance Officer

### Core responsibility — DOCUMENTED

Monitored onboard guidance during powered flight and spacecraft initialization and was responsible for CSM/LM DSKY-related ground monitoring and CMC/LGC command updates.

### Apollo 13 operational evidence

The Apollo 13 GUIDO report records reasoning about:

- IU versus CMC navigation-state disagreement
- CMC restart
- CMC vectors, clock, and REFSMMAT validity
- optics and P23 procedures
- LM platform alignment
- use of the LGC to point the LM for alignment verification
- alternate guidance/alignment techniques when PGNCS/CSM systems were powered down

### Station requirement implication

GUIDO must eventually have access to data representing:

- onboard computer state
- guidance/navigation state vectors
- platform/alignment state
- computer/program status
- uploaded guidance data
- DSKY-related state/commands

This must remain distinct from FIDO's ground trajectory role.

### Unresolved

- actual Apollo 13 GUIDO display-format IDs
- exact command/upload UI
- exact ground representation of DSKY/computer telemetry

Detailed GUIDO specification: [`docs/stations/APOLLO13_GUIDO.md`](stations/APOLLO13_GUIDO.md)

---

## CSM EECOM — Electrical / Environmental / Sequential Systems

### Core responsibility — DOCUMENTED

Monitored and troubleshot CSM:

- electrical power
- environmental control
- sequential systems

### Console hardware — DOCUMENTED for Apollo 13

The Apollo 13 Review Board reproduces the EECOM console and identifies:

- two precision TV monitors
- Display Request Keyboard
- Manual Select Keyboard
- event indicators
- status/status-report keyboard
- summary-message-enable keyboard
- analog meter
- two voice-communications positions

The Review Board states that EECOM had multiple display formats and that the two most frequently used examples were updated **once per second**.

### Representative display: CSM EPS High Density — DOCUMENTED

Figure B7-8 includes, among other values:

- Main Bus A/B voltage
- battery voltages
- AC bus voltages
- total spacecraft current
- total fuel-cell current
- fuel-cell currents and load percentages
- inverter temperatures
- fuel-cell skin/condenser/radiator temperatures
- H2 and O2 fuel-cell flow rates
- instrumentation voltages/status values

### Representative display: CSM ECS-Cryo — DOCUMENTED

Figure B7-9 includes:

- cabin and suit pressure
- suit differential pressure
- surge-tank pressure/quantity
- O2 manifold pressure and flow
- suit/cabin temperature
- CO2 partial pressure
- potable and waste-water quantities
- primary and secondary cooling-loop pressures/temperatures
- cryogenic tank pressure, quantity, temperature
- total fuel-cell current

### Limit-sense/event indicators — DOCUMENTED

The Review Board describes event indicators and manually set limit-sense lights. The EECOM could set relatively tight limits to obtain immediate notice of parameter variation.

This is important: not every illuminated limit light represented a catastrophic warning. Limit management itself was part of monitoring.

### Apollo 13 operational evidence

EECOM's postflight report emphasizes:

- oxygen-tank/fuel-cell diagnosis
- power management
- entry-power planning
- Staff Support Room EPS support
- use of HSD Format 30 for anomaly data playback

### Station requirement implication

EECOM is currently the best-documented candidate for the **first historically reconstructed phone station** because both console anatomy and representative display contents survive.

Detailed station specification: [`docs/stations/APOLLO13_EECOM.md`](stations/APOLLO13_EECOM.md)

---

## CSM GNC — Guidance, Navigation & Control Systems Engineer

### Core responsibility — DOCUMENTED

Monitored and troubleshot CSM:

- guidance/navigation/control hardware
- service propulsion
- reaction control

### Apollo 13 operational evidence

The GNC report records detailed reasoning from:

- SM RCS propellant/manifold pressures
- thruster command behavior
- valve state and electrical power availability
- DAP jet selection
- spacecraft rates
- CM RCS thermal state and preheat requirements

This demonstrates that the GNC task was a hardware/propulsion/control-system diagnosis role, not a duplicate of GUIDO.

### Station requirement implication

GNC data needs will include families for:

- SM/CM RCS quantities and pressures
- thruster/valve state
- rates/attitude-control configuration
- SPS status
- stabilization/control system state

### Unresolved

Exact Apollo 13 GNC display formats and console layout remain to be located.

---

## LM TELMU — Electrical / Environmental / EMU

### Core responsibility — DOCUMENTED

Monitored and troubleshot LM:

- environmental systems
- electrical systems
- sequential systems
- later Apollo EMU/lunar-surface support responsibilities

### Apollo 13 operational evidence

The postflight report tracks:

- LM internal/external power state
- LM heater current
- bus voltage
- known oxygen-system anomaly
- LM tunnel leak rate
- water/oxygen/battery lifetime
- power-down strategy
- consumables needed to support the selected return trajectory

After the CSM accident, TELMU's immediate problem became whether the LM could support the crew until the selected Earth-return time.

### Station requirement implication

TELMU needs an LM counterpart to the CSM EECOM information domain, including:

- electrical buses/batteries
- oxygen/water
- ECS
- cabin/suit environment
- consumable/lifetime trends
- EMU data when relevant to mission phase

### Unresolved

Exact Apollo 13 TELMU display formats and console layout.

---

## LM CONTROL — Guidance / Control / Propulsion

### Core responsibility — DOCUMENTED

Monitored and troubleshot LM:

- guidance/control hardware
- propulsion
- RCS

### Apollo 13 operational evidence

The postflight report shows CONTROL directly analyzing:

- DPS supercritical-helium pressure and rise rate
- thresholds that would trigger additional readings or action
- possible DPS burn/helium-tank venting
- LM RCS quantities
- DAP/deadband/attitude behavior
- LM jettison attitude and separation behavior

A useful operational example is the pre-accident supercritical-helium concern: CONTROL established response branches based on measured pressure ranges and projected PDI pressure.

### Station requirement implication

CONTROL needs data for:

- DPS/APS status and pressures
- supercritical helium
- LM RCS
- attitude/control state
- AGS/PGNCS-related vehicle-control information where it belongs to CONTROL rather than GUIDO

### Unresolved

Exact display formats and division of some guidance information between CONTROL and GUIDO.

---

## INCO — Instrumentation and Communications Officer

### Core responsibility — DOCUMENTED

Responsible for spacecraft communications/instrumentation functions and execution of communications-system commands.

### Apollo 13 operational evidence

The INCO postflight report documents:

- TV downlink configuration
- DSE playback/dump interaction with communications modes
- S-band/FM behavior
- ground-site diagnosis
- omni-antenna switching by ground command
- timing commands around two-way-lock/uplink thresholds
- use of alternate uplink modes when link margin was insufficient

### Station requirement implication

INCO is not simply a signal-strength monitor. The role requires a model of:

- spacecraft transmitter/receiver configuration
- antennas
- telemetry modes
- downlink/uplink state
- DSE/recorded-data handling
- ground-station acquisition/lock
- command path and margins

### Unresolved

- station display formats
- exact command-control interface
- how much MSFN site status was displayed locally versus provided by NETWORK/CCATS

---

## PROCEDURES / O&P

### Documented role

Coordinated detailed MCC/MSFN/interface procedures and handled operational procedure issues including data playback scheduling.

Apollo 13's report contains numerous cases where procedures had to be developed or modified in real time.

### Simulation implication

This position may be extremely important in contingency scenarios, but representation is not yet decided.

---

## FAO — Flight Activities Officer

### Documented role

Developed and coordinated the flight plan and crew activity sequence.

Apollo 13's FAO report shows active coordination with EECOM, GUIDO, CONTROL, FIDO, SPAN, CAPCOM, and Flight Plan Support while procedures and timelines were repeatedly rewritten.

### Simulation implication

FAO is a real workload center during complex contingencies, not merely an administrative scheduler.

Representation is not yet decided.

---

## SURGEON

### Documented role

Operational medical monitoring and evaluation of crew condition.

Exact biomedical display requirements remain to be reconstructed.

---

# Initial station-reconstruction priority

Based solely on source completeness—not on final player-role importance—the current reconstruction order is:

1. **CSM EECOM** — console layout and two actual high-use displays survive.
2. **INCO** — unusually detailed command/network workflow survives in the Mission Operations Report.
3. **CSM GNC** — strong mission-operational evidence for diagnostic reasoning.
4. **LM CONTROL** — strong mission-operational evidence and clear parameter families.
5. **LM TELMU** — strong consumables/electrical/environmental mission chronology.
6. **GUIDO**
7. **FIDO / RETRO**
8. remaining positions

This is a research-priority order only. It does not determine player-role priority or minimum player count.

## Primary sources

- *Mission Operations Report — Apollo 13*, Flight Control Division, 28 April 1970.  
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf

- *Report of Apollo 13 Review Board, Appendix B*, especially figures B7-7 through B7-9.  
  https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-review-report-app-b-c-d-e-19700078726.pdf

- *Report of Apollo 13 Review Board, Appendix A*, Mission Control organization.  
  https://ntrs.nasa.gov/citations/19700078804

- AS-508 MCC/MSFN Mission Configuration/System Description.  
  https://ntrs.nasa.gov/citations/19700024253
