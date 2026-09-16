# Roadmap — PC+2 GDA trim next targets

Date: 2026-09-16

Research Notes 180–190 separate commanded trim, powered-flight control behavior, maneuver outcome, measured actuator state, generic GDA mechanical calibration, LM-7-specific telemetry-channel semantics, the physical actuator-position feedback signal path, later-LM engineering-unit presentation, the post-free-return PC+2 GDA instruction, the upstream mass-properties processor contract, and the distinction between preflight LM-7 engineering mass-property data and the current official operational set.

Note 188 classifies the later `5.85 / 6.74` pair as a ground-issued desired/reference pair with a no-action disposition. Note 189 establishes the generic processor contract `configuration + consumables -> mass-properties / weight-c.g. product -> RTACF/RTCC trajectory processor -> pitch/yaw trim`, while retaining the missing Apollo 13-specific consumption edge.

Note 190 identifies a mission-specific preflight LM-7 source family. The 17 March 1970 LM-7 DPS weight-characteristics table gives a `33,872.3 lbm` LM separation weight and component weights, but explicitly says those mass properties were for that analysis and directs users to Volume III of the Spacecraft Operational Data Book for **current official mass-properties data**. Those values therefore must not be substituted for CONTROL's undocumented ~59 GET premission inputs.

## Priority 1 — mission-specific ground-computation lineage

Recover an Apollo 13 artifact that bridges:

`T+55 LM-burn mass-properties deck -> weight/c.g. product -> specific RTCC/RTACF request/run -> trim output -> 5.86 / 6.75`

Best targets: weight/c.g. sheet, RTCC/RTACF request/output, job/run record, controller working paper, or support-room product. The generic processor edge is source-backed; the missing evidence is the mission-specific consumption edge.

## Priority 2 — CONTROL premission source and disagreement details

Recover the **Volume III Spacecraft Operational Data Book — Mass Properties** set/revision applicable to Apollo 13/LM-7, especially current official preflight docked CSM/LM weight/c.g. tables. Then seek evidence identifying which premission set CONTROL actually used.

Recover CONTROL's competing numerical trim and the actual comparison/acceptance basis. Do not substitute the recovered Volume II LM-7 DPS-analysis values for CONTROL's inputs: that source explicitly points to Volume III for current official mass properties. Do not assume `premission` denotes a single immutable dataset.

Do not apply the T+25 `0.01°` no-update comparison, the later `~0.3°` spacecraft-checkout statement, the `0.01°` per-axis difference between `5.86 / 6.75` and `5.85 / 6.74`, or the Mission Report's `+0.3 ft/s` post-trim velocity residual to this decision without direct evidence.

## Priority 3 — LM-7 telemetry calibration / trim representation

The 61:29 postflight actuator state is documented in Table 6.4-I: initial pitch/roll `-0.02/-0.34 in`; maximum excursion `+0.31/-0.27 in`; steady-state `+0.04/-0.51 in`; cutoff `+0.10/-0.31 in`.

`LED-267-37C` identifies `GH1313V` as Pitch GDA position and `GH1314V` as Roll GDA position, with axis-specific RET/EXT notation. The LM Operations Handbook independently shows actuator-position feedback returning from the GDA into the DECA. A later LM-10-and-subsequent Instrumentation Packet lists the same channel family over `-6..+6 DEG`; this is continuity evidence, not an asserted LM-7 calibration.

Next seek LM-7 instrumentation/calibration or PCM material mapping GH1313V/GH1314V to engineering degrees and establishing polarity, plus the primary definition of the crew-facing GDA trim-number reference/zero.

## Priority 4 — executed propulsion profile

Use the Apollo 13 Mission Report execution baseline: approximately 34.3-second firing; minimum throttle about 12% for the first 5 seconds, then approximately 37%. Preserve nominal preburn `10% / 40%` values separately as planned/commanded procedure.

## Modeling rule meanwhile

Represent mass-property source state with `mission_specific`, `preflight_or_realtime`, `authority/currentness`, `configuration_scope`, `reference_epoch`, and `controller_selected_source`. For Apollo 13, T+55 may populate the upstream deck state but must not automatically set `run_consumed` or provenance-to-trim true. CONTROL's source remains `premission mass properties` with exact dataset and values unresolved.

Use `5.86 / 6.75` only as a sourced commanded/preburn trim reference for the ~59/61:29 chain. Use `5.85 / 6.74` as the later ground-issued PC+2 reference with `okay as it is` disposition. Use the four Mission Report GDA inch values for actual 61:29 actuator state at their source resolution. Do not infer LM-7 telemetry degrees, crew-facing trim zero/reference, or CONTROL's numerical alternative.