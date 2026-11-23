# Eutyches: card edits

Existing fields kept word for word (checked by comparison with Card.existing.json). No "clearly wrong" correction was needed; no existing claim contradicts a held source or the brief. Validator on a scratch copy: only the four errors that release settles remain (secondReading on the two quotations of six words or more; the two renderings not yet in tools/quote_renderings.json).

## New (appended, nothing reordered)

- **legacy.traces**, five added. Peter Mongus and the Henotikon: Zach 5987-5991, 6006-6008, 6161-6163. Life of Severus and Severus's letters: Life of Severus 6855-6858, 7363-7366; Severus letters 711-722. Philoxenus: 1569-1573. Ormanian: 5307-5310. Canon 95 of 692: Councils 30126-30129 (heading at 30100-30101).
- **legacy.remembered**, one added. Michael the Syrian repeats the chronicle's charge: Michael 1706-1712.
- **uncertain**, nine added (outline "to the card" items): Leo's letter of June 1, 448 (Leo 4479-4489; Quesnel note 4475-4477); palace soldiers (Zach 1125-1128, 1206-1213); the emperors' letter against the Syriac heading (Perry 23250-23252, 23291-23293); recantation versus orthodox minutes, and Evagrius on the acts confirmed (Zach 1308-1310; Perry 24016-24020; Evag-E 1741-1745); Nestorius on suborned accusers (Bazaar 18910-18914); the rain or snow image (Zach 1195-1197); seventy years and shipwreck (Leo 4609-4611); the damaged Greek of Q1 (Evag-G 2285-2289; Evag-E 1729-1731; Leo 5597-5598); Hefele on canon 95 (Councils 30147-30150).
- **sources.about**, eight added so every cited file is held: Evagrius (English and Greek), Nestorius's Bazaar, Life of Severus, Severus's letters, Philoxenus, Ormanian, Michael the Syrian.
- **briefReferences**, nine lines, no quotation marks. Each traces to the brief's sentences and the lines in Source_Sheet.
- **quotationOriginals**, three, one per quoted span in the brief:
  1. Q1 (brief paragraph 1). Printed English Perry 23843-23845; Greek Evag-G 2285-2286 checked by hand, ending at "μίαν φύσιν" because a garbled line (2287-2288) falls before the last word; noted under `uncertain`. No secondReading (six words or more).
  2. Q2 (brief paragraph 6). Perry 23494-23495 only; a page break and running head fall at 23496-23503, so the printed wording stops at "against" and the card notes the rest (line 23504). No secondReading.
  3. Q3 (brief paragraph 5). Leo 5028, "this he certainly never did"; secondReading "checked at card" (five words).
- `briefLength` not added (not an allowed key).

## Not found

None. Two items carried from the existing card were not re-checked against a held clean print: Chrysaphius as godson (Liberatus, rough scan, and Feltoe's introduction) and exile after Chalcedon (Feltoe's summary). They stay as the card words them.

## Scan readings to add

None. The checker lists no scan readings.

## Second pass (2026-11-23)

**Checker changes (all four applied word for word, each old text found once)**
1. `uncertain[5]`: "That he was exiled further after Chalcedon rests on ..." became "That he was in exile after Chalcedon rests on Feltoe's summary of a letter of Leo that the English edition does not translate, which suggests he be banished to a still remoter place." Evidence: Leo 11331-11333.
2. `uncertain[13]`: now "In his letter to Leo he asked not to be expelled after seventy years of continence, and so suffer shipwreck at the very end of life. The seventy years are his own claim." Evidence: Leo 4608-4611.
3. `uncertain[15]`: "Hefele, an editor, doubts ..." became "Hefele, a historian of the councils, doubts the text of canon 95". Evidence: Councils 30148.
4. `briefReferences[1]`: "the genuine followers of Dioscorus and Eutyches reduced to a small number." became "the refusing churches called followers of Dioscorus and Eutyches." Evidence: the brief's sentence; Evag-E 6794-6797.

