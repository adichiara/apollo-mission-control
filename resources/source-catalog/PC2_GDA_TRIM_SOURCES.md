# Apollo 13 PC+2 GDA trim source catalog

Date: 2026-09-16

## NASA Apollo 13 air-to-ground transcript — commanded trim

- Relevant GET: approximately 59:03–59:05 and 60:53–60:56
- Source class: primary mission voice transcription

### Supports
CAPCOM passes PC+2 DPS trim/GDA `5.86° / 6.75°` provisionally near 59 GET and later passes the same pair for the actual 61:29 free-return correction. This establishes a commanded/preburn angular reference, not invariant powered-flight actuator state.

## Apollo 13 Flight Director loop — preburn gimbal checkout

- Relevant GET: approximately 61:03–61:12
- Presentation/transcription: https://apollo13realtime.org/
- Underlying source: recovered NASA mission-control audio
- Source class: mission-control voice evidence

### Supports
CONTROL directs the preburn gimbal checkout, reports `Trim looks okay`, and answers FLIGHT's closeness question with `within about 0.3` / `plenty close`.

### Boundary
This is spacecraft-checkout acceptance, not evidence of the earlier Flight Dynamics-versus-CONTROL computational criterion.

## NASA/MSC Apollo 13 Mission Report — exact 61:29 GDA actuator summary

- Report: *Apollo 13 Mission Report*, MSC-02680, September 1970
- NTRS citation: `19710003598`
- Relevant section: 6.4, Table 6.4-I
- Source class: primary mission-specific postflight report

### Supports
For the second midcourse correction at ignition `61:29:43.49`, Table 6.4-I reports Gimbal Drive Actuator position in **inches**:

- initial: pitch `-0.02`, roll `-0.34`;
- maximum excursion: pitch `+0.31`, roll `-0.27`;
- steady-state: pitch `+0.04`, roll `-0.51`;
- cutoff: pitch `+0.10`, roll `-0.31`.

The table also gives cutoff `61:30:17.72`, duration `34.23 s`, and post-trim velocity residual `[+0.2, 0.0, +0.3] ft/s`.

### Boundary
The GDA values are actuator displacement in inches, not trim angles in degrees. The source labels the second actuator axis `Roll`; preserve that label. The four phase values are a postflight summary, not a continuous telemetry trace. The velocity residual is a translational outcome and unrelated to GDA displacement.

## LM-7/8/9 Elementary Functional Diagrams — mission-block GDA measurement semantics

- Document: `LED-267-37C`, *Lunar Module 7, 8, & 9 Elementary Functional Diagrams*
- Public scan: https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf
- Relevant item: Table 3, LM EFD Measurement Index
- Source class: primary LM-7/8/9 engineering documentation

### Supports
The measurement index identifies `GH1313V` as Pitch GDA position `(RET/EXT)` and `GH1314V` as Roll GDA position `(EXT/RET)`, plus separate pitch/roll LGC extend/retract command discretes. This validates Pitch/Roll as the LM-7 hardware GDA axis labels, shows axis-specific opposite extension/retraction notation, and distinguishes analog position measurements from LGC trim-command discretes.

### Boundary
The recovered index does not itself define voltage-to-inch calibration, which numerical sign means EXT or RET in the Mission Report, or the mapping to crew-facing `5.86 / 6.75`.

## Apollo Operations Handbook — GDA actuator-position feedback path

- Document: *Apollo Operations Handbook, Lunar Module LM 10 and Subsequent, Volume I — Subsystems Data*
- Relevant item: figure 2.1-50, *Descent Engine Control Assembly — Trim Control Diagram*
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/LM10HandbookVol1.pdf
- Source class: primary NASA/Grumman subsystem documentation; later LM configuration used only as signal-path continuity evidence

### Supports
The diagram shows **ACTUATOR POSITION FEEDBACK** returning from the Gimbal Drive Actuator into the DECA and places the Pitch/Roll GDA-position measurement family on the actuator/feedback side of the architecture. LGC positive/negative trim-error inputs and extend/retract motor commands are separate paths. Combined with the LM-7/8/9 measurement index, this supports treating GH1313V/GH1314V as physical actuator-position observations rather than aliases for trim commands.

### Boundary
This does not supply LM-7 voltage-to-inch calibration, numerical polarity, or the crew-facing trim-number reference. It is not used to infer any conversion.

## NASA Apollo News Reference — generic LM GDA mechanical range

- NASA-hosted main-propulsion excerpt: https://www.nasa.gov/wp-content/uploads/static/history/alsj/LM09_Main_Propulsion_ppMP1-22.pdf
- Source class: primary NASA LM reference material

### Supports
The gimbal drive actuators extend/retract 2 inches from mid-position to tilt the descent engine a maximum of 6° along each axis. The nominal endpoint ratio is therefore `3°/in`.

