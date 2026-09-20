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
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* — ASPO 45 CRT MSK-1137 definitions | `LR RNG` and `VEL` GOOD/BAD; `VXB/VYB/VZB` LR velocity in body-axis coordinates at `±XXXX FT/SEC`; LR slant range `XXXXX FT`; PGNS altitude `XXXXX FT`; `ACT ΔV` explicitly ground computed | Apollo-11-specific controller-visible field semantics/formatting. Does not establish CRT refresh cadence or complete downlink/ground routing. |
| NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11 — Mission Support | MCC functions through distinct CCATS, RTCC, Voice Communications, Display/Control, and MOCR/SSR elements; telemetry/operational data can be processed by CCATS and RTCC for flight-control evaluation | Apollo-11-effective architecture authority. Supports a layered spacecraft/downlink → ground processing → display model, not exact per-field routing or timing. |
| Sullivan & Burbank, *Apollo Experience Report: Real-Time Display System*, NASA-TN-D-8316 / JSC-S-461 | Apollo real-time display system organized into distinct computer-input multiplexer, plotting, digital-display, and digital-television subsystems | Retrospective architecture cross-check only; not Apollo-11 MSK-1137 cadence or field-routing authority. |
| Costis, Ortolani & Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, 24 Dec 1969 | Mission-specific display/control usage study; archival citation locates it in Box 078-65/66, Mission Documents: Apollo 11, JSC History Collection, University of Houston-Clear Lake | **BLOCKED:** no public digital copy located; do not claim exact request/timing semantics without direct inspection. |
| HAER TX-109-C, *Johnson Space Center, Apollo Mission Control* | Government historical report cites PHO-TN401 and reports aggregate Apollo 11 display-request/use statistics | Secondary/indirect evidence only; useful for system-level usage, not exact GUIDO keys, per-field cadence, latency, or format selection. |
| Direct Apollo 11 / Apollo 13 MSK-1137 comparison, research note 030 | Same display identifier but mission-specific changes in LR coordinate frame, altitude/comparison semantics, and other fields | Requires mission-specific display profiles. |
| NASA TN D-6849 | LM-5 bias correction and qualitative non-Gaussian/near-zero-Doppler error boundary | No numerical flight-effective stochastic distribution. |
| MIT/IL E-1982 | 1966 design-study statistical LR error/weighting assumptions | Design-history only. |

## Current result

The Apollo 11 profile carries the exact LM-5 position-specific geometry and verified estimator chain. Controller-visible formatting is partially controlled by mission-specific MSK-1137 definitions.

The ground/display architecture is controlled at the system-boundary level: Apollo 11 documentation separates telemetry/communications, CCATS/RTCC processing, Display/Control, and controller operations. This prohibits direct authoritative-state aliasing in an eventual Apollo 11 controller product. It is not sufficient to invent the exact CCATS/RTCC transformation for each LR field or a numeric CRT refresh period.

The strongest identified Apollo-11-specific display-usage source, PHO-TN401, is now a documented **BLOCKED** archival retrieval rather than an unclassified gap. Historical stochastic LR generation remains **BLOCKED** separately.

## Effectivity rule

Do not back-project later Luminary or Apollo 13 display semantics into Apollo 11. Do not convert the documented onboard 2-second LR component schedule into an MCC refresh/freshness rule. Do not convert HAER aggregate PHO-TN401 statistics into exact station workflow. Ground-processing and display stages remain explicit even where their exact Apollo-11 timing is unresolved.

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
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionOpReport.pdf
- https://ntrs.nasa.gov/citations/19760024152
- https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf
- `resources/research/334_apollo11_display_usage_source_retrieval_status.md`
- `resources/research/030_apollo11_apollo13_msk1137_comparison.md`
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- https://www.ibiblio.org/apollo/Documents/E-1982_LEM_PGNCS_and_Landing_Radar_Operations.pdf

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** equation-level LM-5 profile geometry + SETPOS + measurement-time NBSM velocity-beam path through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR semantics/formatting at the recorded field-definition level.
- **DOCUMENTED:** Apollo 11 MCC architectural separation of CCATS/RTCC processing, Display/Control, and controller operations.
- **DOCUMENTED:** Apollo-wide real-time display subsystem separation, used only as an architecture cross-check.
- **DOCUMENTED:** PHO-TN401 identity and archival location; HAER-derived aggregate usage is indirect evidence.
- **BLOCKED:** direct PHO-TN401 inspection; numerical stochastic Apollo-11-effective LR error distribution.
- **UNRESOLVED:** exact per-field Apollo 11 CCATS/RTCC transformation/routing, CRT cadence, end-to-end latency, freshness policy, GUIDO request/key workflow, and powered-descent display selection.