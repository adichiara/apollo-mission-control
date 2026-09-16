# Apollo 13 PC+2 ~59 GET trim-provenance sources

Date: 2026-09-16  
Related notes: `resources/research/170_pc2_59h_trim_provenance.md`, `resources/research/171_rtacf_mass_properties_trim_artifact_class.md`, `resources/research/172_apollo13_postflight_mass_properties_validation_bound.md`, `resources/research/173_realtime_mass_properties_update_precedent.md`, `resources/research/174_tplus_mass_properties_deck_semantics.md`

## NASA/MSC Flight Control Division Mission Operations Report — Apollo 13

- Date: 28 April 1970
- Organization: NASA Manned Spacecraft Center, Flight Control Division
- NTRS record/download: `19710010485`
- NASA History scan: `https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf`
- Source class: primary mission-specific controller report
- Relevant section: Flight Dynamics chronology

### Source-evidence policy

The report explicitly says that it describes Apollo 13 flight operations as seen in real time and that no data is used except data available in real time, even where post-mission information later showed the real-time data to be erroneous. Accordingly, chronology entries below are classified as operational real-time evidence rather than postflight reconstruction.

### T+N mass-properties semantics

The same chronology uses the T+N convention repeatedly:

- liftoff `T-6` mass properties (weights, c.g.'s, aerodynamics) were generated and loaded in RTCC before launch;
- `T+25` RTCC mass properties were run and compared with `T+6` trims;
- RTCC LM-burn mass-property decks were later updated to `T+55` decks.

This supports classifying `T+6`, `T+25`, and `T+55` as time-tagged mass-properties set/deck labels or reference epochs. It does **not** support treating `T+55` as a calculation timestamp or RTCC job number. The T+55 update entry appears before the chronology's 53:26 and 54:25 GET LM-ingress entries, so the source does not imply that generation/loading occurred exactly at 55:00 GET.

### T+25 mass-properties update precedent

Before MCC-2, the chronology states that the **T+25 RTCC mass properties were run but an update was not needed because pitch/yaw trims were within `0.01°` of T+6**.

Supports a mission-specific workflow:

`time-tagged mass-properties set -> RTCC mass-properties run -> pitch/yaw trim comparison -> update/no-update decision`

Boundary: `0.01°` is established only for this T+25-versus-T+6 decision. It is not evidence of a universal RTCC rule or the later PC+2 acceptance criterion.

### T+55 and ~59 GET PC+2 provenance

The chronology states that:

- RTCC **LM-burn mass-property decks were updated to T+55 decks**;
- a PC+2 abort/block-data pad was passed at approximately 59 GET;
- the DPS trim passed on that pad was challenged by LM CONTROL;
- CONTROL had used **premission mass properties**, described as not the best data available;
- CONTROL later agreed with Flight Dynamics' data.

This places the T+55 reference-epoch deck family and the PC+2 trim dispute in the same explicitly real-time Flight Dynamics record. It strengthens the hypothesis that newer operational mass-properties data explain why Flight Dynamics' solution superseded CONTROL's premission calculation.

Boundary: the report still does not print the T+55 deck contents or generation/load time, CONTROL's alternative trim, comparison delta, PC+2 acceptance criterion, RTCC/RTACF job identifier, or explicitly state that the specific passed PC+2 trim calculation consumed the T+55 deck. T+55 therefore remains strong contextual real-time provenance, not a closed calculation-level link.

## NASA Apollo 13 air-to-ground / mission voice record — ~59:03 GET

- Relevant GET: approximately 59:03–59:05
- Source class: primary mission voice transcription

### Supports

- CAPCOM identifies the two values as DPS trim/GDA angles for PC+2.
- Crew readback gives pitch `5.86°` and roll `6.75°`.
- CAPCOM accepts the readback.

### Joined finding

The time, maneuver, pad, and passed DPS-trim event coincide with the Flight Dynamics report's ~59 GET PC+2 abort-pad dispute. The pair can therefore be classified as the **Flight Dynamics PC+2 abort-pad trim solution passed to the crew at ~59 GET**.

## MSC Internal Note 70-FM-20 — The Apollo 11 Adventure

- Date: 5 February 1970
- Organization: NASA Manned Spacecraft Center, Flight Dynamics organization
- Source class: primary contemporary adjacent-mission Flight Dynamics report
- Relevant section: RTACF computational capability / mass properties

### Supports

- RTACF mass-properties computations included **weight-c.g. tables**.
- Those weight-c.g. tables were used by **RTACF and RTCC trajectory processors to compute pitch and yaw trim angles**.
- This identifies a concrete computational artifact chain to target when searching for the Apollo 13 ~59 GET trim disagreement.

### Boundary

This is Apollo 11 / Mission G architecture evidence, not Apollo 13 calculation provenance. It does not prove that Apollo 13 used the same RTACF program, job/request procedure, output format, or that `5.86 / 6.75` came from RTACF rather than RTCC. It also does not link a T+55 table directly to that pair.

## NASA/MSC Apollo 13 Mission Report — Appendix A.5, Table A-I

- Report: *Apollo 13 Mission Report*, MSC-02680, September 1970
- NASA NTRS citation: `19710003598`
- Primary PDF: `https://ntrs.nasa.gov/api/citations/19710003598/downloads/19710003598.pdf`
- Source class: primary mission-specific postflight engineering report

### Supports

For the event labeled **Second midcourse correction**, Table A-I reports ignition 95,959.9 lb with c.g. X/Y/Z = 378.8 / 4.9 / 0.7 in, and cutoff 95,647.1 lb with c.g. X/Y/Z = 379.4 / 5.0 / 0.7 in.

### Boundary

The report describes these mass properties as conditions determined from postflight analyses of expendable loadings and usage during flight. They are not evidence that the same numerical values were loaded in the real-time T+55 Flight Dynamics deck, used by CONTROL, or consumed by the ~59 GET trim calculation. Treat them as a mission-specific postflight validation reference only.

## NASA Apollo 13 mission commentary — post-61:29 revised PC+2 pad

- Relevant GET: approximately 63:05–63:10
- Source class: primary mission voice/PAO transcription

### Supports

- CAPCOM says the GDA should be okay as it is from the last burn and gives pitch `5.85`, roll `6.74`.
- Crew readback says the GDA should be okay as is and qualifies the pair with "hopefully."

### Boundary

The `0.01°` difference on each axis from the ~59 GET `5.86 / 6.75` solution does not establish a comparison tolerance, recomputation method, or measured actuator change. The separate T+25 `0.01°` no-update precedent does not justify importing that criterion into PC+2.

## Current provenance chain

`Apollo 13 T+25 mass-properties run -> P/Y trims within 0.01° of T+6 -> no update [mission-specific real-time workflow precedent]`

`Apollo-era mass-properties architecture: weight/c.g. table -> RTACF/RTCC trajectory processor -> pitch/yaw trim [Mission G architecture evidence]`

`Apollo 13 RTCC LM-burn mass-properties reference epoch updated to T+55 [mission-specific real-time context; generation/load time unresolved] -> Flight Dynamics ~59 GET PC+2 calculation [job/deck linkage unresolved] -> passed DPS trim 5.86 / 6.75 -> LM CONTROL challenge using premission mass properties -> CONTROL later agrees with Flight Dynamics data -> 61:29 powered-flight compliance -> later PC+2 "as is" reference 5.85 / 6.74 [generation mechanism unresolved]`

`Apollo 13 Mission Report Table A-I postflight reconstructed mass properties [validation layer; not real-time deck provenance]`

## Next source target

Recover Apollo 13 **real-time** weight/c.g. or mass-properties computation output and the associated RTACF/RTCC trajectory-processor trim artifact/request sheet for the ~59 GET disagreement. Keep reference epoch, generation/load time, and job identity separate. Highest-value fields remain CONTROL's alternative values, PC+2-specific comparison/acceptance basis, job identity, and explicit T+55-deck-to-job/input provenance.