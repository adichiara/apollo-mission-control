# Apollo 13 GUIDO Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Guidance Officer position from mission-specific Mission Control records and the flown LM guidance-computer data-link specification.

GUIDO is distinct from CSM GNC and LM CONTROL.

---

## 1. Position

**Call sign:** GUIDO / GUIDANCE  
**Apollo 13 Mission Operations Report:** Guidance Officer

### Documented responsibility

Apollo Mission Control documentation assigns GUIDO responsibility for:

- utilization/monitoring of the spacecraft guidance and navigation system;
- inertial-platform alignment/correlation;
- powered-flight and spacecraft-initialization guidance monitoring;
- terminal/rendezvous guidance support;
- CSM and LM DSKY monitoring;
- CMC and LGC command/update functions.

This is fundamentally different from the hardware-oriented responsibilities of GNC and CONTROL.

---

# 2. Apollo 13 real-time workload

Apollo 13 operational records show GUIDO working with:

- CMC state after computer restart;
- CMC clock and state-vector validity;
- REFSMMAT/orientation knowledge;
- transfer of alignment from the CSM to the LM;
- LM platform alignment and verification;
- ground updates to onboard computers;
- alternate navigation/alignment procedures after the CSM was powered down;
- trajectory/maneuver targeting products supplied by FIDO/RETRO and loaded into onboard guidance.

During the initial contingency, Flight specifically queried GUIDO on the CSM platform orientation and whether a rapid docked transfer/alignment into the LM could be accomplished.

This indicates that GUIDO's central concern was not merely "where the spacecraft is," but:

> what the onboard guidance computers and inertial platforms currently know, whether that knowledge is trustworthy, and how to update or preserve it.

---

# 3. Mission-specific Apollo 13 LM data-link source

The strongest current Apollo 13 GUIDO source is:

**R-567, Guidance System Operations Plan for Manned LM Earth Orbital and Lunar Missions Using Program LUMINARY 1C (LM131 Rev. 1), Section 2 — Data Links, Revision 8, March 1970.**

This is a mission-specific control document for the flown Apollo 13 LM AGC software.

It specifies:

- digital uplink to the LGC;
- LGC digital downlink;
- P27 update behavior;
- program-dependent downlink lists;
- data verification;
- restart behavior;
- AGS initialization/update data.

---

# 4. Ground-to-LGC update path

The GSOP states that ground control could transmit keyboard-equivalent information to the LGC through the uplink.

Documented update functions include:

- **Verb 70** — liftoff-time increment;
- **Verb 71** — contiguous block update;
- **Verb 72** — scatter update;
- **Verb 73** — octal clock increment.

The uplink path transmits encoded DSKY-key equivalents.

The LGC acknowledges successful receipt through the ground communications path.

## P27 verification

For update operations, the ground monitored a dedicated P27 downlink containing values such as:

- UPBUFF;
- UPVERB;
- UPOLDMOD;
- COMPNUMB;
- UPCOUNT.

The ground was expected to verify that:

1. the proper program was entered;
2. the correct update type was active;
3. the expected number of components was being loaded;
4. the data received by the LGC matched the intended update;
5. the update was accepted/modified/rejected as appropriate.

### Simulation significance

An onboard-computer update should not be represented as a generic instantaneous "upload succeeded" action.

Where this level of fidelity matters, the historical workflow contains:

```text
prepare update
    ↓
configure uplink path
    ↓
transmit encoded DSKY-equivalent input
    ↓
monitor downlink state
    ↓
verify P27/update buffers
    ↓
accept / correct / reject
```

The exact Mission Control console controls used by GUIDO to initiate those actions remain under research.

---

# 5. Program-dependent LM downlists

The Apollo 13 LGC did not continuously transmit one universal data packet.

The DOWNLINK program selected different lists according to active guidance program/state.

The GSOP defines six principal downlist families:

1. **Orbital Maneuvers**
2. **Coast and Align**
3. **Rendezvous and Prethrust**
4. **Descent and Ascent**
5. **Lunar Surface Align**
6. **AGS Initialization and Update**

## Descent/Ascent list

Transmitted during:

- P12 — Powered Ascent Guidance
- P63 — Braking Phase Guidance
- P64 — Approach Phase Guidance
- P66 — Rate-of-Descent Landing Phase
- P68 — Confirm Lunar Landing
- P70 — DPS Abort Guidance
- P71 — APS Abort Guidance

