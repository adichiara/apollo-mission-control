# Progress — PC+2 77-percent thrust-rule applicability

Date: 2026-09-13

## Completed

- Followed the bounded startup-applicability gap left by research note 107.
- Verified in the Apollo 13 Technical Crew Debriefing that PC+2 used 5 seconds at idle/low thrust, 21 seconds at 40-percent throttle, then full throttle, with the configured transition to full throttle at burn +26 seconds.
- Cross-checked the Flight Control Division Mission Operations Report, which independently records the same staged throttle profile in rounded form.
- Retained the antecedent Apollo 10 DPS mission-rule evidence showing throttle-regime qualification rather than importing that earlier rule verbatim into Apollo 13.

## Result

For the current first playable, the crew ENG THRUST <=77-percent criterion is inactive during the commanded 12.6/40-percent startup segments and becomes applicable when the commanded profile enters maximum/full throttle. For nominal Apollo 13 PC+2, the crew debrief fixes that transition at burn +26 seconds.

This is explicitly documented as a lineage-based historical approximation: no recovered Apollo 13 rule page has yet been found that states the applicability gate verbatim.

The gate does not create a crew ENG THRUST value. Evaluation still requires an explicit crew-visible observation path; hidden engine state may not be converted directly into a gauge reading.

## Documentation updated

- `resources/research/108_pc2_thrust_rule_applicability_gate.md`
- `resources/source-catalog/PC2_THRUST_MONITOR_SOURCES.md`
- `docs/ROADMAP.md`
- `resources/README.md`
- dated station-status addendum

## Next boundary

Physical seven-seat validation remains the primary project blocker, followed by the synthetic Delta-P run and five-player compact validation. Further archival work should remain demand-driven unless stronger Apollo 13-specific rule documentation is recovered.
