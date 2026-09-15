# Apollo 13 PC+2 DPS performance sources

## NASA — Flight Control Division, Mission Operations Report — Apollo 13

- Date: 1970-04-28
- Report: MSC-02680
- NASA/Apollo Journal scan: https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- Source class: primary / mission-specific Flight Control Division report

### Supports

- PC+2 TIG `079:27:38.30`;
- actual Flight Dynamics burn duration `4:23.82`;
- staged PC+2 operational throttle profile: initial 12.6-percent region, 40-percent region, then maximum thrust;
- terminal regulator-isolation/blowdown operation;
- operational significance of non-instantaneous DPS thrust buildup, documented during a later Apollo 13 DPS maneuver;
- CONTROL's separate GDA/trim execution observations and the mass-properties/trim reconciliation history;
- RTCC LM-burn mass-property decks updated to `T+55` before early LM ingress;
- ~59-hour CONTROL challenge to Flight Dynamics trim because CONTROL had used premission mass properties, followed by agreement with Flight Dynamics.

### Boundary

The report does not provide a complete numerical LM-7 PC+2 thrust-versus-time or mass-flow history, nor does the recovered material identify the complete later PC+2 commanded GDA trim pair or its mass-properties job number. The surrounding T+55 narrative does not by itself prove a numbered job or exact calculation provenance for a particular trim pair.

## NASA — Apollo 13 technical air-to-ground transcription, ~59-hour contingency PC+2 and 61:29 free-return DPS burn

- Relevant times: GET ~`059:03` and `060:53`
- Corrected transcript navigation: https://www.apollojournals.org/afj/ap13fj/09day3-lifeboat.html
- Source class: primary mission voice transcription; corrected transcript used as navigation aid

### Supports

- ~59-hour contingency PC+2 GDA pair: pitch `5.86°`, roll `6.75°`;
- CAPCOM explicitly says the PC+2 pair **will be updated**;
- for the actual free-return DPS maneuver at TIG `061:29:42.84`, CAPCOM transmits the **same** pitch `5.86°`, roll `6.75°` pair;
- the free-return burn read-up also gives 5 seconds at 10-percent throttle followed by 40 percent and two-jet 10-second ullage.

### Boundary

This proves that `5.86° / 6.75°` became an operationally accepted near-term DPS trim and was used for the actual free-return burn; it was not merely a discarded contingency value. It does not prove a specific numbered mass-properties job, a direct mathematical derivation from T+55, or that the pair remained final for PC+2. Preserve maneuver applicability and lifecycle/finality separately.

## NASA — Apollo 13 technical/PAO air-to-ground transcription, final PC+2 P30 read-up

- Relevant time: GET `077:55:24`
- NASA transcript PDF: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- Corrected transcript navigation: https://www.apollojournals.org/afj/ap13fj/13day4-leaving-moon.html
- Source class: primary mission voice transcription; corrected transcript used as navigation aid

### Supports

- final transmitted P30 fields: TIG `079:27:38.30`, Noun 81 `+0833.0/-0050.9/-0213.9`, HP `+0020.5`, resultant `0861.5`, duration `4:24`, attitude `272/081`;
- final communicated module weights `62480` lb CSM and `33452` lb LM;
- two-jet 10-second ullage and staged throttle comments;
- critically, after the attitude fields CAPCOM states **"the rest is N/A except for comments"** and does not transmit a GDA trim pair.

### Boundary

The omission proves only that the final crew-facing P30 targeting PAD did not contain GDA trim. It does not prove that no later/superseding trim existed, identify how it was generated or set, or connect it to a specific mass-properties job/`T+55` state. Treat the trajectory/P30 product and GDA trim product as separate provenance chains.

## NASA — Apollo 13 Mission Report

- Date: 1970-09
- NTRS document: https://ntrs.nasa.gov/citations/19710003598
- Source class: primary / mission evaluation
- Relevant section: 6.6, Descent Propulsion

### Supports

- normal DPS engine start/throttle response overall;
- PC+2 / transearth-injection duration approximately 264 s;
- pressurization isolation solenoid closed approximately 15 s before shutdown;
- completion of PC+2 in blowdown mode with residual helium as the sole pressure source.

### Boundary

This report does not provide a PC+2-specific calibrated thrust, Isp, mixture-ratio, or mass-flow time history.

## NASA — Report of Apollo 13 Review Board

- Date: 1970-06
- NTRS record: https://ntrs.nasa.gov/citations/19700076776
- Apollo Journal scan: https://apollojournals.org/afj/ap13fj/pdf/report-of-a13-review-board-19700615-19700076776.pdf
- Source class: primary / Apollo 13 configuration baseline

### Supports

- DPS throttleable range 1050–6300 lbf;
- throttle positions above that range produce full thrust;
- nominal full thrust `9870 lbf`;
- descent engine gimbaled and restartable.

