# Progress — Apollo 11 landing-radar discrete tracking losses

Date: 2026-09-20

## Work completed

The next unresolved landing-radar behavior item was checked against the primary NASA *Apollo 11 Mission Report* rather than converted into a synthetic dropout model.

Section 9.11 states that landing-radar range and velocity were acquired at slant ranges of approximately 44,000 and 28,000 ft, respectively. It further states that the tracker was lost briefly at altitudes of 240 and 75 ft, and explicitly describes those losses as expected zero-Doppler effects associated with manual maneuvering.

This is more specific Apollo-11-effective evidence than the later TN D-6849 summary because it supplies two actual mission-event altitudes and the report's stated causal interpretation.

## Result

Historical scenario validation may now require the Apollo 11 LR path to permit the two source-described brief tracking-loss events at 240 and 75 ft when reproducing the corresponding descent history. The source also supports treating zero-Doppler/manual-maneuver geometry as the documented cause of those events.

It does **not** establish:

- the exact duration of either loss;
- a general dropout probability;
- a stochastic zero-Doppler error distribution;
- the exact maneuver kinematics that caused each loss;
- a controller-visible alarm, display symptom, or callout;
- a rule that all similar maneuvers must produce loss of track.

Accordingly, historical stochastic LR generation remains BLOCKED. The discrete Apollo 11 events are now documented separately from that unresolved process.

## Documentation synchronized

- focused landing-radar roadmap;
- landing-radar station research status;
- Apollo 11 / Luminary 1A source catalog;
- this progress record.

## Next discriminating evidence

Continue seeking LM-5 qualification/acceptance or Apollo 11 flight-data reduction material that numerically characterizes residuals, quantization, correlation, bias, or the duration/shape of the documented tracking interruptions. Separately continue the Apollo-11-effective MSK-1137 field-routing and GUIDO-control research threads.

## Evidence status

**DOCUMENTED APOLLO 11 FLIGHT EVENTS; STOCHASTIC PROCESS STILL BLOCKED.** Range/velocity acquisition and the two brief zero-Doppler tracking losses are source-controlled without inventing timing, probability, or controller behavior.
