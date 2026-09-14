# Roadmap addendum — PC+2 inverter direct caution / selector telemetry boundary

Date: 2026-09-14  
Status: **bounded archival refinement complete; physical validation priority unchanged**

## Resolved in this pass

Research note 117 follows note 116's ground electrical-observation result into the remaining direct-telemetry question.

NASA TN D-6845 Figure 27 explicitly labels PCMTEA telemetry paths for inverter-bus frequency `GC0155` and voltage `GC0071`, while separately showing the `GL4046` / `6DS26` derived onboard INVERTER caution and `4S14` selector/inhibit wiring without labeled PCM telemetry taps for those states.

The first playable therefore does not claim direct Mission Control telemetry of either the onboard caution discrete or inverter-selector position.

## Canonical information boundary

`GC0155 / GC0071 → PCMTEA/MSFN → source-backed ground electrical evidence`

`GL4046 / 6DS26 → onboard caution → crew observation/report`

`crew transfer procedure/action → selected-inverter identity → crew/scenario report state`

A station-facing warning derived from sourced voltage/frequency limits must be identified as a project-derived controller aid, not as a recovered Apollo 13 caution bit.

## Evidence guardrail

This is a bounded negative finding. The reviewed schematic is sufficient to prevent unsupported first-playable telemetry claims, but it does not prove that no other mission-era routing document could reveal an additional caution or selector discrete.

## Remaining inverter archival gaps

- exact Apollo 13 routing of `GC0155` / `GC0071` into TELMU/CONTROL or support-room displays;
- exact CRT/MSK field, update cadence, and latency;
- numeric inverter-selection caution-inhibit duration;
- any future primary source explicitly demonstrating an additional direct caution or selector telemetry path.

None currently blocks first playable.

## Priority

The next major PASS boundaries remain:

1. seven-seat nominal PC+2 physical human/device validation;
2. synthetic ΔP physical validation;
3. five-player compact physical validation;
4. reopen exact routing research only when a concrete validation or scenario dependency requires it.