# Roadmap addendum — Apollo 11 landing-radar timing and measurement boundary

Date: 2026-09-20

## Newly closed

The Apollo 11 AC Electronics guidance/navigation manual directly constrains the onboard landing-radar velocity-update schedule: the three LR velocity components are consumed one per 2-second Average-G/PIPA interval, in the illustrated repeating `Vz → Vx → Vy` sequence.

NASA TN D-6849 constrains the error boundary: an LM-5 preflight one-count velocity bias was corrected before flight and a Gaussian assumption used for Doppler-spectrum-simulator test limits required correction because the test approximation produced heavier tails. Its Apollo 11 flight-performance section adds a mission-effective discriminator: LM-5 landing-radar data appeared well within specification limits except for a few low-velocity points near zero Doppler shift, where the radar was not expected to track. Two questionable points were attributed probably to poor data processing during the LGC overload alarm. This documents a localized operating-region/processing exception, not a general random-error distribution.

A NASA primary-source table reproduces Grumman Aircraft Engineering Corporation master end-item specification **LSP-470-2D** for the LM landing radar. It gives explicit **3-sigma accuracy envelopes**. Range accuracy is `1.4% + 15 ft` from 2,000–25,000 ft and `1.4% + 5 ft` from 10–2,000 ft. The velocity cells are now transcribed from the source table: at 25,000–2,000 ft, Vx = `1.5% or 1.5 ft/s`, Vy = `2.0% or 2.0 ft/s`, Vz = `2.0% or 2.0 ft/s`; at 2,000–200 ft, Vx = `1.5% or 1.5 ft/s`, Vy = `3.5% or 3.5 ft/s`, Vz = `3.0% or 3.0 ft/s`; at 200–5 ft, Vx = `1.5% or 1.5 ft/s`, Vy = `2.0% or 1.5 ft/s`, Vz = `2.0% or 1.5 ft/s`. The table says to use the percentage or ft/s value, whichever is greater, and identifies the percentage as a percentage of vector velocity. These are performance/acceptance limits, not a probability model.

MIT Instrumentation Laboratory R-700 Vol. II / NASA-CR-141898 section 5.5.2 closes the Apollo-11-specific measurement-reasonableness thresholds. Velocity admission used `|delta q| <= 7.5 + 0.125 V_T` ft/s, with `V_T` the estimated LM speed. Range-derived altitude admission used `|delta q| <= 200 + 0.125 h` ft, with `h` estimated altitude relative to the landing site. The altitude reasonableness test was omitted above high gate to avoid rejecting valid initial radar altitude that could differ from the estimate by several thousand feet. The report identifies cross-lobe lockup as the design motivation and states that any measurement failing the criterion is rejected regardless of cause. These equations are estimator admission criteria, not radar-noise or cross-lobe probability models.

The flown LUMINARY 099 `VELUPDAT` propagation equation is represented by a mission-neutral executable stage. The repository now also composes propagation → selected-beam reference projection → residual qualification → historical weighting/correction in one proof path. The selected measurement-time beam remains an explicit input, so composition does not silently invent the still-unported AGC geometry transform.

A fresh primary-source check confirms the remaining geometry boundary. `SETPOS` transforms antenna `UNITY`/`UNITX` into NB velocity beams and forms the third by cross product; Memo #95 fixes antenna-to-NB polarity/order; `VELUPDAT` restores measurement-time CDUs and applies `*NBSM*`; `POWERED_FLIGHT_SUBROUTINES.agc` defines that transform through the AGC `AX*SR*T` machinery. The source logic is controlled, but an independently verified executable port is not yet present.

## Current boundary

Keep distinct:

- LR sensor measurement/error generation — **3-sigma performance envelopes and the Apollo 11 observed near-zero-Doppler exception are source-controlled**, but the historical stochastic process/distribution remains **BLOCKED**; do not assume Gaussian noise;
- LGC component-read/update schedule — source-controlled at one component per 2-second navigation interval;
- onboard measurement admission — Apollo-11-specific velocity and altitude reasonableness equations are source-controlled, including omission of the altitude test above high gate;
- onboard measurement-time propagation/reference/qualification/weighting — source-controlled and executable as a composed proof when the measurement-time beam is supplied;
- LM-5 antenna/NB + measurement-time NB/SM beam synthesis — source-controlled but not yet independently ported/verified;
- spacecraft downlink sampling/word-list behavior;
- ground processing/product generation;
- controller display refresh/formatting and operational response.

## Next

Implement and independently verify the Apollo-11-effective `SETPOS` antenna-to-NB and `*NBSM*` measurement-time transforms before allowing the historical profile to synthesize its own beam. Preserve AGC angle order/polarity and test against source-derived invariants rather than selecting a modern Euler convention by assumption.

For sensor generation, LSP-470-2D may be used as a documented component/altitude performance envelope, including the source's `whichever is greater` rule. TN D-6849 may additionally constrain validation around the Apollo 11 near-zero-Doppler region and LGC-overload-associated questionable samples. R-700 Vol. II supplies measurement-admission thresholds, not a distribution of incoming radar errors. None of these sources justifies inventing a random distribution, dropout rate, correlation model, cross-lobe-lock probability, or alarm-time corruption mechanism. Continue searching for LM-5 qualification/acceptance or flight-data reduction material that quantifies those behaviors. MSC-69-EG-14 remains useful adjacent-effectivity evidence if retrieved.

Synthetic perturbations may be injected for tests/scenarios only when labeled synthetic rather than historical.

Controller-facing timing remains a separate evidence problem. Do not infer a two-second GUIDO/MCC refresh rate from onboard estimator cadence.

## Evidence status

- **DOCUMENTED:** LGC descent-state-vector LR velocity-component cadence.
- **DOCUMENTED:** Apollo-11-specific velocity and range-derived-altitude reasonableness criteria and high-gate altitude-test omission from R-700 Vol. II / NASA-CR-141898.
- **DOCUMENTED:** LM landing-radar 3-sigma range and altitude-banded Vx/Vy/Vz accuracy envelope from GAEC LSP-470-2D as reproduced in NASA primary material; this is a performance bound, not a stochastic distribution.
- **DOCUMENTED, APOLLO 11 FLIGHT EXPERIENCE:** LR data were within specification except a few low-velocity/near-zero-Doppler points where tracking was not expected; two questionable samples were probably associated with poor processing during the LGC overload alarm. No probability law follows from this.
- **DOCUMENTED / IMPLEMENTED:** explicit-input measurement-time propagation and composed propagation → projection → qualification → weighting proof.
- **DOCUMENTED:** LM-5 antenna-to-NB and measurement-time NB-to-SM transform structure, polarity/order, and orientation load values.
- **PARTIALLY IMPLEMENTED:** historical beam synthesis; AGC transform is not yet ported and independently verified.
- **UNRESOLVED:** ground/controller-visible cadence and formatting.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective stochastic radar measurement-error distribution/process beyond the documented performance envelope and localized flight exception.
