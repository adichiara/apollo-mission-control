# Research Resources

This directory is the provenance layer for the simulation.

## Structure

- `PRIMARY_SOURCE_CATALOG.md` — master index of identified source documents.
- `source-catalog/` — small implementation/scenario-specific catalog supplements that are part of the active source index and should be folded into the master catalog during comprehensive catalog maintenance.
- `research/` — project research notes derived from sources.
- `audits/` — dated verification reports and file-by-file evidence ledgers.
- `primary-sources/` — reserved for local copies of primary documents when the project decides that mirroring is appropriate and legally/permanently practical.

Current supplements:

- `source-catalog/PC2_IMPLEMENTATION_SOURCES.md` — sources used directly by the Apollo 13 PC+2 executable product-projection, shutdown-rule, and scenario-injection layers.
- `source-catalog/PC2_INLET_PRESSURE_SOURCES.md` — focused source record for the unresolved Apollo 13 150-psi ground inlet-pressure mapping; note 106 identifies fuel inlet / `GQ3611P` as the leading lineage-supported candidate without treating it as proven for Apollo 13.
- `source-catalog/PC2_INVERTER_WARNING_SOURCES.md` — focused source record for the mission-specific inverter-2 starting configuration, inverter-caution path, exact alternate-inverter transfer procedure, fresh-valid-reobservation timing boundary, source-backed ground electrical-observation path through `GC0155`/`GC0071`, note-117 direct caution/selector telemetry boundary, and note-118 MCC dynamic display-request/channel-attach boundary; no unsupported numeric dwell, direct ground caution discrete, selector telemetry, fixed TV-channel assignment, or exact Apollo 13 controller display format is assumed.
- `source-catalog/PC2_INVERTER_TELEMETRY_PRESENTATION_SOURCES.md` — focused source record for inverter-bus voltage/frequency telemetry presentation, including LM-1 ground-display continuity, AS-508 format architecture, Apollo 15 TELMU indicator continuity, later-LM sample/MSK continuity, and Apollo 13's mission-specific onboard Power/Temp Monitor comparison; exact AS-508 TELMU loading/cadence remains unresolved.
- `source-catalog/PC2_THRUST_MONITOR_SOURCES.md` — focused source record for the onboard 77-percent thrust-monitor criterion; note 107 identifies the LM panel-1 CMD THRUST / ENG THRUST instrument family and ENG THRUST actual-thrust scale, while note 108 bounds first-playable applicability to entry into the commanded full/max-throttle segment at burn +26 seconds, explicitly as a lineage-based inference rather than a verbatim recovered Apollo 13 qualifier.
- `source-catalog/PC2_ATTITUDE_SOURCES.md` — focused source record for PC+2 attitude-error/rate criteria; note 109 resolves the prior wording conflict for operational first-playable use by giving precedence to the contemporaneous CAPCOM transmission and crew readback, which attach the startup-transient exception to attitude error. Note 110 adds cross-mission DPS engineering evidence showing that “start transient” was a short engine-start phenomenon, while preserving the absence of an Apollo 13 operational duration/end condition and prohibiting a guessed numeric gate.
- `source-catalog/PC2_FRESHNESS_SOURCES.md` — focused source record for observation age, data validity, and the unresolved absence of a PC+2-specific stale-data threshold.
- `source-catalog/PC2_RESTART_SOURCES.md` — mission-specific sources for the premature DPS shutdown/restart branch and the distinction between rule-caused shutdown and restart-eligible unexplained shutdown.
- `source-catalog/PC2_DPS_RESTART_RESPONSE_SOURCES.md` — mission-specific and contemporary sources for separating an eligible restart procedure from the successful physical engine-on response.
- `source-catalog/PC2_DELTA_P_CALLOUT_SOURCES.md` — mission-specific sources for the ground-only fuel/oxidizer ΔP >25 psi shutdown callout, first playable CONTROL→CAPCOM integration boundary, and explicit unresolved-routing limits.
- `source-catalog/PC2_DPS_SHUTDOWN_RESPONSE_SOURCES.md` — contemporary LM sources for crew STOP-pushbutton control, engine-off command routing, and DPS valve-response semantics.
- `source-catalog/PC2_DPS_SHUTDOWN_CONFIRMATION_SOURCES.md` — mission-specific and contemporary evidence for crew voice shutdown report plus fresh GQ6510P chamber-pressure observation as distinct response-evidence channels, without an invented engine-off threshold.
- `source-catalog/PC2_CREW_RESPONSE_SOURCES.md` — primary-source supplement for CAPCOM ground-call receipt, explicit crew shutdown command, physical DPS response separation, and its HTTP validation exposure.
- `source-catalog/PC2_CREW_ACTION_REPRESENTATION_SOURCES.md` — primary Apollo 13/LM procedure evidence constraining the first-playable crew layer to explicit scenario-authored receipt/action steps rather than a separate player, automatic compliance, or random crew-error mechanics.
- `source-catalog/PC2_CONTROL_PRESENTATION_SOURCES.md` — mission-specific Apollo 13 MSK 1123/1137 and PC+2 operational sources constraining the first player-facing CONTROL rendering.
- `source-catalog/PC2_GUIDO_PRESENTATION_SOURCES.md` — mission-specific Apollo 13 MSK 1123/1137, LUMINARY 1C R-567, and PC+2 operational sources constraining the first player-facing GUIDO rendering.
- `source-catalog/PC2_TELMU_PRESENTATION_SOURCES.md` — mission-specific PC+2 chronology, TELMU post-mission, Review Board, inverter-rule/instrumentation, and MCC display-architecture sources constraining the first player-facing TELMU rendering; inverter voltage/frequency may be project-rendered from source-backed telemetry, but no fixed historical TV channel or exact Apollo 13 inverter display format is claimed.
- `source-catalog/PC2_FIDO_RETRO_PRESENTATION_SOURCES.md` — final PC+2 maneuver/monitor PAD plus mission-specific FIDO/RETRO sources constraining the first target/return player rendering.
- `source-catalog/PC2_INCO_PRESENTATION_SOURCES.md` — mission-specific communications and ranging evidence constraining the first player-facing INCO rendering.
- `source-catalog/PC2_FLIGHT_CAPCOM_PRESENTATION_SOURCES.md` — mission-specific Flight Director and air-ground communication sources constraining the first FLIGHT and CAPCOM renderings.
- `source-catalog/PC2_SESSION_INTEGRATION_SOURCES.md` — historical/state-machine sources governing the first authoritative playable-session orchestration layer.
- `source-catalog/PC2_FINAL_LOAD_UPLINK_SOURCES.md` — mission-specific primary evidence for the staged final PC+2 state-vector/target-load/uplink workflow across Flight Dynamics, GUIDO, INCO, CAPCOM/crew, and FLIGHT, with exact vector and ground-command internals explicitly deferred.
- `source-catalog/PC2_POSTBURN_SOURCES.md` — primary Apollo 13 evidence for the immediate post-PC+2 maneuver assessment, initial LM power-down, retained communications/guidance functions, and PTC-preparation boundary.
- `source-catalog/PC2_SPACECRAFT_MODEL_SCOPE_SOURCES.md` — primary Apollo/NASA LM subsystem sources constraining the amount of spacecraft physics required by the first playable and supporting the decision-relevant causal-fidelity rule.
- `source-catalog/PC2_GROUND_DATA_PROCESSING_SOURCES.md` — Apollo 13 Review Board and March 1970 MCC/MSFN sources constraining MSFN/CCATS/RTCC behavior to decision-relevant tracking, telemetry, trajectory, display, and command/load services rather than full ground-computer emulation.
- `source-catalog/PC2_OBSERVATION_FAILURE_SOURCES.md` — primary LM instrumentation, communications, Apollo 13 ground-processing, and mission evidence constraining first-playable observation failures to explicit layered, scenario-authored faults rather than random telemetry failure.
- `source-catalog/PC2_BACKROOM_SUPPORT_SOURCES.md` — Apollo 13 primary evidence for Staff Support Room/backroom functions and the first-playable rule that omits separate backroom players without pretending the historical support structure did not exist.
- `source-catalog/WEB_TRANSPORT_SOURCES.md` — current Render/FastAPI platform documentation supporting the first phone-accessible transport and deployment shell.
- `source-catalog/FACILITATOR_AUTHORITY_SOURCES.md` — primary NASA simulation-control sources plus current Render secret-management sources supporting the facilitator/controller authority boundary.
- `source-catalog/INTEGRATED_SIMULATION_VALIDATION_SOURCES.md` — primary NASA simulation-training sources supporting integrated multi-station validation with a distinct simulation-control function, without treating HTTP/browser mechanics as historical.
- `source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md` — primary Apollo/NASA simulation-training, mission-rule, and procedure-development sources constraining the real-device/human-play protocol, scenario-blind player preparation/reference packet, structured evidence/debrief package, and separation of mission-like rehearsal from modern browser/mobile usability testing.
- `source-catalog/PC2_LOW_PLAYER_COUNT_SOURCES.md` — Apollo organizational/staffing and PC+2 communications evidence constraining five-player compact play, original-station preservation, and the decision not to approve a sub-five-player PC+2 mode at the current fidelity target.
- `source-catalog/APOLLO13_GROUND_PRODUCT_INTEGRITY_SOURCES.md` — mission-specific sources for the post-MCC-5 RTCC/AGS body-angle processing error and the distinction between product availability/validity and hidden data integrity.

