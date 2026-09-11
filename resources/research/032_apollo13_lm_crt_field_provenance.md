# Apollo 13 LM CRT field provenance — R-567 to MSK 1123/1137

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — direct LGC downlist origins established for multiple display families; full RTCC/PCM provenance remains incomplete.**

## Purpose

The Apollo 13 ASPO 45 material establishes the mission-specific LM CRT layouts **MSK 1123** and **MSK 1137**. This note traces fields on those pages backward into the flown LM guidance-computer data-link definition where the evidence supports doing so.

This is deliberately a provenance map, not a renderer specification.

## Primary sources

1. AC Electronics, *Apollo 13 Guidance & Navigation Summary*, ASPO 45 CRT section:
   - MSK 1123 layout: PDF 186 / ASPO-8
   - MSK 1123 definitions: PDF 187 / ASPO-9
   - MSK 1137 layout: PDF 188 / ASPO-10
   - MSK 1137 definitions: PDF 189–190 / ASPO-11–12
   - https://apollojournals.org/afj/ap13fj/pdf-hr/a13-ac-elect-g-n-summary.pdf
   - Direct-inspection page map: `029_apollo13_aspo45_direct_inspection.md`

2. MIT/MSC, **R-567**, *Guidance System Operations Plan for Manned LM Earth Orbital and Lunar Missions Using Program LUMINARY 1C (LM131 Rev. 1), Section 2 — Data Links*, Revision 8, March 1970:
   - https://www.ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
   - NTRS record: https://ntrs.nasa.gov/citations/19720025988
   - Descent/Ascent descriptions: printed pp. 2-104 through 2-106
   - Descent/Ascent mnemonic inventory: printed p. 2-120

The Apollo 13 Descent/Ascent list is transmitted during P12, P63, P64, P66, P68, P70 and P71. R-567 also documents snapshot behavior for words 2–13 and 52–58; not every displayed value is an independently sampled instantaneous truth.

## Key result

MSK 1123/1137 are **not raw downlist dumps**.

They combine at least three provenance classes:

1. **direct or decoded LGC downlist values**;
2. **ground-derived values built from LGC/downlink inputs**;
3. **other spacecraft telemetry / ground context not contained in the LGC downlist**.

The simulator therefore needs a field-level provenance layer between raw telemetry and CRT rendering.

---

## Directly established LGC source families

The following are strong source mappings because the ASPO field meaning and R-567 mnemonic/description align directly.

| CRT information family | R-567 Descent/Ascent source | Evidence / caution |
|---|---|---|
| Downlist identity / `LGC FMT` | Word 1 list ID and sync | R-567 gives a unique list ID for Descent/Ascent. The final ASPO formatting of the displayed format name/code still belongs to ground processing. |
| Landing-radar antenna CDUs | Words 2–3, `LRXCDUDL`, `LRYCDUDL`, `LRZCDUDL` | Read at LR velocity time; scaled as angular fractions. |
| Landing-radar velocity sample | Words 4–6, `VSELECT`, `LRVTIMDL`, `VMEAS` | Only one antenna-axis velocity component is represented at a time; a different component is read every two seconds during LR velocity updates. |
| Landing-radar range | Word 8, `HMEAS` | Landing-radar slant range, calculated every two seconds during altitude updates. |
| LR minus LGC altitude | Word 22, `DELTAH` | R-567 explicitly defines it as landing-radar altitude minus LGC altitude. This corresponds directly to one Apollo 13 MSK 1137 delta-H family. |
| DSKY display state | Words 45–50, `DSPTAB` series | Downlinked display table cells; CRT presentation still requires decoding/formatting. |
| Desired body rates | Words 59–60, `OMEGAPD`, `OMEGAQD`, `OMEGARD` | Strong candidate/input for the ASPO desired-rate family. |
| Failure/alarm registers | Words 62–63, `FAILREG` family | R-567 defines the retained alarm pattern cells. |
| Radar/DAP state | Word 64, `RADMODES` + `DAPBOOLS` | Two separate flagwords share the transmitted word. |
| Accumulated control torque | Words 65–66 and 90, `POSTORKU/V/P` with adjacent `NEGTORK*` | R-567 explicitly defines the running sums of positive/negative RCS command on-time. This explains why the CRT quantity is displayed in time-like units rather than physical torque. |
| LM / CSM mass | Word 80, `LEMMASS` + `CSMMASS` | R-567 transmits scaled mass. MSK 1137 displays pounds, so a ground unit conversion/formatting step is required. |
| Guidance/control mode words | Word 81, `IMODES30` + `IMODES33` | Contains IMU/channel/status flags used to reconstruct operational state. |
| TIG | Word 82, `TIG` | Meaning changes by powered-flight phase as documented in R-567. |
| Actual body rates | Words 83–84, `OMEGAP`, `OMEGAQ`, `OMEGAR` | Body-axis rates. |
| Desired CDU angles | Words 85–86, `CDUXD`, `CDUYD`, `CDUZD` | Internal desired CDUs. |
| Actual CDUs / radar trunnion | Words 87–88, `CDUX/Y/Z` plus RR trunnion CDU | Direct guidance/radar inputs. |
| Moment offset | Word 89, `ALPHAQ` + `ALPHAR` | R-567 labels these as moment offsets. |
| PIPA time / delta velocity | Words 95–98, `PIPTIME1`, `DELV X/Y/Z` | Stable-member delta-velocity family. Do not equate raw downlink values automatically with the CRT's ground-computed `ACT ΔV` without the intervening ground algorithm. |
| Guidance thrust command | Word 78a, `FC` | Desired DPS thrust computed by lunar-landing guidance, every two seconds during landing. This is a strong match to the ASPO `GUID CMD` family. |
| Throttle-program output candidate | Word 99a, `PSEUDO55` | R-567 says this is exactly what goes into Counter 55 when filled by the landing-throttle program. It is a source candidate for throttle-command processing, but the ASPO MAN/AUTO/CMD/actuator fields should not be collapsed onto it without further evidence. |
| Time-to-go | Word 100, `TTOGO` | During descent/ascent, time to ignition; after ascent ignition, time to cutoff. ASPO uses several time-to-go concepts, so exact CRT-field routing must remain mission/phase specific. |
| Restart count | Word 30, `REDOCTR` | Supports the ASPO restart-count display family. |

