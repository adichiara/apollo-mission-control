# Apollo 13 PC+2 — 77-percent thrust-rule applicability gate

Date: 2026-09-13  
Status: **REVIEWED / BOUNDED FIRST-PLAYABLE RESOLUTION — use entry into the commanded maximum/full-throttle segment as the applicability gate for the crew ENG THRUST <=77-percent criterion. This is a source-bounded lineage inference, not a recovered Apollo 13 sentence explicitly defining the gate.**

## Purpose

Research note 107 identified the crew-side PC+2 percent-thrust instrument as the LM panel-1 CMD THRUST / ENG THRUST indicator family, with ENG THRUST the actual-engine-thrust percent scale. It left one narrow gap: the 77-percent shutdown criterion cannot apply during the intentionally commanded low-thrust startup segments, so when does it become applicable?

This pass resolves that question for the first playable without inventing an arbitrary timestamp.

## 1. Apollo 13 primary sources fix the throttle sequence

The Apollo 13 Technical Crew Debriefing records the PC+2 DPS profile directly from the crew:

- 5 seconds at idle/low thrust;
- 21 seconds at 40-percent throttle;
- the remainder at full throttle;
- Lovell states that the configuration went to full throttle at **26 seconds** after engine start.

The Flight Control Division Mission Operations Report independently gives the same staged profile in rounded form: approximately 5 seconds at 12.6 percent, 21 seconds at 40 percent, then approximately 235 seconds at maximum thrust.

This establishes a historically observed transition from an intentionally sub-77-percent commanded segment to the maximum-thrust segment.

## 2. Antecedent DPS mission-rule lineage uses a high-throttle applicability boundary

As documented in research note 106, the surviving Apollo 10 DPS mission-rule lineage distinguishes propulsion-pressure limits by throttle regime, including a **>65-percent throttle** branch for the 150-psi fuel-inlet-pressure limit.

Apollo 13's PC+2 rules were explicitly described to the crew as similar to LOI Mode I abort rules with tight limits. That does not prove every Apollo 10 rule qualifier was copied unchanged, but it demonstrates that DPS abort criteria were historically conditioned by throttle regime rather than being applied blindly during commanded low-thrust operation.

## 3. First-playable applicability rule

For the current PC+2 slice, the most conservative source-bounded rule is:

```text
crew ENG THRUST <= 77% criterion
    INACTIVE during commanded 12.6% / 40% startup
    ACTIVE when the commanded profile enters maximum/full throttle
```

For the Apollo 13 PC+2 nominal profile, the crew debrief fixes that transition at **burn +26 seconds**.

This is preferable to inventing a free-standing activation delay because the gate is tied directly to a sourced maneuver phase change.

## 4. Confidence and limitation

The following are directly sourced:

- the Apollo 13 crew shutdown criterion of 77 percent onboard;
- the CMD/ENG THRUST instrument family and ENG actual-thrust function;
- the commanded PC+2 startup profile;
- the automatic/full-throttle transition at burn +26 seconds;
- antecedent DPS mission-rule use of throttle-regime qualification.

The following is **not** directly recovered:

- an Apollo 13 mission-rule line stating verbatim that the 77-percent criterion becomes active exactly at full-throttle command or above 65-percent throttle.

Therefore the first-playable gate is a **lineage-based historical approximation with explicit provenance**, not an exact reconstructed rule annotation.

## 5. Implementation consequence

The executable scenario may now represent an applicability state for the crew thrust criterion:

```text
startup_low_thrust -> startup_40_percent -> max_thrust
                                           |
                                           +-> ENG THRUST <=77% rule applicable
```

The nominal transition occurs at burn +26 seconds because that timing is directly reported by the Apollo 13 crew.

This does **not** authorize synthesizing the crew ENG THRUST indication from hidden engine state. The observation path remains separate: a scenario must still provide a crew-visible ENG THRUST observation before the criterion can be evaluated.

## 6. What remains prohibited

Do not:

- apply the 77-percent criterion from ignition;
- invent an activation point inside the 12.6-percent or 40-percent segments;
- assume every Apollo 10 throttle qualifier transferred verbatim to Apollo 13;
- alias ENG THRUST to the ground chamber-pressure product;
- manufacture a crew gauge value directly from hidden physical truth.

## 7. Research consequence

The bounded first-playable applicability question left by note 107 is now resolved sufficiently for implementation. Stronger Apollo 13-specific mission-rule/display documentation, if recovered later, should supersede this lineage-based gate.

Physical seven-seat validation remains the primary project blocker; this archival refinement does not change that priority.

## Primary sources

- NASA Manned Spacecraft Center, *Apollo 13 Technical Crew Debriefing*, 24 Apr 1970, section 9, p. 9-2: crew account of 5 seconds at idle, 21 seconds at 40-percent throttle, and automatic/full-throttle transition at 26 seconds. https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/a13-techdebrief.pdf
- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970: PC+2 shutdown criteria and staged DPS throttle profile. https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- NASA Apollo 13 technical air-ground transcript, approximately 76:30 GET: crew rule read-up describing the 77-percent onboard thrust criterion and the LOI Mode I abort-rule relationship. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- NASA Manned Spacecraft Center, *Apollo 10 Mission Rules*, section 3, item 3-77, 23 Apr 1969: antecedent DPS rule lineage using throttle-regime qualification for fuel-inlet pressure. See `resources/source-catalog/PC2_INLET_PRESSURE_SOURCES.md` and research note 106 for the recovered-page record.
