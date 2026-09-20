# Progress — Apollo 11 landing-radar flight-error boundary

Date: 2026-09-20

## Work completed

The next unresolved landing-radar error item was checked against primary NASA Apollo-program evidence rather than filled with a synthetic distribution.

NASA TN D-6849, *Apollo Experience Report: Lunar Module Landing Radar and Rendezvous Radar*, reports that the LM-5 landing radar performed well during Apollo 11 descent and landing. The flight data appeared well within specification limits except for a few points at low velocities near zero Doppler shift, where the landing radar was not expected to track. The report states that two questionable data points were probably caused by poor data processing during the LGC overload alarm.

This is stronger than a generic specification statement because it describes observed Apollo 11 behavior. It establishes a localized low-velocity/near-zero-Doppler validity boundary and identifies an LGC-overload-associated processing caveat.

## Result

The repository may use this evidence to test that a historical implementation does not claim uniformly valid LR tracking through the near-zero-Doppler region. It may also represent the documented existence of questionable samples associated with the overload episode when reproducing source-described mission state.

It may **not** infer from this source:

- a dropout probability;
- a Gaussian or other probability distribution;
- sample-to-sample correlation;
- a numerical bias outside the separately documented corrected preflight one-count defect;
- an alarm-triggered corruption algorithm;
- exact controller-visible symptoms or timing.

The stochastic process therefore remains BLOCKED. The new evidence narrows the block rather than closing it.

## Documentation synchronized

- focused landing-radar roadmap;
- landing-radar station research status;
- Apollo 11 / Luminary 1A source catalog;
- this progress record.

## Next discriminating evidence

Continue with LM-5 qualification/acceptance or Apollo 11 flight-data reduction material that numerically characterizes actual LR residuals, quantization, correlation, dropout, or bias. In parallel, the roadmap's implementation target remains independent verification of the Apollo-11-effective `SETPOS` antenna-to-NB and `*NBSM*` measurement-time transforms.

## Evidence status

**DOCUMENTED APOLLO 11 FLIGHT BEHAVIOR; STOCHASTIC PROCESS STILL BLOCKED.** The observed exception is source-controlled without inventing a probability law or failure mechanism.
