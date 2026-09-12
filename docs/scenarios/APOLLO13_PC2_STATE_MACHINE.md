# Apollo 13 PC+2 Nominal State Transition Model

Status: **implementation-oriented historical baseline**  
Scenario start: **77:55:00 GET**  
Scenario endpoint: **post-burn verification / power-down transition**

## Purpose

This document converts the source-backed PC+2 chronology into a minimal simulation state machine.

It deliberately does **not** script every historical switch throw or crew action. Only transitions that materially affect controller information, readiness, burn execution, shutdown logic, or validation are frozen here.

The scenario should reproduce the historical nominal sequence while allowing later failure injections to perturb the underlying state and therefore produce different controller decisions.

---

## State model

### S0 — `pc2_final_pad_link_weak`

**Entry:** 77:55:00 GET.

Historical conditions:

- spacecraft is docked CSM/LM stack;
- LM is the active lifeboat;
- prior alignment checks and Mission Rules review are complete;
- air-ground communications have been reacquired after lunar occultation but are weak;
- final PC+2 target information is ready to be passed;
- burn configuration has not yet been fully powered.

Controller consequences:

- CAPCOM can begin final maneuver-PAD transfer;
- INCO sees usable but poor communications quality;
- GUIDO/FIDO own the maneuver data being delivered;
- other stations remain in preparation/monitoring state.

**Nominal transition:** final PAD transmission/readback begins at 77:55:24.

---

### S1 — `pc2_final_pad_transfer`

Historical behavior:

- CAPCOM reads the final P30 LM maneuver PAD;
- weak communications interfere with the exchange;
- crew changes S-band power-amplifier configuration;
- communications become satisfactory for completion of readback.

Required simulation behavior:

- PAD transfer is an information event, not automatic hidden state synchronization;
- the crew/readback channel and ground target state remain distinct;
- communications quality can affect whether the exchange is completed cleanly.

**Nominal evidence point:** communications are reported loud and clear at approximately 77:59:17 GET.

**Exit condition:** final PAD/readback accepted and communications adequate for subsequent preparation.

---

### S2 — `pc2_burn_configuration_powerup`

Approximate historical onset: 78:12 GET.

Historical conditions/actions:

- LM systems required for the maneuver are powered;
- electrical load rises to approximately 38–40 A;
- guidance/control, propulsion, communications, and ranging support enter burn-ready configuration.

Controller consequences:

- TELMU monitors electrical load/configuration;
- CONTROL monitors propulsion/control readiness;
- GUIDO monitors LGC/PGNS state;
- INCO maintains communications/ranging/uplink path.

**Exit condition:** required systems are powered and stable enough for final data/ranging activity.

---

### S3 — `pc2_final_ground_computer_support`

Historical evidence:

- ranging is explicitly requested/confirmed at 78:21:54–78:22:15;
- at 78:23:05 CAPCOM tells the crew, “The computer is yours”;
- Flight Dynamics advises that no further PC+2 PAD update is required.

Required simulation behavior:

- ranging and uplink/computer-support state are explicit;
- crew computer availability can be temporarily constrained by ground update activity;
- FIDO/GUIDO products must reach an accepted final state before final readiness.

**Exit condition:** final targeting/uplink activity complete; computer returned to crew; no further target update required nominally.

---

### S4 — `pc2_final_readiness`

Historical interval: roughly 78:23 through final GO poll.

Required readiness dimensions:

- trajectory target accepted;
- PGNS/LGC operational;
- AGS available as backup/cross-check;
- alignment accepted;
- DPS/RCS ready;
- LM electrical state satisfactory;
- communications usable;
- no documented shutdown criterion already active.

Controller behavior:

- stations monitor their own information, not a common omniscient readiness flag;
- FLIGHT integrates reports.

**Nominal transition:** final GO/NO-GO poll around 79:17 GET results in GO.

---

### S5 — `pc2_go_for_burn`

Historical result: team is GO.

Simulation rule:

`FLIGHT GO` is a decision state produced from controller reports. It must not be generated merely because the authoritative simulation is nominal.

Required consequences:

- crew receives continuation through CAPCOM;
- guidance/control sequence proceeds toward P40 and ignition;
- controllers continue monitoring because GO does not disable shutdown logic.

---

### S6 — `pc2_p40_preignition`

Historical evidence:

- by approximately 79:23 GET the LM is in Program 40;
- final countdown proceeds;
- engine is armed;
- ullage and ignition preparation occur immediately before TIG.

Required authoritative state:

- P40 active;
- target Vg loaded;
- ullage available;
- DPS ready;
- attitude/rates within limits;
- warnings nominal.

The simulator should not require exact second-by-second cockpit switch choreography unless a future procedure/failure case depends on it.

---

### S7 — `pc2_ullage`

Historical maneuver specification:

- two RCS jets;
- 10 seconds.

Purpose:

- settle DPS propellants before engine start.

Required model behavior:

- RCS ullage is a real propulsion/control event;
- loss of ullage capability can later be used as a failure injection;
- nominal ullage leads to DPS ignition readiness.

**Exit:** ignition at 79:27:38.30 GET.

---

### S8 — `pc2_dps_start_minimum_thrust`

