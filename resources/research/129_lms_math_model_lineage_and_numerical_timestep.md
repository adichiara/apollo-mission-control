# LMS mathematical-model lineage and numerical timestep evidence

Date: 2026-09-14  
Status: **source lineage established; full model extraction still pending**

## Research question

Can the surviving archive record identify concrete Lunar Module Mission Simulator mathematical-model documents—not just general simulator descriptions—and can those records tell us anything useful about the numerical architecture we should investigate?

Yes.

## Grumman LED 500-5 — direct LMS math-model report

The NASA/NARA corporate index preserved in the Virtual AGC archive identifies:

**LED 500-5**  
**Date:** 22 April 1965  
**MSC accession:** *66-10469  
**Contract:** NAS 9-1100  
**Title:** *LMS Math Model — Equations of Motion, Subsystem Interfaces and Visual Display Drive Equations*

This is a high-value direct match to the project's needs.

The title establishes that the LMS mathematical-model package explicitly covered at least three separable domains:

1. **equations of motion**;
2. **subsystem interfaces**;
3. **visual-display drive equations**.

That is important architecturally. It suggests the original simulator distinguished dynamic truth, subsystem coupling, and display-driving outputs rather than representing training behavior as one monolithic event script.

Source: Virtual AGC/NASA corporate index, Grumman Aircraft Engineering Corp. records.

## LED 500-16 — LGC math model for FMES and LMS

The same corporate index identifies:

**LED 500-16**  
**Date:** 8 June 1966  
**MSC accession:** *66-13246  
**Contract:** NAS 9-1100  
**Title:** *LEM Guidance Computer (LGC) Math Model for the Full Mission Engineering Simulator (FMES) and LEM Mission Simulator (LMS)*

This establishes another model boundary: the LGC was represented through a dedicated mathematical-model artifact used by both the Full Mission Engineering Simulator and the training LMS.

We should therefore avoid assuming that every simulated guidance consequence came from a generic spacecraft dynamics block. The historical simulator architecture appears to have had explicit subsystem/model partitions.

## Fifty-millisecond integration-step memo

TechWorks' archival catalog lists a 1965 Grumman document titled:

**Effect of LMS Fifty-Millisecond Integration Steps on Simulated Response of Abort Attitude Control System**

The full memo has not yet been extracted in this repository, so no detailed conclusion about its numerical method should be made.

However, the title alone establishes a very useful research lead:

- at least one LMS dynamic-response path was sensitive enough to numerical integration cadence that Grumman documented the effect of a **50 ms integration step** on simulated Abort Attitude Control System response.

This does **not** mean the entire LMS ran at 50 ms, nor that our simulator should adopt that step globally.

It does mean timestep/integration method was a documented fidelity issue in the original LMS and should be treated explicitly in our architecture rather than hidden inside arbitrary polling/event cadence.

## Why this changes the implementation plan

The first numerical proof should be structured as a model with an explicit integration contract.

At minimum, a numerical model interface should eventually state:

- authoritative state vector;
- derivative/update function;
- integration method;
- integration timestep or adaptive-step policy;
- command/configuration inputs;
- external-force/disturbance inputs;
- outputs consumed by other subsystem models;
- outputs consumed by instrumentation/display models;
- source provenance and fidelity class.

This lets us improve individual models later without changing the rest of the simulation architecture.

## Initial dynamics model boundary

For the first causal proof, the strongest chain remains:

```text
crew/CAPCOM burn instruction
        ↓
crew command execution
        ↓
engine commanded/actual state
        ↓
thrust magnitude + mass flow
        ↓
vehicle attitude / thrust direction
        ↓
translational equations of motion
        ↓
position / velocity / mass
        ↓
derived maneuver / trajectory result
        ↓
tracking / RTCC-like controller product
```

The scenario should supply initial state and any external failure injection. It should not supply the resulting velocity or trajectory outcome except as a validation oracle for known historical cases.

## Fidelity implications

The historical record now supports the idea of a **modular numerical simulator**, but not yet any particular equation implementation.

Before coding the dynamics core, we still need to extract:

- the actual LED 500-5 report if accessible;
- the Link LMS proposal mathematical flowcharts;
- the 50 ms integration-step memo;
- the LGC LMS/FMES model where available;
- coordinate-system standards and mass-property conventions;
- Apollo 13/LM-7 mission-specific propulsion and mass inputs.

A modern integrator may be more accurate/stable than the 1960s simulator implementation. Historical timestep choices are therefore evidence about model sensitivity and validation, not a requirement to reproduce numerical limitations.

## Source references

- Virtual AGC / NASA corporate index: Grumman LED 500 series, including LED 500-5 and LED 500-16.
- TechWorks archival catalog: 1965 LMS Math Model and *Effect of LMS Fifty-Millisecond Integration Steps on Simulated Response of Abort Attitude Control System*.
- Virtual AGC change log: Link Group *Proposal for LEM Mission Simulator, Volume II, Technical Addendum*, described as containing flowcharts of LMS mathematical equations.

See also:

- `resources/research/127_causal_simulation_engine_and_crew_model.md`
- `resources/research/128_lm_mission_simulator_mathematical_model_sources.md`
- `resources/source-catalog/APOLLO_SIMULATION_ENGINE_SOURCES.md`
