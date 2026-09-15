# Apollo 13 PC+2 RTCC mass-properties sources

## NASA — Flight Control Division, Mission Operations Report — Apollo 13

- Date: 1970-04-28
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf
- Source class: primary / mission-specific Flight Control Division report

### Supports

- `T-6`, `T+6`, `T+25`, and `T+55` operational mass-properties lineage; `T±N` is not generation/loading time;
- ~59-hour PC+2 trim challenge caused by LM Control using inferior premission mass properties, followed by agreement with Flight Dynamics;
- final PC+2 pad at about GET 78 hours based on GYM 289;
- late-entry mass properties **job 27**, proving numbered job identity but not identifying the PC+2 job;
- LM CONTROL PC+2 execution narrative: at ignition the roll GDA actuator displacement moved to approximately `-2 in`, a `-1.2 in` change from its pre-ignition value, implying an approximate pre-ignition displacement of `-0.8 in`.

### Boundary

The report proves that the ~59-hour interim product was superseded, but it does not provide the complete final commanded angular trim pair, identify the PC+2 mass-properties job, or explicitly tie the final trim to `T+55`. The inferred `-0.8 in` is an approximate actuator state, not a recovered pad field. Research note 154 corrects earlier project references that mislabeled these actuator quantities as degrees.

## Apollo 13 restored mission-audio transcript — GET ~59:01–59:05

- Presentation: https://apollo13realtime.org/
- Source class: restored/edited transcript of mission audio; corroborating operational evidence

### Supports

CAPCOM reads an interim PC+2 DPS GDA angular pair `5.86°` and `6.75°` and explicitly says the angles **will be updated**. The exchange contains inconsistent axis wording; Haise's accepted readback gives **pitch `5.86°` / roll `6.75°`**. Project documentation should not normalize the second value to yaw.

### Boundary

These are interim/update-expected angular values. Do not assign them specifically to `T+55`, infer a job number, assume they survived into the final ~78-hour solution, or compare them numerically with later GDA actuator displacement in inches.

## NASA MSC — Apollo 12 Flight Control Division postflight report, RETRO

- Mission: Apollo 12
- Archival scan: https://www.ibiblio.org/apollo/Documents/Apollo_12_Postflight_Report_RETRO.pdf
- Source class: primary / immediately preceding mission

Supports controller-run pre-maneuver mass-properties calculations in an offline computer in lieu of RTACF and SPS trims agreeing within 0.1° with onboard postburn values. Architectural/workflow evidence only; do not project exact Apollo 12 implementation into H-2.

## NASA MSC — Apollo 13 Mission Report

- Date: 1970-09
- Report: `MSC-02680` / `NASA-TM-X-66449`
- NTRS: https://ntrs.nasa.gov/citations/19710003598
- Source class: primary / mission-specific postflight mission report

Appendix A defines mass properties as postflight reconstructions from expendable loading/usage and spacecraft-property data. PC+2/TEI mass is `95,424.0 lb` ignition / `87,456.0 lb` cutoff. This is not demonstrated as an RTCC targeting input. Its `508 lb` difference from the final P30 module-weight sum (`95,932 lb`) compares distinct product classes.

The maneuver-performance table also explicitly reports **Gimbal drive actuator, in.** For PC+2 it gives a postflight actuator trace including initial pitch/roll `+0.13 / -0.28 in`, roll maximum excursion `-0.44 in`, steady-state pitch/roll `-0.21 / -0.55 in`, and cutoff pitch/roll `+0.23 / -0.85 in`.

### GDA boundary

These are postflight physical actuator-displacement values, not the missing final commanded angular trim pair. Do not convert inches to degrees without sourced GDA geometry/calibration. The exact sampling relationship between this table and LM CONTROL's larger ignition-transient narrative is unresolved.

## NASA MSC Internal Note 71-FM-214 — Skylab RTCC Mass Properties System Requirements

- Date: 1971-06-14
- Identifiers: `MSC-04378`, `MSC-IN-71-FM-214`, `NASA-TM-X-67442`
- NTRS: https://ntrs.nasa.gov/citations/19720006192
- Source class: primary NASA RTCC requirements documentation explicitly describing carryover of the Apollo RTCC Mass Properties System

Supports module summation, total weight/CG state, engine-trim calculations from weight/CG, and temporary/permanent propellant depletion tables. Architecture only; not H-2 deck contents.

## NASA MSC Mission Planning and Analysis Division — Apollo 11 Mission Support Section

- Archival scan: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- Source class: primary Apollo operational-support documentation

Supports `mass-properties weight/CG tables -> RTACF/RTCC trajectory processors -> pitch/yaw trim outputs` and updateable mass-properties/thrust constants. Architecture only; not Apollo 13 values or software identity.

## Project rule

Keep separate: physical mass/CG; postflight reconstructed mass; RTCC deck/state; depletion state; reference epoch; load timestamp; calculation provenance/run/job identity; processor inputs/outputs; P30 module weights; commanded angular trim; GDA actuator displacement; sampled/postflight actuator trace; ignition compliance response; and product lifecycle/finality.

Do not label `62480 + 33452` as exact physical ignition mass, inject `95424.0 lb` into RTCC without evidence, assign job 27 to PC+2, treat the ~59-hour angular pair as final, or silently mix angular GDA trim with actuator inches.

## Next archival target

Highest value remains the final ~78-hour PC+2 P30/GDA artifact, Flight Director Log page, or H-2 Flight Dynamics/CONTROL worksheet that gives the complete superseding angular trim pair and connects it to a numbered mass-properties job/run and/or `T+55`. Also seek LM GDA calibration/geometry documentation and Apollo 13 Mission Report Supplement 2 to reconcile commanded angle, actuator displacement, and postflight trace.