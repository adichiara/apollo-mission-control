# LMS flight-derived validation sources

Status: **active source catalog; qualitative postflight validation evidence only unless a source supplies numerical comparison data**

## Purpose

Track primary flight/postflight sources that compare Lunar Module Simulator behavior or training transfer with the flown LM. This evidence class is separate from formal LMS acceptance/correlation documentation.

Use these sources to identify:

- simulator behavior families that NASA considered representative of flight;
- operational techniques that transferred from simulator training into flight;
- operator-facing observables worth preserving in reusable model boundaries;
- postflight cross-check targets for recovered LMS equations/configuration.

Do **not** convert qualitative phrases such as “nearly identical” or “high fidelity” into invented numerical tolerances.

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

## Relationship to engineering acceptance evidence

Formal acceptance/correlation evidence remains cataloged separately in:

- `resources/source-catalog/LMS_ACCEPTANCE_PROCEDURES.md`
- `resources/source-catalog/LMS_VOLUME2_SECTION7_OUTPUT_TABLES.md`

Canonical distinction:

`engineering acceptance/correlation = quantitative when source-defined`

versus

`flight-derived validation = operational/qualitative unless source supplies comparison numbers`.
