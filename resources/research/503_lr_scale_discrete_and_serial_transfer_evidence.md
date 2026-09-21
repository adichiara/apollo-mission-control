# 503 — Landing-radar scale discrete and serial-transfer evidence

Date: 2026-09-20
Research thread: `apollo11-landing-radar`

## Question

Can the landing-radar high/low altitude-scale transition and raw LGC transfer path be bounded independently of the later Luminary 1B count-scale table?

## Primary evidence

AC Electronics manual ND-1021042, *LEM Primary Guidance, Navigation, and Control System*, prepared from source data available through 15 January 1966, Table 1-III identifies the LR/LGC interface signals. It states that:

- `Range low scale factor` originates in the LR and tells the LGC that a scale-factor change is necessary;
- that discrete is issued automatically at approximately 2,500 ft;
- `LR in "0" and LR in "1"` are digital pulses from the LR containing range and velocity data;
- the LGC supplies readout, gate-reset, range-strobe, and velocity-strobe signals.

A later near-mission primary vehicle source, the LM-6 Apollo Operations Handbook (LMA790-3-LM, basic date 15 December 1968, change 15 September 1969), preserves the same architecture in greater detail: at range PRF equivalent to 2,500 ft or less, the altimeter changes mode, enables the range-low-scale-factor discrete to the LGC, converts radar PRF data to the LGC 15-bit format, counts a selected pulse train for an 80-ms interval, and reads the resulting shift-register data serially to the LGC.

The two independent contractor/NASA-era sources therefore establish continuity of the **interface architecture and automatic ~2,500-ft scale-change indication** on both sides of Apollo 11. They do not by themselves prove the exact LM-5 high-scale bit weight.

## Consequence for the current scale question

This strengthens the interpretation of flown LUMINARY 099 `ALTSCBIT`: the software's high/low state corresponds to an actual LR-originated scale-state interface, not merely an internal software convention. It also narrows the raw-transfer problem: the LR supplied digital pulse data under LGC strobes/readout control, with an explicit scale discrete.

It does **not** resolve why the Apollo 11 prelaunch erasable-load table records `SKALSKAL = 00000`, nor does it prove that the Luminary 1B 5.3950-ft/count high-scale value was exactly the LM-5 hardware value.

## Prohibited inference

Do not infer from these sources alone:

- exact LM-5 high-scale altitude bit weight;
- exact LM-5 15-bit word coding, sign convention, bias, framing order, or rounding/truncation;
- that the ~2,500-ft transition occurred at an exact invariant altitude in Apollo 11 flight;
- that the scale-state discrete was exposed directly on an MCC/GUIDO display;
- a stochastic LR measurement-error model.

## Sources

1. AC Electronics Division, General Motors, ND-1021042, *LEM Primary Guidance, Navigation, and Control System*, Table 1-III, source data available through 15 January 1966: https://www.ibiblio.org/apollo/Documents/apollolunarexcuracel_0.pdf
2. Grumman, LMA790-3-LM, *Apollo Operations Handbook, Lunar Module, Subsystems Data*, LM-6, basic date 15 December 1968, change 15 September 1969; LR signal-processing description.
3. LUMINARY 099 `SERVICER.agc` / `FLAGWORD_ASSIGNMENTS.agc` for Apollo-11-effective software handling of the LR scale state.

## Evidence status

- **DOCUMENTED:** automatic LR-originated low-scale indication near 2,500 ft and digital pulse/strobe transfer architecture have independent primary-source support before and immediately after Apollo 11.
- **UNRESOLVED:** exact LM-5 high-scale bit weight and complete raw serial sign/bias/framing and rounding/truncation.
