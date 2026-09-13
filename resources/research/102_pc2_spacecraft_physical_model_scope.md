# 102 — PC+2 spacecraft physical-model scope

Date: 2026-09-13  
Status: **RESOLVED FOR FIRST PLAYABLE — decision-relevant causal model bounded; full-spacecraft emulation not required**

## Question

How much of the Apollo spacecraft must be physically modeled for the PC+2 first playable?

This resolves open question 12 for the selected Apollo 13 PC+2 slice only. It does not define the fidelity needed by later scenarios.

## Primary evidence reviewed

### Apollo 13 PC+2 operational record

The Apollo 13 Mission Operations Report and preserved air-ground chronology already establish the scenario's operational dependencies: the LM descent propulsion system performs PC+2; guidance supplies maneuver execution/residual information; communications and uplink support the final load and crew coordination; controllers monitor source-derived spacecraft data; and the immediate post-burn state transitions into LM power conservation while retaining functions needed for communications, guidance/navigation, and PTC preparation. See research notes 098–101 and their source catalogs.

### Apollo Experience Report — Lunar Module Instrumentation Subsystem

NASA TN D-6845 states that the LM instrumentation subsystem processed approximately 250 measurements for display, caution/warning, and telemetry, including analog values such as pressure, temperature, and quantity and discrete values such as switch closures. It also describes instrumentation as the layer that monitored LM subsystems and prepared data for transmission to the Manned Space Flight Network.

Implication: the simulation should preserve the causal distinction between physical state, sensed/conditioned observation, telemetry/product state, and controller interpretation. It does **not** follow that all ~250 LM measurements must be modeled for a scenario whose controller decisions touch only a small subset.

### Apollo Experience Report — Descent Propulsion System

NASA TN D-7143 documents the DPS as a pressure-fed, throttleable propulsion system with distinct pressurization, propellant storage/feed, engine, and guidance/control interfaces. The PC+2 slice and its synthetic ΔP branch depend on those causal relationships.

Implication: the first playable needs enough DPS physics/state to distinguish propellant/feed/pressure observations, commanded engine response, chamber-pressure evidence, and maneuver outcome. It does not need a complete thermofluid engine simulation.

### Apollo Experience Report — Guidance and Control / LM stabilization and control

NASA TN D-8086 describes the stabilization/control subsystem as providing LM attitude and translation control, using the reaction-control jets and interfacing with guidance and propulsion.

Implication: PC+2 needs authoritative attitude/guidance state sufficient for sourced attitude/rate criteria, burn execution/residuals, and the transition toward PTC. A full six-degree-of-freedom vehicle dynamics and RCS pulse-level simulation is not required before a controller decision depends on it.

### Apollo Experience Report — Lunar Module Electrical Power Subsystem

NASA TN D-6977 documents the LM electrical-power subsystem as an integrated spacecraft subsystem whose configuration and flight performance determine equipment availability.

Implication: because PC+2 includes maneuver power-up followed by a deliberate post-burn power-down while selected communications/guidance/PTC functions remain available, the simulator needs coarse causal electrical state: power source/bus/inverter/load configuration sufficient to govern whether modeled equipment/products remain available. It does not need wire-, breaker-, or battery-electrochemistry-level emulation for the current slice.

### Apollo Experience Report — Lunar Module Communications System

NASA TN D-6974 states that the LM communications system provided voice, telemetry, ranging information, and communications links between the LM, MSFN, CSM, and crew.

Implication: the first playable must model communications **availability/state and operational consequences** where they affect INCO, CAPCOM, ranging, telemetry, or the final uplink workflow. It need not reproduce RF propagation, modulation, antenna patterns, or detailed ground-network signal processing unless a later failure scenario requires those mechanisms.

## First-playable physical-model boundary

The authoritative spacecraft model should contain only physical or equipment state needed to produce historically sourced player information, enforce sourced procedures/rules, or support a selected scenario branch.

### Required causal domains

1. **DPS / maneuver state**
   - engine command/running state;
   - source-bounded propellant/feed/pressure state used by CONTROL evidence and the synthetic ΔP branch;
   - chamber-pressure observation pathway;
   - maneuver execution/result sufficient for nominal PC+2 and a premature-shutdown/restart path.

2. **Guidance / attitude / control state**
   - guidance solution/load state already modeled by the staged final-load workflow;
   - attitude/error/rate state sufficient for sourced PC+2 monitoring criteria;
   - post-burn residual/result state;
   - coarse control/PTC-readiness state where needed for the note-101 transition.

3. **Electrical configuration / equipment availability**
   - enough power-source/bus/inverter/load state to make selected equipment and telemetry products available or unavailable;
   - explicit distinction between burn configuration and post-burn partial power-down;
   - no unsupported breaker-by-breaker or current-draw simulation.

4. **Communications / uplink / ranging availability**
   - operational availability/state affecting INCO/CAPCOM, final-load transmission, ranging, crew communication, and telemetry flow;
   - no RF/link-budget simulation unless demanded by a later communications failure.

5. **Instrumentation / observation integrity**
   - physical state must remain distinct from sensor observation, validity/freshness, telemetry/product state, and controller conclusion;
   - model only measurements actually needed by implemented station products, rules, or failure branches.

### Not required for current first playable

Do not build merely for completeness:

- full LM ECS consumables/thermal/CO2 dynamics;
- full CSM subsystem physics while Odyssey is not driving a PC+2 controller decision;
- structural dynamics;
- landing/rendezvous radar physics unrelated to the selected ranging/uplink products;
- full six-degree-of-freedom translational/orbital propagation;
- pulse-level RCS jet simulation;
- detailed battery chemistry, wiring, breaker, or load-current emulation;
- RF propagation/modulation/antenna physics;
- all LM instrumentation channels;
- internal RTCC/CCATS computation beyond products required by players.

A deferred subsystem becomes required only when a sourced player decision, procedure, observable, or selected failure mechanism depends on it.

## Design rule

Use a **decision-relevant causal fidelity** test before adding spacecraft physics:

`historical/player decision dependency → required physical cause → required sensed/processed observation → station product/action`

If that chain cannot be stated from evidence and scenario need, the physical detail stays out of the first playable.

This is a scope rule, not permission to fake missing historical data. When a required link is historically unresolved, preserve it as unresolved rather than inventing a convenient mechanism.

## Open-question effect

Open question 12 is resolved **for the PC+2 first playable**. Later scenarios may require additional LM, CSM, MSFN, or trajectory physics and must reopen the boundary from their own sourced decision dependencies.