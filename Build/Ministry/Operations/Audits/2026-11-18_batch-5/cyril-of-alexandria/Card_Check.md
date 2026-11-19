# Card check: Cyril of Alexandria

Card checker, batch 5, 2026-11-18. I did not write this card. Read: `cyril-of-alexandria.brief.txt` (and `.brief.v1.txt`), `cyril-of-alexandria.card.json`, `Card_Edits.md`, `Card.existing.json`, `Outline.md`, `Source_Sheet.md`, `Revision.md`, and every cited line in its file.

**Verdict: FIX.** One quotation is not Cyril's words as the brief gives them (ruling 1). The bush quotation needs a scan reading before the card validates (ruling 2). Everything else passes.

## 1. Each edit is justified

- `uncertain[2]`, "Those letters are held in Latin in Mansi V." Stands. Mansi V file, line 97081 heads the letter of Epiphanius, "Archidiaconi & Syncelli Cyrilli", to Maximian; line 97312 has "mille quingentas". Line 81296 heads the letter of Acacius of Beroea. The old sentence was contradicted by a held source, so this is a fair "clearly wrong" edit, and only those words changed.
- `sources.about`, seven added items. Each is a file the brief draws on or an entry cites. Stands (see FIX 3 for one title).
- `briefReferences`, seventeen entries. Spot-checked against Socrates VII.7, 13, 14, 15; Nikiu 6481–6492; Mansi V 97081; Hefele 2280–2283, 6387–6390, 9933–9935; Zachariah 5740–5746; Synaxarium 55272–55278. They stand.
- `briefLength` correctly left out (`tools/validate-census.mjs`, `CARD_KEYS`).

## 2. Nothing else moved

By object comparison: the census card equals `Card.existing.json`. Every existing field of the new card is the same as it, word for word and in order, except `uncertain[2]` and the seven items added at the end of `sources.about`. The first four `about` items and all of `ownWords` are unchanged.

## 3. References

The brief lost nothing between v1 and the final text (the revision only added), so no reference names something the brief no longer tells. All seventeen remain. None has quotation marks.

## 4. Census rules

- Keys: all allowed; no `briefLength`.
- The brief has eight quoted spans; seven entries cover them ("one nature" twice, one entry). None covers a span the brief no longer quotes.
- `printed` wordings, by the census fold at their cited lines: Q1 (Pusey 1872, 4334–4336), the gold (Bazaar 15817), "one nature" (JD 33086–33087), "no commingling, no confusion" (Pusey 1881, 19847) and Severus (2106–2108) stand. The bush does not stand without a reading (ruling 2). Every cited file is in `sources`.
- No audit, review or ruling named. American spelling throughout.
- Every entry lacks `secondReading`, which the census check requires. Card_Edits marks all seven as awaiting a second reading, and `card.md` forbids inventing one. That is not a card fault, but the card will not validate until the batch's second readings are copied in.
- Q1 `original`: checked by eye against Pusey 1872, 954–957. The fold empties Greek, so the census check cannot test it. Line 956 scans `Λόγος"` where the card gives `Λόγος·`: the card has the raised dot the scan misread. That is a fair reading, and no listing is needed, since the check cannot see Greek punctuation. The second reader should see it.

## 5. Originals

Q1's Greek is held and carried. The Greek of the bush passage, of the letters to Succensus and the Syriac of Severus are not held. Nothing is missing.

## 6. Rulings

### Ruling 1: "one incarnate nature of God the Word" is not Cyril's wording in any held text

The brief says: Cyril held to "one incarnate nature of God the Word". The quotation marks give those exact words to Cyril. No held text prints them in his mouth.

