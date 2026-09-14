# Progress — PC+2 inverter transfer procedure

Date: 2026-09-13

## Completed

Recovered a direct Apollo 13-era cockpit procedure for the previously unresolved PC+2 inverter transfer.

The Apollo 13 *LM Malfunction Procedures* INVERTER caution flowchart gives the alternate-inverter selection sequence, with inverter 2 as the operating source:

1. close `CB(11) EPS: INV 1`;
2. set `INVERTER` to `1`;
3. open `CB(16) EPS: INV 2`;
4. re-observe whether the INVERTER caution has cleared.

This sequence fits the mission-specific PC+2 inverter-2 starting configuration already established in research note 112 and removes the remaining need to represent the transfer as an unnamed/generic switch action.

## Evidence boundary

No numeric persistence dwell, crew-member assignment, exact controller-to-CAPCOM wording, independent ground visibility of selector position, or exact TELMU/CONTROL telemetry/display field was recovered. Those details remain unfrozen.

## Documentation updates

- added research note 114;
- updated the inverter source catalog;
- updated `docs/OPEN_QUESTIONS.md` and canonical roadmap;
- added a station-status record and roadmap addendum;
- updated the research index / resource README and PR description.

## Validation impact

No physical-play PASS claim is added. Seven-seat nominal, synthetic ΔP, and five-player compact human/device validation remain the principal unclosed validation boundaries.
