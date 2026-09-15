# Progress — Apollo 13 Luminary V34/N47 branch verification

Date: 2026-09-15
Research note: `resources/research/159_luminary131_v34_n47_software_path.md`

## Completed

- Inspected Apollo 13 Luminary 131 `EXTENDED_VERBS.agc` rather than relying on generic AGC behavior.
- Verified the actual R03/Verb 48 response path at Noun 47.
- Confirmed that `V34E` at Noun 47 branches to `ENDR03` and `ENDEXT`, ending the routine before Noun 48.
- Confirmed that only the proceed path continues through mass/moment processing to `V06N48`, and that the later proceed path invokes `TRIMGIMB`.
- Upgraded the PC+2 no-new-Noun-48 interpretation from transcript/checklist inference to mission-software-confirmed behavior.
- Preserved the unresolved controller-side question: why CONTROL judged the existing gimbal condition acceptable remains undocumented in recovered material.

## Architecture consequence

Implement the DAP-load workflow as an explicit branch:

`N47 -> terminate -> end`

or

`N47 -> proceed -> mass/moment update -> N48 -> trim path`.

Apollo 13 PC+2 uses the first branch. Do not fabricate the controller rationale or a missing final trim pair.