# Causal Simulation Engine

Status: **current architecture direction; implementation staged through the validation harness**

This document defines the project-level numerical/state architecture needed to let controller actions produce realistic consequences without pre-authoring every outcome branch.

It is not a claim that the Apollo spacecraft or original LMS software used these exact software abstractions. Historical simulator documentation is used to constrain model boundaries and fidelity; modern implementation details remain project choices.

## Goal

The simulator should support this general loop:

scenario initial conditions / external failures
+ controller instructions / simulated crew actions
+ elapsed time
→ authoritative causal state
→ subsystem models
→ instrumentation / onboard indications
→ telemetry / communications / ground processing
→ controller products and crew reports
→ player decisions / CAPCOM instructions
→ back into the causal state loop

A scenario supplies the starting problem. It does not enumerate all possible player outcomes.

## Historical simulator basis

Current research has identified direct evidence for this type of architecture:

- Grumman LED 500-5, *LMS Math Model — Equations of Motion, Subsystem Interfaces and Visual Display Drive Equations*, 22 April 1965;
- Grumman LED-440-3, *LEM Mission Simulator (LMS) Math Model: True Motion Equations*, August 1965, whose separately reconstructed model flow exposes interfaces among propulsion, stabilization/control, weight/balance, disturbances, and true-motion integration;
- Grumman LED 500-16, *LEM Guidance Computer (LGC) Math Model for the Full Mission Engineering Simulator (FMES) and LEM Mission Simulator (LMS)*, 8 June 1966;
- Link Group's *Proposal for LEM Mission Simulator, Volume II, Technical Addendum*, whose surviving scan contains LMS mathematical-equation flowcharts;
- a Grumman memo studying the effect of 50-millisecond LMS integration steps on simulated Abort Attitude Control System response;
- North American Aviation's 1965 preliminary *Apollo Mission Simulator Instructor Handbook, Volume II*, which directly documents five operational-program classes, a continually updated equations-of-motion feedback loop, manual/preprogrammed/time-dependent malfunction insertion, and separable simulator/telemetry/interface paths;
- the separately archived *Lunar Module Mission Simulator Instructor's Handbook, Volume I*, whose direct extraction remains pending.

These sources establish that equations of motion, subsystem interfaces, model partitions, numerical integration behavior, display-driving outputs, and malfunction placement were explicit simulator concerns. The AMS handbook also shows that telemetry could be derived from simulated systems or affected through a direct telemetry malfunction, strengthening the project's physical-truth/observation separation. They do not yet establish every equation, constant, or Apollo-13-specific configuration we should implement.

The public 1965 AMS handbook is preliminary initial-configuration evidence and explicitly is not design-requirements data. It must not be silently generalized to accepted Block II/Apollo 13 behavior or conflated with the LMS handbook lineage.

See research notes 127–130 and 134–136 and resources/source-catalog/APOLLO_SIMULATION_ENGINE_SOURCES.md. LED-440-3 and LED 500-5 remain distinct document identities unless future primary-source review establishes their relationship.

## Modern simulator reference boundary

Orbiter and Project Apollo–NASSP may be used to review implementation choices, discover missing mechanisms and primary-source leads, or construct independently specified comparison cases. They are not evidence of historical Apollo behavior.

- Orbiter is MIT-licensed and useful for numerical integration, state propagation, timestep, and convergence review.
- NASSP is GPL-licensed and useful for Apollo subsystem reconnaissance, but its code must not be copied into this project without a deliberate license decision. Its values and equations must be traced to primary documents, and its explicit approximations must not become hidden project assumptions.

Research note 136 records this boundary. No modern simulator dependency is currently selected.

## Core architecture rule

If the simulator supports an action, the action must change commanded/configuration state or an external condition. It should not directly select a narrative result.

Bad pattern:

wrong burn duration → assign bad-trajectory outcome

Required pattern:

burn instruction → crew action → propulsion state → thrust/mass flow → attitude/thrust direction → numerical dynamics → new position/velocity/mass → tracking/trajectory products → controller observation

The same model therefore handles a nominal burn, early cutoff, late cutoff, wrong throttle setting, incorrect attitude, or combinations of those conditions.

## Model types

The engine is intentionally hybrid. Not every subsystem requires the same mathematics.

### Continuous numerical models

Use where state changes continuously and timing matters.

Likely examples:

- translational dynamics;
- rotational/attitude dynamics where required;
- thrust and propellant depletion;
- battery charge depletion;
- consumable depletion;
- tank/pressure evolution where supported by source and gameplay need.

### Algebraic models

