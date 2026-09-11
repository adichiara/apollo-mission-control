# Controller Information Workflow

Status: **Phase 1 research baseline**

This document records the currently documented path by which Apollo Mission Control controllers obtained, requested, interpreted, and acted on information.

It is not yet a final player-interface specification.

## 1. Information was not simply "on the console"

Apollo Mission Control was built around requested and routed information products.

For the Apollo lunar missions, the controller's working information could come from several distinct mechanisms:

- computer-generated CRT display formats
- event/status indicators
- analog meters and recorders
- voice loops
- hard-copy material
- support-room analysis
- spacecraft/crew voice reports
- ground-network status information

The simulation should preserve these distinctions where they affect controller judgment.

## 2. Mission G / Apollo 11 RTCC evidence

The **Project Apollo 500 RTCC Operations Support Plan for Mission G**, MSC Internal Note 69-FS-2 (April 1969), is especially important because it is directly tied to Apollo 11.

It documents:

- PBI inputs
- MED inputs
- display requests
- telemetry-reference displays
- display-generation operations
- hard-copy verification for some transmissions
- Flight Controllers Operations Handbook references
- detailed television-display-format requirements

The plan states that during RTCC restart/initialization, PBI inputs, MED inputs, display requests, and other switches were inhibited until normal operations were restored.

This confirms that these controller inputs were operational interfaces into the real-time ground system, not cosmetic console controls.

## 3. Apollo 11 telemetry-reference display numbers

Mission G RTCC documentation identifies the following **Computer Telemetry Reference Displays** by MSK number:

| MSK | Title |
|---:|---|
| 1616 | APOLLO SMEK MSG LOG (SLV/LM) |
| 1617 | APOLLO SMEK MSG LOG (CSM) |
| 1621 | MED INPUTS (CSM/AGC SLV AGS AMD) |
| 1625 | MED INPUTS (LM/LGC) |
| 2001 | TLM STATUS DISPLAY PAGE 1 |
| 2002 | TLM STATUS DISPLAY PAGE 2 |
| 2009 | SIC TM CENTRF |
| 2010 | CSM TM CENTRF |
| 2011 | IU TM CENTRF |
| 2012 | AGC TM CENTRF |
| 2013 | SII TM CENTRF |
| 2014 | LM TM CENTRF |
| 2015 | LGC TM CENTRF |
| 2016 | AGS TM CENTRF |
| 2017 | AMD TM CENTRF |
| 2018 | TM MESSAGE LABELS |

This is the first mission-specific Apollo 11 display-number set entered into the project.

Important limitation:

> These are RTCC computer telemetry reference displays. They are not yet proven to be the normal operational front-room display set for any specific controller.

Do not treat this table as an EECOM/GNC/GUIDO screen menu until station ownership/use is documented.

## 4. MSK numbers appear in mission-specific RTCC operations

The same Mission G plan gives a concrete example of a requested display:

- **Landmark Acquisition Display — MSK 1508**

The RTCC procedure instructs generation of that display using specified inputs.

This is strong evidence that numeric MSK display identifiers should be preserved in the simulator when the exact historical display is known.

## 5. Computer-driven TV channels

Apollo Experience Report NASA-TN-D-7685 describes two important TV-display modes.

### Display-request mode

A console requested a display format.

The computer:

1. generated/formatted the display,
2. assigned it to the next available computer-driven TV channel,
3. automatically connected that TV channel to the requesting console monitor.

### Channel-attach mode

A console requested an existing TV channel and received whatever display was already active on that channel.

For Apollo lunar missions the system expanded from 28 to **36 computer-driven TV channels**.

This means a historically faithful interface may eventually need to distinguish:

- requesting a display format
- attaching to an already-active channel

That distinction should not be implemented until controller-specific operating procedures are confirmed.

## 6. Console interaction hardware

Apollo 13 Review Board Appendix B provides a concrete CSM EECOM console example. The diagram labels:

- two precision TV monitors
- Display Request Keyboard
- Manual Select Keyboard
- event indicators
- status/status-report keyboard
- summary-message-enable keyboard
- analog meter
- two voice communication positions

The report states that EECOM had several data formats available and that the two most frequently used formats shown in the appendix updated **once per second**.

This is valuable evidence about controller-console interaction, but it is Apollo 13 evidence. It must not be copied into Apollo 11 without mission-specific confirmation.

## 7. Controller-specific documentation

NASA SP-287 explicitly distinguishes two procedure-document classes:

### Flight Control Operations Handbook (FCOH)

Contained **interface procedures** involving more than two console positions.

### Flight Controller Console Handbook

Prepared for each console position and containing:

- the controller's job
- personal procedures
- checklists where possible

This is highly relevant to the physical documents players will eventually use.

The project should therefore distinguish at least:

- mission-wide Flight Mission Rules
- team/interface procedures
- controller-specific console procedures

rather than giving every player the same generic rulebook.

## 8. Front room versus backroom information

Staff Support Rooms provided detailed analysis and anomaly isolation to front-room controllers.

Therefore a front-room player's information environment may eventually need both:

- direct console products
- backroom-generated recommendations or analysis

The exact mechanism has not yet been selected.

## 9. Implementation constraint

For known historical data products, do not replace their workflow with a modern dashboard simply because it is convenient.

If the actual flow was:

```text
request display → wait/receive channel → inspect data → consult procedure → ask support room → report to FLIGHT
```

then that sequence is potentially part of the simulation.

The goal is not to maximize interface efficiency; it is to reproduce the controller's operational task closely enough for controller skill to matter.

## Sources

1. Project Apollo 500 RTCC Operations Support Plan for Mission G, MSC Internal Note 69-FS-2, April 1969.  
   https://www.ibiblio.org/apollo/Documents/RTCC%20Operations%20Support%20Plan%20for%20Mission%20G.pdf

2. Richard A. Hoover, *Apollo Experience Report: Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements*, NASA-TN-D-7685, 1974.  
   https://ntrs.nasa.gov/citations/19740015284

3. Report of Apollo 13 Review Board, Appendix B, EECOM console figures B7-7 through B7-9.  
   https://ntrs.nasa.gov/citations/19700078726

4. *What Made Apollo a Success?*, NASA-SP-287, Flight Operations chapter.  
   https://ntrs.nasa.gov/citations/19720005243
