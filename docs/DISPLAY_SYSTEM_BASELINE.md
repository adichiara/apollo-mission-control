# Apollo MCC Display-System Baseline

Status: **Phase 1 research baseline**

This document records what is currently supported by source material about the Mission Control Center display architecture. It does **not** yet define the exact displays for any player station.

## 1. Controller CRTs were selectable information displays

Apollo-era Mission Control did not present each controller with a fixed modern-style dashboard.

NASA historical documentation describes flight controllers requesting information in pre-established display formats and receiving the resulting display on cathode-ray-tube (CRT) television monitors embedded in their consoles.

The data path described for Apollo-era MCC was broadly:

```text
mission / telemetry data
        ↓
Real-Time Computer Complex (RTCC)
        ↓
Display and Control System
        ↓
Digital-to-Television / display-generation equipment
        ↓
video distribution
        ↓
controller CRT
```

Static/background information and changing real-time information were combined to make a complete display.

## 2. Static and dynamic display components

The Philco-Ford *Display Formats Manual* distinguishes:

- **static/background information** — labels, titles, lines, diagrams, and other information that does not change during use of the format
- **dynamic information** — real-time computer-controlled values and status information such as pressures, temperatures, velocities, and discrete-state indications

The historical MCC therefore did not simply render character strings as a contemporary terminal would. The displayed image could be assembled from separately produced static and dynamic components.

This is an important constraint for visual reconstruction.

## 3. Displays were requested, not continuously exposed

The HAER history of Apollo Mission Control, citing an Apollo 11 Philco-Ford usage study, reports that controllers requested preset charts/graphs for their console CRTs.

For a 12-hour, 45-minute Apollo 11 period, the cited study recorded an average of **1044.9 display requests per hour** across the system, with each resulting display/transmission viewed for an average of approximately **5.3 minutes**.

This indicates an extremely active display-selection workflow rather than a small set of permanently visible subsystem pages.

The underlying Apollo 11 source is:

> B. Costis, W. Ortolani, and W. Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, Philco-Ford Corporation, 24 December 1969.

A public digital copy has not yet been located. The source is identified in the Johnson Space Center History Collection at University of Houston-Clear Lake.

## 4. Console controls were controller-specific

The historical account states that consoles contained switches and indicator lights selected and tailored to the functions and responsibilities of each controller.

Therefore the project must not assume:

- every station had the same controls
- every station had the same number of displays
- every station used the same display-request workflow
- a single generic "Apollo terminal" can represent every role faithfully

Controller-specific console research remains required.

## 5. Manual Select Keyboard and Display Request Keyboard

Apollo documentation contains the **Manual Select Keyboard (MSK)** abbreviation, and later Apollo documentation clearly describes display selection through console keyboards.

A detailed secondary reconstruction, citing the 1967 Philco *Mission Control Center Houston Familiarization Manual*, NASA TN D-7685, the Philco-Ford display manual, and Apollo 13 console documentation, describes:

- an MSK available for display/channel selection
- a Display Request Keyboard (DRK) at selected technical consoles for rapid access to preset displays
- separate functions for selecting a display versus attaching a console monitor to an already active TV channel

This is plausible and well supported for the Apollo MCC generally, but **exact Apollo 11 station configurations must still be confirmed from primary mission-era material before implementation**.

Do not yet implement a standardized MSK/DRK layout from this note.

## 6. Group displays were separate from console displays

The large front-of-room displays were a different display system from the controller CRTs.

Historical documentation describes:

- large rear-projection plotting displays
- background map imagery
- spotting projectors for vehicle position
- scribing/plotting projectors for trajectories and alphanumeric/XY information
- separate group television displays

The group displays are potentially important to a full room simulation, but they should not be confused with what each player sees on a phone representing a controller console.

## 7. Hard copy was operationally significant

Flight controllers also used hard-copy products distributed by pneumatic tube between the RTCC, MOCR, and Staff Support Rooms.

The HAER history describes charts, graphs, messages, and other documents being physically transmitted through tube stations integrated into the consoles.

This establishes that some operational information may be more authentic as a document/hard-copy product than as another phone screen.

The project should eventually identify:

- which products were requested as hard copy
- which controller positions used them
- which mission phases relied on them
- whether any should become physical or printable artifacts in the simulation

## 8. What is established versus unresolved

### Documented

- controller CRTs were selectable displays
- the RTCC prepared/generated controller display information
- static and dynamic material were combined in display production
- many preset display formats existed
- Apollo 11 controllers made display requests at very high frequency
- console controls were tailored to controller responsibilities
- group displays were technically distinct from controller CRTs
- hard-copy/pneumatic-tube products were part of controller work

### Partially documented

- exact MSK/DRK configuration for each Apollo 11 console
- exact Apollo 11 TV-channel/display-request mechanics
- exact Apollo 11 format inventory by controller and mission phase

### Unresolved

- exact pixel/scan/character appearance of the Apollo 11 formats to be reproduced
- exact Apollo 11 display IDs for each controller
- which formats were normally selected during the proposed first simulation interval
- update rates for each displayed parameter
- station-specific PBI/switch/indicator layouts
- which hard-copy products materially affect the target scenario

## 9. Implementation consequence

Do **not** create a generic VT220/IBM-VGA-style interface as the historical display.

The eventual renderer should be based on reconstructed MCC display formats. Until those formats are documented, interface work should remain a technical prototype rather than a claim of historical fidelity.

## Sources

1. Philco-Ford Corporation, R. L. Runnels, *Display Formats Manual*, PHO-TR515 / NASA-CR-128843, 12 January 1973.  
   https://ntrs.nasa.gov/citations/19730010501

2. *Johnson Space Center, Apollo Mission Control*, Historic American Engineering Record HAER TX-109-C, especially pp. 16–20.  
   https://www.nasa.gov/wp-content/uploads/2025/09/apollomc-habshaer.pdf

3. Richard A. Hoover, *Apollo Experience Report: Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements*, NASA-TN-D-7685, May 1974.  
   https://ntrs.nasa.gov/citations/19740015284

4. Apollo 11 Flight Mission Rules, abbreviation listing includes MSK — Manual Select Keyboard.  
   https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf

5. Secondary technical reconstruction used only as a discovery/interpretation aid for MSK/DRK details:  
   https://www.earlyspaceflight.nl/Mission_Management/JSC/MCC/MOCR/MOCR-page2.html

6. Identified but not yet digitally obtained: B. Costis, W. Ortolani, W. Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, 24 December 1969.
