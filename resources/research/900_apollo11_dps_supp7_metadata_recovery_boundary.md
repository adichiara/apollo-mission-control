# Research note 900 — Apollo 11 DPS Supplement 7 metadata and recovery boundary

Date: 2026-09-24
Research thread: `apollo11-descent-dynamics-runtime`

## Question

What can be established from primary NASA records about Apollo 11 Mission Report Supplement 7, *Descent Propulsion System, Final Flight Evaluation*, before the report body itself is recovered?

## Primary evidence

NASA/MSC's controlled-document index (NTRS 19900007273) lists MSC-00171 and its supplements. For Supplement 7 it gives:

- title: **Descent Propulsion System, Final Flight Evaluation**;
- item-level date: **03-28-70**;
- responsible author: **R. K. Seto**.

Later NASA mission-report supplement tables preserve a different metadata value. The Apollo 13 Mission Operations Report (28 April 1970) lists Apollo 11 Supplement 7 with publication date/status **September 1970**; later Apollo mission reports repeat September 1970.

These records need not be forced into a single date. The controlled-document index supplies an item-level date while the mission-report appendix explicitly labels its column publication date/status. Until the report title page/body is recovered, retain both with their source semantics.

## Retrieval boundary

The ordinary historical NTRS Apollo index exposes Apollo 11's main mission reports and Supplement 5, but does not expose Supplement 7 as a normal downloadable Apollo 11 item. This is evidence of a current public-digital recovery gap, not evidence that the report no longer exists.

The report body has **not** been recovered in this research pass. Therefore this note does not assert LM-5 as-flown thrust, specific impulse, mixture ratio, engine calibration, uncertainty, or a TRW contractor-report number.

## Modeling consequence

The powered-descent runtime may use already sourced mission-event/checkpoint evidence, but a continuous LM-5 propulsion model must not be presented as historically calibrated from Supplement 7 until the report body or equivalent LM-5 primary performance data are recovered.

## Sources

- NASA/MSC controlled-document index, NTRS document 19900007273, MSC-00171 entry.
- NASA, *Mission Operations Report: Apollo 13*, 28 April 1970, table E-I.
- NASA Apollo mission-report appendix tables retaining the September 1970 publication value.
- Historical NTRS Apollo document index, used only to characterize the current public-digital retrieval gap.

## Evidence status

- **CLOSED:** Supplement 7 identity, title, R. K. Seto attribution, and the existence of two differently scoped date fields.
- **OPEN:** report-body recovery and LM-5 as-flown propulsion/calibration values.
- **BLOCKED:** historically calibrated continuous LM-5 DPS dynamics from this source until the body or equivalent primary evidence is recovered.
