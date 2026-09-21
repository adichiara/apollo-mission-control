# Apollo 11 LR convergence monitoring — source catalog addendum

Date: 2026-09-21
Parent: `resources/APOLLO11_DESCENT_TRAJECTORY_RULES_SOURCE_CATALOG_ADDENDUM.md`

| Source | Evidence used | Boundary |
| --- | --- | --- |
| Floyd V. Bennett, NASA MSC, *Apollo Lunar Descent and Ascent Trajectories*, NASA TM X-58040, March 1970 | Apollo 11 LR lock near 37,000 ft; Δh -2,200 ft; altitude-data incorporation near 31,600 ft; convergence to about 100 ft within 30 s; velocity updates near 29,000 ft. States that flight controllers and crew monitored altitude/altitude rate and that ground advice was based on projected trends because of communications delay. | Primary NASA postflight trajectory/operations evidence. Does not identify exact Mission-G CRT fields or station-specific voice ownership. |
| NASA MSC, *Apollo 11 Mission Report*, MSC-00171 / NASA TM X-62633, November 1969 | Event chronology: LR data good 102:37:51; radar updates enabled 102:38:45; velocity-update condition 102:38:50; P64 entry 102:41:32. | Primary mission report; supports event ordering, not exact ground display routing. |
| NASA MSC Flight Control Division, *Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)*, April 16, 1969 | Mission-effective LR acquisition/convergence/dropout and PGNS-vs-LR decision rules from the parent research thread. | Rule authority; does not itself identify the CRT/call implementation. |

## URLs

- NASA TM X-58040 NTRS record: https://ntrs.nasa.gov/citations/19700024568
- Apollo 11 Mission Report NTRS record: https://ntrs.nasa.gov/citations/19700008096
- Apollo 11 Flight Mission Rules scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf

## Catalog consequence

The repository now has primary evidence for the **flown LR convergence sequence** and the existence of a ground flight-controller trajectory-monitoring role. The parameter-level Mission-G display-routing question remains BLOCKED on its previously named archival artifacts; the station-specific voice/call workflow remains OPEN and is the next bounded research target.

## Evidence status

- **DOCUMENTED:** postflight LR sequence and ground trend-monitoring role.
- **UNRESOLVED:** exact Mission-G display/routing and named station call chain.