# Apollo 11 / Luminary 1A source-catalog addendum

Date: 2026-09-20

## Controlled source chain

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| Mission G rendezvous report | References *Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program*, May 1969 | Primary mission-period evidence for the Luminary 1A equation document. |
| MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B* | Complete re-issue of `69-FS-3` updated for Luminary 1B | Bibliographic/change-control evidence; not automatic Apollo 11 equation authority. |
| LUMINARY 099 `SERVICER.agc` | `SETPOS1/2`, measurement-epoch capture, beam transform, propagation, qualification, update | Apollo-11-effective stage order and discrete antenna-position authority. |
| LUMINARY 099 `POWERED_FLIGHT_SUBROUTINES.agc` | `AX*SR*T` Y-Z-X order and SM/NB direction semantics | Apollo-11-effective transform contract. |
| MIT Apollo `Sunburst37/INFLIGHT_ALIGNMENT_ROUTINES.agc` | Predecessor SM/NB rotation arithmetic | Algorithmic lineage/sign oracle only. |
| LUMINARY 099 `CONTROLLED_CONSTANTS.agc` | `HBEAMANT` fixed range-beam geometry | Apollo-11-effective geometry. |
| LUMINARY Memo #95, *Landing Radar Orientation* | `LRALPHA/LRBETA` antenna→NB rotations, beta then alpha | Apollo-11-period polarity/order authority. |
| `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch load | Position-specific `LRALPHA/LRBETA` plus LR weighting constants | Mission/configuration authority. |
| AC Electronics, *Apollo 11 Guidance and Navigation System Manual* | Average-G/PIPA 2-second LR component schedule; ASPO 45 MSK-1137 LR field definitions | Onboard cadence plus Apollo-11 controller field semantics. Onboard cadence is not MCC display cadence. |
| NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11 | Distinct CCATS, RTCC, Voice Communications, Display/Control, MOCR/SSR elements | Apollo-11-effective architecture authority; not exact per-field routing/timing. |
| Sullivan & Burbank, *Apollo Experience Report: Real-Time Display System*, NASA TN D-8316 | CIM requests carry requester/type/request fields; D/TV generators have random-access buffers; computer may update complete instruction lists or single data words independently of CRT refresh; reference-slide system had a four-second access/display requirement | Primary Apollo-wide display-system evidence. Separates operator request, dynamic-word update, CRT refresh, and reference-slide access. **Four seconds is not dynamic telemetry cadence.** |
| Costis, Ortolani & Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, 24 Dec 1969 | Mission-specific display/control usage study; archival citation locates Box 078-65/66, JSC History Collection, University of Houston-Clear Lake | **BLOCKED:** no public digital copy located; do not claim exact request/timing semantics without direct inspection. |
| HAER TX-109-C, *Johnson Space Center, Apollo Mission Control* | Government historical report cites PHO-TN401 and reports aggregate Apollo 11 display-request/use statistics | Secondary/indirect evidence only; not exact GUIDO keys, per-field cadence, latency, or format selection. |
| Direct Apollo 11 / Apollo 13 MSK-1137 comparison, research note 030 | Mission-specific differences in coordinate frame and field semantics | Requires mission-specific display profiles. |
| NASA TN D-6849 | LM-5 bias correction and qualitative non-Gaussian/near-zero-Doppler error boundary | No numerical flight-effective stochastic distribution. |
| MIT/IL E-1982 | 1966 design-study statistical LR error/weighting assumptions | Design-history only. |

## Current result

The Apollo 11 profile carries exact LM-5 position-specific geometry and a verified estimator chain. Controller-visible formatting is partially controlled by mission-specific MSK-1137 definitions. Ground/display architecture is controlled at the system-boundary level and prohibits direct authoritative-state aliasing.

TN D-8316 further closes an important false equivalence: dynamic data updates are buffered independently of CRT refresh, and the documented four-second figure applies to reference-slide access. No numeric Apollo 11 GUIDO/MSK-1137 dynamic update period is thereby established.

PHO-TN401 remains a documented **BLOCKED** archival retrieval. Historical stochastic LR generation remains **BLOCKED** separately.

## Effectivity rule

Do not back-project later Luminary or Apollo 13 display semantics into Apollo 11. Do not convert the onboard two-second LR schedule, the TN D-8316 four-second reference-slide requirement, or HAER aggregate PHO-TN401 statistics into an MCC dynamic-data refresh/freshness rule. Ground-processing, display selection, dynamic update, and presentation stages remain explicit where exact Apollo-11 timing is unresolved.

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
- `resources/research/030_apollo11_apollo13_msk1137_comparison.md`
- https://ntrs.nasa.gov/api/citations/19720016521/downloads/19720016521.pdf
- https://www.ibiblio.org/apollo/Documents/E-1982_LEM_PGNCS_and_Landing_Radar_Operations.pdf

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** equation-level LM-5 profile geometry + SETPOS + measurement-time NBSM velocity-beam path through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR semantics/formatting at recorded field-definition level.
- **DOCUMENTED:** Apollo 11 MCC architectural separation of CCATS/RTCC processing, Display/Control, and controller operations.
- **DOCUMENTED:** Apollo D/TV buffered-update behavior and separation of dynamic update from CRT refresh/reference-slide access.
- **DOCUMENTED:** PHO-TN401 identity and archival location; HAER-derived aggregate usage is indirect evidence.
- **BLOCKED:** direct PHO-TN401 inspection; numerical stochastic Apollo-11-effective LR error distribution.
- **UNRESOLVED:** exact per-field Apollo 11 CCATS/RTCC transformation/routing, numeric dynamic-data cadence/latency/freshness, GUIDO request/key workflow, and powered-descent display selection.