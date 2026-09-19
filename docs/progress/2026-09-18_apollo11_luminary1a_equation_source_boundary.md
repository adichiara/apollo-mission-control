# Progress — Apollo 11 Luminary 1A equation-source boundary

Date: 2026-09-18

The D-024 portfolio review leaves Apollo 11 powered descent as the active research exception. This pass addressed the first provenance problem before further equation extraction: identifying the correct Apollo 11-era programmed-guidance-equation source.

Resolved:

- the primary Mission G rendezvous report cites a May 1969 **Programmed Guidance Equations for Luminary 1A** document;
- MSC `69-FS-4` directly identifies that predecessor as **Internal Note 69-FS-3**;
- `69-FS-4` explicitly says it is a complete reissue of `69-FS-3` updated for **Luminary 1B**.

Therefore `69-FS-3`, not `69-FS-4` or later R-567 revisions, is the named primary equation target for the Apollo 11 / Luminary 1A reference. Later documents remain useful for comparison but do not establish Apollo 11 effectivity by themselves.

This is a provenance/effectivity advance only. No landing-radar equation, estimator rule, powered-descent constant, station display, or executable behavior was promoted.

Next dependency-driven retrieval: recover/open `69-FS-3` and inspect its landing-radar measurement/update and descent-guidance sections; if only `69-FS-4` is available, use it to locate candidate sections and explicitly identify the 1A→1B delta before admitting any equation into the Apollo 11 profile.

Sources:

- https://ibiblio.org/apollo/Documents/Mission_G_Rendezvous.pdf
- https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
