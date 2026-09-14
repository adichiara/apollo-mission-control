# Contingency test item recovery defect — 2026-09-14

Live guided contingency validation exposed a state-recovery bug in `web/contingency.html`.

The page kept the CAPCOM shutdown `item_id` only in the in-page `itemId` variable or attempted to recover it from `controller_shutdown_callout_decision.details.item_id`. The audit event does not contain `item_id`; the authoritative queue event is `capcom_item_queued`. Switching from the admin screen back to the contingency screen therefore lost the in-memory item ID and Step 4 could report `No CAPCOM shutdown item exists yet` despite a valid shutdown item having been queued and transmitted.

Observed audit evidence from the live run:

- `controller_shutdown_callout_decision` was recorded without an `item_id`.
- `capcom_item_queued` immediately followed with `item_id: 1` and action `callout_dps_shutdown_criterion`.
- `capcom_item_transmitted` then transmitted that same item.
- A second CONTROL callout was subsequently made while troubleshooting, which created `item_id: 2`; the guided page should therefore avoid creating a duplicate shutdown item when one already exists.

The fix reconstructs the relevant shutdown item from the audit log whenever the page refreshes or is revisited. It prefers a transmitted-but-not-yet-received shutdown item, then a queued-but-not-yet-received shutdown item, then the latest shutdown item as a fallback. The guided CONTROL callout step also reuses an existing shutdown item instead of creating a duplicate.

This is a validation UI state-recovery defect; it does not indicate failure of the underlying queue/transmit chain.

The same live run also shows the session was manually resumed after the setup pause and subsequently reached nominal guided cutoff. That run is therefore not suitable for validating an in-burn contingency through physical engine shutdown; the contingency validation should be rerun after this UI fix while the clock remains paused at the setup point.
