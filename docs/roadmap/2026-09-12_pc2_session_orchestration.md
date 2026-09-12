# Roadmap addendum — PC+2 integrated session orchestration

Date: 2026-09-12

## Completed before this transition

The first-pass player-facing presentation set is now complete enough for integrated play:

- [x] CONTROL
- [x] GUIDO
- [x] TELMU
- [x] FIDO/RETRO
- [x] INCO
- [x] FLIGHT
- [x] CAPCOM

Broad station/display expansion is no longer the immediate priority.

## Session integration — current checkpoint

- [x] define framework-neutral authoritative session core
- [x] monotonic synchronized GET
- [x] station/player assignment
- [x] per-station readiness reports
- [x] explicit FLIGHT decision event
- [x] queued callout distinct from CAPCOM crew transmission
- [x] ordered audit/replay events
- [ ] project readiness reports into FLIGHT player information
- [ ] project pending crew callouts into CAPCOM player information
- [ ] connect session FLIGHT decision to existing `flight.go_for_burn` product
- [ ] connect CAPCOM transmission to the existing procedural communication log
- [ ] provide one session snapshot that selects the correct station presentation for each assigned player
- [ ] validate nominal PC+2 sequence through readiness poll, crew GO, burn, shutdown report, and immediate post-burn transition

## After domain integration

Only then select/implement:

- [ ] server transport/API boundary
- [ ] synchronized multi-client update mechanism
- [ ] reconnect/resume semantics
- [ ] persistence needed for active sessions
- [ ] phone station-client shell
- [ ] administrative session controls

The transport framework remains intentionally undecided until the domain/session interface is stable.

## Historical constraints carried forward

- readiness reports are player/controller inputs, not hidden-health summaries;
- FLIGHT GO/NO-GO is an explicit decision;
- FLIGHT decision does not automatically transmit to the crew;
- CAPCOM is the crew-facing Mission Control communication boundary for this slice;
- callout transmission does not certify spacecraft response;
- exact internal voice-loop routing is not invented where the reviewed evidence does not establish it;
- player clients continue to consume controller-visible products, never authoritative physical state directly.

## Next item

Implement the **session-to-station product bridge**. This is the next unresolved item and should be completed before researching additional display detail or choosing a web framework.
