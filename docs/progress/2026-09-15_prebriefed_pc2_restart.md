# Progress — prebriefed PC+2 restart integration

Date: 2026-09-15

The deterministic crew layer now distinguishes live CAPCOM-driven actions from procedures briefed before the playable window.

For the Apollo 13 PC+2 premature-stop branch:

- restart eligibility remains a separate conservative classification;
- listed shutdown rules override a contradictory non-rule flag;
- unknown cause remains ineligible;
- the prebriefed sequence is preserved as PRO on Noun 97, manual ullage, Engine Start, and Descent Engine Command Override on;
- crew steps do not restart the engine;
- successful engine-on response remains a separate explicit vehicle event;
- no post-stop FLIGHT approval or CAPCOM transmission is invented.

Facilitator validation endpoints expose premature stop, crew procedure execution, and the separate physical restart response. HTTP integration tests cover eligible, unknown-cause, and rule-caused branches.


## Site-facing validation

The deployed `/contingency` validation page now includes a **Premature DPS stop / prebriefed restart chain** alongside the ΔP and inverter tests.

The guided positive path verifies:

`premature stop with affirmative non-rule cause`
→ `RESTART_ELIGIBLE`
→ `prebriefed four-step crew procedure`
→ `explicit physical DPS restart response`

The page also exposes two negative branch checks:

- unknown cause → `INSUFFICIENT_CONTEXT` and procedure blocked;
- listed shutdown criterion present → `DO_NOT_RESTART_RULE_SHUTDOWN` and procedure blocked.

The browser check explicitly verifies that no post-stop CAPCOM queue/transmission is inserted. This preserves the historical boundary that the procedure was already briefed to the crew before the burn.
