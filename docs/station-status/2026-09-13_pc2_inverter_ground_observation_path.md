# Station status — PC+2 inverter ground-observation path

Date: 2026-09-13

## TELMU / CONTROL

Research note 116 adds a primary-source ground-data boundary for the inverter criterion.

NASA LM instrumentation documentation explicitly routes inverter-bus frequency **`GC0155`** and voltage **`GC0071`** to PCMTEA telemetry and onward through the communications/MSFN path. The onboard INVERTER caution is a separate derived indication identified as **`GL4046` / `6DS26`**.

### Station consequence

For first playable, TELMU/CONTROL may receive source-backed inverter-bus electrical measurements as a project-rendered ground product. This is stronger than treating all inverter evidence as crew-only.

Do not claim a recovered Apollo 13 ground INVERTER caution light, direct selector-position telemetry, or a specific CRT/MSK field. The reviewed source does not establish those paths.

### Maturity

TELMU and CONTROL remain **B — Strong workflow**. The new evidence improves data provenance but does not recover exact Apollo 13 station routing/display, update cadence, selector visibility, or console workflow.
