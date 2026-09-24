# 513 — Apollo 11 MOCR display availability

Date: 2026-09-24

## Question

Can Mission-G primary evidence narrow the display resources actually required for GUIDO without inventing GUIDO's DRK labels or powered-descent format callups?

## Primary-source result

Yes. The Apollo 11 Flight Mission Rules, dated 16 April 1969, rule 4-9, provide Mission-G-specific ground-display requirements.

For **MOCR D/TV channels**, the rule states that **10 of 36** channels were mandatory prelaunch and allocates that minimum by position: RETRO 1, FIDO 1, **GUIDO 1**, EECOM 1, GNC 1, RTCC 1, and BOOSTER 4.

The same rule separately lists trajectory/display products. Of particular relevance to guidance monitoring, it identifies:

- `GAMMA(I) VS V(I) (CMC DYNAMIC STATUS)` as highly desirable on a 10 x 10 scriber plotter, with the cue that it monitors launch-vehicle/spacecraft navigation performance by comparing CMC with tracking;
- `WEDGE ANGLE MONITOR` as highly desirable on D/TV for launch-vehicle and spacecraft navigation-performance monitoring;
- `GUIDO ANALOG CHART RECORDERS ONE AND TWO` as highly desirable on D/TV.

This is stronger than the adjacent-mission evidence in note 512 for one narrow question: it establishes an Apollo-11-effective minimum D/TV resource for GUIDO and confirms that GUIDO's information environment included analog chart-recorder products that could be displayed on D/TV.

## Effectivity and interpretation boundary

Rule 4-9 is a **ground instrumentation requirement**, not a console wiring or display-format assignment record. Its phase is `PRELAUNCH`. Therefore:

- `GUIDO 1` is treated as a required minimum D/TV-channel resource for the position under the rule, not proof that GUIDO permanently owned one fixed physical channel throughout the mission;
- the rule does not identify a GUIDO DRK key, four-digit RTCC format number, FDK loading, or CRT screen assignment;
- the rule does not establish which display Steve Bales selected during P63/P64/P66 or the 1201/1202 alarms;
- the rule does not establish that the listed launch-navigation products were the powered-descent products used during lunar landing;
- the rule does not supersede NASA TN D-7685's Apollo-generic evidence that display-request mode dynamically assigned an available computer-driven TV channel.

No powered-descent display callup is inferred from this prelaunch requirement.

## Simulator consequence

The Apollo 11 reference may now encode a Mission-G-specific **display-resource constraint**: GUIDO was among the MOCR positions for which one D/TV channel was part of the mandatory prelaunch minimum. This should be modeled as availability/capacity, not as a permanently bound modern monitor or channel identity.

The station may also acknowledge analog chart recorders as part of the documented GUIDO information environment, but their exact powered-descent use, variables, routing, and on-screen presentation remain open unless separately sourced.

## Source

- NASA/MSC, _Flight Mission Rules, Apollo 11_, 16 April 1969, rule 4-9, Ground Instrumentation Requirements, MCC p. 4-5: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf

## Evidence status

- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC:** Apollo 11 rule 4-9 requires 10 of 36 MOCR D/TV channels prelaunch, including one for GUIDO.
- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC:** rule 4-9 lists GUIDO analog chart recorders one and two as highly desirable on D/TV and identifies adjacent launch-navigation monitoring products.
- **OPEN / MISSION-G-SPECIFIC:** GUIDO DRK labels/format numbers, FDK configuration, exact powered-descent display callups, channel identity, and request cadence/latency.
- **NO INFERENCE:** prelaunch D/TV requirements are not treated as proof of powered-descent display selection or permanent channel ownership.
