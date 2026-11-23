# Card check: Ephrem the Syrian

Checked `ephrem-the-syrian.card.json` against `Card.existing.json`, the final brief, `Card_Edits.md`, `Revision.md`, `Fresh_Read.md` and `Fresh_Read_Applied.md`. No census entry is written; none is needed. The existing card equals the census `card` field.

**Verdict: PASS.**

## 1. Edits justified

- **Palladius briefReferences entry.** The old quoted words "See, on your behalf I appoint myself hospitaller." do not stand in the brief. The new quoted words "Look, on your behalf I appoint myself to run the shelter." stand verbatim in paragraph 1. The printed wording is kept in `quotationOriginals`. Justified.
- **New Jerome 115 entry.** `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` lines 41540-41542 read "deacon of the church at Edessa, composed many works in the Syriac language". The entry paraphrases this without quotation marks. It supports the brief's "a deacon of its Syriac church". Justified.

## 2. Nothing else moved

A JSON diff of the two cards shows only those two changes. Everything else is word for word.

## 3. briefReferences against the brief

Every entry names something the brief still tells: the famine and its date, Nisibis origin, the Palladius exchange, the year and the month, the prose against the three, the resurrection line, Harmonius and Ephrem's fear (now "In Sozomen's account"), the homily blaming Bardaisan, Greek and Basil, Jerome's reading aloud, Theodoret's martyrs' festivals, Barhadbeshabba's schools, and the census tradition. Theodoret II.26 (Nisibis on the border) stays as the nearest held support for the brief's border clause, which is unchanged from the approved brief. Nothing to remove.

## 4. Census rules

- Keys: only allowed keys; no `briefLength`.
- `quotationOriginals`: the brief has one quoted span (`tools/list_second_readings.py`: 1 span, CARRIED). One entry, `modern` identical to the brief.
- `printed` is verbatim at `cic/texts/palladius_lausiac-history_clarke1918.txt` line 471 (re-read). The file is in `sources.about`.
- `secondReading` "changes meaning" is carried from the existing card, set by an earlier release. The validator requires a verdict for a quotation of six or more words. The fresh read's MINOR 2 sends this to the second-reading step; that is not a card fault.
- No audit file, review or ruling named. American spelling.
- No outline or held original in another language for this quote, so no `original` field is owed.

## 5. "checked at card"

No quotation under six words. Nothing to check.

## 6. Not found and clearly wrong

- The brief's "Edessa ... on Rome's border with Persia": held lines put Nisibis on the border (Theodoret II.26, npnf203 11065-11067), not Edessa. This is correctly listed as not found. The clause is broadly fair for Roman Edessa near the Persian frontier, and it is not contradicted by a held source, so it is not clearly wrong.
- I found nothing clearly wrong left in the card.

## 7. Census entry

None written; not applicable.
