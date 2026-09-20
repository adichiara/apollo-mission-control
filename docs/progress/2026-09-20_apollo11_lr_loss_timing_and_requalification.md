# Progress — Apollo 11 LR loss timing and requalification

Date: 2026-09-20

## Work completed

The next unresolved landing-radar item was the duration/shape boundary around the two Apollo 11 zero-Doppler tracking losses. Primary NASA mission evidence closes the event-table duration at one-second resolution.

Apollo 11 Mission Report table 5-I records:

- `Landing radar data not good` — 102:44:11
- `Landing radar data good` — 102:44:21
- `Landing radar data not good` — 102:44:59
- `Landing radar data good` — 102:45:03

Thus the report supports historical replay intervals of 10 seconds and 4 seconds at its one-second event resolution. The report narrative separately attributes the two brief losses to expected zero-Doppler effects associated with manual maneuvering.

The Apollo 11 AC Electronics guidance manual supplies an important second constraint: the LR `DATA GOOD` discrete must have been continuously present for at least four seconds before range/velocity measurement tests permit state-vector updating. Reacquisition and renewed filter eligibility are therefore distinct states.

## Result

The prior statement that no duration evidence existed is narrowed. Historical Apollo 11 replay may use the two recorded not-good/good intervals as deterministic event anchors, while preserving the report's timing resolution. After each `DATA GOOD` return, onboard LR-aided updating must remain separately gated by the documented four-second qualification rule.

This does **not** establish:

- sub-second transition timing;
- a random dropout probability or duration distribution;
- a stochastic zero-Doppler error law;
- exact maneuver kinematics producing either loss;
- controller-visible display symptoms or callouts;
- MCC display cadence.

Historical stochastic LR generation remains BLOCKED.

## Documentation synchronized

- focused landing-radar roadmap;
- landing-radar station research status;
- Apollo 11 / Luminary 1A source catalog;
- this progress record.

## Next discriminating evidence

Continue seeking LM-5/Apollo 11 flight-data reduction or qualification material for numerical residuals, bias, quantization, correlation, and any timing finer than the Mission Report event table. Separately continue Apollo-11-effective MSK-1137 per-field routing and GUIDO-control research.

## Evidence status

**DOCUMENTED APOLLO 11 EVENT TIMING + ONBOARD REQUALIFICATION RULE; STOCHASTIC PROCESS STILL BLOCKED.** The two flight interruptions are bounded at one-second event-table resolution, and reacquired data must satisfy the independently documented four-second `DATA GOOD` qualification before LR measurement tests permit state-vector updating.
