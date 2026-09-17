# Research note 237 — AGS verification / validation architecture and simulated-flight criteria

Date: 2026-09-17  
Status: **PRIMARY APOLLO-ERA GUIDANCE-SOFTWARE VERIFICATION ARCHITECTURE RECOVERED; criteria families identified, exact radar-filter bounds/curves not yet extracted**

## Question

What verification architecture did Apollo use for the LM Abort Guidance System, and what parts of that architecture are useful for this project's reusable numerical-model validation without conflating AGS software verification with Lunar Module Simulator acceptance testing?

## Primary source identity

Pat M. Kurten, *Apollo Experience Report — Guidance and Control Systems: Lunar Module Abort Guidance System*.

- NASA Technical Note: **NASA TN D-7990**
- JSC report: **JSC S-424**
- NTRS document ID: **19750018954**
- Publication: July 1975
- NTRS record: https://ntrs.nasa.gov/citations/19750018954
- Public PDF mirror used for page inspection: https://apollojournals.org/alsj/19750018954_tnD7990LM_AGS.pdf

NTRS identifies the report as a NASA Technical Note by Pat M. Kurten and states that it covers AGS development from requirements through qualification/testing, software generation, mission operations, and flight performance.

## Verification hierarchy recovered

The report explicitly describes a layered software/program verification process.

### 1. Equation testing / engineering simulation

Scientific or engineering simulations of the AGS equations were run in **closed-loop configuration** to demonstrate equation performance under:

- nominal conditions; and
- vehicle, sensor, or trajectory dispersions of **3 standard deviations (3σ)**.

This is a mathematical/model-level verification layer.

### 2. Coded-program implementation verification

The coded AEA program was tested with a **bit-by-bit interpretive computer simulation (ICS)**.

Purpose: verify that the implemented program agreed with the governing equations.

This distinguishes:

`equation/model correctness`

from

`software implementation fidelity to equations`.

### 3. Closed-loop AEA + vehicle flight simulation

A closed-loop interpretive simulation of:

- the AEA program; and
- vehicle flight characteristics

was used as an **ICS flight simulator (FS)** for verification testing.

The report says this was used to verify that the program could guide/control the vehicle in all operating modes. Special ICS driver routines augmented the testing.

### 4. Statistical performance analysis

A **600-cycle Monte Carlo analysis** was performed to determine detailed AGS performance relative to mission requirements.

The report does not authorize treating 600 cycles as a universal Apollo simulation standard. It is the documented AGS program's analysis sample size in this verification context.

### 5. Independent / hardware-in-loop verification

MSC also performed verification using a **hybrid computer facility with actual ASA and DEDA hardware** for independent test cases.

Additional mission-specific testing by the prime contractor used a **six-degree-of-freedom computer simulation** incorporating:

- AGS; and
- other hardware components in the LM flight-control system.

This adds two distinct verification layers:

`independent facility + real subsystem hardware`

and

`mission-specific integrated vehicle/control simulation`.

## Simulated-flight operational checkout

The report says AGS simulated-flight procedures were delivered and used with a specified flight program to simulate mission phases. Their purpose was to gain confidence in AGS operation with interfacing LM subsystems.

The procedures included tests of:

- AGS simulated-flight initialization;
- CSM acquisition;
- **radar filter**;
- abort from powered descent;
- abort from the lunar surface;
- coelliptic sequence initiation (CSI);
- constant-differential-height (CDH) guidance;
- terminal phase initiation (TPI); and
- external delta-V guidance solutions.

Most importantly, the report states that **test criteria were obtained from interpretive computer simulations and resulted in value bounds or bounded curves for various AEA and display parameters**.

This is direct primary evidence that Apollo operational simulated-flight checkout used source-derived **parameter bounds / bounded curves**, rather than relying only on generic qualitative GO/NO-GO judgment.

## Development/configuration control

The report also documents a mission-program development/release sequence in which:

- mission requirements/reference trajectory were supplied months before launch;
- verification-test plans and performance-analysis plans were delivered;
- the program package included verification-test results and performance-analysis results;
- final program constants were updated from mission data and the actual flight ASA history;
- customer acceptance/readiness reviews and flight-readiness reviews occurred before final loading.

This matters because validation criteria were attached to a **program/version/mission data package**, not treated as timeless universal constants.

## A concrete test-discrepancy example