### Boundary
This is generic mechanism documentation, not an LM-7 calibration sheet. It does not define the crew-facing GDA trim-number zero/reference or sign convention, and the nominal endpoint ratio must not be used to convert the Apollo 13 `5.86 / 6.75` pair or Table 6.4-I values into asserted historical equivalents.

## NASA Apollo 13 mission material — DPS automatic gimbal trim

- Primary PDF: https://ntrs.nasa.gov/api/citations/19700076776/downloads/19700076776.pdf
- Source class: primary NASA Apollo 13 mission reference material

### Supports
Gimbal trim compensates for changing vehicle center of gravity and can be automatically accomplished by PGNS or AGS; the initial commanded pair therefore must not be treated as invariant physical actuator position through powered flight.

## Apollo 13 LM131 flight software — trim-gimbal control law

- File: `TRIM_GIMBAL_CONTROL_SYSTEM.agc`
- Listing: https://ibiblio.org/apollo/listings/LM131R1/TRIM_GIMBAL_CONTROL_SYSTEM.agc.html
- Source class: reconstructed final Apollo 13 LM flight-software listing preserving original program comments

### Supports
Original comments describe trim-gimbal control operating with the descent engine and digital autopilot on.

## NASA Flight Control Division Mission Operations Report — Apollo 13

- Date: 28 April 1970
- Source class: primary mission-specific controller report

### Supports
T-6 mass properties generated/loaded in RTCC; T+25 RTCC mass-properties run with P/Y trim comparison; RTCC LM-burn decks updated to T+55; ~59 GET CONTROL/Flight Dynamics disagreement and reconciliation; CONTROL's challenged basis used premission mass properties; T+25 no-update because P/Y trims were within `0.01°` of T+6; powered-flight GDA behavior and expectation that 61:29 compliance would leave optimum PC+2 alignment.

### Boundary
The report does not identify T+55 deck contents, a downstream trim run, CONTROL's alternative numerical trim, PC+2 computational comparison criterion, job identity, or a direct T+55-to-`5.86 / 6.75` calculation link.

## NASA Apollo 13 mission commentary — post-free-return PC+2 GDA reference

- Relevant transcript page: GET 63:00:00, 14 April 1970
- Source class: primary mission voice/PAO transcription

### Supports
CAPCOM introduces a new PC+2 P30 maneuver pad and states that the GDA `ought to be okay as it is from the last burn`, while specifying **pitch `5.85`, roll `6.74`** as what it `ought to be`.

This is stronger than the earlier OCR/search rendering documented in note 169: it identifies CAPCOM as the speaker, uses pitch/roll axis wording, and classifies `5.85 / 6.74` as a ground-issued PC+2 desired/reference pair with a no-action disposition based on the prior burn.

### Boundary
This is not measured actuator telemetry and does not prove that the pair was generated by a new RTCC/RTACF trim run. The `0.01°` per-axis difference from `5.86 / 6.75` does not establish an acceptance threshold.

## Apollo 13 GN&C performance-analysis supplement

- NTRS citation: `19730017939`
- Report: `MSC-02680-SUPPL-1` / `TRW-11176-H586-R0-00-SUPPL-1`
- Date: September 1970
- Source class: primary mission-specific postflight GN&C analysis

### Status
Still useful for finer DAP/telemetry interpretation, but no longer required to establish exact phase-summary GDA values for 61:29 because Mission Report Table 6.4-I supplies them directly.

## Current synthesis

`mass-properties provenance [generation/load/update/run distinct] -> calculation/comparison [details unresolved] -> ~59 provisional 5.86 / 6.75 -> same pair commanded for 61:29 -> preburn checkout within ~0.3 judged plenty close -> LGC trim-command path distinct from physical GH1313V/GH1314V actuator-position feedback -> powered flight under nominal primary guidance/AUTO -> measured Pitch/Roll GDA phase summary in inches (-0.02/-0.34 initial; +0.31/-0.27 max excursion; +0.04/-0.51 steady; +0.10/-0.31 cutoff) -> post-trim velocity residual +0.2/0.0/+0.3 ft/s -> CAPCOM issues later PC+2 reference 5.85/6.74 with 'okay as it is from the last burn' disposition`.

The exact-value powered-flight actuator-history target is closed at the Mission Report's phase-summary resolution. Generic LM mechanical scale is bounded at nominal 3°/in, LM-7/8/9 documentation identifies the GDA measurement channels and polarity descriptors, and the subsystem handbook confirms the physical actuator-position feedback signal class. Numerical telemetry calibration and crew-facing trim representation remain unresolved. The main archival target remains a T+55 generation/load record or downstream RTCC/RTACF LM-burn run/request/output tying the deck to the candidate trim, plus weight/c.g. inputs, CONTROL's competing trim, comparison values/criterion, and job identity.