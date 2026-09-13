# 094 — PC+2 four-player boundary

Date: 2026-09-13  
Status: **RESEARCHED — no four-player PC+2 configuration approved at current fidelity**

## Question

Can the implemented five-player compact Apollo 13 PC+2 configuration be reduced to four human players without collapsing an operationally meaningful historical distinction?

## Primary-source findings

### CAPCOM and INCO are different functions

The Apollo 13 Press Kit places **CAPCOM** in mission command and control as the spacecraft communicator who serves as the voice contact with the flight crew. It separately places **INCO** in Systems Operations as the Communications Systems Engineer, sharing responsibility with O&P for monitoring and troubleshooting spacecraft/lunar-surface communications and coordinating MCC procedures with the network.

That evidence does not support treating CAPCOM and INCO as one historical job. More importantly for the simulator, the two roles sit on different sides of a useful information/action boundary:

- INCO assesses whether the communications/command path is usable and what communications-system state exists;
- CAPCOM is the privileged crew-facing voice path and deliberately transmits approved information to the crew.

### Communications are active during the selected PC+2 slice

The selected slice begins immediately after lunar occultation and deliberately includes communications recovery. The Apollo 13 mission record documents that the final PC+2 preparation interval includes loss/reacquisition of communications, final maneuver information passed to the crew, LM high-bit-rate data during burn preparation, and the communications/data path needed for ranging/uplink activity.

Therefore INCO is not merely an idle station that can be removed from this particular scenario without changing what the scenario asks players to reason about.

### Historical sharing does not generalize to CAPCOM + INCO

Apollo documentation records selected shared responsibility (notably INCO/O&P). That is evidence that Apollo sometimes paired related functions, but it does not justify an arbitrary CAPCOM/INCO merger. The documented INCO/O&P sharing joins technical communications and procedures coordination; CAPCOM remains separately defined as the crew voice contact.

## Design conclusion

The current **five-player compact configuration remains the minimum supported human configuration for the PC+2 first playable**:

1. FLIGHT
2. CAPCOM
3. LM SYSTEMS = TELMU + CONTROL
4. FLIGHT DYNAMICS = GUIDO + FIDO/RETRO
5. INCO

A general four-player mode is **not approved** at the current fidelity target.

This is not a claim that Apollo required exactly five people. It is a simulator-design boundary: reducing the current PC+2 player set further would require either:

- merging CAPCOM with INCO and thereby collapsing crew-voice authority with communications-system monitoring;
- hiding/automating an operationally active communications station;
- merging FLIGHT with a recommending technical discipline and thereby collapsing decision authority with source judgment; or
- otherwise removing coordination that the selected scenario is intended to exercise.

None is justified by the current historical evidence or by a demonstrated live-play need.

## What could reopen this decision

Four-player play may be reconsidered only if one of these conditions is met:

- live five-player testing shows a concrete usability requirement for a smaller mode;
- a different scenario window makes one station genuinely inactive/nonessential;
- stronger primary evidence supports a historically meaningful pairing that preserves the intended decision/communication boundaries; or
- the project deliberately adopts a lower-fidelity accessibility mode and labels the lost coordination explicitly.

Until then, do not implement CAPCOM+INCO, facilitator automation of INCO, or silent station omission for PC+2.

## Historical claim boundary

Supported:

- CAPCOM was the crew voice contact;
- INCO/CSE monitored and troubleshot spacecraft communications and shared communications/procedures responsibility with O&P;
- these were separately defined Mission Control functions;
- communications/data-path activity remained operationally relevant during PC+2 preparation.

Not supported:

- that Apollo historically combined CAPCOM and INCO for PC+2;
- that Apollo 13 PC+2 was staffed by the project's five-player compact arrangement;
- that five is a historical minimum staffing number.

## Primary sources

1. *Apollo 13 Press Kit*, NASA, 1970, Mission Control Center section, pp. 116–118 in the scanned kit.
   - https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A13_PressKit.pdf
   - CAPCOM is identified as crew voice contact; INCO/CSE and O&P are separately assigned communications-system monitoring/troubleshooting and MCC/network coordination.
2. *Mission Operations Report — Apollo 13*, Flight Control Division, 28 April 1970.
   - NASA/Apollo historical archive copy; PC+2 chronology and controller appendices.
   - Documents the PC+2 preparation interval, communications loss/reacquisition context, final maneuver information, high-bit-rate LM data during preparation, and separately documented controller responsibilities.
3. *Report of Apollo 13 Review Board*, Appendix A / flight-control organization material, NASA, 1970, NTRS `19700078804`.
   - https://ntrs.nasa.gov/citations/19700078804
   - Independently preserves distinct CAPCOM and INCO responsibilities and the selected INCO/O&P shared-console arrangement.

See `resources/source-catalog/PC2_LOW_PLAYER_COUNT_SOURCES.md`.
