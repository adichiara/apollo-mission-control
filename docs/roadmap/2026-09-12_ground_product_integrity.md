# Roadmap addendum — ground-product integrity

Date: 2026-09-12

This addendum advances the active Phase 5 Mission Control data-path work from observation age/freshness into **ground-product integrity**.

## Completed checkpoint

- [x] Identify a mission-specific Apollo 13 case where source/spacecraft state remained satisfactory but a ground-derived product was wrong.
- [x] Bound the post-MCC-5 RTCC/AGS body-angle case without inventing erroneous values or an automatic validity flag.
- [x] Separate product availability/declared validity from hidden simulation integrity.
- [x] Add a generic wrong-but-present ground-product helper.
- [x] Add independent-reference and controller-detection test coverage.
- [x] Keep the historical case outside the PC+2 nominal timeline.

## Active next work

- [ ] Integrate integrity annotations with common station product/audit structures without exposing hidden integrity to players.
- [ ] Represent controller suspicion/rejection as a decision/audit event rather than silently changing the product.
- [ ] Add a complete architecture validation fixture: correct source → incorrect ground transformation → conflicting independent reference → controller rejection.
- [ ] Only after that, resume PC+2-specific nonnominal paths where source evidence is sufficient.

## Constraints retained

- No hidden `CORRECT/INCORRECT` label may appear in player-facing UI unless historically documented.
- A wrong product is not automatically `INVALID`; the Apollo 13 case demonstrates that controller cross-checking may be required.
- No erroneous AGS body-angle numbers are reconstructed without a source.
- Ground-processing failure must not mutate the underlying spacecraft state or raw telemetry unless the scenario separately specifies such a fault.

This addendum supplements `docs/ROADMAP.md`; the main roadmap remains authoritative for phase definitions and broader project sequencing.
