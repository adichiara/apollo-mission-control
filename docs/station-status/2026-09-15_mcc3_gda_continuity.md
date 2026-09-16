# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/190_lm7_premission_mass_properties_source_boundary.md`

## CONTROL

**Improved; exact input set unresolved.** The Flight Dynamics primary account establishes that LM CONTROL challenged the ~59 GET PC+2 DPS trim because CONTROL used **premission mass properties**; CONTROL later agreed with Flight Dynamics' data. Primary voice identifies the passed/commanded pair as pitch `5.86°`, roll `6.75°` and shows CONTROL accepting the preburn gimbal checkout as `within about 0.3` / `plenty close`.

Note 190 identifies a mission-specific preflight LM-7 engineering mass-properties source family. A 17 March 1970 LM-7 DPS weight-characteristics table contains a preflight LM separation weight of `33,872.3 lbm` and component weights, but explicitly says those values were for that analysis and refers users to Volume III of the Spacecraft Operational Data Book for **current official mass-properties data**. Therefore these recovered values are not assigned to CONTROL's ~59 GET calculation.

CONTROL's exact premission source/revision, alternative numerical trim, exact mass-properties inputs, ground-computation comparison delta/acceptance rule, and direct T+55 run lineage remain unrecovered.

## FLIGHT / CAPCOM

**Improved.** Primary voice at ~59 GET identifies `5.86 / 6.75` as a provisional PC+2 DPS trim/GDA pair and says the angles `will be updated`. At 60:53–60:56 GET CAPCOM passes the same pair on the 61:29 free-return DPS pad. FLIGHT explicitly queries CONTROL about preburn trim closeness and accepts CONTROL's checkout disposition.

The later PC+2 P30 pad carries pitch `5.85`, roll `6.74`, with CAPCOM saying the GDA `ought to be okay as it is from the last burn`. Treat this as a ground-issued reference plus no-action disposition, not telemetry or a demonstrated recomputation.

## GUIDANCE

**Boundary retained.** The immediate post-61:29 `0.2` trim exchange remains unclassified as a GDA quantity absent explicit primary evidence.

## Flight Dynamics / RTCC / RTACF

**Improved; mission-specific consumption edge unresolved.** Apollo 13 documentation distinguishes T-6 mass properties generated/loaded in RTCC, a T+25 RTCC mass-properties run with pitch/yaw trim evaluation, and later RTCC LM-burn mass-property decks updated to T+55. Contemporary primary RTACF documentation establishes the generic processor contract from configuration/consumables through mass-properties/weight-c.g. products to RTACF/RTCC pitch/yaw trim computation.

Note 190 adds an important source-authority distinction: mission-specific preflight LM-7 engineering mass-property tables existed, but at least one such table explicitly deferred to Volume III for the **current official** mass-properties data. `Premission mass properties` must therefore remain a source-state class rather than being mapped to the first recovered LM-7 preflight table.

Still unresolved: T+55 weight/c.g./deck contents, generation/load event, downstream Apollo 13 run/request/output, CONTROL's exact premission source and competing numerical values, PC+2 ground-computation acceptance criterion, RTCC/RTACF job identity, and direct T+55-to-`5.86 / 6.75` lineage.

## Simulator constraint

Represent `reference_epoch`, `processing_domain`, `generated`, `loaded`, `deck_updated/reference_set_selected`, and `run_consumed` separately. For mass-property inputs also track `mission_specific`, `preflight_or_realtime`, `authority/currentness`, `configuration_scope`, and `controller_selected_source`. Do not equate `premission` with `current official Volume III` unless the controller source is recovered.

Also separate `computed_trim`, `ground_issued_reference`, `commanded_trim`, `preburn_checkout_observed_delta`, `checkout_acceptance`, `powered_flight_compliance`, `postburn_actuator_state`, and `no_action_disposition`.