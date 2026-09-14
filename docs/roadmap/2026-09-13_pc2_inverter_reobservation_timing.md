# PC+2 inverter re-observation timing — roadmap addendum

Date: 2026-09-13

## Resolved boundary

Research note 115 closes the first-playable question of whether the inverter shutdown criterion requires a numeric crew persistence wait after transfer to the alternate inverter.

The Apollo 13 *LM Malfunction Procedures* places the `INVERTER lt — off?` evaluation directly after the alternate-inverter transfer sequence and specifies no numeric dwell. NASA LM instrumentation documentation separately places normal inverter-selection transient suppression in spacecraft caution/inhibit logic for the LM-5-and-subsequent configuration family.

First playable therefore uses:

`transfer complete → inverter indication transitioning/not yet valid as required → fresh valid caution state → caution remains = shutdown criterion satisfied`

No arbitrary persistence timer is historicalized.

## Still unresolved

- exact inverter-selection inhibit duration;
- exact telemetry/ground-display latency;
- exact TELMU/CONTROL field or routing;
- independent ground visibility of selector position;
- crew-member assignment and exact voice wording.

These do not currently block first playable.

## Priority consequence

This archival refinement does not alter the main roadmap priority. The next PASS boundaries remain physical seven-seat nominal play, synthetic ΔP play, and five-player compact play on real clients/devices.
