# Station status — 2026-09-13 — PC+2 staged final-load workflow

## FIDO / RETRO

Maturity remains **B**.

The executable first-playable now distinguishes preliminary versus final/stable PC+2 ground-solution status. This strengthens the workflow model without asserting exact RTCC displays, Cartesian vector contents, or controller-key sequences.

## GUIDO

Maturity remains **B**.

State-vector and target-load status are now staged as `preliminary_loaded` → `final_pending` → `transmitting` → `final_loaded`, with the separate ground-solution stage exposed to GUIDO. This replaces the former generic `pending_final_verification` state.

## INCO

Maturity remains **B**.

INCO now receives separate uplink-configuration readiness and transmission-active products while ranging remains independent. Exact command-system internals and look-angle/command display layouts remain unresolved.

## CAPCOM

Maturity remains **B**.

CAPCOM now receives final-load requested/completed status in the crew-facing workflow. The model does not invent an exact historical internal routing or approval chain beyond the source-supported coordination boundary.

## FLIGHT

Maturity remains **B**.

FLIGHT now receives final-solution stage and final-load completion status, preserving its supervisory/readiness role without exposing hidden vector contents or synthetic omniscient telemetry.

## Overall consequence

No station maturity grade changes. The change improves first-playable workflow fidelity and information separation, not exact console/display reconstruction.