# Progress — playability instrumentation and LMS blocker scope

Date: 2026-09-19

## LMS research-state correction

D-024 now distinguishes two different questions that had been collapsed into one DEFERRED handbook thread:

- generic LMS architecture/output/acceptance retrieval remains dependency-triggered and mostly **DEFERRED**;
- the narrower capability to claim or reconstruct a **specific historical LMS-injectable malfunction / instructor script** is **BLOCKED** on inaccessible primary Volume II Section 2 **Malfunction Data** and/or Section 6 **Scripting Data Sheets**.

This BLOCKED state is scoped. It does not block current PC+2 validation, player-lab work, or the generic causal architecture. It does put Virginia Tech Section 2/6 retrieval/digitization on the critical path if the project selects a specifically historical LMS SimSup/non-nominal case or wants an affirmative injectability claim.

Section 7 output tables and NASA RG 255 acceptance material remain separate bounded questions rather than being swept into the same blocker.

## Note-314 instrumentation

A session-scoped playability stream now exists separately from the authoritative mission audit.

Both `/` and `/player-lab` record:

- page load;
- join attempt/success;
- automatic rejoin attempt/success/failure;
- workspace ready;
- action attempt/success/error.

The original validation client additionally records compact-role original-station switching.

Each event includes authoritative GET and client elapsed time. The stream intentionally excludes free-text readiness notes and decision/approval bases.

Facilitator retrieval:

`/api/session/admin/playability-events`

The facilitator LOG drawer includes **COPY PLAYABILITY LOG**.

## Interpretation boundary

The instrumentation can measure interaction timing, retries, failures, switching, and recovery. It does not determine why a player was slow or whether a controller judgment was correct.

Findability and operational/interface-friction classification remain observer judgments paired with the event stream.

See:

- `docs/testing/PLAYABILITY_INSTRUMENTATION.md`
- `docs/testing/PLAYER_LAB_PART_TASK_CHECKOUT.md`
- `docs/testing/PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`
