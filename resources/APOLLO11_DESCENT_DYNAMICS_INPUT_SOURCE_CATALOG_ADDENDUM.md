# Apollo 11 descent dynamics input source-catalog addendum

Date: 2026-09-22
Parent: `resources/APOLLO11_DESCENT_CONTINUOUS_TRAJECTORY_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA TN D-7143, *Apollo Experience Report: Descent Propulsion System* (1973), NTRS 19730011150 | DPS design requirements include 10:1 throttling ratio, 10,500-lbf maximum-rated thrust, ±6° gimbal capability, pressure feed, hypergolic propellants, and 305 lbf-sec/lbm end-of-duty-cycle specific impulse. | Primary NASA engineering source for design envelope and parameter semantics. Do not represent design requirements as LM-5 delivered-flight thrust/Isp history. |
| *Apollo 11 Press Kit* (1969), NASA historical archive | LM-5 launch weight 33,205 lb; dry ascent stage 4,804 lb; dry descent stage 4,483 lb; RCS propellant 604 lb; DPS propellant 18,100 lb; APS propellant 5,214 lb. | Contemporary primary mission documentation for launch bookkeeping. Not PDI mass; do not substitute for an epoch-specific descent initial state. |
| *Apollo 11 Mission Report* (MSC-00171, Nov. 1969) | Powered descent lasted 756.3 s; DPS propellant usage exceeded prediction because of additional landing-site redesignation time. | Primary postflight mission source for event/checkpoint validation. Does not by itself supply a continuous delivered throttle/thrust history. |
| TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume 1* (16 Mar. 1970), §7.2.3.1 | Original powered-descent BET used a fit to low-speed MSFN data from revolution-14 acquisition through touchdown and a landing-site constraint. A subsequent reconstruction combined onboard + high-speed MSFN data with pre-PDI relative tracking to produce a consistent continuous LM trajectory from DOI through touchdown. | Mission-specific NASA-contractor postflight reconstruction. Use as **RECONSTRUCTED** trajectory reference/validation evidence. Do not label as raw telemetry, exact physical truth, PDI mass evidence, or delivered DPS thrust/Isp history. |

## Source URLs

- https://ntrs.nasa.gov/citations/19730011150
- https://www.nasa.gov/wp-content/uploads/static/history/afj/ap11fj/pdf/a11-press-kit2.pdf
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- https://ntrs.nasa.gov/citations/19700014995
- https://www.ibiblio.org/apollo/Documents/19700014995_1970014995.pdf

## Evidence status

**PARTIALLY DOCUMENTED.** Design envelope, LM-5 launch resource bookkeeping, powered-descent duration, and a mission-specific postflight DOI→touchdown trajectory reconstruction are documented. The continuous trajectory is explicitly reconstructed. Apollo-11-specific PDI mass and continuous delivered DPS thrust/Isp history remain unresolved.