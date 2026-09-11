# Apollo Flight-Control Organization Baseline

Status: **Phase 1 research baseline**

This document summarizes the controller organization that is currently supported by Apollo-era NASA documentation. It is not yet a player-role design.

The principal detailed source used here is Appendix A of the Apollo 13 Review Board baseline-data report. Apollo 11-specific manning is checked against the official June 30, 1969 flight-control manning memorandum reproduced in NASA-TM-103373.

## 1. Mission Operations Control Room (MOCR)

Apollo documentation divides the prime MOCR positions into three operating groups:

1. Mission Command and Control
2. Systems Operations
3. Flight Dynamics

The MOCR was not the whole flight-control organization. Each discipline depended on Staff Support Rooms and on MCC computer/communications support.

## 2. Mission Command and Control Group

Documented positions include:

| Position | Documented responsibility |
|---|---|
| Mission Director (MD) | Overall conduct of the mission |
| Flight Operations Director (FOD) | Interface between Flight Director and management |
| Flight Director (FD / FLIGHT) | MOCR decisions and actions concerning vehicle systems, vehicle dynamics, and MCC/MSFN operations |
| Assistant Flight Director (AFD) | Assists the Flight Director |
| Flight Activities Officer (FAO) | Develops and coordinates the flight plan |
| DOD Representative | Coordinates/directs Department of Defense mission-support forces and sites |
| Assistant DOD Representative | Assists DOD representative |
| Network Controller (NETWORK) | Detailed operational control and failure analysis of the Manned Space Flight Network |
| Assistant Network Controller | Assists NETWORK; responsible for MCC equipment ability to support |
| Public Affairs Officer (PAO) | Keeps the public informed on mission progress |
| Surgeon | Analysis/evaluation of operational medical activities |
| Spacecraft Communicator (CAPCOM) | All voice communications with the flight crew; also a crew-procedures adviser with FAO |
| Experiments Officer (EO / EXPO) | Coordinates/control experiments and reports experiment status that may affect the mission |

### Simulation relevance

This group contains both direct operational decision positions and management/public-information positions. The complete historical complement must not automatically be treated as a list of player stations.

CAPCOM is operationally distinct: the Apollo documentation identifies CAPCOM as the voice path to the crew.

## 3. Systems Operations Group

### CSM positions

| Position | Documented responsibility |
|---|---|
| CSM EECOM | Monitor/troubleshoot CSM environmental, electrical, and sequential systems |
| CSM GNC | Monitor/troubleshoot CSM guidance, navigation, control, and propulsion systems |

### LM positions

For the Apollo 11-era terminology currently supported by the official manning list:

| Position | Documented responsibility |
|---|---|
| LM/TELCOM | Monitor/troubleshoot LM environmental, electrical, and sequential systems |
| LM/CONTROL | Monitor/troubleshoot LM guidance, navigation, control, and propulsion systems |

### Launch vehicle positions

The Booster Systems Engineer function was divided among three positions:

- **BSE 1:** overall launch-vehicle responsibility including command capability; S-IC and S-II functions
- **BSE 2:** S-IVB functions except command
- **BSE 3:** Instrument Unit functions except command

### Communications / procedures

Apollo documentation describes INCO and O&P as sharing a console/responsibility area.

- **INCO / Apollo Communications Engineer:** spacecraft, LM, TV, PLSS, and erectable-antenna communications; execution of communications-system commands
- **O&P / PROCEDURES:** detailed MCC/MSFN/GSFC/KSC interface procedures; telemetry and DSE voice playback scheduling; ground-support timeline communications inputs/changes

## 4. Flight Dynamics Group

| Position | Documented responsibility |
|---|---|
| FIDO | Prelaunch readiness; powered-flight trajectory/mission feasibility; reentry trajectory monitoring; impact-point updates |
| RETRO | Prelaunch readiness; maintain an updated reentry plan throughout the mission |
| GUIDO | Guidance monitoring during powered flight and spacecraft initialization; CSM/LM DSKY and CMC/LGC command updates |
| YAW | Second guidance officer with similar monitoring duties but without command responsibility |

These definitions show why FIDO, RETRO, and GUIDO should not be collapsed conceptually into one generic "navigation" role before workload is studied.

## 5. Staff Support Rooms (SSR)

Apollo flight control was explicitly a front-room/backroom organization.

Documented support rooms include:

### Flight Dynamics SSR

Provided:

- detailed launch and reentry analysis
- maneuver requirements
- orbital trajectory analysis
- real-time trajectory/guidance support with MPAD
- interface to program-office and contractor personnel

### Flight Director's SSR

Supported:

- Flight Director
- Assistant Flight Director
- Data Management Officer
- FAO
- detailed communications-system monitoring for the Apollo Communications Engineer

It also maintained Ground Timeline and Flight Plan TV-channel displays.

### Vehicle Systems SSR

Supported the Systems Operations Group by:

- monitoring detailed system status and trends
- preventing/correcting/circumventing failures
- detecting and isolating malfunctions

### Life Systems SSR

Provided detailed physiological/environmental monitoring concerning the crew and their environment.

### Other documented support areas

- Spaceflight Meteorological Room
- Space Environment Console
- Spacecraft Planning and Analysis (SPAN) Room
- Recovery Operations Control Room (ROCR)
- ALSEP SSR

## 6. MCC computer / communications support

Two primary technical support areas interfaced with the MOCR team:

### CCATS

The Communications, Command, and Telemetry System interfaced between MCC and MSFN sites and handled reception, transmission, routing, processing, display, and control for telemetry, command, tracking, and administrative information.

Documented support positions included:

- Real-Time Command Controller (RTC)
- Command Load Controller
- CCATS Command Controller
- Telemetry Instrumentation Controller (TIC)
- CCATS Telemetry Controller
- Instrumentation Tracking Controller (TRK)
- USB Controller
- Central Processor Controller
- Central Processor Maintenance & Operations
- Communications Controller

### RTCC

The Real-Time Computer Complex provided MCC data-processing support including:

- telemetry processing
- storage and limit sensing
- trajectory/ephemeris calculations
- command-load generation
- display generation
- other mission logic/calculations

Documented RTCC positions included:

- RTCC Director
- Computer Supervisor
- Tracking Data Selection Controller
- Flight Dynamics Processing Controller
- Network and Command Processing Controller
- Telemetry Processing Controller

This supports a simulation architecture in which controller displays are downstream of ground processing rather than direct views of physical state.

## 7. Apollo 11-specific manning evidence

The official Apollo 11 manning memorandum dated June 30, 1969 contains explicit MOCR shift columns and includes, among others:

- Director of Flight Operations
- Flight Director
- Assistant Flight Director
- CSM/GNC
- CSM/EECOM
- CSM/INCO
- Flight Dynamics Officer
- Retrofire Officer
- Guidance Officer
- Booster Systems Engineers 1–3
- LM/CONTROL
- LM/TELCOM
- Surgeons
- Experiments Officer
- Network Controller
- Operations and Procedures Officer
- Public Affairs
- CAPCOM
- Flight Activities Officer
- Mission Director / staff

The same source separately lists substantial Flight Dynamics SSR personnel.

### Important caution

The Apollo 13 baseline document describes three 9-hour shifts. The Apollo 11 manning memorandum is organized into **four shift columns**. Therefore staffing/shift assumptions must be mission-specific rather than generalized from one Apollo mission.

## 8. TELCOM versus TELMU

For Apollo 11, the official flight-control manning list uses **LM/TELCOM**.

An Apollo 11 Flight Director loop transcript during the EVA also records the Flight Director calling **Telcom**.

Robert Heselmeyer's NASA oral history explicitly recalls that the front-room call sign was TELCOM for the early lunar flights (including Apollo 11) and changed to TELMU later as EMU/lunar-surface responsibilities became more prominent; he recalls TELMU from approximately Apollo 12 onward.

Therefore:

> If Apollo 11 is selected as a baseline, use the mission-specific call sign **TELCOM** unless a stronger mission-specific source for a particular interval establishes otherwise.

Do not retroactively normalize every mission to TELMU.

## 9. What this establishes for the simulation

### Documented

- controller work was discipline-separated
- FLIGHT sat above discipline decisions rather than replacing them
- front-room controllers depended on support-room specialists
- flight dynamics, vehicle systems, and command/control were organizationally distinct
- controller-visible information depended on MSFN/CCATS/RTCC processing
- CAPCOM was the voice interface to the crew
- mission-specific staffing and nomenclature varied

### Not yet decided

- which positions become player roles
- minimum player count
- which roles can be combined
- whether any SSR function is represented automatically or by players
- whether CCATS/RTCC support positions become explicit simulation agents
- how voice loops are implemented
- exact role set for the first mission interval

Those decisions wait for role workload, display, and mission-phase research.

## Sources

1. **Report of Apollo 13 Review Board, Appendix A: Baseline Data — Apollo 13 Flight Systems and Operations**, Part A4, Mission Control Center Activities.  
   https://ntrs.nasa.gov/api/citations/19700078804/downloads/19700078804.pdf

2. **Flight Operations reunion for the Apollo 11 20th anniversary of the first manned lunar landing**, NASA-TM-103373; includes June 30, 1969 official flight-control manning memorandum.  
   https://ntrs.nasa.gov/citations/19910008862

3. **Flight control of the Apollo lunar landing mission**, M. P. Frank, NASA-TM-X-58036, December 1969.  
   https://ntrs.nasa.gov/citations/19700009496

4. **Apollo 11 Flight Director Loop — EVA transcript/audio**, NASA Apollo Lunar Surface Journal.  
   https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/Apollo11EVA_FD_Loop_Audio.html

5. **Robert H. Heselmeyer Oral History**, NASA Johnson Space Center Oral History Project, November 12, 2004.  
   https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/HeselmeyerRH/HeselmeyerRH_11-12-04.pdf
