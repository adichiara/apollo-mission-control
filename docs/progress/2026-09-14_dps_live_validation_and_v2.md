# DPS live validation and suite v2

User-supplied report: dps-numerical-v1, 2026-09-14T16:57:44.386Z through
16:57:45.916Z. Render build 40e3bcff58795009d861da85a3c5e5501217da51 was
unchanged before/after. Ten cases, twelve PASS checks, no reported errors.
This is a summary of the report pasted in chat, not an independently rerun test
or an archived verbatim copy.

The report supports successful deployed numerical API/report workflow use.
It does not validate historical Apollo physics, live crew behavior, or mission
integration.

Suite v2 adds multi-segment thrust/direction changes with a zero-thrust interval,
an independent piecewise analytic vector comparison, split-profile invariance,
cutoff/coast comparison, and expected HTTP 400 propellant-limit rejection.
There are fourteen requests and sixteen checks. Existing export workflow applies.

Important: command changes here are specified at segment boundaries, not
interactive commands to a running mission. Propellant exhaustion is currently
rejected, not simulated as an automatic engine cutoff. No new depletion behavior
or historical restart eligibility is claimed. Live v2 validation is pending.
