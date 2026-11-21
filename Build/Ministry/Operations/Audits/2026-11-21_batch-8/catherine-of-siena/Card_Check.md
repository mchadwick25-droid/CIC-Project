# Card check: Catherine of Siena

Batch 8, 2026-11-21. Independent checker; I wrote neither the brief nor the card. New card (no census entry, no starting card), so every field was checked against its evidence in `Card_Edits.md`. Files are under `cic/texts/` unless noted.

**Verdict: FIX** (5 changes and 2 scan readings, below; FIX 5 needs the coordinator).

## 1. Each field justified

Spot-read against the files: Scudder's chronology (LET-ed 1258-1261, 1228-1229, 1370-1374, 1392-1395), Raymond's death date and Genoa (AASS 211676-211679), Barduccio's sixth hour (AASS 214957), Covel's thirty-three and Pius II (COVEL 51460-51461), the Mansi notice's Ides of January 1376 (MANSI 53392-53393), the Guidini memoir (LIB 14403-14407). All hold as the card states them. The datesNote and placeNote end without a full stop, as on the other cards of this batch.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

Checked each entry against the brief and against `catherine-of-siena.brief.v1.txt`. Three name what the brief no longer tells (FIX 1 to 3). The revision cut "She knows no Latin and he no Italian". The brief never says "without monastic vows" and never names Robert of Geneva. The other ten stand, and none has quotation marks.

## 4. Census rules

- Keys: all allowed. No `briefLength`, no `label`.
- Six quoted spans in the brief, six entries, each `modern` exactly the brief's. Entries of six words or more carry no `secondReading`, as the new-card prompt says. "incarnate demons." and "with her leading him." carry "checked at card".
- Prints at their lines: [1] LET 5039, [2] LET 5221-5222, [4] LET 7063-7064, [5] LIB 14405-14407 stand verbatim. [0] stands at MIRBT 13887-13891 only with the two readings below.
- Every cited file is in `sources`. No audit, review or ruling is named.
- Spelling: "fulfil" in `uncertain[0]` is card prose, not printed wording (FIX 4). "honour" is the brief's own word, inside `modern`.

## 5. Originals

- **[0] Raymond, section 152 (MIRBT 13887-13891): KEEP, with two readings.** This rests on the batch 6 originals ruling.
  - "onmipotentis" reads omnipotentis. A held print confirms it: the Acta Sanctorum prints "omnipotentis" cleanly (AASS 200986).
  - The "30" at the head of 13890 is a margin line number, a stray mark. Without the reading, the validator joins "commit-" to "30 tuntur".
  - Mirbt's "quae" and the AASS "qui" are both recorded in `uncertain`, as Mark's guidance asks.
  - The rendering matches the Latin clause by clause. "In Romana curia" is given as "in the papal court".
- **[1], [2], [4]: Scudder's English.** No original is held. Correct as entered. Checked at card for [1]: Scudder prints "rulers whom you know yourself to be incarnate demons" (LET 5038-5039), and the rendering is exact.
- **[5] Guidini (LIB 14405-14407): clean Italian; the rendering holds.**
- **[3] "with her leading him." (FIX 5).** The `printed` wording is Scudder's chronology: "Gregory, swayed by her representations, returns to Italy" (LET-ed 1228-1229). It is not the print of the span. It is an editor's summary that renders nothing in the brief's words. Using it as the span's printed wording misstates where the words come from.
  - The only print of the words is Raymond's "ipsa eum indiicente" (AASS 214145), in a damaged scan.
  - Under the batch 6 ruling, "indiicente" cannot be read as inducente without a held print. None exists: section 422 is held nowhere else, and no English of the Life is held. So the Latin is left out.
  - That leaves the span with no printed wording at all.

## 6. "Not found" claims and anything left wrong

- **"Catharina Senensis", the 1377 Barberini copy, the Florence copy and Bernardino: left out. Correct.** No held line supports them.
- **The two Scudder lines on her leaving Avignon (LET-ed 1345, 7168-7169):** both are on the card, credited. Nothing is wrong.
- Nothing else found wrong.

## Fixes

**FIX 1.** `briefReferences[0]`
- Old: `Raymond of Capua, Life, section 152, in Mirbt: the audience before Gregory XI at Avignon, Raymond interpreting because she knew no Latin and the pope no Italian; the pope's question how she knew the court after a few days; her answer about the stench of the sins committed in the papal court; the pope's silence.`
- New: `Raymond of Capua, Life, section 152, in Mirbt: the audience before Gregory XI at Avignon, Raymond interpreting; the pope's question how she knew the court after a few days; her answer about the stench of the sins committed in the papal court; the pope's silence.`

**FIX 2.** `briefReferences[1]`
- Old: `Raymond, Life, and Scudder's headnote: her father the dyer; her asking the Sisters of Penance of St. Dominic for their habit, and Scudder on how they lived in their own homes without monastic vows.`
- New: `Raymond, Life, and Scudder's headnote: her father the dyer; her asking the Sisters of Penance of St. Dominic for their habit, and Scudder on how they lived in their own homes.`

**FIX 3.** `briefReferences[10]`
- Old: `Scudder's chronology and Raymond: the cardinals declare Urban VI's election invalid on 20 September 1378 and choose Robert of Geneva; Urban summons her to Rome and she writes letters on his behalf.`
- New: `Scudder's chronology and Raymond: the cardinals declare Urban VI's election invalid on 20 September 1378 and choose a rival; Urban summons her to Rome and she writes letters on his behalf.`

**FIX 4.** `uncertain[0]`, one word
- Old: `in 1375 she urges him to fulfil what he had begun`
- New: `in 1375 she urges him to fulfill what he had begun`

**FIX 5.** `quotationOriginals[3]`. This is the coordinator's call, because the remedy touches the brief.
- **Recommended:** take the quotation marks off the brief's span. Old: `says the pope decided to return "with her leading him."` New: `says the pope decided to return with her leading him.` Then remove the entry `quotationOriginals[3]` entirely (the object whose `modern` is `with her leading him.`). Raymond is still credited in the brief's sentence, and `uncertain[0]` keeps "she leading him" as his claim.
- **Alternative, only if the coordinator overrules the batch 6 rule here** (as the Pliny "O" was allowed):
  - Replace the entry's `printed` with `ipsa eum inducente`.
  - Replace `work` with `Raymond of Capua, Life of Catherine, section 422, in Latin, in the Acta Sanctorum, April, volume 3`.
  - Replace `file` with `cic/texts/acta-sanctorum_aprilis-tomus-3-lat_palme1866.txt`, and `lines` with `214145`.
  - Replace `uncertain` with `The scan prints indiicente; no second print of the sentence is held.`
  - Add the reading `{"file": "cic/texts/acta-sanctorum_aprilis-tomus-3-lat_palme1866.txt", "lines": "214145", "scan": "indiicente", "reads": "inducente", "kind": "OCR misread"}`.
  - The same scan prints ii for u nearby ("Qiiomodo", AASS 200981), but that is not a held print. Keeping Scudder's line is not an option.

## Scan readings to add (for entry [0])

```json
{"file": "cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt", "lines": "13887", "scan": "onmipotentis", "reads": "omnipotentis", "kind": "OCR misread"},
{"file": "cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt", "lines": "13890", "scan": "30  tuntur", "reads": "tuntur", "kind": "margin line number run into the line"}
```
