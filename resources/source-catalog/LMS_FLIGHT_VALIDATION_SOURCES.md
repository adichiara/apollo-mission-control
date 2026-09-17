# LMS flight-derived validation sources

Status: **active source catalog; retain favorable, mismatch, and training-transfer evidence separately; qualitative unless a source supplies numerical comparison data**

## Purpose

Track primary flight/postflight sources that compare Lunar Module Simulator / LM mission-simulation behavior or training transfer with the flown LM. This evidence class is separate from formal LMS acceptance/correlation documentation.

Use these sources to identify:

- simulator behavior families that NASA considered representative of flight;
- domains where flight behavior departed from simulator expectation;
- operational techniques that transferred from simulator training into flight;
- operator-facing observables worth preserving in reusable model boundaries;
- postflight cross-check targets for recovered LMS equations/configuration.

Do **not** convert qualitative phrases such as “nearly identical,” “high fidelity,” or “much more rapidly” into invented numerical tolerances.

## Apollo 9 Mission Report — AGS between-update degradation mismatch

- Document: *Apollo 9 Mission Report*
- Report: MSC-PA-R-69-2
- Date: May 1969
- Preserved public scan: https://www.ibiblio.org/apollo/Documents/A09_MissionReport.pdf
- Relevant location: Pilots' Report / LM rendezvous discussion, approximately p. 10-17.

### Direct validation evidence

After manual rendezvous-radar range/range-rate updates brought AGS information into good agreement with radar data, the crew reported that **abort-guidance range and range-rate information degraded much more rapidly in flight than it did in the simulator**.

In the same operational discussion, LM pulse-mode control response was reported as behaving **very similarly** to the mission simulator.

### Evidence use

Supports a domain-specific negative validation boundary:

1. post-update agreement is not sufficient to validate between-update state propagation;
2. AGS relative-state/range/range-rate error growth needs separate validation;
3. one simulator domain may compare favorably while another differs materially in the same mission phase.

### Boundary

The passage does not establish:

- the exact simulator site/configuration/revision;
- a numerical flight or simulator degradation rate;
- the cause of the mismatch;
- direct applicability to Apollo 13 LMS H-2;
- that the mismatch belongs to a specific LMS mathematical-model component rather than sensor/state initialization/filtering/interface behavior.

Research record: `resources/research/236_apollo9_simulator_flight_mismatch_boundary.md`.

## Apollo 14 Mission Report — powered descent and landing visuals

- Document: *Apollo 14 Mission Report*
- Report: MSC-04112
- Date: May 1971
- Primary NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap14fj/pdf/a14_mission-report.pdf
- Relevant sections: 9.8–9.9, lunar landing / powered descent.

### Direct validation evidence

The mission report states that:

- the LMS **steering equations** and **torque-to-inertia ratio** were nearly identical to those of the actual vehicle;
- the pilot's preflight training was therefore adequate for the vehicle response actually encountered during descent;
- the **high fidelity of the simulator visual display**, together with training time, was a determining factor in recognizing the target landing point;
- the LMS and LLTV more than adequately equipped the pilot for the manual landing task.

### Evidence use

Supports flight-derived qualitative validation of:

1. guidance/steering behavior;
2. rotational response coupling between torque and inertia;
3. visual/terrain-recognition fidelity.

### Boundary

Does not provide:

- equations or constants;
- error bands, correlation residuals, or pass/fail tolerances;
- configuration revision/effectivity mapping back to Apollo 13 H-2;
- a global LMS integration timestep;
- permission to import Apollo 14 values into Apollo 13 PC+2.

Research record: `resources/research/234_apollo14_lms_flight_validation_boundary.md`.

## Apollo 15 Mission Report — visual-rate/manual-landing transfer

- Document: *Apollo 15 Mission Report*
- Date: 1971
- Public mission-report copy: https://an.rsl.wustl.edu/apollo/data/A15/resources/A15_MissionReport.pdf
- Searchable mission-report presentation: https://apollojournals.org/alsj/a15/a15mr-9.htm
- Relevant location: pilot's report / powered descent and landing.

### Direct validation evidence

The report states that, based on **preflight experience with visual simulator displays**, descent rates appeared completely nominal and comfortable. It also states that the combination of **visual simulations** and LLTV flying provided excellent training for the manual portion of the lunar landing.

### Evidence use

Supports flight-derived qualitative validation of:

1. visual-simulation transfer into descent-rate expectation;
2. visual simulation as part of manual-landing preparation.

### Boundary

This does not establish:

- numerical visual/display correlation tolerances;
- LMS-only attribution, because the report also credits LLTV training;
- exact visual-system configuration/effectivity;
- Apollo 13 H-2 applicability.

Research synthesis: `resources/research/234_apollo14_lms_flight_validation_boundary.md`.

## Apollo 17 Mission Report — landing technique transfer

- Document: *Apollo 17 Mission Report*
- NTRS ID: `19730015117`
- Date: 1973
- NTRS record: https://ntrs.nasa.gov/citations/19730015117
- Relevant location: lunar landing narrative, p. 10-12.

### Direct validation evidence

The mission report attributes the comfortable/safe manual landing approach partly to LMS training and partly to LLTV training. It also records that the Commander's technique of dividing attention between outside visual references and in-cockpit velocity/attitude displays was a technique practiced in the LMS and LLTV.

### Evidence use

Supports flight-derived qualitative validation of:

1. operational transfer of instrument/out-the-window attention technique;
2. LMS contribution to manual landing preparation.

### Boundary

This does not establish:

- mathematical equivalence of Apollo 17 LMS and vehicle dynamics;
- numerical display/visual tolerances;
- LMS-only attribution, because the report explicitly also credits LLTV training;
- Apollo 13 H-2 configuration applicability.

Research synthesis: `resources/research/234_apollo14_lms_flight_validation_boundary.md`.

## Apollo Program Summary Report — program-level synthesis

- Document: *Apollo Program Summary Report: Synopsis of the Apollo Program Activities and Technology for Lunar Exploration*
- Report: JSC-09423 / NASA-TM-X-68725
- Date: April 1975
- NTRS: https://ntrs.nasa.gov/citations/19750013242
- Relevant location: flight-crew training summary, section 6.1.2, approximately p. 6-8.

### Direct validation evidence

The report states at program level that **all lunar module crews** found the LMS and LLTV control-system responses representative of flight hardware, and that the high-fidelity visual landing/ascent presentation together with those trainers provided excellent training for the manually controlled final landing phase.

It also records that training simulations demonstrated manual landing capability under degraded guidance/landing-radar conditions, including cases without landing radar, within Mission Control 3-sigma altitude/targeting dispersion criteria.

### Boundary

The cited summary passage does not provide the numerical 3-sigma values, simulator configuration/effectivity, or a numerical LMS-vs-flight residual. It therefore remains qualitative for this project unless the underlying criteria are separately recovered.

## Relationship to engineering acceptance evidence

Formal acceptance/correlation evidence remains cataloged separately in:

- `resources/source-catalog/LMS_ACCEPTANCE_PROCEDURES.md`
- `resources/source-catalog/LMS_VOLUME2_SECTION7_OUTPUT_TABLES.md`

Canonical distinction:

`engineering acceptance/correlation = quantitative when source-defined`

versus

`flight-derived validation = favorable comparison, mismatch, or operational/training transfer unless source-defined numerical comparison data are recovered`.