Latest scenario-integration research:

- `research/098_pc2_final_state_vector_target_load_uplink.md` — resolves the first-playable final-load workflow into a source-backed staged FIDO/GUIDO/INCO/CAPCOM/crew/FLIGHT process while leaving exact vector contents, RTCC/CCATS internals, controller keying, and transmission duration unfrozen.
- `research/099_pc2_final_load_staged_implementation.md` — carries note 098 into executable solution/load/uplink states and station-scoped products while preserving the same explicit evidence limits.
- `research/100_pc2_backroom_staff_support_boundary.md` — documents Apollo 13 SSR support and resolves the current first-playable boundary: backrooms remain acknowledged but non-playable until a scenario exposes a concrete support-product dependency.
- `research/101_pc2_immediate_postburn_verification_powerdown.md` — establishes the source-backed immediate post-PC+2 sequence through maneuver assessment, initial LM power-down, and PTC preparation without inventing console keying or full PTC dynamics.
- `research/102_pc2_spacecraft_physical_model_scope.md` — resolves how much spacecraft physics the first playable needs: causal DPS, guidance/control, electrical availability, communications, and observation-integrity state only where a sourced player decision or selected failure mechanism depends on it.
- `research/103_pc2_ground_data_processing_scope.md` — resolves how much MSFN/CCATS/RTCC behavior the first playable needs: functional tracking/telemetry/trajectory/display/load services and data-quality consequences only where a sourced player decision depends on them; internal ground-computer emulation remains deferred.
- `research/104_pc2_sensor_telemetry_failure_scope.md` — resolves first-playable sensor/telemetry failure scope: no additional nominal historical instrumentation fault is added, while unavailable, stale/delayed, biased/shifted, warning-only, communications-path, and ground-product faults remain explicit scenario capabilities only when sourced or labeled synthetic.
- `research/105_pc2_crew_action_representation_boundary.md` — resolves first-playable crew representation: no separate crew player; CAPCOM communication, crew receipt/action, spacecraft response, telemetry, and crew report remain explicit stages, with no invented random crew delay/error mechanics.
- `research/106_pc2_inlet_pressure_rule_lineage.md` — follows the Apollo 13 “LOI Mode I abort” rule lineage into surviving Apollo 10/11 mission rules; identifies fuel inlet / `GQ3611P` as the leading candidate behind the 150-psi ground criterion while preserving the lack of an Apollo 13-specific exact mapping and leaving the executable rule `NOT_EVALUABLE`.
- `research/107_pc2_onboard_thrust_indicator_identification.md` — identifies the LM panel-1 CMD THRUST / ENG THRUST instrument family behind the Apollo 13 onboard percent-thrust rule with high confidence, identifies ENG THRUST as the actual-engine-thrust percent scale, and narrows the remaining gap to the startup applicability gate.
- `research/108_pc2_thrust_rule_applicability_gate.md` — resolves that bounded first-playable gate: commanded low-thrust startup is exempt and the 77-percent criterion becomes applicable on entry to maximum/full throttle; the Apollo 13 crew debrief fixes that nominal transition at burn +26 seconds. The gate is explicitly recorded as a source-bounded lineage inference, not a verbatim recovered Apollo 13 rule qualifier, and does not synthesize a crew gauge from hidden state.
- `research/109_pc2_attitude_start_transient_scope.md` — resolves the operational allocation of the PC+2 attitude startup exception: the real-time CAPCOM transmission and Haise readback attach it to attitude error, not rate. The conflicting later postflight wording is retained, and the exact transient duration remains deliberately unresolved.
- `research/110_pc2_attitude_start_transient_duration_boundary.md` — bounds the remaining duration question: Apollo DPS engineering records show “start transient” is a short engine-start phenomenon measured in seconds, but no reviewed Apollo 13 operational source defines the PC+2 exception’s exact duration/end condition. Cross-mission 2.14-second/4.0-second values are not promoted into historical executable behavior.
- `research/111_pc2_inverter_switch_identity.md` — records the earlier generic LM inverter-convention synthesis; superseded in part by mission-specific evidence in notes 112–122.
- `research/112_pc2_inverter_selection_correction.md` — establishes from the mission-specific PC+2 read-up that inverter 2, not the generic inverter-1 burn convention, was retained for this maneuver.
- `research/113_pc2_inverter_alternate_identity.md` — resolves the alternate source as inverter 1 from the mission-specific starting state plus the two-inverter LM architecture.
- `research/114_pc2_inverter_transfer_procedure.md` — recovers the exact Apollo 13 malfunction-procedure transfer sequence: close inverter-1 feeder breaker, select inverter 1, open inverter-2 feeder breaker, then re-observe the INVERTER caution.
- `research/115_pc2_inverter_reobservation_timing_boundary.md` — resolves first-playable post-transfer timing semantics: the mission procedure supplies no numeric crew dwell, while LM-5-and-subsequent instrumentation design handles normal selection transient through caution/inhibit logic; evaluate a fresh valid caution state rather than inventing a timer.
- `research/116_pc2_inverter_ground_observation_path.md` — resolves the underlying ground electrical-observation provenance: inverter-bus frequency `GC0155` and voltage `GC0071` are routed to PCMTEA/MSFN, while the onboard derived `GL4046`/`6DS26` caution remains separate. Exact controller routing/CRT presentation, latency, and inhibit duration remain unresolved.
- `research/117_pc2_inverter_direct_caution_selector_telemetry_boundary.md` — bounds the next direct-telemetry question: the reviewed primary inverter schematics explicitly label PCMTEA taps for `GC0155`/`GC0071` but do not establish direct telemetry of the derived `GL4046` caution or INV1/INV2 selector position. First playable therefore keeps caution persistence and selector identity on the crew action/report path unless stronger primary routing evidence is recovered.
- `research/118_pc2_inverter_mcc_display_routing_boundary.md` — resolves the fixed-channel architectural ambiguity using NASA MCC display-system documentation: computer-driven TV formats were dynamically requested/assigned or attached rather than permanently bound to one station/channel. Exact Apollo 13 inverter format identity, field placement, controller selection state, MSK/DRK action, cadence, and latency remain unresolved.
- `research/119_pc2_inverter_telemetry_sample_display_continuity.md` — documents later-LM format-dependent sampling and MSK routing for `GC0071V`/`GC0155F` while explicitly refusing to import LM-10 rates or destinations into Apollo 13.
- `research/120_pc2_inverter_as508_format30_boundary.md` — uses the mission-specific AS-508 MCC/MSFN configuration to separate normal LM telemetry from High Speed Format 30 post-pass playback; Format-30 10/50-sample/s analog slots are not treated as live PC+2 station cadence.
- `research/121_pc2_inverter_telmu_indicator_continuity_boundary.md` — adds pre-/post-Apollo-13 primary continuity evidence that both inverter measurements were ground-display products and were explicitly presented on TELMU operational indicators by Apollo 15, strengthening station-family ownership without importing the later panel layout into AS-508.
- `research/122_pc2_inverter_onboard_ground_monitoring_boundary.md` — adds mission-specific Apollo 13 transcript evidence that the PC+2 activation read-up explicitly used the onboard Power/Temp Monitor to compare inverter 2 then inverter 1 and that caution/warning versus telemetry availability were separately managed; crew-local and ground TELMU evidence remain distinct parallel paths.

Earlier notes 081–097 remain the authoritative history for continuous-clock architecture, shutdown/crew/evidence integration, facilitator/client separation, multi-client validation, compact-role ownership, live-play evidence capture, player preparation, and reference-packet structure.

## Research rule

A source being listed here does **not** mean every statement in it has been validated or implemented. Research notes should identify specific sections/pages used.

When a source conflicts with another source, record the conflict rather than silently selecting one.

## Source status

Use these labels where helpful:

- **IDENTIFIED** — source found but not yet reviewed in sufficient detail.
- **REVIEWED-PARTIAL** — relevant portions reviewed.
- **REVIEWED** — reviewed for the research question being documented.
- **IMPLEMENTATION-SOURCE** — currently used to justify a simulation implementation.

## Local source files

The repository currently catalogs authoritative documents by stable NASA/NTRS or archival URL. Whether full PDFs should also be mirrored under `primary-sources/` is intentionally undecided; see `docs/OPEN_QUESTIONS.md`.

If files are mirrored later, retain source metadata and original filenames where practical.