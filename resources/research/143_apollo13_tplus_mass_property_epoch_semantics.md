# 143 — Apollo 13 T+N mass-property epoch-semantics boundary

## Question

Does mission-specific Apollo 13 evidence narrow the meaning of the `T+55` LM-burn mass-property deck label beyond the general conclusion that it was an in-flight updated operational state?

## Primary source

NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970.

NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf

## Mission-specific sequence

The Flight Dynamics mission narrative uses a repeated `T+N` convention for mass-properties products:

- prelaunch, **lift-off (`T-6`) mass properties** — weights, centers of gravity, and aerodynamic data — were generated and loaded into the RTCC by `T-2:46`;
- later, **`T+25` RTCC mass properties were run**, but no update was required because pitch/yaw trims were within 0.01 degree of the **`T+6`** values;
- before the abort-maneuver work, RTCC **LM-burn mass-property decks were updated to `T+55` decks**;
- during PC+2 preparation, Flight Dynamics rejected LM Control's use of **premission mass properties** as not the best data available for the DPS trim.

The report separately uses mission-time notation such as `T+24 hr telescope data`, while the flight narrative is organized in GET. This makes the mass-property labels part of a broader mission-relative time convention rather than arbitrary revision letters.

## What this establishes

Within the Apollo 13 Flight Dynamics record, `T-6`, `T+6`, `T+25`, and `T+55` are successive time-tagged mass-properties bases/products. The `T+25` run explicitly tests whether the newer state warrants replacing the earlier `T+6` trim basis; the later `T+55` LM-burn update likewise represents a later mission-relative mass-properties basis.

For project purposes, it is now reasonable to interpret **`T+55` as a mass-properties state/deck associated with approximately mission time +55 hours**, rather than merely an opaque configuration identifier.

That interpretation is supported by the mission-specific sequence itself and does not depend on adjacent-mission inference.

## Evidence boundary

The source still does **not** establish:

- whether `T+55` means an exact 55:00:00 GET state, a nominal calculation epoch near +55 hours, a deck generated at that time, or a propagated state referenced to that time;
- the deck generation/update timestamp;
- the H-2 deck record layout or individual weights, centers of gravity, inertias, or aerodynamic fields;
- which RTCC/ACF program generated or consumed each field;
- the exact transformation from the `T+55` deck to the PC+2 trim or final P30 CSM/LM weight pair;
- whether the P30 weights equal physical spacecraft mass at ignition.

Accordingly, project documentation should replace the stronger unresolved statement "exact meaning of `T+55` is unknown" with the narrower statement: **the mission-relative epoch sense is established, but the precise epoch convention and deck semantics remain unresolved**.

## Model consequence

Represent the PC+2 Flight Dynamics mass-properties input as a mission-time-tagged operational state with a historical label of `T+55`. Preserve separate fields/concepts for:

1. mission-relative deck epoch label;
2. deck generation/update time, if later recovered;
3. physical vehicle mass/CG state;
4. targeting/P30 weights;
5. controller-visible trim/trajectory products.

Do not force `T+55` to an exact 55:00:00 state until an H-2 RTCC/Flight Dynamics definition, deck listing, or equivalent primary source establishes that convention.

## Next archival target

The highest-value remaining mass-properties target is no longer the broad question of whether `T+55` is time-related. It is the **precise H-2 RTCC/Flight Dynamics epoch convention and deck contents**: documentation defining whether the label denotes calculation epoch, propagated-state epoch, scheduled mission-time state, or another time-tagged convention, plus the LM-burn deck fields used for PC+2.