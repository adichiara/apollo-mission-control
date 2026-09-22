# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the next unresolved LM-5 descent inputs against primary Apollo documentation, preserving the distinction among design values, planned/commanded behavior, as-flown telemetry, reconstructed trajectory, and model inputs.

### PDI mass search narrowed to the correct primary table class

The Apollo 11 final Flight Plan documents an **unmanned LM weight of 33,278.3 lb** in its SPS budget assumptions and separately records **436.7 lb CSM→LM lunar-orbit weight transfer**. These are useful configuration-accounting anchors, but neither is promoted to PDI mass.

The targeted search identified **SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968, CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties** as the primary mission-specific mass-properties source family. Its stated purpose is to provide per-mission mass properties and consumable loading, maintained through actual consumable loading. The 20 August 1969 revision covers G/H/J mission data.

Repository work already performed for Apollo 13 independently demonstrates the relevant structure of this same source family: later LM-7 amendment pages contain an `LM PRE P.D.I.` row in the effective sequential mass-properties table and a consumables-change summary spanning separation, pre-PDI, touchdown, ascent, rendezvous/docking, and jettison. That LM-7 value is **not** used for Apollo 11. It tells us exactly what Mission-G/LM-5 pages must be recovered and checked.

Result: the PDI-mass task is no longer a generic search for a plausible number. It is a bounded extraction/provenance task: recover the LM-5 sequential mass-properties and consumables-change pages, preserve amendment dates, then reconcile their event states with the Apollo 11 Flight Plan bookkeeping.

### As-flown DPS evidence retained

Apollo 11 Mission Report §9.8 documents the 756.3-second powered descent, approximately 6775 ft/s velocity change, 13% minimum-throttle start, throttle-up to full after about 26 seconds, the early data dropout, and flight throttle/pressure histories. These constrain validation but do not establish an exact delivered thrust/Isp history.

### Named propulsion source remains blocked

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation* (September 1970), remains **BLOCKED ON NAMED SOURCE RECOVERY**. No neighboring-mission values were substituted.

## Boundary preserved

No launch/unmanned mass plus transfer arithmetic was promoted to PDI mass. No Apollo 13 LM-7 pre-PDI value was transferred to LM-5. No design Isp was promoted to flight-effective Isp. No throttle percentage was converted into unsupported exact thrust. No reconstructed state was relabeled raw telemetry.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Extract the Mission-G/LM-5 sequential mass-properties and consumables-change pages from SNA-8-D-027(III) Rev. 2, including amendment provenance and any `LM PRE P.D.I.` row. Continue the parallel archival search for Apollo 11 Mission Report Supplement 7. Do not spend another broad-web pass on TRW Volume II absent a new archival lead.

## Evidence status

**PARTIALLY DOCUMENTED.** The primary source family/table class needed to close LM-5 PDI mass is now identified and Apollo 11 configuration bookkeeping is strengthened. The exact Mission-G pre-PDI value still requires extraction and provenance checking. Exact delivered thrust/Isp remain unresolved; Apollo 11 DPS Supplement 7 and TRW BET Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.