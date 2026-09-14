# Station status addendum — PC+2 inverter MCC display routing

Date: 2026-09-14

## TELMU

Status remains unchanged.

New evidence from NASA TN D-7685 clarifies the MCC display architecture used to present telemetry-derived data. Computer-driven TV displays were requested by consoles and dynamically assigned to available TV channels; consoles could also attach to an already active channel. This means source-backed inverter telemetry (`GC0155` frequency and `GC0071` voltage) should not be modeled as if a fixed historical TV channel were permanently wired to TELMU.

For first playable, TELMU may receive a clearly labeled project-rendered inverter electrical product derived from those source-backed telemetry measurements. Exact Apollo 13 format identity, field layout, selection key, update cadence, and latency remain unresolved.

## CONTROL

Status remains unchanged.

The same display-system evidence prevents assigning a fabricated dedicated CONTROL channel for inverter voltage/frequency. CONTROL's PC+2 role and products remain those already established by source-backed station research; no new historical inverter display is attributed to CONTROL from this pass.

## Shared LM SYSTEMS compact role

No compact-mode rule changes. The modern TELMU+CONTROL player may switch between the two original station identities as already defined. If inverter electrical evidence is shown, it must remain attributable to the original station presentation and identified as a project rendering unless an Apollo 13 display-format record is recovered.

## Evidence boundary

Resolved:

- Apollo MCC computer-driven TV access used dynamic display-request/channel-attach behavior rather than requiring permanently assigned display channels.

Still unresolved:

- Apollo 13 format number/name carrying `GC0155` / `GC0071`;
- exact TELMU/CONTROL field placement and labels;
- which controller had the relevant format selected during PC+2;
- exact MSK/DRK action;
- cadence and end-to-end display latency;
- any support-room presentation.

No station maturity grade or physical-play validation status changes.