### Boundary

`9870 lbf` is a mission/configuration **nominal full-thrust value**, not proof of constant measured PC+2 full-thrust delivery.

## NASA TN D-7143 — Apollo Experience Report: Descent Propulsion System

- NTRS: https://ntrs.nasa.gov/citations/19730011150
- Date: 1973-03
- Source class: primary NASA engineering retrospective / general DPS design

### Supports as general design context

- maximum rated thrust `10,500 lbf`;
- fixed throttle point at 92.5 percent of rated thrust;
- minimum throttle point 10 percent;
- 65–92.5 percent treated as a nonoperating thrust region;
- design specific impulse at end of duty cycle `305 lbf-sec/lbm`.

### Boundary

These are fleet/design-level values. Do not relabel them as LM-7 PC+2 measured performance without a mission/configuration bridge.

## Related adjacent-mission postflight evaluations

NTRS catalogs dedicated DPS final-flight evaluations for Apollo 10, Apollo 12, Apollo 14, and Apollo 15. These are useful for method discovery and terminology, but their numerical performance values are not Apollo 13/LM-7 evidence.

Examples:

- Apollo 10 LM-4 DPS final flight evaluation: https://ntrs.nasa.gov/citations/19690026326
- Apollo 12 DPS final flight evaluation: https://ntrs.nasa.gov/citations/19730078844
- Apollo 14 LM-8 DPS final flight evaluation: https://ntrs.nasa.gov/citations/19730021081
- Apollo 15 LM-10 DPS final flight evaluation: https://ntrs.nasa.gov/citations/19730023018

### Adjacent-report provenance useful for Apollo 13 retrieval

Primary NTRS catalog records establish a repeated contractor/reporting lineage:

- Apollo 10 LM-4: R. K. M. Seto, TRW Systems Group, `TRW-11176-H314-R0-001`, `NASA-CR-101869`, contract `NAS9-8166`.
- Apollo 12: R. K. M. Seto / R. L. Barrows, `TRW-11176-H585-R0-00-SUPPL-5`, `MSC-01855-SUPPL-5`, `NASA-TM-X-68933`, contract `NAS9-8166`.
- Apollo 14 LM-8: A. T. Avvenire / S. C. Wood, TRW Systems Group, `TRW-17618-H219-R0-00-SUPPL-5`, `MSC-04112-SUPPL-5`, `NASA-TM-X-69491`, contract `NAS9-8166`.

This supports using `TRW Systems Group` and `NAS9-8166` as search terms for the missing Apollo 13 report. It does **not** prove an Apollo 13 TRW report number, author, or numerical applicability.

## Project rule

For historical PC+2 numerical validation, keep **trajectory/P30 targeting product**, **GDA trim product**, **trim maneuver applicability/finality**, **commanded throttle state**, **delivered thrust history**, **specific impulse/mass flow**, and **pressurization/blowdown state** as separate concepts until primary evidence supports collapsing any of them.

## Apollo 13 Mission Report Supplement 2 — publication status and retrieval

- Source: *Apollo 13 Mission Report*, September 1970
- NTRS: https://ntrs.nasa.gov/citations/19710003598
- Source class: primary / mission report publication-status table

### Supports

Appendix E lists:

- Apollo 13 Supplement 2;
- title: *Descent Propulsion System Final Flight Evaluation*;
- status: **Preparation**.

### Later official status

Later NASA mission-report supplement tables (Apollo 14 through at least Apollo 16, with Apollo 17 as an additional cross-check) list Apollo 13 Supplement 2 with publication date **October 1970**.

Representative sources:

- Apollo 14 Mission Report: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap14fj/pdf/a14_mission-report.pdf
- Apollo 15 Mission Report Appendix E: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a15/a15mrp9.pdf
- Apollo 16 Mission Report, NTRS 19720026127: https://ntrs.nasa.gov/citations/19720026127

### Retrieval boundary

The October 1970 publication date is established. A direct public copy/report identifier is still unrecovered. Exact-title and `MSC-02680-SUPPL-2` searches do not currently expose an authoritative direct record.

`MSC-02680-SUPPL-2` remains a **structurally plausible archival search key only**. Do not cite it as the verified report number until a primary catalog record, scan, cover page, citation, or distribution record confirms it.

### Refined archival priority after research note 141

Search using the combined primary-supported provenance tuple:

`Apollo 13 + LM-7 + Descent Propulsion System Final Flight Evaluation + October 1970 + TRW Systems Group + NAS9-8166 + MSC-02680`

Prioritize NASA/NTRS catalog backfiles, MSC/JSC report indexes, NARA technical-report holdings, and TRW/Northrop Grumman legacy bibliographies before substituting adjacent-mission numerical values.