**Items added from the outline: none.** Every item the outline marks "to the card" (Outline.md lines 74, 103-105, 107, and the Cut first items 1, 3, 4, 6) was already held, so nothing was added:
- Leo's letter of June 448 (Cut first 1): `uncertain`, Leo 4479-4489.
- Severus of Antioch against him (Cut first 3): `legacy.traces`, Life of Severus 6855-6858.
- Palace soldiers (Cut first 4): `uncertain`, Zach 1206-1213.
- Emperors' letter blaming Flavian (Cut first 6): `uncertain`, Perry 23250-23252.
- Peter Mongus and the Henotikon, eastern monks, Severus's letters, Philoxenus, Armenia's anathema (line 103): `legacy.traces` and `sources.about`.
- Rain or snow image (line 104): `uncertain`.
- "The ignorant old man", seventy years and shipwreck (line 105): `legacy.remembered` and `uncertain`.
- Canon 95 of 692 (line 107): `legacy.traces` and `uncertain`.
- Nestorius on suborned accusers (line 74): `uncertain`, Bazaar 18910-18914.

**Skipped:** the outline's Leave out items not marked for the card (Chrysaphius as godson, his fate after 451, the second inquiry, Flavian's death, the Coptic legend); the existing card already carries Chrysaphius and the exile, now corrected under change 1. Review.md and Fresh_Read.md send nothing to the card.

**Validator** (scratch census, `--skip-quotes`): two errors for this entry, `secondReading` missing on quotationOriginals[0] and [1] (six words or more; release sets them).

## Third pass: what it was about (2026-11-23)

Starting card `eutyches.card.json` copied to `Card.pass2.json`; every other field word for word. Brief compared with `eutyches.brief.v3.txt`.

**briefReferences (new explanations)**
1. `[0]` (Perry minutes): added "The notary's deposition has him denying that Christ's flesh shared our nature." Evidence: brief, "his judges recorded that he denied it shared our nature"; Perry 23807-23809.
2. `[2]` (Eutyches to Leo): "and his claim that he appealed." → "his claim that he appealed, and his claim that the fathers before him had rejected the phrase two natures." Evidence: brief, "the fathers who, he said, had rejected the words "two natures""; Leo 4560.
3. `[3]` (Flavian to Leo, Letter 22): "the old evil dogmas of Valentinus and Apollinaris revived." → "his judges' account that Eutyches denied Christ's flesh was of the same substance as ours." Evidence: Leo 4744-4746. The old clause named the cut "old heresies" charge.
4. `[4]` (Tome): added "; one Christ in two natures, each keeping its own character." Evidence: brief; Leo 5301-5302, 5434-5435.
5. `[6]` (Perry, session of 449): added the sentence the record gave as Basil's (denying two natures after the union meant mixing God and man; Perry 23858-23859), the shout that all who affirm two natures be cursed (Perry 23931-23933), and Flavian deposed, the council ruling that he had altered the faith (Perry 24114-24118, 24146-24148). Evidence: brief paragraphs 7.

**briefReferences (cut events removed)**
6. `[1]`: "a rhetorician when he first exposed Nestorius, " removed (brief no longer says it); " Theodoret deposed at Ephesus;" removed (brief no longer names him).
7. `[3]`: the Valentinus and Apollinaris sentence replaced (see 3).
8. `[8]`: "Nestorius deposed; " removed (brief no longer says he was deposed).

**quotationOriginals**
9. Appended a fourth entry for the new quoted span "two natures": printed "rejected the phrase “two natures,”", Eutyches to Leo, Letter 21, tr. Feltoe, `cic/texts/npnf212_leo-great-gregory-great.xml` line 4560 (verified verbatim); `secondReading` "checked at card" (two words); no original held. The three existing entries are unchanged (the brief's three quotations are unchanged).

**Skipped**
- Outline items marked "to the card" (Leo's letter of June 1, 448; Severus; palace soldiers; the emperors' letter; Mongus and the Henotikon; rain or snow; "ignorant old man" and shipwreck; canon 95; Nestorius on suborned accusers): already on the card under `uncertain`, `legacy.traces` and `legacy.remembered`; nothing to add.
- Fresh read's "gray hairs" to "grey hairs": not applied. The rendering stays "gray hairs" and the printed field keeps Perry's "grey".
- Outline items 10 (Theodoret) and 5 (reviving old heresies) are left out of the brief; the card's existing claims about Chrysaphius and exile stay.

**Validator** (scratch census, brief set to the current text, `--skip-quotes`): no errors for this entry. The two missing `secondReading` values reported in the second pass were not reported this time.

## Card check applied (2026-11-23)

`Card_Check_About.md` (FIX, one change), applied word for word: `quotationOriginals[3].printed`, `rejected the phrase “two natures,”` → `two natures`.
