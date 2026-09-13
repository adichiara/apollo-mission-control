# 100 — PC+2 backroom / Staff Support Room boundary

Date: 2026-09-13  
Status: **RESOLVED FOR FIRST PLAYABLE — historical SSR support acknowledged; no playable backroom roles yet**

## Question

For the Apollo 13 PC+2 first playable, should Staff Support Room (SSR) / backroom functions be playable, silently absorbed by front-room players, automated, or omitted?

## Primary-source findings

Apollo 13 did not operate as a front-room-only Mission Operations Control Room.

The Apollo 13 Review Board appendix states that each MOCR operations group had a Staff Support Room. It identifies a Flight Dynamics SSR supporting the MOCR flight-dynamics team with detailed trajectory/guidance analysis and external technical interfaces, a Flight Director SSR, and a Vehicle Systems SSR that monitored detailed system status/trends and supported malfunction detection, isolation, correction, and circumvention.

The Apollo 13 Mission Operations Report independently confirms the operational importance of this support structure: its general comments explicitly praise EECOM SSR personnel, especially electrical-power specialists, for their work during the oxygen-tank anomaly and entry planning.

The Apollo 13 press kit likewise states that each MOCR operations group had a same-floor staff support room for detailed monitoring and analysis, alongside other support areas such as SPAN, meteorology, and the space-environment function.

## First-playable decision

For PC+2 at the current fidelity target:

1. **Do not add playable SSR/backroom seats yet.** Physical front-room validation is already the next unclosed boundary, and no first-playable decision currently requires a separately operated support-room role.
2. **Do not describe the simulation as reconstructing the complete Apollo control team.** The historical support structure must remain explicit in documentation and player-facing authenticity notes.
3. **Do not silently transfer undocumented backroom actions to front-room players.** A front-room player may only receive/use information or actions already supported by source-bounded station products, rules, procedures, or explicit scenario state.
4. **Do not invent automated expert advice.** If a later scenario needs an SSR-derived analysis, recommendation, calculation, or troubleshooting product, research that dependency and model it explicitly as a sourced support product or add a support role.
5. **Treat backroom omission as a scope adaptation, not a historical claim.** The omission is acceptable only while it does not remove a decision dependency that matters to the selected PC+2 slice.

## Reopen trigger

Reopen playable or explicit automated SSR support when physical play, a new nonnominal branch, or a later scenario exposes a concrete need for:

- trajectory/guidance analysis beyond current FIDO/RETRO/GUIDO products;
- detailed LM/CSM systems troubleshooting not already represented in station products/rules;
- a support-generated recommendation that materially affects FLIGHT/controller decisions;
- a historically documented handoff whose absence makes the front-room workflow misleading.

## Evidence limits

This note does **not** establish the exact PC+2 shift roster inside each SSR, the exact voice-loop topology between every front-room and support-room specialist, or the precise support-room product flow for every PC+2 event. Those remain research targets only if implementation demands them.

## Sources

See `resources/source-catalog/PC2_BACKROOM_SUPPORT_SOURCES.md`.
