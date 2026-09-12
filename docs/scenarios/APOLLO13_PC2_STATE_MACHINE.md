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

**Entry:** **79:27:28.30 GET**, ten seconds before TIG.

Historical commanded/procedural profile:

- manual ullage;
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

**Entry:** TIG **79:27:38.30 GET**.

Historical commanded/procedural profile:

- minimum-throttle segment begins at ignition;
- after 5 seconds, at **79:27:43.30**, the procedure commands 40-percent throttle.

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

The commanded throttle state is not the same thing as exact physical engine response or the crew's later voice report.

---

### S9 — `pc2_40_percent_thrust`

**Commanded entry:** **79:27:43.30 GET**, TIG + 5 seconds.

Historical commanded profile:

- 21 seconds at 40 percent;
- command to maximum thrust at **79:28:04.30 GET**.

Historical air-ground record:

- at **79:27:51**, Lovell reports that the engine is burning at 40 percent.

Required model behavior:

- commanded and actual thrust remain separate values;
- the 79:27:51 crew report is a communication event, not the authoritative throttle-transition timestamp;
- controller-visible measurements can differ from true state if a later telemetry/sensor failure is injected.

---

### S10 — `pc2_full_thrust`

**Commanded entry:** **79:28:04.30 GET**.

Historical evidence:

- final maneuver instructions call for maximum thrust for the remainder of the burn;
- at **79:28:09**, Lovell reports 100-percent thrust.

Required model behavior:

- the maximum-thrust command, physical engine response, telemetry indication, and crew voice report remain distinct layers;
- detailed physical DPS ramp/lag dynamics are deferred until required by a controller decision or failure case.

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

## Command / physical / information timing boundary

The first executable model must preserve the following distinction during the throttle sequence:

```text
crew procedure / throttle command
        ↓
engine physical response
        ↓
telemetry / onboard indication
        ↓
crew voice report / ground interpretation
```

The currently frozen 79:27:43.30 and 79:28:04.30 events are **command/procedure milestones** derived from the final maneuver instructions. They are not claims that the physical engine reached exactly 40 or 100 percent at those instants.

A NASA postflight LM-systems analysis contains a more detailed physical throttle/ramp description, but its rounded segment timing and timing convention are not yet reconciled with the higher-precision Flight Control Division TIG/cutoff validation values. Detailed engine-response timing therefore remains deferred. See `resources/research/051_pc2_ullage_and_throttle_profile.md`.

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
7. begin manual two-jet ullage at 79:27:28.30 and sustain it to TIG;
8. ignite/minimum-throttle command at 79:27:38.30;
9. command 40 percent at 79:27:43.30 and maximum at 79:28:04.30;
10. preserve the later 79:27:51 and 79:28:09 crew throttle reports as separate communication events;
11. trigger none of the documented shutdown conditions;
12. cut off at 79:32:02.12 GET;
13. produce the documented small PGNS residuals within validation tolerance;
14. enter post-burn verification and power-down transition.

## Sources

Primary authority:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, especially Flight Director, GUIDO, CONTROL, FIDO/RETRO and systems-controller sections.
- Apollo 13 Technical Air-to-Ground Voice Transcription, for final PAD/procedure and communication/readback timing.
- NASA TM X-66935 / REPT-70-FC13-47-ADD-1, *Analysis of Apollo 13 lunar module systems during emergency operation following command service module oxygen tank explosion*, for later physical DPS-response refinement.

Navigation aid / corrected transcript:

- Apollo 13 Flight Journal, Day 4 Part 2, *Leaving the Moon*.

The Flight Journal is used to navigate the underlying mission record; computed maneuver times and engineering validation values are taken from NASA mission documentation where available.
