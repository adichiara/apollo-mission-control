# Research note 702 — Garman staff-support-room voice keyset semantics

Date: 2026-09-23
Research thread: `apollo-mocr-controller-interface`

## Question

Can the unresolved Apollo 11 GUIDO/support-room communications boundary be narrowed without inventing a named loop assignment?

## Sources

NASA Johnson Space Center Oral History Project, John R. Garman interview, 27 March 2001.

NASA transcript: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf

## Direct evidence

Garman describes the Apollo staff-support-room communications panels from firsthand experience. He says the panels used white buttons for loops on which the operator could talk and amber buttons for loops the operator could listen to; many loops had both. He specifically says very few people had a white air-ground button, while the support-room personnel could listen to air-ground.

For the flight-director loop, Garman says the support room likewise listened, and recalls that the support position received a flight-director talk button only "later on" because explaining unusual problems otherwise forced the flight director to leave his loop or listen elsewhere. He connects that later evolution with the eventual move of the computer-support function into the front room as DPS in the Shuttle era.

Garman also identifies his Apollo room as the flight-dynamics/trench staff support room and describes standard consoles, multiple simultaneously monitored voice loops, per-loop listening volume, and a console speaker that could carry additional loops.

## Consequence

This materially narrows the communications model without identifying the alarm-assessment loop by name:

- Apollo support-room communications were multi-loop and privilege-sensitive, not a single generic intercom.
- talk and monitor capability were distinct keyset privileges;
- support personnel could monitor crew-facing air-ground without possessing crew-transmit authority;
- the flight-director loop should **not** be assumed to have been a support-room talk path during Apollo 11 merely because it was monitorable.

Garman's retrospective phrase "later on" is not precise enough to prove the exact date on which his support position gained an FD-loop talk button. It therefore cannot by itself prove a negative station assignment for 20 July 1969. It does, however, make an invented direct AGC-support → FD talk path historically unsafe.

## Simulator consequence

Represent loop **monitor** and **talk** permissions separately. For the Apollo 11 reference, permit guidance-software support to monitor relevant traffic as required by sourced role behavior, but do not give the back-room support position direct air-ground transmit authority or a named FD-loop talk privilege without mission-effective configuration evidence. Keep the actual GUIDO ↔ AGC-support alarm-assessment loop identity unresolved.

This strengthens the existing architecture in which guidance-software support advises GUIDO/Bales, while CAPCOM remains the crew-facing voice. It does not justify assigning that advice to `MOCR DYN`, `FD LOOP`, or any other named loop.

## Evidence status

- **DOCUMENTED / PARTICIPANT:** Apollo staff-support-room voice keysets distinguished talk (white) from listen (amber), supported simultaneous loop monitoring, and allowed support personnel to monitor A/G without general A/G transmit authority.
- **DOCUMENTED / PARTICIPANT, DATE-IMPRECISE:** Garman recalls FD-loop talk capability being added to the support position only later.
- **UNRESOLVED:** exact Apollo 11 GUIDO ↔ AGC-support loop identity; 20 July 1969 per-position keyset matrix; exact date of FD-loop talk-button addition.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection for display/control configuration; a Mission-G-effective station/keyset record remains desirable for exact voice routing.
