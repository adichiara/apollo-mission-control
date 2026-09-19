# Roadmap addendum — Apollo 11 Luminary 1A equation-source boundary

Date: 2026-09-18  
Parent: `docs/ROADMAP.md`

## Bounded question

Which primary programmed-guidance-equation document should anchor the open Apollo 11 powered-descent reference before later Luminary equation sets are used?

## Newly resolved

The primary Mission G rendezvous report cites **Programmed Guidance Equations for Luminary 1A Manned LM Earth Orbital and Lunar Program**, Flight Software Branch, Flight Support Division, **May 1969**. The surviving MSC `69-FS-4` page-change record independently identifies that predecessor as **MSC Internal Note 69-FS-3**, and states that `69-FS-4` is a complete reissue of `69-FS-3` updated for **Luminary 1B**.

This establishes `69-FS-3` as the correct named period target for Apollo 11 / Luminary 1A programmed guidance equations. It also establishes an effectivity guardrail: equations found only in `69-FS-4` or later Luminary documents must not be back-projected into the Apollo 11 reference without change-level corroboration.

## Roadmap consequence

The active Apollo 11 powered-descent work should now prioritize:

1. recover/open `69-FS-3` itself, or a source that reproduces its relevant pages with controlled provenance;
2. compare the landing-radar measurement/update and descent-guidance portions against `69-FS-4` to identify what changed for Luminary 1B;
3. use Apollo 11 mission-specific operational sources to constrain controller-visible products and decision rules;
4. keep later R-567/Luminary 1C/1E material as comparative evidence unless Apollo 11 effectivity is independently demonstrated.

No runtime equation, radar transform, station maturity, or executable Apollo 11 model is promoted by this bibliographic/effectivity result alone.

## Sources

- Mission G rendezvous report, primary mission-planning document; references section cites `Programmed Guidance Equations For Luminary 1A Manned LM Earth Orbital and Lunar Program`, Flight Software Branch, Flight Support Division, May 1969: https://ibiblio.org/apollo/Documents/Mission_G_Rendezvous.pdf
- MSC `69-FS-4`, *Programmed Guidance Equations for Luminary 1B, Manned LM Earth Orbital and Lunar Program*, page-change record: identifies `69-FS-3` as the May 1969 Luminary 1A predecessor and `69-FS-4` as its complete reissue updated for Luminary 1B: https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
