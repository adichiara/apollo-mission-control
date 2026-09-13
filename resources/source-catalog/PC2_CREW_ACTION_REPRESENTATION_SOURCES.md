# PC+2 crew-action representation source supplement

Status: **REVIEWED for first-playable scope boundary**  
Date: 2026-09-13

This supplement records the primary sources used by research note 105 to constrain how spacecraft-crew actions are represented in the PC+2 first playable.

## 1. Mission Operations Report — Apollo 13

- Organization: Flight Control Division, Manned Spacecraft Center
- Date: April 28, 1970
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- Status: **REVIEWED for PC+2 chronology**
- Use in project:
  - records final PC+2 maneuver pads being passed to the crew at about 77+59;
  - records LM power-up beginning at about 78+12;
  - records nominal PC+2 ignition at 79:27:38.30;
  - records LM power-down beginning at about 79+34;
  - records CAPCOM reading a detailed PTC procedure to the crew at about 79+52;
  - supports explicit separation between ground preparation/communication and crew execution.
- Limitation:
  - the chronology does not establish a universal crew-response latency or justify random crew noncompliance/error behavior.

## 2. Apollo Operations Handbook — Lunar Module, Vol. 2 Operational Procedures

- Report: LMA790-3-LM-11 / NASA-CR-115269
- Date: September 26, 1971
- NTRS: https://ntrs.nasa.gov/citations/19710071423
- Status: **REVIEWED-PARTIAL for crew-procedure role**
- Use in project:
  - defines LM normal, backup, abort, malfunction, and emergency procedures as sequences of crew actions;
  - supports modeling crew execution as an operational layer distinct from ground-controller conclusions and spacecraft physical response.
- Limitation:
  - LM 11-and-subsequent documentation is not mission-specific proof of every Apollo 13 switch action or timing.

## 3. Apollo 13 Mission Report

- Report: MSC-02680 / NASA-TM-X-66449
- Date: September 1970
- NTRS: https://ntrs.nasa.gov/citations/19710003598
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionReport.pdf
- Status: **REVIEWED-PARTIAL for mission operations context**
- Use in project:
  - documents crew execution of modified/contingency procedures during Apollo 13;
  - supports preserving crew action and onboard execution as a distinct part of the mission-control causal chain.

## First-playable boundary supported by this catalog

- do not add a separate human crew role for the current Mission Control vertical slice;
- represent crew activity as explicit scenario-authored external actions;
- keep CAPCOM transmission, crew receipt/action, spacecraft response, and resulting evidence distinct;
- deterministic nominal crew steps are permitted only as scenario scaffolding where no crew-discretion mechanic is being claimed;
- do not invent response-delay distributions, random misunderstanding/noncompliance, or crew-error rates;
- reopen the boundary if a later scenario depends on meaningful astronaut discretion, manual flying/workload, ambiguous onboard observations, or detailed checklist execution.
