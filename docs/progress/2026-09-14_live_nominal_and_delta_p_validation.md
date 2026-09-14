# Live validation — nominal PC+2 and synthetic ΔP contingency

Date: 2026-09-14  
Status: **PASS for facilitator-driven live browser validation; multi-human station play remains pending**

## Scope

A live deployed browser session was exercised through the nominal Apollo 13 PC+2 timeline and, separately, through the source-bounded synthetic fuel/oxidizer ΔP contingency path. The runs used the facilitator/admin and guided contingency interfaces against the deployed application. These results validate the integrated runtime/API/browser chain; they do not constitute a seven-seat or five-player multi-human playtest.

## Nominal live validation

The nominal run completed the source-bounded PC+2 sequence from the 77:55 GET scenario start through immediate post-burn transition. Observed scheduled events included:

- 77:55 weak communications link;
- 77:55:24 final P30 LM PAD readup;
- 77:59:17 communications improvement;
- 78:00 final PC+2 solution ready;
- 78:12 LM burn-configuration powerup;
- 78:17 final load request/transmission;
- 78:21:54 ranging-switch verification;
- 78:23:05 computer returned to crew;
- 79:17 final GO/NO-GO gate and FLIGHT GO;
- 79:23 P40 active;
- 79:27:28.30 manual two-jet ullage;
- 79:27:38.30 DPS ignition;
- 79:27:43.30 40-percent throttle command;
- 79:27:51 crew 40-percent report;
- 79:28:04.30 maximum-throttle command;
- 79:28:09 crew 100-percent report;
- 79:32:02.12 guided cutoff;
- 79:32:41 post-burn residual review;
- approximately 79:34 LM power-down transition;
- approximately 79:52 PTC preparation.

Pause/resume, continuous GET behavior, station assignment/readiness, FLIGHT decision gating, CAPCOM queue/transmission, and audit recording were also exercised during validation.

## Synthetic ΔP contingency live validation

Final successful guided run audit established the following ordered chain:

1. synthetic `dps_fuel_oxidizer_delta_p_psi = 26` observation injected;
2. CONTROL applied the ground ΔP criterion and issued a shutdown callout;
3. a CAPCOM shutdown item was queued;
4. CAPCOM transmitted the item;
5. crew receipt was recorded separately;
6. crew DPS shutdown command was recorded;
7. the authoritative physical DPS engine-off response was applied;
8. crew shutdown report was recorded;
9. a fresh post-command chamber-pressure observation was injected at 100 psi;
10. CONTROL shutdown evidence returned `state = corroborated`.

The successful evidence result contained the crew report and fresh chamber-pressure observation but did not expose hidden authoritative engine truth. The deliberately high 100 psi synthetic pressure sample demonstrates that chamber-pressure magnitude is not being interpreted as a binary engine-off threshold; freshness after the command is the evidence property being exercised.

Observed final evidence values in the successful run:

- shutdown command GET: `286139.4650241677`;
- crew shutdown report GET: `286163.83909794036`;
- chamber-pressure observation: `100 psi`;
- chamber-pressure observation GET: `286163.9635030022`;
- evidence state: `corroborated`.

The CONTROL test-console presentation independently displayed the same controller-observable evidence.

## Validation defects found and repaired during the run

The live exercise exposed validation-interface defects that were repaired before the final PASS:

- facilitator token state did not initially survive cleanly across admin/test screens;
- the guided contingency page initially lost the CAPCOM shutdown item ID after screen switching/reload because it attempted recovery from the CONTROL decision event instead of `capcom_item_queued`;
- the guided test initially paused at 79:29 even though controller/crew command endpoints require a RUNNING session;
- the guided test initially omitted the fresh post-command chamber-pressure observation required for corroborated CONTROL evidence.

The final guided test leaves the simulation RUNNING, begins early enough to execute the chain before nominal cutoff, reconstructs the CAPCOM item from audit history, and supplies the same explicitly synthetic fresh pressure observation used by the network smoke test.

## Interpretation and remaining boundary

This closes the previously pending **facilitator-driven live deployed nominal and synthetic ΔP integration** boundary. It confirms the intended separation between source observation, controller interpretation, CAPCOM communication, crew receipt/action, physical vehicle response, and controller-observable evidence.

It does **not** close the physical multi-human play boundary. Still pending are simultaneous real-device station-player runs, human coordination/usability assessment, five-player compact substation switching under time pressure, packet findability, and player-facing presentation refinement.
