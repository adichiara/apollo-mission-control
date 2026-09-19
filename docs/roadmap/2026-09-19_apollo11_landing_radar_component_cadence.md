# Roadmap addendum — Apollo 11 landing-radar timing and measurement boundary

Date: 2026-09-19

## Newly closed

The Apollo 11 AC Electronics guidance/navigation manual directly constrains the onboard landing-radar velocity-update schedule: the three LR velocity components are consumed one per 2-second Average-G/PIPA interval, in the illustrated repeating `Vz → Vx → Vy` sequence.

NASA TN D-6849 constrains the error boundary: an LM-5 preflight one-count velocity bias was corrected before flight and a Gaussian assumption used for Doppler-spectrum-simulator test limits required correction because the test approximation produced heavier tails. Apollo 11 flight data were reported within specification limits apart from low/near-zero-Doppler behavior, but the recovered source does not supply a numerical flight-effective stochastic distribution.

The flown LUMINARY 099 `VELUPDAT` propagation equation is represented by a mission-neutral executable stage. The repository now also composes propagation → selected-beam reference projection → residual qualification → historical weighting/correction in one proof path. The selected measurement-time beam remains an explicit input, so composition does not silently invent the still-unported AGC geometry transform.

A fresh primary-source check confirms the remaining geometry boundary. `SETPOS` transforms antenna `UNITY`/`UNITX` into NB velocity beams and forms the third by cross product; Memo #95 fixes antenna-to-NB polarity/order; `VELUPDAT` restores measurement-time CDUs and applies `*NBSM*`; `POWERED_FLIGHT_SUBROUTINES.agc` defines that transform through the AGC `AX*SR*T` machinery. The source logic is controlled, but an independently verified executable port is not yet present.

## Current boundary

Keep distinct:

- LR sensor measurement/error generation — historical stochastic generation is **BLOCKED**, not free to assume Gaussian noise;
- LGC component-read/update schedule — source-controlled at one component per 2-second navigation interval;
- onboard measurement-time propagation/reference/qualification/weighting — source-controlled and executable as a composed proof when the measurement-time beam is supplied;
- LM-5 antenna/NB + measurement-time NB/SM beam synthesis — source-controlled but not yet independently ported/verified;
- spacecraft downlink sampling/word-list behavior;
- ground processing/product generation;
- controller display refresh/formatting and operational response.

## Next

Implement and independently verify the Apollo-11-effective `SETPOS` antenna-to-NB and `*NBSM*` measurement-time transforms before allowing the historical profile to synthesize its own beam. Preserve AGC angle order/polarity and test against source-derived invariants rather than selecting a modern Euler convention by assumption.

Synthetic perturbations may be injected for tests/scenarios only when labeled synthetic rather than historical. Reopen historical stochastic LR generation only if an LM-5 end-item specification, qualification/acceptance report, applicable performance specification, or sufficiently resolved Apollo 11 flight-data source supplies the missing error model.

Controller-facing timing remains a separate evidence problem. Do not infer a two-second GUIDO/MCC refresh rate from onboard estimator cadence.

## Evidence status

- **DOCUMENTED:** LGC descent-state-vector LR velocity-component cadence.
- **DOCUMENTED / IMPLEMENTED:** explicit-input measurement-time propagation and composed propagation → projection → qualification → weighting proof.
- **DOCUMENTED:** LM-5 antenna-to-NB and measurement-time NB-to-SM transform structure, polarity/order, and orientation load values.
- **PARTIALLY IMPLEMENTED:** historical beam synthesis; AGC transform is not yet ported and independently verified.
- **UNRESOLVED:** ground/controller-visible cadence and formatting.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical stochastic radar measurement-error distribution.
