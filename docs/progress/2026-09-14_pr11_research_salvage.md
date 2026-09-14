# PR #11 research salvage — 2026-09-14

## Purpose

PR #11 accumulated valuable PC+2 research on controller observation boundaries, shutdown-rule lineage, attitude/thrust criteria, and inverter/TELMU telemetry while the implementation and live-validation branches continued moving independently. By 2026-09-14 the PR itself had diverged too far from `main` to merge safely.

This clean extraction preserves only research and source-catalog material that remains useful on the current branch.

## Preserved from PR #11

- research notes 104–123;
- corrections/refinements to research notes 053, 057, 059, and 061;
- the supporting attitude, inlet-pressure, thrust-monitor, inverter-warning, inverter-telemetry, TELMU-presentation, observation-failure, crew-action, and PHO-TR155 source catalogs.

The preserved material includes these bounded findings:

- observation failures should remain attributable to their actual layer rather than becoming a generic `telemetry failure`;
- the 150-psi inlet-pressure criterion is narrowed toward fuel inlet / `GQ3611P`, but an Apollo 13-specific exact mapping remains unproven;
- the onboard percent-thrust criterion is tied to the CMD THRUST / ENG THRUST instrument family, with first-playable applicability beginning at the sourced transition to maximum/full throttle rather than during commanded low-thrust startup;
- the attitude start-transient exception is source-bounded without inventing an unsupported numeric transient duration;
- Apollo 13 PC+2 retained inverter 2, and the alternate inverter transfer procedure is source-backed;
- `GC0071V` AC-bus voltage and `GC0155F` AC-bus frequency provide a source-backed ground electrical observation path through PCMTEA telemetry;
- direct PCM telemetry of the inverter caution output or inverter selector position is not established by the reviewed schematics;
- MCC display access was dynamically requested/attached rather than a permanent parameter-to-console channel;
- later-LM sample schedules, MSKs, and Apollo 15 TELMU indicator positions are useful continuity evidence but are not promoted into Apollo 13 facts;
- the Apollo 13 transcript provides a separate crew-local electrical/caution observation path;
- contemporaneous Philco material confirms the H-2 PHO-TR155 Revision C and data-pack Revision N date as 1970-03-06, while the actual Revision C content remains unrecovered.

## Deliberately not carried forward

The extraction does **not** copy PR #11's old roadmap, progress, station-status, README, or live-validation state. Those were overtaken by subsequent implementation and the completed nominal deployed PC+2 timing pass.

It also does not promote PR #11's crew-representation wording into a current design decision. The research note is retained as context for the current first-playable architecture, while broader crew representation remains deferred.

No implementation code, scenario timing, player UI, facilitator UI, or live-validation behavior is changed by this salvage.
