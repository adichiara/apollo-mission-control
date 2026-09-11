# Apollo 13 AGS Flight Program 7 — DEDA address evidence and in-flight validation

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — Flight Program 7 operational address structure is directly documented and selected addresses are validated by Apollo 13 in-flight use; exact MSK 1123 field routing remains incomplete.**

## Purpose

Research note 035 identified the Apollo 13 AGS / AEA side of MSK 1123 as the next major provenance gap.

The mission-specific Apollo 13 Flight Crew G&N Dictionary exists and is dated 25 March 1970, but the 36.9 MB scan is currently too large for the available PDF web reader. Rather than infer the missing AGS details, this pass uses two additional evidence streams:

1. the directly rendered **LM PGNS/AGS Training Card**, which explicitly documents **AGS Flight Program 7** operational DEDA addresses;
2. the actual Apollo 13 air-to-ground / Flight Journal record, which shows several of the same DEDA operations being used during the flown mission.

This provides a strong operational bridge while preserving the distinction between:
- FP7 DEDA memory/address semantics;
- spacecraft telemetry transport;
- Mission Control MSK 1123 CRT fields.

---

# 1. Flight Program 7 reference

## Source

TRW Systems Group, **LM PGNS/AGS Training Card**, October 1970.

The cover memo states that the card contains:

- PGNS LUMINARY Rev. 178;
- **AGS Flight Program 7**;
- operationally oriented data;
- only those DEDA-addressable quantities considered operationally useful.

The memo references the Apollo 14 LM-8 Flight Crew G&N Dictionary. Independent Virtual AGC comparison work reports that the Flight Program 7 address list agrees with the Apollo 13 G&N Dictionary, which is why the Apollo 13 dictionary is uniquely useful for FP7 where a full public source listing has not survived.

### Evidence classification

- The TRW card is a primary technical document for **Flight Program 7**, but is later than Apollo 13 and references Apollo 14.
- Apollo 13 mission use below independently validates selected parts of the address logic.
- Do not treat every address on the card as mission-specific Apollo 13 configuration until checked against the Apollo 13 dictionary or flight record.

---

# 2. Directly inspected Flight Program 7 address families

The training-card page was directly rendered and visually checked.

## AGS mode / alignment selector — address 400

The card documents several values of DEDA address 400:

### Attitude / steering

- **400 +0** — attitude hold
- **400 +1** — automatic guidance steering
- **400 +2** — Z-axis steering

### Alignment / calibration

- **400 +3** — AGS/PGNS alignment
- **400 +4** — lunar alignment
- **400 +5** — body-axis alignment
- **400 +6** — gyro/accelerometer calibration
- **400 +7** — accelerometer calibration

This is a good example of why a DEDA address cannot be modeled as one fixed “parameter.” The entered value selects operational logic.

---

# 3. Delta-V / burn-monitor address family

The training card's delta-V monitor material identifies:

- **404 / 405 / 406** — reset values used before the delta-V monitor;
- **450 / 451 / 452** — local-vertical delta-V / VG family;
- **470 / 471 / 472** — sensed delta-velocity family for the LM, expressed in local up/right/forward axes on the card;
- **500 / 501 / 502** — velocity-to-be-gained family for the LM, up/right/forward.

The card also contains:

- **267R** — delta-V to be gained magnitude in rendezvous material;
- **407 +1** — freeze local-vertical reference / start delta-V count in the select-logic area.

The exact relationship of these values to MSK 1123's **AGS VEL**, **AGS DEL VEL**, **AGS ULL**, and **ACT VEL** fields is not yet certified.

### Critical constraint

Do not equate:
- DEDA 470 automatically with CRT “AGS DEL VEL”;
- DEDA 500 automatically with CRT “ACT VEL”;
- DEDA 614 automatically with CRT “AGS ULL”.

The names are suggestive, but frame, scaling, transformation, and telemetry routing must be established first.

---

# 4. Navigation / timing addresses

The FP7 card directly lists operational addresses including:

- **377** — AGS clock time;
- **337R** — LM altitude;
- **360R / 361R / 362R** — LM present inertial velocity X/Y/Z;
- **367R** — LM altitude rate / HDOT;
- **340R / 341R / 342R** — LM present inertial position X/Y/Z;
- **344R / 345R / 346R** — CSM present inertial position X/Y/Z;
- **364R / 365R / 366R** — CSM present inertial velocity X/Y/Z.

These are strong candidates for understanding the source variables behind the “AGS velocity” portions of MSK 1123, but the final CRT path still needs the AEA telemetry/ground-processing source.

---

# 5. Accelerometer / gyro calibration addresses

The FP7 training card identifies:

- **540 / 541 / 542** — X/Y/Z accelerometer-bias values;
- **544 / 545 / 546** — X/Y/Z gyro-drift values;
- **550 / 551 / 552** — gyro attitude-rate scale-factor correction;
- **547** — lunar-alignment azimuth correction.

These fields connect directly to the broader Apollo 13 PIPA/AGS alignment research, but are AGS/AEA quantities and should remain distinct from the LGC PIPA-bias fields documented in research note 033.

---

# 6. Ullage logic addresses

The select-logic section identifies:

- **614R** — ullage counter, in 2-second count units;
- **616** — ullage counter limit, in count / 2-second terms.

This aligns with AGS documentation stating that ullage detection was evaluated over repeated 2-second computation cycles.

### Important non-equivalence

