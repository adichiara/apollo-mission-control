# Progress — Apollo 11 LR SDC gate quantization boundary

Date: 2026-09-21

## Question

Does the landing-radar Signal Data Converter apply a numerical rounding or truncation rule to the 80-ms measurement sample?

## Primary-source result

MIT/MSC R-700 Volume II §5.4.5 describes each radar measurement as passing through a computer-controlled gate into a binary high-speed counter. The counter accumulates the selected measurement and then serially transfers its integer contents to the computer.

MIT/IL E-1982 independently describes the LR velocity path: on LGC command, the selected LR velocity signal is allowed to **accumulate in the radar high-speed counter for an 80-millisecond count interval controlled by the LGC**. MIT/IL HSI-208625 uses the same count-domain semantics for LR self-test values, specifying Vx, Vy, Vz, and range as counts accumulated over an 80-ms sample period.

## Controlled conclusion

The earlier open item was phrased too much like a software numeric conversion. The recovered primary descriptions do not show an ideal real-valued measurement being multiplied by 0.080 and then passed through `round`, `floor`, or another arithmetic quantizer. They show a hardware event counter accumulating pulses admitted while the measurement gate is open.

For the simulator, the historically supported boundary is therefore:

- form the LR digital sample as an **integer gated pulse count**;
- do not add a separate nearest-rounding or truncation operation merely to reproduce an idealized `frequency × gate_time` value;
- preserve the already documented 15-bit serialization and velocity bias downstream.

This does **not** establish the circuit-level treatment of a pulse arriving exactly at a gate transition. If sub-count phase/timing is ever modeled, gate-edge inclusion remains unresolved and requires circuit-level evidence. It also does not establish stochastic measurement-error distributions.

## Documentation synchronization

Updated:

- `docs/roadmap/2026-09-20_apollo11_lr_scale_selection.md`
- `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`
- `resources/APOLLO11_LR_SCALE_SELECTION_SOURCE_CATALOG_ADDENDUM.md`

The next substantive LR/GUIDO question is controller visibility of the PCR-775 compensation/scale state; the stochastic historical LR error generator remains BLOCKED.

## Evidence status

- **RESOLVED MODEL BOUNDARY:** gated integer pulse accumulation is the documented SDC measurement mechanism.
- **NOT ESTABLISHED / NOT TO BE INVENTED:** an independent arithmetic rounding or truncation operator.
- **UNRESOLVED BELOW MODEL BOUNDARY:** exact gate-edge pulse inclusion/phase behavior.
- **UNRESOLVED:** controller-visible consequence.
- **BLOCKED:** flight-effective stochastic LR residual/error distribution.
