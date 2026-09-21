# Station-status addendum — Apollo 11 program alarms

Date: 2026-09-21
Parent: `docs/STATION_RESEARCH_STATUS.md`

## GUIDANCE / GUIDO

**DOCUMENTED for front-room alarm recommendation; PARTIAL for decision criterion.** During the descent alarm sequence, GUIDANCE supplies the GO assessment to FLIGHT. NASA's Garman history corroborates that computer-specialist back-room support informed Bales's assessment. Primary postflight MIT/IL and Grumman engineering memos establish the executive-overflow mechanism and restart behavior. The exact late-preflight written GO/abort rule has not been recovered.

The available Apollo 11 mission-rule copies dated 16 April and 16 May 1969 predate the late descent simulation that triggered the alarm review, so they cannot be used to manufacture the resulting criterion. Do not invent exact support-room wording, CRT fields, a recurrence count/time threshold, or a blanket rule that the alarm number itself means GO.

## FLIGHT

**DOCUMENTED for disposition ownership.** FLIGHT receives the GUIDANCE recommendation and owns the operational continue/abort disposition before CAPCOM relay. The later 1201 sequence is sufficiently compact that GUIDANCE's `same type / GO` assessment feeds directly into the continuing GO. This flown disposition is evidence of the decision made, not by itself the text of a general rule.

## CAPCOM

**DOCUMENTED for crew relay.** CAPCOM transmits the GO-on-alarm disposition to Eagle; the primary technical air-to-ground transcript preserves this leg.

## Computer-specialist support

**DOCUMENTED role; PARTIAL interface.** Jack Garman is institutionally documented by NASA as supporting Bales from the back room and recognizing the 1202 overload condition. Exact loop topology, wording, player-visible representation, and the contemporary cue-sheet text remain unresolved.

## Implementation guardrail

Preserve `alarm → specialist/GUIDANCE evaluation → FLIGHT disposition → CAPCOM relay`. The simulation may reproduce the documented flown GO outcomes when modeling the Apollo 11 reference descent, but reusable decision logic must not encode an unsupported recurrence threshold or treat every 1201/1202 as automatically safe.

## Evidence status

- **DOCUMENTED:** GUIDANCE recommendation, FLIGHT disposition, CAPCOM relay.
- **DOCUMENTED / PRIMARY POSTFLIGHT ENGINEERING:** executive-overflow mechanism and restart behavior.
- **DOCUMENTED / RETROSPECTIVE NASA:** Garman support role.
- **SOURCE-GAP BOUNDED:** April/May mission-rule copies predate the late simulation-driven review.
- **UNRESOLVED:** exact late-preflight written criterion, support-loop mechanics, alarm-specific CRT basis, and cue-sheet wording.