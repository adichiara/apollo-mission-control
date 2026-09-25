# 901 — Apollo 11 DPS Supplement 7 recovery boundary

Research thread: `apollo11-descent-runtime`

## Bounded question

Does currently recoverable primary evidence provide the Apollo 11 LM-5 Descent Propulsion System final-flight evaluation needed to calibrate a continuous as-flown powered-descent force history?

## Findings

The NASA/MSC controlled-document index identifies `MSC-00171`, Apollo 11 Mission Report, Supplement 7, **Descent Propulsion System, Final Flight Evaluation**. Its item-level entry gives **03-28-70** and **R. K. Seto**.

Later mission-report appendix tables use a different metadata field. The Apollo 13 Mission Report (MSC-02680, September 1970), table E-I, lists Apollo 11 Supplement 7 with **September 1970** under **Publication date/status**. Preserve both source statements rather than silently replacing one with the other.

The March 1970 Apollo 12 Mission Report still lists Apollo 11 Supplement 7 as **Preparation**. The report body itself has not been recovered in the present public-source path. NTRS does expose the adjacent Apollo 10 LM-4 DPS final-flight evaluation by R. K. M. Seto (TRW-11176-H314-R0-001 / NASA-CR-101869, 8 August 1969); that establishes report-family context only, not Apollo 11 constants or an Apollo 11 TRW identifier.

## Runtime consequence

Research 900's event/checkpoint-constrained runtime remains admissible. Exact continuous LM-5 thrust, specific impulse, mixture ratio, calibration uncertainty, or throttle-performance history must not be invented from nominal hardware values, plotted curves, or adjacent-mission reports.

The next discriminating evidence is the body of MSC-00171 Supplement 7 or equivalent primary LM-5 flight-performance/calibration material. Continuous historically calibrated LM-5 propulsion is therefore **BLOCKED**; checkpoint/event runtime implementation is not.

## Closure challenge

Targeted exact-title, document-number, author, and report-family searches recovered the controlled-document index and later publication/status tables but not the Supplement 7 body. Adjacent-mission DPS evaluations are not same-vehicle substitutes. Further broad searching is not decision-relevant without a new archive/repository lead.

## Sources

1. NASA Manned Spacecraft Center controlled-document index, public scan NTRS 19900007273, entry 00171.
2. NASA MSC, *Apollo 13 Mission Report*, MSC-02680, September 1970, table E-I.
3. NASA MSC, *Apollo 12 Mission Report*, MSC-01855, March 1970, mission-report supplement table.
4. R. K. M. Seto, *Apollo 10 LM-4, Descent Propulsion System Final Flight Evaluation*, TRW-11176-H314-R0-001 / NASA-CR-101869, 8 August 1969, NTRS 19690026326.

## Evidence status

- **DOCUMENTED:** MSC-00171 Supplement 7 title; controlled-document-index association with R. K. Seto and 03-28-70.
- **DOCUMENTED:** September 1970 Apollo 13 Mission Report table lists Apollo 11 Supplement 7 as September 1970 under “Publication date/status.”
- **DOCUMENTED:** March 1970 Apollo 12 Mission Report lists the supplement as “Preparation.”
- **PARTIALLY DOCUMENTED:** adjacent Seto/TRW DPS reports establish report-family context only.
- **BLOCKED:** exact LM-5 as-flown continuous DPS calibration/performance pending recovery of Supplement 7 or equivalent primary evidence.
