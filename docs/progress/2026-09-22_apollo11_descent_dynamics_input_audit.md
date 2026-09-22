# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the next unresolved LM-5 descent inputs against primary Apollo documentation, preserving the distinction among design values, planned/commanded behavior, as-flown telemetry, reconstructed trajectory, and model inputs.

### PDI mass search narrowed to the correct primary table class

The Apollo 11 final Flight Plan documents an **unmanned LM weight of 33,278.3 lb** in its SPS budget assumptions and separately records **436.7 lb CSM→LM lunar-orbit weight transfer**. These are useful configuration-accounting anchors, but neither is promoted to PDI mass.

The targeted search identified **SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968, CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties** as the primary mission-specific mass-properties source family. The base revision is dated 20 August 1969 and covers G/H/J mission data.

### Public-scan amendment provenance audited

A new recovery pass checked the surviving digitized Rev. 2 binder rather than assuming that its title-page date applies to every page. It does not. Indexed primary-document text shows the section 3 introduction at **Amendment 86 (9/10/70)** and a table 3.1-8 page at **Amendment 110 (7/19/71)** describing **LM-10**. The public binder therefore contains later replacement pages and is not a clean Mission-G-era snapshot.

This is a material provenance finding. Section/table numbering in that scan cannot by itself prove Apollo 11 applicability, and a value extracted from a later page cannot be back-assigned to LM-5. The remaining mass task is now narrower: recover a sequential mass-properties/consumables page that explicitly identifies Mission G or LM-5 and preserves an effective amendment date appropriate to that state.

Repository Apollo 13 work remains useful only as structural evidence that this source family contains `LM PRE P.D.I.` rows and consumables-change summaries. No LM-7 or LM-10 value is used for Apollo 11.

### As-flown DPS evidence retained

Apollo 11 Mission Report §9.8 documents the 756.3-second powered descent, approximately 6775 ft/s velocity change, 13% minimum-throttle start, throttle-up to full after about 26 seconds, the early data dropout, and flight throttle/pressure histories. These constrain validation but do not establish an exact delivered thrust/Isp history.

### Named propulsion source remains blocked

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation* (September 1970), remains **BLOCKED ON NAMED SOURCE RECOVERY**. No neighboring-mission values were substituted.

## Boundary preserved

No launch/unmanned mass plus transfer arithmetic was promoted to PDI mass. No Apollo 13 LM-7 or later LM-10 pre-PDI value was transferred to LM-5. No amendment-overwritten table was treated as Mission-G evidence solely from its section number. No design Isp was promoted to flight-effective Isp. No throttle percentage was converted into unsupported exact thrust. No reconstructed state was relabeled raw telemetry.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Recover a Mission-G/LM-5 sequential mass-properties or consumables-change page with explicit amendment/effective-date provenance, preferably from an earlier/superseded-page archive or mission-specific postflight mass-properties source. Continue the parallel archival search for Apollo 11 Mission Report Supplement 7. Do not spend another broad-web pass on TRW Volume II absent a new archival lead.

## Evidence status

**PARTIALLY DOCUMENTED.** The primary source family/table class is identified, and the public Rev. 2 scan is now proven to contain later amendment replacements, preventing unsafe extraction by section number alone. Exact Mission-G pre-PDI mass remains unresolved pending a correctly provenanced LM-5 page. Exact delivered thrust/Isp remain unresolved; Apollo 11 DPS Supplement 7 and TRW BET Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.