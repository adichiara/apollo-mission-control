# Progress — Apollo 11 landing-radar beam transform

Date: 2026-09-19

## Completed

Recovered a primary-source chain sufficient to close both the **static antenna-position** and the **dynamic attitude/reference-frame** portions of the Apollo 11 landing-radar velocity-beam geometry.

LUMINARY 099 directly shows `SETPOS` transforming antenna-frame basis vectors into navigation-base beam vectors. LUMINARY Memo #95 controls the sign/order convention, and the LM-5 Mission G LUMINARY 99 prelaunch load supplies the actual position-1 and position-2 alpha/beta values. The final-program controlled constants also supply `HBEAMANT` rather than requiring a guessed range-beam vector.

The dynamic leg is now explicit in the flown listing. `LRVJOB` schedules `RDGIMS` 170 ms after initiation of the five-sample velocity read; `RDGIMS` stores `TIME2,TIME1` in `LRVTIME`, stores `CDUX/CDUY/CDUZ` in `LRXCDU/LRYCDU/LRZCDU`, and snapshots the PIPAs. `VELUPDAT` later copies those saved CDU values into `CDUSPOT` in Y-Z-X order, calls `QUICTRIG`, and calls `*NBSM*` on the selected `V?BEAMNB`. The LUMINARY 099 powered-flight subroutine listing explicitly defines `*NBSM*` as the navigation-base-to-stable-member transformation using the already computed CDU sines/cosines.

This preserves the intended measurement-time attitude rather than silently using whatever attitude exists when the later update executes.

## Repository consistency repair

The prior landing-radar note was incorrectly created as research 405 inside the already allocated `apollo11-p66-pcr700` 400–499 block. That violated the repository's research-block allocation rule and made CI fail both the unit/index check and documentation audit. The invalid note was removed; its sourced conclusions are retained in this progress record, roadmap, station-status record, and Apollo 11 source-catalog addendum without claiming a research number from another thread.

## Boundary retained

The geometric reference chain is now controlled well enough to implement without an arbitrary beam vector. The next unresolved dependency is the **velocity reasonableness/update estimator** beginning after `*NBSM*`: reconstruction of measured velocity, comparison against the propagated estimate, inhibit/failure logic, and the altitude/velocity-dependent update weights.

No station-visible display cadence, controller-product timing, or executable scenario behavior changes in this documentation step.

## Next

Trace the Apollo-11-effective `VELUPDAT` estimator/update path through `VFAIL`, `VUPDAT`, `LRVF/LRVMAX`, `LRWV*`, `LRWVFF`, `GNUV`, and `GNURVST`, including mode-dependent behavior in P65/P66/P67. Keep controller-facing products as a separate evidence problem.

## Evidence status

- **DOCUMENTED:** static LM-5 antenna-position beam transform inputs and algorithm.
- **DOCUMENTED:** measurement-midpoint CDU/time capture and navigation-base-to-stable-member velocity-beam transformation.
- **PARTIALLY DOCUMENTED:** downstream landing-radar velocity reasonableness/update estimator.
- **UNRESOLVED:** controller-visible product timing and formatting.
