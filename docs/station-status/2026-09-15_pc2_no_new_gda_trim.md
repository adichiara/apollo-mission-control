# Station-status update — PC+2 no-new-GDA-trim workflow

Date: 2026-09-15  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research note 158 materially sharpens the PC+2 CONTROL/GUIDO/FLIGHT workflow.

## CONTROL

The PC+2 activation procedure now has direct crew-facing evidence that no new Noun 48 GDA trim was loaded. Mission Control inserted `VERB 34 ENTER` after Noun 47; Haise asked whether this meant the gimbals looked all right, and Duke confirmed it. CONTROL therefore needs a simulation action/state for **accept existing gimbal state / no trim update**, not an invented final trim pair.

Unresolved: the controller-side comparison, tolerance, mass-properties job, or display evidence supporting that acceptance.

## GUIDO

The DAP-load workflow must preserve the distinction between Noun 46 configuration, Noun 47 vehicle weights, and Noun 48 gimbal trim. For PC+2, the historical procedure terminated after Noun 47 rather than proceeding into Noun 48.

Unresolved: exact LGC/display state and whether a ground-computed candidate trim existed despite no crew entry.

## FLIGHT / CAPCOM

The crew-facing procedure demonstrates selective checklist editing rather than wholesale execution of a standard activation page. The no-update decision was communicated as an explicit procedural omission and confirmed verbally.

## FIDO / RETRO

No maturity change. Their mass-properties/trajectory provenance remains relevant to explaining why a trim update was or was not required, but no new evidence identifies a numbered PC+2 mass-properties job.

## Simulation boundary

Keep separate:

`computed trim -> update/no-update decision -> crew-entered Noun 48 (none newly entered for PC+2) -> retained gimbal state -> ignition/powered-flight GDA response`.

Do not populate a final PC+2 Noun 48 pair unless new primary evidence shows that one was entered by another procedure.