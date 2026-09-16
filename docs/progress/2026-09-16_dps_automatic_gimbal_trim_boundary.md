# Progress — DPS automatic gimbal-trim boundary

Date: 2026-09-16

- Continued the PC+2 GDA provenance thread through Research Note 181.
- Confirmed NASA states that DPS gimbal trim compensates for changing vehicle center of gravity and is automatically accomplished by PGNS or AGS; cross-checked the Apollo 13 LM131 powered-flight trim-gimbal control law.
- Tightened the evidence boundary: `5.86 / 6.75` is a commanded/preburn reference, not evidence of a fixed powered-flight or exact postburn actuator state.
- Added mission-specific postflight performance evidence from the Apollo 13 Mission Report: the 61:29 free-return maneuver used primary guidance/AUTO, performance was nominal, no vehicle attitude excursions were reported, and firing time was as predicted.
- Added the executed propulsion profile: 34.3 seconds, initially minimum throttle reported postflight as 12%, then manually increased after 5 seconds to approximately 37%. This is kept distinct from the nominal preburn instruction of 10% then 40%.
- Identified the Apollo 13 GN&C performance-analysis supplement (`19730017939`, `MSC-02680-SUPPL-1`) as a high-priority primary source for the unresolved actuator-history branch; no gimbal value is attributed to it without inspecting the relevant data.
- Kept the unresolved T+55 -> RTCC/RTACF -> trim lineage unchanged; no missing ground-computation values were inferred.

Next: continue searching for the T+55 generation/load/run artifact and, independently, recover mission-specific GN&C/telemetry evidence for actual GDA positions during or immediately after the 61:29 burn.