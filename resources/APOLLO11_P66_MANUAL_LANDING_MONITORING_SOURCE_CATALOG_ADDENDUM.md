# Source catalog addendum — Apollo 11 P66 manual-landing monitoring

Date: 2026-09-21

## NASA TM X-58038 — Apollo 11 descent guidance monitoring

**Citation:** H. G. de Vezin Jr., C. C. Kraft Jr., C. B. Parker, and E. R. Schiesser, *Development of Guidance-Monitoring Techniques and Guidance-Monitoring Experience During the Apollo 11 Lunar Descent*, NASA TM X-58038, 1970.  
**URL:** https://ntrs.nasa.gov/citations/19700023940  
**Class:** NASA technical memorandum; primary/contemporary postflight engineering source.  
**Use:** authoritative for the ground guidance-monitoring architecture and Apollo 11 monitoring experience. Establishes PGNS/AGS/MSFN-ground-track comparison, descent abort/guidance-switchover monitoring purpose, the operational ~500-ft manual-landing boundary, and continued trajectory comparison after P66 initiation.  
**Limit:** does not by itself identify an exact Mission-G CRT field or prove a station-specific P66 voice call.

## Apollo 11 Mission Report — MSC-00171

**Citation:** NASA Manned Spacecraft Center, *Apollo 11 Mission Report*, MSC-00171, November 1969.  
**URL:** https://ntrs.nasa.gov/citations/19700008096  
**Class:** primary postflight mission report.  
**Use:** cross-check for P66/manual takeover at approximately 102:43:22 GET, terminal-descent trajectory/control behavior, and subsequent landing-radar-data loss.  
**Limit:** postflight reconstruction is not automatically a controller-visible real-time product.

## Apollo 11 Technical Air-to-Ground Voice Transcription

**Citation:** NASA, *Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)*, July 1969.  
**URL:** https://ntrs.nasa.gov/citations/20160014392  
**Class:** primary operational transcript.  
**Use:** bounds the crew-facing voice sequence around final descent and prevents insertion of unsupported CAPCOM calls.  
**Limit:** air-to-ground alone does not expose all internal MOCR loops.

## Apollo 11 Flight Mission Rules — Rule 5-91

**Repository treatment:** see `docs/roadmap/2026-09-21_apollo11_descent_trajectory_rules.md` and its source catalog.  
**Class:** primary operational rule evidence.  
**Use:** establishes the decision-semantic change after crew takeover: trajectory/guidance constraints are not themselves abort causes.

## Combined implementation result

The source chain supports:

`continued PGNS/AGS/ground observations → P66/manual crew control state → continued controller assessment → changed trajectory-rule semantics`

It does **not** support:

`P66 → ground data disappears`

or

`post-P66 trajectory deviation → automatic abort`.

## Evidence status

**SUFFICIENT** for the current manual-takeover monitoring/decision boundary. Exact Mission-G P66 indication, CRT field, keying, and internal voice-loop wording remain unresolved and non-blocking.