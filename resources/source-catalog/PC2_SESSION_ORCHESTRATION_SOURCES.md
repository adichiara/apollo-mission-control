# Apollo 13 PC+2 Session-Orchestration Sources

Status: active source supplement for the first integrated multiplayer/session boundary.

## 1. Apollo 13 Technical Air-to-Ground Voice Transcription

- **Source class:** PRIMARY, contemporaneous mission communications
- **NASA transcript collection:** `AS13_TEC.PDF`
- **Use:** establishes the operational sequence around final PC+2 readiness and crew-facing GO transmission.
- **Key interval:** approximately 78:57–79:18 GET.
- **Supported boundary:** controller/team readiness assessment precedes the Flight Director's burn decision; CAPCOM then transmits the GO to the crew as a separate event.
- **Limitation:** air-ground transcription does not document every internal MOCR voice-loop exchange or exact controller polling wording.

## 2. Mission Operations Report — Apollo 13

- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific operational report
- **Use:** controller responsibilities, Flight Director integration/decision role, PC+2 controller chronology, and discipline boundaries.
- **Presentation/session consequence:** supports preserving discipline reports, Flight decision, and CAPCOM crew-facing communication as separate layers.
- **Limitation:** does not define the project's multiplayer transport, persistence, authentication, or reconnect architecture.

## 3. NASA Mission Transcript Collection

- **Organization:** NASA History Office
- **Source class:** PRIMARY-source archive/index
- **Use:** identifies the official Apollo 13 technical air-to-ground transcription (`AS13_TEC.PDF`) and distinguishes it from PAO commentary and onboard recordings.

## Repository research

- `resources/research/078_pc2_flight_capcom_player_presentation_boundary.md`
- `resources/research/079_pc2_session_orchestration_boundary.md`
- `docs/SIMULATION_ARCHITECTURE.md`

## Evidence rule

Do not:

- derive FLIGHT GO automatically from hidden authoritative subsystem state;
- collapse readiness reporting, FLIGHT decision, and CAPCOM transmission into one event;
- assume an undocumented internal voice-loop sequence;
- equate CAPCOM transmission or crew acknowledgement with successful physical spacecraft response;
- describe the framework-neutral session code as historical Apollo software architecture.