Use where output is a direct function of current state/configuration.

Examples may include:

- bus/load power balance;
- some sensor conversions;
- static pressure/temperature relationships;
- derived controller quantities.

### Discrete state machines

Use for configuration and logic.

Examples:

- switch/breaker/valve position;
- engine command state;
- guidance/program mode;
- communications path selection;
- relay/contactor logic where circuit-level modeling is unnecessary;
- crew procedural state.

### Event models

Use for genuinely external/discrete occurrences.

Examples:

- a scenario malfunction injection;
- ground-station loss;
- external tank rupture;
- scheduled mission-plan communication;
- exercise-control intervention.

An event may modify state. It should not bypass causal state to impose downstream consequences that should be calculated.

## Time and integration

Mission GET remains continuous when the session is RUNNING.

The causal engine adds an internal model clock beneath the existing session clock.

Each numerical model must declare:

- state variables;
- input variables;
- derivative/update rule;
- integration method;
- numerical step policy;
- outputs;
- source provenance;
- validity/fidelity limits.

### Timestep rule

Do not assume one historical timestep globally.

The surviving Grumman 50 ms memo establishes that timestep sensitivity mattered for at least one LMS attitude-control response. It does not prove that every LMS model ran at 50 ms.

Project implementation may use a modern fixed or adaptive integrator. The important requirements are:

1. deterministic results for identical inputs/configuration;
2. convergence checks showing materially similar outcomes when the step is refined;
3. an explicit model-level integration contract;
4. no coupling of physical integration cadence to browser polling cadence;
5. no assumption that historical numerical limitations are fidelity requirements.

## Authoritative state vs observations

The engine must continue the separation already established in the project.

authoritative physical/logical state != onboard indication != raw telemetry != ground-processed value != controller interpretation != crew report

A physical state change may produce several observations with different delays, failures, validity states, or biases.

Conversely, an observation failure must not silently modify physical truth.

## Scenario contract

A scenario should define only what is external to the reusable model or necessary to initialize it.

Typical scenario content:

- epoch / GET start;
- spacecraft configuration/profile;
- initial dynamic state;
- initial subsystem configuration;
- initial consumable quantities;
- mission objectives and nominal plan;
- externally injected malfunction/environment/network events;
- scenario-specific crew/ground communications where intentionally fixed.

Scenario files should not contain tables enumerating every possible player-error outcome.

## Simulated crew contract

The flight crew is simulation-controlled.

CAPCOM messages are structured simulation inputs. For supported message types:

1. crew receives the transmission;
2. crew may acknowledge/report using bounded canned text/state;
3. crew performs the associated cockpit action at the applicable time;
4. that action changes command/configuration state;
5. the physical subsystem decides what actually happens;
6. later crew reports remain an observation channel rather than hidden truth.

The crew model is not an AI decision-maker at this stage. It is deterministic exercise infrastructure representing the non-player spacecraft crew.

## First numerical vertical slice

The first implementation should prove that arbitrary burn inputs create computed consequences.

### Model chain

burn command / crew action
→ DPS propulsion model
→ thrust magnitude + mass flow + engine state
→ attitude / thrust-direction model
→ translational dynamics
→ position + velocity + vehicle mass
→ derived maneuver / trajectory result
→ controller-observable tracking/trajectory product

### Source-bounded PC+2 validation case

Existing Apollo 13 evidence provides a useful regression case:

- PC+2 TIG: 79:27:38.30 GET;
- actual burn duration: approximately 263.82 s;
- staged throttle-command profile beginning at low thrust, then 40 percent, then maximum thrust; the terminal portion was completed in blowdown after pressurization isolation;
- executed PGNS velocity components are documented;
- resultant maneuver magnitude and postburn residual evidence are documented;
- Apollo 13 documentation gives final-PAD CSM/LM weights and separately shows that RTCC LM-burn mass-property decks had been updated to a T+55 set; premission mass properties were explicitly rejected as inferior for PC+2 DPS trim work;
- Apollo 13 configuration documentation gives 9870 lbf nominal full thrust, while general DPS engineering documentation uses distinct rated-thrust/fixed-throttle-point terminology; exact LM-7 delivered thrust and effective Isp remain unfrozen.

The historical case is a validation oracle, not the simulation algorithm.

The engine should calculate the result from state and commands, then compare with the historical result.

## First acceptance tests

The validation harness should support at least these cases without adding separate outcome branches.

### Nominal

Use the source-backed PC+2 command profile.

Expected: computed burn result falls within an explicitly documented model tolerance of the source-backed historical target once required model inputs are frozen.

