# Evidence Verification Audit — 2026-09-11

## Conclusion

The repository's documented historical claims are supportable after the corrections in this audit. No material claim was found that requires reversal. The audit corrected four obsolete NASA file URLs, the title/use description of NTRS 19710010485, the metadata for NTRS 19760066779, and three stale statements that said the Apollo 13 ASPO 45 pages had not been inspected.

The remaining uncertainty is expressly labeled. In particular, a shared MSK number does not prove unchanged fields between missions; several station display sets remain incomplete; and some cataloged sources are identified but not yet reviewed deeply enough to support implementation.

## Scope and method

The audit covered every Markdown file in the repository and every external URL it cites. It used four checks:

1. inventory all evidence-bearing files and citations;
2. resolve document identity and provenance, preferring NASA/NTRS records and contemporaneous mission documents;
3. compare each material claim family with the relevant source text, tables, figures, or directly rendered scan pages;
4. distinguish historical evidence from project decisions, cross-mission comparison, retrospective testimony, and unresolved questions.

After the edits, the reproducible inventory reports 68 Markdown files, 158 external URL references representing 54 unique URLs, and no broken internal Markdown links. The audit report itself accounts for the increase from the 67-file pre-audit inventory. Run `python3 scripts/audit_documentation.py` to reproduce the structural checks.

HTTP reachability was treated separately from evidentiary validity. Four genuinely obsolete NASA file paths were replaced with working NTRS or Apollo Journals records. Some NASA, ibiblio, oral-history, and Smithsonian endpoints reject or time out under bulk automated requests even though their records or downloaded documents were independently inspected; those responses were not mislabeled as evidence failure.

## Material source families checked

| Evidence family | Primary basis checked | Result |
|---|---|---|
| MCC structure and console data flow | Apollo 13 press kit (NTRS 19760066779), MCC familiarization manual, HAER documentation, Display Formats Manual | Verified. The press-kit metadata is now identified; CRT composition, D/TV behavior, support rooms, pneumatic tubes, and the cited Apollo 11 request rate agree with the sources. |
| Controller organization and duties | *Flight Control of the Apollo Lunar Landing Mission* (NTRS 19700009496), mission manning material, Apollo 13 Mission Operations Report appendices | Verified at the role/responsibility level claimed. |
| Apollo 13 station operations | Mission Operations Report appendices A–N | Verified. The appendix/station mapping, CONTROL decision thresholds, INCO MSK 1475 limitation, PROCEDURES MSK 1503 issue, and station chronology are present in the report. |
| EECOM displays and telemetry playback | Apollo 13 Review Board Appendix B; AS-508 MCC/MSFN configuration; Mission Operations Report | Verified. Two monitors, one-second display updates, manually set limits, panel indications, and Format 30 capabilities/use are supported. |
| GNC/GUIDO/CONTROL CRTs | Apollo 13 AC Electronics G&N Summary, ASPO 45; Apollo 11 comparison volume | Verified for MSK 683/966/1123/1137 identities and layouts. MSK 1137 changed materially between Apollo 11 and 13, so unchanged field semantics are explicitly rejected. |
| LM computer data and mission techniques | R-567 section 2; Mission H-2 descent/ascent/orbit/abort/contingency notes | Verified. Data paths, approved decision logic, multi-cue diagnosis, ground/crew responsibility, telemetry contingencies, and plotted margin use agree with the cited documents. |
| Software/simulator behavior | Apollo 13 FSRR/FMES records, program notes, simulator operations and discrepancy reports | Verified within the notes' partial-review scope. Known anomalies, workarounds, test families, and configuration-control claims are supported. Engineering tests remain distinguished from integrated controller scenarios. |
| RTCC flight-dynamics displays | Mission G RTCC Operations Support Plan | Verified as Apollo 11/Mission G evidence only. MSK 55/56, 1501, 1502, and 1506 and their manual update behavior are not asserted as Apollo 13 facts. |
| Voice and public recordings | NASA mission audio/transcripts and Apollo in Real Time | Valid for workflow examples and recorded mission material. Reconstruction limits and retrospective-source status remain labeled. |

## Corrections made

- Replaced obsolete Apollo 13 Review Board, AS-508 configuration, and Mission Operations Report URLs with NTRS or Apollo Journals records.
- Identified NTRS 19760066779 as the *Apollo 13 Third Lunar Landing Mission Press Kit*, NASA release 70-50K, dated April 2, 1970.
- Replaced the repository's informal title for NTRS 19710010485 with the NTRS catalog title and limited its role; GNC operational claims now point to Appendix F of the Mission Operations Report where possible.
- Updated Research Notes 013 and 022 and the GNC station specification to reflect completed direct inspection of the Apollo 13 ASPO 45 section.
- Preserved the difference between verified display identifiers/layouts and incomplete field transcription or operational access details.

## Known limitations and integrity notes

- `REVIEWED-PARTIAL` means the sections needed for the recorded claim were checked; it does not mean the entire source was transcribed.
- The repository originally contained duplicate research-note identifiers. Under D-023, later-created duplicates were renumbered and references updated; duplicate identifiers are now a failing documentation-audit condition rather than a tolerated provenance hazard.
- Smithsonian's catalog endpoint and one NASA oral-history PDF are unreliable for automated clients. Neither is the sole basis for a material implementation claim.
- The source catalog is intentionally not an implementation whitelist. Entries marked `IDENTIFIED` require claim-level review before use.

## File-by-file ledger

