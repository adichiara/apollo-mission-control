# Research note 151 — Apollo 13 RTCC mass-properties job-number boundary

Date: 2026-09-15

## Question

Can mission-specific H-2 primary documentation narrow the operational identity of an RTCC mass-properties calculation run beyond the `T+N` reference-state label?

## Primary source

NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, dated 28 April 1970.

NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf

Relevant Flight Dynamics/RETRO entry in the late return/entry chronology states that final stowage definitions were used to compute entry aerodynamics at approximately GET 122 hours and that those entry aerodynamics were loaded into RTCC as EOM aerodynamics **based on mass properties job 27**, with `L/D = .29052`.

## Finding

This is direct Apollo 13/H-2 evidence that an operational mass-properties calculation could possess a **numbered job identity** distinct from its mission-relative mass-properties epoch/state.

The report therefore supports a more specific H-2 provenance model than research note 150 could establish from Apollo 12 alone:

`mass-properties basis/state -> numbered mass-properties job -> derived operational product -> RTCC load/use`

For the documented late-entry case, the chain is specifically:

`final stowage definitions -> mass properties job 27 -> entry aerodynamics -> EOM aerodynamics loaded in RTCC`

This also shows that a downstream operational product could preserve the identity of the mass-properties job on which it was based.

## PC+2 consequence

The evidence does **not** identify the job number used for PC+2, nor does it connect job 27 to PC+2. Job 27 belongs to the later entry-aerodynamics chronology at approximately GET 122 hours.

It does, however, materially narrow the archival target. The missing pre-PC+2 artifact may have been identifiable not only by a `T+55` deck/reference state but also by a **mass-properties job number**. Searches for H-2 run sheets, RTCC listings, worksheets, or support records should therefore include `mass properties job`, `job number`, and neighboring numbered-job references.

## Boundary retained

Do not infer:

- that `T+55` was mass properties job 27;
- any PC+2 mass-properties job number;
- that job numbers were globally sequential across all RTCC processing rather than local to the mass-properties workflow;
- that every H-2 mass-properties run produced an RTCC load;
- that the PC+2 P30 `62,480 / 33,452 lb` values were outputs of a particular numbered job;
- exact job inputs, fields, commands, table layouts, software version, or execution venue from this sentence alone.

Research note 150's Apollo 12 evidence remains architectural support for controller-initiated pre-maneuver runs; this note supplies the first mission-specific H-2 evidence in the current project that such a mass-properties computation had a separately referencable job identity.

## Simulation implication

The mass-properties calculation-run object should permit, but not require, a historically sourced `job_id`/`job_number` provenance field separate from:

1. reference epoch/state (`T+N` when known);
2. generation/run time;
3. input/deck provenance;
4. maneuver or downstream-product association;
5. computational venue/version;
6. derived weight/CG, trim, aerodynamics, or other products.

For H-2, only job `27` is currently source-identified, and only for the late entry-aerodynamics chain. PC+2 must remain `job_number: unknown` until direct evidence is recovered.

## Next archival target

Search Apollo 13/H-2 RTCC controller procedures, Flight Dynamics/RETRO worksheets, mass-properties listings, and processor records for **numbered mass-properties jobs near GET 55–59 hours**, especially records that also mention `T+55`, DPS trim, PC+2, LM burn, or the final P30 module weights.