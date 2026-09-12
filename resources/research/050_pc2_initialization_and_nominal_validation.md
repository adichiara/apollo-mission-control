# Apollo 13 PC+2 — initialization state and nominal validation

Date: 2026-09-12  
Status: **REVIEWED — sufficient to define the first-slice initialization contract and nominal validation targets; exact RTCC state-vector numerics remain deferred until required by the trajectory implementation.**

## Purpose

Research note 049 mapped the controller actions and burn rules for the selected Apollo 13 PC+2 vertical slice. This pass answers the next implementation question:

> What state must exist when the scenario begins, and what historical values should a nominal run reproduce?

The scope is deliberately bounded. The objective is not to reconstruct every spacecraft or RTCC state variable at 77:55 GET. It is to identify the minimum authoritative state needed to support the documented controller workflow from the final PC+2 PAD through burn completion and immediate power-down.

---

## 1. Recommended scenario start: 77:55:00 GET

The strongest natural start boundary is **77:55 GET**.

This is preferable to an arbitrary round time because the surviving air-ground record shows a real operational transition at that point:

- communications have just been reacquired after lunar occultation;
- the link is weak;
- CAPCOM begins the **final PC+2 P30 LM maneuver PAD** at 77:55:24;
- the weak link causes an incomplete readback and requires the crew to raise S-band power before confirming the PAD;
- the final maneuver data are therefore still an active information-transfer task rather than preloaded scenario context.

This gives the first slice an immediate historically grounded controller/crew communication task without requiring simulation of the preceding lunar flyby.

### Initial communication state

At approximately 77:55:

- LM air-ground contact exists but is weak;
- CAPCOM reports the crew very weak;
- the crew later raises the S-band power amplifier and communications become loud and clear at 77:59:17;
- ranging is explicitly required later during burn preparation;
- telemetry/uplink state therefore belongs in the authoritative scenario state, not as an always-on assumption.

---

## 2. Historical state already established before scenario start

The scenario may initialize the following as **completed historical context** rather than replaying it:

- the CSM/LM stack is docked;
- the CSM is largely powered down and the LM is serving as the lifeboat;
- the spacecraft is already on the free-return trajectory established by the earlier LM DPS maneuver;
- LM PGNS/LGC is operating;
- the LM platform was docked-aligned to the CMC earlier in the contingency;
- the 74-hour Sun check and backside gross star check found the LM platform acceptable for PC+2 without a new P52;
- the Sun check corresponded to approximately **0.33°** platform error under the documented assumptions;
- Mission Control accepted a **±1°** attitude/alignment tolerance for PC+2;
- the PC+2 Mission Rules review has already occurred;
- the team has selected the Mid-Pacific return option rather than the faster high-ΔV alternatives.

These facts should be scenario setup data or briefing material, not hidden simulation events.

---

## 3. Final PC+2 maneuver PAD — player-visible target data

The final P30 LM maneuver PAD transmitted beginning at **77:55:24 GET** gives:

| Item | Final value |
|---|---:|
| TIG / Noun 33 | **79:27:38.30 GET** |
| LVLH ΔV X | **+833.0 ft/s** |
| LVLH ΔV Y | **-50.9 ft/s** |
| LVLH ΔV Z | **-213.9 ft/s** |
| Resultant ΔV | **861.5 ft/s** |
| Expected perigee | **20.5 nmi** |
| Burn duration on PAD | **4:24** |
| Burn attitude roll | **272°** |
| Burn attitude pitch | **81°** |
| CSM weight | **62,480 lb** |
| LM weight | **33,452 lb** |
| Ullage | **2 jets for 10 s** |
| DPS throttle | **5 s minimum, 21 s at 40%, remainder maximum** |

The associated CSM monitoring PAD gives:

- predicted landing latitude: **21.65° S**;
- predicted landing longitude: **165.00° W**;
- range-to-go at 0.05-g event: **1163.5 nmi**;
- expected velocity at 0.05 g: **36,292 ft/s**;
- predicted 0.05-g GET: **142:39:22**.