**Entry:** TIG 79:27:38.30 GET.

Historical planned profile:

- initial minimum-thrust period approximately 5 s;
- crew reports the engine burning and 40-percent thrust shortly after ignition.

Required monitoring begins immediately:

- chamber/thrust indication;
- inlet pressure;
- fuel/oxidizer differential pressure;
- attitude error;
- body rates;
- gimbal warning;
- LGC/ISS/program-alarm state;
- CES DC power;
- inverter condition.

Startup transients must be treated separately from steady-state attitude/rate limits where historically specified.

---

### S9 — `pc2_40_percent_thrust`

Historical profile:

- approximately 21 s at 40% after the minimum-thrust start segment.

Historical air-ground record:

- crew reports 40% thrust after ignition.

Required model behavior:

- commanded and actual thrust remain separate values;
- controller-visible measurements can differ from true state if a later telemetry/sensor failure is injected.

---

### S10 — `pc2_full_thrust`

Historical evidence:

- crew reports 100% thrust shortly after the 40% phase;
- burn continues at maximum thrust for the principal ΔV accumulation.

Controllers continue applying the same shutdown criteria throughout the burn.

There is no generic “burn nominal” state exposed to players.

---

### S11 — `pc2_guided_burn_monitoring`

This is the sustained burn phase.

Authoritative state evolves continuously:

- physical thrust/acceleration;
- velocity change;
- PGNS velocity-to-be-gained;
- guidance residuals;
- attitude/rates;
- propulsion pressures/status;
- electrical/control warnings;
- telemetry freshness/validity.

Ground and crew information remain separate.

Nominal historical expectation:

- no shutdown criterion is triggered;
- Mission Control periodically reports that the burn looks good.

A future nonnominal case should be implemented by perturbing these underlying quantities, not by changing a scripted success flag.

---

### S12 — `pc2_guided_cutoff`

Historical physical/guidance cutoff:

- **79:32:02.12 GET actual**;
- planned cutoff 79:32:01.99;
- actual burn duration 263.82 s.

Important timing rule:

- physical/guidance cutoff time is authoritative for simulation validation;
- crew voice report occurs later and is a communication event.

Required consequences:

- DPS thrust falls to zero;
- guidance transitions to residual/postburn state;
- controllers assess residuals and vehicle condition.

---

### S13 — `pc2_residual_review`

Historical PGNS residual target values:

- X approximately +1.0 ft/s;
- Y approximately +0.3 ft/s;
- Z approximately 0.0 ft/s.

Historical decision:

- small residuals are accepted and left untrimmed.

Required player workflow:

- GUIDO evaluates guidance result;
- FIDO awaits/uses post-burn trajectory determination;
- CONTROL verifies propulsion/control condition;
- FLIGHT integrates burn-success assessment.

No single “burn success” field should bypass those discipline reports.

---

### S14 — `pc2_postburn_powerdown`

Historical onset: approximately 79:34 GET.

Required behavior:

- TELMU leads/monitors return toward low-power LM configuration;
- guidance/control functions needed for subsequent attitude-control activity remain according to the historical configuration;
- first vertical slice may terminate once burn verification and the power-down transition are established.

This is the initial endpoint of the first implementation. Subsequent PTC establishment belongs to an expansion of the slice.

---

## Failure-transition architecture

The nominal chain above must not be implemented as an unconditional timer sequence.

Future failure injections may interrupt or branch it through documented conditions such as:

- inadequate communications preventing clean target transfer;
- unavailable ranging/uplink support;
- guidance/computer warning;
- unacceptable attitude/rate;
- inadequate DPS thrust/chamber pressure;
- low inlet pressure;
- excessive fuel/oxidizer differential pressure;
- gimbal warning;
- CES DC failure;
- persistent inverter warning;
- premature engine shutdown.

For premature engine shutdown, the Mission Rules review included a documented restart procedure if the shutdown was not caused by one of the specified mandatory-shutdown conditions.

That branch should be added only when the first nonnominal scenario is authored.

---

## Validation contract

A deterministic nominal run must satisfy:

1. start at 77:55:00 with weak but available air-ground communications;
2. complete final PAD exchange after communications improve;
3. enter burn electrical configuration near the documented period;
4. complete final ranging/uplink support and return computer control to crew;
5. reach a controller-derived GO state;
6. enter P40 before ignition;
7. perform two-jet, 10-s ullage;
8. ignite at 79:27:38.30 GET;
9. progress through minimum/40%/full-thrust profile;
10. trigger none of the documented shutdown conditions;
11. cut off at 79:32:02.12 GET;
12. produce the documented small PGNS residuals within validation tolerance;
13. enter post-burn verification and power-down transition.

## Sources

Primary authority:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, especially Flight Director, GUIDO, CONTROL, FIDO/RETRO and systems-controller sections.
- Apollo 13 Technical Air-to-Ground Voice Transcription, for communication/readback timing.

Navigation aid / corrected transcript:

- Apollo 13 Flight Journal, Day 4 Part 2, *Leaving the Moon*.

The Flight Journal is used to navigate the underlying mission record; computed maneuver times and engineering validation values are taken from NASA mission documentation where available.
