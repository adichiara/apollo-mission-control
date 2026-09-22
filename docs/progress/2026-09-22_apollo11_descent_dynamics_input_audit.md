# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the next unresolved LM-5 descent inputs against primary Apollo documentation, preserving the distinction among design values, planned/commanded behavior, as-flown telemetry, reconstructed trajectory, and model inputs.

### PDI mass search narrowed to the correct primary table class

The Apollo 11 final Flight Plan documents an **unmanned LM weight of 33,278.3 lb** in its SPS budget assumptions and separately records **436.7 lb CSM→LM lunar-orbit weight transfer**. These are useful configuration-accounting anchors, but neither is promoted to PDI mass.

The targeted search identified **SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968, CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties** as the primary mission-specific mass-properties source family. The base revision is dated 20 August 1969 and covers G/H/J mission data.

### Public-scan amendment provenance audited

A recovery pass checked the surviving digitized Rev. 2 binder rather than assuming that its title-page date applies to every page. It does not. Indexed primary-document text shows the section 3 introduction at **Amendment 86 (9/10/70)** and a table 3.1-8 page at **Amendment 110 (7/19/71)** describing **LM-10**. The public binder therefore contains later replacement pages and is not a clean Mission-G-era snapshot.

### Primary postflight event masses recovered

The Apollo 11 Mission Report Appendix A.6/table A-I provides mission-specific postflight mass properties based on expendable loading/usage analysis and measured spacecraft/stage weights. For the LM it documents **33,683.5 lb at separation**, **33,669.6 lb at DOI ignition**, **33,401.6 lb at DOI cutoff**, and **16,153.2 lb at lunar landing**.

The table does not contain a PDI row, so PDI mass remains unresolved. These values are now the preferred primary event-mass checkpoints around the missing state.

A cross-check of NASA SP-4029, *Apollo by the Numbers*, found a provenance hazard: its cross-mission table places **33,669.6 lb** under Apollo 11 PDI and **33,401.6 lb** under DOI ignition, whereas the primary Mission Report explicitly identifies those values as DOI ignition and DOI cutoff respectively. The secondary compilation is therefore not used to close PDI mass.

### As-flown DPS evidence retained

Apollo 11 Mission Report §9.8 documents the 756.3-second powered descent, approximately 6775 ft/s velocity change, 13% minimum-throttle start, throttle-up to full after about 26 seconds, the early data dropout, and flight throttle/pressure histories. These constrain validation but do not establish an exact delivered thrust/Isp history.

### Named propulsion source remains blocked

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation* (September 1970), remains **BLOCKED ON NAMED SOURCE RECOVERY**. No neighboring-mission values were substituted.

## Boundary preserved

No launch/unmanned mass plus transfer arithmetic was promoted to PDI mass. No Apollo 13 LM-7 or later LM-10 pre-PDI value was transferred to LM-5. No amendment-overwritten table was treated as Mission-G evidence solely from its section number. The secondary SP-4029 event labels were not allowed to override the primary Mission Report. No design Isp was promoted to flight-effective Isp. No throttle percentage was converted into unsupported exact thrust. No reconstructed state was relabeled raw telemetry.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Continue PDI-mass recovery only from a source explicitly labeling Mission G/LM-5 at PDI or pre-PDI with trustworthy provenance. Prioritize superseded ODB pages, contractor/postflight mass ledgers, and Apollo 11 Mission Report Supplement 7. Do not use SP-4029's apparent PDI value as closure.

## Evidence status

**PARTIALLY DOCUMENTED.** Mission-specific postflight LM masses at separation, DOI ignition, DOI cutoff, and landing are now primary-source documented. Exact Mission-G PDI mass remains unresolved. A conflicting secondary NASA event table has been identified and quarantined from historical model inputs. Exact delivered thrust/Isp remain unresolved; Apollo 11 DPS Supplement 7 and TRW BET Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.