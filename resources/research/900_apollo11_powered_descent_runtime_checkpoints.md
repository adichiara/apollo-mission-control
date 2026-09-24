# 900 — Apollo 11 powered-descent runtime checkpoints

Research thread: `apollo11-descent-runtime`

## Bounded question

Which primary-source trajectory, propulsion, and monitoring checkpoints can constrain the next Apollo 11 powered-descent runtime without inventing a continuous LM-5 force history or controller-visible data?

## Findings

NASA TM X-58040, *Apollo Lunar Descent and Ascent Trajectories* (Floyd V. Bennett, MSC, March 1970), supplies an operational skeleton.

- PDI coincides with DPS ignition near 50,000 ft and follows a 7.5-second RCS ullage burn.
- DPS ignition is at trim (10 percent) throttle, held for 26 seconds for gimbal alignment before fixed-throttle operation.
- The premission event table gives throttle-up at TFI 00:26, windows-up rotation at 02:56, LR altitude update at 04:18, throttle recovery at 06:24, LR velocity update at 06:42, high gate at 08:26, low gate at 10:06, and probe contact at 11:54.
- P-63 braking terminates when guidance TGO reaches 60 seconds, about 7,000 ft and TFI 8:25, with automatic transition to P-64.
- P-66 is crew-selected rate-of-descent guidance: crew controls attitude while the computer commands DPS throttle to maintain desired altitude rate.
- The postflight discussion places Apollo 11 P-66 manual takeover at about 410 ft with forward velocity about 50 ft/s.

The report also defines controller-relevant monitoring:

- controllers compare PGNCS, AGS, and MSFN-derived velocity with two-out-of-three logic;
- DPS/PGNCS performance is monitored with guidance thrust command (GTC) versus horizontal velocity, with GTC divergence tied to an abort rule;
- LR altitude-update availability and magnitude are monitored before incorporation;
- altitude and altitude-rate limits are monitored for abort capability, with ground advice based on projected trends because of communications delay.

## Runtime consequence

The source supports an event/checkpoint-constrained descent profile and explicit monitoring relationships. It does not justify digitizing the plotted thrust curve into an exact LM-5 force law, treating nominal fixed-throttle descriptions as calibrated as-flown values, exposing postflight values directly to controllers, collapsing PGNCS/AGS/MSFN/GTC/LR into one perfect state, or inventing unsupported latency/cadence/display routing.

## Closure challenge

A focused search did not recover a directly usable Apollo 11 LM-5 final DPS calibration/performance report. Later NASA DPS material is useful for subsystem context but is not a substitute for LM-5 calibration. This checkpoint/monitoring question is therefore sufficient for the bounded runtime; exact LM-5 continuous propulsion calibration remains separately unresolved.

## Sources

1. Floyd V. Bennett, NASA MSC, *Apollo Lunar Descent and Ascent Trajectories*, NASA TM X-58040, March 1970, NASA NTRS document 19700024568.
2. W. R. Hammock Jr., E. C. Currie, A. E. Fisher, *Apollo Experience Report: Descent Propulsion System*, NASA TN D-7143 / MSC-S-349, March 1973, NASA NTRS document 19730011150.

## Evidence status

- **DOCUMENTED:** the Apollo 11 premission descent event/checkpoint sequence and phase logic above are directly reported in NASA TM X-58040.
- **DOCUMENTED:** PGNCS/AGS/MSFN comparison, GTC monitoring, LR update monitoring, and altitude/altitude-rate abort monitoring are directly described there.
- **DOCUMENTED:** Apollo 11 P-66 manual takeover is reported at approximately 410 ft altitude and 50 ft/s forward velocity.
- **PARTIALLY DOCUMENTED:** plotted thrust history and nominal engine descriptions constrain shape and operating regions but do not establish a calibrated continuous LM-5 force history.
- **UNRESOLVED:** exact LM-5 as-flown thrust, specific impulse, mixture ratio, and uncertainty through the complete powered descent.
- **UNRESOLVED:** exact display routing, cadence, and precision for monitoring quantities beyond separately sourced station-product evidence.
