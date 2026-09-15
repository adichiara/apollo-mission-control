# Apollo 13 LM-7 Inverter Measurement Profile

## Status

**Partial historical vehicle-measurement profile.**

Profile:
`data/measurement_profiles/apollo13_lm7_inverter_electrical_partial.json`

Loader:
`src/apollo_mission_control/measurement_profiles.py`

This profile is intentionally executable only at the spacecraft
source-to-measurement boundary. It is **not** executable as an exact Apollo 13
Mission Control telemetry/display product.

## Why this profile exists

The generic measurement/output model needs historical profiles only where the
source evidence is strong enough to define the mapping without importing
adjacent-mission assumptions.

For the Apollo 13 PC+2 inverter contingency, the source record supports two
specific LM-7-family measurement identities:

- `GC0071V` — **VOLT INVERTER BUS**
- `GC0155F` — **FREQ INVERTER BUS**

The LM 7/8/9 Elementary Functional Diagram measurement index establishes those
measurement identities for the vehicle family that includes Apollo 13 LM-7.

NASA TN D-6845 Figure 27 independently shows the inverter-bus voltage and
frequency measurement paths, including isolation into PCMTEA telemetry, while
keeping the derived INVERTER caution logic separate.

Research notes 116, 117, and 119 preserve this evidence chain and its limits.

## Executable boundary

The profile may evaluate:

```text
authoritative selected inverter-bus electrical state
    ->
GC0071V voltage measurement
GC0155F frequency measurement
```

The project source-variable names:

- `inverter_bus_voltage_v_ac`
- `inverter_bus_frequency_hz`

are implementation identifiers. They are not claimed to be historical LMS,
spacecraft, PCM, or MCC variable names.

The profile deliberately labels its stage:

`vehicle_measurement_output_pre_ground_loading`

That distinction is important: a source-backed spacecraft measurement is not
automatically a sourced Apollo 13 console value.

## Ground-product boundary remains closed

`historical_ground_product_executable` is `false`.

The profile records the following unresolved downstream gates:

1. Mission H-2 TDFCB Revision 4 contents have not been recovered, so live
   Apollo 13 PCM format placement for these two measurements is unresolved.
2. Apollo 13 sample cadence is unresolved. The later LM-10 1 sample/s and
   0.2 sample/s assignments must not be copied into LM-7.
3. Exact MSFN/CCATS/RTCC processing and TELMU/CONTROL routing are unresolved.
4. Exact Apollo 13 CRT/MSK field, precision, refresh cadence, and display
   latency are unresolved.

The loader exposes `require_historical_ground_product()` as a hard gate. It
raises while these boundaries remain unresolved rather than selecting a
plausible route.

## Why later LM-10 data are not frozen here

Research note 119 shows that the LM-10 instrumentation packet treated
`GC0071V` and `GC0155F` as operational telemetry and assigned
format-dependent sample rates and primary MSK destinations. That is strong
continuity evidence, but LM-10 was Apollo 15's lunar module.

The current profile therefore does **not** import:

- LM-10 format membership;
- LM-10 1 Hz / 0.2 Hz sampling;
- LM-10 MSK destination numbers;
- LM-10 display routing.

Research note 120 separately shows why Apollo 13 AS-508 high-rate Format 30
figures must not be used as live PC+2 display cadence: those high rates describe
a post-pass playback capability.

## Mission H-2 configuration evidence

Research note 125 establishes that Mission H-2 had a mission-specific
**Telemetry Data Format Control Book Revision 4**, delivered before flight, with
LM Flight Control and PCM ground-station configuration products, and that its
PCMGS material was checked against PHO-TR155.

That proves the correct mission-specific configuration authority existed. The
surviving report does not expose the TDFCB contents, so the profile records the
missing H-2 loading as an archival gate rather than inferring it from the
existence of the book.

## Direct caution and selector state remain separate

This profile contains no direct ground channels for:

- the derived `GL4046` INVERTER caution;
- the INV 1 / INV 2 selector position.

Research note 117 records that the reviewed primary schematics positively show
PCMTEA taps for the underlying voltage/frequency measurements but do not
establish equivalent direct telemetry taps for the derived caution or selector
position.

The current first-playable information boundary therefore remains:

```text
GC0071V / GC0155F
    -> source-backed spacecraft measurements
    -> ground path only when H-2 configuration/routing is sourced

crew inverter action/report
    -> selected-inverter identity known operationally

crew caution observation/report
    -> onboard INVERTER caution persistence
```

These paths must not be collapsed into an invented direct ground Boolean.

## Tests

`tests/test_measurement_profiles.py` verifies that:

- the Apollo 13 profile is vehicle-mapping executable but ground-product
  blocked;
- only `GC0071V` and `GC0155F` are present;
- source-variable names are explicitly project implementation names;
- source-state evaluation produces the two measurement values;
- ground-product certification raises while downstream gates remain;
- profile discovery remains unique;
- contradictory "ground ready + unresolved gates" metadata is rejected;
- duplicate historical measurement identities are rejected.

## Evidence basis

Primary sources represented in the profile:

- *Lunar Module 7, 8, & 9 Elementary Functional Diagrams*, LED-267-37C,
  measurement index;
- NASA TN D-6845 / MSC-S-294, *Apollo Experience Report — Lunar Module
  Instrumentation Subsystem*, Figure 27;
- Philco-Ford PHO-TR474, 10 April 1970, for the Mission H-2 TDFCB Revision 4
  configuration-control boundary.

Repository research notes 116–120 and 125 preserve the detailed interpretation
and limitations.

## Next historical integration step

Recover Mission H-2 TDFCB Revision 4 or its special LM Flight Control / PCMGS
listings. If those documents establish actual live loading for these
measurements, the profile can advance the telemetry-loading gate without
changing the generic measurement model.

Exact controller display reconstruction remains a separate downstream question.
