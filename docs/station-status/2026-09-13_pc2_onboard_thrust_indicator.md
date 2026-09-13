# Station status — PC+2 onboard thrust indication

Date: 2026-09-13

## CONTROL

Maturity remains **B**.

New evidence clarifies the separation between the crew and ground thrust observations during PC+2:

- ground: CONTROL/Mission Control chamber-pressure criterion remains a distinct ground product;
- onboard: crew actual-thrust monitoring is now constrained to the LM panel-1 dual-scale CMD THRUST / ENG THRUST instrument family;
- ENG THRUST is the source-backed actual-engine-thrust percent scale and is derived from a chamber-pressure transducer.

This does **not** establish that CONTROL saw the crew's ENG THRUST pointer, nor does it authorize mirroring the crew gauge into a ground display.

## CAPCOM

Maturity remains **B**.

The 76:30 GET rule read-up is now linked to a concrete crew-station instrument family rather than an unidentified “thrust monitor” concept. CAPCOM still communicates the rule; CAPCOM does not acquire a private propulsion measurement from the crew gauge.

## Crew boundary

The crew remains a scenario-authored external actor. If the first playable ever exercises the 77-percent rule, the correct information path is conceptually:

`DPS actual thrust → chamber-pressure-derived ENG THRUST indication → crew observation/report/action → CAPCOM/ground consequence`

The current executable model does not fabricate that observation path.

## Remaining gap

The exact startup applicability gate for the 77-percent limit remains unresolved because PC+2 intentionally begins at 12.6 percent and 40 percent thrust before maximum thrust.

No station maturity grade changes from this research pass.
