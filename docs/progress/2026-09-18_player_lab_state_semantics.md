# Progress — player lab state semantics

Date: 2026-09-18

## Completed

A second playability audit of the FLIGHT/CAPCOM `/player-lab` found four pieces of project-internal state that should not become controller-facing concepts by accident.

### Removed from the player surface

- session `pending_gate` is no longer rendered;
- raw state-machine phase strings are converted to readable phase labels;
- the ambiguous `flight.go_for_burn` Boolean is no longer presented as a player indication;
- the join/setup form collapses once a position is established or automatically rejoined.

## Why the FLIGHT Boolean was removed

The current domain state uses `flight_go = False` both before any FLIGHT disposition and after an explicit NO-GO. A UI rendering of `false` as “NO” would therefore invent a decision that may not have occurred.

The authoritative FLIGHT action remains explicit. If player-facing decision status is later required, it needs an unambiguous domain representation such as pending / GO / NO-GO or an event-derived recorded-decision state.

## Boundary

These changes affect only the non-final player interaction lab.

They do not change:

- the PC+2 domain/state machine;
- FLIGHT authority;
- the validated `/` integration client;
- scenario timing or decision-gate enforcement;
- historical station products.

## Next

Use the lab to validate the FLIGHT/CAPCOM coordination sequence under continuous GET before adding more stations. CONTROL/GUIDO should not be added merely to increase surface area; their next prototype should follow evidence from this interaction test plus their station-product scanning needs.