These are information products delivered to the crew. They are not themselves the authoritative physical trajectory state.

---

## 4. Guidance target representation — do not collapse coordinate frames

The GUIDO postflight report preserves the PC+2 maneuver in **IMU coordinates**, which differ from the LVLH components read on the maneuver PAD.

### Planned PGNS velocity-to-be-gained

- X: **+743.08 ft/s**
- Y: **-426.42 ft/s**
- Z: **+90.84 ft/s**

### Executed PGNS values

- X: **+742.21 ft/s**
- Y: **-425.88 ft/s**
- Z: **+91.04 ft/s**

### Consequence

The simulation parameter dictionary must distinguish at least:

- maneuver target in LVLH / PAD coordinates;
- PGNS/IMU velocity-to-be-gained components;
- achieved physical velocity change;
- post-burn guidance residuals.

Do not create one generic `delta_v_vector` and use it for all four concepts.

---

## 5. Burn execution validation targets

The Mission Operations Report gives:

| Quantity | Planned | Actual |
|---|---:|---:|
| TIG | 79:27:38.30 | 79:27:38.30 |
| Burn duration | 4:23.69 | **4:23.82** |
| Cutoff | 79:32:01.99 | **79:32:02.12** |
| Total planned ΔV | **861.5 ft/s** | — |

The Flight Director report records a normal burn. The air-ground record shows:

- crew reports 40% thrust immediately after ignition;
- full thrust is reported shortly afterward;
- Mission Control reports the burn looking good at one/two/three-minute checkpoints;
- shutdown occurs at approximately 79:32:05 in the voice transcript, consistent with transmission/reporting delay after the actual guided cutoff;
- no shutdown rule is triggered in the nominal case.

### Validation rule

Use the Mission Operations Report's computed event times for physical/guidance validation. Treat voice timestamps as communication events, not exact engine-state timestamps.

---

## 6. Post-burn guidance validation

After shutdown, Mission Control can read the LGC/DSKY state via telemetry.

The post-burn PGNS residuals are documented as approximately:

- X: **+1.0 ft/s**
- Y: **+0.3 ft/s**
- Z: **0.0 ft/s**

The crew and ground leave these small residuals untrimmed.

The Mission Operations Report also records the PGNS residual display as:

- R1 `+00010`
- R2 `+00003`
- R3 `+00000`

This gives a useful validation bridge between engineering values and a controller/crew-visible computer representation.

---

## 7. PC+2 authoritative parameter dictionary — minimum viable set

The following state is sufficient for the first nominal model. Display formatting is deliberately separate.

### A. Mission / configuration

| Parameter | Class | Initial/nominal state | Why required |
|---|---|---|---|
| `get` | authoritative time | 77:55:00 start | event sequencing |
| `vehicle_configuration` | physical/config | docked CSM+LM+SM | mass/control dynamics |
| `scenario_phase` | simulation control | final PC+2 preparation | procedure/event gating |

### B. Ground trajectory products

| Parameter | Class | Initial/nominal state | Why required |
|---|---|---|---|
| `rtcc_trajectory_solution` | ground-derived | valid/current | FIDO basis |
| `pc2_target_solution` | ground-derived | final solution becoming available | PAD/uplink workflow |
| `landing_target_lat_lon` | ground-derived | 21.65 S / 165.00 W | RETRO return product |
| `predicted_005g_get` | ground-derived | 142:39:22 | return-plan validation |
| `postburn_trajectory_solution` | ground-derived | unavailable until after burn/tracking | FIDO verification |

The first prototype does **not** need an exposed historical RTCC state vector with every Cartesian component simply to represent the controller workflow. A numerical trajectory state becomes mandatory when the physics/trajectory propagator is implemented; at that point it should be sourced from mission trajectory documentation rather than reverse-engineered from the PAD.

### C. PGNS/LGC