MSK 1123's **AGS ULL** is defined as an “Abort Guidance ullage measurement” in velocity units.

The DEDA 614 counter is therefore **not automatically the same displayed quantity**.

It is part of the AGS ullage logic and may help explain its derivation/status, but a direct CRT mapping would currently be an unsupported shortcut.

---

# 7. Apollo 13 actual in-flight validation

## Body-axis alignment

Apollo 13's actual voice record repeatedly uses:

**400 +5 — body-axis alignment**

Mission Control tells the crew to perform the AGS body-axis alignment before manual contingency burns.

The crew is subsequently instructed to return to **400 +0**, attitude hold.

This directly validates the Flight Program 7 400-address selector semantics during Apollo 13 itself.

## MCC-7 delta-V monitoring sequence

Before the final course correction, Mission Control calls for:

1. body-axis alignment;
2. zeroing **404, 405, 406**;
3. going to **470**.

Haise then reports approximately **-0.2 bias at 470** immediately before / as the burn begins.

The Apollo Flight Journal annotation explains that the sequence prepares the AGS to monitor acceleration for the burn and display it on the DEDA.

### Why this matters

This is more than a dictionary entry. It demonstrates an actual Apollo 13 operational workflow:

```text
establish attitude reference
        ↓
initialize/reset AGS delta-V state
        ↓
select monitored DEDA quantity
        ↓
inspect pre-burn bias
        ↓
execute burn
        ↓
use AGS indication as an independent burn monitor
```

This is a particularly useful simulator behavior because it preserves:
- preparation state;
- measurement bias;
- independent AGS monitoring;
- crew/Mission Control coordination.

---

# 8. Relationship to MSK 1123

MSK 1123 includes:

- AGS time;
- AGS body attitude;
- AGS attitude error;
- AGS indicated velocity;
- AGS measured delta velocity;
- AGS ullage measurement;
- DEDA address/readout/clear/register information.

The FP7 card and Apollo 13 flight record now establish concrete onboard meanings for multiple AGS addresses.

However, the following chain remains incomplete:

```text
AEA internal variable / DEDA address
        ↓
AEA telemetry encoding
        ↓
LM PCM / downlink
        ↓
ground decoding / scaling
        ↓
MSK 1123 field
```

Until the AEA telemetry mapping is found, the project should preserve DEDA addresses and CRT field identities as related but separate evidence objects.

---

# 9. Simulation consequences

The eventual AGS model should preserve at least three different interfaces:

## AEA internal state

Examples:
- velocity vectors;
- alignment state;
- bias / drift estimates;
- steering mode;
- delta-V accumulators;
- ullage logic.

## Crew DEDA interface

Examples:
- address selection;
- readout;
- entered selector values;
- continuous/held display behavior;
- manual reset / load sequences.

## Mission Control telemetry / CRT interface

Examples:
- decoded AGS engineering quantities on MSK 1123;
- current DEDA state if telemetered;
- ground comparisons against PGNS and trajectory products.

These must not be collapsed into one generic AGS “screen.”

---

# 10. Evidence boundaries

## DOCUMENTED

- Apollo 13 used the AGS Flight Program 7 family.
- FP7 training material preserves operational DEDA address semantics.
- Apollo 13 flight operations explicitly used 400+5, 400+0, 404/405/406, and 470 in contingency-burn workflows.
- MSK 1123 displays multiple AGS-derived quantities and DEDA state.

## STRONG CONTINUITY / PARTIAL

- The October 1970 FP7 training card address list is reported to agree with the Apollo 13 G&N Dictionary.
- Additional FP7 addresses on the card are strong candidates for Apollo 13 mapping.

## NOT YET ESTABLISHED

- exact AEA telemetry word/channel for each DEDA variable;
- which DEDA variables directly populate each MSK 1123 AGS field;
- field scaling and ground conversion;
- MSK 1123 refresh cadence;
- exact station request/access behavior.

---

# 11. Sources

### Apollo 13 mission-specific

- Apollo 13 Flight Crew G&N Dictionary, 25 March 1970 — identified on the Apollo 13 Flight Journal mission-document index; direct full scan currently exceeds available PDF reader limit.
- NASA, *Apollo 13 Air-to-Ground Voice Transcription* — confirms actual AGS procedures such as 400+5 / 400+0.
- Apollo 13 Flight Journal, Day 6 Part 4 — final course correction transcript and annotation for 404/405/406 → 470 sequence.

### Flight Program 7 technical reference

- TRW Systems Group, *LM PGNS/AGS Training Card*, October 1970:
  https://ibiblio.org/apollo/Documents/LM%20PGNS-AGS%20Training%20Card.pdf
- Directly rendered page 8 used for address transcription.

### Context / cross-check

- Virtual AGC AGS history and document-library notes comparing the Apollo 13 G&N Dictionary with FP7 material.

---

# 12. Next work

1. Locate an accessible transcription or page-level copy of the Apollo 13 G&N Dictionary AGS section for direct address comparison.
2. Locate AEA / AGS telemetry format documentation connecting Flight Program 7 memory quantities to LM PCM.
3. Map the MSK 1123 DEDA block itself: current address, readout, clear/register status.
4. Determine which of 1123 AGS VEL / DEL VEL / ULL / ACT VEL correspond to onboard FP7 variables versus ground-transformed values.
5. Preserve actual Apollo 13 burn-monitor sequences as candidate scenario/procedure validation cases, without yet turning them into gameplay abstractions.
