# Station status — PC+2 ΔP nonnominal session integration

Date: 2026-09-12

## CONTROL

Status remains **B — strong workflow**.

New integration result:

- the modeled ground-derived fuel/oxidizer ΔP product can now enter the authoritative playable session through an explicit source-state injection;
- CONTROL sees the resulting product through its existing station projection/presentation;
- the common shutdown-rule evaluator must report the >25 psi criterion as triggered before CONTROL can issue the ground callout;
- the callout is an explicit controller decision event, not an automatic consequence of hidden simulation state.

Historical boundary remains unchanged: the exact ground computation, display routing, and internal voice-loop routing are unresolved.

## CAPCOM

Status remains **B — strong workflow**.

New integration result:

- a CONTROL-originated shutdown callout can enter the existing CAPCOM queue;
- the queue marks `requested_by=CONTROL` and explicitly labels its routing as a project abstraction because the exact historical CONTROL→FLIGHT→CAPCOM sequence is not established;
- CAPCOM transmission remains a distinct action;
- transmission does not automatically create crew compliance or physical DPS shutdown.

## Research consequence

No station maturity grade changes. The work improves **playable workflow integration**, not exact console/display reconstruction.

The next station/workflow boundary is crew response after a transmitted shutdown callout, followed by the already-separated crew-command → physical DPS response → controller-evidence chain.

See `resources/research/082_pc2_delta_p_session_integration_boundary.md` and `resources/source-catalog/PC2_DELTA_P_CALLOUT_SOURCES.md`.
