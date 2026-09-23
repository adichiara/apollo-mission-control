# Research note 507 — Apollo 11 mission-rules MOCR voice-loop baseline

Date: 2026-09-23

## Question

Can the adjacent Apollo 10 communications baseline in note 506 be replaced by a mission-specific Apollo 11 primary source without inventing a station-to-loop mapping?

## Primary source

NASA Manned Spacecraft Center, _Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)_, 16 April 1969, Section 4, Ground Instrumentation Requirements, rule 4-5 COMMUNICATIONS, p. 4-3.

NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf

## Direct evidence

Apollo 11 rule 4-5 lists the MOCR communications facilities as:

- `FD LOOP`
- `AFD CONF LOOP`
- `MOCR SYS 1 & 2`
- `MOCR DYN`
- `A/G 1 LOOP`
- `A/G 2 LOOP`

The rule states that one of the two flight-director loops is mandatory and the remaining listed MOCR communications are highly desirable for mission control. The same rule separately lists an MCC/remote-sites air-ground path and states that it is used for communication with the crew.

## Consequence

Note 506's Apollo 10 evidence is no longer merely an adjacent-mission naming baseline: the same communications inventory is directly documented in the Apollo 11 mission rules. The simulator may therefore treat these names and the internal-MOCR versus crew-facing air-ground separation as **Mission-G-specific documented architecture**.

This still does **not** identify which internal loop Steve Bales/GUIDO and Jack Garman's guidance-software support room used during the 1201/1202 assessments. Rule 4-5 does not provide per-console monitor/talk privileges, support-room keyset assignments, detailed alarm-call routing, or DRK/display routing. `MOCR DYN` must not be assigned to GUIDO merely because the name appears trajectory-related.

## Simulator consequence

Use the documented Apollo 11 loop vocabulary where a named communications layer is needed, and preserve CAPCOM/A-G as distinct from internal controller traffic. Keep the exact GUIDO ↔ guidance-software support-room ↔ FLIGHT channel mechanics unresolved until a source with station/keyset assignments is recovered.

PHO-TN401 remains the primary blocked Mission-G display/control recovery target; it is not assumed to contain voice-loop keyset assignments until directly inspected.

## Evidence status

- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary and internal-MOCR versus crew-facing A/G separation.
- **UNRESOLVED:** Apollo 11 GUIDO ↔ guidance-software support-room loop/channel identity, per-console keyset privileges, and detailed internal alarm-call routing.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection for display/control configuration.
