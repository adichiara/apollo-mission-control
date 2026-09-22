# Apollo 11 descent dynamics input source-catalog addendum

Date: 2026-09-22
Parent: `resources/APOLLO11_DESCENT_CONTINUOUS_TRAJECTORY_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA TN D-7143, *Apollo Experience Report: Descent Propulsion System* (1973), NTRS 19730011150 | DPS design requirements include 10:1 throttling ratio, 10,500-lbf maximum-rated thrust, ±6° gimbal capability, pressure feed, hypergolic propellants, and 305 lbf-sec/lbm end-of-duty-cycle specific impulse. | Primary NASA engineering source for design envelope and parameter semantics. Do not represent design requirements as LM-5 delivered-flight thrust/Isp history. |
| *Apollo 11 Press Kit* (1969), NASA historical archive | LM-5 launch weight 33,205 lb; dry ascent stage 4,804 lb; dry descent stage 4,483 lb; RCS propellant 604 lb; DPS propellant 18,100 lb; APS propellant 5,214 lb. | Contemporary primary mission documentation for launch bookkeeping. Not PDI mass. |
| *Apollo 11 Final Flight Plan* (1 July 1969), table 5-5 | SPS-budget assumptions specify LM (unmanned) **33,278.3 lb** and lunar-orbit CSM→LM weight transfer **436.7 lb** (with LM→CSM transfer separately 284.0 lb). | Primary mission planning/configuration bookkeeping. These states prove that simple launch-weight substitution is invalid, but do not themselves establish PDI mass. Do not add transfer values mechanically to manufacture a PDI state. |
| **SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968**, *CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties* (base revision 20 Aug. 1969), NTRS 19730060772 | NASA states that Volume III provides per-mission spacecraft mass properties and consumable loading. The base revision covers G/H/J mission data. The surviving digitized binder, however, includes later replacement pages: indexed section 3 material is marked **Amendment 86, 9/10/70**, and an indexed table 3.1-8 page is **Amendment 110, 7/19/71** and identifies **LM-10**. | **PRIMARY SOURCE FAMILY, BUT PUBLIC SCAN IS AMENDMENT-OVERWRITTEN.** Do not infer Mission-G applicability from section/table number or title-page revision date alone. |
| **Apollo 11 Mission Report, MSC-00171 (Nov. 1969), Appendix A.6 / table A-I** | NASA says these mass properties are postflight values based on expendable loadings/usage and measured spacecraft/stage weights updated for changes. LM event rows: **33,683.5 lb separation; 33,669.6 lb DOI ignition; 33,401.6 lb DOI cutoff; 16,153.2 lb lunar landing**. | **PRIMARY MISSION-SPECIFIC POSTFLIGHT MASS CHECKPOINTS.** No PDI row is present; do not relabel DOI values as PDI. |
| NASA SP-4029, *Apollo by the Numbers* | Cross-mission table places **33,669.6 lb** under Apollo 11 `LM at Powered Descent Initiation` and **33,401.6 lb** under `LM at Descent Orbit Insertion Ignition`. | **SECONDARY CONFLICT / DO NOT USE FOR PDI CLOSURE.** Primary Mission Report assigns those exact values to DOI ignition and DOI cutoff. Preserve primary event identity. |
| *Apollo 11 Mission Report* §9.8 and fig. 9.8-1 | Powered descent lasted 756.3 s for about 6775 ft/s velocity change. Engine began at 13% minimum throttle and was advanced to full throttle after about 26 s; a roughly 45-s data dropout occurred. Figure 9.8-1 records flight throttle position, chamber pressure, regulator outlet pressure, and fuel/oxidizer interface pressures versus mission time. | Primary postflight as-flown propulsion evidence. Use measured/telemetry relationships for validation; do not infer an exact delivered thrust/Isp history. |
| *Apollo 11 Mission Report Supplement 7: Descent Propulsion System Final Flight Evaluation* (Sep. 1970) | Later primary NASA supplement tables identify Apollo 11 Supplement 7 by exact title and publication date. | **BLOCKED ON NAMED SOURCE RECOVERY.** Highest-value named source for mission-specific DPS performance. Do not infer its contents from neighboring missions. |
| TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume I* (16 Mar. 1970) | Documents DOI→touchdown reconstruction method/data sources and states that Volume II contains the 45-day BET listing in NASA Apollo Trajectory format. | Use for **RECONSTRUCTED** provenance/methodology. Do not fabricate Volume-II states or label reconstructed states raw telemetry. |
| TRW Note 70-FMT-819, *Volume II* — 45-day Apollo 11 BET listing | Named by Volume I as NAT-format state listing; not generally distributed. | **BLOCKED ON NAMED SOURCE RECOVERY.** Broad web searching exhausted; reopen on archive/digitization lead. |
| NASA TN D-6846 / MSC-S-295, Floyd V. Bennett, *Apollo Experience Report: Mission Planning for Lunar Module Descent and Ascent* (June 1972), NTRS 19720018205 | Preserves Apollo 11 premission/postflight descent event, trajectory, guidance thrust-command, radar-update, attitude, altitude-rate, and landing-phase products. | Source-backed validation/checkpoint envelope; not exact delivered LM-5 thrust/Isp or missing BET states. |

## Source URLs

- https://ntrs.nasa.gov/citations/19730011150
- https://www.nasa.gov/wp-content/uploads/static/history/afj/ap11fj/pdf/a11-press-kit2.pdf
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/a11final-fltpln.pdf
- https://ntrs.nasa.gov/citations/19730060772
- https://ntrs.nasa.gov/api/citations/19730060772/downloads/19730060772.pdf
- https://www.ibiblio.org/apollo/Documents/SNA-8-D-027III-Rev2-CsmLmSpacecraftOperationalDataBook-Volume3-MassProperties.pdf
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- https://www.nasa.gov/wp-content/uploads/2023/04/sp-4029.pdf
- https://ntrs.nasa.gov/citations/19700014995
- https://ntrs.nasa.gov/citations/19720018205

## Evidence status

**PARTIALLY DOCUMENTED.** Mission-specific postflight LM masses are now primary-source documented at separation, DOI ignition, DOI cutoff, and landing. Exact PDI mass remains unresolved. NASA SP-4029's apparent Apollo 11 PDI value is explicitly rejected for closure because its event assignments conflict with the primary Mission Report. The official BET Volume II and Apollo 11 DPS Supplement 7 remain **BLOCKED ON NAMED SOURCE RECOVERY**. Exact delivered thrust/Isp remain unresolved.