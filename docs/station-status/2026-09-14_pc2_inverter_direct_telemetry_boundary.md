# Station status — PC+2 inverter direct caution / selector telemetry boundary

Date: 2026-09-14

## TELMU / CONTROL

Research note 117 narrows the remaining inverter information-boundary question using primary LM instrumentation schematics.

NASA TN D-6845 Figure 27 explicitly routes inverter-bus frequency `GC0155` and voltage `GC0071` to PCMTEA telemetry. It separately shows the derived `GL4046` / `6DS26` onboard INVERTER caution and the `4S14` selector/inhibit wiring without a labeled PCM telemetry tap for either caution state or selector position.

### First-playable consequence

TELMU/CONTROL may receive source-backed inverter-bus electrical measurements as a project-rendered station product. They should **not** receive a purported historical direct `GL4046` caution bit or independent INV1/INV2 selector-position telemetry unless a later primary source explicitly establishes such routing.

Selected-inverter identity remains available through the explicit crew procedure/action/report state. Onboard caution persistence likewise remains crew-observed/reported; ground electrical evidence is independently represented by `GC0155` / `GC0071`.

A controller-facing derived electrical warning may be calculated from sourced voltage/frequency limits only when clearly labeled as a project-derived aid rather than a recovered Apollo 13 caution discrete.

### Maturity

TELMU and CONTROL remain **B — Strong workflow**. The information boundary is now better constrained, but exact Apollo 13 station routing, CRT/MSK presentation, update cadence/latency, and numeric inverter-selection inhibit duration remain unresolved.

## CAPCOM / crew boundary

CAPCOM remains the crew-facing path for the contingency. Research note 117 does not add a new ground caution indication or selector-state source. The crew action/report sequence in notes 112–115 remains authoritative for transfer identity and onboard caution persistence.

## Evidence limit

The absence of labeled caution/selector PCM taps in the reviewed schematics is a bounded negative finding, not proof that no additional Apollo routing document could exist. No station is promoted and no physical-play PASS claim is added.