| Parameter | Class | Initial/nominal state | Why required |
|---|---|---|---|
| `lgc_operating` | onboard | true | guidance availability |
| `pg_ns_alignment_valid` | onboard/ground assessment | accepted | burn readiness |
| `alignment_error_estimate_deg` | ground assessment | within 1°; prior Sun check ~0.33° | readiness/rule context |
| `state_vector_load_status` | onboard/uplink | final load pending/being verified during prep | GUIDO/uplink workflow |
| `target_load_status` | onboard/uplink | final load pending/being verified | GUIDO/uplink workflow |
| `p40_state` | onboard | not active at start; active by final preburn phase | burn execution |
| `pg_ns_vg_imu_xyz` | onboard | planned +743.08, -426.42, +90.84 ft/s when loaded | guidance target |
| `pg_ns_program_alarm` | onboard | none nominal | shutdown rule |
| `lgc_warning` | onboard | false nominal | shutdown rule |
| `pg_ns_residual_xyz` | onboard | evolves; final +1.0,+0.3,0.0 ft/s | postburn validation |

### D. AGS backup

| Parameter | Class | Initial/nominal state | Why required |
|---|---|---|---|
| `ags_available` | onboard | true | backup/cross-check |
| `ags_mode` | onboard | backup rate-command/rate-damping role | documented burn setup |
| `ags_crosscheck_state` | onboard/ground | acceptable nominal | GUIDO confidence |

Exact MSK 1123 AGS ULL / ACT VEL algorithms are not required by the nominal PC+2 contract unless a later failure case needs them.

### E. DPS / propulsion

| Parameter | Class | Initial/nominal state | Why required |
|---|---|---|---|
| `dps_armed` | physical/control | false at start | preignition sequence |
| `dps_throttle_command` | command | off at start | burn profile |
| `dps_thrust_actual` | physical | zero at start | engine model |
| `dps_chamber_pressure` | measured/physical | nominal | 85-psi ground shutdown rule |
| `dps_inlet_pressure` | measured/physical | nominal | 150-psi ground rule |
| `dps_fuel_oxidizer_delta_p` | measured/physical | nominal, <25 psi | ground-callout-only rule |
| `engine_gimbal_warning` | onboard/telemetry | false | shutdown rule |
| `gda_control_state` | physical/control | nominal | thrust-vector control |
| `descent_regulator_state` | physical/control | nominal sequence | late-burn procedure |

Do not invent nominal pressure values where the current source only gives shutdown thresholds. The nominal run needs values on the safe side of the thresholds; exact baseline pressures require a telemetry source if they become player-visible.

### F. RCS / attitude control

| Parameter | Class | Initial/nominal state | Why required |
|---|---|---|---|
| `rsc_ullage_available` | physical | true | two-jet 10-s ullage |
| `ullage_command` | command | off at start | preignition event |
| `attitude_error_deg_xyz` | physical/onboard | within limits | ±10° rule |
| `body_rate_deg_s_xyz` | physical/measurement | within limits | ±10°/s rule |
| `ces_dc_failure` | physical/telemetry | false | shutdown rule |

### G. Electrical / TELMU-relevant

| Parameter | Class | Initial/nominal state | Why required |
|---|---|---|---|
| `lm_burn_configuration_current_a` | physical/measurement | approximately 38–40 A once powered for burn | readiness/load check |
| `inverter_warning` | electrical/telemetry | false | shutdown rule |
| `lm_power_configuration` | config | low-power at start; burn configuration from ~78:12 | event progression |
| `postburn_powerdown_state` | config | not begun at start | endpoint transition |

Do not build the entire LM consumables model merely to supply this slice. Battery/water/O2 quantities become first-slice parameters only if they alter a live PC+2 decision.

### H. Communications / telemetry

