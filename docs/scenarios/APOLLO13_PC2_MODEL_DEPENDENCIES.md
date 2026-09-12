# Apollo 13 PC+2 — Subsystem Dependency Contract

Status: **pre-implementation model contract**

## Purpose

This document defines which parts of the authoritative simulation must depend on which other parts for the PC+2 vertical slice.

It intentionally avoids unsupported detailed equations. A dependency is included because the historical workflow requires it; numerical fidelity is added only when a source or validation requirement justifies it.

---

## 1. Mission clock and scenario phase

`mission.get_s` drives:

- scheduled communication events;
- PAD/readback window;
- power-up sequence;
- GO/NO-GO window;
- P40/preignition sequence;
- ullage/TIG;
- expected cutoff window;
- post-burn transition.

Clock time alone must **not** force a state transition when the transition historically depends on readiness or action. For example, reaching the GO-poll time does not make the vehicle GO automatically.

---

## 2. Communications path

Physical/command configuration:

`S-band configuration + geometry/network availability`

feeds:

`voice quality / telemetry availability / uplink availability / ranging availability`

which feeds:

- CAPCOM PAD/readback success;
- telemetry validity/age at controller stations;
- GUIDO update workflow;
- FIDO ranging/trajectory support;
- readiness recommendations.

The nominal scenario begins with degraded air-ground quality and improves after the S-band power-amplifier change.

The data model must therefore allow a healthy spacecraft subsystem to be temporarily unavailable or stale at Mission Control.

---

## 3. Ground trajectory and maneuver target

Authoritative trajectory state, once implemented, feeds:

- RTCC trajectory solution;
- PC+2 maneuver target;
- predicted perigee;
- landing/entry return products;
- post-burn trajectory assessment.

For the first non-propagating fixture, source-backed RTCC products may be loaded directly as historical ground products.

Do **not** infer an exact historical Cartesian trajectory vector from the maneuver PAD merely to populate an internal structure.

When propagation is implemented, the trajectory layer must become authoritative and these products must be derived from it.

---

## 4. Maneuver coordinate representations

Maintain distinct values for:

1. RTCC / maneuver-PAD LVLH ΔV components;
2. PGNS target Vg in IMU coordinates;
3. true achieved physical ΔV;
4. PGNS sensed/estimated achieved ΔV;
5. post-burn PGNS residuals;
6. post-burn ground trajectory residual/solution.

These may agree closely in the nominal case but are not the same state.

A later guidance, sensor, alignment, or ground-processing failure must be able to make them disagree.

---

## 5. Guidance and attitude knowledge

True vehicle attitude/rate feeds:

- spacecraft physical orientation/dynamics;
- attitude-control requirements.

PGNS sensing/computation feeds separate onboard estimates:

- PGNS attitude knowledge;
- guidance attitude error;
- velocity-to-be-gained;
- program state and guidance residuals.

AGS provides a separate backup/cross-check information path.

Controller products may contain combinations/comparisons of these states but must not collapse them into a single `attitude_ok` value.

---

## 6. RCS ullage → DPS ignition readiness

Nominal dependency:

`RCS capability`

→ `two-jet ullage command`

→ `10-s ullage event`

→ `propellant settling / DPS ignition readiness`

The first nominal model may represent settling with a simple state transition because PC+2 validation does not require tank-fluid dynamics.

However, ignition readiness must remain causally dependent on successful ullage so a later failure case can interrupt it.

---

## 7. DPS propulsion chain

Minimum causal chain:

`engine arm/start + propellant/inlet availability + control-electronics availability`

→ `engine operating state`

→ `throttle command`

→ `actual thrust / chamber-pressure behavior`

→ `vehicle acceleration / achieved ΔV`

→ `PGNS sensed guidance progression`

→ `guided cutoff / residuals`

The nominal throttle schedule is source-backed:

- initial minimum-thrust segment;
- approximately 21 seconds at 40%;
- remainder at maximum thrust.

