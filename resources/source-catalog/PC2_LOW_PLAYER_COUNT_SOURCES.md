# PC+2 low-player-count station-aggregation sources

Status: **IMPLEMENTATION-SOURCE — five-player compact mode implemented; sub-five-player PC+2 reduction researched and not approved at current fidelity; physical compact play validation pending**

This supplement records the historical evidence used to constrain low-player-count station aggregation for the Apollo 13 PC+2 first playable. The resulting bundles are project adaptations, not claims about historical Apollo staffing.

## Primary sources

### Apollo 13 Press Kit

- NASA, 1970.
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A13_PressKit.pdf
- Mission Control Center section, scanned pp. 116–118.
- Relevant evidence:
  - CAPCOM is the crew voice contact;
  - TELMU/TELCOM and CONTROL are LM counterparts within Systems Operations;
  - FIDO, RETRO, and GUIDO belong to the Flight Dynamics Group;
  - INCO/CSE and O&P share responsibility for monitoring/troubleshooting spacecraft and lunar-surface communications and coordinating MCC procedures with the network.

Implementation use:

- supports choosing historically related functional domains when a project role must combine multiple stations;
- supports keeping CAPCOM distinct from technical communications engineering;
- constrains the four-player question because CAPCOM and INCO are explicitly different functions, not interchangeable communications labels.

Does not establish:

- a five-player Apollo 13 staffing pattern;
- combined TELMU+CONTROL or GUIDO+FIDO/RETRO historical operators;
- a CAPCOM+INCO historical pairing.

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
- supports retaining original station ownership even when one modern player UI presents more than one station;
- demonstrates that historical sharing was selective and does not by itself justify CAPCOM+INCO.

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
- NASA historical archive / Apollo mission-document collection.
- Separate post-mission controller appendices for FIDO, RETRO, GUIDO, TELMU, CONTROL, INCO, etc.
- Relevant evidence:
  - station responsibilities remained independently documented even within common organizational groups;
  - the selected PC+2 preparation interval includes communications loss/reacquisition context, final maneuver information to the crew, and high-bit-rate LM data during burn preparation;
  - communications/data-path behavior is therefore active scenario content rather than a safely ignorable background function.

Implementation use:

- supports retaining original station-scoped products, actions, readiness, and audit identity inside any bundle;
- supports the implemented model in which a compact player owns several original stations rather than a new synthetic historical station;
- weighs against silently omitting or automating INCO solely to reach four players.

### Mission Operations Control Room flight-controller assignments

- NASA History / Apollo Lunar Surface Journal archive.
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/flight_controller_assigns.pdf
- Relevant evidence: FIDO, RETRO, GUIDO, LM/TELMU, LM/CONTROL, INCO, CAPCOM, and FLIGHT leadership are separately enumerated Mission Control positions.

Implementation use:

- reinforces the requirement that compact transport/browser presentation keep the original call signs visible and independently attributable;
- does not establish any modern compact staffing arrangement.

## Derived project boundary

Minimum supported PC+2 configuration at the current fidelity target: **five players**.

- FLIGHT
- CAPCOM
- LM SYSTEMS = TELMU + CONTROL
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO
- INCO

Historical station identity remains authoritative underneath the bundled UI.

The session and HTTP layers implement this boundary through station-set ownership, exact-set rejoin, station-qualified readiness/action authorization, and bundled snapshots containing separate original-station presentations. The browser persists the station set and active substation and provides explicit original-call-sign navigation rather than a merged synthetic station display.

### Four-player result

Research note 094 closes the previously unresolved general four-player PC+2 question **without approving a four-player mode**.

CAPCOM+INCO is not accepted merely because both concern communications: Apollo documentation distinguishes crew-voice authority from technical communications-system monitoring/troubleshooting, and the selected PC+2 slice actively uses communications/data-path state. Silent INCO omission or facilitator automation would therefore remove scenario-relevant coordination rather than simply remove an idle seat.

Five is a project minimum for this scenario/fidelity target, **not** a historical Apollo minimum-staffing claim. A smaller mode may be reconsidered after live play, for a different scenario window, or as an explicitly lower-fidelity accessibility mode.

Physical five-player usability validation remains pending.

See:

- `resources/research/091_low_player_count_station_aggregation_boundary.md`
- `resources/research/092_multi_station_player_ownership.md`
- `resources/research/093_compact_http_browser_integration.md`
- `resources/research/094_pc2_four_player_boundary.md`
