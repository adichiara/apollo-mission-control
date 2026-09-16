# Apollo 13 PC+2 ~59 GET trim-provenance sources

Date: 2026-09-16  
Related notes: `resources/research/170_pc2_59h_trim_provenance.md` through `resources/research/179_preburn_gda_checkout_acceptance_bound.md`

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

## MSC Internal Note 70-FM-20 — The Apollo 11 Adventure

Contemporary adjacent-mission architecture evidence: RTACF mass-properties computations produced weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles. This identifies an artifact class, not Apollo 13 calculation provenance.

## NASA/MSC Apollo 13 Mission Report — Appendix A.5, Table A-I

- Report: *Apollo 13 Mission Report*, MSC-02680, September 1970
- NTRS citation: `19710003598`

Postflight validation values for the second midcourse correction: ignition 95,959.9 lb, c.g. 378.8 / 4.9 / 0.7 in; cutoff 95,647.1 lb, c.g. 379.4 / 5.0 / 0.7 in. These are postflight values, not the real-time T+55 deck.

## Current provenance chain

`T-6 -> generated -> loaded in RTCC`

`T+25 -> RTCC mass-properties run -> P/Y comparison -> within 0.01° -> no update`

`T+55 -> RTCC LM-burn decks updated -> generation/load/run consumption unresolved`

`~59 Flight Dynamics PC+2 calculation -> 5.86 / 6.75 -> CONTROL challenge using premission mass properties -> reconciliation -> same pair commanded for 61:29 -> preburn spacecraft gimbal checkout within ~0.3 judged plenty close -> powered-flight compliance -> exact resulting GDA state unrecovered -> later PC+2 as-is reference 5.85 / 6.74`

## Next source target

Recover Apollo 13 T+55 real-time weight/c.g. output plus an explicit generation/load or downstream RTACF/RTCC LM-burn run/request/output artifact. Highest-value fields remain CONTROL's alternative values, **ground-computation** PC+2 comparison/acceptance basis, job identity, explicit T+55-deck-to-`5.86 / 6.75` lineage, and exact post-61:29 complied GDA state. Do not substitute either the T+25 `0.01°` comparison or the 61:11 `~0.3°` spacecraft checkout for the missing computational criterion.