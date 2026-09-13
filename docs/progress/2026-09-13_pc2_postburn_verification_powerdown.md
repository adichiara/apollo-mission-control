# Progress — PC+2 immediate post-burn verification / power-down

Date: 2026-09-13

## Completed

- Took open question 35 as the next unresolved first-playable historical item after note 100.
- Reviewed primary Apollo 13 mission-operation, air-ground/commentary, and change-of-shift records.
- Established the source-backed immediate sequence: nominal cutoff/result → post-burn assessment → initial LM power-down while retaining PTC-required functions → PTC setup.
- Recorded nominal PGNS residuals and the documented 79+34 / 79+52 transition timing without converting them into unsupported controller automation.
- Explicitly deferred exact console keying, switch-by-switch power-down timing, unsupported formal poll structure, and full PTC dynamics.
- Resolved open question 35 for the current first playable.

## Effect on first playable

A successful PC+2 should not terminate gameplay at engine cutoff. The scenario should expose a short post-burn verification/transition state and then move into power conservation/PTC preparation. Additional station-specific implementation is deferred until physical play shows a concrete need.

## Next boundary

Physical seven-seat nominal validation remains the highest-priority unclosed PASS boundary, followed by the synthetic ΔP run and five-player compact validation. Any further historical work should be driven by a concrete dependency exposed there.