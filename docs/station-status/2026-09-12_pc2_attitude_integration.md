# Station status addendum — PC+2 attitude projection integration

Date: 2026-09-12

## CONTROL — remains B

Newly implemented:

- optional three-axis `vehicle.attitude_error_xyz_deg` projection;
- optional three-axis `vehicle.body_rate_xyz_deg_s` projection;
- source/provenance metadata for both observation families;
- integrated shutdown-rule evaluation against the documented ±10 deg and ±10 deg/s operational thresholds;
- explicit handling of the unresolved startup-transient context without deriving it from elapsed time or throttle phase.

Primary-source support now covers the full information-contract chain at a bounded level:

`modeled observation → CONTROL product → PC+2 rule audit`

Still unresolved:

- exact LM-7 PCM word assignments;
- engineering conversion/calibration path;
- exact MSK/CRT fields used by CONTROL during PC+2;
- exact source/definition of the operational startup-transient interval.

Those gaps prevent promotion to maturity A.

## GUIDO — remains B

No duplicate attitude/rate products were added to GUIDO. Existing evidence supports guidance relevance but does not yet establish which PC+2 attitude/rate observations GUIDO independently used versus CONTROL. Preserving that boundary is preferable to sharing CONTROL data for convenience.

## CAPCOM — remains B

The contemporaneous CAPCOM read-up and crew readback remain the operational evidence used to allocate the startup-transient exception to attitude error in the executable rule. Exact procedure-card/staging evidence is still incomplete.

## Evidence conflict status

The contradiction is now independently supported on both sides:

- Mission Operations Report and Apollo 13 Review Board appendices: exception attached to attitude rate;
- CAPCOM read-up and Haise readback: exception attached to attitude error.

No source reviewed in this pass defines the transient duration. Station maturity therefore remains unchanged.
