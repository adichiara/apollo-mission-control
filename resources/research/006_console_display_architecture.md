# Research Note 006 — Console and Display Architecture

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Question

What can currently be stated with evidence about how Apollo Mission Control controllers selected and viewed information at their consoles?

## Findings

### 1. Controller CRT displays were generated products

The NASA/HAER history states that controller-requested data was prepared by the Real-Time Computer Complex and then processed by the Display and Control System for presentation on console CRT television monitors.

The description specifically identifies Digital-to-Television equipment and a process that combined:

- a dynamic computer-generated image
- a static background image from photographic material

This agrees with the later Philco-Ford *Display Formats Manual*, which formally divides MCC display information into static/background and dynamic real-time information.

### 2. The interface was format-based

Controllers selected among pre-established display formats rather than navigating a hierarchical graphical UI.

The HAER history states that data could be requested as charts and graphs in preset formats.

The Philco-Ford manual was explicitly written to standardize creation of these operational formats.

### 3. Apollo 11 display use was intensive

The HAER report cites the Apollo-11-specific Philco-Ford report PHO-TN401 and states that, during one 12 h 45 min period, the system averaged 1044.9 display requests per hour.

This is useful design evidence: display selection itself was routine controller work.

### 4. PHO-TN401 is now a priority source

Full citation found:

B. Costis, W. Ortolani, W. Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, Contract NAS 9-1261, Philco-Ford Corporation for NASA, 24 December 1969.

Archive location reported by HAER:

Box 078-65/66, Mission Documents: Apollo 11, Apollo Program, Johnson Space Center History Collection, University of Houston-Clear Lake.

A public digitized copy was not found in the first search pass.

### 5. Console hardware was not generic

The historical description emphasizes that switches and indicator lights were selected according to controller responsibilities.

That means physical-console photographs from one station cannot be used uncritically to construct another station.

### 6. Hard-copy information was part of the operating system

The MOCR console environment included pneumatic-tube delivery of charts, graphs, messages, and other documents among RTCC, MOCR, and SSR personnel.

This is not just visual atmosphere; it was part of the controller information flow.

## MSK / DRK caution

Several later or reconstructed sources document:

- Manual Select Keyboard (MSK)
- Display Request Keyboard (DRK)
- display-ID selection
- TV-channel selection
- hard-copy requests

The Apollo 11 Flight Mission Rules confirm the acronym MSK.

However, before constructing station controls we still need a primary source that establishes **which Apollo 11 positions had which keyboard modules during the target mission phase**.

## Source-quality note

The following are excellent sources for system architecture but are post-Apollo-11:

- PHO-TR515 (1973)
- NASA TN D-7685 (1974)

They can describe the Apollo system and preserve Apollo experience, but any specific configuration detail must be checked against Apollo-11-era material before being treated as mission-specific.

## Research targets created by this pass

1. Locate PHO-TN401 or obtain archival scans.
2. Locate Philco PHO-FAM001, *Mission Control Center Houston Familiarization Manual* (30 June 1967).
3. Identify Apollo 11 console layout documentation by position.
4. Find Apollo 11 display-format ID inventories.
5. Find controller-specific data/display requirements.
6. Determine display update rates and data-quality/status indications.
7. Identify hard-copy products actually used during the selected mission interval.

## Sources

- https://www.nasa.gov/wp-content/uploads/2025/09/apollomc-habshaer.pdf
- https://ntrs.nasa.gov/citations/19730010501
- https://ntrs.nasa.gov/citations/19740015284
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf
