# Apollo Simulation-Engine Sources

Status: active source catalog for the project's causal simulation-engine architecture.

This catalog separates evidence about how Apollo simulation/training worked from project architecture decisions. It does not imply that the original simulator software or complete mathematical models have been recovered.

## NASA TN D-7290 — *Apollo Experience Report: Simulation of Manned Space Flight for Crew Training*

- Authors: C. H. Woodling et al.
- NASA/JSC, 1973.
- NTRS document ID: `19730011149`.
- NTRS record: https://ntrs.nasa.gov/citations/19730011149
- Evidence use: Apollo crew-training mission simulators; functional uses, characteristics, development experience, and fidelity evolution.
- Status: identified/reviewed at report-record level; detailed simulator internals remain a target for deeper extraction.

## NASA TN D-7436 — *Apollo Experience Report: Systems and Flight Procedures Development*

- Author: P. C. Kramer.
- NASA/JSC, 1973.
- NTRS document ID: `19730023040`.
- NTRS record: https://ntrs.nasa.gov/citations/19730023040
- Evidence use: mission-simulation procedure verification; coupling of the Apollo mission simulator to simulated MSFN/MCC functions; coverage of spacecraft trajectories, telemetry, uplink/voice communications, and major spacecraft systems operations.
- Key boundary: NASA describes the Apollo mission simulator as the highest-fidelity spacecraft simulator available for mission simulation, used together with Mission Control for procedure verification and training.

## NASA TN D-7287 — *Apollo Experience Report: Guidance and Control Systems—Engineering Simulation Program*

- Author: David W. Gilbert.
- NASA/JSC, 1973.
- NTRS document ID: `19730016146`.
- NTRS record: https://ntrs.nasa.gov/citations/19730016146
- Evidence use: real-time engineering simulation; use of general-purpose analog/digital computing, subsystem hardware, special interfaces, and large hybrid mission-evaluation simulators for closed-loop verification.
- Key boundary: this is engineering-simulation evidence, not a direct software listing for the crew-training mission simulator, but it confirms that Apollo system behavior was modeled causally rather than only replayed as scripted event sequences.

## NASA Apollo training overview, 1964

- NTRS document ID: `19660019476`.
- NTRS PDF: https://ntrs.nasa.gov/api/citations/19660019476/downloads/19660019476.pdf
- Evidence use: description of planned Apollo mission simulators.
- Relevant evidence: the command-module controls, displays, and window scenes were to be active and driven closed-loop by peripheral computing equipment; the instructor console was to include duplicate displays and malfunction-insertion units.
- Key boundary: early-program description; later mission-specific implementation details may differ.

## AIAA Paper 65-266 — *Integrated Operating Mode of the Apollo Mission Simulator*

- Authors: F. O. Martikan and S. H. Nassiff.
- 1965.
- NTRS document IDs: `19650039405` / `19660033487`.
- NTRS records:
  - https://ntrs.nasa.gov/citations/19650039405
  - https://ntrs.nasa.gov/citations/19660033487
- Evidence use: integrated Apollo mission simulator/Mission Control training concept.
- Status: record identified; public full text not currently recovered through NTRS.

## NASA TN D-7822 — *Apollo Experience Report: The Role of Flight Mission Rules in Mission Preparation and Conduct*

- Author: L. W. Keyser.
- NASA/JSC, 1974.
- NTRS document ID: `19750002893`.
- NTRS record: https://ntrs.nasa.gov/citations/19750002893
- Evidence use: mission-rule development and controller training, including training for nonnominal situations for which no complete response had been preplanned.
- Architecture relevance: supports a simulator that allows controllers to reason through consequences rather than merely select the one expected historical branch.

## Apollo Operations Handbooks and subsystem engineering reports

The mission-simulator documents establish the need for causal/closed-loop behavior but do not by themselves provide every subsystem equation or failure consequence. The project should continue using mission-specific or vehicle-specific sources for physical mechanisms, including:

- Apollo Operations Handbook LM/CSM systems descriptions and operational procedures;
- subsystem specifications and malfunction procedures;
- Apollo Experience Reports for propulsion, electrical, guidance/control, communications, instrumentation, etc.;
- telemetry/instrumentation documentation where observation behavior matters;
- mission rules and controller console documentation for controller interpretation/action boundaries.

## Current evidence conclusion

The surviving Apollo documentation strongly supports the architecture direction of a **closed-loop, stateful simulator with malfunction insertion and derived spacecraft/controller observations**. It does not yet justify claiming recovery of the original Apollo simulator's full mathematical model, software architecture, or malfunction inventory.
