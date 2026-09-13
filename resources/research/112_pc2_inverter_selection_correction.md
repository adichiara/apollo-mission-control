# Apollo 13 PC+2 — inverter selection correction

Date: 2026-09-13  
Status: **CORRECTED — Apollo 13 mission-specific PC+2 procedure evidence overrides the generic LM handbook convention used in note 111. The burn preparation retained inverter 2 rather than selecting inverter 1.**

## Purpose

Research note 111 combined the LM Operations Handbook's generic statement that inverter 1 is normally used during DPS/APS burns with Apollo 13's preparation of inverter 2, and inferred a first-playable mapping of inverter 1 → inverter 2 after an inverter warning.

A closer review of the Apollo 13 mission-specific PC+2 read-up shows that inference is not supportable.

## Mission-specific evidence

At approximately 75:11 GET, while reading modifications to Contingency Checklist page 17, CAPCOM instructed the crew:

- `CB(16) Inverter 2, Close`; and
- **scratch out `Select Inverter 1`.**

Haise read the change back. At approximately 75:15 GET CAPCOM corrected the breaker-panel number and again specified `CB(16) Inverter 2, Close`.

Earlier, at approximately 73:12 GET, the crew had explicitly verified/selected inverter 2 for LM AC use. After the associated task they opened the inverter-2 feed breaker; no reviewed intervening mission-specific instruction re-selected inverter 1. The PC+2 read-up then restored the inverter-2 breaker while deliberately deleting the checklist instruction that would have selected inverter 1.

Primary mission-specific sources:

- NASA Apollo 13 air-ground/PAO transcript, approximately 72:48–73:15 GET and 74:55–75:15 GET.
- Apollo 13 Flight Journal transcript presentation of the same exchanges.

## Interpretation

The Apollo 13-specific procedure has priority over the generic handbook convention.

For the current first playable, the supported pre-burn state is therefore:

```text
inverter selector retained on inverter 2
+ CB(16) INVERTER 2 closed at the PC+2 -4 minute configuration step
+ checklist instruction "Select Inverter 1" explicitly deleted
→ PC+2 burn AC configuration uses inverter 2
```

The generic handbook statement remains historically useful: it explains why the stock procedure contained `Select Inverter 1`. Apollo 13's emergency PC+2 procedure was a mission-specific deviation from that normal convention.

## Shutdown-rule consequence

The contemporaneous shutdown rule still says to shut down for an inverter light if it remains after the crew has tried switching inverters. The reviewed sources establish the **initial PC+2 selection as inverter 2**, but they do not yet provide a verbatim Apollo 13 post-warning instruction naming the alternate as inverter 1.

Accordingly, the first-playable rule should be represented as:

```text
PC+2 AC source: inverter 2
        ↓
inverter warning/light
        ↓
crew attempts switch to redundant inverter
        ↓
warning remains after switch
        ↓
shutdown criterion satisfied
```

Do not hard-code `inverter 2 → inverter 1` as the contingency action until a mission-specific procedure, malfunction checklist, or equally direct source confirms the alternate-selection action. The electrical architecture makes inverter 1 the obvious redundant unit, but the project should preserve the distinction between architectural implication and recovered procedure.

## Correction to note 111

Research note 111 is superseded on its first-playable inverter identity conclusion. Its cited generic handbook evidence remains valid, but its synthesis gave that generic convention too much weight over the mission-specific PC+2 modification.

## Sources

1. NASA Apollo 13 Mission Commentary / air-ground transcript, approximately 72:48–73:15 GET and 74:55–75:15 GET. https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
2. Apollo 13 Flight Journal, Day 4 Part 1, transcript of the same mission-specific procedure read-up. https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
3. Grumman/NASA, *Apollo Operations Handbook — Lunar Module, Subsystems Data*, LMA790-3-LM, §2.5.3.3 A-C Section, retained only for the generic normal-convention comparison.
