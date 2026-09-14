# Progress — PC+2 inverter MCC display routing

Date: 2026-09-14

## Completed

- Researched the next unresolved inverter item: how source-backed `GC0155` inverter frequency and `GC0071` inverter voltage should be understood once they reach Mission Control.
- Reviewed NASA TN D-7685, which documents Apollo MCC computer-driven TV display architecture.
- Established that computer-driven TV channels were dynamically assigned in **display request mode** and could also be shared through **channel attach mode**; they were not necessarily permanently tied to one console/display.
- Used the Apollo 15 MCC operational configuration only as a later architecture cross-check for separate LM TELMU and LM CONTROL console identities, not as Apollo 13 format proof.
- Added research note `118_pc2_inverter_mcc_display_routing_boundary.md`.

## First-playable consequence

The project must not invent a dedicated historical TELMU/CONTROL TV channel for `GC0155` or `GC0071`. A source-backed project rendering may expose inverter voltage/frequency evidence to the appropriate station, but the exact Apollo 13 format number, field placement, selection key, cadence, and latency remain unresolved.

## Documentation reconciled

- `resources/research/118_pc2_inverter_mcc_display_routing_boundary.md`
- `resources/source-catalog/PC2_INVERTER_WARNING_SOURCES.md`
- `resources/source-catalog/PC2_TELMU_PRESENTATION_SOURCES.md`
- `docs/station-status/2026-09-14_pc2_inverter_mcc_display_routing.md`
- `docs/roadmap/2026-09-14_pc2_inverter_mcc_display_routing.md`
- PR #11 summary

## Remaining validation boundary

No physical-play PASS claim is added. Seven-seat nominal, synthetic ΔP, and five-player compact human/device validation remain outstanding.
