# Apollo 13 AGS ullage logic and handbook chronology correction

Date: 2026-09-12  
Status: **REVIEWED-PARTIAL — mission-era ullage logic is strongly constrained; exact MSK 1123 AGS ULL/ACT VEL routing remains unresolved.**

## Purpose

Research note 046 recovered the AEA telemetry-list structure but misstated the document chronology of the Apollo 13 LM-7 handbook. This pass corrects that record and uses primary AGS specification/handbook evidence to narrow the physical quantity behind the ullage logic.

---

## 1. Handbook chronology correction

The Apollo 13 **LM 7 and Subsequent** Volume I is:

- document: **LMA790-3-LM**;
- Basic Date: **15 December 1968**;
- Change Date: **1 February 1970**.

The searchable **LM 10 and Subsequent** copy used to recover Table 2.1-7 is:

- document: **LMA790-3-LM**;
- Basic Date: **1 February 1970**;
- Change Date: **15 June 1970**.

Therefore the LM-10 copy is not a "same-basic-date" copy of the LM-7 handbook. It is a later configuration carrying a new basic date and a later change date.

The evidence rule is consequently stricter:

> **LM-10 Table 2.1-7 is continuity evidence only until the corresponding LM-7 table rows are directly inspected.**

The Apollo 13 Flight Journal and Smithsonian catalog independently confirm the LM-7-and-subsequent handbook identity and 1 February 1970 revision/change state.

---

## 2. Primary AGS specification defines the ullage test in velocity terms

The Grumman **Abort Guidance Section Specification** states that AGS ullage is detected when:

- accumulated velocity increments along the vehicle X axis exceed a threshold;
- the test is performed for each **2-second computer cycle**;
- the criterion must be satisfied for **three consecutive cycles**;
- loss of the criterion in a cycle resets the ullage condition.

The inspected specification revision gives a **0.2 ft/s** threshold.

This is important because the fundamental ullage discriminator is expressed as an accumulated velocity increment, not merely as a Boolean state or counter.

---

## 3. Later handbook wording preserves the same architecture but changes the engineering expression

The searchable LM-10 handbook describes AGS ullage as requiring the average +X acceleration to exceed **0.1 ft/s²** for three consecutive 2-second cycles.

That is dimensionally equivalent to **0.2 ft/s accumulated velocity per 2-second cycle**.

Thus the two sources describe the same physical test in two equivalent forms:

```text
average acceleration > 0.1 ft/s² for 2 sec
                  ⇕
accumulated +X velocity increment > 0.2 ft/s per cycle
```

This strengthens the physical interpretation without proving the exact Apollo 13 FP7 constant or display calculation.

---

## 4. Consequence for MSK 1123 AGS ULL

Cross-mission ASPO 45 definitions label **AGS ULL** as an *Abort Guidance ullage measurement* displayed in **ft/s**.

The AGS source architecture now contains three separate ullage-related objects:

1. the **2-second accumulated +X velocity increment** used for threshold qualification;
2. the **ullage counter**, which counts qualifying consecutive cycles and is telemetered separately;
3. the resulting **ullage-acquired state** used by engine-on logic.

Therefore:

- AGS ULL cannot be the raw ullage counter;
- AGS ULL cannot be merely the acquired/not-acquired Boolean;
- the strongest physical candidate is a velocity-valued quantity in the 2-second +X ullage-test chain.

However, no MCC/RTCC/display source inspected yet proves whether MSK 1123 shows:

- the current 2-second accumulated +X increment;
- a transformed/scaled version of that quantity;
- a related AEA telemetry accumulator;
- or another ground-calculated representation.

So the exact field source remains **unresolved**.

---

## 5. ACT VEL remains distinct

MSK 1123 separately defines **ACT VEL** as *accumulated velocity along thrust* in ft/s.

Although this sounds related to the ullage accumulation process, the display contains both AGS ULL and ACT VEL as separate rows. They must remain separate parameters unless a source explicitly defines their relationship.

Do not merge them merely because both involve accumulated velocity.

---

## 6. Table 2.1-7 cross-check

The searchable LM-10 Table 2.1-7 independently shows:

- words 20–22: compensated incremental body-axis velocity components accumulated per 20 ms;
- words 28–30: present LM inertial velocity components;
- word 31: ullage counter for telemetry;
- words 48–50: sensed velocity increments along LM body axes.

This again shows that several velocity layers coexist in the AEA data path.

The table does not itself label an MSK 1123 destination, so the controller-facing mapping remains a separate evidence question.

---

## Sources

### Apollo 13 mission-specific handbook identity

- *Apollo Operations Handbook, Lunar Module LM 7 and Subsequent, Volume I — Subsystems Data*, LMA790-3-LM, Basic Date 15 December 1968, Change Date 1 February 1970.
- Apollo 13 Flight Journal mission-document index: https://apollojournals.org/afj/ap13fj/a13-documents.html
- Smithsonian NASM catalog record: https://www.si.edu/object/archives/components/sova-nasm-xxxx-0093-ref859
- Search-index copy exposing the title pages/table list: https://www.scribd.com/document/942911911/a13-Lm-Aoh-v1-Lm7-Subs-300ppi

### AGS ullage logic

- Grumman Aircraft Engineering Corporation, *Specification, Abort Guidance Section*, engine-on/off command requirements and ullage-detection criterion: https://www.ibiblio.org/apollo/Documents/Specification%2C%20Abort%20Guidance%20Section.pdf

### Later handbook continuity / Table 2.1-7

- *Apollo Operations Handbook, Lunar Module LM 10 and Subsequent, Volume I — Subsystems Data*, LMA790-3-LM, Basic Date 1 February 1970, Change Date 15 June 1970: https://www.ibiblio.org/apollo/Documents/LMA790-3-LM10-ApolloOperationsHandbookLunarModuleLM10AndSubsequent-Volume1-SubsystemsData.pdf

### Display semantics

- Delco/AC Electronics, *Apollo 12 Guidance & Navigation Summary*, MSK 1123 definitions: https://ibiblio.org/apollo/Documents/apollo12_delco.pdf

---

## Next work

1. Directly inspect LM-7 Table 2.1-7 page images if a page-level copy becomes accessible.
2. Search PHO/RTCC/display-format material for AGS ULL and ACT VEL calculation definitions.
3. Search for a field-level equation or telemetry-ID mapping for MSK 1123.
4. Keep AGS ULL and ACT VEL separate in the eventual parameter dictionary.
