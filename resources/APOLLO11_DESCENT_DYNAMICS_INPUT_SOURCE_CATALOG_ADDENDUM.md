# Apollo 11 descent dynamics input source-catalog addendum

Date: 2026-09-22
Parent: `resources/APOLLO11_DESCENT_CONTINUOUS_TRAJECTORY_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA TN D-7143, *Apollo Experience Report: Descent Propulsion System* (1973), NTRS 19730011150 | DPS design requirements include 10:1 throttling ratio, 10,500-lbf maximum-rated thrust, ±6° gimbal capability, pressure feed, hypergolic propellants, and 305 lbf-sec/lbm end-of-duty-cycle specific impulse. | Primary NASA engineering source for design envelope and parameter semantics. Do not represent design requirements as LM-5 delivered-flight thrust/Isp history. |
| *Apollo 11 Press Kit* (1969), NASA historical archive | LM-5 launch weight 33,205 lb; dry ascent stage 4,804 lb; dry descent stage 4,483 lb; RCS propellant 604 lb; DPS propellant 18,100 lb; APS propellant 5,214 lb. | Contemporary primary mission documentation for launch bookkeeping. Not PDI mass; do not substitute for an epoch-specific descent initial state. |
| *Apollo 11 Mission Report* (MSC-00171, Nov. 1969) | Powered descent lasted 756.3 s; DPS propellant usage exceeded prediction because of additional landing-site redesignation time. | Primary postflight mission source for event/checkpoint validation. Does not by itself supply a continuous delivered throttle/thrust history. |
| TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume I* (16 Mar. 1970), foreword; §§7.2.1, 7.2.3.1, 7.3.3, 7.4.1 | Volume I documents the DOI→touchdown reconstruction method and data sources. It states that Volume II contains the 45-day BET listing in NASA Apollo Trajectory (NAT) format and was not generally distributed. Section 7.4.1 compares RTCC, low-speed MSFN, onboard, BET #3, Lear high-speed MSFN, and onboard/MSFN high-speed solutions. Lear used 10 samples/s over a 232-s pre-PDI arc; the combined HOPE solution used compacted high-speed Doppler, CSM sextant/VHF data, and telemetered acceleration in the IGS burn model. Section 7.3.3 defines the CSM-centered UVW-type axes for its relative-trajectory comparison figures. | Mission-specific NASA-contractor primary postflight analysis. Use Volume I to document **RECONSTRUCTED** provenance/methodology and comparison semantics. Do not fabricate the Volume-II state listing from plots, assume its NAT frame/epoch from the UVW comparison frame, or label reconstructed states raw telemetry. |
| TRW Note 70-FMT-819, *Volume II* — 45-day Apollo 11 BET listing | Named by Volume I as the NAT-format state listing; not generally distributed, historically available from MSC Central Metric Data File. A targeted exact-title/report-number/accession search on 2026-09-22 recovered no public primary copy or traceable archival derivative. | **BLOCKED ON NAMED SOURCE RECOVERY.** Required before treating the official 45-day BET as a machine-usable state-series fixture unless a traceable archival derivative preserving NAT metadata is recovered. Broad web searching is exhausted; reopen on an archive/digitization lead. |
| NASA TN D-6846 / MSC-S-295, Floyd V. Bennett, *Apollo Experience Report: Mission Planning for Lunar Module Descent and Ascent* (June 1972), NTRS 19720018205 | Primary NASA synthesis of premission planning, real-time events, and postflight Apollo 11/12 analysis. For Apollo 11 it preserves the premission event table and thrust/attitude profile and the postflight comparison products, including guidance thrust command versus horizontal velocity, landing-radar updates, approach/landing trajectory, attitude, altitude-rate, and landing-phase events. The report states that flight results agreed with premission planning while documenting the landing-phase divergence associated with manual terrain avoidance. | Use as a source-backed **validation/checkpoint envelope** for modeled descent behavior. It does not convert a plotted/commanded thrust relationship into an exact delivered LM-5 thrust or Isp time series, and it does not supply the missing Volume-II NAT state listing. |

## Source URLs

- https://ntrs.nasa.gov/citations/19730011150
- https://www.nasa.gov/wp-content/uploads/static/history/afj/ap11fj/pdf/a11-press-kit2.pdf
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- https://ntrs.nasa.gov/citations/19700014995
- https://www.nasa.gov/wp-content/uploads/static/history/afj/ap11fj/pdf/19700014995_as11-trajectory-reconstruction-vol1.pdf
- https://www.ibiblio.org/apollo/Documents/19700014995_1970014995.pdf
- https://ntrs.nasa.gov/citations/19720018205
- https://ntrs.nasa.gov/api/citations/19720018205/downloads/19720018205.pdf

## Evidence status

**PARTIALLY DOCUMENTED.** Design envelope, LM-5 launch resource bookkeeping, powered-descent duration, reconstruction methodology/data sources, a mission-specific postflight DOI→touchdown reconstruction, and a primary NASA set of descent validation/checkpoint products are documented. The continuous trajectory is explicitly RECONSTRUCTED. The official 45-day BET state listing is **BLOCKED ON NAMED SOURCE RECOVERY (Volume II)** and broad online discovery has been exhausted. Apollo-11-specific PDI mass and continuous delivered DPS thrust/Isp history remain unresolved; TN D-6846 constrains validation behavior without closing those exact inputs.