# Roadmap Addendum — PC+2 inverter transfer procedure

Date: 2026-09-13

Research note 114 closes the previously deferred cockpit-transfer chronology for the PC+2 inverter-warning branch.

Canonical first-playable sequence:

`PC+2 on inverter 2 → INVERTER caution → close CB(11) EPS: INV 1 → select INVERTER 1 → open CB(16) EPS: INV 2 → re-observe caution → if it remains, shutdown criterion satisfied`

The recovered Apollo 13 LM Malfunction Procedures do not supply a numeric post-transfer persistence interval. Crew-member assignment, exact controller voice wording, ground selector-position visibility, and exact TELMU/CONTROL display routing remain unresolved and non-blocking.

This archival closure does not change the immediate implementation priority: physical seven-seat nominal, synthetic ΔP, and five-player compact validation remain the next unclosed PASS boundaries.
