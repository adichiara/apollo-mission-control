# Station-status addendum — Apollo 11 landing GO poll

Date: 2026-09-21
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical Apollo 13 station maturity grades remain unchanged. This addendum concerns the Apollo 11 reference descent.

## FLIGHT

**DOCUMENTED for landing-GO workflow.** FLIGHT initiates the late-descent go/no-go poll, receives station responses, and hands the resulting team GO to CAPCOM. This is a player-facing coordination function directly supported by the descent audio record.

## GUIDANCE / GUIDO

**DOCUMENTED as a landing-poll participant; PARTIAL for LR basis.** GUIDANCE is explicitly polled and returns a status. This supports a required GUIDANCE vote at the landing gate. It does not prove a separate spoken LR-convergence declaration or recover the exact Mission-G CRT/support-room basis for the vote.

## RETRO, FIDO, CONTROL, TELCOM, GNC, EECOM, SURGEON

**DOCUMENTED as landing-poll participants.** Each is called by FLIGHT and returns status in the recorded poll. This evidence supports station participation in the gate but, by itself, does not define the subsystem criteria each controller evaluated.

## CAPCOM

**DOCUMENTED as crew relay.** After FLIGHT closes the poll, CAPCOM transmits the GO for landing to Eagle. The NASA technical air-to-ground transcript independently preserves this crew-facing leg.

## Implementation guardrail

Represent the interaction as a team gate, not as a GUIDO-only landing authorization. Keep each station's vote criteria tied to separately sourced station evidence; do not reverse-engineer undocumented criteria from the fact that the station said GO.

## Remaining station question

The exact support-room/GUIDANCE chain for LR convergence remains unresolved, as does the Mission-G display basis. The next active voice-workflow target is the 1201/1202 alarm chain, where contemporary audio can potentially identify support-room→GUIDANCE→FLIGHT→CAPCOM propagation.

## Evidence status

- **DOCUMENTED:** named front-room station participation, FLIGHT poll ownership, CAPCOM crew relay.
- **PARTIAL:** GUIDANCE's underlying LR/display/support inputs.
- **UNRESOLVED/BLOCKED:** exact Mission-G parameter/display routing under the existing archival boundary.