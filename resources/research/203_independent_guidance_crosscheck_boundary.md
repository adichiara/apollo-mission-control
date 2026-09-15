# 203 — Independent guidance cross-check boundary

## Purpose

Define a reusable comparison layer for cases where Mission Control has more than one guidance/navigation source and must reason from agreement or disagreement without direct access to hidden truth.

## Apollo pressure cases

Apollo 11 powered descent provides the immediate pressure test: surviving simulation/debrief evidence emphasizes that primary and abort-guidance information provided independent cues that should have been considered alongside the program alarm.

Apollo 13 also uses PGNS/AGS comparison as a backup/cross-check concept.

The common architecture requirement is therefore not “AGS validates PGNS.” It is:

`independent source A observation <-> independent source B observation -> controller-visible comparison evidence`

## Implemented boundary

The generic model compares caller-selected numerical fields using:

- source identity;
- validity;
- observation time/freshness;
- caller-supplied per-field tolerances.

It returns:

- comparable vs indeterminate;
- agreement/disagreement when comparable;
- per-field signed and absolute differences;
- explicit reasons for invalid, stale, or incomplete comparisons.

## Deliberate exclusions

The model does not:

- designate a truth source;
- infer hidden vehicle state;
- define Apollo-specific fields/tolerances;
- issue GO/NO-GO or abort/continue decisions;
- synthesize PGNS or AGS measurements.

## Apollo 11 readiness consequence

The `backup_guidance` domain remains **partial**.

Generic comparison machinery now exists, but historical implementation still requires the actual fields, tolerances, freshness/update timing, and controller presentation used during the selected powered-descent interval.