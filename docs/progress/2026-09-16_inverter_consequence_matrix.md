# Progress — inverter consequence matrix

Date: 2026-09-16

Added isolated consequence probes for the source-backed PC+2 inverter contingency.

Cases:
- correct transfer + fresh continuing warning → rule triggers;
- omitted transfer + later warning → rule remains not evaluable;
- crew action attempted before explicit receipt → rejected and rule remains not evaluable;
- correct transfer + fresh clear observation → rule clears.

The 0.1-second increment used to distinguish action time from the fresh observation is test event ordering only. It is not a historical dwell, reaction-time allowance, or controller tolerance.

The proof runs through the authoritative PC2Session, CAPCOM transport, deterministic simulated crew, scenario observation injection, and the existing persistent-inverter-warning rule. No automatic engine shutdown is introduced.
