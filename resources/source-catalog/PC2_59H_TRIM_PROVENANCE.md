# Apollo 13 PC+2 ~59 GET trim-provenance sources

Date: 2026-09-16  
Related notes: `resources/research/170_pc2_59h_trim_provenance.md` through `resources/research/177_mass_properties_operation_verb_boundary.md`

## NASA/MSC Flight Control Division Mission Operations Report — Apollo 13

- Date: 28 April 1970
- Organization: NASA Manned Spacecraft Center, Flight Control Division
- NTRS record/download: `19710010485`
- NASA History scan: `https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf`
- Source class: primary mission-specific controller report

### Supports

- The report describes Apollo 13 flight operations using real-time-available data.
- For T-6, mass properties (weights, c.g.'s, aerodynamics) were **generated** and **loaded in the RTCC** by T-2:46.
- The T+25 RTCC mass properties were **run** and their pitch/yaw trims compared with T+6; no update was needed because they were within `0.01°`.
- Later, **"RTCC (LM burn) mass property decks were updated to T+55 decks."**
- A PC+2 abort/block-data pad was passed at approximately 59 GET.
- LM CONTROL challenged the DPS trim on that pad using premission mass properties, then later agreed with Flight Dynamics' data.
- CONTROL later expected the GDA state resulting from the 61:29 free-return maneuver's 40% powered-flight compliance to provide optimum PC+2 alignment.

### Joined provenance finding

The chronology distinguishes `generated`, `loaded in the RTCC`, `mass properties were run`, and `decks were updated`. These operations are therefore retained as separate provenance events. T+55 is directly source-backed as an RTCC LM-burn deck update/reference-set state; the statement does not independently establish generation, load time, or a downstream trim run.

### Boundary

The report does not print the T+55 deck contents, generation/load time, downstream run/request/output, CONTROL's alternative trim, comparison delta, PC+2 acceptance criterion, RTCC/RTACF job identifier, or explicitly state that the `5.86 / 6.75` calculation consumed the T+55 deck. The T+25 `0.01°` result is not generalized into a PC+2 threshold.

## NASA Apollo 13 air-to-ground record — ~59:03 GET

- Source class: primary mission voice transcription

### Supports

- CAPCOM passes pitch `5.86°`, roll `6.75°` with the PC+2 DPS abort pad.
- CAPCOM says these gimbal trim angles **"will be updated"** but instructs the crew to use them for the moment.
- Crew identifies them as DPS trim/GDA angles and reads them back; CAPCOM accepts the readback.

## NASA Apollo 13 Technical Air-to-Ground Voice Transmission — 60:53–60:56 GET

- NASA PDF: `https://www.nasa.gov/wp-content/uploads/2026/01/as13-tec.pdf`
- Relevant transcript: tape 41/9–41/10, pages 217–218
- Source class: primary mission voice transcription

### Supports

- CAPCOM passes the P30 pad for the 61:29:42.84 free-return midcourse correction.
- The pad explicitly gives LM GDA pitch `5.86°`, roll `6.75°`.
- Haise reads the same pair back and CAPCOM accepts it.

### Boundary

This does not prove that the exact post-compliance actuator state remained `5.86 / 6.75`, nor that the same RTCC/RTACF job generated both maneuver products.

## MSC Internal Note 70-FM-20 — The Apollo 11 Adventure

- Date: 5 February 1970
- Organization: NASA Manned Spacecraft Center, Flight Dynamics organization
- Source class: primary contemporary adjacent-mission Flight Dynamics report

### Supports

RTACF mass-properties computations included weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch and yaw trim angles. This identifies a concrete computational artifact class to target for Apollo 13.

### Boundary

This is Apollo 11 architecture evidence, not Apollo 13 calculation provenance.

## NASA/MSC Apollo 13 Mission Report — Appendix A.5, Table A-I

- Report: *Apollo 13 Mission Report*, MSC-02680, September 1970
- NASA NTRS citation: `19710003598`
- Primary PDF: `https://ntrs.nasa.gov/api/citations/19710003598/downloads/19710003598.pdf`
- Source class: primary mission-specific postflight engineering report

### Supports

For the event labeled Second midcourse correction, Table A-I reports ignition 95,959.9 lb with c.g. X/Y/Z = 378.8 / 4.9 / 0.7 in, and cutoff 95,647.1 lb with c.g. X/Y/Z = 379.4 / 5.0 / 0.7 in.

### Boundary

These are postflight-analysis values, not evidence for the real-time T+55 deck or ~59 GET trim calculation.

## NASA Apollo 13 mission commentary — post-61:29 revised PC+2 pad

- Relevant GET: approximately 63:05–63:10
- Source class: primary mission voice/PAO transcription

### Supports

CAPCOM says the GDA should be okay as it is from the last burn and gives pitch `5.85`, roll `6.74`; crew readback qualifies the numerical identification with "hopefully."

### Boundary

The `0.01°` difference on each axis from `5.86 / 6.75` does not establish a comparison tolerance, recomputation method, or measured actuator change.

## Current provenance chain

`T-6 mass properties -> generated -> loaded in RTCC [explicit operation precedent]`

`T+25 RTCC mass properties -> run -> P/Y trims compared with T+6 -> within 0.01° -> no update [explicit run precedent]`

`T+55 reference epoch -> RTCC LM-burn mass-property decks updated -> generation/load/run consumption unresolved`

`Apollo-era architecture: weight/c.g. table -> RTACF/RTCC trajectory processor -> pitch/yaw trim [adjacent-mission evidence]`

`Flight Dynamics ~59 GET PC+2 calculation -> provisional DPS trim 5.86 / 6.75 -> LM CONTROL challenge using premission mass properties -> CONTROL later agrees -> same 5.86 / 6.75 commanded for 61:29 free-return DPS burn -> 40% powered-flight compliance -> exact resulting GDA state unrecovered -> later PC+2 "as is" reference 5.85 / 6.74 [not actuator telemetry]`

## Next source target

Recover Apollo 13 T+55 real-time weight/c.g. output plus an explicit generation/load or downstream RTACF/RTCC LM-burn run/request/output artifact. Highest-value fields remain CONTROL's alternative values, PC+2-specific comparison/acceptance basis, job identity, explicit T+55-deck-to-`5.86 / 6.75` data lineage, and the exact two-axis post-61:29 complied GDA state.