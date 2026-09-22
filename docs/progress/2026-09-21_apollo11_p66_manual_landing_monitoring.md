# Progress — Apollo 11 P66 manual-landing monitoring

Date: 2026-09-21

Continued from the descent-propellant-countdown stopping point into the next controller/player decision dependency: what changes at P66/manual takeover.

## Completed

- Recovered primary NASA TM X-58038 as the discriminating ground-monitoring source.
- Confirmed that descent guidance monitoring compared **PGNS, AGS, and MSFN-derived ground tracking** for abort/guidance-switchover assessment.
- Confirmed that P66/manual takeover did **not** terminate ground observation; Apollo 11 ground-monitoring material continues through the manual landing portion.
- Cross-checked the Apollo 11 Mission Report for the approximately **102:43:22 GET** P66/manual-takeover event and the later landing-radar-data loss.
- Applied already-sourced Flight Mission Rule 5-91: after crew takeover, trajectory/guidance constraints are not themselves abort causes.
- Defined the architecture boundary as **continued observation with changed decision semantics**, rather than loss of telemetry or automatic ground abort authority.

## Repository updates

- `docs/roadmap/2026-09-21_apollo11_p66_manual_landing_monitoring.md`
- `docs/progress/2026-09-21_apollo11_p66_manual_landing_monitoring.md`
- `docs/station-status/2026-09-21_apollo11_p66_manual_landing_monitoring.md`
- `resources/APOLLO11_P66_MANUAL_LANDING_MONITORING_SOURCE_CATALOG_ADDENDUM.md`

## Boundary preserved

No exact Mission-G CRT field, parameter mnemonic, internal P66 indication route, or GUIDANCE voice call has been inferred. P66 is not modeled as making ground trajectory data vanish, and post-P66 trajectory deviation is not promoted into an abort cause contrary to the mission-rule evidence.

## Next

Connect the explicit manual-control/P66 state to the reusable Apollo 11 descent decision-gate/model-lab proof so that the same observations can remain visible while their rule interpretation changes after crew takeover.

## Evidence status

**SUFFICIENT** for the current architecture dependency. Exact ground display/keying detail is optional unless a later player-facing implementation requires it.