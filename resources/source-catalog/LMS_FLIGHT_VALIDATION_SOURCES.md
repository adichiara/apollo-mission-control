# LMS flight-derived validation sources

Status: **active source catalog; research use is dependency-triggered under D-024; retain favorable, mismatch, training-transfer, and mission-specific operational evidence separately; qualitative unless a source supplies numerical comparison data**

## Purpose

Track primary flight/postflight sources that compare Lunar Module Simulator / LM mission-simulation behavior or training transfer with the flown LM. This evidence class is separate from formal LMS acceptance/correlation documentation. Mission-specific crew operational material may also be cataloged here as a cross-check on player-visible symptoms, but it does not establish simulator implementation.

Do **not** convert qualitative phrases such as “nearly identical,” “high fidelity,” or “much more rapidly” into invented numerical tolerances.

## D-024 portfolio state

The general question "what additional flight-derived LMS validation evidence exists?" is **DEFERRED** unless a selected model, scenario, or validation claim names the dependency. The Apollo 13 malfunction-procedure source remains available as a mission-specific operational cross-check, but complete checklist inventory/page extraction is likewise deferred until a selected failure or player-visible symptom requires it. Exact historical LMS acceptance/correlation criteria remain a separate dependency and are not supplied by qualitative flight-transfer evidence.

See `docs/RESEARCH_PORTFOLIO_STATUS.md`.

## Apollo 13 LM Malfunction Procedures — mission-specific operational cross-check

- Document: **Apollo 13 LM Malfunction Procedures**
- Flight Data File retrieval key: `SKB32100076-386`
- Effectivity: Apollo 13; surviving-copy records expose March 16 / April 1, 1970 states, requiring page-level control/change verification.
- Public preservation record: Virtual AGC records a digitization from James Lovell's original copy, added 6 March 2023: https://www.ibiblio.org/apollo/changes.html

### Evidence use

Once its own control pages are verified, use the checklist to test candidate **player-visible** Apollo 13 LM malfunction symptoms, caution/warning indications, crew troubleshooting branches, and phase restrictions. This provides a mission-specific operational boundary much closer to Apollo 13 than the 1967 LMS handbook.

### Boundary

The crew checklist does **not** establish LMS instructor controls, scripting syntax, internal failure representation, processor behavior, or whether a listed malfunction was LMS-injectable. Conversely, absence from a crew checklist does not prove absence from LMS instructor capability. Keep this evidence class separate from 1967 Volume II Section 2 **Malfunction Data** and Section 6 **Scripting Data Sheets**.

Research record: `resources/research/325_apollo13_lm_malfunction_procedures_effectivity_anchor.md`.

## Apollo 9 Mission Report — AGS between-update degradation mismatch

- Document: *Apollo 9 Mission Report*
- Report: MSC-PA-R-69-2
- Date: May 1969
- Preserved public scan: https://www.ibiblio.org/apollo/Documents/A09_MissionReport.pdf
- Relevant location: Pilots' Report / LM rendezvous discussion, approximately p. 10-17.

### Direct validation evidence

After manual rendezvous-radar range/range-rate updates brought AGS information into good agreement with radar data, the crew reported that **abort-guidance range and range-rate information degraded much more rapidly in flight than it did in the simulator**.

The report also records flight-side AGS solution variation reaching approximately **±3 ft/s about the mean** during rendezvous. That value is an observed flight magnitude, not a simulator-vs-flight error band.

In the same operational discussion, LM pulse-mode control response was reported as behaving **very similarly** to the mission simulator.

### Evidence use

Supports a domain-specific negative validation boundary:

1. post-update agreement is not sufficient to validate between-update state propagation;
2. AGS relative-state/range/range-rate error growth needs separate validation;
3. the approximate ±3 ft/s flight-side variation is a candidate observable for later same-input comparison, not a tolerance;
4. one simulator domain may compare favorably while another differs materially in the same mission phase.

### Boundary

The passage does not establish the exact simulator site/configuration/revision, corresponding simulator-side variation under the same inputs, a numerical degradation rate over a common interval, the cause of the mismatch, direct Apollo 13 LMS H-2 applicability, or attribution to a specific LMS model component.

Research record: `resources/research/236_apollo9_simulator_flight_mismatch_boundary.md`.

## Apollo 14 Mission Report — powered descent and landing visuals

- Document: *Apollo 14 Mission Report*
- Report: MSC-04112
- Date: May 1971
- Primary NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap14fj/pdf/a14_mission-report.pdf
- Relevant sections: 9.8–9.9, lunar landing / powered descent.

The mission report states that the LMS steering equations and torque-to-inertia ratio were nearly identical to those of the actual vehicle; the pilot's preflight training was therefore adequate for the vehicle response encountered during descent; and the high fidelity of the simulator visual display, together with training time, was a determining factor in recognizing the target landing point. This is qualitative flight-derived validation, not a source of equations, constants, error bands, or Apollo 13 effectivity.

Research record: `resources/research/234_apollo14_lms_flight_validation_boundary.md`.

## Apollo 15 Mission Report — visual-rate/manual-landing transfer

- Document: *Apollo 15 Mission Report*
- Date: 1971
- Public mission-report copy: https://an.rsl.wustl.edu/apollo/data/A15/resources/A15_MissionReport.pdf
- Searchable presentation: https://apollojournals.org/alsj/a15/a15mr-9.htm

The report states that, based on preflight experience with visual simulator displays, descent rates appeared nominal and comfortable, and credits visual simulations plus LLTV flying with excellent manual-landing training. This does not establish numerical visual/display tolerances, LMS-only attribution, exact configuration, or Apollo 13 applicability.

## Apollo 17 Mission Report — landing technique transfer

- Document: *Apollo 17 Mission Report*
- NTRS ID: `19730015117`
- Date: 1973
- NTRS: https://ntrs.nasa.gov/citations/19730015117

The report attributes comfortable/safe manual-landing preparation partly to LMS and partly to LLTV training, including the practiced division of attention between outside references and cockpit velocity/attitude displays. It does not establish mathematical equivalence, numerical tolerances, LMS-only attribution, or Apollo 13 applicability.

## Apollo Program Summary Report — program-level synthesis

- Document: *Apollo Program Summary Report: Synopsis of the Apollo Program Activities and Technology for Lunar Exploration*
- Report: JSC-09423 / NASA-TM-X-68725
- Date: April 1975
- NTRS: https://ntrs.nasa.gov/citations/19750013242

The report states at program level that all lunar module crews found LMS and LLTV control-system responses representative of flight hardware, and credits high-fidelity visual landing/ascent presentation with excellent final-landing training. It also records training simulations demonstrating manual landing under degraded guidance/landing-radar conditions within Mission Control 3-sigma criteria, but does not provide those numerical values in the cited passage.

## Relationship to engineering acceptance evidence

Formal acceptance/correlation evidence remains cataloged separately in:

- `resources/source-catalog/LMS_ACCEPTANCE_PROCEDURES.md`
- `resources/source-catalog/LMS_VOLUME2_SECTION7_OUTPUT_TABLES.md`

Canonical distinction:

`engineering acceptance/correlation = quantitative when source-defined`

versus

`flight-derived/mission-operational validation = favorable comparison, mismatch, operational/training transfer, or period symptom/procedure constraint unless source-defined numerical comparison data are recovered`.
