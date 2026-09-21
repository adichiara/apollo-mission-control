# Station-status addendum — Apollo 11 program alarms

Date: 2026-09-21
Parent: `docs/STATION_RESEARCH_STATUS.md`

## GUIDANCE / GUIDO

**DOCUMENTED for front-room alarm recommendation.** During the descent alarm sequence, GUIDANCE supplies the GO assessment to FLIGHT. NASA's Garman history corroborates that computer-specialist back-room support informed Bales's assessment. Do not invent exact support-room wording or CRT fields.

## FLIGHT

**DOCUMENTED for disposition ownership.** FLIGHT receives the GUIDANCE recommendation and owns the operational continue/abort disposition before CAPCOM relay. The later 1201 sequence is sufficiently compact that GUIDANCE's `same type / GO` assessment feeds directly into the continuing GO.

## CAPCOM

**DOCUMENTED for crew relay.** CAPCOM transmits the GO-on-alarm disposition to Eagle; the primary technical air-to-ground transcript preserves this leg.

## Computer-specialist support

**DOCUMENTED role; PARTIAL interface.** Jack Garman is institutionally documented by NASA as supporting Bales from the back room and recognizing the 1202 overload condition. Exact loop topology, wording, and player-visible representation remain unresolved.

## Implementation guardrail

Do not turn alarm code recognition into an automatic GO. Preserve a GUIDANCE/computer-support evaluation step and FLIGHT disposition. The exact contemporary written decision criterion is the next research target.

## Evidence status

- **DOCUMENTED:** GUIDANCE recommendation, FLIGHT disposition, CAPCOM relay.
- **DOCUMENTED / RETROSPECTIVE NASA:** Garman support role.
- **UNRESOLVED:** exact written criterion, support-loop mechanics, and alarm-specific CRT basis.