### Early cutoff

Cut the engine before nominal cutoff.

Expected:

- less accumulated impulse/Delta-V;
- more remaining propellant;
- changed postburn trajectory product.

### Late cutoff

Continue beyond nominal cutoff.

Expected:

- greater accumulated impulse/Delta-V;
- less remaining propellant;
- changed postburn trajectory product.

### Wrong throttle

Hold an incorrect supported throttle setting.

Expected consequence emerges from thrust and mass-flow integration.

### Wrong attitude

Apply the same thrust history at an offset attitude.

Expected:

- similar scalar impulse if thrust history is unchanged;
- different vector Delta-V;
- different trajectory product.

### Combined error

Allow wrong attitude plus wrong duration/throttle.

Expected: no special scenario branch is required.

## Fidelity ladder

The model should grow by replacing abstractions, not by rewriting the architecture.

### Level 1 — impulse / translational proof

- thrust magnitude;
- mass depletion;
- prescribed attitude/thrust direction;
- translational integration;
- derived Delta-V / trajectory state.

### Level 1B — translational trajectory propagation

- position + velocity state;
- optional caller-supplied central gravity;
- propulsion/trajectory coupling;
- explicit frame/epoch applicability boundary;
- synthetic orbit/coast convergence tests.

This layer is implemented in `causal_translational_model.py`. It contains no Earth, Moon, Apollo, or scenario constants and remains a model proof until a scenario supplies sourced frame, state, gravity, propulsion, and tolerance inputs.

### Level 2 — propulsion state

- engine command vs actual state;
- throttle limits/zones;
- restart/shutdown eligibility;
- propellant/pressurization dependencies needed by supported failures.

### Level 3 — attitude/control coupling

- commanded vs actual attitude;
- rotational response where needed;
- gimbal/RCS authority and failure effects.

### Level 4 — electrical / consumables

- sources, buses, loads, switching;
- battery energy/current;
- consumable rates tied to active equipment.

The first mission-neutral electrical proof is implemented in `electrical_power_model.py`. It evaluates caller-supplied source capacity, bus enablement, commanded load demand, and explicit load priority to derive equipment powered/unpowered state. A separate `resource_inventory_model.py` now propagates finite resource quantities under caller-supplied piecewise flow rates and reports depletion/overflow boundaries. The models remain deliberately separate: a depleted resource does not silently disable an electrical source until an explicit sourced coupling is configured.

### Level 4B — tracking observation proof

- authoritative trajectory state remains hidden;
- internal geometric range/range-rate truth is derived separately;
- caller-supplied delay, bias, availability, and validity create downstream observations;
- unavailable observations withhold values;
- invalid observations may remain visible but are explicitly flagged;
- no Apollo/MSFN/RTCC tracking constants are embedded.

Implemented in `tracking_observation.py`; see `docs/models/TRACKING_OBSERVATION_PROOF.md`. The facilitator validation API now exposes the combined synthetic chain through `POST /api/admin/model-proof/trajectory-tracking`.

### Level 5 — observation chain

- onboard sensors/indications;
- telemetry channels;
- communications/ground processing;
- controller products.

The order may change if newly recovered simulator documentation shows a more useful model boundary.


## Cross-model composition proof

The reusable resource, electrical, and observation layers are now exercised in one synthetic causal chain:

`finite resource -> electrical source availability -> powered load -> observation availability`

The chain uses an explicit `ResourceElectricalSourceRule` coupling with caller-supplied operating threshold/provenance. A depletion outcome is therefore propagated through model state rather than selected by a scenario branch. Hardware/source availability remains distinct from resource sufficiency.

See `docs/models/RESOURCE_POWER_OBSERVATION_CHAIN.md`. The facilitator validation API exposes independent resource/electrical proofs plus the composed chain; the composed endpoint does not accept a direct electrical-source availability override.

## Source and validation requirements

Every implemented numerical model must carry:

- source list;
- mission/profile applicability;
- modeled variables and units;
- assumptions;
- unsupported/deferred mechanisms;
- regression cases;
- numerical convergence test where integration is used.

A simulator-era equation may be adopted only after checking whether it describes the relevant LMS/FMES configuration and whether its constants/configuration are applicable to Apollo 13/LM-7.

## Validation / acceptance boundary

Research note 219 locates a NASA/JSC archival series for the Lunar Module Simulator (RG 255 E.155B1, 1968–1970) whose inventory explicitly includes **acceptance test plans and procedures**. This establishes that formal acceptance documentation existed and survives as a targeted source family, but the inventory does not disclose the tests' numerical criteria.

