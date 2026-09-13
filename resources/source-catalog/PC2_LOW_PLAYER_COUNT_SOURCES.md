# PC+2 low-player-count station-aggregation sources

Status: **IMPLEMENTATION-SOURCE — compact role boundary researched; multi-station domain ownership implemented; HTTP/UI wiring pending**

This supplement records the historical evidence used to constrain low-player-count station aggregation for the Apollo 13 PC+2 first playable. The resulting bundles are project adaptations, not claims about historical Apollo staffing.

## Primary sources

### Apollo 13 Press Kit

- NASA, 1970.
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_PressKit.pdf
- Relevant evidence:
  - CAPCOM is the crew voice contact;
  - TELMU/TELCOM and CONTROL are LM counterparts within Systems Operations;
  - FIDO, RETRO, and GUIDO belong to the Flight Dynamics Group;
  - INCO/O&P responsibilities are communications/procedures rather than crew voice.

Implementation use:

- supports choosing historically related functional domains when a project role must combine multiple stations;
- supports keeping CAPCOM distinct from technical communications engineering.

Does not establish:

- a five-player Apollo 13 staffing pattern;
- combined TELMU+CONTROL or GUIDO+FIDO/RETRO historical operators.

### Report of Apollo 13 Review Board — Mission Control organization / Appendix A material

- NASA, 1970.
- NTRS: `19700078804`.
- https://ntrs.nasa.gov/citations/19700078804
- Relevant evidence:
  - FLIGHT is responsible for Mission Control decisions/actions;
  - CAPCOM is responsible for voice communications with the crew;
  - CONTROL is responsible for LM guidance/navigation/control/propulsion;
  - TELMU/TELCOM is the LM electrical/environmental specialist;
  - FIDO, RETRO, and GUIDO are separate Flight Dynamics specialties;
  - INCO and O&P shared a console and responsibility, providing a real Apollo example of selected functional sharing.

Implementation use:

- supports preserving FLIGHT and CAPCOM as independent player roles in the recommended compact mode;
- supports retaining original station ownership even when one modern player UI presents more than one station.

### Report of Apollo 13 Review Board — main report organization figure

- NASA, 1970.
- NTRS: `19700076776`.
- https://ntrs.nasa.gov/citations/19700076776
- Relevant evidence: Mission Control organization chart separates Mission Command and Control, Systems Operations, and Flight Dynamics under the Flight Director.

Implementation use:

- provides the organizational basis for selecting the two compact technical bundles:
  - `LM SYSTEMS` = TELMU + CONTROL;
  - `FLIGHT DYNAMICS` = GUIDO + existing FIDO/RETRO.

The bundle names and one-player assignment are project abstractions.

### Mission Operations Report — Apollo 13

- NASA / MSC, 28 April 1970.
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- Separate post-mission controller appendices for FIDO, RETRO, GUIDO, TELMU, CONTROL, INCO, etc.
- Relevant evidence: station responsibilities remained independently documented even within common organizational groups.

Implementation use:

- supports retaining original station-scoped products, actions, readiness, and audit identity inside any bundle;
- supports the implemented model in which a compact player owns several original stations rather than a new synthetic historical station.

## Derived project boundary

Recommended compact PC+2 configuration: **five players**.

- FLIGHT
- CAPCOM
- LM SYSTEMS = TELMU + CONTROL
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO
- INCO

Historical station identity remains authoritative underneath the bundled UI.

The framework-neutral session layer now implements this semantic boundary through station-set ownership, station-qualified readiness/action authorization, and bundled snapshots containing separate original-station presentations. HTTP join/rejoin and browser presentation are still pending.

Four-player-or-smaller configurations remain unresolved. In particular, CAPCOM+INCO is not accepted merely because both concern communications: Apollo documentation distinguishes the crew-voice function from technical communications engineering.

See:

- `resources/research/091_low_player_count_station_aggregation_boundary.md`
- `resources/research/092_multi_station_player_ownership.md`
