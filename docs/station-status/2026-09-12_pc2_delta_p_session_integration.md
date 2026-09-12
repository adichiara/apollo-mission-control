# Station status — PC+2 ΔP nonnominal session integration

Date: 2026-09-12

## CONTROL

Status remains **B — strong workflow**.

Current integration result:

- the modeled ground-derived fuel/oxidizer ΔP product enters the authoritative playable session through an explicit source-state injection;
- CONTROL sees the resulting product through its existing station projection/presentation;
- the common shutdown-rule evaluator must report the >25 psi criterion as triggered before CONTROL can issue the ground callout;
- the callout is an explicit controller decision event, not an automatic consequence of hidden simulation state;
- after the downstream crew/vehicle response, CONTROL can now request a shutdown-evidence assessment built only from controller-observable channels;
- a post-command crew shutdown report and a fresh post-command `GQ6510P` product remain independent channels;
- pre-command chamber-pressure data cannot count as shutdown-response evidence;
- the evidence assessment deliberately does not inspect authoritative `engine_running` state and never creates `engine_off_confirmed`.

Historical boundary remains unchanged: the exact ground computation, display routing, internal voice-loop routing, and a formal engine-off pressure threshold remain unresolved.

## CAPCOM

Status remains **B — strong workflow**.

Current integration result:

- a CONTROL-originated shutdown callout enters the existing CAPCOM queue;
- the queue marks `requested_by=CONTROL` and explicitly labels its routing as a project abstraction because the exact historical CONTROL→FLIGHT→CAPCOM sequence is not established;
- CAPCOM transmission remains a distinct action;
- transmission does not automatically create crew receipt, compliance, physical DPS shutdown, or controller confirmation;
- the HTTP validation chain continues beyond transmission only through explicit crew, vehicle, and evidence operations.

## Crew / vehicle integration boundary

The crew is not represented as another front-room controller station. For validation, the HTTP layer exposes explicit operations for:

1. crew receipt of the transmitted shutdown call;
2. crew DPS shutdown command;
3. physical DPS engine-off response;
4. crew shutdown report as a controller-observable evidence channel.

These operations reuse the existing domain models and remain separate. No response delay, exact hypothetical readback, unique crewmember assignment, or automatic chamber-pressure response is invented.

## Research consequence

No station maturity grade changes. The work improves **playable workflow integration**, not exact console/display reconstruction.

The source-bounded ΔP branch now reaches CONTROL-observable evidence end to end. The next useful work is runnable multi-client integration validation and player-surface cleanup, not further low-value DPS display reconstruction unless testing exposes a concrete missing decision dependency.

See:

- `resources/research/082_pc2_delta_p_session_integration_boundary.md`
- `resources/research/083_pc2_crew_response_after_ground_shutdown_call.md`
- `resources/research/085_pc2_http_crew_response_integration.md`
- `resources/research/086_pc2_shutdown_evidence_http_integration.md`
- `resources/research/070_pc2_dps_shutdown_confirmation_evidence.md`
- `resources/source-catalog/PC2_CREW_RESPONSE_SOURCES.md`
- `resources/source-catalog/PC2_DPS_SHUTDOWN_CONFIRMATION_SOURCES.md`
