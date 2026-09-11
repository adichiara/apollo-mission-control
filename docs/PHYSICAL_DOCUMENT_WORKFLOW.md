# Physical Document Workflow

Status: **design direction grounded in documented Apollo practice**

## Historical basis

Apollo Mission Control used multiple forms of physical hard copy.

Historical sources document:

- pneumatic-tube stations integrated into Mission Control consoles
- charts, graphs, messages, and other materials moved between operational areas
- teletype hard copy used to verify some RTCC transmissions
- controller-specific console handbooks
- Flight Control Operations Handbooks
- Flight Mission Rules
- mission plans, tables, and reference products

Hard copy was therefore part of the operational information system, not simply office paperwork.

## Project adaptation

For an in-person tabletop simulation, a physical sheet handed from one player to another can represent an Apollo hard-copy product that historically would have reached a controller through the MCC's pneumatic-tube/document-distribution system.

This is a **simulation adaptation**, not a claim that Apollo controllers literally passed the same sheet across the MOCR table.

The adaptation has several advantages:

- preserves the fact that information could arrive as a discrete document rather than appearing automatically on-screen
- creates a natural distinction between console telemetry and analysis products
- allows support-room/RTCC outputs to exist physically
- preserves finite controller attention
- avoids adding modern UI panels for information that was historically paper-based

## Current design decision

Use physical paper **where the historical information product was paper/hard copy or where a documented hard-copy path is the closest practical representation**.

Do not convert arbitrary digital telemetry into paper merely for atmosphere.

## Candidate document classes

These are research categories, not yet approved game components:

### Player reference documents

- Flight Mission Rules
- controller console handbook extracts
- Flight Control Operations Handbook procedures
- mission timelines
- controller-specific tables/reference pages

### Dynamically delivered hard-copy products

Potential examples to research:

- trajectory solutions
- maneuver products
- message/command verification
- plotted data
- generated tables
- support-room analysis
- updated procedures or flight-plan pages

### Administrative / simulation-control material

Could include scenario setup or SimSup materials, but these should not become visible to controller players unless historically appropriate.

## Representation options still open

The project has not yet chosen whether dynamic hard copy will be:

1. preprinted and released by SimSup at the appropriate time,
2. printed live by the server,
3. displayed to a non-player operator who physically hands over a prepared sheet,
4. produced through another practical mechanism.

The choice should depend on the actual source/product and the burden of live play.

## Important constraint

Physical paper should not become a disguised hint system.

If the historical product contained raw or processed data, the simulation paper should contain the corresponding information—not an explanation of what the player ought to conclude.

## Sources

- Apollo MCC Historic American Engineering Record, HAER TX-109-C.  
  https://www.nasa.gov/wp-content/uploads/2025/09/apollomc-habshaer.pdf

- Project Apollo 500 RTCC Operations Support Plan for Mission G, MSC Internal Note 69-FS-2.  
  https://www.ibiblio.org/apollo/Documents/RTCC%20Operations%20Support%20Plan%20for%20Mission%20G.pdf

- NASA-SP-287, *What Made Apollo a Success?*  
  https://ntrs.nasa.gov/citations/19720005243
