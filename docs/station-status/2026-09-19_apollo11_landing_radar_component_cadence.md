# Station research status — Apollo 11 landing-radar cadence and display boundary

Date: 2026-09-20

## GUIDO / guidance-monitoring consequence

The onboard PGNCS landing-radar estimator timing is constrained to one LR velocity component during each 2-second Average-G/PIPA interval, cycling `Vz`, `Vx`, `Vy`. Mission-specific MSK-1137 evidence constrains the controller-visible LR field family: GOOD/BAD range/velocity status, body-axis `VXB/VYB/VZB`, slant range, PGNS altitude, display masks, and separately ground-computed `ACT ΔV`.

Apollo 11 ground-system evidence constrains the intervening CCATS/RTCC and Display/Control layers. NASA TN D-8316 establishes buffered dynamic display updates independent of CRT refresh. PHO-FAM001 constrains the generic request transaction, and NASA TN D-7685 constrains Apollo-program display-request/channel-allocation behavior.

The Apollo-11-effective AC Electronics MSK-1137 format shows explicit `D/L` and `RTCC` source-category labeling. Together with the field note identifying `ACT ΔV` as ground computed, this establishes a controller product mixing spacecraft-downlink and ground/RTCC provenance, but not the per-field routing table.

The Apollo 11 Mission Report assigns LR incorporation to the crew based on reasonability/precalculated limits and convergence verification. MIT R-700 Vol. II supplies the Apollo-11-specific onboard reasonableness criteria: velocity `|delta q| <= 7.5 + 0.125 V_T` ft/s and range-derived altitude `|delta q| <= 200 + 0.125 h` ft, with the altitude test omitted above high gate. These do not justify a GUIDO accept/reject control.

NASA TN D-6849 adds a useful hardware-interface boundary. It states that processed LR velocity and slant-range information was supplied to the **LGC in serial binary form**, while LR information was separately supplied to **LM displays as pulse trains and dc analog voltages**. Thus the spacecraft's LGC measurement input and local crew-display electrical output are distinct paths. This does not identify the MCC telemetry/downlink field mapping, and the local LM display path must not be treated as the source of MSK-1137 without separate evidence.

TN D-6849 also reports LM-5 LR data generally within specification except for a few low-velocity points near zero Doppler, with two questionable samples probably associated with processing during the LGC overload alarm. This constrains validation but not a numerical random-error process.

PHO-TR515 remains a later primary-system baseline for provenance representation only; its 1973 identifiers and update-rate fields are not back-projected into Apollo 11.

## Station boundary

`LR physical measurement/error → LR processed output → serial-binary LGC path → LGC reasonableness admission → LGC estimator/update → crew reasonability/acceptance + convergence state → downlink/telemetry → CCATS/RTCC source/computation/logic → Display/Control dynamic-field formatting → TV-channel allocation/attach → controller-visible field`

A separate spacecraft-local branch exists from LR processed output to LM displays via pulse trains/dc analog voltages. Do not conflate that local branch with either the LGC serial path or the MCC/MSK-1137 path.

Keep spacecraft acceptance, field provenance, dynamic-data update, CRT refresh, operator format request, TV-channel allocation, and station-specific controls separate.

## Maturity

No station maturity change. Mission-specific onboard measurement-admission gates, mixed provenance, crew LR-acceptance/convergence workflow, Apollo 11 sensor-flight exceptions, and the LR's separate LGC/local-display output architecture are established. Apollo-11-effective per-field source mapping is still required before claiming exact MSK-1137 routing or timing.

## Evidence status

- **DOCUMENTED:** onboard LGC LR velocity-component update schedule and Apollo 11 MSK-1137 field semantics.
- **DOCUMENTED:** Apollo-11-specific onboard LR velocity/altitude reasonableness criteria and high-gate altitude-test omission; not an MCC/GUIDO display rule.
- **DOCUMENTED:** Apollo 11 MSK-1137 distinguishes `D/L` and `RTCC` provenance categories; `ACT ΔV` is ground computed.
- **DOCUMENTED:** Apollo 11 Mission Report assigns LR incorporation to the crew; AGS was not LR-updated.
- **DOCUMENTED, APOLLO-PROGRAM HARDWARE / LM-5 EXPERIENCE SOURCE:** LR velocity/range goes to LGC in serial binary form and separately to LM displays as pulse trains/dc analog voltages.
- **DOCUMENTED, APOLLO 11 FLIGHT EXPERIENCE:** LR generally within specification, with localized near-zero-Doppler exceptions and two questionable samples probably associated with LGC-overload processing.
- **DOCUMENTED:** Apollo MCC processing/display separation and buffered D/TV update behavior.
- **DOCUMENTED, LATER SYSTEM BASELINE:** PHO-TR515 metadata model; not Apollo 11 field mapping or cadence.
- **BLOCKED:** direct PHO-TN401 inspection; flight-authentic numerical LR stochastic error generation.
- **UNRESOLVED:** per-field Apollo 11 MSK-1137 `D/L`/`RTCC` mapping, external-name/downlist/computation identifiers, GUIDO exact request controls and descent selection, controller-visible consequence of onboard reasonableness rejection, numeric dynamic-data cadence/latency/freshness, and LM-5 serial word bit weighting/quantization/transfer behavior.
