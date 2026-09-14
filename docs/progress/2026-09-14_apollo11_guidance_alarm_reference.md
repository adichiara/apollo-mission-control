# Progress — Apollo 11 guidance alarm reference

Date: 2026-09-14

## Completed

- Added a mission-neutral guidance-computer alarm/restart model.
- Kept alarm classification and restart-protected program identities caller supplied.
- Explicitly separated program-alarm state from abort/continue decisions and from independent guidance/radar/trajectory validity.
- Added synthetic unit tests.
- Added Apollo 11 Mission G powered-descent model-readiness profile.
- Added the actual-flight 102:37:30–102:43:22 powered-descent/program-alarm interval as a second historical scenario reference.
- Deliberately assigned the reference an unsupported `apollo11_descent_v1` adapter so the catalog exposes it as non-executable.
- Added research note 143 and a model-proof document.

## Source-backed Apollo 11 guidance boundary

The current evidence supports 1201/1202 Executive resource-exhaustion semantics, software restart, and P63/P64 restart protection. It does not support treating either alarm code alone as an automatic abort or continue command.

## Consequence

The simulator now has:

1. a first executable historical reference (Apollo 13 PC+2);
2. a second cataloged historical architecture reference (Apollo 11 powered descent);
3. generic runtime mechanics independent of PC+2;
4. a reusable guidance alarm/restart state model.

The remaining Apollo 11 gating domains are landing radar, independent PGNS/AGS observations, powered-descent propulsion/trajectory state, and controller-product/rule reconstruction.
