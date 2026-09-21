# Apollo 11 LR velocity-bias closure

Date: 2026-09-21
Parent: `docs/progress/2026-09-21_apollo11_lr_msb_first_closure.md`

## Question

How did the Apollo 11 landing-radar interface carry signed velocity in the 15-bit serial word: a sign bit/complement representation, or a biased unsigned count?

## Primary-source result

Flown LUMINARY 099 closes this at the LGC boundary.

`CONTROLLED_CONSTANTS.agc` defines `LVELBIAS` as `DEC -12288 B-14` with the original comment `LANDING RADAR BIAS FOR 153.6 KC.` In the flown `P20-P25.agc` radar-interrupt reader, the landing-radar velocity path masks `RNRAD` with `POSMAX`, adds `LVELBIAS`, and then forms the double-precision sample used by the accumulation path. Thus the raw LR velocity word is not interpreted by LUMINARY 099 as an AGC signed number whose MSB is a sign bit; software removes a fixed 12,288-count offset to recover signed velocity.

This matches the independently documented hardware architecture: the LR velocity pulse train is superimposed on a 153.6-kHz reference so velocity sign can be determined upstream, while the Signal Data Converter counts the selected pulse train for 80 ms. A later but near-mission programmed-guidance-equations document explicitly describes `K:LVELBIAS = -12288` as the bias added to raw DNLRVEL counts, corroborating the flown-code interpretation.

The flown code also gives component conversion signs separately (`VXSCAL` = -0.644 ft/s/count, `VYSCAL` = +1.212 ft/s/count, `VZSCAL` = +0.8668 ft/s/count). Those component scale signs must not be confused with a serial sign-bit convention.

## Boundary retained

This closes the **numerical representation / integer-bias** question at the Apollo-11-effective LGC interface. It does **not** establish the Signal Data Converter's exact fractional-cycle handling at the end of the 80-ms counting gate, so hardware rounding versus truncation remains unresolved. It also does not create a controller-visible indication or procedure.

## Primary sources

- Flown LUMINARY 099 `CONTROLLED_CONSTANTS.agc`, hardware-related parameters: `LVELBIAS = -12288`, original comment `LANDING RADAR BIAS FOR 153.6 KC.`
- Flown LUMINARY 099 `P20-P25.agc`, `VELCHK`: masks `RNRAD` with `POSMAX`, then adds `LVELBIAS` before accumulating the velocity sample.
- NASA TN D-6849, *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar*: velocity pulse trains are superimposed on a 153.6-kHz reference to facilitate sign determination before SDC serialization.
- MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B*: independently identifies DNLRVEL bias handling with `K:LVELBIAS = -12288`.

## Evidence status

- **RESOLVED, APOLLO-11-EFFECTIVE:** raw LR velocity is a biased nonnegative 15-bit count at the LGC interface; LUMINARY 099 removes a 12,288-count bias in software.
- **NOT A SERIAL SIGN BIT:** bit 15 is masked away with `POSMAX` before the bias correction; signed physical velocity is recovered by offset removal plus the component conversion scale.
- **UNRESOLVED:** SDC end-of-gate rounding/truncation and any controller-visible consequence.
