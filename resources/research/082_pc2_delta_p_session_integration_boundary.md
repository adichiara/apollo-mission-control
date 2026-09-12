# Apollo 13 PC+2 — ΔP nonnominal session integration boundary

Date: 2026-09-12
Status: implementation boundary established from primary mission sources

## Question

How far can the already-modeled fuel/oxidizer differential-pressure shutdown rule be carried through the playable session and web transport without inventing Apollo 13 internal routing, wording, or vehicle response?

## Primary-source basis

### Flight Control Division, Mission Operations Report — Apollo 13, 28 April 1970

The PC+2 Mission Rules review identifies **fuel/oxidizer differential pressure greater than 25 psi** as a shutdown criterion and explicitly identifies it as a **ground call-out** condition.

The same material distinguishes rule-caused shutdown from the separate premature-shutdown restart case.

The reviewed source does **not** establish:

- the exact computation producing the singular ground ΔP value;
- exact CONTROL console/display routing;
- exact CONTROL→FLIGHT→CAPCOM voice-loop sequence;
- exact callout wording;
- exact crew switch/control sequence following the callout.

### Apollo 13 Technical Air-To-Ground Voice Transcription

The pre-burn Mission Rules read-up/readback around 76:30 GET independently confirms that the fuel/oxidizer ΔP criterion is a **ground call** to the crew and that the crew is to shut down for the listed condition.

This is a rules briefing, not evidence that a ΔP exceedance actually occurred during Apollo 13 PC+2.

## Integration decision

The first nonnominal web/session path is therefore:

```text
explicit SimSup/source injection
        ↓
CONTROL-visible ground ΔP product
        ↓
common shutdown-rule evaluator
        ↓
explicit CONTROL callout decision
        ↓
project CAPCOM queue
        ↓
explicit CAPCOM transmission
```

The following are deliberately **not automatic**:

- an injected ΔP value does not announce a diagnosis;
- a triggered rule does not create a controller decision;
- a CONTROL decision does not imply CAPCOM transmission;
- CAPCOM transmission does not imply a crew shutdown command;
- a crew shutdown command does not imply physical engine shutdown.

## Project routing boundary

The CAPCOM queue is an implementation transport abstraction. For a CONTROL-originated ΔP shutdown callout it is marked `requested_by=CONTROL` and carries a routing note that the exact historical internal Apollo routing remains unresolved.

This avoids falsely claiming FLIGHT approval or a particular voice-loop sequence while still allowing the documented ground-callout-to-crew workflow to be played.

## Synthetic test value

The integration tests use **26 psi** solely as a source-bounded threshold test because it is above the documented >25 psi rule boundary.

It is **not** represented as an Apollo 13 measurement or historical anomaly.

## Current stopping point

The nonnominal path now reaches CAPCOM transmission through the same authoritative session/API architecture used by nominal play.

The next research/integration question is the crew-response boundary: connect a transmitted ground shutdown callout to an explicit crew operational action and then to the already-separated DPS physical-response/evidence path, without assuming automatic compliance, exact response timing, or an unsupported cockpit sequence.

## Sources

- NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, PC+2 Mission Rules review, p. III-25 in the searchable copy.
- NASA, *Apollo 13 Technical Air-To-Ground Voice Transcription*, NTRS document 20160014370, rules read-up/readback near 76:30 GET.
- Repository research notes 058 and 068 for the observation path and earlier ground-callout boundary.
