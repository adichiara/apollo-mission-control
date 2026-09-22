# Apollo 11 powered-descent phase source-catalog addendum

Date: 2026-09-21
Parent: `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA, *Apollo 11 Flight Plan, AS-506, CSM-107/LM-5*, final 1 Jul 1969 | Nominal powered-descent profile marking fixed throttle, LR updates, throttle recovery, high gate/P63→P64, low gate and touchdown; high-gate-to-touchdown panel provides nominal event/state anchors | Apollo-11-effective **planned** trajectory/phase authority. Do not promote nominal values to exact flown states or controller-visible fields without separate evidence. |
| NASA, *Apollo 11 Mission Report*, MSC-00171, Nov 1969, §9.8 | Flown powered descent 756.3 s, approximately 6775 ft/s delta-V; DPS starts at 13-percent minimum throttle and advances to full throttle after approximately 26 s; approximately 45 s early data dropout; P66 manual landing is initiated by crew control actions and retains computer throttle/descent-rate functions | Apollo-11 **flown/postflight** propulsion and P66 operational authority. The report's smoothed propulsion plot must not be treated as measured history through the dropout. P66 is not equivalent to loss of computer involvement or ground observation. |
| NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11, 24 Jun 1969 | Powered descent defined as braking, approach and landing phases; approach begins near 7,600 ft/high gate; landing begins at 500 ft/low gate | Mission-effective operational phase-definition authority; planned description, not exact flown transition state. |
| NASA, *Apollo 11 Flight Mission Rules*, Mission G, 16 Jul 1969, rule 5-11 | "There are no trajectory or guidance constraints which are cause for abort after crew takeover of powered descent." | Mission-effective rule authority for the P66/manual-takeover decision boundary. It changes trajectory/guidance abort-rule applicability; it does **not** erase observations or disable independently sourced systems/propellant criteria. |
| NASA TM X-58038, *Development of Guidance-Monitoring Techniques and Guidance-Monitoring Experience During the Apollo 11 Lunar Descent*, 1970 | Ground monitoring compared PGNS, AGS, and MSFN-derived tracking; terminal descent/manual takeover occurs near the 500-ft boundary and monitoring plots continue through the post-takeover interval | Primary NASA technical account supporting continued ground observation/comparison after manual takeover. Do not infer an exact Mission-G CRT field or unique GUIDANCE voice call from the report. |

## Current result

The Apollo 11 architecture reference can use a deterministic phase/event skeleton for powered descent while keeping nominal planning, flown propulsion evidence, hidden causal state, and controller-visible products separate. The P66/manual-control transition is now executable at the reusable decision-gate layer as a **rule-authority change without observation loss**. Continuous historical thrust/trajectory reconstruction and exact station product routing remain unresolved.

## Sources

- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/a11final-fltpln.pdf
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionOpReport.pdf
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf
- https://ntrs.nasa.gov/citations/19700023940

## Evidence status

- **DOCUMENTED / MISSION PLAN:** nominal powered-descent phase/event skeleton and high-/low-gate definitions.
- **DOCUMENTED / FLOWN:** 756.3-s powered-descent firing, approximately 6775 ft/s delta-V, 13-percent initial minimum throttle, approximately +26-s advance to full throttle, normal transients/response.
- **DOCUMENTED / LIMITATION:** approximately 45 s of early propulsion data were lost; the Mission Report's smoothed plot does not represent that gap.
- **DOCUMENTED / MISSION RULE:** after crew takeover, trajectory/guidance constraints are not themselves abort causes.
- **DOCUMENTED / PRIMARY TECHNICAL ACCOUNT:** ground guidance monitoring continued through the manual-landing interval.
- **IMPLEMENTED / SOURCE-BOUNDED:** decision-gate control mode changes trajectory/guidance abort-rule applicability while preserving controller-visible observations.
- **UNRESOLVED:** exact continuous flown thrust/trajectory history, exact Mission-G P66 ground indication/CRT field, and exact station product routing/cadence where not already recovered.