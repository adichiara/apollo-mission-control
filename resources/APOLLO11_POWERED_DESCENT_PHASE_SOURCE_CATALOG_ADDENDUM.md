# Apollo 11 powered-descent phase source-catalog addendum

Date: 2026-09-21
Parent: `resources/APOLLO11_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| NASA, *Apollo 11 Flight Plan, AS-506, CSM-107/LM-5*, final 1 Jul 1969 | Nominal powered-descent profile marking fixed throttle, LR updates, throttle recovery, high gate/P63→P64, low gate and touchdown; high-gate-to-touchdown panel provides nominal event/state anchors | Apollo-11-effective **planned** trajectory/phase authority. Do not promote nominal values to exact flown states or controller-visible fields without separate evidence. |
| NASA, *Apollo 11 Mission Report*, MSC-00171, Nov 1969, §9.8 | Flown powered descent 756.3 s, approximately 6775 ft/s delta-V; DPS starts at 13-percent minimum throttle and advances to full throttle after approximately 26 s; transients/throttle response normal; approximately 45 s data dropout during early interval | Apollo-11 **flown/postflight** propulsion authority. The report says its plotted data are smoothed and do not reflect the dropout; do not reconstruct measured history through the gap from the plot. |
| NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11, 24 Jun 1969 | Powered descent defined as braking, approach and landing phases; approach begins near 7,600 ft/high gate; landing begins at 500 ft/low gate | Mission-effective operational phase-definition authority; planned description, not exact flown transition state. |

## Current result

The Apollo 11 architecture reference can use a deterministic phase/event skeleton for powered descent while keeping nominal planning, flown propulsion evidence, hidden causal state, and controller-visible products separate. Continuous historical thrust/trajectory reconstruction and station product/rule mapping remain unresolved.

## Sources

- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/a11final-fltpln.pdf
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionOpReport.pdf

## Evidence status

- **DOCUMENTED / MISSION PLAN:** nominal powered-descent phase/event skeleton and high-/low-gate definitions.
- **DOCUMENTED / FLOWN:** 756.3-s powered-descent firing, approximately 6775 ft/s delta-V, 13-percent initial minimum throttle, approximately +26-s advance to full throttle, normal transients/response.
- **DOCUMENTED / LIMITATION:** approximately 45 s of early propulsion data were lost; the Mission Report's smoothed plot does not represent that gap.
- **UNRESOLVED:** exact continuous flown thrust/trajectory history and Apollo-11-effective controller-visible propulsion/trajectory products and rules at the phase boundaries.