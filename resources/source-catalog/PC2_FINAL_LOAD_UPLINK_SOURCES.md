# Apollo 13 PC+2 Final Load / Uplink Sources

Status: active source supplement for the first-playable final state-vector/target-load workflow.

## 1. Mission Operations Report — Apollo 13

- **Organization:** NASA Manned Spacecraft Center, Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Documents PC+2 state-vector/target-load handling, including the LGC cislunar-navigation constraint, vector timetagging at TIG−30 seconds, consistency between vector and external ΔV reference basis, earlier load activity, final maneuver-pad timing, and executed burn timing.
- **NASA scan:** https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- **Limitation:** Does not provide a complete byte/word load dump, exact controller key sequence, or complete internal RTCC/CCATS command path.

## 2. Apollo 13 Technical Air-To-Ground Voice Transcription

- **Organization:** NASA
- **Date:** April 1970
- **Source class:** PRIMARY, mission-specific
- **NTRS:** 20160014370
- **Use:** Supports the final-load crew configuration sequence near 78:17 GET: crew request for state-vector update; CAPCOM requirement for P00, DATA/ACCEPT, and UPDATA LINK configuration; transmission; subsequent ranging verification.
- **Link:** https://ntrs.nasa.gov/citations/20160014370
- **Limitation:** Air-ground does not expose all internal Mission Control computation/authorization steps.

## 3. Apollo 13 Flight Director loop audio/transcription

- **Origin:** NASA Johnson Mission Control audio; modern presentation/transcription by Apollo 13 in Real Time
- **Source class:** PRIMARY audio for controller-loop content; modern site is an access layer
- **Use:** Records FLIGHT directing state-vector + target-load uplink when P00/DATA are available, GUIDO tying readiness to the uplink configuration, and INCO working that configuration. This supports a cross-station dependency rather than a GUIDO-only instantaneous update.
- **Access:** https://apollo13realtime.org/
- **Limitation:** Modern transcription/commentary must not be treated as a substitute for the original audio where wording is critical.

## 4. Mission Operations Report flight-plan timeline

- **Source class:** PRIMARY, mission-specific
- **Use:** Places P30 external ΔV, state-vector update, LM power-up, and PC+2 in the 78–80 GET preparation sequence and confirms TIG 79:27:38.30.
- **Limitation:** Timeline placement is coarse and does not establish exact sub-minute uplink timing by itself.

## Implementation rule

Model the final state-vector/target load as a staged information-transfer workflow across FIDO/RTCC, GUIDO, INCO, CAPCOM/crew, and FLIGHT. Do not invent exact Cartesian vector values, internal command strings, display IDs, or transmission durations unless a primary source establishes them.