Until those records or equivalent LMS validation/correlation documents are directly recovered, the project separates:

1. **numerical/model verification** — convergence, invariants, and declared project numerical behavior;
2. **historical source/profile validation** — comparison only against source-backed mission/vehicle targets or ranges;
3. **measurement/output validation** — source state to sourced output representation without unsourced routing or hidden-truth leakage;
4. **causal scenario validation** — action/crew/subsystem/observation consequence propagation;
5. **live integration validation** — preservation of those boundaries through the deployed multi-client runtime.

A project test passing one layer is not described as a historical LMS acceptance test. Historical error bounds, correlation tolerances, or pass/fail limits remain source-gated.

The known LMS **Simulator Output Tables** (LMA-790-2-LMS Volume II, Section 7, accession *67-16127) are a complementary retrieval target because they may identify validation-observable outputs, but their existence alone does not establish acceptance tolerances.

## Near-term implementation gate

Do not build a broad subsystem framework just because this architecture anticipates one.

Research note 134 partially clears this gate at the interface level. The first proof may use:

- time, mass, vector velocity, optional position, accumulated impulse, and explicit frame metadata as state;
- separate propulsion, prescribed-attitude/thrust-direction, mass-properties, dynamics, and observation-product boundaries;
- an assumption-visible deterministic integrator with convergence and correct/early/late/wrong-input ordering tests.

This authorizes a **model proof**, not a historically validated Apollo 13 PC+2 propagator. Mission-specific delivered-thrust/mass-flow history, exact mass/depletion convention, coordinate-frame mapping, and numerical acceptance tolerance remain integration gates until closed under D-022.

A gate closes by either:

1. **recovery** of the required value/mechanism from primary sources; or
2. **demonstrated irrelevance** across the full sourced plausible range, evaluated at the resolution of the actual player-visible station products.

Demonstrated irrelevance must use sourced range endpoints, compare controller-readable products rather than hidden model state, and be recorded in a research note with the tested range and observed product deltas. If any player-visible product changes at its real resolution, the gate remains closed and archival work continues. A value frozen after an irrelevance result is an arbitrary in-range implementation choice, not a historical claim.

This does not permit averaging conflicting sources, inventing a bracket, or collapsing an unresolved mechanism.

Research notes 137–138 establish final PAD weights plus an in-flight updated T+55 RTCC mass-property-deck lineage, but not exact physical ignition mass. Research note 139 establishes PC+2 command timing, terminal blowdown, and a mission-configuration nominal full-thrust value, while leaving startup transient, LM-7 thrust calibration, and effective Isp unresolved. Research note 147 adds a separate mission-report PC+2 ignition/cutoff event-mass datum that must not be silently equated with the final P30 module-weight sum.

## Level-1 implementation status

The first mission-neutral numerical proof is implemented in `causal_dps_model.py` and exposed only through the facilitator validation API/console. Subsequent reusable proofs now include translational dynamics, tracking observations, guidance cross-checks, landing-radar qualification/gating, deterministic simulated crew behavior, coarse electrical power/equipment availability, and finite resource inventory/depletion.

It now demonstrates, through one model path:

- thrust-driven mass depletion and impulse;
- prescribed-direction vector Delta-V;
- deterministic fixed-step midpoint integration;
- constant-thrust and caller-supplied linear start-to-end thrust segments;
- optional segment-specific effective-Isp overrides;
- explicit caller-supplied regime labels such as startup/regulated/blowdown without hidden regime physics;
- convergence as the step is refined;
- correctly ordered early, late, wrong-thrust, wrong-direction, and combined-error consequences;
- explicit applicability, provenance, assumptions, and a non-historical-validation status.

See `docs/models/DPS_LEVEL1_MODEL_PROOF.md`, `docs/models/TRANSLATIONAL_DYNAMICS_MODEL_PROOF.md`, and `docs/models/TRACKING_OBSERVATION_PROOF.md`.

The existing historical PC+2 event model remains the deployed integration scaffold. A separate mission-neutral translational proof now propagates position, velocity, and mass under supplied propulsion plus optional central gravity, providing a reusable trajectory foundation for later scenarios. The proof does not yet mutate live scenario state or generate player-visible products. Historical scenario integration remains gated on source-backed delivered-thrust/mass-flow treatment, mass/depletion convention, frame mapping, gravity/trajectory treatment, and acceptance tolerance appropriate to that scenario. For PC+2 specifically, the model can now accept a recovered startup/blowdown profile without another integrator redesign; no Apollo 13 transient curve or propulsion constant has been inserted.
