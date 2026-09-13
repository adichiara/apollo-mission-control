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
- `source-catalog/PC2_INLET_PRESSURE_SOURCES.md` — focused source record for the unresolved singular inlet-pressure selection/aggregation question.
- `source-catalog/PC2_INVERTER_WARNING_SOURCES.md` — focused source record for the inverter-caution, crew-switch, and post-switch mission-rule path.
- `source-catalog/PC2_THRUST_MONITOR_SOURCES.md` — focused source record for the unresolved onboard 77-percent thrust-monitor indication and rejected unsupported mappings.
- `source-catalog/PC2_ATTITUDE_SOURCES.md` — focused source record for PC+2 attitude-error/rate criteria, the startup-transient source conflict, and CONTROL observation provenance.
- `source-catalog/PC2_FRESHNESS_SOURCES.md` — focused source record for observation age, data validity, and the unresolved absence of a PC+2-specific stale-data threshold.
- `source-catalog/PC2_RESTART_SOURCES.md` — mission-specific sources for the premature DPS shutdown/restart branch and the distinction between rule-caused shutdown and restart-eligible unexplained shutdown.
- `source-catalog/PC2_DPS_RESTART_RESPONSE_SOURCES.md` — mission-specific and contemporary sources for separating an eligible restart procedure from the successful physical engine-on response.
- `source-catalog/PC2_DELTA_P_CALLOUT_SOURCES.md` — mission-specific sources for the ground-only fuel/oxidizer ΔP >25 psi shutdown callout, first playable CONTROL→CAPCOM integration boundary, and explicit unresolved-routing limits.
- `source-catalog/PC2_DPS_SHUTDOWN_RESPONSE_SOURCES.md` — contemporary LM sources for crew STOP-pushbutton control, engine-off command routing, and DPS valve-response semantics.
- `source-catalog/PC2_DPS_SHUTDOWN_CONFIRMATION_SOURCES.md` — mission-specific and contemporary evidence for crew voice shutdown report plus fresh GQ6510P chamber-pressure observation as distinct response-evidence channels, without an invented engine-off threshold.
- `source-catalog/PC2_CREW_RESPONSE_SOURCES.md` — primary-source supplement for CAPCOM ground-call receipt, explicit crew shutdown command, physical DPS response separation, and its HTTP validation exposure.
- `source-catalog/PC2_CONTROL_PRESENTATION_SOURCES.md` — mission-specific Apollo 13 MSK 1123/1137 and PC+2 operational sources constraining the first player-facing CONTROL rendering.
- `source-catalog/PC2_GUIDO_PRESENTATION_SOURCES.md` — mission-specific Apollo 13 MSK 1123/1137, LUMINARY 1C R-567, and PC+2 operational sources constraining the first player-facing GUIDO rendering.
- `source-catalog/PC2_TELMU_PRESENTATION_SOURCES.md` — mission-specific PC+2 chronology, TELMU post-mission, Review Board, and inverter-rule sources constraining the first player-facing TELMU rendering.
- `source-catalog/PC2_FIDO_RETRO_PRESENTATION_SOURCES.md` — final PC+2 maneuver/monitor PAD plus mission-specific FIDO/RETRO sources constraining the first target/return player rendering.
- `source-catalog/PC2_INCO_PRESENTATION_SOURCES.md` — mission-specific communications and ranging evidence constraining the first player-facing INCO rendering.
- `source-catalog/PC2_FLIGHT_CAPCOM_PRESENTATION_SOURCES.md` — mission-specific Flight Director and air-ground communication sources constraining the first FLIGHT and CAPCOM renderings.
- `source-catalog/PC2_SESSION_INTEGRATION_SOURCES.md` — historical/state-machine sources governing the first authoritative playable-session orchestration layer.
- `source-catalog/PC2_FINAL_LOAD_UPLINK_SOURCES.md` — mission-specific primary evidence for the staged final PC+2 state-vector/target-load/uplink workflow across Flight Dynamics, GUIDO, INCO, CAPCOM/crew, and FLIGHT, with exact vector and ground-command internals explicitly deferred.
- `source-catalog/PC2_POSTBURN_SOURCES.md` — primary Apollo 13 evidence for the immediate post-PC+2 maneuver assessment, initial LM power-down, retained communications/guidance functions, and PTC-preparation boundary.
- `source-catalog/PC2_SPACECRAFT_MODEL_SCOPE_SOURCES.md` — primary Apollo/NASA LM subsystem sources constraining the amount of spacecraft physics required by the first playable and supporting the decision-relevant causal-fidelity rule.
- `source-catalog/PC2_GROUND_DATA_PROCESSING_SOURCES.md` — Apollo 13 Review Board and March 1970 MCC/MSFN sources constraining MSFN/CCATS/RTCC behavior to decision-relevant tracking, telemetry, trajectory, display, and command/load services rather than full ground-computer emulation.
- `source-catalog/PC2_BACKROOM_SUPPORT_SOURCES.md` — Apollo 13 primary evidence for Staff Support Room/backroom functions and the first-playable rule that omits separate backroom players without pretending the historical support structure did not exist.
- `source-catalog/WEB_TRANSPORT_SOURCES.md` — current Render/FastAPI platform documentation supporting the first phone-accessible transport and deployment shell.
- `source-catalog/FACILITATOR_AUTHORITY_SOURCES.md` — primary NASA simulation-control sources plus current Render secret-management sources supporting the facilitator/controller authority boundary.
- `source-catalog/INTEGRATED_SIMULATION_VALIDATION_SOURCES.md` — primary NASA simulation-training sources supporting integrated multi-station validation with a distinct simulation-control function, without treating HTTP/browser mechanics as historical.
- `source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md` — primary Apollo/NASA simulation-training, mission-rule, and procedure-development sources constraining the real-device/human-play protocol, scenario-blind player preparation/reference packet, structured evidence/debrief package, and separation of mission-like rehearsal from modern browser/mobile usability testing.
- `source-catalog/PC2_LOW_PLAYER_COUNT_SOURCES.md` — Apollo organizational/staffing and PC+2 communications evidence constraining five-player compact play, original-station preservation, and the decision not to approve a sub-five-player PC+2 mode at the current fidelity target.
- `source-catalog/APOLLO13_GROUND_PRODUCT_INTEGRITY_SOURCES.md` — mission-specific sources for the post-MCC-5 RTCC/AGS body-angle processing error and the distinction between product availability/validity and hidden data integrity.

