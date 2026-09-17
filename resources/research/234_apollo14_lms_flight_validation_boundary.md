# Research note 234 — Apollo 14 LMS flight-derived validation boundary

Date: 2026-09-17  
Status: **PRIMARY FLIGHT-DERIVED QUALITATIVE VALIDATION EVIDENCE; Apollo 15/17 add operational/visual-transfer corroboration; no numerical acceptance tolerance recovered**

## Question

Can flown Apollo missions provide an independent validation boundary for what aspects of the Lunar Module Simulator were considered faithful/useful relative to the actual vehicle, while the formal LMS acceptance/correlation criteria remain unrecovered?

## Primary evidence — Apollo 14

The **Apollo 14 Mission Report** provides two direct comparisons between preflight simulator experience and flight behavior.

### Powered-descent dynamics/control behavior

In section 9.9, *Powered Descent*, the report states that the **steering equations and torque-to-inertia ratio of the lunar module simulator were nearly identical to those for the actual vehicle** and concludes that the pilot's preflight training was completely adequate for the actual vehicle response exhibited during descent.

Primary source:

- NASA, *Apollo 14 Mission Report*, MSC-04112, May 1971, section 9.9, p. 9-5 / scanned PDF page 73.
- Public NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap14fj/pdf/a14_mission-report.pdf

### Landing-site visual fidelity

Immediately before the powered-descent section, the crew-performance narrative states that the target landing point was recognized without reference to the computer landing-point designator and identifies the **high fidelity of the simulator visual display and the training time associated with the device** as the determining factor. The report further says the lunar module simulator and LLTV had more than adequately equipped the pilot for the landing task.

Same primary source, section 9.8 / pp. 9-5 to 9-6.

## Corroborating primary evidence — Apollo 15

The **Apollo 15 Mission Report** adds another direct postflight training-transfer statement during the terminal landing narrative.

The report says that, based on **preflight experience with visual simulator displays**, descent rates appeared completely nominal and comfortable. It then states that the combination of **visual simulations** and LLTV flying provided excellent training for the manual portion of the lunar landing and that comfort and confidence existed throughout this phase.

Primary source:

- NASA, *Apollo 15 Mission Report*, pilot's report / powered descent and landing section.
- Public mission-report copy: https://an.rsl.wustl.edu/apollo/data/A15/resources/A15_MissionReport.pdf
- Searchable transcript presentation: https://apollojournals.org/alsj/a15/a15mr-9.htm

This supports **visual-rate / manual-landing expectation transfer** rather than a numerical display-correlation claim.

## Corroborating primary evidence — Apollo 17

The **Apollo 17 Mission Report** provides a different but compatible kind of postflight LMS validation.

In the landing narrative, the report attributes the comfortable/safe manual landing approach partly to **lunar module simulator** training and partly to LLTV training. It also states that the Commander's technique of dividing attention between outside visual references and in-cockpit velocity/attitude displays was a technique practiced in the **lunar module simulator** and LLTV.

Primary source:

- NASA, *Apollo 17 Mission Report*, 1973, section covering lunar landing / manual landing phase, p. 10-12.
- NTRS record/PDF: https://ntrs.nasa.gov/citations/19730015117

This source does not supply a mathematical comparison like Apollo 14's steering/torque-to-inertia statement. Instead it supports **operational technique transfer** from LMS training to flight.

## What this establishes

For Apollo 14, postflight mission reporting treats at least these LMS fidelity categories as materially validated by flight experience:

1. **descent steering behavior**;
2. **torque-to-inertia response relationship**;
3. **visual-scene / landing-site recognition fidelity**.

Apollo 15 adds:

4. **transfer of visual descent-rate expectations from simulator displays into the actual landing**;
5. **usefulness of visual simulation as part of manual-landing preparation**.

Apollo 17 independently adds:

6. **transfer of trained instrument/out-the-window attention technique into actual lunar landing operations**;
7. **usefulness of LMS training as part of preparation for manual landing control**.

This is stronger than a generic statement that the LMS was “high fidelity.” It identifies concrete simulator behavior and training-transfer families that NASA postflight reporting linked to flown performance.

The sources support two useful validation architecture distinctions:

`simulator mathematical behavior → trained pilot expectation/control response → actual flight behavior → postflight qualitative comparison`

and

`simulator display/operational technique → trained observation/control strategy → actual lunar task → postflight transfer assessment`.

## What this does **not** establish

These mission reports do **not** provide:

- the actual LMS steering equations;
- numerical torque-to-inertia values or tolerances;
- a simulator-vs-flight residual/error band;
- an LMS integration timestep;
- coordinate-frame definitions;
- inertia tensor, mass properties, thrust/gimbal constants, or control-law gains;
- numerical visual-scene, display-rate, or terrain-recognition tolerances;
- the acceptance-test method used before these missions;
- the configuration/revision of the LMS math-model documents that produced the cited behavior;
- proof that Apollo 14/15/17 LMS configurations were identical to the Apollo 13 H-2 configuration;
- a basis for importing later-mission constants into the PC+2 model.

The phrases “nearly identical,” “high fidelity,” and operational-training attribution are therefore **qualitative validation conclusions**, not numerical D-022 intervals.

## Project consequence

Add a second validation evidence class alongside formal acceptance/correlation documentation:

### A. Engineering acceptance/correlation evidence

Desired chain:

`model/configuration → reference input → simulator output → reference output → numerical criterion/tolerance → pass/fail/result`

This remains the target of RG 255 E.155B1 and the surviving acceptance-procedure search.

### B. Flight-derived operational validation evidence

Available chain:

`simulator behavior/training technique → trained operator expectation/strategy → flown vehicle/task behavior → postflight comparison/conclusion`

This evidence can validate **which model domains and operator-facing effects mattered, and whether broad behavior/technique transfer was credible**, but it cannot define numerical tolerances unless the source supplies them.

For this project, the evidence reinforces the importance of keeping the following reusable domains explicit and independently testable:

- guidance/steering computation;
- mass/inertia and rotational dynamics coupling;
- pilot/controller-visible visual/observation generation;
- operator-facing display/attention information sufficient to support the trained control technique.

It also supplies a cross-check target for future LMS source extraction: recovered steering equations, mass/inertia interfaces, and visual/display-generation paths should be traceable to the same behavioral categories NASA later described as matching or transferring to flight.

## Relationship to current LMS acceptance research

This note does **not** reduce the priority of retrieving:

- RG 255 E.155B1 acceptance test plans/procedures;
- `1L5-102-(H)` or related Link/Grumman acceptance documentation;
- LMS output tables and model/configuration effectivity;
- numerical correlation criteria.

Instead, it adds a distinct postflight validation layer that can be used after those engineering sources are recovered.

## Sources

- NASA, *Apollo 14 Mission Report*, MSC-04112, May 1971: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap14fj/pdf/a14_mission-report.pdf
- NASA, *Apollo 15 Mission Report*: https://an.rsl.wustl.edu/apollo/data/A15/resources/A15_MissionReport.pdf
- NASA, *Apollo 17 Mission Report*, NTRS `19730015117`: https://ntrs.nasa.gov/citations/19730015117
