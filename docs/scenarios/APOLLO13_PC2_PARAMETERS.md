# Apollo 13 PC+2 Parameter Specification

Status: **implementation-oriented research specification — nominal vertical slice**  
Scenario start: **77:55:00 GET**  
Research basis: `resources/research/050_pc2_initialization_and_nominal_validation.md`, with later refinements in notes 051–055.

## Purpose

This file defines stable project-level parameter names for the first Apollo 13 PC+2 implementation. It is not a historical display transcript. Historical CRT fields are mapped onto these parameters separately.

Each parameter must preserve its information layer. A physical value, onboard estimate, telemetry sample, RTCC product, and controller display are not interchangeable simply because they use the same units.

## Common metadata

Every time-varying value exposed outside its owning subsystem should support, where applicable:

- `value`
- `units`
- `sample_time_get`
- `receive_time_get`
- `validity` (`valid`, `stale`, `invalid`, `unavailable`)
- `source_layer`
- `provenance`

The nominal first pass may use zero transport error, but the fields should not be structurally collapsed.

## Mission and scenario

| Project name | Type | Units | Initial state | Owner |
|---|---|---|---|---|
| `mission.get_s` | float | s | 285300.0 (77:55:00) | mission clock |
| `mission.phase` | enum | — | `pc2_final_prep` | scenario |
| `vehicle.stack_config` | enum | — | `csm_lm_sm_docked` | vehicle |
| `scenario.pc2.tig_get_s` | float | s | 286058.30 | scenario/target |

## Ground trajectory / return products

| Project name | Type | Units | Nominal value/state | Primary user |
|---|---|---|---|---|
| `ground.rtcc.solution_valid` | bool | — | true | FIDO |
| `ground.pc2.target_status` | enum | — | `final_being_delivered` at start | FIDO/GUIDO |
| `ground.pc2.pad_dv_lvlh_x` | float | ft/s | +833.0 | FIDO/GUIDO/CAPCOM |
| `ground.pc2.pad_dv_lvlh_y` | float | ft/s | -50.9 | FIDO/GUIDO/CAPCOM |
| `ground.pc2.pad_dv_lvlh_z` | float | ft/s | -213.9 | FIDO/GUIDO/CAPCOM |
| `ground.pc2.pad_dv_resultant` | float | ft/s | 861.5 | FIDO/RETRO |
| `ground.pc2.pad_burn_duration_s` | float | s | 264 nominal PAD display | FIDO/CAPCOM |
| `ground.pc2.expected_perigee_nmi` | float | nmi | 20.5 | FIDO/RETRO |
| `ground.return.landing_lat_deg` | float | deg | -21.65 | RETRO |
| `ground.return.landing_lon_deg` | float | deg | -165.00 | RETRO |
| `ground.return.range_to_go_005g_nmi` | float | nmi | 1163.5 | RETRO/CAPCOM |
| `ground.return.velocity_005g_fps` | float | ft/s | 36292 | RETRO/CAPCOM |
| `ground.return.get_005g_s` | float | s | 513562 (142:39:22) | RETRO/CAPCOM |
| `ground.postburn.solution_status` | enum | — | `not_available` until tracking | FIDO |

`ground.pc2.*pad_dv_lvlh_*` must remain separate from PGNS IMU-coordinate Vg.

## PGNS / LGC