- **The outline's citation does not carry it.** Outline (Words to explain; beat 6; Do not say) cites CIO 19833–19848 and E8. Source Sheet E8 gives three held wordings, and none is this one:
  - CIO 19832–19835 (Pusey's note quoting Cyril's second letter to Succensus): "One Incarnate Nature of the Word". This is Cyril.
  - HEF 7748 (Hefele's English of the letter to Eulogius): "one incarnate nature of God". Cyril, in the historian's English.
  - JD 33083–33095 (John of Damascus quoting the letter to Succensus): "the one nature of the Word".
- **The card's entry is worse than the writer says.** It cites JD 32751–32752: "And we confess also that there is one incarnate nature of God the Word". That is John of Damascus's own confession, in the first person. The words "according to the blessed Cyril" (32756) belong to the next clause, his gloss on "incarnate", and the endnote points the phrase itself to a creed "a Patribus Nicaenis". So the `work` field ("giving the phrase according to the blessed Cyril") misstates its source.
- **The nearest attributions are later and worded differently.** JD 33084–33085 says Cyril interpreted "one nature of God the Word Incarnate". Hefele vol. 5, line 1537, quotes a later council's "one incarnate nature of God the Logos, as S. Cyril taught". Neither is held for Cyril himself, and neither has the brief's word order.

**Ruling: the attribution does not hold.** The brief must quote Cyril's held wording, which the outline already cites: Pusey's "One Incarnate Nature of the Word". It is the same letter and the same note that supplies "no commingling, no confusion" in the same sentence. The brief has already told the listener that "the Word" is God's own Son, so nothing is lost.

**Brief replacement** (paragraph 7, last sentence; for the brief's owner to make, not made here):

- Old: `Cyril held to "one incarnate nature of God the Word": the Word himself become a human being, body and soul, with "no commingling, no confusion".`
- New: `Cyril held to "one incarnate nature of the Word": the Word himself become a human being, body and soul, with "no commingling, no confusion".`

**Outline, Do not say** (replace line 126 in full):

- Old: `- WRONG "Cyril taught that Christ has only one nature, divine", "Christ's humanity was absorbed", "Cyril was a Monophysite". RIGHT "one incarnate nature of God the Word": one Christ, the Word with a full human body and soul of his own, "no commingling, no confusion" (E8).`
- New: `- WRONG "Cyril taught that Christ has only one nature, divine", "Christ's humanity was absorbed", "Cyril was a Monophysite"; also WRONG quoting "one incarnate nature of God the Word" as Cyril's words (no held text prints it in his mouth: it is John of Damascus's own confession, JD 32751–32752; Hefele's English of the letter to Eulogius has "one incarnate nature of God", HEF 7748). RIGHT "one incarnate nature of the Word" (CIO 19834–19835, Pusey's note quoting the second letter to Succensus): one Christ, the Word with a full human body and soul of his own, "no commingling, no confusion" (E8).`

The same wording "of God the Word" stands elsewhere in the outline: the essence (line 5), Words to explain (line 23), beat 6 (line 56), What came 1 (line 61), the witness-phrase list (line 68) and the Connection (line 87). They should follow the Do not say line when the outline is next touched. That is the outline owner's call, not this card's.

**Card changes once the brief carries the new wording:**

FIX 1. `quotationOriginals[4]`, replace the whole entry.

Old:
```json
{
  "modern": "one incarnate nature of God the Word",
  "printed": "one incarnate nature of God the Word",
  "work": "John of Damascus, Exposition of the Orthodox Faith III.7, giving the phrase according to the blessed Cyril",
  "file": "cic/texts/npnf209_hilary-poitiers-john-damascus.xml",
  "lines": "32751-32752",
  "uncertain": "John of Damascus gives the phrase as Cyril's. Pusey prints Cyril's letter to Succensus with One Incarnate Nature of the Word, and Hefele prints the letter to Eulogius with one incarnate nature of God; the Greek of the letters to Succensus is not held."
}
```
New:
```json
{
  "modern": "one incarnate nature of the Word",
  "printed": "One Incarnate Nature of the Word",
  "work": "Cyril, second letter to Succensus, as Pusey quotes it in a note to That Christ is One",
  "file": "cic/texts/cyril-alexandria_five-tomes-against-nestorius-scholia-christ-is-one_pusey1881.txt",
  "lines": "19834-19835",
  "uncertain": "The Greek of the letter is not held. John of Damascus has Cyril interpret one nature of God the Word Incarnate, and Hefele's English of the letter to Eulogius has one incarnate nature of God."
}
```
Checked by the census fold: the printed wording stands at 19834–19835. A new span needs its own second reading.

FIX 2. If Mark keeps the brief as it is, the old entry still cannot stand: its `work` names a source that does not attribute those words to Cyril. There is then no held wording to cite. So FIX 1 depends on the brief change, and the brief change is required.

FIX 3. `sources.about[10].title` (John of Damascus). After FIX 1, the card cites chapter 11 only.

- Old: `"An Exposition of the Orthodox Faith, Book 3, chapters 7 and 11"`
- New: `"An Exposition of the Orthodox Faith, Book 3, chapter 11"`

`briefReferences[10]` already names only Exposition III.11 and stays as it is.

### Ruling 2: the scan reading for the bush

Card_Edits gives the line numbers one off. In the Pusey 1881 file, line 19879 ends `kept  play-`, line 19880 is blank, and line 19881 begins `4  ivriarp-  ing  "^  ou  the  shrub`. The fault is all on 19881: a margin note (`4  ivriarp-`), a note mark (`"^`) and "ou" for "on". The line-end hyphen at 19879 is already joined by the census check across the blank line, so only 19881 needs listing.

Add to `readings` in `tools/quote_scan_readings.json` (exact; two spaces between scan words, as the file has them):

```json
{
 "file": "cic/texts/cyril-alexandria_five-tomes-against-nestorius-scholia-christ-is-one_pusey1881.txt",
 "lines": "19881",
 "scan": "4  ivriarp-  ing  \"^  ou  the",
 "reads": "ing on the",
 "kind": "margin note and note mark run into the line, with an OCR misread"
}
```

Tested against the census check's own matching rules (fold and line-end join), run inline: with this entry, the card's bush `printed` stands at lines 19878–19881; without it, it does not. The card's `lines` stay "19878-19881".

**No other entries are needed.** Every other `printed` wording stands without one. The replacement wording in FIX 1 has no scan fault in its span ("trutli" at 19834 lies before it). The Greek dot at Pusey 1872, line 956, is beyond what the check can see (section 4).

## Not found

The writer reported none. I agree, and I found nothing else clearly wrong left in the card.

## Applied (coordinator, 2026-11-18)
Brief sentence, outline Do not say line 126, FIX 1 and FIX 3 applied word for word as the checker worded them. The six other outline uses of "of God the Word" are left for the outline's next touch, as the check says. The scan entry is added at release.

## Applied (card fixer)
- FIX 1 and FIX 3 were applied earlier by the coordinator; nothing further applied to the card.
- The scan reading of ruling 2 is copied to `Scan_Readings.json`.