The surviving mnemonic list includes data such as:

- landing-radar quantities;
- measured velocity/altitude;
- body rates;
- desired and actual CDU angles;
- LM/CSM mass;
- DAP/internal mode data;
- LGC failure/status registers;
- guidance/control channels;
- PIPA/velocity-change data;
- TIG and maneuver-related quantities.

## Lunar Surface Align list

Transmitted during:

- P22 — Rendezvous Radar Lunar Surface Navigation
- P57 — Lunar Surface Alignment

It includes state vectors, body-rate/alignment quantities, CDU state, guidance status, and radar/navigation-related information.

## AGS Initialization/Update list

Transmitted during:

- P21 — LGC Update
- R47 — AGS Initialization

It contains the LM/CSM state-vector and guidance quantities required to support AGS initialization/update.

---

# 6. Time coherence matters

The GSOP explicitly notes that some multiregister values are copied into "snapshot" areas before downlink transmission so that the set remains internally time-coherent while being sent.

Different lists snapshot different ranges of words.

This establishes another important simulation principle:

> telemetry values that appear together do not necessarily represent independently sampled instantaneous truth.

The telemetry pipeline has timing and packaging behavior that can matter when values are changing rapidly.

---

# 7. Data categories justified for GUIDO

## Onboard-computer state

- active program/major mode;
- restart/failure state;
- DSKY/display-table state;
- update/P27 state;
- erasable memory data where downlinked;
- computer clock/time relationships.

## Navigation state

- LM and CSM state vectors;
- vector time tags;
- guidance target quantities;
- landing-site / rendezvous / maneuver data where applicable.

## Inertial/alignment state

- REFSMMAT-related orientation knowledge;
- desired and actual CDU/gimbal quantities;
- platform/alignment status;
- body rates relevant to alignment/guidance verification.

## Guidance/program status

- DAP/guidance flagwords;
- failure registers;
- radar/navigation inputs;
- PIPA / velocity-change information;
- program-specific guidance quantities.

## Uplink/update state

- update buffers;
- count/index state;
- acknowledgement/error state;
- command/load verification.

---

# 8. GUIDO versus other positions

## GUIDO

Concerned with:

- what the CMC/LGC knows;
- whether its navigation/alignment state is valid;
- which guidance program/mode is active;
- what computer update is required;
- whether an update was correctly received;
- whether onboard guidance can support the maneuver/mission phase.

## GNC / CONTROL

Concerned primarily with:

- whether the physical propulsion and control hardware can execute the required maneuver;
- thruster/valve/gimbal/propellant/control-electronics state;
- actual vehicle response.

## FIDO

Concerned with:

- the ground trajectory solution;
- tracking data;
- maneuver targeting and trajectory consequences.

The same maneuver therefore naturally requires information exchange among FIDO, GUIDO, and GNC/CONTROL rather than a single "navigation" player.

---

# 9. Display status

## DOCUMENTED

- Apollo 13 LGC downlink contents and program-dependent list behavior;
- Apollo 13 LGC uplink/update mechanism;
- operational GUIDO responsibility;
- real-time use of platform/REFSMMAT/computer state during the Apollo 13 contingency.

## PARTIAL

- mission-specific CRT display families are known to exist in the Apollo 13 AC Electronics Guidance & Navigation Summary;
- that volume contains an **ASPO 45 CRT Displays** section.

## UNRESOLVED

- exact Apollo 13 GUIDO CRT display numbers;
- exact CRT page layouts;
- exact DRK/MSK arrangement;
- which raw LGC downlist fields appeared directly on which GUIDO display;
- exact command-control console hardware;
- voice-panel/loop selections.

Do not substitute Apollo 11/12 CRT pages for Apollo 13 until the Apollo 13 ASPO 45 section has been extracted.

---

# 10. Research targets

1. Extract Apollo 13 Guidance & Navigation Summary — ASPO 45 CRT Displays.
2. Map R-567 downlist parameters into actual MCC display formats.
3. Identify GUIDO DRK/MSK/display assignments.
4. Locate GUIDO console handbook/procedures.
5. Reconstruct the CMC Apollo 13 data-link side to the same level as the LM.
6. Determine RTCC processing between raw AGC downlink and GUIDO display products.
7. Reconstruct command-load handoff among GUIDO, INCO, CCATS, remote site, and spacecraft.

