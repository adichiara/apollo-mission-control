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
- [x] bind the session to authoritative PC+2 state and deterministic scenario events
- [x] monotonic forward GET and session lifecycle
- [x] unique station/player assignment
- [x] station-scoped view selection from existing controller projections/presentations
- [x] per-station readiness reports with audit history
- [x] intercept the nominal 79:17 GO/NO-GO event as an explicit player gate
- [x] explicit FLIGHT decision drives normal `state.flight_go` / FLIGHT product state
- [x] queued FLIGHT callout remains distinct from CAPCOM crew transmission
- [x] ordered audit/replay events
- [ ] project readiness reports into FLIGHT player information
- [ ] project pending approved callouts into CAPCOM player information
- [ ] connect CAPCOM transmission to the existing procedural communication log
- [ ] validate nominal PC+2 sequence through readiness poll, crew-facing GO, burn, shutdown report, residual review, and immediate post-burn transition

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

Implement the remaining **session-derived FLIGHT/CAPCOM product bridge**: readiness reports for FLIGHT, pending approved callouts for CAPCOM, and CAPCOM transmission into the existing procedural-communication log. Then run the first fully integrated nominal PC+2 session validation before selecting a network framework.
