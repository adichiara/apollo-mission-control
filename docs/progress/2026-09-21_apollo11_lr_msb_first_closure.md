# Progress — Apollo 11 landing-radar serial bit-order closure

Date: 2026-09-21

## Research target

Resolve the next open LR/LGC raw-transfer property: serial bit order. Keep serial sign representation/integer bias and radar-side rounding/truncation unresolved unless the recovered primary evidence explicitly defines them.

## Primary evidence recovered

MIT/MSC report R-700, Volume II, in its landing-radar interface description, states that after the computer readout command the radar shift-register contents cross the interface serially, with `1` bits on the ones bus and `0` bits on the zeros bus, and that **the most significant bit is read out first**.

An MIT/IL guidance-and-navigation functional description independently describes the LR Signal Data Converter as a 15-bit counter plus 15-bit shift register and states that the resulting range or velocity word is shifted out **most-significant-bit-first (MSBF)** on two lines. This matches the already recovered GSOP `LR in "1"` / `LR in "0"` interface and the Apollo-11-specific 15-pulse readout sequence.

## Controlled conclusion

Serial bit order is now closed at **MSB first** for the Apollo landing-radar/LGC interface. The two complementary data lines carry bit value separately: a `1` is transferred on the ones line and a `0` on the zeros line. Combined with the mission-specific Apollo 11 15-readout-pulse evidence, the project may model each LR quantity as a 15-bit serial transfer, MSB first, over complementary `1`/`0` data lines.

This finding does **not** establish how signed velocity is numerically represented inside the 15-bit word, whether any integer offset/bias is present, or how the Signal Data Converter rounds/truncates a physical measurement into its count. Those remain separate unresolved properties.

## Project consequence

- Close `serial bit order` as an unresolved LR interface item.
- Preserve `sign representation/integer bias` and `rounding/truncation` as unresolved.
- No GUIDO/CONTROL/FLIGHT display or procedure consequence is inferred from the electrical transfer format.

## Sources

- MIT/MSC, R-700, Volume II, landing-radar interface description: https://www.ibiblio.org/apollo/Documents/R-700-Volume-2.pdf
- MIT/IL, guidance-and-navigation functional description, Signal Data Converter §2.5.2.1.5: https://www.ibiblio.org/apollo/Documents/sundance_functional_description_vol1.pdf
- Existing Apollo-11-specific transfer-length evidence: `docs/progress/2026-09-21_apollo11_lr_15bit_word_closure.md`

## Evidence status

- **DOCUMENTED, PRIMARY APOLLO INTERFACE:** LR serial transfer is most-significant-bit-first; complementary ones/zeros lines carry bit value.
- **DOCUMENTED, APOLLO-11-SPECIFIC RAW TRANSFER LENGTH:** 15 readout pulses at 3200 pps, followed by radar interrupt.
- **UNRESOLVED:** signed-velocity numerical representation/integer bias and Signal Data Converter rounding/truncation.
