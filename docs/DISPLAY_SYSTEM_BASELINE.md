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

The Philco-Ford *Display Formats Manual* distinguishes static/background information from dynamic computer-controlled values and status information. The historical MCC therefore did not simply render character strings as a contemporary terminal would; displayed images could be assembled from separately produced static and dynamic components.

## 3. Displays were requested, not continuously exposed

HAER TX-109-C, citing an Apollo 11 Philco-Ford usage study, reports that controllers requested preset charts/graphs for their console CRTs. For a 12-hour, 45-minute Apollo 11 period, the cited study recorded an average of **1044.9 display requests per hour** across the system, with each resulting display/transmission viewed for an average of approximately **5.3 minutes**. These are aggregate system-level figures, not per-station refresh rates.

The underlying Apollo 11 primary source is:

B. Costis, W. Ortolani, and W. Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, Philco-Ford Corporation, 24 December 1969.

A targeted retrieval found no public digital copy. HAER identifies the physical holding as Box 078-65/66, Mission Documents: Apollo 11, Apollo Program, Johnson Space Center History Collection, University of Houston-Clear Lake. Direct inspection is therefore **BLOCKED** pending archival retrieval or an authenticated scan. Do not infer exact controller request keys, per-field cadence, latency, or powered-descent format selection from the aggregate HAER figures.

## 4. Console controls were controller-specific

Historical accounts state that consoles contained switches and indicator lights selected and tailored to each controller's responsibilities. Therefore the project must not assume every station had identical controls, displays, or request workflow.

## 5. Manual Select Keyboard and Display Request Keyboard

Apollo documentation contains the **Manual Select Keyboard (MSK)** abbreviation, and later Apollo documentation describes display selection through console keyboards. A detailed secondary reconstruction cites a 1967 Philco familiarization manual, NASA TN D-7685, the Philco-Ford display manual, and Apollo 13 console documentation for MSK/DRK behavior.

This is plausible for the Apollo MCC generally, but **exact Apollo 11 station configurations must still be confirmed from primary mission-era material before implementation**. Do not implement a standardized MSK/DRK layout from secondary reconstruction.

## 6. Group displays were separate from console displays

The large front-of-room displays were technically distinct from controller CRTs. Historical documentation describes rear-projection plotting displays, background maps, spotting and scribing/plotting projectors, and group television displays. These should not be conflated with each player's console display.

## 7. Hard copy was operationally significant

Flight controllers also used hard-copy products distributed by pneumatic tube between the RTCC, MOCR, and Staff Support Rooms. Future work should identify which products, positions, and mission phases materially affect the target scenarios before turning them into physical or printable game artifacts.

## 8. What is established versus unresolved

### Documented

- controller CRTs were selectable displays;
- RTCC/Display-Control architecture separated processing from presentation;
- static and dynamic material were combined in display production;
- many preset display formats existed;
- Apollo 11 controllers made display requests at high aggregate frequency;
- console controls were tailored to controller responsibilities;
- group displays were distinct from controller CRTs;
- hard-copy/pneumatic-tube products were part of controller work;
- PHO-TN401's identity and physical archival location are known.

### Blocked

- direct inspection of PHO-TN401, pending archival retrieval or authenticated scan.

### Partially documented / unresolved

- exact MSK/DRK configuration for each Apollo 11 console;
- exact Apollo 11 TV-channel/display-request mechanics;
- exact Apollo 11 format inventory by controller and mission phase;
- exact Apollo 11 display IDs for each controller;
- powered-descent format selections;
- update rates, latency, and freshness behavior for displayed parameters;
- station-specific PBI/switch/indicator layouts;
- which hard-copy products materially affect the target scenario.

## 9. Implementation consequence

Do **not** create a generic VT220/IBM-VGA-style interface as the historical display. The eventual renderer should be based on reconstructed MCC display formats. Until those formats and station workflows are documented, interface work remains a technical prototype rather than a claim of historical fidelity.

## Sources

1. Philco-Ford Corporation, R. L. Runnels, *Display Formats Manual*, PHO-TR515 / NASA-CR-128843, 12 January 1973. https://ntrs.nasa.gov/citations/19730010501
2. *Johnson Space Center, Apollo Mission Control*, Historic American Engineering Record HAER TX-109-C. https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf
3. Richard A. Hoover, *Apollo Experience Report: Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements*, NASA-TN-D-7685, May 1974. https://ntrs.nasa.gov/citations/19740015284
4. Apollo 11 Flight Mission Rules, abbreviation listing includes MSK — Manual Select Keyboard. https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf
5. Secondary discovery aid only: https://www.earlyspaceflight.nl/Mission_Management/JSC/MCC/MOCR/MOCR-page2.html
6. **BLOCKED primary source:** B. Costis, W. Ortolani, W. Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, 24 December 1969; Box 078-65/66, Mission Documents: Apollo 11, Johnson Space Center History Collection, University of Houston-Clear Lake.
7. Retrieval-status record: `resources/research/334_apollo11_display_usage_source_retrieval_status.md`.