# Apollo MCC Display-System Baseline

Status: **Phase 1 research baseline**

This document records what is currently supported by source material about the Mission Control Center display architecture. It does **not** yet define the exact displays for any player station.

## 1. Controller CRTs were selectable information displays

Apollo-era Mission Control did not present each controller with a fixed modern-style dashboard. NASA historical documentation describes flight controllers requesting information in pre-established display formats and receiving the resulting display on CRT television monitors embedded in their consoles.

The data path was broadly mission/telemetry data → RTCC → Display and Control System → D/TV/display generation → video distribution → controller CRT. Static/background information and changing real-time information were combined to make a complete display.

## 2. Static and dynamic display components

The Philco-Ford *Display Formats Manual* distinguishes static/background information from dynamic computer-controlled values and status information. The historical MCC therefore did not simply render character strings as a contemporary terminal would.

NASA TN D-8316 adds an important timing boundary: D/TV display generators had full random-access buffer memories, so the real-time computers could update displays without regard to CRT refresh requirements, and could update either complete instruction lists or individual data words. The report's four-second access requirement applies to electromechanical **reference-slide** selection, not to dynamic telemetry update cadence. CRT refresh, dynamic-word update, operator display selection, and reference-slide access must therefore remain separate mechanisms in the simulation.

## 3. Displays were requested from a shared TV-channel pool

NASA TN D-7685 records Apollo flight-control experience with two TV-display control modes. Earth-orbital Apollo flights used 28 computer-driven TV channels; lunar-landing missions required 36. In **display request mode**, a console requested a display format, the computer generated and formatted it, output it to the next available computer-driven TV channel, and automatically connected that channel to the requesting console monitor. Channel assignment was first-come/first-served. In **channel attach mode**, a console requested an existing TV channel and received whatever data were already on it, allowing displays to be shared.

When all channels were occupied, the system provided a display identifying the format on each channel and the console that had requested it, allowing the flight-control team to decide which formats to release. This is shared-resource behavior, not evidence for a particular Apollo 11 GUIDO keyboard or a numeric refresh cadence.

HAER TX-109-C, citing an Apollo 11 Philco-Ford usage study, reports that controllers requested preset charts/graphs for their console CRTs. For a 12-hour, 45-minute Apollo 11 period, the cited study recorded an average of **1044.9 display requests per hour** across the system, with each resulting display/transmission viewed for an average of approximately **5.3 minutes**. These are aggregate system-level figures, not per-station refresh rates.

The underlying Apollo 11 primary source is B. Costis, W. Ortolani, and W. Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, 24 December 1969. A targeted retrieval found no public digital copy. HAER identifies the physical holding as Box 078-65/66, Mission Documents: Apollo 11, Apollo Program, Johnson Space Center History Collection, University of Houston-Clear Lake. Direct inspection is **BLOCKED** pending archival retrieval or an authenticated scan.

## 4. Console controls were controller-specific

Historical accounts state that consoles contained switches and indicator lights selected and tailored to each controller's responsibilities. Therefore the project must not assume every station had identical controls, displays, or request workflow.

## 5. Manual Select Keyboard and Display Request Keyboard

Apollo documentation contains the **Manual Select Keyboard (MSK)** abbreviation, and later Apollo documentation describes display selection through console keyboards. Exact Apollo 11 station configurations must still be confirmed from primary mission-era material before implementation. Do not implement a standardized MSK/DRK layout from secondary reconstruction.

## 6. Group displays were separate from console displays

The large front-of-room displays were technically distinct from controller CRTs. Historical documentation describes rear-projection plotting displays, background maps, spotting and scribing/plotting projectors, and group television displays. These should not be conflated with each player's console display.

## 7. Hard copy was operationally significant

Flight controllers also used hard-copy products distributed by pneumatic tube between the RTCC, MOCR, and Staff Support Rooms. Future work should identify which products, positions, and mission phases materially affect target scenarios before turning them into physical or printable artifacts.

## 8. What is established versus unresolved

### Documented

- controller CRTs were selectable displays;
- RTCC/Display-Control architecture separated processing from presentation;
- static and dynamic material were combined in display production;
- lunar-landing missions used a 36-channel computer-driven TV pool, compared with 28 channels for Earth-orbital Apollo flights;
- display-request mode assigned the next available channel and automatically connected it to the requesting console on a first-come/first-served basis;
- channel-attach mode allowed a console to share an already active TV channel;
- a channel-usage display supported identification and release of occupied channels;
- D/TV dynamic data could be updated independently of CRT refresh;
- complete display instruction lists or individual data words could be updated;
- the four-second TN D-8316 timing figure concerns reference-slide access, not dynamic telemetry cadence;
- many preset display formats existed;
- Apollo 11 controllers made display requests at high aggregate frequency;
- console controls were tailored to controller responsibilities;
- group displays were distinct from controller CRTs;
- PHO-TN401's identity and physical archival location are known.

### Blocked

- direct inspection of PHO-TN401, pending archival retrieval or authenticated scan.

### Partially documented / unresolved

- exact MSK/DRK configuration for each Apollo 11 console;
- exact Apollo 11 GUIDO button/format mapping and powered-descent selection;
- exact Apollo 11 format inventory and display IDs by controller and mission phase;
- numeric dynamic-data update rates, latency, and freshness behavior;
- station-specific PBI/switch/indicator layouts;
- which hard-copy products materially affect the target scenario.

## 9. Implementation consequence

Do **not** create a generic VT220/IBM-VGA-style interface as the historical display. Preserve source observation, ground processing/product generation, display selection, TV-channel allocation/attach/release, dynamic-word update, and visual presentation as distinct layers. Do not substitute the onboard two-second landing-radar cadence, the four-second reference-slide access requirement, or channel assignment behavior for an unsupported Apollo 11 controller-product update rate.

## Sources

1. Philco-Ford Corporation, R. L. Runnels, *Display Formats Manual*, PHO-TR515 / NASA-CR-128843, 12 January 1973. https://ntrs.nasa.gov/citations/19730010501
2. *Johnson Space Center, Apollo Mission Control*, HAER TX-109-C. https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf
3. Richard A. Hoover, *Apollo Experience Report: Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements*, NASA-TN-D-7685, May 1974. https://ntrs.nasa.gov/citations/19740015284
4. Cornelius J. Sullivan and LaRue W. Burbank, *Apollo Experience Report — Real-Time Display System*, NASA TN D-8316, September 1976. https://ntrs.nasa.gov/citations/19760024152
5. Apollo 11 Flight Mission Rules, abbreviation listing includes MSK — Manual Select Keyboard. https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf
6. **BLOCKED primary source:** B. Costis, W. Ortolani, W. Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, 24 December 1969; Box 078-65/66, Mission Documents: Apollo 11, Johnson Space Center History Collection, University of Houston-Clear Lake.