## Landing-radar transformation is explicitly not a direct-field mapping

The most important provenance finding in this pass concerns MSK 1137 landing-radar velocity.

R-567 shows that the Descent/Ascent list sends:

- landing-radar CDUs;
- `VSELECT`, identifying which X/Y/Z antenna-axis component was read;
- one LR velocity measurement;
- a time tag.

A different velocity component is read every two seconds.

The Apollo 13 MSK 1137 definition instead presents **VXS/VYS/VZS in stable-member coordinates** and also presents radar-minus-guidance comparison quantities.

Therefore:

> the three CRT velocity components are not simply three simultaneous raw downlist registers.

At minimum, the ground/display path has to assemble time-tagged radar samples and apply coordinate processing. The exact RTCC/display algorithm remains to be located before implementation.

This also reinforces the project's telemetry rule: **displayed values may be transformations, comparisons, and temporally assembled products rather than raw spacecraft samples.**

## Ground-derived / not-yet-resolved CRT families

The following Apollo 13 MSK 1137 families cannot yet be assigned to one raw LGC register without overclaiming:

- `ACT ΔV` — ASPO explicitly calls it ground-computed; the downlinked PIPA/DELV family is an input, not sufficient evidence for the full ground computation.
- VXS/VYS/VZS stable-member landing-radar velocities — require transformation from time-tagged antenna-axis measurements/CDUs.
- radar-minus-PGNS velocity comparisons — require radar and guidance quantities plus documented correction/transform logic.
- radar-minus-AGS velocity comparisons — require AGS data not supplied solely by the LGC Descent/Ascent list.
- radar-minus-AGS altitude — likewise requires AGS altitude plus radar altitude.
- RTCC mass — ASPO explicitly distinguishes an RTCC-computed mass from the spacecraft/downlinked LM and CSM masses.
- `BIAS` / octal PIPA-bias load values — ASPO identifies these as ground-computed. A February 1970 H-2 planning note now documents the intended **lunar-surface** bias-estimation method, but the general mission-phase calculation/routing and OCTAL load-generation path remain unresolved. See note 033.

## Clearly non-LGC / additional-source families

Several MSK 1137 fields belong to spacecraft instrumentation or ground context outside the LGC downlist and therefore need PCM/telemetry/RTCC sources:

- receiving site identifier;
- actuator position;
- thrust chamber pressure;
- electrical voltages;
- radar/PIPA temperatures;
- selected hardware validity/status indications where the CRT uses non-LGC instrumentation;
- AGS DEDA/state quantities not carried as the specific LGC words above.

This distinction is important for CONTROL. A simulated LGC alone cannot populate the full CONTROL-oriented CRT page.

## Update-rate caution

R-567 provides many **calculation/sample intervals**, including several two-second quantities. These are not automatically the MCC CRT refresh cadence.

Keep separate:

```text
spacecraft calculation cadence
→ downlist packaging/transmission
→ ground reception/processing
→ CRT display update cadence
```

The last item is still unresolved for these pages.

## Architecture consequence

A controller-visible field should eventually carry metadata such as:

```text
display_id
field_id
source_document/page
spacecraft_source
downlist_word/register (if applicable)
data_origin = raw | onboard-computed | ground-derived | contextual
units_at_source
display_units
reference_frame
sample_time / cadence
validity source
ground transform
mission-profile override
```

Repeated labels such as `LGC`, `DAP`, `BIAS`, `RANGE`, and `PROG` are not sufficient field identifiers.

## Station consequences

### GUIDO

This pass materially improves the evidence chain from LGC state to controller information:

- active downlist identity;
- DSKY state;
- alarm/restart state;
- desired/actual CDUs;
- rates;
- radar state;
- PIPA/delta-V information;
- guidance thrust and timing.

### CONTROL

This pass also establishes that CONTROL-oriented CRT information spans multiple sources:

- LGC guidance/control values;
- ground-derived comparisons;
- non-LGC propulsion/control instrumentation.

That is a strong reason not to model MSK 1137 as a single subsystem-owned data packet.

## Remaining work

1. Locate the ground/RTCC processing definitions for LR coordinate conversion and PGNS/AGS comparison quantities.
2. Trace the non-LGC PCM/telemetry measurements used for actuator position, chamber pressure, voltages, temperatures, and validity flags.
3. Complete MSK 1123 field-by-field provenance using the same method.
4. Resolve exact CRT refresh behavior and station access/request workflow.
5. Only after those steps, create an implementation parameter dictionary.


## PIPA-bias workflow lead

Research note 033 documents a February 27, 1970 Apollo 13 planning procedure for lunar-surface PIPA-bias estimation. The method combines MPAD lunar gravity, gimbal angles, GUIDO's local-vertical attitude determination, and PIPA-derived measured gravity to form a ground bias estimate.

This resolves **one intended H-2 ground-computation workflow**, not the complete MSK 1137 BIAS/OCTAL implementation for all phases. The Apollo 13 Mission Operations Report independently confirms active PIPA-bias monitoring and actual CSM bias updates during the flown mission.

See `033_apollo13_pipa_bias_ground_workflow.md`.
