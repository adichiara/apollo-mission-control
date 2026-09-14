# LMS true-motion equation boundary and first implementation contract

Date: 2026-09-14  
Status: **source-triangulated architecture boundary; primary report extraction still pending**

## Question

Does the recovered simulator evidence constrain a narrow propulsion/dynamics implementation contract strongly enough to begin design without treating one modern reconstruction as the original LMS source?

## Newly identified source lineage

The Virtual AGC document index identifies the surviving Link Group proposal as:

- *Proposal for LEM Mission Simulator, Volume II, Technical Addendum: Glossary of Symbols*;
- General Precision, Inc., Link Group — Systems Division;
- dated 13 April 1964;
- a direct LMS proposal source whose scan contains mathematical-equation flowcharts.

A separate surviving equation lineage is now identifiable and must not be conflated with that proposal or with Grumman LED 500-5:

- Grumman Aircraft Engineering Corporation, *LEM Mission Simulator (LMS) Math Model: True Motion Equations*;
- report **LED-440-3**, August 1965;
- described as part 1 of 3 in the reference list of Brian Woycechowsky's 2021 *Lunar Module Moon-Referenced Equations of Motion*.

Woycechowsky's report is a modern reconstruction/explanation, not the original 1965 report. It is useful as an extraction aid and provenance lead because it reproduces a model flow and identifies the original report number, date, title, and formerly public TechWorks file. It does not replace review of the primary LED-440-3 scan.

The repository's previously identified **LED 500-5** title—*LMS Math Model — Equations of Motion, Subsystem Interfaces and Visual Display Drive Equations*, 22 April 1965—comes from the NASA/NARA corporate index. The relationship between LED 500-5 and LED-440-3 is unresolved. They may be distinct reports, revisions, reorganized document series, or related model packages. No equivalence is asserted.

## Extractable model boundary

The 2021 reconstruction exposes a source-attributed LMS true-motion interface with the following partitions:

- **Propulsion model** supplies ascent- and descent-engine thrust magnitude.
- **Stabilization and Control model** supplies main-engine thrust-direction/misalignment angles.
- **RCS model** supplies individual jet thrusts.
- **Weight and Balance model** supplies vehicle mass, moments/products of inertia, and force application points relative to the center of gravity.
- **Fuel/oxidizer slosh model** supplies force and moment contributions.
- **Stage-separation model** supplies separation force and moment.
- **Ephemeris/gravity model** supplies frame transformation and lunar gravitational inputs.
- **True-motion equations** combine those inputs to integrate translational state, rotational rates, and attitude representation.
- Quaternion normalization/rectification is explicit in the reproduced rotational flow.

This is the first concrete recovered boundary showing that the LMS did not treat “burn outcome” as one monolithic lookup. Propulsion, control/thrust direction, mass properties, disturbances, and true-motion integration were separate coupled model responsibilities.

## Implication for the first project slice

The evidence is sufficient to choose the **shape** of the first narrow project contract:

```text
propulsion state/configuration
    -> thrust magnitude and propellant mass flow

prescribed or modeled attitude/control state
    -> body-frame thrust direction

weight/mass state
    -> current mass and center-of-gravity inputs

dynamics
    -> integrate vector acceleration and mass
    -> velocity / position / accumulated impulse

observation/ground-product layer
    -> controller-visible maneuver and trajectory products
```

This contract should preserve replaceable boundaries even when Level 1 uses simplifications:

- prescribed attitude rather than a full rotational model;
- propulsion-only/free-space regression before mission trajectory propagation;
- omitted slosh, RCS, stage-separation, and detailed center-of-gravity torque effects unless a supported PC+2 decision depends on them;
- a modern deterministic integrator with convergence tests rather than presumed reproduction of an undocumented historical step schedule.

The historical model boundary supports these interfaces. It does **not** supply Apollo 13/LM-7 values automatically.

## What is not yet justified

The current evidence does not yet justify:

- adopting constants from the 1964 proposal or 1965 true-motion report as Apollo 13 values;
- treating a moon-referenced LMS model as the complete PC+2 translunar/free-return propagator;
- claiming LED 500-5 and LED-440-3 are the same document;
- choosing a global 50 ms timestep;
- freezing DPS thrust buildup, throttle mapping, specific impulse, mass epoch, gimbal state, or cutoff transient;
- implementing slosh, full rotational dynamics, or high-fidelity lunar gravity merely because the original LMS modeled them;
- using Woycechowsky's reconstruction as a substitute citation for an unreviewed primary page.

## Implementation gate status

The gate in `docs/CAUSAL_SIMULATION_ENGINE.md` is now **partially cleared**:

- the modular input/output boundary for a first translational proof is defensible;
- the Level 1 state can be time, mass, vector velocity, optional position, accumulated impulse, and explicit frame metadata;
- the first implementation can keep propulsion, attitude/thrust direction, mass properties, dynamics, and observation products separable.

The gate is **not cleared for historical PC+2 numerical acceptance tolerances**. The exact mission-specific thrust history, mass epoch, coordinate-frame mapping, and end-to-end trajectory oracle remain unresolved.

A safe next code step is therefore an assumption-visible propulsion/translational kernel with convergence and ordering tests. It must be labeled a model proof until source extraction freezes the Apollo 13 profile.

## Next retrieval targets

1. Recover/open the original LED-440-3 parts and capture page-level model interfaces.
2. Open the Link proposal scan and extract its propulsion, weight/balance, stabilization/control, and true-motion flowchart families.
3. Determine the documentary relationship among the Link proposal, LED-440-3, and LED 500-5.
4. Recover the LMS 50 ms AACS memo to bound what the timestep claim actually applies to.
5. Trace Apollo 13 PC+2 mass and thrust-profile values to exact mission-specific pages/epochs.
6. Define the working coordinate frame separately from the model architecture before trajectory propagation is accepted.

## Sources

- Virtual AGC document library/index: https://www.ibiblio.org/apollo/links2.html
- Link Group, *Proposal for LEM Mission Simulator, Volume II, Technical Addendum*, public scan: https://www.ibiblio.org/apollo/Documents/proposal_for_lem_mission_simulator_vol2.pdf
- Brian Woycechowsky, *Lunar Module Moon-Referenced Equations of Motion* (2021), including its citation to Grumman LED-440-3: https://static1.squarespace.com/static/567433669cadb6ac8da3ff92/t/6071a7ea04f3ed70ebd956f0/1618061309500/lunar%2Bv6.0%2B%2Bincl%2Bcover%2Bsupplement%2B%2B%2Bfront%2Bmatter.pdf
- NASA/NARA corporate-index evidence for Grumman LED 500-5 and LED 500-16, preserved through the Virtual AGC index lineage.

## Evidence boundary

The Link proposal is a primary contractor source but has not yet been page-extracted in this pass. LED-440-3 is identified through a modern source that explicitly cites and reconstructs it; the original report still requires direct review. Claims above are therefore limited to document identity, model partition/interface evidence visible in the reconstruction, and a project architecture inference. No primary-source evidence label is upgraded.
