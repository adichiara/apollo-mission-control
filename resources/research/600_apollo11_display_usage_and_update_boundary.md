# Research note 600 — Apollo 11 MCC display usage and update boundary

Research thread: `apollo11-controller-displays`
Date: 2026-09-20
Status: **BLOCKED for mission-specific workflow; PARTIALLY DOCUMENTED for generic Apollo display update behavior**

## Question

Can the next unresolved Apollo 11 controller-display item — exact request behavior, display usage, or timing — be closed from mission-specific or primary Apollo display-system evidence rather than inferred from onboard cadence or later mission material?

## Primary-source-first result

The mission-specific source is identified bibliographically as B. Costis, W. Ortolani, and W. Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, Philco-Ford Corporation, 24 December 1969. A targeted public-web retrieval did not locate a digital copy. HAER TX-109-C cites it to Box 078-65/66, Mission Documents: Apollo 11, Apollo Program, Johnson Space Center History Collection, University of Houston-Clear Lake.

Direct inspection of PHO-TN401 is therefore **BLOCKED** pending archival retrieval or an authenticated scan. HAER's aggregate Apollo 11 display-request statistics cannot establish exact GUIDO request keys, per-format behavior, or timing.

A separate primary NASA source, Sullivan and Burbank, *Apollo Experience Report — Real-Time Display System*, NASA TN D-8316 (1976), narrows the timing question without supplying a mission-specific numeric cadence:

- console keyboard switch closures were encoded and held until operator initiation, then transmitted to the RTCC for action;
- the request word carried requester identification, request type, and request fields;
- D/TV display generators used full random-access buffer memories, allowing the computer to update displays without regard to CRT refresh requirements;
- the computer could update either a complete instruction list or a single data word;
- the cited four-second requirement concerns access/display of one of roughly one thousand **reference slides**, not dynamic telemetry update cadence.

Therefore **CRT refresh, dynamic-data update cadence, operator display-request latency, and reference-slide access time are distinct mechanisms**. No numeric Apollo 11 GUIDO/MSK-1137 dynamic update period is supported by these sources. In particular, neither the onboard two-second landing-radar component cadence nor the four-second reference-slide access requirement may be reused as a controller dynamic-data refresh period.

## Implementation consequence

The controller product must preserve separate provenance/timestamps for source observation, ground processing/product generation, and presentation. A renderer may retain a selected display while individual dynamic words change; it must not assume that every visual refresh requires a new display request. Numeric Apollo 11 display latency/freshness remains unimplemented until sourced or shown irrelevant at player-visible resolution under D-022.

## Research closure state

- **BLOCKED:** exact Apollo 11 mission-specific request workflow and usage/timing details that require PHO-TN401 or equivalent mission-era evidence.
- **SUFFICIENT for the current architecture boundary:** dynamic data update is not equivalent to CRT refresh or reference-slide access, and the simulator must keep these mechanisms distinct.
- **Reopen triggers:** authenticated PHO-TN401 access; another mission-effective Apollo 11 Display/Control or RTCC procedure; or an implementation that requires a numeric latency/update period.

## Sources

- B. Costis, W. Ortolani, W. Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, 24 Dec 1969. Identified archival holding: Box 078-65/66, Mission Documents: Apollo 11, Apollo Program, Johnson Space Center History Collection, University of Houston-Clear Lake.
- National Park Service / Historic American Engineering Record, *Johnson Space Center, Apollo Mission Control*, HAER TX-109-C. https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf
- Cornelius J. Sullivan and LaRue W. Burbank, *Apollo Experience Report — Real-Time Display System*, NASA TN D-8316, September 1976. https://ntrs.nasa.gov/citations/19760024152

## Evidence status

- **DOCUMENTED:** PHO-TN401 exists, is Apollo-11-specific, and is held in the cited JSC History Collection archival box.
- **DOCUMENTED SECONDHAND:** HAER reports aggregate Apollo 11 display-request/use statistics from PHO-TN401.
- **DOCUMENTED:** Apollo D/TV generators buffered display instructions/data so computer updates were independent of CRT refresh requirements; complete lists or single data words could be updated.
- **DOCUMENTED:** the four-second figure in TN D-8316 applies to reference-slide access/display, not dynamic telemetry update cadence.
- **BLOCKED:** direct inspection of PHO-TN401.
- **UNRESOLVED:** exact Apollo 11 GUIDO request/key workflow, per-field routing, numeric dynamic-data cadence/latency/freshness, and powered-descent format selection.