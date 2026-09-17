# Research note 236 — Apollo 9 simulator-to-flight mismatch boundary

Date: 2026-09-17  
Status: **PRIMARY FLIGHT-DERIVED NEGATIVE VALIDATION EVIDENCE; flight-side AGS variation magnitude identified; simulator-side same-input magnitude and exact configuration remain unresolved**

## Question

Can Apollo flight evidence identify a domain in which simulator behavior was observably less representative of flight, so the project's validation framework does not rely only on favorable simulator comparisons?

## Primary evidence

The **Apollo 9 Mission Report** provides a direct negative simulator-to-flight comparison during LM rendezvous operations.

After rendezvous-radar range/range-rate data were manually inserted into the Abort Guidance System (AGS), the crew observed that the AGS solution initially moved into good agreement with radar data. The pilots' report then states that the **abort-guidance range and range-rate information degraded much more rapidly in flight than it did in the simulator**.

The same passage immediately provides a useful contrast: the LM pulse control mode was described as responding in a manner **very similar to that in the mission simulator**.

The report also records that AGS solution variation during rendezvous was greater than expected, with variations reaching approximately **±3 ft/s about the mean**. This is a flight-side observable magnitude; it is not a simulator-vs-flight residual and does not provide the simulator-side variation under the same conditions.

Primary source:

- NASA Manned Spacecraft Center, *Apollo 9 Mission Report*, MSC-PA-R-69-2, May 1969, Pilots' Report / rendezvous discussion, approximately p. 10-17.
- Public preserved scan: https://www.ibiblio.org/apollo/Documents/A09_MissionReport.pdf

The report is independently identified as Apollo 9's mission report by the later NASA Apollo Program Summary Report reference list.

## What this establishes

Apollo 9 flight experience supports a domain-specific validation result rather than a blanket judgment about simulator fidelity:

### Broadly representative behavior

- pulse-mode LM control response was described as very similar to the mission simulator.

### Observed simulator/flight mismatch

- AGS range/range-rate solution degradation between radar updates was perceived to occur materially faster in flight than in the simulator;
- flight-side AGS solution variation during rendezvous reached roughly ±3 ft/s about the mean.

This is important because the favorable and unfavorable observations occur in the same rendezvous operational context. It shows why simulator validation must be attached to a **specific behavior/domain**, not generalized from one successful comparison to the whole simulator.

## Likely causal domain implicated

The flight observation points most directly toward the modeled chain:

`radar range/range-rate observation`
→ `manual AGS update`
→ `AGS relative-state estimate`
→ `coast / propagation between updates`
→ `displayed range/range-rate divergence`

The mission report does **not** identify the cause of the simulator/flight difference in that passage.

Do not infer without further source evidence that the discrepancy was caused by:

- AGS software equations;
- inertial-sensor bias/drift;
- radar measurement error;
- state initialization;
- simulator sensor/noise modeling;
- coordinate transformations;
- update timing;
- a particular LMS mathematical-model defect.

Those are candidate mechanisms only.

## Simulator identity boundary

The Apollo 9 crew's preflight section states that multiple command-module and lunar-module simulators were assigned to the crew and that integrated simulations used the Mission Control Center, lunar-module simulator, and command-module simulator.

The rendezvous passage itself uses the shorter phrase **“the simulator” / “mission simulator.”** The operational context is LM rendezvous, but the report does not identify in this sentence:

- Houston versus KSC;
- exact simulator serial/configuration;
- exact software/model revision;
- whether the cited AGS behavior came from a standalone LMS run or a particular integrated-simulation configuration.

The project may therefore classify this as **Apollo LM mission-simulation flight-comparison evidence**, but should not attach it to an Apollo 13 H-2 configuration or a specific LMS software revision without additional records.

## Numerical boundary

The source provides one useful flight-side magnitude: AGS solution variation reached approximately **±3 ft/s about the mean** during rendezvous.

It still does **not** supply a same-input comparison pair. In particular, the reviewed mission-report passage does not provide:

- the simulator-side variation corresponding to the ±3 ft/s flight observation;
- a simulator degradation/error-growth rate;
- a flight degradation/error-growth rate over a defined common interval;
- a common initial state and radar-update input;
- a simulator-vs-flight residual time history;
- a ratio between simulator and flight behavior;
- a numerical acceptance tolerance or pass/fail criterion.

Therefore this is **not** a D-022 numerical interval. The ±3 ft/s value is a **flight-side validation observable** and a retrieval target for corresponding simulator/reference cases, not a tolerance.

A future numerical reconstruction would need a common input/initial state and flight/simulator outputs at the same observable level before a defensible sensitivity range could be formed.

## Validation-framework consequence

Flight-derived validation needs at least three result classes:

1. **representative / favorable comparison** — behavior reported as similar to flight;
2. **mismatch / negative comparison** — flight behavior departed materially from simulator expectation;
3. **training transfer without model-equivalence claim** — simulator practice transferred usefully to flight even when no direct mathematical comparison was stated.

The project should retain both positive and negative evidence at the domain level.

A recovered LMS/AGS model should not be judged historically credible merely because another LMS domain matched flight well. For guidance/navigation state propagation in particular, future validation should compare **observable error growth between updates**, not just agreement immediately after an update.

## Relationship to later AGS documentation

NASA TN D-7990, Pat M. Kurten's *Apollo Experience Report — Guidance and Control Systems: Lunar Module Abort Guidance System* (NTRS `19750018954`), documents the AGS verification process in detail. It establishes equation-level closed-loop simulation under nominal and 3σ dispersions, bit-by-bit interpretive computer simulation, a closed-loop AEA/vehicle interpretive flight simulator, 600-cycle Monte Carlo performance analysis, and mission-phase simulated-flight procedures whose criteria were derived as value bounds or bounded curves for AEA/display parameters.

That source provides an Apollo-era verification methodology and likely reference-test lineage. It must remain separate from the Apollo 9 flight observation until a specific Apollo 9 radar-filter / between-update case is cross-walked to the applicable verification configuration.

## Project consequence

No executable constant changes from this note.

The reusable guidance/navigation validation architecture should support tests shaped like:

`same initialization + same radar update`
→ `propagate without new update for Δt`
→ `compare range/range-rate error growth`
→ `compare against source-backed flight/reference behavior`

without assuming that post-update agreement proves correct between-update dynamics.

The approximate ±3 ft/s flight-side variation should be retained as a candidate comparison observable, not used as a tolerance or injected simulator constant.

## Next research actions

1. Review Apollo 9 Mission Report Supplement 3, *LM Abort Guidance System Postflight Analysis Report*, for quantitative explanation of rendezvous-state error growth.
2. Extract the applicable radar-filter / simulated-flight test criteria from NASA TN D-7990 and identify whether its value bounds or bounded curves survive elsewhere.
3. Search LMS/AGS integration and acceptance records for the radar-update / between-update propagation test case.
4. Do not assign the Apollo 9 discrepancy to Apollo 13 LMS H-2 until configuration continuity is demonstrated.
