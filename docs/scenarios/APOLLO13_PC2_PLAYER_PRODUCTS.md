# Apollo 13 PC+2 — Minimum Player-Facing Product Set

Status: **implementation-oriented scope definition**  
Purpose: define the smallest historically defensible set of controller-facing information products required for the first PC+2 vertical slice.

## Principle

The first slice does not need a complete reconstruction of every station console.

A player-facing product is included only if it is needed to perform a documented PC+2 responsibility or apply a documented decision/shutdown rule.

Each product is classified as:

- **A — exact historical display/product substantially reconstructable now**;
- **B — historical product semantics documented, exact presentation incomplete**;
- **C — communication/report workflow documented, no dedicated display required for the slice**.

Where exact format evidence is incomplete, the first implementation may use a restrained period-appropriate tabular presentation, clearly marked in provenance as a project rendering of documented information rather than a claimed historical CRT transcription.

---

## FLIGHT

### Required products

| Product | Class | Purpose |
|---|---|---|
| Mission clock / phase reference | B | orient final preparation and burn sequence |
| Controller readiness reports | C | integrate GO/NO-GO |
| Mission Rules / PC+2 shutdown-rule reference | C | decision authority |
| CAPCOM/crew report stream | C | receive crew-side observations and confirmations |

### Explicitly excluded

FLIGHT does **not** receive an omniscient consolidated subsystem-health dashboard.

The first-slice FLIGHT interface should emphasize communication and decision integration rather than data density.

---

## FIDO / RETRO

### Required products

| Product | Class | Purpose |
|---|---|---|
| Accepted RTCC trajectory-solution status | B | establish current trajectory solution validity |
| Final PC+2 maneuver target/PAD product | B | target and maneuver verification |
| Return-plan product | B | landing area / return timing consequences |
| Post-burn trajectory solution status | B | determine whether burn achieved acceptable return state |

### Minimum fields

- target TIG;
- LVLH ΔV components;
- resultant ΔV;
- expected perigee;
- predicted landing latitude/longitude;
- predicted 0.05-g time / velocity / range-to-go;
- solution validity/currentness;
- post-burn solution pending/available state.

### Deferred

- exact historical FIDO/RETRO CRT layout;
- complete RTCC trajectory display catalog;
- exact Cartesian state vector until required by the physics implementation.

---

## GUIDO

### Required products

| Product | Class | Purpose |
|---|---|---|
| LM guidance/control real-time product | A/B | LGC/PGNS state, program/warnings, attitude/guidance monitoring |
| Final maneuver/load status product | B | state-vector and target-load verification |
| AGS backup/cross-check product | A/B | backup guidance availability and comparison |
| Post-burn residual product | A/B | assess guidance result |

### Historical display basis

MSK 1123 and 1137 are mission-specific Apollo 13 CRTs and can supply much of the visual language for GUIDO/CONTROL. Their complete field routing is not required for the first slice.

### First-slice fields

- LGC operating/program state;
- program alarm / LGC warning;
- alignment accepted / error estimate;
- state-vector load status;
- target-load status;
- PGNS Vg components;
- Vg remaining / ΔV gained as needed for burn monitoring;
- AGS available / cross-check acceptable;
- attitude error/rate information needed at the GUIDO boundary;
- post-burn residuals.

### Deferred

- noncritical MSK 1123 velocity rows;
- exact AGS ULL / ACT VEL routing unless a later failure case requires them;
- full DEDA-status reproduction.

---

## CONTROL

### Required products

| Product | Class | Purpose |
|---|---|---|
| LM guidance/control/propulsion real-time display family | A/B | principal burn monitoring |
| Propulsion-rule monitor | B | apply shutdown limits |
| Attitude/rate monitor | A/B | detect shutdown criteria |
| Warning/event indications | B | gimbal/CES/control failures |

### First-slice fields

- DPS engine running/state;
- throttle command / actual thrust representation;
- chamber pressure or documented ground thrust indication;
- inlet pressure;
- fuel/oxidizer differential pressure;
- GDA/gimbal warning/state;
- attitude error;
- body rates;
- CES DC failure;
- RCS ullage state;
- regulator/control configuration needed by the burn sequence.

