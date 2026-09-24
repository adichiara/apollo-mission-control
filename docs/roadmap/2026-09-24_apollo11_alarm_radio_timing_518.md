# Roadmap update — Apollo 11 descent alarm radio timing

Date: 2026-09-24
Research note: 518
Parent: `docs/roadmap/2026-09-24_apollo11_descent_voice_scope_517.md`

## Change

NASA's primary GOSS NET 1 transcript now closes the **crew/CAPCOM radio-side timing** for key alarm calls. The first 1202 is explicitly spoken by the crew at 102:38:30/32 and receives the CAPCOM GO at 102:38:53. In the 1201 window CAPCOM acknowledges the alarm at 102:42:19, Armstrong identifies 1201 at 102:42:24, and CAPCOM gives the GO/same-type disposition at 102:42:25. A later 1202 is acknowledged by CAPCOM at 102:42:58.

The Mission Report event anchors remain separate. In particular, 102:38:22 (first 1202 event) precedes the explicit crew 1202 call by 8 seconds, while the 102:42:18 1201 event precedes CAPCOM's alarm acknowledgement by 1 second. Do not merge event and voice clocks.

## Immediate next work

1. Use these GOSS NET 1 timestamps as radio-side anchors when inspecting restored GUIDO L/R and NASA `792-AAI`.
2. Recover the internal Garman→Bales→Flight calls on their native recordings before assigning internal latency or overlap.
3. Reconcile the internal recording clocks to the radio/event anchors before asserting exact cross-loop timing.
4. Keep named Garman/Bales circuit, complete keyset privileges, GUIDO DRK/FDK mapping, and exact descent display callups unresolved pending direct evidence.
5. PHO-TN401 and a Mission-G-effective station/keyset/display record remain blocked recovery targets.

Source: https://ntrs.nasa.gov/citations/20160014392