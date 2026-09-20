# Progress — Apollo 11 landing-radar reasonableness criteria

Date: 2026-09-20

## Work completed

The next unresolved landing-radar item was the mission-specific numerical boundary for the onboard measurement reasonableness test. Primary NASA contractor evidence now closes that parameter gap.

MIT Instrumentation Laboratory, *MIT's Role in Project Apollo, Volume II: Optical, Radar, and Candidate Subsystems* (R-700 Vol. II / NASA-CR-141898), section 5.5.2, states that all LM program assemblies contained a radar reasonableness test comparing each radar measurement with the corresponding quantity estimated from the LM state vector.

For **Apollo 11**, the report gives:

- velocity: `|delta q| <= 7.5 + 0.125 V_T` ft/s, where `V_T` is estimated LM speed;
- range-derived altitude: `|delta q| <= 200 + 0.125 h` ft, where `h` is estimated altitude relative to the landing site.

The report states that the altitude reasonableness test was omitted above high gate because valid radar altitude could initially differ from the estimated altitude by several thousand feet. It also explains that the test was introduced to protect against possible cross-lobe lockup, while noting that any measurement failing the criterion is rejected regardless of the error's cause.

## Result

The repository no longer needs to treat Apollo 11 residual qualification as merely a caller-defined generic affine gate. The historical profile can be parameterized with mission-specific velocity and altitude criteria once that profile wiring is implemented.

This evidence does **not** establish:

- a probability of cross-lobe lockup;
- a stochastic radar-error distribution;
- correlation or bias behavior;
- how an onboard reasonableness rejection appeared to GUIDO;
- an MCC recomputation of the onboard test;
- controller display cadence or latency.

Historical stochastic LR measurement generation therefore remains BLOCKED.

## Documentation synchronized

- landing-radar model proof;
- focused landing-radar roadmap;
- landing-radar station research status;
- Apollo 11 / Luminary 1A source catalog;
- this progress record.

## Next discriminating evidence

Continue the LM-5/Apollo-11 qualification/flight-data thread for actual residual distributions, bias, correlation, and quantization. Separately, seek Apollo-11-effective evidence for the controller-visible consequence of an onboard LR reasonableness rejection and for MSK-1137 per-field routing.

## Evidence status

**DOCUMENTED APOLLO-11-SPECIFIC ONBOARD MEASUREMENT-ADMISSION CRITERIA; SENSOR STOCHASTIC PROCESS AND CONTROLLER-VISIBLE CONSEQUENCE REMAIN UNRESOLVED.**
