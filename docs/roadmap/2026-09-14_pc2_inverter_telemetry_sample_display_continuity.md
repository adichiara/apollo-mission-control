# Roadmap Addendum — PC+2 inverter telemetry sample/display continuity

Date: 2026-09-14

## Newly resolved boundary

Research note 119 narrows the inverter ground-presentation gap without overclaiming Apollo 13 configuration.

Primary later-LM telemetry documentation demonstrates that `GC0071V` and `GC0155F` were operational MSFN telemetry products with **format-dependent** sampling and multiple primary MSK destinations. The Apollo 13 LM-7/8/9 elementary diagrams independently confirm the measurement identities for the mission vehicle family.

## Decision

Do not freeze a historical Apollo 13 inverter display rate or MSK number from LM-10 evidence.

For first playable:

- preserve `GC0071V` / `GC0155F` as source-backed ground electrical evidence;
- keep exact CRT/MSK presentation explicitly project-rendered;
- keep telemetry sample cadence separate from MCC/display refresh latency;
- do not invent a fixed rate from the later 1 sample/s or 0.2 sample/s values.

## Next archival target

Priority order:

1. LM-7/Apollo 13 instrumentation packet or telemetry-format loading record;
2. Apollo 13 MCC display-format/load artifact identifying these measurement IDs;
3. controller configuration/log evidence identifying an actual PC+2 display selection.

If none is recovered, retain the current project-rendered presentation rather than synthesizing historical detail.

## Validation roadmap impact

No change. Research refinement does not substitute for the existing human/device validation gates:

- seven-seat nominal;
- synthetic ΔP;
- five-player compact.
