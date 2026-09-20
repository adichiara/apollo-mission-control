# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-19

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References `Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program`, Flight Software Branch, Flight Support Division, May 1969 | Primary mission-period evidence for the Luminary 1A equation document. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Complete re-issue of `69-FS-3` updated for Luminary 1B | Bibliographic/change-control evidence; not automatic Apollo 11 equation authority. |
| LUMINARY 099 `SERVICER.agc` | `SETPOS1` selects position-1 alpha/beta; `SETPOS2` selects position-2; `HIGATJOB` waits for physical position-2 success, recomputes beams, then enables LR reads. `SETPOS` transforms antenna UNITY/UNITX to NB and cross-products the third velocity beam. `RDGIMS` captures measurement epoch/CDUs/PIPAs; `VELUPDAT` applies measurement-time `*NBSM*`, propagation, qualification, and update. | Apollo-11-effective stage order and discrete antenna-position authority; no continuous slew model. |
| LUMINARY 099 `POWERED_FLIGHT_SUBROUTINES.agc` | `AX*SR*T` consumes sine/cosine state in Y-Z-X order; `-3` selects SM→NB and `+3` NB→SM; `*NBSM*` reuses prepared trig state | Apollo-11-effective transform contract. |
| MIT Apollo `Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc` | Primary predecessor `SMNB` rotates Y→Z→X; `NBSM` reverses X→Z→Y; `AXISROT` gives explicit arithmetic | Algorithmic lineage/sign oracle only; not Apollo-11 constant authority. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | `HBEAMANT = (-.4687018041, 0, -.1741224271)` | Apollo-11-effective fixed range-beam geometry. |
| LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969 | `LRALPHA/LRBETA` are antenna→NB rotations, beta then alpha, negatives of R-567 angles | Primary Apollo-11-period polarity/order authority. |
| `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load, Table LM5/4.5.1-1 | Addresses 2522–2525: `LRALPHA1=0.0163371759 rev` and `LRBETA1=0.0665287037 rev` (stow); `LRALPHA2=0.0161680555 rev` and `LRBETA2=0.0001361111 rev` (hover). Also supplies `LRVMAX`, `LRVF`, `LRWV*`, `LRWVF*`, `LRWVFF`. | Mission/configuration authority. Store geometry in source units; convert only at executable adapter boundary. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* — lunar-descent state-vector section | Average-G/PIPA 2-second intervals; one LR velocity component per interval, cycling `Vz, Vx, Vy, Vz` | Onboard cadence only; not MCC display cadence. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* — ASPO 45 CRT MSK-1137 definitions (PDF 205–207 in the repository's inspected scan) | `LR RNG` and `VEL` GOOD/BAD; `VXB/VYB/VZB` LR velocity in body-axis coordinates at `±XXXX FT/SEC`; LR slant range `XXXXX FT`; PGNS altitude `XXXXX FT`; `ACT ΔV` explicitly ground computed | Apollo-11-specific controller-visible field semantics/formatting. Does not establish CRT refresh cadence or complete downlink/ground routing. Do not substitute Apollo 13 MSK-1137 stable-member/residual semantics. |
| Direct Apollo 11 / Apollo 13 MSK-1137 comparison, research note 030 | Same display identifier but mission-specific changes in LR coordinate frame, altitude/comparison semantics, and other fields | Requires mission-specific display profiles; shared display number is not evidence of shared field contract. |
| NASA TN D-6849 | LM-5 bias correction and qualitative non-Gaussian/near-zero-Doppler error boundary | No numerical flight-effective stochastic distribution. |
| MIT/IL E-1982 | 1966 design-study statistical LR error/weighting assumptions | Design-history only. |

## Current result

The Apollo 11 profile carries the exact LM-5 position-1/position-2 angle loads in revolutions and exposes a provenance-bearing adapter that converts the selected pair to radians and combines it with explicit measurement-time CDUs. This feeds the verified SETPOS/NBSM estimator chain without manual historical-constant transcription.

Controller-visible **formatting is now partially controlled** at the mission-specific MSK-1137 field-definition level: the LR validity fields, body-axis velocity frame, engineering units/display masks, slant range, PGNS altitude, and ground-computed identity of `ACT ΔV` are directly documented. Exact Apollo 11 downlink/ground routing and CRT timing remain unresolved.

Historical stochastic LR generation remains **BLOCKED**.

## Effectivity rule

Do not back-project Luminary 1B/1C or later behavior into Apollo 11 without controlled comparison. `Sunburst37` is used only as an algorithmic lineage/sign cross-check; Apollo-11-effective interfaces and constants remain controlled by LUMINARY 099, Memo #95, and LM-5 sources. Likewise, do not back-project Apollo 13 MSK-1137 stable-member landing-radar velocity or residual semantics into Apollo 11 merely because the display number is unchanged.

## Sources

- https://ibiblio.org/apollo/Documents/Mission_G_Rendezvous.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
- https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/POWERED_FLIGHT_SUBROUTINES.agc.html
- https://www.ibiblio.org/apollo/listings/Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc.html
- https://www.ibiblio.org/apollo/listings/Luminary099/CONTROLLED_CONSTANTS.agc.html
- https://www.ibiblio.org/apollo/Documents/LUM95_text.pdf
- https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- `resources/research/030_apollo11_apollo13_msk1137_comparison.md`
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- https://www.ibiblio.org/apollo/Documents/E-1982_LEM_PGNCS_and_Landing_Radar_Operations.pdf

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** equation-level LM-5 profile geometry + SETPOS + measurement-time NBSM velocity-beam path through the estimator.
- **DOCUMENTED:** discrete position-1/position-2 selection and recomputation behavior.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point equivalence.
- **DOCUMENTED:** one LR velocity component per 2-second Average-G/PIPA interval.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR status/velocity/range/PGNS-altitude field semantics, body-axis velocity frame, units, and display masks; `ACT ΔV` is explicitly ground computed.
- **UNRESOLVED / BLOCKED:** numerical stochastic Apollo-11-effective LR error distribution.
- **UNRESOLVED:** exact Apollo 11 downlink/ground routing and controller-display cadence, latency, freshness, and request workflow.