| Parameter | Class | Initial/nominal state | Why required |
|---|---|---|---|
| `air_ground_link_quality` | link | weak at scenario start; improves after power-amplifier change | final PAD/readback workflow |
| `voice_available` | link | true but degraded initially | CAPCOM path |
| `telemetry_available` | link | available after AOS; validity tracked separately | controller data |
| `uplink_available` | link | configuration-dependent | final state-vector/target update |
| `ranging_enabled` | comm/nav | required during preparation | tracking support |
| `data_age` / `validity` | telemetry metadata | per product | preserves stale/invalid distinction |

---

## 8. Required event/state timeline for the nominal run

The initial implementation should support these source-backed milestones:

| GET | State/event |
|---|---|
| 77:55:00 | scenario start; weak communications; final maneuver PAD imminent |
| 77:55:24 | final P30 LM maneuver PAD begins |
| 77:59:17 | stronger link after S-band power-amplifier change |
| ~78:00 | final PAD/readback complete; monitoring PAD follows |
| 78:12 | LM burn-configuration power-up underway; ~38–40 A required |
| 78:21–78:23 | ranging confirmed; uplink/computer activity completes sufficiently for crew computer control to be returned |
| ~79:17 | Flight performs GO/NO-GO poll; team is GO |
| ~79:23 | LM in P40 / final burn program state |
| 79:27:38.30 | physical/guidance ignition target |
| 79:32:02.12 | actual guided cutoff |
| 79:32:41+ | residual review |
| 79:34 onward | power-down transition begins |

The exact second for every internal switch transition does not need to be pre-scripted unless required by a procedure or failure case.

---

## 9. Information-boundary requirements

For each parameter, implementation should preserve separate values where historically meaningful:

```text
true physical value
    ↓
sensor/onboard-computer representation
    ↓
telemetry value + validity + age
    ↓
ground-derived/processed value
    ↓
controller-visible field or indication
```

Examples:

- true DPS chamber pressure is not identical to the ground telemetry value;
- physical attitude is not identical to PGNS attitude knowledge;
- RTCC trajectory state is not identical to the state vector loaded in the LGC;
- final maneuver PAD components are not identical to PGNS IMU-coordinate Vg values;
- actual cutoff time is not identical to the timestamp of the crew's verbal “shutdown” report.

This separation is required even if the nominal first implementation initially assigns zero error between some layers.

---

## 10. Deferred items / stop conditions

The following are explicitly **not blockers** for beginning the PC+2 simulation model:

- exact Cartesian RTCC state vector at 77:55 GET;
- complete MSK 1123/1137 field routing;
- exact normal values for every propulsion pressure above/below the shutdown limit;
- complete LM consumables inventory;
- exact historical CRT used by FIDO for every target product;
- exact AGS ULL / ACT VEL calculation;
- full INCO look-angle display.

Research these only if a first-slice player decision or validation test requires them.

---

## 11. Next work

1. Convert this research dictionary into an implementation-oriented parameter specification with stable project names, units, ownership, update behavior, validity metadata, and provenance fields.
2. Define the nominal event/state transition model from 77:55 through 79:34.
3. Identify the smallest player-facing display/product set needed to expose these parameters to GUIDO, CONTROL, FIDO/RETRO, TELMU, INCO, FLIGHT, and CAPCOM.
4. Use the historical run as the first deterministic validation fixture before authoring any nonnominal failure case.

---

## Primary sources

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, especially Flight Director's Report, RETRO appendix, and GUIDO appendix.  
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- Apollo 13 Technical Air-to-Ground Voice Transcription, preserved through the Apollo 13 Flight Journal document collection.  
  https://apollojournals.org/afj/ap13fj/a13-documents.html

## Transcript navigation / cross-check

- Apollo 13 Flight Journal, Day 4 Part 2, *Leaving the Moon*, used to navigate the underlying air-ground chronology and cross-check final PAD/readback and burn events.  
  https://www.apollojournals.org/afj/ap13fj/13day4-leaving-moon.html

The Flight Journal commentary is not used to override conflicting primary mission documentation.