| Project name | Type | Units | Nominal / initial state | Primary user |
|---|---|---|---|---|
| `pg_ns.lgc.operating` | bool | — | true | GUIDO |
| `pg_ns.lgc.program` | int/enum | — | preburn state; transitions to P40 | GUIDO |
| `pg_ns.lgc.program_alarm` | optional code | — | none | GUIDO |
| `pg_ns.iss.warning` | bool | — | false | GUIDO |
| `pg_ns.lgc.warning` | bool | — | false | GUIDO |
| `pg_ns.alignment.accepted` | bool | — | true | GUIDO/FLIGHT |
| `pg_ns.alignment.error_estimate_deg` | float | deg | prior Sun check ~0.33; accepted <1 | GUIDO |
| `pg_ns.state_vector_load_status` | enum | — | `pending_final_verification` | GUIDO |
| `pg_ns.target_load_status` | enum | — | `pending_final_verification` | GUIDO |
| `pg_ns.vg_imu_x` | float | ft/s | +743.08 planned | GUIDO |
| `pg_ns.vg_imu_y` | float | ft/s | -426.42 planned | GUIDO |
| `pg_ns.vg_imu_z` | float | ft/s | +90.84 planned | GUIDO |
| `pg_ns.dv_gained` | float | ft/s | 0 at preburn; evolves during P40 | GUIDO |
| `pg_ns.vg_remaining` | vector | ft/s | derived onboard | GUIDO |
| `pg_ns.residual_x` | float | ft/s | nominal final +1.0 | GUIDO |
| `pg_ns.residual_y` | float | ft/s | nominal final +0.3 | GUIDO |
| `pg_ns.residual_z` | float | ft/s | nominal final 0.0 | GUIDO |

Historical nominal executed Vg values for validation are +742.21, -425.88, +91.04 ft/s in the GUIDO report.

`pg_ns.iss.warning` is source-backed as a distinct onboard warning signal with an instrumentation path. The project does **not** yet claim the exact Apollo 13 LM-7 telemetry word or GUIDO CRT field. The PC+2 shutdown criterion is conjunctive: ISS warning **plus** computer program alarm. See research note 054.

## AGS

| Project name | Type | Units | Nominal state | Primary user |
|---|---|---|---|---|
| `ags.available` | bool | — | true | GUIDO |
| `ags.backup_mode` | enum | — | rate-command/rate-damping backup role | GUIDO/CONTROL |
| `ags.crosscheck_acceptable` | bool | — | true | GUIDO |

Do not add a fabricated exact `ags.ullage_display` or `ags.act_vel` mapping until a PC+2 requirement demands it or stronger routing evidence is found.

## DPS / propulsion

| Project name | Type | Units | Nominal state | Primary user |
|---|---|---|---|---|
| `dps.arm_state` | enum | — | `safe` at start | CONTROL |
| `dps.engine_running` | bool | — | false | CONTROL |
| `dps.throttle_command_pct` | float | % | 0; profile minimum → 40 → max | CONTROL |
| `dps.thrust_actual` | float | lbf | 0 preburn; modeled during burn | CONTROL |
| `dps.chamber_pressure` | optional float | psi | exact nominal PC+2 value intentionally unfrozen; when modeled, measurement identity is LM-7-family `GQ6510P` | CONTROL |
| `dps.inlet_pressure` | float | psi | safe nominal condition; exact baseline TBD | CONTROL |
| `dps.fuel_oxidizer_delta_p` | float | psi | <25 nominal condition; exact baseline TBD | CONTROL |
| `dps.engine_gimbal_warning` | bool | — | false | CONTROL |
| `dps.gda_state` | enum | — | nominal | CONTROL |
| `dps.regulator_1_state` | enum | — | nominal pre-cutoff sequence | CONTROL |
| `dps.guided_cutoff_get_s` | optional float | s | validation target 286322.12 | GUIDO/CONTROL |

Rule thresholds are separate configuration data:

- ground chamber-pressure shutdown threshold: approximately 85 psi;
- onboard thrust criterion: approximately 77% thrust;
- ground inlet-pressure threshold: approximately 150 psi;
- onboard inlet-pressure threshold: approximately 160 psi;
- fuel/oxidizer differential-pressure threshold: >25 psi, ground callout.

### Chamber-pressure observation path

Research note 055 establishes `GQ6510P` as the LM-7-family thrust-chamber-pressure measurement. This is sufficient to model an optional chamber-pressure observation reaching CONTROL and to evaluate the documented ground shutdown criterion when a numerical measurement is explicitly supplied.

Important limits remain:

- the nominal fixture still does **not** invent a PC+2 chamber-pressure trace;
- `None` means the project has not supplied a numerical model value, not that historical telemetry is unavailable;
- the exact Apollo 13 PCM/ground-conversion path and exact MSK 1137 `TCP` routing/update cadence remain unresolved;
- the separate onboard 77-percent-thrust observation remains a distinct deferred path.

