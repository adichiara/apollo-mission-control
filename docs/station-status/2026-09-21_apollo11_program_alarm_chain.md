# Station-status addendum — Apollo 11 program alarms

Date: 2026-09-21
Parent: `docs/STATION_RESEARCH_STATUS.md`

## GUIDANCE / GUIDO

**DOCUMENTED for front-room alarm recommendation; BLOCKED for exact late-preflight written criterion.** During the descent alarm sequence, GUIDANCE supplies the GO assessment to FLIGHT. NASA's Garman history corroborates that computer-specialist back-room support informed Bales's assessment. Primary postflight MIT/IL and Grumman engineering memos establish the executive-overflow mechanism and restart behavior.

The available Apollo 11 mission-rule copies dated 16 April and 16 May 1969 predate the late descent simulation that triggered the alarm review. A targeted recovery pass did not recover the post-simulation change page/change notice, authenticated Bales/Garman cue sheet, or revised Guidance/training procedure. NASA's later institutional history confirms that Garman prepared an alarm list before landing but does not reproduce it. Under D-024, exact rule wording/threshold is now BLOCKED on recovery of one of those named artifacts.

Do not invent exact support-room wording, CRT fields, a recurrence count/time threshold, or a blanket rule that the alarm number itself means GO.

## FLIGHT

**DOCUMENTED for disposition ownership.** FLIGHT receives the GUIDANCE recommendation and owns the operational continue/abort disposition before CAPCOM relay. The later 1201 sequence is sufficiently compact that GUIDANCE's `same type / GO` assessment feeds directly into the continuing GO. This flown disposition is evidence of the decision made, not by itself the text of a general rule.

## CAPCOM

**DOCUMENTED for crew relay.** CAPCOM transmits the GO-on-alarm disposition to Eagle; the primary technical air-to-ground transcript preserves this leg.

## Computer-specialist support

**DOCUMENTED role; BLOCKED cue-sheet text.** Jack Garman is institutionally documented by NASA as supporting Bales from the back room, recognizing the 1202 overload condition, and preparing an alarm list before landing. Exact loop topology, wording, player-visible representation, and the contemporary cue-sheet text remain unrecovered.

## Implementation guardrail

Preserve `alarm → specialist/GUIDANCE evaluation → FLIGHT disposition → CAPCOM relay`. The simulation may reproduce the documented flown GO outcomes when modeling the Apollo 11 reference descent, but reusable decision logic must not encode an unsupported recurrence threshold or treat every 1201/1202 as automatically safe.

## Evidence status

- **DOCUMENTED:** GUIDANCE recommendation, FLIGHT disposition, CAPCOM relay.
- **DOCUMENTED / PRIMARY POSTFLIGHT ENGINEERING:** executive-overflow mechanism and restart behavior.
- **DOCUMENTED / RETROSPECTIVE NASA:** Garman support role and preparation of a preflight alarm list.
- **BLOCKED / NAMED SOURCE RECOVERY:** exact late-preflight written criterion and cue-sheet wording.
- **UNRESOLVED BUT NOT INFERRED:** support-loop mechanics and alarm-specific CRT basis.