# Live human-play validation sources

Status: **IMPLEMENTATION-SOURCE — protocol boundary defined; physical execution pending**

This supplement supports the project's first real-device/human integrated play validation. It distinguishes historical Mission Control training principles from modern browser/mobile usability validation.

## Primary historical sources

### Martikan & Nassiff — Integrated operating mode of the Apollo mission simulator

- AIAA Paper 65-266.
- NTRS records: `19650039405` and `19660033487`.
- https://ntrs.nasa.gov/citations/19650039405
- https://ntrs.nasa.gov/citations/19660033487
- Relevant evidence: Apollo mission simulator integration with the Mission Control Center for combined flight- and ground-crew training.

Implementation use:

- supports validating the prototype as an integrated multi-role environment;
- supports treating isolated station testing as insufficient for the final first-playable boundary.

Does not establish:

- browser/mobile layout criteria;
- network latency limits;
- project facilitator authentication;
- exact prototype test sequence.

### Harold G. Miller — Simulation Training for Flight Control Decisionmaking

- NASA SP-209, 1970.
- NTRS document: `19700013438`.
- https://ntrs.nasa.gov/citations/19700013438
- Relevant evidence: simulation in a mission environment as final readiness training for flight controllers; emphasis on decisionmaking, controller interfaces, procedures, and adverse-condition response.

Implementation use:

- supports observing information acquisition, decisionmaking, coordination, and procedure use during live play rather than measuring only software correctness.

Does not establish:

- a historical Apollo usability questionnaire;
- exact pass/fail UI timing metrics;
- modern mobile-device behavior.

### Apollo training / mission simulator history

- NTRS document: `19720005243`.
- https://ntrs.nasa.gov/citations/19720005243
- Relevant evidence: integration of Apollo mission simulators with the Mission Control Center as a major step in realistic crew/ground-controller training.

Implementation use:

- supports requiring simultaneous human roles and a shared mission context for the live validation milestone.

## Supporting official NASA training doctrine

### Evolution of Training in NASA's Mission Operations Directorate

- NTRS document: `20120002563`.
- https://ntrs.nasa.gov/citations/20120002563
- Relevant evidence: NASA's later explicit "train like you fly" framing — replicating the operational environment and using the same operational mindset in training.

Implementation use:

- supports using the normal player/facilitator authority boundaries and continuous mission-time behavior during play validation rather than creating a special simplified test mode.

This later source is supporting doctrine, not evidence that the exact phrase or modern training method was used during Apollo.

## Derived project boundary

The live human-play run should validate:

- coherent shared mission time;
- separate station information/authority;
- distinct facilitator/simulation-control authority;
- human readiness and FLIGHT/CAPCOM coordination;
- phone/browser readability and rejoin behavior;
- explicit classification of defects as historical/research, simulation, UI, network, or instruction/training issues.

Modern browser, phone, HTTP, localStorage/sessionStorage, and token mechanics remain project infrastructure, not Apollo reconstruction.

See `resources/research/090_live_device_human_play_validation_boundary.md` and `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md`.
