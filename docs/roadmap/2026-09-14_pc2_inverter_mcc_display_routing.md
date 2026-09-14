# Roadmap addendum — PC+2 inverter MCC display routing

Date: 2026-09-14

## Resolved in this pass

Research note 118 narrows the remaining inverter ground-display question.

NASA TN D-7685 documents two relevant Apollo MCC computer-driven TV control modes:

1. **Display request mode** — a console requested a display format; the computer formatted it, assigned the next available TV channel, and connected that channel to the requesting console.
2. **Channel attach mode** — a console attached to a TV channel already carrying a display.

This means the unresolved PC+2 inverter routing problem should not be represented as a missing permanently wired TELMU/CONTROL channel. The source-backed `GC0155` frequency and `GC0071` voltage telemetry can reach the MCC display system without implying a fixed channel assignment.

## Canonical first-playable boundary

```text
selected inverter bus
    ↓
GC0155 frequency + GC0071 voltage
    ↓
PCMTEA / MSFN
    ↓
MCC computer-driven display capability
    ↓
project-rendered station electrical evidence
```

The final presentation remains explicitly project-rendered until Apollo 13 display-format/configuration evidence is recovered.

Do not invent:

- a fixed TV-channel number;
- a permanent TELMU/CONTROL channel assignment;
- an Apollo 13 display-format number;
- a specific MSK/DRK key sequence;
- exact field placement, cadence, or latency.

## Remaining archival targets

1. Recover Apollo 13 MCC display-format/configuration material that names the format containing `GC0155` and/or `GC0071`, if such a format survives.
2. Recover exact row/column labels, engineering-unit treatment, and any limit/event behavior.
3. Determine which Apollo 13 controller(s) actually selected the relevant format during PC+2 if contemporaneous configuration or loop evidence survives.
4. Determine display update cadence and end-to-end latency only from direct primary evidence.
5. Preserve the separate unresolved search for any additional direct caution/selector telemetry path.

## Priority

These remain archival refinements. Physical seven-seat nominal, synthetic ΔP, and five-player compact human/device validation remain the principal unclosed first-playable PASS boundaries.
