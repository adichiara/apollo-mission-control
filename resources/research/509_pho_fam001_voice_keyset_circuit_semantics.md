# Research Note 509 — PHO-FAM001 voice-keyset circuit semantics

**Date:** 2026-09-23  
**Status:** REVIEWED-PARTIAL

## Primary technical source

Philco-Ford / Western Development Laboratories, *Familiarization Manual — Mission Control Center Houston*, PHO-FAM001, revised through 30 June 1967.

https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf

## Finding

Section III, paragraph 3-2-2-1 provides the primary technical-system description that complements Jack Garman's participant account. The MCC voice intercom was an internal communications network operated from station keyset units. Pushbutton keys connected a station to **local conference loops** or **intersite loops**. Critically, the manual says a keyset could provide **talk/listen** circuits or **monitor-only** circuits.

Section II also states that station keyset units existed in different configurations according to usage requirements and were installed at consoles, desks, walls, pedestals, and equipment racks. The associated control/interconnection circuitry provided the MCC-H internal communications network. Air/ground control was a separate equipment function that keyed remote ground-to-air transmitters.

## Consequence

The repository's separation of `monitor` and `talk` privileges is now supported by both:

1. a contemporary primary technical manual (PHO-FAM001), which explicitly distinguishes talk/listen from monitor-only circuits; and
2. Garman's firsthand account, which describes the operational talk/listen distinction and restricted A/G transmit authority.

The runtime may therefore treat voice access as a per-loop capability rather than binary loop membership. A station can legitimately monitor a circuit without having transmit authority on it.

PHO-FAM001 also supplies safe generic circuit classes — local conference loop and intersite loop — but **does not identify the Apollo 11 Bales/Garman alarm-assessment loop** or the exact Mission-G per-station keyset matrix.

## Effectivity boundary

PHO-FAM001 is revised through 30 June 1967. It establishes MCC-H system architecture before Apollo 11, not the exact 20 July 1969 Mission-G configuration. Mission-specific Apollo 11 Mission Rules remain controlling for documented Mission-G loop names. No exact GUIDO/support-room assignment is inferred by combining the two sources.

## Next discriminating evidence

A Mission-G-effective station/keyset configuration record is still required to freeze exact station-to-loop assignments and privileges. PHO-TN401 remains blocked pending archival recovery for display/control configuration and is not assumed to contain voice-keyset assignments.

## Evidence status

- **DOCUMENTED / PRIMARY TECHNICAL:** station keysets connected to local conference or intersite loops and could provide talk/listen or monitor-only circuits.
- **DOCUMENTED / PRIMARY TECHNICAL:** keyset configurations varied by usage requirement; A/G transmitter control was a distinct subsystem function.
- **CORROBORATED:** runtime distinction between loop monitoring and loop transmission.
- **UNRESOLVED:** Apollo 11 GUIDO ↔ AGC-support loop identity, complete 20 July 1969 keyset privilege matrix, and exact alarm-assessment channel.
- **BLOCKED ON DOCUMENT RECOVERY:** Mission-G-effective station/keyset configuration; PHO-TN401 direct inspection remains separately blocked for display/control configuration.
