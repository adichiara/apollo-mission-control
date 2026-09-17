# Research note 234 — Apollo 14 LMS flight-derived validation boundary

Date: 2026-09-17  
Status: **PRIMARY FLIGHT-DERIVED QUALITATIVE VALIDATION EVIDENCE; no numerical acceptance tolerance recovered**

## Question

Can a flown Apollo mission provide an independent validation boundary for what aspects of the Lunar Module Simulator were considered faithful to the actual vehicle, while the formal LMS acceptance/correlation criteria remain unrecovered?

## Primary evidence

The **Apollo 14 Mission Report** provides two direct comparisons between preflight simulator experience and flight behavior.

### Powered-descent dynamics/control behavior

In section 9.9, *Powered Descent*, the report states that the **steering equations and torque-to-inertia ratio of the lunar module simulator were nearly identical to those for the actual vehicle** and concludes that the pilot's preflight training was completely adequate for the actual vehicle response exhibited during descent.

Primary source:

- NASA, *Apollo 14 Mission Report*, MSC-04112, May 1971, section 9.9, p. 9-5 / scanned PDF page 73.
- Public NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap14fj/pdf/a14_mission-report.pdf

### Landing-site visual fidelity

Immediately before the powered-descent section, the crew-performance narrative states that the target landing point was recognized without reference to the computer landing-point designator and identifies the **high fidelity of the simulator visual display and the training time associated with the device** as the determining factor. The report further says the lunar module simulator and LLTV had more than adequately equipped the pilot for the landing task.

Same primary source, section 9.8 / pp. 9-5 to 9-6.

## What this establishes

For Apollo 14, postflight mission reporting treats at least these LMS fidelity categories as materially validated by flight experience:

1. **descent steering behavior**;
2. **torque-to-inertia response relationship**;
3. **visual-scene / landing-site recognition fidelity**.

This is stronger than a generic statement that the LMS was “high fidelity.” It identifies concrete simulator behavior families that NASA compared favorably with the flown LM.

The source also supports a useful validation architecture distinction:

`simulator mathematical behavior → trained pilot expectation/control response → actual flight behavior → postflight qualitative comparison`

and, separately:

`simulator visual scene → trained terrain/target recognition → actual lunar visual task → postflight qualitative comparison`.

## What this does **not** establish

The Apollo 14 Mission Report does **not** provide:

- the actual LMS steering equations;
- numerical torque-to-inertia values or tolerances;
- a simulator-vs-flight residual/error band;
- an LMS integration timestep;
- coordinate-frame definitions;
- inertia tensor, mass properties, thrust/gimbal constants, or control-law gains;
- the acceptance-test method used before Apollo 14;
- the configuration/revision of the LMS math-model documents that produced the cited behavior;
- proof that the Apollo 14 LMS configuration was identical to the Apollo 13 H-2 configuration;
- a basis for importing Apollo 14 constants into the PC+2 model.

The phrases “nearly identical” and “high fidelity” are therefore **qualitative validation conclusions**, not numerical D-022 intervals.

## Project consequence

Add a second validation evidence class alongside formal acceptance/correlation documentation:

### A. Engineering acceptance/correlation evidence

Desired chain:

`model/configuration → reference input → simulator output → reference output → numerical criterion/tolerance → pass/fail/result`

This remains the target of RG 255 E.155B1 and the surviving acceptance-procedure search.

### B. Flight-derived operational validation evidence

Available chain:

`simulator behavior → trained operator expectation → flown vehicle behavior → postflight comparison/conclusion`

This evidence can validate **which model domains matter and whether broad behavior was credible**, but it cannot define numerical tolerances unless the source supplies them.

For this project, the Apollo 14 evidence specifically reinforces the importance of keeping the following reusable domains explicit and independently testable:

- guidance/steering computation;
- mass/inertia and rotational dynamics coupling;
- pilot/controller-visible visual/observation generation.

It also supplies a cross-check target for future LMS source extraction: recovered steering equations and mass/inertia interfaces should be traceable to the same behavioral categories NASA later described as matching flight.

## Relationship to current LMS acceptance research

This note does **not** reduce the priority of retrieving:

- RG 255 E.155B1 acceptance test plans/procedures;
- `1L5-102-(H)` or related Link/Grumman acceptance documentation;
- LMS output tables and model/configuration effectivity;
- numerical correlation criteria.

Instead, it adds a distinct postflight validation layer that can be used after those engineering sources are recovered.

## Source

NASA, *Apollo 14 Mission Report*, MSC-04112, May 1971. Public scan:
https://www.nasa.gov/wp-content/uploads/static/history/afj/ap14fj/pdf/a14_mission-report.pdf
