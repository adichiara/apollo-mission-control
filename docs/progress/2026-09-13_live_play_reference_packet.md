# Progress — PC+2 live-play reference packet

Date: 2026-09-13  
Status: **COMPLETE FOR INITIAL PHYSICAL RUN — packet structure/content prepared; physical usability still pending**

## Completed

- Revisited the remaining player-packet organization question from the physical-validation stopping point.
- Used primary NASA sources first: Keyser on Flight Mission Rules, Kramer on systems/flight procedures, and Miller on integrated flight-controller simulation training.
- Added research note 097 defining a five-part packet structure that keeps responsibility, rules, nominal phase context, and modern client mechanics distinct.
- Added `docs/testing/PC2_PLAYER_REFERENCE_PACKET.md` for the initial seven-seat and five-player physical runs.
- Preserved scenario blindness: the packet does not reveal whether/when the synthetic ΔP branch occurs, hidden state, another station's private evidence, or intended diagnosis.
- Preserved unresolved historical criteria rather than simplifying them into invented displays: singular 150-psi inlet-pressure aggregation and exact onboard 77-percent thrust indication remain unresolved.
- Preserved original-station sheets in compact mode instead of creating synthetic historical `LM SYSTEMS` or `FLIGHT DYNAMICS` station references.

## Research consequence

Open question 23 is resolved for the **initial first-playable packet structure**, but not as a claim about an Apollo-era handout format. Physical play must still validate findability, clarity, compact-role switching, and whether neutral criteria remain usable without becoming hints.

## New stopping point

Repository-side preparation for the physical run now includes:

- preparation boundary/package;
- player reference packet;
- live-play protocol;
- incident/debrief report template.

The primary remaining first-playable boundary is still physical execution with actual simultaneous devices and human players. Any historical-content change proposed from play must be routed back through source review.