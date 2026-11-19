# Card check: Barsauma of Nisibis

**Verdict: FIX** (five references; two scan readings needed before the card validates).

Base: `Card.existing.json` (the census card). Diffed field by field: only `knownFor`, `legacy`, `uncertain`, `sources`, `briefReferences` and `quotationOriginals` differ, as `Card_Edits.md` lists.

## 1. Edits justified

Every listed edit checks against its evidence.
- Babai to Babowai, five places: Mark's ruling; the brief uses Babowai throughout. Each change touches only the name.
- The 'Amr claim stands: AMR 14051-14052, "quin aperiret, eam ad Pherozem transmisit" (the scan reads "eain ad Pherozom").
- New `sources.about` entry, Babken's letter: TM 36823-36842 has the Armenians refusing the canons "welche Akak und Barsauma und Mani und Paule ... aufgestellt haben". It grounds the brief's "About 506" sentence.
- Every quotation line was re-read; see 4.

## 2. Nothing else moved

Confirmed. `otherNames`, `datesNote`, `placeNote`, `role` and `keyWorks` are word for word. Inside the changed fields, only the listed words differ.

## 3. References

Rule: remove what the brief does not tell. Keep a date that grounds one of the brief's dates.

FIX 1. `briefReferences[1]`. The brief does not tell the five bishops.
- Old: `Synodicon orientale, Appendix I, Barsauma's six letters: the first, with five bishops, annuls the volume made at Beth Lapat, with its \"murmurs, blames, charges and testimonies\"; the third says \"Satan stirred up a quarrel\" between him and the catholicos Babowai.`
- New: `Synodicon orientale, Appendix I, Barsauma's six letters: the first annuls the volume made at Beth Lapat, with its \"murmurs, blames, charges and testimonies\"; the third says \"Satan stirred up a quarrel\" between him and the catholicos Babowai.`

FIX 2. `briefReferences[2]`. The brief gives drought and horsemen, but not "two years" or "four hundred".
- Old: `Synodicon orientale, Barsauma's second letter: two years of drought, raiding tribes, the Roman general brought to Nisibis to the Persian governor, the raid by four hundred horsemen and the Romans' anger.`
- New: `Synodicon orientale, Barsauma's second letter: drought, raiding tribes, the Roman general brought to Nisibis to the Persian governor, the raid by horsemen and the Romans' anger.`

FIX 3. `briefReferences[4]`. The brief tells two of the marriage rulings (bishops may not stop clergy marrying; new assistant ministers to be married), not three.
- Old: `Synodicon orientale, the synod of 486 under Acacius: the confession of Christ fully God and fully human, the order on the wandering men in black, and the three rulings on clergy marriage. Chabot's note: Barsauma and the bishops of his province were not at the synod.`
- New: `Synodicon orientale, the synod of 486 under Acacius: the confession of Christ fully God and fully human, the order on the wandering men in black, and its rulings on clergy marriage. Chabot's note: Barsauma and the bishops of his province were not at the synod.`

FIX 4. `briefReferences[5]`. The brief does not name Beth Edrai. ("the excommunications of 491" stays: it grounds the brief's "by 491".)
- Old: `Synodicon orientale, the compiler's account of the reconciliation at Beth Edrai in 485, and the synod of 497, which annuls the excommunications of 491 and accepts Beth Lapat \"but only on this point\" while letting every cleric, from the head of the church down, marry one wife.`
- New: `Synodicon orientale, the compiler's account of the reconciliation in 485, and the synod of 497, which annuls the excommunications of 491 and accepts Beth Lapat \"but only on this point\" while letting every cleric, from the head of the church down, marry one wife.`

FIX 5. `briefReferences[7]`. The brief does not tell the briefing of the king, the nun's name, or Acacius as fellow student.
- Old: `Mari ibn Sulayman, On the patriarchs of the East, tr. Gismondi: the catholicos chooses Barsauma to brief the king; Babowai's letter passed to the king and Barsauma's regret; his marriage to the nun Mammaea at the king's order; Acacius, his fellow student at Edessa.`
- New: `Mari ibn Sulayman, On the patriarchs of the East, tr. Gismondi: Babowai's letter passed to the king and Barsauma's regret; his marriage to a nun at the king's order.`

These stay as they are:
- [0] The compiler's note.
- [3] The third letter, and the fourth accepting the synod in advance.
- [6] The synod of 605.
- [8] Bar Hebraeus.
- [9] Michael and Maruta. Chabot's note grounds "built on old men's memories".
- [10] Narsai and the school.
- [11] Babken.
- [12] The census, for 424.

## 4. Census rules

Pass, except for the two scan readings below.
- Only allowed keys, and no `briefLength`.
- There are ten quoted spans in the brief and ten entries, none left over.
- Every cited file is in `sources`.
- The quotation marks in the references are verbatim in the brief.
- No audit, review or ruling is named. The spelling is American.

Eight `printed` wordings stand at their lines as given (SO 20258, 35256-35257, 35479-35483, 35509-35510, 20484, 31682, 31684; BH 3758-3762). Two hit scan faults, and both readings are confirmed. Each needs an entry in `tools/quote_scan_readings.json`:

```json
{
  "file": "cic/texts/synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt",
  "lines": "35397",
  "scan": "Satan 4 suscité",
  "reads": "Satan a suscité",
  "kind": "OCR misread"
}
```

```json
{
  "file": "cic/texts/synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt",
  "lines": "31685",
  "scan": "Bar CGauma",
  "reads": "Bar Çauma",
  "kind": "OCR misread"
}
```

The file prints the name "Bar Çauma" elsewhere (20257, 40936). `tools/quote_scan_readings.json` has no reading for this file yet.

No `secondReading` has been given yet. That is expected: the census card had no `quotationOriginals`, and step 7 fills them in.

## 5. Originals

Pass. The brief renders from Chabot's French and Abbeloos and Lamy's Latin. Those printed wordings are carried. No Syriac original is held.

## 6. Not found, and left in

- **"my lord" for Mar**: upheld. I found no held text that glosses Mar this way (searched Connolly, Badger, Labourt and the Synodicon). The gloss is only in the outline. The entry says so honestly. Note for Mark, not a card fix: the brief puts the gloss in quotation marks, as if it were quoted.
- The spot-checked claims hold. Nothing clearly wrong was left in.

## Applied (card fixer)

FIX 1 applied (briefReferences[1]).
FIX 2 applied (briefReferences[2]).
FIX 3 applied (briefReferences[4]).
FIX 4 applied (briefReferences[5]).
FIX 5 applied (briefReferences[7]).
Scan readings (2) copied to Scan_Readings.json; not added to tools/quote_scan_readings.json.
Not applied: none.
