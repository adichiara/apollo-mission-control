# Apollo 13 PC+2 FIDO/RETRO Presentation Sources

Status: active source supplement for the first-pass FIDO/RETRO player-facing presentation.

## 1. Apollo 13 final P30 LM maneuver PAD

- **Source class:** PRIMARY, contemporaneous mission communications
- **Interval:** approximately 77:52 GET
- **Use:** Final PC+2 target: TIG 79:27:38.30 GET; LVLH delta-V +833.0 / -50.9 / -213.9 fps; resultant 861.5 fps; expected perigee 20.5 nmi.
- **Presentation consequence:** Defines the maneuver-target section of the first FIDO/RETRO project rendering.
- **Limitation:** Does not establish the exact ground CRT layout used by FIDO or RETRO.

## 2. Apollo 13 final PC+2 monitor PAD

- **Source class:** PRIMARY, contemporaneous mission communications
- **Time:** 78:00:58 GET
- **Use:** Final Noun 61 return values: latitude -21.65 deg, longitude -165.00 deg, range-to-go 1163.5 nmi, entry-interface velocity 36,292 fps, 0.05-g GET 142:39:22.
- **Presentation consequence:** Defines the return-plan product already frozen in the nominal fixture.
- **Limitation:** Crew-facing PAD evidence does not prove the exact FIDO/RETRO console formatting.

## 3. Mission Operations Report — Apollo 13, FIDO Post Mission Report

- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes FIDO responsibility for ground trajectory solutions, tracking-data quality, vector selection/comparison, and RTCC trajectory state.
- **Presentation consequence:** Supports separate ground-solution status and reinforces that trajectory data can be present yet questionable or wrong.

## 4. Mission Operations Report — Apollo 13, RETRO Post Mission Report

- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes RETRO responsibility for return/reentry planning, PC+2 return-time/landing-area tradeoffs, recovery geometry, and use of accepted trajectory products.
- **Presentation consequence:** Supports return-plan/landing consequences as distinct from raw trajectory state.

## 5. Apollo 13 Mission Report

- **NASA report:** MSC-02680 / NASA-TM-X-66449
- **Date:** September 1970
- **Source class:** PRIMARY, mission report
- **Use:** Confirms that the PC+2 descent-engine maneuver shortened transearth transit and moved the landing point from the Indian Ocean to the South Pacific.

## Repository research

- `resources/research/076_pc2_fido_retro_player_presentation_boundary.md`
- `docs/stations/APOLLO13_FIDO.md`
- `docs/stations/APOLLO13_RETRO.md`

## Evidence rule

Do not:

- substitute GUIDO residuals for a FIDO post-burn trajectory solution;
- infer satisfactory return trajectory merely from physical burn completion;
- fabricate an RTCC Cartesian state vector or propagated landing solution;
- expose hidden integrity metadata;
- claim the project rendering is an exact FIDO/RETRO CRT.
