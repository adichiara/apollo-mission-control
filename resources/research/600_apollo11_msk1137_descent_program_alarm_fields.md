# 600 — Apollo 11 MSK-1137 descent/program-alarm fields

Date: 2026-09-23
Research thread: `apollo11-program-alarm-controller-flow`
Status: **SUFFICIENT for controller-product field semantics; exact DRK/button routing remains OPEN**

## Bounded question

Does Apollo-11-specific primary documentation establish controller-visible ground fields that directly support the powered-descent/program-alarm interval beyond the previously cataloged landing-radar and trajectory quantities?

## Primary-source result

Yes. The AC Electronics _Apollo 11 Manual_ identifies the LM ground CRT display **MSK-1137** and its continuation explicitly defines additional controller-visible fields relevant to descent and program-alarm monitoring:

- `TIG` — time of ignition;
- `TGO` — time to engine cutoff;
- time of last/next significant event;
- **time to end of phase (descent only)**;
- LGC warning-lamp status;
- ISS warning-lamp status;
- PGNCS caution-lamp status;
- program caution-lamp status;
- first, second, and most recent alarm code;
- **number of restarts**;
- computer program number;
- DSKY verb and noun;
- verb/noun flasher status;
- DSKY rows 1–3.

The same MSK-1137 family also includes the already cataloged landing-radar status/range, PGNS altitude, AGS altitude, ground-computed actual delta-V, and related guidance fields.

## Consequence

The Apollo 11 powered-descent/program-alarm reference no longer needs to invent a modern alarm panel or expose hidden AGC state to give ground controllers meaningful alarm context. Mission-specific source evidence supports a ground display product carrying alarm codes, restart count, active computer program, DSKY state, and descent-phase timing alongside navigation/guidance information.

This does **not** establish which controller requested MSK-1137 at a particular instant, a one-button DRK legend, display cadence/latency, or that every field was simultaneously visible to every station. Those remain separate configuration/routing questions.

## Sources

AC Electronics, _Apollo 11 Manual_, Apollo 11 mission-era guidance/control documentation, section `ASPO 45 CRT DISPLAYS`, `MSK-1137` and `MSK-1137 (CONTINUED)`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf

## Evidence status

- **DOCUMENTED:** Apollo-11-specific MSK-1137 field semantics listed above.
- **DOCUMENTED:** descent-only time-to-end-of-phase and ground-visible alarm/restart/program/DSKY context.
- **UNRESOLVED:** exact Mission-G station request/routing, DRK button mapping, update cadence/latency, and historical request timing.
- **NO INFERENCE:** no controller ownership or alarm decision rule is assigned solely from the display-field inventory.