Exact thrust-vs-throttle curves, engine transient equations, propellant flow, and chamber-pressure dynamics are **not yet frozen**. Add them when required to reproduce the historical burn duration/ΔV and support meaningful failure cases.

---

## 8. Mass dependency

The final maneuver PAD gives separate CSM and LM weights.

When a physical burn propagator is added:

`CSM mass + LM mass + propellant consumption`

must influence acceleration and achieved ΔV.

Until then, the historical weights are retained as scenario inputs rather than used to imply unsupported high-fidelity mass-flow behavior.

---

## 9. Propulsion shutdown-rule measurements

Underlying propulsion state feeds separate measured/controller products:

- thrust/chamber-pressure indication;
- inlet pressure;
- fuel/oxidizer differential pressure;
- gimbal warning/state.

Rules apply to the **historically available indication**, not automatically to perfect internal state.

This is especially important for the fuel/oxidizer ΔP criterion because the crew depended on a ground callout.

---

## 10. Vehicle attitude/control shutdown rules

Physical/control state feeds:

- attitude error indication;
- body-rate indication;
- CES status;
- engine-gimbal status.

PC+2 shutdown limits include approximately:

- ±10° attitude error outside startup transients;
- ±10°/s attitude rate.

A startup-transient allowance must therefore exist in rule evaluation rather than applying the threshold blindly from ignition instant.

---

## 11. Electrical power dependency

LM electrical configuration feeds:

- LGC/PGNS operation;
- CES/control availability;
- communication equipment availability;
- instrumentation/telemetry availability;
- burn-configuration current draw;
- inverter warning/status.

The first slice needs enough electrical behavior to distinguish:

- low-power configuration;
- burn configuration (~38–40 A historical load);
- relevant warning/failure states;
- post-burn power-down.

It does not require a full mission-long battery/thermal model initially.

---

## 12. Telemetry and controller data

For each player-facing dynamic parameter:

`authoritative/onboard/measured source`

→ `sampling`

→ `transmission/link`

→ `ground reception`

→ `ground processing`

→ `controller product`

Metadata must support:

- source sample time;
- ground receive time;
- validity;
- stale/unavailable state;
- provenance/source layer.

Nominal first implementation may set many transport delays/errors to zero after communications stabilize, but the boundaries must remain in the schema.

---

## 13. Controller readiness is not authoritative state

Each station derives a recommendation from its own products.

Examples:

- GUIDO: guidance/alignment/load readiness;
- CONTROL: propulsion/control readiness;
- TELMU: electrical configuration readiness;
- FIDO: trajectory/target readiness;
- INCO: communication/data-path readiness.

FLIGHT integrates those recommendations.

The simulation may record these decisions, but it must not expose a hidden `vehicle_ready=true` flag to players as a substitute for controller work.

---

## 14. Burn success is an assessment, not a primitive

There is no player-visible authoritative `burn_success` parameter.

Nominal success emerges from:

- no mandatory shutdown condition;
- guided cutoff near expected time;
- acceptable PGNS residuals;
- acceptable post-burn trajectory result;
- viable vehicle state for power-down/return.

The simulation engine may compute an internal validation result for automated testing, but it is not an operational display.

---

## 15. Deferred dependencies

Do not add unless first-slice behavior demands them:

- detailed cryogenic/environmental physics;
- full LM thermal model;
- complete RCS propellant plumbing;
- exact AGS ullage CRT transformation;
- radar models not used by PC+2;
- full RTCC implementation;
- complete MSFN station/network simulation;
- exact display routing for noncritical fields.

## Immediate implementation consequence

The first code/data layer should represent:

1. source-backed scenario constants;
2. rule thresholds/conditions;
3. state-machine phases;
4. authoritative state containers with information-layer separation;
5. controller-product metadata;
6. historical nominal validation targets.

Detailed subsystem equations should follow after this structure is executable and validated.
