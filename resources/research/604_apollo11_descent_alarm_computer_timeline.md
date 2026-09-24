# Research note 604 — Apollo 11 descent alarm computer timeline

Date: 2026-09-24
Research thread: `apollo11-program-alarm-controller-flow`
Status: DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC

## Question

Before direct GUIDO L/R and Flight Director-loop audio comparison, can the alarm search windows be anchored to a primary Mission-G event chronology without treating later transcripts as exact timing authority?

## Sources

NASA/MSC, _Apollo 11 Mission Report_, MSC-00171, November 1969, table 5-I, `Lunar descent event times`.

NASA-hosted PDF:
https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf

## Finding

Table 5-I provides the postflight computer/event chronology for powered descent:

| GET | Event |
| --- | --- |
| `102:38:22` | `1202 alarm (computer determined)` |
| `102:39:02` | `1202 alarm` |
| `102:41:32` | Enter program P64 |
| `102:42:18` | `1201 alarm (computer determined)` |
| `102:42:43` | `1202 alarm (computer determined)` |
| `102:42:58` | `1202 alarm (computer determined)` |
| `102:43:22` | Enter program P66 |
| `102:45:40` | Landing / engine off |

This gives five alarm events and places the final three after P64 entry and before P66 entry.

## Evidence consequence

Use these Mission Report times as **computer/event anchors** for primary-audio inspection. They are not automatically the timestamps of spoken crew reports, GUIDO calls, Garman advice, Flight-loop relays, or CAPCOM responses. Those voice events necessarily have their own recording/timing path and must be established from the recordings.

This distinction is important because the NASA Apollo Lunar Surface Journal's air-ground chronology places Armstrong's first audible `Program Alarm` report at `102:38:26`, several seconds after the Mission Report's first computer-determined event at `102:38:22`. The journal itself notes timing differences between its transcript chronology and table 5-I. Therefore the project must not force transcript timestamps and postflight computer-event timestamps into a single exact clock without reconciliation.

For the next audio pass, search around each Mission Report anchor with enough lead/lag to capture the spacecraft report, back-room advice, GUIDO disposition, Flight-loop relay, and CAPCOM response. Cross-compare GUIDO L/R and `792-AAI` before assigning exact voice timing or overlap.

## What this does not establish

- exact spoken wording or speaker identity on internal loops;
- the named circuit between Garman/support and Bales;
- station keyset privileges;
- whether every internal call is present on either GUIDO L/R or `792-AAI`;
- a single reconciled timestamp system across spacecraft telemetry, air-ground transcript, Historical Recorder channels, and `792-AAI`.

## Evidence status

- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC:** five postflight alarm-event anchors and P64/P66 boundaries from table 5-I.
- **DOCUMENTED / TIMING BOUNDARY:** computer-determined event time is not treated as exact spoken-call time.
- **OPEN:** direct GUIDO L/R ↔ `792-AAI` voice chronology, speaker attribution, overlap, and clock reconciliation.