### Critical historical distinction

The fuel/oxidizer ΔP rule is a **ground callout only**. The CONTROL product therefore must expose that ground measurement independently of crew indications.

### Deferred

- complete propulsion telemetry catalog;
- exact normal numeric pressure baselines where surviving evidence currently provides only shutdown thresholds.

---

## TELMU

### Required products

| Product | Class | Purpose |
|---|---|---|
| LM electrical-load/configuration product | B | verify burn power-up and post-burn power-down |
| Inverter/electrical warning state | B | shutdown-rule support |
| Limited consumables context | B | ensure burn configuration does not compromise return plan |

### First-slice fields

- LM power configuration;
- current draw, including approximately 38–40 A burn-configuration state;
- inverter warning/status;
- power-down status;
- only consumable quantities that can actually alter a PC+2 readiness decision.

### Deferred

- complete TELMU consumables dashboard;
- full ECS/EMU modeling;
- detailed water/O2/thermal state unless required by a later scenario branch.

---

## INCO

### Required products

| Product | Class | Purpose |
|---|---|---|
| Air-ground link status | B | manage weak post-AOS communication |
| Telemetry availability/quality | B | determine whether controller data are current |
| Uplink/command path state | B | support final guidance updates |
| Ranging state | B | support FIDO/trajectory solution |

### First-slice fields

- voice available / quality;
- telemetry available / validity / age;
- uplink available;
- ranging enabled/confirmed;
- S-band power-amplifier state or resulting link-quality state.

### Deferred

- exact MSK 1475 look-angle layout;
- detailed antenna-geometry product unless a communications failure case is added.

---

## CAPCOM

### Required products

| Product | Class | Purpose |
|---|---|---|
| Air-ground voice channel | C | sole normal operational crew communication path |
| Maneuver PAD / procedure text | C | transmit final target and rules |
| Crew readback/response stream | C | verify transfer and receive onboard observations |
| FLIGHT-directed callout queue | C | communicate GO/shutdown/procedure decisions |

CAPCOM should not have direct authoritative access to hidden subsystem state merely to make the interface easier.

---

## FAO / PROCEDURES

These functions are historically relevant but do not yet require dedicated player stations in the minimum vertical slice.

### Required system functions

- maintain the updated activity sequence;
- make the correct burn/power-down procedure available;
- preserve procedural ordering and dependencies;
- support FLIGHT/CAPCOM with procedure context.

Initial implementation may represent these as documented support products rather than separate player interfaces until player-count design is addressed.

---

## Cross-product metadata

Every controller-facing dynamic datum should be capable of carrying:

- sample time;
- receive time;
- validity;
- stale/unavailable state;
- source layer;
- provenance identifier.

This is required even when the first nominal run uses perfect communications after the initial weak-link period.

---

## First implementation display priority

### Priority 1 — build first

1. CONTROL burn-monitor product.
2. GUIDO guidance/load/residual product.
3. FIDO/RETRO target and return product.
4. INCO link/ranging product.
5. TELMU power/configuration product.
6. FLIGHT readiness/report view.
7. CAPCOM PAD/voice workflow.

### Priority 2 — add only if required by usability/validation

- additional MSK 1123/1137 fields;
- secondary trajectory displays;
- detailed consumables pages;
- antenna look-angle page;
- full DEDA/status panels.

---

## Historical-presentation rule

For an exact historical display, preserve its documented layout and labeling.

For a product whose semantics are known but exact screen is not, use a neutral project rendering that:

- uses historical terminology and units;
- does not add diagnosis or modern alert semantics;
- does not claim to be an exact Apollo screen;
- preserves source/validity distinctions;
- can later be replaced by an exact historical format without changing the underlying parameter model.

This permits implementation to proceed without inventing archival details.

## Sources / repository basis

- Apollo 13 *Mission Operations Report*, controller appendices and PC+2 chronology.
- Apollo 13 Technical Air-to-Ground Voice Transcription.
- Apollo 13 AC Electronics *Guidance & Navigation Summary*, MSK 1123/1137.
- Existing station specifications under `docs/stations/`.
- Research notes 029–050.
