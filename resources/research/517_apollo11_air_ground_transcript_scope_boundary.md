# Research note 517 — Apollo 11 air-ground transcript scope boundary

Date: 2026-09-24
Status: DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC SOURCE SCOPE

## Question

Can NASA's contemporary Apollo 11 technical voice transcript be used to close any part of the open descent-alarm voice chronology, and what does it *not* record?

## Primary source

NASA, _Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)_, NTRS document 20160014392, publication date July 1969.

NTRS catalog:
https://ntrs.nasa.gov/citations/20160014392

NASA History's mission-transcript collection independently catalogs `AS11_TEC.PDF` as the Apollo 11 Technical Air-to-Ground Voice Transcription and describes the collection as transcripts made from recorded air-to-ground transmissions:
https://www.nasa.gov/history/mission-transcripts-mercury-gemini-and-apollo/

## Finding

The source identifies itself specifically as **GOSS NET 1 / technical air-to-ground voice**. Its evidentiary scope is therefore the spacecraft-ground radio path. It is primary evidence for the crew-facing side of the alarm exchange, but it is not a transcript of the internal MOCR conference loops, GUIDO headset channels, support-room circuits, or Flight Director loop.

This closes an evidence-control ambiguity in the current descent work: the technical air-ground transcript may establish what Eagle transmitted and what CAPCOM transmitted to Eagle, but it cannot establish the missing Garman → Bales → Flight internal wording, named loop, overlap, or timing merely because those internal actions led to a later CAPCOM call.

The direct-audio plan therefore remains necessary. Internal voice claims must come from the restored Historical Recorder GUIDO L/R recordings and/or NASA `792-AAI` Flight Director-loop audio, with the Mission Report event times used only as search anchors.

## Simulator consequence

For the Apollo 11 reference implementation, keep the crew radio path and controller internal-loop path as distinct evidence domains. A CAPCOM air-ground disposition may be reproduced when supported by the air-ground record; preceding internal calls must not be reverse-engineered from that disposition unless separately supported.

This is consistent with the Mission-G Flight Mission Rules' separate identification of A/G loops and internal MOCR loops and with PHO-FAM001's distinction among station circuits.

## What this does not establish

- exact internal wording by Garman, Bales, Kranz, or other controllers;
- the name of the Garman/Bales back-room circuit;
- exact internal-call timing or overlap;
- complete station keyset privileges;
- reconciliation of GOSS NET 1 timestamps with Historical Recorder / IRIG-B or `792-AAI` clocks.

## Evidence status

- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC SOURCE SCOPE:** `AS11_TEC` is GOSS NET 1 air-to-ground evidence.
- **SUFFICIENT FOR EVIDENCE CONTROL:** crew/CAPCOM radio claims and internal-controller voice claims must be sourced separately.
- **OPEN:** direct GUIDO L/R ↔ `792-AAI` internal chronology and clock reconciliation.
