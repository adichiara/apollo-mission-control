# 086 — Apollo 13 PC+2 shutdown-evidence HTTP integration

Date: 2026-09-12  
Status: **IMPLEMENTED — controller-observable evidence available without automatic engine-off verdict**

## Question

After an explicit crew shutdown command and physical DPS response, how should the existing source-bounded shutdown-evidence model be exposed through the authoritative session/API without leaking hidden physical state or inventing a chamber-pressure threshold?

## Primary-source check

The implementation was rechecked against the evidence already established in research note 070:

- Apollo 13 mission-operations material establishes thrust chamber pressure as a ground-monitored PC+2 rule quantity.
- The Apollo 13 air-ground record includes a crew shutdown report during the actual nominal PC+2 cutoff sequence, establishing crew voice as an independent controller-observable channel.
- Contemporary LM documentation identifies `GQ6510P` as thrust-chamber pressure.
- The Apollo 10 LM DPS final flight evaluation (NASA NTRS 19690026326) shows the `GQ6510P` measurement responding through ignition and shutdown, supporting its use as response evidence.

The Apollo 10 trace is **not** imported as Apollo 13 timing, tailoff, or a binary pressure threshold.

## Session integration

New `session_shutdown_evidence.py` provides two operations.

### Explicit crew report

`record_crew_shutdown_report(...)` records a semantic `shutdown` crew-report category at current authoritative GET after a crew shutdown command exists.

The semantic label is not asserted as the exact wording of the hypothetical nonnominal response.

### CONTROL evidence assessment

`assess_session_shutdown_evidence(...)`:

1. locates the authoritative crew shutdown-command GET;
2. locates a later explicit crew shutdown report, if present;
3. projects the normal CONTROL products;
4. takes the normal `dps.chamber_pressure_psi` product, if available;
5. calls the existing `assess_dps_shutdown_evidence(...)` aggregator.

Crucially, this helper does **not** inspect `state.engine_running`. Physical truth is therefore not leaked into the controller evidence result.

## HTTP integration

Added:

- `POST /api/session/crew/shutdown-report` — records the crew-report evidence channel;
- `GET /api/session/control/{player_id}/shutdown-evidence` — CONTROL-only evidence assessment.

The assessment returns only evidence availability:

- `none`;
- `crew_reported`;
- `ground_pressure_observed`;
- `corroborated`.

It does not return `engine_off_confirmed`.

## Freshness boundary

A chamber-pressure observation counts only when its observation/sample time is later than the crew shutdown-command GET.

A pre-command pressure value may remain numerically present in state, but it does not count as shutdown-response evidence.

This prevents stale pre-command data from masquerading as post-command confirmation.

## Threshold boundary

A fresh chamber-pressure observation is treated only as an independent evidence channel.

The integration deliberately permits a synthetic test in which a fresh **100 psi** observation produces `ground_pressure_observed`/`corroborated` evidence availability. That high value is intentionally useful: it demonstrates that the software is **not** interpreting a pressure magnitude as an engine-off threshold.

## Validation

`tests/test_web_shutdown_evidence.py` covers:

- pre-command pressure excluded from response evidence;
- crew shutdown report producing `crew_reported` evidence;
- fresh pressure plus crew report producing `corroborated` evidence;
- no `engine_off_confirmed` field;
- CONTROL-only access to the controller evidence endpoint.

Synthetic pressure values are explicitly non-historical.

## Next boundary

The source-bounded ΔP branch now reaches fresh controller-observable evidence end to end.

The next useful integration work is operational rather than additional DPS archaeology:

1. exercise the complete branch in a runnable multi-client environment;
2. review the phone UI for realtime operation and decide which validation/admin controls should remain hidden from normal players;
3. only reopen historical research if that integrated play exposes a concrete missing decision dependency.
