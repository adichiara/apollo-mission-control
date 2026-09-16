# Apollo 13 PC+2 GDA trim source catalog

Date: 2026-09-16

## Apollo 13 Luminary 1C / Luminary 131 source listing — Verb 48 DAP-load routine

- File: `EXTENDED_VERBS.agc`
- Listing: https://www.ibiblio.org/apollo/listings/Luminary131/EXTENDED_VERBS.agc.html
- Relevant printed pages: 297–298
- Source class: Apollo 13 mission flight-software source listing

### Supports
R03 reaches Noun 47 as the mass-load step. `V34E` branches to termination before Noun 48; the PC+2 instruction to enter V34 after N47 therefore selected a real software termination path before N48.

## NASA Apollo 13 air-to-ground transcript — ~59 GET provisional PC+2 pad

- Relevant GET: approximately 59:03–59:05
- Source class: primary mission voice transcription

### Supports
CAPCOM passes PC+2 DPS trim/GDA pitch `5.86°`, roll 6.75°, says the angles "will be updated," and accepts the crew readback.

## NASA Apollo 13 Technical Air-to-Ground Voice Transmission — 61:29 free-return DPS burn

- NASA PDF: https://www.nasa.gov/wp-content/uploads/2026/01/as13-tec.pdf
- Relevant GET: `060:53:09`–`060:56:21`
- Source class: primary mission voice transcription

### Supports
CAPCOM's P30 pad for the 61:29:42.84 free-return correction gives LM GDA pitch `5.86°`, roll `6.75°`; Haise reads it back and CAPCOM accepts it.

## Apollo 13 Flight Director loop — preburn gimbal checkout

- Relevant GET: approximately `61:03`–`61:12`
- Presentation/transcription: https://apollo13realtime.org/
- Underlying source: recovered NASA mission-control audio; presentation credits NASA/NASA Johnson for source audio/transcription availability
- Source class: mission-control voice evidence

### Supports
CONTROL explicitly directs gimbal rather than throttle trim and the DAP-set gimbal/throttle-test sequence. At about 61:11 CONTROL reports `Trim looks okay`; when FLIGHT asks how close the values are, CONTROL answers `within about 0.3` / `plenty close`, then reports readiness.

### Boundary
This is an operational **preburn spacecraft gimbal-checkout** acceptance statement. It is not evidence that `0.3°` was the acceptance criterion for the earlier Flight Dynamics-versus-CONTROL mass-properties calculation disagreement, and it is not a PC+2 computational trim tolerance. Editorial annotations on the presentation site are not treated as primary evidence.

## NASA Apollo 13 mission material — DPS automatic gimbal trim

- Primary PDF: https://ntrs.nasa.gov/api/citations/19700076776/downloads/19700076776.pdf
- Source class: primary NASA Apollo 13 mission reference material

### Supports
The descent engine is gimbaled; gimbal trim compensates for changing vehicle center of gravity and is automatically accomplished by PGNS or AGS. Therefore the initial commanded GDA pair must not be treated as invariant physical actuator position through powered flight.

## Apollo 13 LM131 flight software — trim-gimbal control law

- File: `TRIM_GIMBAL_CONTROL_SYSTEM.agc`
- Listing: https://ibiblio.org/apollo/listings/LM131R1/TRIM_GIMBAL_CONTROL_SYSTEM.agc.html
- Source class: reconstructed final Apollo 13 LM flight-software listing preserving original program comments

### Supports
Original comments describe trim-gimbal control operating with the descent engine and digital autopilot on. This independently bounds powered-flight behavior but does not reconstruct the missing ground mass-properties computation or actual 61:29 actuator history.

## NASA Apollo 13 mission commentary — post-61:29 revised PC+2 pad readback

- Relevant GET: approximately `63:10`
- Source class: primary mission voice/PAO transcription

### Supports
GDA should be "okay as is" with retained reference `5.85 / 6.74`, qualified by the crew's "hopefully." Not measured actuator telemetry.

## NASA Apollo 13 air-to-ground transcript — PC+2 activation and burn rules

- Relevant GET: `075:07:43` onward
- Source class: primary mission voice transcription

### Supports
CAPCOM instructs `VERB 34 ENTER` immediately after Noun 47 and confirms the gimbals already look all right. Later ground rules state no PC+2 maneuver trims required. Final P30 targeting read-up omits a GDA pair.

## NASA Flight Control Division Mission Operations Report — Apollo 13

- Date: 28 April 1970
- Source class: primary mission-specific controller report

### Supports
T-6 mass properties generated/loaded in RTCC; T+25 RTCC mass properties run with P/Y trim comparison; RTCC LM-burn decks updated to T+55; ~59 GET CONTROL/Flight Dynamics disagreement and reconciliation; CONTROL's challenged basis used premission mass properties; T+25 no-update because P/Y trims were within `0.01°` of T+6; no PC+2 maneuver trims required; powered-flight GDA behavior and expectation that 61:29 compliance would leave optimum PC+2 alignment.

### Boundary
The report does not identify the T+55 deck contents, downstream trim run, CONTROL alternative numerical trim, PC+2 ground-computation comparison criterion, job identity, or direct T+55-to-`5.86 / 6.75` calculation link.

## Current synthesis

`mass-properties provenance [generation/load/update/run distinct] -> calculation/comparison [details unresolved] -> ~59 provisional PC+2 5.86 / 6.75 -> same pair commanded for 61:29 -> preburn gimbal checkout within ~0.3 judged plenty close -> powered-flight automatic trim available to compensate changing c.g. -> exact gimbal history/post-compliance state unrecovered -> later 5.85 / 6.74 "okay as is" reference -> no new PC+2 Noun 48 entry`.

The next archival target remains a T+55 generation/load record or downstream RTCC/RTACF LM-burn run/request/output tying the deck to the PC+2 candidate trim, plus real-time weight/c.g. inputs, CONTROL's competing trim, ground-computation comparison values/criterion, and job identity. A parallel target is actual GDA-position telemetry/controller evidence during or immediately after 61:29. Keep the recovered `~0.3°` checkout acceptance strictly separate from the unresolved computational criterion.