For a modeled valid CONTROL observation, `dps.chamber_pressure <= 85 psi` triggers the ground chamber-pressure rule audit. The audit does not directly shut down the engine or issue a controller decision.

Do not invent exact nominal pressure readings solely from shutdown thresholds.

## RCS and vehicle attitude

| Project name | Type | Units | Nominal state | Primary user |
|---|---|---|---|---|
| `rcs.ullage_available` | bool | — | true | CONTROL |
| `rcs.ullage_active` | bool | — | false preburn | CONTROL |
| `rcs.ullage_jets_count` | int | — | 2 when commanded | CONTROL |
| `rcs.ullage_duration_s` | float | s | 10 | CONTROL |
| `vehicle.attitude_error_xyz` | vector | deg | within shutdown limits; exact values TBD | CONTROL/GUIDO |
| `vehicle.body_rate_xyz` | vector | deg/s | within shutdown limits; exact values TBD | CONTROL |
| `ces.dc_failure` | bool | — | false | CONTROL |

The sources agree on approximately ±10° attitude error and ±10°/s rate limits but conflict on which wording receives the startup-transient exception. The implementation preserves that conflict rather than choosing one interpretation.

## Electrical / LM burn configuration

| Project name | Type | Units | Nominal state | Primary user |
|---|---|---|---|---|
| `lm.power.mode` | enum | — | low-power at start; transitions to burn configuration | TELMU |
| `lm.power.current_a` | float | A | about 38–40 A in burn configuration | TELMU |
| `lm.inverter_warning` | bool | — | false | TELMU/CONTROL |
| `lm.powerdown.status` | enum | — | `not_started` at start | TELMU |

Full water/O2/thermal inventories are deferred unless they affect a live decision in this interval.

## Communications / data path

| Project name | Type | Units | Initial state | Primary user |
|---|---|---|---|---|
| `comm.air_ground_available` | bool | — | true | INCO/CAPCOM |
| `comm.air_ground_quality` | enum/float | — | weak at 77:55; improves after S-band power-amplifier change | INCO |
| `comm.voice_available` | bool | — | true | CAPCOM |
| `comm.telemetry_available` | bool | — | true after AOS | INCO/all stations |
| `comm.uplink_available` | bool | — | configuration-dependent | INCO/GUIDO |
| `comm.ranging_enabled` | bool | — | required during final prep | INCO/FIDO |
| `comm.sband_power_amp_high` | bool | — | false at start; changed during final PAD readback | INCO/crew |

Telemetry-facing products should carry validity and age independently of physical subsystem health.

## Crew-report events

Crew voice is a distinct source channel. At minimum the event model supports PAD readback, burn-rule readback, ignition/throttle reports, shutdown report, post-burn residual report, and requests for power-down instructions. These are not direct truth-state notifications.

## Nominal validation fixture

A deterministic nominal run should reproduce:

| Validation target | Historical value |
|---|---:|
| physical/guidance TIG | 79:27:38.30 GET |
| planned burn duration | 263.69 s |
| actual burn duration | 263.82 s |
| planned cutoff | 79:32:01.99 GET |
| actual cutoff | 79:32:02.12 GET |
| target resultant ΔV | 861.5 ft/s |
| executed PGNS Vg X | +742.21 ft/s |
| executed PGNS Vg Y | -425.88 ft/s |
| executed PGNS Vg Z | +91.04 ft/s |
| final residual X | +1.0 ft/s |
| final residual Y | +0.3 ft/s |
| final residual Z | 0.0 ft/s |
| shutdown-rule triggers | none |
| post-burn transition | power-down begins immediately after verification |

## Deferred numeric/state detail

The exact RTCC Cartesian state vector at 77:55 GET remains intentionally unfrozen until the propagator requires it. The exact nominal PC+2 chamber-pressure trace, exact LM-7 chamber-pressure ground/display routing, exact LM-7 ISS-warning telemetry-word assignment, and exact GUIDO CRT placement also remain deferred rather than being reverse-engineered.

## Sources

Principal authority remains the NASA Flight Control Division *Mission Operations Report — Apollo 13* (28 April 1970), with technical air-ground transcription for communication chronology. See research notes 050–055 and `resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md` for implementation-specific provenance.
