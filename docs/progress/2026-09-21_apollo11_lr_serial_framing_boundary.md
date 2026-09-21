# Progress — Apollo 11 LR serial framing boundary

Date: 2026-09-21

## Question

After closing the Apollo-11-effective altitude scaling, what can primary sources establish about the previously unresolved raw LR/LGC serial framing without importing later LM configurations?

## Primary-source result

The MIT/IL *LEM PGNCS Guidance System Operations Plan*, Section 3, lists the LGC/LEM landing-radar inputs as separate `LR in "1" (Data Flow)` and `LR in "0" (Data Flow)` signals. Range/velocity-data-good, antenna-position, and range-low-scale signals are separately enumerated discretes.

AC Electronics ND-1021042 Table 1-III independently identifies `LR in "0" and LR in "1"` as digital pulses containing range and velocity data. It also identifies the complementary LGC controls: `Readout command`, a continuous 3,200-cps `Gate reset`, `Range strobe`, and Vx/Vy/Vz strobe pulses; the strobes enable the LR transfer gates.

## Controlled conclusion

This closes a limited but useful part of `framing`: the interface separates binary data value (`LR in 0/1`) from LGC-controlled transfer timing and quantity selection (readout/reset plus range/Vx/Vy/Vz strobes). A simulator can preserve that architectural separation without inventing a raw numeric word format.

The sources inspected here do **not** establish LM-5 raw word length, serial bit order, sign convention, integer bias, or rounding/truncation. The LM-6 handbook's explicit 15-bit description remains adjacent-effectivity corroboration only and is not promoted to Apollo 11.

No controller-visible consequence follows from this electrical-interface evidence.

## Repository updates

- `docs/roadmap/2026-09-19_apollo11_landing_radar_beam_transform.md`
- `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`
- `resources/APOLLO11_LR_SCALE_SELECTION_SOURCE_CATALOG_ADDENDUM.md`
- this progress record

No station maturity change. Historical stochastic LR measurement generation remains **BLOCKED** pending flight-effective residual/bias/correlation evidence.

## Next discriminating target

Seek LM-5/Apollo-11-effective hardware documentation for raw word length and bit order/sign coding. Treat rounding/truncation as a separate question unless a recovered interface or signal-data-converter description explicitly specifies it.
