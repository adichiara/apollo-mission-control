# Apollo 13 PC+2 ~59 GET trim-provenance sources

Date: 2026-09-16  
Related notes: `resources/research/170_pc2_59h_trim_provenance.md` through `resources/research/189_rtacf_mass_properties_processor_contract.md`

## NASA/MSC Flight Control Division Mission Operations Report — Apollo 13

- Date printed on report: 28 April 1970
- Organization: NASA Manned Spacecraft Center, Flight Control Division
- NASA History/ALSJ scan historically cataloged at `A13_MissionOpReport.pdf`
- NTRS citation `19710010485` has a documented metadata/payload mismatch; see note 178.
- Source class: primary mission-specific controller report

### Supports
- T-6 mass properties (weights, c.g.'s, aerodynamics) generated and loaded in RTCC.
- T+25 RTCC mass properties run and P/Y trims compared with T+6; no update because within `0.01°`.
- RTCC LM-burn mass-property decks later updated to T+55 decks.
- ~59 GET PC+2 pad and LM CONTROL challenge using premission mass properties; CONTROL later agreed with Flight Dynamics' data.
- CONTROL expected 61:29 powered-flight compliance to leave optimum PC+2 GDA alignment.

### Boundary
T+55 deck update is not proof of generation/load/downstream run. The report does not print T+55 deck contents, CONTROL's alternative trim, comparison delta, PC+2 computational acceptance criterion, job identity, or direct T+55-to-`5.86 / 6.75` linkage. T+25 `0.01°` is not generalized to PC+2.

## NASA/MSC Operational Support Plan for the RTACF — Apollo 10 Flight Annex

- Organization: NASA Manned Spacecraft Center
- Source class: primary contemporary RTACF operations documentation; adjacent mission
- Public scan: `https://www.ibiblio.org/apollo/Documents/Operational%20Support%20Plan%20for%20the%20Real-Time%20Auxiliary%20Computing%20Facility%20Apollo%2010%20Flight%20Annex.pdf`

### Supports
- RTACF Systems programs updated CSM and LM mass properties to reflect consumables usage and vehicle reconfiguration.
- One Systems program computed mass properties for a specified CSM/LM configuration.

### Boundary
Architecture evidence only. It does not identify the Apollo 13 T+55 job, inputs, output values, or requestor.

## MSC Internal Note 70-FM-20 — The Apollo 11 Adventure

- Date: 5 February 1970
- Organization: NASA Manned Spacecraft Center, Mission Planning and Analysis Division
- Public scan: `https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf`
- Source class: primary contemporary adjacent-mission mission-support report

### Supports
- RTACF mass-properties computations included **weight-c.g. tables**.
- Those tables were used by **RTACF and RTCC trajectory processors to compute pitch and yaw trim angles**.
- RTACF constants-update capability included mass-properties tables.

### Provenance significance
Together with the Apollo 10 operations plan, this establishes a source-backed generic processor contract:

`configuration + consumables -> mass-properties / weight-c.g. product -> RTACF/RTCC trajectory processor -> pitch/yaw trim`

Apollo 13's T+55 LM-burn deck is therefore the correct class of upstream product, but direct consumption by the `5.86 / 6.75` calculation remains unproven.

## NASA Apollo 13 air-to-ground — ~59:03 GET

CAPCOM passes pitch `5.86°`, roll `6.75°` with the PC+2 DPS abort pad, says the angles "will be updated," and accepts the crew readback.

## NASA Apollo 13 Technical Air-to-Ground Voice Transmission — 60:53–60:56 GET

- NASA PDF: `https://www.nasa.gov/wp-content/uploads/2026/01/as13-tec.pdf`
- Source class: primary mission voice transcription

The 61:29 free-return P30 pad uses the same `5.86 / 6.75` GDA pair and the crew readback is accepted.

## Apollo 13 Flight Director loop — 61:03–61:12 GET

- Presentation/transcription: `https://apollo13realtime.org/`
- Underlying evidence: recovered NASA mission-control audio

CONTROL directs the gimbal-trim checkout. After the procedure CONTROL says `Trim looks okay`; when FLIGHT asks how close, CONTROL answers `within about 0.3` and `plenty close`, then reports readiness.

### Provenance significance
This supplies a mission-specific **spacecraft checkout acceptance** value/context. It does not close the ~59 GET **ground-computation comparison** gap. The repository therefore models these as different acceptance layers.

## NASA/MSC Apollo 13 Mission Report — Appendix A.5, Table A-I

- Report: *Apollo 13 Mission Report*, MSC-02680, September 1970
- NTRS citation: `19710003598`

Postflight validation values for the second midcourse correction: ignition 95,959.9 lb, c.g. 378.8 / 4.9 / 0.7 in; cutoff 95,647.1 lb, c.g. 379.4 / 5.0 / 0.7 in. These are postflight values, not the real-time T+55 deck.

The same mission report separately establishes that the 61:29 firing used primary guidance/AUTO with nominal guidance performance and no reported vehicle attitude excursions. Section 6.6 gives the executed firing as 34.3 seconds, ~12% minimum throttle for 5 seconds followed by approximately 37%. These postflight execution facts constrain simulation but do not recover trim-calculation provenance or exact GDA actuator history.

## Apollo 13 GN&C performance-analysis supplement

- NTRS citation: `19730017939`
- Report: `MSC-02680-SUPPL-1` / `TRW-11176-H586-R0-00-SUPPL-1`

Mission-specific primary postflight GN&C analysis including the LM digital autopilot. Treat as a priority archival target for the exact-actuator-state branch; do not attribute gimbal-position values until the relevant pages/data are inspected.

## Current provenance chain

`configuration + consumables -> [generic Apollo RTACF mass-properties processor contract] -> mass-properties / weight-c.g. product -> RTACF/RTCC trajectory processor -> pitch/yaw trim`

`T-6 -> generated -> loaded in RTCC`

`T+25 -> RTCC mass-properties run -> P/Y comparison -> within 0.01° -> no update`

`T+55 -> RTCC LM-burn decks updated -> mission-specific generation/load/run consumption unresolved`

`~59 Flight Dynamics PC+2 calculation -> 5.86 / 6.75 -> CONTROL challenge using premission mass properties -> reconciliation -> same pair commanded for 61:29 -> preburn spacecraft gimbal checkout within ~0.3 judged plenty close -> primary-guidance/AUTO firing nominal, no reported attitude excursions -> automatic powered-flight trim available -> exact resulting GDA state unrecovered -> later PC+2 as-is reference 5.85 / 6.74`

## Next source target

Recover Apollo 13 T+55 real-time weight/c.g. output plus an explicit generation/load or downstream RTACF/RTCC LM-burn run/request/output artifact. Highest-value fields remain CONTROL's alternative values, **ground-computation** PC+2 comparison/acceptance basis, job identity, and explicit T+55-deck-to-`5.86 / 6.75` lineage. The generic mass-properties-to-trim processor relationship is now closed; do not mistake that architecture closure for mission-specific run provenance. Do not substitute the T+25 `0.01°`, the 61:11 `~0.3°` checkout, or stable vehicle attitude for the missing computational criterion.