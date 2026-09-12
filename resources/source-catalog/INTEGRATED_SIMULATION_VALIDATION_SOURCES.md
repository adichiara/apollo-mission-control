# Integrated simulation validation sources

Status: **IMPLEMENTATION-SOURCE**

This supplement supports the project's decision to validate several controller clients and a distinct facilitator/simulation-control surface together against one authoritative simulation. It does **not** claim that the project's HTTP/browser architecture is historical Apollo hardware or software.

## Primary historical sources

### Harold G. Miller — Simulation Training for Flight Control Decisionmaking

- NASA SP-209, 1970.
- NTRS document: `19700013438`.
- https://ntrs.nasa.gov/citations/19700013438
- Relevant evidence:
  - Mercury/Gemini/Apollo flight controllers manned consoles for monitoring/control of crew and spacecraft activity;
  - simulation training occurred in a mission environment;
  - final simulation exercises developed contingency handling and decision-making proficiency;
  - simulation supported verification of procedures and mission-facility readiness.

Implementation use:

- supports integrated rather than station-isolated validation;
- supports exercising controller information, decisions, and contingency handling together;
- supports treating readiness of the complete player-facing simulation path as a validation objective.

Does not establish:

- web/HTTP architecture;
- phone/browser polling cadence;
- exact software concurrency requirements;
- player authentication or facilitator-token behavior.

### NASA — Apollo Mission Control Center Restoration

- NASA Johnson Space Center history/restoration documentation.
- https://www.nasa.gov/johnson/history/apollo-mcc-restoration/
- Relevant evidence: the Simulation Control Room was a distinct support room adjacent to the Mission Operations Control Room and was used for simulations preparing teams for flight missions.

Implementation use:

- supports maintaining separate controller and facilitator/simulation-control surfaces during integrated validation.

Does not establish:

- the project's `/admin` interface;
- HTTP authorization details;
- one-to-one mapping between prototype validation actions and historical simulation-console controls.

## Derived project boundary

The primary sources support validating an integrated mission-like controller environment while preserving a distinct simulation-control function.

The project therefore tests multiple station clients and a facilitator against one shared authoritative state, while labeling transport, browser concurrency, and credential behavior as modern implementation infrastructure.

See `resources/research/089_multiclient_integrated_validation_boundary.md`.
