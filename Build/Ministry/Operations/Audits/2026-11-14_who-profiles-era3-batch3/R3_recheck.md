# R3 recheck: era 3 batch 3

Scope: round 3, the last allowed. This recheck covers only the round 2 changes, read as `git diff --word-diff 61dd8f97 14a7c37b`. It checks them against `R2_recheck.md` (N1 to N5 and C-M15) and `R2_changes.md`. Under `era3/batch3/`, five files changed:
- the Marcellinus Comes card
- the Procopius of Caesarea card
- the Romanos the Melodist card
- the Vigilius of Rome card
- `records.json`

The batch's Open-Gaps entry (`Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`, entry "Era 3 Who batch 3", 2026-11-14) was also added, and was read only for C-M15. No brief or audio script changed. Text that did not change was not reviewed again. I opened each changed sentence at its line in the vendored file, to confirm who is speaking there. I edited no drafts, and I made no paid calls, model calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given.

## 1. The R2 findings

| Finding | Status | Check against source |
|---|---|---|
| N1 Marcellinus card `legacy.traces` 1: "two lost early copies" | RESOLVED | Now "two early copies of nearly the author's own time, Mommsen says." Mommsen: "quibus repraesentari archetypa duo auctori fere aequaeva… Tilianus… narrationem continuans ad a. 548, ubi desinit mutilus, ipse scriptus est saeculo eo quo auctor vixit" (`chronica-minora-2_…_mommsen1894.txt` l.3717–3721). "Lost" is gone; "nearly the author's own time" renders "auctori fere aequaeva". |
| N2 Romanos card `uncertain` 1 and records: the Bollandists and others said to name Vatican 1613 | RESOLVED | The card gives the number to PG 99 alone: "Ex Menologio Basilii imperatoris. Cod. Vatic. n. 1613." (`theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt` l.7839). The Bollandists' "Menologio Graecorum, jussu. Basilii Porphyrogeniti Imperatoris seculo Christi decimo conscripto" (`acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` l.180301–180302) supports "a Menologion made by order of the emperor Basil Porphyrogenitus"; the file's five "1613" hits are all years, none a manuscript. Records: the PG 99 claim now stands alone (Contested); the new claim's witnesses match Assemani "in Menologio Græcorum, quod Basilii Porphyrogeniti Imperatoris jussu prodiit" (OCR, l.39715–39716) and Studia Biblica "the menologion of Basilius II (976-1025) in the Vatican Library" (l.16385–16386); none of the three cited passages gives a number. The `contested_claim` ends "(PG 99 names Vatican 1613; the others give no number)". The changed card sentence runs past 25 words (N6). |
| N3 Vigilius card `dates` and `uncertain` 6: 555 given as the record's own year | RESOLVED | Both now give "7 June in the third indiction, 555 by [Louis] Duchesne's reckoning". Loomis's note: "the seventh day before the Ides of June in the third indiction (June 7, 555)" Duchesne, op. cit., p. 302, n. 33" (`liber-pontificalis_book-of-the-popes-v1_loomis1916.txt` l.11934–11936). `uncertain` 6 adds the third side: "Indictione II. XIII p. c. Basilii v. c. Vigilius papa… in Sicilia morbo calculi tactus decessit" (mommsen1894 l.3260–3261, OCR), rendered "the second indiction, the thirteenth year after Basil's consulship". Card and records now agree, and no year is told as settled. The changed `dates` sentence runs past 25 words (N7). |
| N4 Procopius card `uncertain` 1: "would not set down its disputes" | RESOLVED | Now "would not set down the points of faith in dispute". Dewing: "to confer about a tenet of faith, which is a subject of disagreement and controversy among the Christians. As for the points in dispute, although I know them well, I shall by no means make mention of them" (`procopius_wars-5-6-gothic_dewing1919.txt` l.406–408). The sentence was already long before the change; see N7. |
| N5 Mar Aba records: double comma | RESOLVED | `records.json` l.440 now reads "held in Braun's German, 'aurait besoin…'". |
| C-M15 Antony and Ephrem: the Open-Gaps line owed | RESOLVED | The batch's Open-Gaps entry has: "Left in the source's form: Theodore the Studite's 'Antony and Ephrem', beside whom he says Barsanuphius's image stood, are given no place in the source, so the profile does not add one. Owner: the coordinator, if a place is wanted." |

## 2. New findings in changed text

- **N6 MINOR (`romanos-the-melodist.card.json` `uncertain` 1, second sentence; R2's own fix wording).** "Migne's edition of Theodore the Studite gives the same Vatican manuscript, number 1613, to the emperor Basil, and the Bollandists cite a Menologion made by order of the emperor Basil Porphyrogenitus." It is 31 words, past the ~25-word limit. Fix: end the sentence at "to the emperor Basil." and start a new one, "The Bollandists cite a Menologion made by order of the emperor Basil Porphyrogenitus." The content is right; this does not block clearing.
- **N7 MINOR (`vigilius-of-rome.card.json` `dates`, last sentence; `procopius-of-caesarea.card.json` `uncertain` 1, last sentence).** Vigilius: "A record of the time that Loomis reports gives 7 June in the third indiction, 555 by Louis Duchesne's reckoning; Henry Percival gives the end of 554 or the start of 555" is 32 words joined by a semicolon. Fix: a full stop after "reckoning", then "Henry Percival gives the end of 554 or the start of 555." Procopius: the sentence was 32 words before R2 and is 35 now. Fix: a full stop after "in dispute", then "It makes no claim about his faith." Neither changes a claim; this does not block clearing.

No changed text adds a misquotation, a witness swap, a false absence, an unsupported claim or a contested point told as settled.

## 3. Mechanical checks

- `records.json` and the four changed cards parse as JSON.
- No brief or audio script changed, so the audio-brief match, tag placing, `grade_text` scores and `briefLength` values stand as R2 gives them.

## Verdict

All five R2 findings (N1 to N5) are resolved, and each holds against its source. C-M15 is resolved by the batch's Open-Gaps entry. Two new minor points (N6, N7) are sentence-length splits in card text. They do not block. No change adds a wrong or unsupported claim.

## Totals

R2 findings: N1 to N5, 5 of 5 RESOLVED; C-M15 RESOLVED. None is PARTLY or NOT RESOLVED. New: 0 blocking, 2 minor (N6 `romanos-the-melodist` card; N7 `vigilius-of-rome` and `procopius-of-caesarea` cards).

Verdict: clear.
