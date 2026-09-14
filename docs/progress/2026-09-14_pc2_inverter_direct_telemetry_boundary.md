# Progress — PC+2 inverter direct caution / selector telemetry boundary

Date: 2026-09-14

## Completed

Continued from research note 116's source-backed inverter-bus voltage/frequency path and targeted the next unresolved information-boundary question: whether the derived `GL4046` INVERTER caution or INV1/INV2 selector position had a direct ground telemetry path.

Primary schematic review of NASA TN D-6845 Figure 27 found explicit PCMTEA telemetry taps for inverter-bus frequency `GC0155` and voltage `GC0071`. The same figure shows `GL4046` / `6DS26` as the derived onboard caution path and `4S14` in the selector/inhibit logic, but does not show a labeled PCM telemetry tap for either the caution output or selector position.

## Result

Research note 117 records a bounded negative finding rather than inventing a missing signal:

- use `GC0155` / `GC0071` as the source-backed ground electrical evidence;
- keep `GL4046` / `6DS26` as an onboard crew indication unless a later primary source explicitly establishes direct caution-discrete telemetry;
- keep selected-inverter identity tied to the explicit crew procedure/action/report path rather than hidden selector telemetry;
- any derived ground warning from voltage/frequency must be labeled as a project-derived aid, not a recovered Apollo 13 caution discrete.

The absence of labeled taps in the reviewed schematics is not asserted as universal proof that no other Apollo routing document could exist. It is sufficient to prevent the first playable from claiming those direct paths.

## Repository consequence

Added research note 117 and a dated station-status/roadmap record; the active inverter source catalog and canonical tracking are reconciled to the same information boundary.

## Validation consequence

No physical-play PASS claim changes. Seven-seat nominal, synthetic ΔP, and five-player compact human/device validation remain the principal unclosed boundaries.