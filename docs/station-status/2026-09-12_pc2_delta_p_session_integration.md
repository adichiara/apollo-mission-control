# Station status — PC+2 ΔP nonnominal session integration

Date: 2026-09-12

## CONTROL

Status remains **B — strong workflow**.

Current integration result:

- the modeled ground-derived fuel/oxidizer ΔP product enters the authoritative playable session through an explicit source-state injection;
- CONTROL sees the resulting product through its existing station projection/presentation;
- the common shutdown-rule evaluator must report the >25 psi criterion as triggered before CONTROL can issue the ground callout;
- the callout is an explicit controller decision event, not an automatic consequence of hidden simulation state;
- after the downstream crew/vehicle response, CONTROL confirmation must still come from fresh controller-observable evidence rather than hidden physical state.

Historical boundary remains unchanged: the exact ground computation, display routing, internal voice-loop routing, and a formal engine-off pressure threshold remain unresolved.

## CAPCOM

Status remains **B — strong workflow**.

Current integration result:

- a CONTROL-originated shutdown callout enters the existing CAPCOM queue;
- the queue marks `requested_by=CONTROL` and explicitly labels its routing as a project abstraction because the exact historical CONTROL→FLIGHT→CAPCOM sequence is not established;
- CAPCOM transmission remains a distinct action;
- transmission does not automatically create crew receipt, compliance, or physical DPS shutdown;
- the HTTP validation chain now continues beyond transmission only through explicit crew and vehicle operations.

## Crew / vehicle integration boundary

The crew is not represented as another front-room controller station. For validation, the HTTP layer now exposes three explicit operations after CAPCOM transmission:

1. crew receipt of the transmitted shutdown call;
2. crew DPS shutdown command;
3. physical DPS engine-off response.

These operations reuse the existing domain models and remain separate. No response delay, exact hypothetical readback, unique crewmember assignment, or automatic chamber-pressure response is invented.

## Research consequence

No station maturity grade changes. The work improves **playable workflow integration**, not exact console/display reconstruction.

The next station-relevant boundary returns to CONTROL: expose and exercise the already-modeled shutdown evidence channels—crew shutdown report and fresh post-command `GQ6510P` observation—without creating an automatic engine-off verdict.

See:

- `resources/research/082_pc2_delta_p_session_integration_boundary.md`
- `resources/research/083_pc2_crew_response_after_ground_shutdown_call.md`
- `resources/research/085_pc2_http_crew_response_integration.md`
- `resources/research/070_pc2_dps_shutdown_confirmation_evidence.md`
- `resources/source-catalog/PC2_CREW_RESPONSE_SOURCES.md`
