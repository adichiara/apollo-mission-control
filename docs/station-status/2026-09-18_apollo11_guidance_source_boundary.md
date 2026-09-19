# Station research status addendum — Apollo 11 guidance-source boundary

Date: 2026-09-18  
Parent: `docs/STATION_RESEARCH_STATUS.md`

The Apollo 13 station maturity table is unchanged. This addendum concerns the separate Apollo 11 powered-descent architecture reference now active under D-024.

## Guidance/flight-dynamics consequence

Primary-source control now identifies MSC Internal Note **69-FS-3**, *Programmed Guidance Equations for Luminary 1A Manned LM Earth Orbital and Lunar Program* (May 1969), as the correct named equation target for the Apollo 11-era reference. MSC `69-FS-4` is explicitly a later complete reissue updated for Luminary 1B.

Until `69-FS-3` is opened and the relevant pages are inspected:

- Apollo 11 landing-radar measurement/update equations remain unresolved;
- downstream estimator/filter details remain unresolved;
- powered-descent guidance constants/equations must not be imported from `69-FS-4` or later R-567 revisions solely because they are similar;
- controller-visible GUIDO/FIDO/CONTROL products should continue to be sourced independently from mission-specific operational/display evidence.

No station maturity grade changes from this pass.

## Sources

- Mission G rendezvous report: https://ibiblio.org/apollo/Documents/Mission_G_Rendezvous.pdf
- MSC `69-FS-4` page-change record: https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf
