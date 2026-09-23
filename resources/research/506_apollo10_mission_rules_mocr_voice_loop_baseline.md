# Research note 506 — Apollo 10 mission-rules MOCR voice-loop baseline

Date: 2026-09-23

## Question

Can a primary, mission-era source narrow the unresolved Apollo 11 Mission Control voice-loop vocabulary without inventing an Apollo 11 station-to-loop mapping?

## Primary source

NASA Manned Spacecraft Center, _Apollo 10 Mission Rules_, final revision, 15 April 1969, Section 4, Ground Instrumentation Requirements, rule 4-5 COMMUNICATIONS, p. 4-3.

NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap10fj/pdf/a10-mission-rules-19690415.pdf

## Direct evidence

Rule 4-5 lists the MOCR communications facilities required before flight as:

- `FD LOOP`
- `AFD CONF LOOP`
- `MOCR SYS 1 & 2`
- `MOCR DYN`
- `A/G 1 LOOP`
- `A/G 2 LOOP`

The rule classifies one of the two flight-director loops as mandatory and the remaining listed MOCR communications as highly desirable for mission control. The same page separately requires an MCC/remote-site air-ground path for communication with the crew.

## What this establishes

This is a primary NASA/MSC, immediately pre-Apollo-11 baseline proving that `FD LOOP`, `AFD CONF LOOP`, `MOCR SYS 1 & 2`, `MOCR DYN`, and the two air-ground loops were operational Mission Control loop names/categories in the adjacent Apollo 10 configuration. It also reinforces the architectural separation between internal MOCR communications and the external air-ground path.

## What it does not establish

The source does **not** identify which of these loops Steve Bales/GUIDO or Jack Garman's guidance-software support room used for the Apollo 11 1201/1202 calls. It does not provide Apollo-11-specific keyset assignments, back-room loop names, per-console monitor/talk privileges, alarm-call timing, or DRK/display routing. Those details must not be back-projected from Apollo 10 or inferred from generic loop purpose.

## Simulator consequence

The reference architecture may use the documented Apollo-era loop vocabulary as a constrained naming baseline, while keeping the exact Apollo 11 GUIDO/support-room alarm channel unresolved. Internal controller traffic and crew-facing CAPCOM/A-G traffic should remain separate communication layers.

PHO-TN401 remains the primary blocked Mission-G display/control recovery target; an Apollo-11-effective communications/keyset source is still required before exact loop assignments are frozen.

## Evidence status

- **DOCUMENTED:** adjacent-mission primary-source MOCR loop vocabulary and internal-versus-A/G separation.
- **UNRESOLVED:** Apollo 11 GUIDO ↔ guidance-software support-room loop/channel identity and keyset configuration.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection for display/control configuration.