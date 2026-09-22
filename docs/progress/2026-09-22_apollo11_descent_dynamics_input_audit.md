# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited unresolved LM-5 descent inputs against primary Apollo documentation while preserving design/planned/as-flown/reconstructed/model distinctions.

### PDI mass boundary

The Apollo 11 Mission Report Appendix A.6/table A-I documents **33,683.5 lb at separation**, **33,669.6 lb at DOI ignition**, **33,401.6 lb at DOI cutoff**, and **16,153.2 lb at landing**. It contains no PDI row. The surviving SNA-8-D-027(III) Rev. 2 mass-properties binder contains later replacement pages, so exact PDI mass remains unresolved pending an explicitly Mission-G/LM-5 page with trustworthy event provenance.

### Propulsion boundary

The Apollo 11 Press Kit gives **9,870 lbf maximum rated thrust**; the Mission Report documents LM-5 advancing to FTP about 26 seconds after PDI. Later LMA790-3-LM Volume-I material gives 9,870-lbf fixed-full-throttle semantics, but catalog provenance places the surviving complete handbook at LM-7-and-subsequent or later, so it is not promoted to LM-5 calibration.

### LM-5 Volume II recovered

A public scan of **LMA790-3-LM 5 and Subsequent, Volume II — Operational Procedures** establishes LM-5-specific operational-handbook provenance, but does not supply the missing force calibration.

### LM-5-era Volume I excerpt recovered

A NASA Apollo Lunar Surface Journal-hosted PDF excerpt from **LMA790-3-LM, Apollo Operations Handbook, Subsystems Data** carries **Basic Date 15 December 1968** and explicitly distinguishes **“On LM 5”** hardware from **“LM 6 and subsequent vehicles.”** This establishes that configuration-aware LM-5-era Volume-I pages are publicly recoverable, but the excerpt is waste-management/crew-equipment material and contains no DPS calibration.

### FTP control provenance tightened

NASA's Apollo News Reference GN&C material describes the descent-engine control assembly hard stop as **92.5-percent thrust** and states that each automatic-throttle counter pulse corresponds to a **2.7-lb thrust increment**. Searchable LMA790-3-LM material carrying the **15 December 1968 basic date** includes page 2.2-222, changed **15 March 1969**, stating that automatic throttle increases can drive the counter to the level which, combined with the fixed 10-percent TTCA output, corresponds to **92.5-percent thrust**.

A further page-level recovery now passes the LM-5 provenance test directly. In the 15 September 1969 LM-6-and-subsequent scan, **page 2.2-215 carries Change Date 15 June 1969**—the date of the superseded LM-5-and-subsequent issue—and figure 2.2-62, *Thrust/Translation Controller Assembly — Angular Displacements*, labels the throttle hard-stop position **“92.5% THRUST.”** The surrounding retained control pages also include 15 June 1969 effective dates. This establishes that the **92.5-percent manual/control hard-stop semantics were actually present in the LM-5 handbook state**, not merely in a later mature-LM issue.

This still does **not** establish an LM-5 engine-specific force calibration at that control point. The separate Apollo 11 Press Kit value of 9,870 lbf remains a mission-specific preflight specification; no arithmetic equivalence between 92.5 percent and 9,870 lbf is asserted.

### Volume-I publication lineage narrowed

**LMA790-3-LM 6 and Subsequent, Volume I, dated 15 September 1969, states that it supersedes LMA790-3-LM 5 and Subsequent dated 15 June 1969**. Its effective-page record and retained page dates now provide concrete LM-5-effective evidence, including the 92.5-percent throttle hard-stop page above.

The DPS performance/design table itself has not yet been recovered with a 15 June-or-earlier effective date, so exact FTP force and Isp remain unresolved.

### Supplement 7

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation*, remains **BLOCKED ON NAMED SOURCE RECOVERY**; no performance values are inferred from neighboring mission supplements.

## Boundary preserved

No later-LM force calibration was back-projected onto Eagle. No excerpt-level LM-5 provenance was misrepresented as recovery of the complete LM-5 Volume I. No preflight/design thrust was promoted to delivered thrust. PDI mass remains unresolved.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Recover the **DPS §2.3 performance/design pages whose individual effective dates are 15 June 1969 or earlier** from the September LM-6 scan or another copy. Test whether those pages tie a force value to fixed-full-throttle and provide an LM-5-applicable Isp/performance basis. In parallel, retain LM-5 engine acceptance/performance records and Apollo 11 DPS Supplement 7 as preferred delivered-performance targets. Continue PDI-mass recovery only from explicitly Mission-G/LM-5 event-provenance records.

## Evidence status

**PARTIALLY DOCUMENTED.** The 92.5-percent throttle hard stop is now directly documented on a **15 June 1969 effective handbook page retained from the LM-5-and-subsequent issue**. Exact LM-5 FTP force calibration, delivered thrust/Isp, and PDI mass remain unresolved. Apollo 11 DPS Supplement 7 and TRW BET Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.