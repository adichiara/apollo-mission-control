# Progress — Apollo 13 mass-properties job-number provenance

Date: 2026-09-15
Research note: `resources/research/151_apollo13_mass_properties_job_number_boundary.md`

## Completed

- Continued from research note 150's unresolved H-2 mass-properties run provenance.
- Re-examined the primary Apollo 13 Flight Control Division Mission Operations Report.
- Identified a mission-specific late-entry statement that EOM aerodynamics loaded into RTCC were based on **mass properties job 27**.
- Established that H-2 mass-properties computation had a separately referencable **numbered job identity**, distinct from the `T+N` state/epoch label.
- Preserved the chronology boundary: job 27 is documented around GET 122 hours for entry-aerodynamics work and is **not** evidence for the PC+2 job number.
- Updated the PC+2 numerical roadmap, station-status addendum, and RTCC mass-properties source catalog.

## Result

The simulation provenance model may now include an optional sourced mass-properties `job_number` separate from deck/reference epoch, run time, and downstream product. For PC+2 the job number remains unknown.

## Next

Search H-2 Flight Dynamics/RETRO worksheets, RTCC listings, controller procedures, and mass-properties records for numbered jobs near GET 55–59 hours that also identify `T+55`, DPS trim, PC+2, LM burn, or P30 module weights.