# Research note 214 — D-022 initial PC+2 numerical-gate survey

Date: 2026-09-15

## Question

Does any currently unresolved Apollo 13 PC+2 numerical integration gate already have a **fully sourced plausible range for one historical model input** that can be tested under Decision D-022?

D-022 permits a gate to close by demonstrated irrelevance only when both ends of the tested range are independently sourced as bounds on the same input/semantics and the full range is shown not to alter controller-visible products at their actual resolution.

This note is a repository-reading survey. It does not add new historical source claims.

## Survey

| Integration gate | Current sourced evidence | Valid D-022 range today? | Reason |
|---|---|---:|---|
| Physical ignition mass / mass convention | Final P30 module weights total 95,932 lb; postflight reconstructed PC+2 ignition event mass 95,424.0 lb | **No** | Research notes 147–148 classify these as different historical product classes. No source establishes them as lower/upper bounds on one physical/RTCC input. |
| RTCC T+55 mass/depletion state | T+55 LM-burn deck family is documented; exact deck semantics, job, candidate trim, and depletion propagation remain unresolved | **No** | No two sourced numerical endpoints for the same T+55 model quantity. |
| LM-7 full-thrust force | Apollo 13 vehicle baseline gives 9,870 lbf nominal full thrust; general DPS design material gives 10,500 lbf maximum rated thrust | **No** | Research note 139 explicitly warns that these are different definitions/configuration terms, not two estimates of one delivered-thrust value. |
| Startup transient | Mission-specific evidence shows startup buildup can be non-instantaneous and operationally material | **No** | The surviving evidence in note 139 does not provide a quantitative minimum/maximum startup history or duration for PC+2. |
| Effective specific impulse | General DPS design evidence gives 305 lbf-s/lbm at end of duty cycle | **No** | This is a single fleet/design value, not a sourced LM-7 PC+2 interval. |
| Throttle-dependent thrust / mass flow | Commanded 12.6%, 40%, maximum phases and terminal blowdown are sourced | **No** | Command labels/timing are sourced, but no same-variable force/mass-flow endpoint pair is recovered for LM-7 PC+2. |
| Terminal blowdown pressure/thrust history | Blowdown mode and isolation timing are source-backed | **No** | No quantitative same-input min/max curve or endpoint range has been recovered. |
| Final commanded GDA trim | Final trim remains unrecovered; generic LM hardware supports ±6° gimbal travel and ±2 in actuator stroke | **No current D-022 test** | Hardware travel limits are not a sourced plausible PC+2 final-trim interval, and exact LM-7 calibration plus thrust-direction coupling remain unresolved. Using the full hardware envelope as a PC+2 trim bracket would collapse the unresolved mechanism rather than source it. |
| Historical translational frame / initial state | Generic propagator exists; historical PC+2 frame/state remains unresolved | **No** | No two sourced bounds for one missing state-vector component/epoch convention are established. |
| MSFN/RTCC tracking cadence/latency/configuration | Generic observation machinery exists | **No** | No sourced interval for the missing H-2 observation cadence/latency/configuration has been established. |
| Historical numerical acceptance tolerance | Required by the validation contract | **No** | No sourced historical/product-resolution tolerance pair has been established for the numerical propagator regression. |

## Finding

**D-022 currently has no valid PC+2 numerical target.**

This is not a failure of D-022. It is a positive governance result: the policy prevents the project from converting semantically different values or generic hardware/design limits into invented uncertainty brackets.

The immediate consequence is that the affected gates remain open and the archival work already identified by the research notes remains justified.

## What would activate D-022

A future D-022 test becomes valid when primary evidence supplies two defensible endpoints for the **same** model input and applicability. Examples could include:

- an LM-7 acceptance/performance report giving a bounded delivered-thrust or Isp range for the relevant regime;
- PC+2 high-speed propulsion data with stated measurement/calibration uncertainty;
- an H-2 mass-properties/depletion document giving an explicit numerical tolerance/range for the same state quantity;
- a source-backed final GDA trim tolerance or bounded candidate interval tied to PC+2;
- a controller-product specification giving a true historical resolution/tolerance paired with a sourced input interval.

Once such a range exists, D-022 requires endpoint propagation through the causal model and comparison against the actual player-visible station products—not only against hidden internal delta-v/state.

## Priority consequence

Until one of those range-producing artifacts is recovered, D-022 should remain available but **not be scheduled as if a current target already exists**.

Highest-value archival targets remain:

1. Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*;
2. LM-7 engine acceptance/calibration or PC+2 high-speed propulsion data;
3. H-2 RTCC/Flight Dynamics mass-property/depletion working records;
4. the final PC+2 GDA/P30 working artifact;
5. source material defining historical trajectory/tracking product resolution and acceptance tolerances.

## Related repository evidence

- research notes 137–139 — P30 mass semantics, T+55 lineage, DPS performance boundary;
- research notes 147–148 — event mass versus operational P30 product-class separation;
- research notes 153–155 — final GDA/dual-unit/calibration boundary;
- research notes 159–161 — Luminary N47 path, no-update precedent, T+55 deck-epoch boundary;
- `data/model_profiles/apollo13_h2_dynamics_partial.json`;
- `docs/CAUSAL_SIMULATION_ENGINE.md`.
