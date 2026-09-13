# 091 — Low-player-count station aggregation boundary

Date: 2026-09-12  
Status: **RESEARCHED — compact PC+2 role bundles defined as project adaptations**

## Question

How can the Apollo 13 PC+2 first-playable station set be reduced for fewer human players without silently rewriting historical controller responsibilities or collapsing important authority/information boundaries?

## Primary-source findings

### Apollo 13 organizational grouping

The Apollo 13 Press Kit and Apollo 13 Review Board organization material separate Mission Control into functional groups rather than treating every console as interchangeable.

The **Flight Dynamics Group** contains:

- FIDO — trajectory/powered-flight monitoring and maneuver planning;
- RETRO — abort/reentry planning and landing/impact consequences;
- GUIDO — guidance monitoring, spacecraft initialization, DSKY/computer updates.

The **Systems Operations Group** contains spacecraft-systems positions including:

- TELMU/TELCOM — LM electrical/environmental systems;
- CONTROL — LM guidance/navigation/control and propulsion systems.

The Apollo 13 Review Board also records that **INCO and O&P shared a console and responsibility**, demonstrating that physical console/functional sharing existed in Apollo, but this specific historical pairing does **not** justify arbitrary combinations among other stations.

### Authority boundaries

The same Apollo 13 organization material keeps:

- **FLIGHT** as the position responsible for Mission Control decisions/actions;
- **CAPCOM** as the spacecraft communicator responsible for voice communication with the crew.

Those are not merely subject-matter specialties. They are distinct authority/communication functions and should remain separate in the game unless later evidence and playtesting justify a deliberate, explicitly non-historical simplification.

## Design conclusion

Low-player-count aggregation is a **project usability adaptation**, not a historical reconstruction of Apollo manning.

The safest first compact configuration is **five human players**:

1. **FLIGHT** — unchanged.
2. **CAPCOM** — unchanged.
3. **LM SYSTEMS** — combines TELMU + CONTROL player surfaces.
4. **FLIGHT DYNAMICS** — combines GUIDO + existing FIDO/RETRO player surfaces.
5. **INCO** — unchanged.

This preserves the two highest-risk authority boundaries while using Apollo's own functional group structure to choose the least-arbitrary technical combinations.

## Required semantic preservation

A combined player role must not merge the underlying station models.

For every bundled role:

- TELMU and CONTROL retain separate source products, alerts, readiness judgments, actions, and audit identities;
- GUIDO and FIDO/RETRO retain separate source products, readiness judgments, and audit identities;
- information available to one component station is not automatically reclassified as information historically available to the other;
- rules and action authorization continue to use the original station identity;
- UI aggregation may present multiple station panels to one player, but the domain layer should still know which original station owns each field/action;
- historical call signs should remain visible at the subpanel/action level where practical.

## Why not merge FLIGHT or CAPCOM in the recommended compact mode?

Merging FLIGHT with a technical specialty risks combining final decision authority with the station supplying the recommendation.

Merging CAPCOM with a technical specialty risks combining technical diagnosis with the privileged crew-facing voice path.

Either change could remove coordination that is central to the Mission Control experience. The current evidence does not justify that simplification as the default compact mode.

## INCO treatment

INCO remains independent in the recommended five-player mode.

Apollo sources place communications engineering in Systems Operations / mission-command support and distinguish it from CAPCOM's crew-voice function. Combining INCO with CAPCOM may be technically possible as a later four-player project mode, but it would be a stronger abstraction and is **not approved by this research note**.

## Player-count tiers

### Seven-seat/full first-playable mode

Current station set:

- FLIGHT
- CAPCOM
- CONTROL
- TELMU
- GUIDO
- FIDO/RETRO
- INCO

This remains the highest-fidelity first-playable configuration.

### Five-player compact mode — recommended

- FLIGHT
- CAPCOM
- LM SYSTEMS = TELMU + CONTROL
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO
- INCO

This is the first aggregation target for implementation after the live seven-seat protocol is exercised or when a smaller group is required.

### Four players or fewer — unresolved

No four-player-or-smaller configuration is accepted yet.

Possible future approaches include:

- CAPCOM + INCO as a project communications bundle;
- facilitator automation of a low-activity station;
- scenario-specific omission of a station whose information/actions are not active in that scenario window.

Each would require explicit analysis of lost coordination, authority, and information-boundary effects. Do not silently hide or auto-resolve a station simply to hit a player-count target.

## Historical claim boundary

Supported historical claims:

- Apollo organized FIDO/RETRO/GUIDO under Flight Dynamics;
- Apollo organized LM systems specialists within Systems Operations;
- FLIGHT and CAPCOM had distinct decision/voice functions;
- at least one Apollo pairing, INCO + O&P, shared a console/responsibility.

Not supported and therefore not claimed:

- that one Apollo controller simultaneously performed TELMU + CONTROL during Apollo 13 PC+2;
- that one Apollo controller simultaneously performed GUIDO + FIDO/RETRO;
- that five controllers historically manned the PC+2 interval in this bundled arrangement;
- that Apollo used the labels `LM SYSTEMS` or bundled `FLIGHT DYNAMICS` as player roles in this sense.

Those are simulator design choices constrained by historical organization.

## Implementation implications

The current one-player/one-station session assignment should eventually be generalized to **one player owning one or more original stations**, not replaced by new synthetic station identities throughout the domain model.

Preferred implementation shape:

```text
player identity
  -> assigned station set
       -> original station-scoped snapshots/actions/readiness
  -> bundled player presentation
```

This minimizes risk of leaking data between historical stations and keeps existing tests/action authorization reusable.

## Sources

1. *Apollo 13 Press Kit*, NASA, 1970 — Mission Control position descriptions and Systems Operations / Flight Dynamics groupings.
   - https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_PressKit.pdf
2. *Report of Apollo 13 Review Board*, Appendix A / Mission Control organization material, NASA, 1970, NTRS `19700078804`.
   - https://ntrs.nasa.gov/citations/19700078804
   - documents FLIGHT/CAPCOM responsibilities, Systems Operations positions, INCO/O&P console sharing, and FIDO/RETRO/GUIDO responsibilities.
3. *Report of Apollo 13 Review Board*, main report, NASA, 1970, NTRS `19700076776` — Mission Control organization figure placing Mission Command and Control, Systems Operations, and Flight Dynamics as distinct groups under the Flight Director.
   - https://ntrs.nasa.gov/citations/19700076776
4. *Mission Operations Report — Apollo 13*, 28 April 1970 — separate controller post-mission appendices reinforce station-specific responsibilities.

See `resources/source-catalog/PC2_LOW_PLAYER_COUNT_SOURCES.md`.
