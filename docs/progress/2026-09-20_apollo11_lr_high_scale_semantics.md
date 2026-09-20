# Progress — Apollo 11 LR high-scale semantics

Date: 2026-09-20

## Question

What does LUMINARY 099's `SKALSKAL = .2 NOM` mean numerically, and can it establish the raw LM-5 high-scale landing-radar altitude conversion?

## Primary-source result

The flown LUMINARY 099 source already establishes a low-scale altitude representation of 1.079 ft/count and a conditional `SKALSKAL` rescaling path documented as `.2 NOM`.

MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B, Manned LM Earth Orbital and Lunar Program*, explicitly tabulates `DNLRALT` as:

- low scale: 0.3288792 m = 1.0790 ft/count;
- high scale: 1.64440 m = 5.3950 ft/count.

1.0790 / 5.3950 = 0.2 exactly at the stated precision. This provides a primary-source semantic explanation for the LUMINARY 099 `.2 NOM` comment: it is the low/high LR altitude scale-factor ratio.

## Boundary

MSC-69-FS-4 is Luminary 1B, not the flown Apollo 11 Luminary 1A build. It therefore strongly corroborates the interpretation and supplies a sourced candidate high-scale conversion, but does not alone prove that LM-5 used 5.3950 ft/count. The Apollo 11 prelaunch erasable-load table's `SKALSKAL = 00000` also remains unexplained as a run-time initialization fact; no numerical behavior is inferred from that zero.

No controller display, GUIDO procedure, stochastic error law, serial framing, or rounding rule is inferred.

## Next discriminating evidence

Seek Apollo-11-effective LM-5 radar/interface documentation or Luminary 1A guidance equations that directly state the high-scale altitude count value or raw encoding. Separately seek pad-load/initialization documentation explaining why the mission table records zero for an erasable whose source comment gives `.2 NOM`.

## Evidence status

- **DOCUMENTED:** `.2 NOM` semantics are consistent exactly with the primary Luminary 1B low/high count ratio.
- **STRONGLY BOUNDED, NOT YET APOLLO-11-EFFECTIVE:** 5.3950 ft/count high-scale conversion.
- **UNRESOLVED:** Apollo 11 zero-padload/run-time relationship; raw serial framing/bias/rounding.
- **BLOCKED:** stochastic historical LR measurement generator.