The result describes each file's role in this audit. “Trace verified” means its material evidence claims were checked through the cited source family and its limitations were preserved.

| File | Class | Audit result | Note |
|---|---|---|---|
| `README.md` | Project record | Consistent | Governance/progress content checked against the current evidence state. |
| `docs/APOLLO13_STATION_BASELINE.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/CONTROLLER_INFORMATION_WORKFLOW.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/DECISIONS.md` | Project record | Consistent | Governance/progress content checked against the current evidence state. |
| `docs/DISPLAY_RECONSTRUCTION_STATUS.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/DISPLAY_SYSTEM_BASELINE.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/FLIGHT_CONTROL_ORGANIZATION.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/MISSION_PROFILE_MODEL.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/OPEN_QUESTIONS.md` | Project record | Consistent | Governance/progress content checked against the current evidence state. |
| `docs/PHYSICAL_DOCUMENT_WORKFLOW.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/PROGRESS.md` | Project record | Consistent | Governance/progress content checked against the current evidence state. |
| `docs/PROJECT_PRINCIPLES.md` | Project record | Consistent | Governance/progress content checked against the current evidence state. |
| `docs/ROADMAP.md` | Project record | Consistent | Governance/progress content checked against the current evidence state. |
| `docs/SIMULATION_ARCHITECTURE.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/SIMULATION_SCENARIO_RESEARCH.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/SIMULATION_VALIDATION.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/STATION_RESEARCH_STATUS.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/VOICE_COMMUNICATIONS_BASELINE.md` | Derived/project doc | Trace verified | Evidence claims trace to audited research notes; design decisions are labeled as such. |
| `docs/stations/APOLLO13_CAPCOM.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_CONTROL.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_EECOM.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_FAO.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_FIDO.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_FLIGHT.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_GNC.md` | Derived station spec | Corrected/trace verified | Stale extraction text removed; station claims trace to mission report and ASPO 45 scan. |
| `docs/stations/APOLLO13_GUIDO.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_INCO.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_PROCEDURES.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_RETRO.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `docs/stations/APOLLO13_TELMU.md` | Derived station spec | Trace verified | Operational claims trace to mission-specific reports or explicitly labeled comparison sources. |
| `resources/PRIMARY_SOURCE_CATALOG.md` | Catalog | Corrected | Metadata and source locations audited; obsolete URLs and one NTRS title corrected. |
| `resources/README.md` | Project record | Consistent | Governance/progress content checked against the current evidence state. |
| `resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md` | Audit record | Verified | Records the audit scope, findings, corrections, limits, and complete file ledger. |
| `resources/research/001_mcc_high_level_structure.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/002_apollo11_source_baseline.md` | Research note | Source-qualified | Identified-source claims are valid; implementation authority is not asserted. |
| `resources/research/003_mocr_positions_and_responsibilities.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/004_support_rooms_and_ground_processing.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/005_apollo11_manning_and_nomenclature.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/006_console_display_architecture.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/007_mission_g_rtcc_operations.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/008_controller_console_and_document_evidence.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/009_voice_communications_system.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/010_apollo13_controller_station_evidence.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/011_apollo_simulation_cases.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/012_apollo13_eecom_reconstruction.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/206_apollo13_eecom_reference_station.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/207_apollo13_gnc_crt_source.md` | Research note | Superseded/corrected | Original extraction limit is retained as history and linked to direct inspection. |
| `resources/research/013_apollo13_gnc_reconstruction.md` | Research note | Corrected | Continuity conclusion updated after direct Apollo 13 inspection. |
| `resources/research/014_apollo13_control_reconstruction.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/208_mission_simulator_technical_sources.md` | Research note | Source-qualified | Identified-source claims are valid; implementation authority is not asserted. |
| `resources/research/015_apollo13_telmu_reconstruction.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/209_simulator_configuration_fidelity.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/016_apollo13_lm_data_links.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/017_telmu_control_source_conflict.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/018_apollo13_inco_station.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/019_apollo13_fido_retro.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/020_flight_capcom_workflow.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/021_procedures_fao.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/022_cross_mission_lm_crt_evidence.md` | Research note | Corrected | Apollo 13 identifiers are now direct evidence; unchanged field semantics remain unproven. |
| `resources/research/023_apollo13_simulator_discrepancies.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/024_apollo13_lm7_redline_data.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/025_apollo13_fsrr_fmes.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/026_mission_g_flight_dynamics_displays.md` | Research note | Cross-mission verified | Mission G evidence checked and clearly excluded from Apollo 13 fact status. |
| `resources/research/027_apollo13_known_program_notes.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/028_apollo13_mission_techniques.md` | Research note | Trace verified | Material claims trace to the cited primary source; stated partial-review limits remain. |
| `resources/research/029_apollo13_aspo45_direct_inspection.md` | Research note | Directly verified | Scan identity, hash, page map, and four layouts checked. |
| `resources/research/030_apollo11_apollo13_msk1137_comparison.md` | Research note | Directly verified | Both mission scans compared; differences support the stated non-continuity conclusion. |
| `resources/research/031_apollo13_msk1137_field_inventory.md` | Research note | Directly verified with limits | Visible fields inventoried; unclear OCR and implementation gaps remain labeled. |

## Reproduction

```bash
python3 scripts/audit_documentation.py
```

Use `--check-http` only as a reachability diagnostic. A non-200 result may reflect throttling, bot protection, or a server that rejects HEAD-like automated access; validate source identity and content independently before treating it as invalid evidence.
