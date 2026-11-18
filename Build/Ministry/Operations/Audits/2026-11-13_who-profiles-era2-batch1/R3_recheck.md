# R3 recheck: nine Who profiles, era 2 batch 1

Scope: round 3, the last allowed. A targeted recheck of the round 2 changes only (`git diff ee109116~1 ee109116`), against `R2_recheck.md` and `R2_changes.md`. Unchanged text was not re-reviewed. Each changed line was searched in its vendored file (whitespace-tolerant, tags stripped, quote marks straightened) and read in context. No drafts were edited and no model or paid calls were made.

## 1. The R2 blocking finding

| Finding | Status | Check against source |
|---|---|---|
| NB1 Frumentius, card and records.json: Jackson's own Theophilus sentence given to the Dictionary of Christian Biography | RESOLVED | Card: "Blomfield Jackson, in a note to Theodoret, says the emperor Constantius later asked the prince of Axum to replace Frumentius with an Arian, Theophilus, without success. The chapter of Athanasius he cites does not name Theophilus." In the note (Theodoret I.23, npnf203 l.7764–7773) the Dictionary quotation closes with "(Dict. of Christ. Biog., Art. Ethiopian Church)". Jackson then writes in his own voice: "Constantius afterwards wrote to the Ethiopian Prince to ask him to replace Frumentius by Theophilus, an Arian, but without success (Ath. Ap. ad Const. 31)" (l.7771–7773). The sentence is now given to Jackson. Apology to Constantius 31 (npnf204, section "Letter of Constantius to the Ethiopians against Frumentius", from l.36103) has no "Theophilus": the word does not occur anywhere near it. The letter asks the princes to send "the Bishop Frumentius" into Egypt (l.36145) and fears someone will "pass over into Auxumis" (l.36166). It does not name a replacement. So "does not name Theophilus" is true, and the card no longer lends Jackson's detail the authority of the source he cites. records.json `frumentius/claims[5]/witness` now reads "Blomfield Jackson, in his own words in a note to Theodoret I.23, after quoting the Dictionary of Christian Biography; he cites Athanasius, Apology to Constantius 31, which does not name Theophilus." Accurate. The separate Abba Salama witness (records.json, "the Dictionary of Christian Biography, quoted in Jackson's note") is correct as it stands: that phrase is inside Jackson's quotation marks (l.7767–7768). |

**Resolved.**

## 2. Changed sentences (R2 minors N1–N7)

**Arius**
- N1, brief: "Sozomen, the church historian, gives three views. Arius's friends blamed magic. Others saw God's judgment. Some blamed a sudden heart disease." Sozomen II.29: "Some believed that he died at that very hour, seized by a sudden disease of the heart, or suffering weakness from his joy ...; others imagined that this mode of death was inflicted on him in judgment ... Those who held his sentiments were of opinion that his death was brought about by magical arts" (npnf202 l.30400–30406). Robertson's "most people" and "Alexander's side" are gone, and the held witness now speaks for itself. "Friends" fairly renders "those who held his sentiments". Dropping Sozomen's second option ("weakness from his joy") shortens without misstating. Card: "Those who held Arius's views blamed magic. Others saw God's judgment, and some a sudden disease of the heart." Exact in substance. records.json contested_claim: "Sozomen II.29-30" is the right reference (chapter XXIX from l.30357, XXX follows). Its "(Athanasius's view)" against the judgment group matches the narrative Sozomen quotes next, where "judgment was visited upon him". Not participant-facing. Resolved.
- N2, card dates: "In dispute with Bishop Alexander of Alexandria from about 318 or 319; died in Constantinople in 336, both by Archibald Robertson's dating." Robertson: the controversy "certainly must be placed as early as 318 or 319" (npnf204 l.1673–1674). The unsupported "taught from about 318" is gone and the dating is attributed. Resolved.
- N3: "who calls Philostorgius a liar." The pronoun no longer points at Arius. Resolved.
- N7: "Theodoret of Cyrrhus" in the brief, card (three places) and records.json. No "Theodoret of Cyrus" remains in the batch. This matches Frumentius, Lucifer and the site. npnf203 itself gives "Cyrus or Cyrrhus" (l.2576). Resolved.
- Readability edits: "books by his foes", "foes" for "enemies" twice, "as the presbyter Macarius told him", "Socrates says." No claim changes. "Socrates says" for "Socrates records" keeps the attribution.

**Pachomius**
- N4, card: "if not verbatim from his pen, are yet authentic enough for all practical purposes." Exact (Schodde l.162). The qualifier is back. Resolved.

**Hilarion of Gaza**
- N5, card: the theory that it was "a sort of religious romance" is one that "seems destitute of foundation." Both quotations exact (npnf206 l.30093). The hedge "seems" is kept. Resolved.

**Aetius of Antioch**
- N6, brief: "Sozomen the church historian says" and "Photius, a later patriarch of Constantinople." Both are true descriptions and match the context used elsewhere in the batch. Resolved. See m1 for punctuation.
- "Soon" is removed from "Leontius had to stop him." Removing a word adds no claim.

No new witness swap, dropped hedge, role for a named witness, or settled-sounding contested claim came in with these changes. The only new verbatim quotations are the Schodde and Fremantle lines above, both exact.

## 3. Mechanical checks

| Profile | Words | Cap | FK | Flesch | Audio matches brief, tags removed |
|---|---|---|---|---|---|
| Arius (major) | 403 | 405, within | 7.8 | 60.7 | yes |
| Aetius of Antioch | 323 | 324, within | 8.0 | 61.3 | yes |
| Frumentius (card only changed) | 401 | 405 | 7.9 | 60.4 | yes |
| Pachomius (card only changed) | 401 | 405 | 8.4 | 62.3 | yes |
| Hilarion of Gaza (card only changed) | 323 | 324 | 6.7 | 70.0 | yes |

`grade_text` passes for Arius and Aetius (FK ≤ 10, Flesch ≥ 60), and for the other seven, whose briefs did not change. All nine audio scripts equal their briefs once `[calmly]` and `[warmly]` are removed. `records.json` and all nine cards parse. `briefLength` is "about 2 minutes 30 seconds" for Arius (403 words, 2:29) and "about 2 minutes" for Aetius (323 words, 1:59), at 162 words a minute. No changed narrator sentence in a brief runs past 25 words.

## 4. New findings

### Blocking

None.

### Minor

- **m1 (Aetius, brief, optional).** "Aetius spoke so boldly about God, Sozomen the church historian says, that ..." reads better on the page with commas: "Sozomen, the church historian, says". The Arius brief already uses that form. The spoken audio is not affected, and nothing is wrong in substance.

### N8 decline (card sentences over 25 words)

The decline holds. Era 1 batch 2 set the same point aside on the same reason: card text is read by eye, it is not scored by `grade_text`, and the long sentences tie a claim to its named witness (`2026-11-12_who-profiles-era1-batch2/R2_changes.md`, "Not changed"; accepted in that batch's `R3_recheck.md`). The new Frumentius card sentence (26 words) is of the same kind. No long sentence is in a brief.

## Summary

The one R2 blocking finding (NB1, Frumentius) is resolved, and checked against Jackson's note and Athanasius's Apology to Constantius 31. Minors N1–N7 are resolved, each true to its vendored source. No new blocking finding came in. One optional punctuation point remains (m1). The N8 decline holds against the era 1 batch 2 precedent. The batch clears review at round 3.
