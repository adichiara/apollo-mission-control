# Roadmap addendum — PC+2 inverter ground-observation path

Date: 2026-09-13  
Status: **bounded archival refinement complete; physical validation priority unchanged**

## Resolved in this pass

Research note 116 establishes from NASA TN D-6845 / MSC-S-294 that the LM instrumentation system telemetered the electrical quantities behind the INVERTER caution:

- inverter-bus frequency `GC0155` → PCMTEA telemetry;
- inverter-bus voltage `GC0071` → PCMTEA telemetry;
- PCMTEA data proceed through communications to the MSFN;
- the onboard derived caution is separately identified as `GL4046` / `6DS26`.

This closes the question of whether a primary-source ground electrical-observation path existed without claiming that the onboard caution itself was directly telemetered or that an exact Apollo 13 TELMU/CONTROL display has been recovered.

## First-playable boundary

A station-facing inverter electrical product may use `GC0155` / `GC0071` as source-backed telemetry if it is labeled as a project rendering. Do not infer INV1/INV2 selector identity from those measurements, do not invent direct `GL4046` caution telemetry, and do not invent exact CRT routing, latency, or selection-inhibit duration.

## Remaining priorities

The canonical roadmap remains centered on physical validation:

1. seven-seat nominal PC+2 human/device run;
2. synthetic ΔP run after nominal coordination is coherent;
3. five-player compact human/device run;
4. reopen exact display/routing research only when validation exposes a concrete decision dependency.

The unresolved inverter details are now exact routing/display provenance, direct caution-discrete telemetry, selector-position ground visibility, ground cadence/latency, and numeric selection-inhibit duration. None is currently promoted to a first-playable blocker.
