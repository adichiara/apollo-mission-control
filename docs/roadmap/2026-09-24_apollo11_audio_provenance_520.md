# Roadmap update — Apollo 11 descent audio provenance

Date: 2026-09-24
Research note: 520
Parent: `docs/roadmap/2026-09-24_apollo11_flight_loop_recovery_519.md`

## Change

The descent-alarm audio task now has an explicit clock/channel evidence gate. Historical Recorder #1 provides separate FLIGHT, CAPCOM, and GUIDO L/R channels and an IRIG-B GMT timing channel. Therefore catalog time, player elapsed time, IRIG-B/GMT, and mission GET must not be silently merged.

## Next unresolved item

Directly inspect the historical Flight Director descent audio (`792-AAI`) at the note-516/518 alarm windows, establish a reproducible clock offset to mission GET, then compare the corresponding GUIDO L/R material. Record exact audible wording only after direct verification.

## Still blocked / open

- Mission-G GUIDO keyset and named support-room circuit identity.
- PHO-TN401 archival recovery.
- Exact Garman→Bales internal timing and wording.
- Any claim that L/R labels correspond to a particular listening/transmit function beyond the recorder labels themselves.

## Evidence status

- **READY:** audio-channel provenance and timing-discipline rule.
- **NEXT:** direct audio inspection and clock reconciliation.