Latest scenario-integration research:

- `research/081_pc2_mission_clock_and_decision_gate_semantics.md` — primary-source GET findings plus the explicitly superseded provisional pause-gate policy.
- `research/082_pc2_delta_p_session_integration_boundary.md` — carries the documented >25-psi ground-callout rule through CONTROL decision and CAPCOM transmission without inventing internal routing or automatic crew/vehicle response.
- `research/083_pc2_crew_response_after_ground_shutdown_call.md` — extends that branch through explicit crew receipt, crew shutdown command, and a separate physical DPS engine-off response without inventing timing or telemetry confirmation.
- `research/084_continuous_mission_clock_architecture.md` — current architecture: GET continues through controller decisions, explicit pause is the only normal clock stop, and nominal milestones whose prerequisites are absent are missed rather than replayed later.
- `research/085_pc2_http_crew_response_integration.md` — exposes the source-bounded crew receipt → command → physical-response chain through HTTP while preserving continuous GET and avoiding invented response timing.
- `research/086_pc2_shutdown_evidence_http_integration.md` — exposes crew-report and fresh GQ6510P evidence through CONTROL without leaking physical truth or inventing an engine-off threshold.
- `research/087_player_admin_client_separation.md` — separates ordinary station UI from validation/SimSup controls.
- `research/088_facilitator_authority_boundary.md` — uses primary NASA simulation-control evidence to keep facilitator/SimSup authority separate from controller stations, with a modern server-side credential for exercise-wide operations.
- `research/089_multiclient_integrated_validation_boundary.md` — establishes source-bounded integrated validation across several controller clients and a distinct facilitator, and records the automated/network smoke artifacts and defects found during the first validation pass.
- `research/090_live_device_human_play_validation_boundary.md` — defines the remaining real-device/human-play boundary as a structured integrated mission rehearsal, with modern browser/mobile defects kept distinct from historical research gaps.
- `research/091_low_player_count_station_aggregation_boundary.md` — defines the first compact five-player PC+2 configuration from Apollo functional group/authority evidence while requiring original station identities to survive under bundled player presentation.
- `research/092_multi_station_player_ownership.md` — implements that compact-domain boundary as one player owning multiple original stations, with separate presentations, station-qualified readiness/actions, and original-station audit provenance.
- `research/093_compact_http_browser_integration.md` — carries compact ownership through HTTP join/rejoin and browser substation navigation while keeping TELMU, CONTROL, GUIDO, and FIDO/RETRO visibly and operationally distinct.
- `research/094_pc2_four_player_boundary.md` — resolves the previously open sub-five-player question for PC+2: CAPCOM and INCO remain separate and five players are the minimum supported configuration at the current fidelity target, without claiming a historical staffing minimum.
- `research/095_live_play_evidence_capture_and_debrief.md` — defines structured incident provenance and post-run debrief separation so physical play observations can drive reproducible software fixes or new historical research without converting player difficulty into unsupported Apollo behavior.
- `research/096_live_play_player_preparation_boundary.md` — defines the reproducible pre-run knowledge boundary: players receive station responsibility, relevant rules/procedures, authority context, and modern client-operation knowledge while remaining blind to nonnominal branch timing/content, hidden state, and other stations' private information.
- `research/097_live_play_reference_packet_structure.md` — defines the initial first-playable reference packet: separate common context, original-station sheets, neutral rule/criterion references, nominal phase/procedure context, and visibly modern client-operation instructions; unresolved historical criteria remain unresolved rather than becoming hints.
- `research/098_pc2_final_state_vector_target_load_uplink.md` — resolves the first-playable final-load workflow into a source-backed staged FIDO/GUIDO/INCO/CAPCOM/crew/FLIGHT process while leaving exact vector contents, RTCC/CCATS internals, controller keying, and transmission duration unfrozen.
- `research/099_pc2_final_load_staged_implementation.md` — carries note 098 into executable solution/load/uplink states and station-scoped products while preserving the same explicit evidence limits.
- `research/100_pc2_backroom_staff_support_boundary.md` — documents Apollo 13 SSR support and resolves the current first-playable boundary: backrooms remain acknowledged but non-playable until a scenario exposes a concrete support-product dependency.
- `research/101_pc2_immediate_postburn_verification_powerdown.md` — establishes the source-backed immediate post-PC+2 sequence through maneuver assessment, initial LM power-down, and PTC preparation without inventing console keying or full PTC dynamics.
- `research/102_pc2_spacecraft_physical_model_scope.md` — resolves how much spacecraft physics the first playable needs: causal DPS, guidance/control, electrical availability, communications, and observation-integrity state only where a sourced player decision or selected failure mechanism depends on it.
- `research/103_pc2_ground_data_processing_scope.md` — resolves how much MSFN/CCATS/RTCC behavior the first playable needs: functional tracking/telemetry/trajectory/display/load services and data-quality consequences only where a sourced player decision depends on them; internal ground-computer emulation remains deferred.

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

The repository currently catalogs authoritative documents by stable NASA/NTRS URL. Whether full PDFs should also be mirrored under `primary-sources/` is intentionally undecided; see `docs/OPEN_QUESTIONS.md`.

If files are mirrored later, retain source metadata and original filenames where practical.