# Apollo 13 GDA checkout sources

Date: 2026-09-15

## Apollo 13 mission-control loop — 61:29 free-return DPS checkout

- Mission: Apollo 13
- Relevant GET: approximately `061:08–061:12`
- Archive/navigation: https://apollo13realtime.org/
- Source class: primary mission-control voice record presented in synchronized mission archive

### Supports

- FLIGHT explicitly directs CONTROL to watch the gimbal trim during the DPS gimbal/throttle checkout.
- CONTROL observes the gimbal drive against the stop and return.
- CONTROL calls the trim GO and says it looks okay.
- When FLIGHT asks how close the observed result is, CONTROL answers **"within about 0.3"** and **"plenty close."**

### Boundary

Treat `~0.3°` as an observed/accepted **pre-61:29 checkout discrepancy**. The exchange does not identify it as an RTCC mass-properties trim-update tolerance and does not connect it to the later PC+2 no-trim decision.

The same controller record contains an immediate post-burn `0.2` trim exchange with GUIDANCE. It is not explicitly identified as a GDA angle residual. Do not classify it as a GDA state, GDA comparison tolerance, or PC+2 trim value without corroborating primary evidence.

## Cross-reference

- `resources/research/166_mcc3_nomenclature_and_gda_state_continuity.md`
- `resources/research/167_free_return_gda_test_acceptance_bound.md`
- `resources/source-catalog/PC2_DPS_PERFORMANCE_SOURCES.md`

## Retrieval priority

Continue searching controller/RTCC/RTACF working records for the distinct PC+2 mass-properties comparison: post-61:29 complied GDA state, candidate PC+2 trim, delta/criterion, job identity, and T+55 deck provenance.