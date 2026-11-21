# Card check: Timothy I of Baghdad

**Verdict: FIX** (three references, and two scan readings the card needs before it can pass).

Base: the census card for `timothy-i-of-baghdad`. It is identical to `Card.existing.json` (object comparison). Diffed field by field: only `briefReferences` and `quotationOriginals` are new, as `Card_Edits.md` lists.

## 1. Edits justified

Every listed edit checks against its evidence. Re-read:
- MARI 12983-12990, 13014-13016, 13024-13028, 13079-13086, 13091-13098.
- EL 3716-3722. AS1 29750-29751. AMR 12935-12940, 13026-13027.
- AS2 42357-42364, 52755-52760.
- SO 40359-40361, 40543-40546.
- TM 20155-20161, 20186, 21848-21852, 21888-21892, 21955-21960, 21978-21986, 21998-22005.
- MIN 1684-1691, 1703-1704, 1719-1722. BH 9812-9821.

## 2. Nothing else moved

Confirmed. Every other field is word for word and in order.

## 3. References

Rule applied: remove what the brief does not tell, but keep a date that grounds one of the brief's dates. Kept on that ground:
- Elias's 7 May 780, which grounds "May 780".
- The year al-Ma'mun entered Baghdad, which grounds "the early 820s, under the fifth caliph".
- Chabot's 790, which grounds "About 790".

FIX 1. `briefReferences[1]`. The brief does not tell the eight months, or the fifteen bishops on Timothy's side.
- Old: `Mari ibn Sulayman, in Henricus Gismondi's Latin: Timothy's trick with sacks of stones shown to the electors as money, his consecration eight months later, and his answer to those who asked for the money. The same account has the metropolitans' opposition, Ephrem and thirteen bishops pronouncing him cursed, Timothy and fifteen bishops cutting them off, the killings and imprisonments among the Christians, and the metropolitan of Merv, whom Timothy deposed, accusing him before al-Mahdi without success.`
- New: `Mari ibn Sulayman, in Henricus Gismondi's Latin: Timothy's trick with sacks of stones shown to the electors as money, his consecration, and his answer to those who asked for the money. The same account has the metropolitans' opposition, Ephrem and thirteen bishops pronouncing him cursed, Timothy cutting them off, the killings and imprisonments among the Christians, and the metropolitan of Merv, whom Timothy deposed, accusing him before al-Mahdi without success.`

FIX 2. `briefReferences[5]`. The brief says only that no one could promise gifts. It gives no date but "About 790".
- Old: `... the rule against asking for or promising gifts; and why he had not visited, the rebuilding of destroyed churches and six audiences with the king. Chabot dates the synod to 790, on 'Abdisho's Arab year 174, and the editors of Bar Hebraeus give 786 and 804.`
- New: `... the rule against promising gifts; and why he had not visited, the rebuilding of destroyed churches and six audiences with the king. Chabot dates the synod to 790, on 'Abdisho's Arab year 174.`
- (The entry's opening, up to "the rule against", is unchanged.)

FIX 3. `briefReferences[6]`. The brief says "Two brothers from one monastery". It does not say the monastery was Thomas's own.
- Old: `Kardagh and Yahballaha, two monks sent for from Thomas's own monastery, anointed metropolitans of Gilan and Dailom;`
- New: `Kardagh and Yahballaha, two brothers sent for from one monastery, anointed metropolitans of Gilan and Dailom;`

All other references name what the brief tells.

## 4. Census rules

FIX, for two scan faults.
- Only allowed keys, and no `briefLength`.
- There are three quoted spans in the brief and three entries, with none left over.
- Every cited file is in `sources`.
- There are no quotation marks in the references.
- No audit, review or ruling is named.
- The new fields use American spelling.

Q1 (MARI 13084-13085) stands as is. Q2 and Q3 keep the page's words, which is right, but the scan breaks each span. The census check will fail on both until `tools/quote_scan_readings.json` has these two readings. With them applied, both wordings stand at their lines (checked under the census fold).

```json
{
 "file": "cic/texts/synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt",
 "lines": "40545",
 "scan": "avons 1 néanmoins",
 "reads": "avons dû néanmoins",
 "kind": "OCR misread"
}
```

```json
{
 "file": "cic/texts/thomas-of-marga_book-of-governors-v2-english_budge1893.txt",
 "lines": "21980",
 "scan": "w^homsoever",
 "reads": "whomsoever",
 "kind": "OCR misread"
}
```

Three entries have no `secondReading` yet. That is expected: second readings come at step 7.

## 5. Originals

Pass.
- Q1 is Gismondi's Latin; Mari's Arabic is not usable in the scan.
- Q2 is Chabot's French. The Syriac is in the same file, but the outline does not render from it.
- Q3 is Budge's English, and no Syriac of Thomas is held.

## 6. Not found, and left in

The edit list names no claim as not found. One existing claim the card writer did not re-read stands: Chabot's index gives "Timothée I (7 mai 780-9 janv. 825)" (SO 49679), while his note gives 823 (SO 40361). Nothing clearly wrong is on the card.

## Applied (card fixer)

FIX 1 applied (briefReferences[1]).
FIX 2 applied (briefReferences[5]). The old text was given with a leading "..."; the replacement was applied to the exact text after it, which is unique in the entry.
FIX 3 applied (briefReferences[6]).
Scan readings (2) copied to Scan_Readings.json; not added to tools/quote_scan_readings.json.
Not applied: none.