## Primary sources

- Apollo 13 Mission Operations Report, Appendix D — Guidance Officer.
- Apollo 13 Review Board Appendix A/B — Mission Control responsibilities.
- MIT/Charles Stark Draper Laboratory R-567, Section 2, Rev. 8 — LUMINARY 1C Data Links, March 1970:
  https://www.ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- Apollo 13 Guidance & Navigation Summary — AC Electronics, public scan indexed by Apollo 13 Flight Journal.


## 9A. Cross-mission CRT continuity evidence

Earlier AC/Delco Apollo guidance summaries explicitly define the ASPO 45 CRT family:

- MSK 683 — CM
- MSK 966 — CM
- MSK 1123 — LM
- MSK 1137 — LM

For the LM, **MSK 1123** is documented as a combined guidance/control/propulsion real-time page containing timing, downlink/site identification, DAP/body rates, attitude commands, gimbal/CDU/IMU/AGS attitude, PGNS/AGS errors, and velocity/delta-velocity information.

**MSK 1137** is documented as a powered-descent/control page containing throttle-selection/command, commanded thrust, thrust-chamber pressure, guidance/DAP error, desired rates, gimbal direction, control-mode state, and accumulated torque information.

Later Apollo telemetry tables continue to map individual LM guidance/radar/propulsion measurements to 1123 and 1137.

This is strong continuity evidence, but the Apollo 13 ASPO 45 pages still must be extracted before either page is treated as unchanged Apollo 13 configuration.


## 2026-09-11 evidence update — mission-specific CRT pages inspected

The former size/extraction blocker is resolved. Direct inspection of the Apollo 13 scan confirms MSK 683, 966, 1123, and 1137 in ASPO-1–12 (PDF pages 179–190). Layouts are on PDF 180, 182, 186, and 188 respectively. These identifiers/layout references are now **MISSION-SPECIFIC**, superseding earlier unresolved identifier status in this document. Unchanged field-level continuity from Apollo 11 remains unproven.

See [direct inspection and page map](../../resources/research/029_apollo13_aspo45_direct_inspection.md). Full transcription, refresh behavior, operational revisions, and station access remain open. No station maturity rating is raised by this update alone.


## 2026-09-11 field-provenance update

R-567 Rev. 8 now provides a direct source path for a substantial subset of the Apollo 13 LM CRT information. The Descent/Ascent downlist includes, among other families:

- list identity/sync;
- landing-radar CDU/time/velocity/range data;
- DSKY display-table words;
- desired and actual body rates;
- failure registers and restart count;
- RADMODES and DAPBOOLS;
- desired and actual CDU angles;
- PIPA/delta-velocity data;
- LM/CSM mass;
- guidance thrust command;
- TIG and time-to-go information.

This does **not** mean MSK 1123/1137 are raw downlist displays. In particular, the Apollo 13 MSK 1137 stable-member landing-radar velocity components require ground-side assembly/transformation from time-tagged antenna-axis measurements, and several displayed comparison quantities are explicitly ground-derived.

See `resources/research/032_apollo13_lm_crt_field_provenance.md`.

### Revised GUIDO gap

The question is no longer simply "which LGC values existed." The remaining implementation-critical gap is the **ground transformation and display-routing layer** between downlist words and the final CRT fields, plus station access/request behavior.


## 2026-09-11 PIPA-bias workflow evidence

A February 27, 1970 H-2 Lunar Surface Branch planning note documents a specific Apollo 13 ground method for lunar-surface PIPA-bias estimation. The method used:

- MPAD lunar gravity;
- gimbal angles;
- the **Guidance Officer's determination of local-vertical attitude**;
- PIPA-derived measured gravity.

Expected gravity was resolved into LM stable-member axes and differenced from measured gravity to obtain the bias estimate.

The actual Apollo 13 Mission Operations Report also records PIPA-bias monitoring during the contingency: after late LM PGNS initialization for MCC-7, the PIPA bias was judged satisfactory before the alignment/burn-planning sequence continued.

This provides concrete evidence that GUIDO's role in inertial-state validity extended into ground-derived bias assessment rather than merely reading raw accelerometer telemetry.

See `resources/research/033_apollo13_pipa_bias_ground_workflow.md`.