The report later describes a simulated lunar-ascent checkout discrepancy: an out-of-plane inertial velocity of about **5 ft/s (1.5 m/s)** appeared while body-axis velocity did not show the component.

The issue was traced to roundoff during transformation of compensated sensed velocity from body to inertial coordinates in a **20-millisecond computing cycle**. The report says the static roundoff buildup was accounted for in test-result evaluation and that its flight effects in a dynamic environment were negligible.

This is useful architecture evidence because it demonstrates:

`test discrepancy → causal localization → numerical mechanism → operational significance assessment → evaluation adjustment`

### Critical 20-ms boundary

The 20-ms value belongs to the **AEA computing / AGS simulated-flight calculation context described in this discrepancy**.

It is **not** evidence for:

- a universal LMS integration step;
- a global Apollo simulator cadence;
- a PC+2 numerical timestep;
- every AGS subfunction's independent update rate.

Do not merge it with the separately identified LMS 50-ms AACS integration-step study.

## Relationship to Apollo 9 mismatch evidence

Research note 236 records that Apollo 9 crew reporting found AGS range/range-rate information degraded much faster in flight than in the simulator after radar updates, while pulse-mode LM control behavior compared favorably.

TN D-7990 is highly relevant because it confirms that **radar-filter simulated-flight tests existed** and that test acceptance criteria were represented by bounds/bounded curves.

However, the reviewed TN D-7990 text does **not yet** establish that:

- the Apollo 9 simulator comparison used the same ICS/FS reference case;
- the applicable radar-filter bound/curve has been recovered;
- the Apollo 9 flight-side ~±3 ft/s AGS variation corresponds directly to a TN D-7990 criterion;
- the simulator mismatch was caused by AGS equations/software rather than sensor/error-model/interface assumptions.

The crosswalk remains an open research task.

## Reusable validation architecture consequence

This primary source strongly supports a layered project validation model:

1. **equation/model tests** — verify the mathematical implementation under nominal and dispersed inputs;
2. **code-to-equation equivalence tests** — verify implementation against the equation/reference model;
3. **closed-loop subsystem/vehicle tests** — verify causal interaction in all supported modes;
4. **Monte Carlo / ensemble tests** — characterize performance under uncertainty against requirements;
5. **hardware/independent-reference tests** — compare against independent implementations or real hardware where available;
6. **mission-specific operational scenario tests** — validate procedures and displayed/observable parameters using source-defined bounds/curves;
7. **flight-derived postflight validation** — compare simulator/model behavior against actual mission behavior, retaining both favorable and negative comparisons.

The project already implements parts of 1–3 and 6 through synthetic model proofs and authoritative-session consequence tests. The historical source says these layers should remain distinguishable rather than collapsed into one 'validated' flag.

## Evidence-class consequence

Validation artifacts should record at least:

- model/program identity and version/effectivity;
- input/reference case;
- dispersion/error assumptions;
- observable/output;
- source/reference implementation;
- criterion representation (scalar bound, interval, bounded curve, trajectory, categorical result);
- comparison result;
- causal explanation for discrepancies where known;
- whether evidence is engineering verification, operational checkout, or flight-derived validation.

## What this source does **not** authorize

Do not infer from TN D-7990:

- LMS acceptance criteria in general;
- Apollo 13 H-2 simulator configuration;
- RTCC/Mission Control validation methods;
- an LMS-global 20-ms timestep;
- that the AGS radar-filter criterion is numerically known merely because the report says bounded curves existed;
- that a 3σ verification dispersion is itself an allowable output-error tolerance;
- that 600 Monte Carlo cycles is required for this project.

## Project consequence

No executable model constant changes from this note.

The project should add a reusable validation-case schema only when it can preserve these source distinctions cleanly. Historical criteria remain profile/test-case data, not generic engine constants.

## Next research actions

1. Locate the underlying AGS radar-filter simulated-flight procedure and its value-bound/bounded-curve criteria.
2. Crosswalk Apollo 9 Supplement 3 postflight AGS results against the applicable preflight error model / simulated-flight criteria.
3. Identify which AGS software/configuration revision and simulator/test facility corresponded to Apollo 9.
4. Recover equivalent LMS acceptance/correlation cases from RG 255 E.155B1 to determine how closely LMS validation mirrored the AGS methodology.
5. Preserve the 20-ms AEA computation evidence as AGS-specific unless a direct LMS program source independently establishes the same cadence.
