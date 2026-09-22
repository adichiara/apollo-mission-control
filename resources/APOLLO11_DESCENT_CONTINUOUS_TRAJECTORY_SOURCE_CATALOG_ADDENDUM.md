# Apollo 11 continuous-descent trajectory source-catalog addendum

Date: 2026-09-22
Parent: `resources/APOLLO11_DESCENT_TRAJECTORY_RULES_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA TM X-58038, *Development of Guidance-Monitoring Techniques and Guidance-Monitoring Experience During the Apollo 11 Lunar Descent* (1970), NTRS 19700023940 | Apollo 11 descent ground-tracking/guidance-monitoring architecture; independent ground-derived information compared with onboard guidance sources through descent. | Primary technical/postflight source for monitoring architecture. Does not supply a complete continuous vehicle state history or exact Mission-G display reconstruction. |
| NASA TN D-7143, *Apollo Experience Report: Descent Propulsion System* (1973), NTRS 19730011150 | DPS design/operation: throttleable, gimbaled, pressure-fed descent engine; guidance/navigation interface; Apollo operational experience. | Primary NASA engineering source for reusable DPS physics/architecture. Post-program and not an Apollo-11-specific continuous time history. |
| NASA lunar-descent guidance technical documentation, NTRS 19710015566 | P63 braking, P64 approach, P65 automatic landing, P66 manual landing; computer/crew control relationships and throttle/descent-rate behavior. | Primary technical source for guidance-mode semantics. Do not infer exact Apollo 11 switch times or arbitrary-time state values beyond mission-specific evidence. |
| NASA TM-20220007267, Miller et al., *Reconstruction of the Apollo 11 Moon Landing Final Descent Trajectory* (2022), NTRS 20220007267 | States that archival/open-literature data are insufficient for direct final-descent reconstruction; derives a trajectory using digitized graphics and estimation methods. | Secondary/later NASA reconstruction. Useful for reconstruction methodology and evidence-limit boundary only. Any adopted fitted path must be labeled RECONSTRUCTED, not DOCUMENTED primary-source truth. |

## Source URLs

- https://ntrs.nasa.gov/citations/19700023940
- https://ntrs.nasa.gov/citations/19730011150
- https://ntrs.nasa.gov/api/citations/19710015566/downloads/19710015566.pdf
- https://ntrs.nasa.gov/citations/20220007267

## Evidence status

**PARTIALLY DOCUMENTED.** Primary sources establish the causal guidance/propulsion/monitoring architecture. Exact continuous Apollo 11 as-flown state history remains unresolved; the available modern NASA trajectory reconstruction is explicitly an estimate and must retain that provenance.
