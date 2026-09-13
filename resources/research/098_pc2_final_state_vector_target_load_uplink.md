# 098 — Apollo 13 PC+2 final state-vector / target-load / uplink sequence

Date: 2026-09-13  
Status: **RESEARCHED — first-playable final-load sequence narrowed; exact RTCC vector components remain intentionally unfrozen**

## Question

Open question 33 asked which maneuver-state-vector / target-load / uplink steps should be expanded beyond the currently initialized first-playable state.

## Primary-source findings

### 1. PC+2 required a deliberately prepared LGC vector/target workflow

The Flight Control Division *Mission Operations Report — Apollo 13* records that the LGC could not simply be treated as a normal cislunar navigator after the accident. Flight Dynamics/Guidance therefore constrained the state-vector handling: RTCC vectors used for the LM were kept in the appropriate sphere of influence, the uploaded state vector was time-tagged at **TIG−30 seconds**, and the external ΔV components had to use the same sphere/reference basis as the vector.

This is operationally important. `state vector load status` and `target load status` are not merely generic readiness flags; they represent a coordinated ground-computed load package whose consistency mattered to GUIDO/Flight Dynamics.

### 2. There was more than one load cycle before PC+2

The Mission Operations Report records an updated PC+2 Maneuver PAD and a state-vector/target load uplink at approximately **75:35 GET**, followed by a **final** PC+2 maneuver PAD near **78:00 GET**. The contemporaneous air-ground record then shows Lovell explicitly asking at about **78:17 GET** whether Houston planned a state-vector update. CAPCOM replied that the ground needed the LM in **P00**, **DATA/ACCEPT**, and the **UPDATA LINK** circuit breaker configured, after which the update would be sent.

Therefore the first-playable should distinguish:

- earlier/preliminary PC+2 load complete;
- final load pending after AOS/final solution;
- crew/uplink configuration ready;
- final state vector + target load transmitting;
- final load complete / computer returned to crew.

The current single `pending_final_verification` state collapses too much chronology.

### 3. Flight-loop evidence ties GUIDO, INCO, CAPCOM, and FLIGHT together

The restored Flight Director loop records FLIGHT directing that, once the crew supplied **P00 and DATA**, Mission Control would put a **state vector and target load** into the LM. GUIDO states that the load must wait for the uplink configuration and that **INCO is working on it**. This supports a multi-station dependency rather than an instantaneous GUIDO-only state change.

Supported coordination chain:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink path configured → CAPCOM obtains crew P00/DATA + uplink configuration → ground sends state vector + target load → GUIDO/FLIGHT receive completion/readiness`.

This does **not** prove every internal CCATS/RTCC command step or exact console-key sequence.

### 4. Ranging remained part of the final-prep data path

After the state-vector transmission exchange, CAPCOM requested that the crew verify **Ranging** was selected because the ground needed it. The flight journal and PAO chronology place this in the same final-preparation window. The simulator should therefore preserve ranging availability as an INCO/FIDO dependency during final prep rather than treating it as decorative communications state.

### 5. The final target was stable after the update

At approximately **78:23 GET**, CAPCOM returned the computer to the crew; contemporaneous commentary records Flight Dynamics advising that no further PC+2 maneuver-PAD update was required. The final burn then occurred at **79:27:38.30 GET**.

For the first playable this is enough to support a state transition from `final_load_pending` to `final_load_complete/stable` before the GO/NO-GO poll, without inventing exact RTCC Cartesian components.

## First-playable implementation boundary

Add/retain explicit states at the information/product level:

- `ground.pc2.solution_stage`: `preliminary` → `final_ready` → `final_stable`;
- `pg_ns.state_vector_load_status`: `preliminary_loaded` → `final_pending` → `transmitting` → `final_loaded`;
- `pg_ns.target_load_status`: same staged states;
- `comm.uplink_configuration_ready`: crew/INCO path ready for load;
- `comm.ranging_enabled`: separately tracked and required for final trajectory support;
- optional event/audit records for `final_load_requested`, `final_load_transmission_started`, `final_load_complete`, and `computer_returned_to_crew`.

Do **not** add:

- fabricated state-vector Cartesian components;
- invented RTCC display identifiers;
- invented CCATS command strings;
- exact transmission duration unless directly sourced;
- automatic inference that successful communications means the load is verified;
- hidden diagnosis or branch information in GUIDO/INCO player views.

## Open-question disposition

Open question 33 is **resolved for first-playable workflow fidelity**: the project now has enough primary-source evidence to model the final vector/target/uplink sequence as a staged cross-station process.

Still deferred:

- exact Cartesian state-vector values at the scenario start/final load;
- exact RTCC/CCATS internal command path;
- exact controller CRT/key sequence;
- byte/word-level load contents beyond historically documented maneuver quantities.

These details should only be pursued when a propagator, exact-console reconstruction, or a scenario-specific failure mode requires them.

## Sources

1. NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970. Primary, mission-specific. NASA History scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
2. NASA, *Apollo 13 Technical Air-To-Ground Voice Transcription*, April 1970, NTRS 20160014370. Primary, mission-specific: https://ntrs.nasa.gov/citations/20160014370
3. Apollo 13 Flight Director loop recordings/transcription, Mission Control Center audio preserved by NASA JSC and presented by Apollo 13 in Real Time. Primary audio/transcript evidence for FLIGHT/GUIDO/INCO coordination; presentation site is a modern access layer: https://apollo13realtime.org/

See `resources/source-catalog/PC2_FINAL_LOAD_UPLINK_SOURCES.md`.