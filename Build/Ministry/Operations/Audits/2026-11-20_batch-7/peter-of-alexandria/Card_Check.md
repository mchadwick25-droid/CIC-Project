# Card check: Peter of Alexandria

Card checker, batch 7 (2026-11-20), under `Card_Check_Prompt.md`. I wrote none of this card. Read: `peter-of-alexandria.brief.txt`, `peter-of-alexandria.card.json`, `Card_Edits.md`, `Card.existing.json` (identical to the census `card` for `peter-of-alexandria`), `Outline.md`, and each cited line in its file. Originals are ruled under `Build/Ministry/Operations/Audits/2026-11-19_batch-6/Batch_Originals_Ruling.md`. Greek was checked by hand, against the file's code points.

**Verdict: FIX** (seven changes below).

## 1. Each edit is justified

- **The spelling, Meletius to Melitius.** This follows the coordinator's instruction and the brief. There are seven places, not six: `uncertain[3]` ("over the Melitians", "with the Melitians") also changed, and `Card_Edits.md` does not list it. The change is right, since no quoted wording holds the name. Only the list is short.
- **`keyWorks[0].about`, three sentences.** These hold at ANF6 27480-27486 (canon 12), 27534-27538 and 27600-27603 (canon 13), 27036-27047 (canon 9) and 27632-27646 (canon 14). Outline 7 and 49 and Recheck 26 send them to the card.
- **`legacy.traces[2]`.** This holds at NPNF14 26731-26744 and PED 49704-49706.
- **`uncertain[8]` to `[11]`.** These hold at EUS 43236-43240, ANF6 25775-25778 and PED 49702-49703 ("Ἐν δὲ τῷ 304 ἔτει"); BELL 3198-3200; BELL 3205-3207, HEF 21952-21954 and ANF6 16836-16837 (it is the presbyters who were "then in hiding"); EUS 43218-43226, ANF6 25767-25776 and BELL 3210-3212.
- **`sources`.** Each added file is cited by a statement or a quotation entry.
- **`briefReferences`, fifteen entries.** Each draws on a passage the brief uses. Some parts name what the brief does not tell, and one says something untrue (FIX 3 to 7).
- **`quotationOriginals`, three entries.** Each `modern` stands word for word in the brief. Each cited file is in `sources`. The `printed` and `original` wordings are ruled in section 3.

## 2. Nothing else moved

A field-by-field diff against `Card.existing.json` shows only the spelling changes, the three sentences added to `keyWorks[0].about`, and the additions at the ends of `legacy.traces`, `uncertain`, `sources.ownWords` and `sources.about`, plus the new `briefReferences` and `quotationOriginals`. Every other field is word for word and in order.

## 3. Originals

**[0] Canon 1, σίγματα to στίγματα: KEEP. A held print confirms the reading.** The Pedalion scan prints "τὰ σίγματα τοῦ Ἰησοῦ" (PED 49723). Two held prints give στίγματα:
1. **The editor's own note on this very canon.** Hawkins's note 2284 in ANF6 (26618-26619) reads "The marks of Jesus, στίγματα", and it gives the Greek word of the canon. That is "the editor's own note", the first kind of confirmation in the batch 6 rule. It is a held print of the same word in the same text.
2. **A parallel held text.** The canon echoes Galatians 6:17, "τὰ στίγματα τοῦ Ἰησοῦ ἐν τῷ σώματί μου βαστάζω", which the held Nestle 1904 prints cleanly (`cic/texts/nestle1904_greek-new-testament-grc.txt` line 587).

Read by hand, the rest of the span matches PED 49722-49723 code point for code point. The bracket before οὐ is outside it. Only στ differs. The `uncertain` note says this plainly. One step remains outside the card: the census check needs this reading in `tools/quote_scan_readings.json` (scan "σίγματα", reads "στίγματα", confirmed by ANF6 26619). I have not touched that file.

**[1] Panarion 68.3, "0" to ὁ: KEEP. A held print confirms the reading.** Oehler prints "Πέτρου 0 λόγος" (EPI 43852). This is not the Pliny case, where a zero stood for the same capital shape: here the zero stands for an omicron with breathing and accent, so it needs a print. Migne's PG 42 prints "Πέ-/τρου ὁ λόγος" cleanly (13796-13797), and it is another held edition. The rest matches Oehler code point for code point, including Oehler's mixed ϑ and θ (one letter in two forms, not a reading). The card rightly does not take over PG's own faults ("Μελητίον", "χαὶ"). No English print of the sentence is held (Hefele and Bell were searched), so the Greek is the printed wording. This also needs a line in `tools/quote_scan_readings.json` (EPI 43852, "0" reads "ὁ", confirmed by PG 42 13797).

**[2] HE IX.6.2: English alone, correct.** Schwartz's Greek (EUS-G 17556-17558) has "διαξιμίνου", "χαὶ" and "ὡἧς", with no other print. McGiffert's English stands verbatim at EUS 47996-47998.

## 4. Not found, and anything clearly wrong left in

**FIX 1.** `uncertain[0]`, "Socrates of Constantinople and Theodoret say the same": **partly wrong, so FIX.** Socrates does say it: Melitius was deposed by Peter "in consequence of many other charges, and more especially because during the persecution he had denied the faith and sacrificed" (SOC 2405-2409). Theodoret does not. He says Melitius "was convicted of certain crimes by the most holy Peter" and deposed (NPNF3 6551-6553), with no sacrifice and no council. A held source contradicts "the same" for Theodoret. Each source is credited for what it says.
- Old: `Socrates of Constantinople and Theodoret say the same.`
- New: `Socrates of Constantinople says the same; Theodoret says only that Peter convicted him of certain crimes and deposed him.`

**"Later Coptic and Ethiopic lives give a family, and do not agree with each other" (`uncertain[5]`): not found, so it stands.** No held source supports it. The held Coptic life (History of the Patriarchs, 24858 on) gives no parents, and it calls Peter Theonas's "son and disciple" in the spiritual sense. The held Ethiopic Synaxarium has only index entries and the succession (19817-19818). Neither contradicts the clause, because each is silent. By the card rule it stays, listed as not found. The coordinator should log it in the world's `Open_Gaps_Tracking.md` as an existing card claim with no held source.

**FIX 2.** `sources.about[4].title`. The brief and the card's `legacy.remembered[2]` draw on Socrates I.15 (SOC 4007-4008), and `briefReferences[14]` cites it, but the title leaves it out. Adding it is a "new" edit justified by the brief.
- Old: `Church History, Book 1, chapters 6 and 9 (Socrates); Book 1, chapters 15 and 24 (Sozomen)`
- New: `Church History, Book 1, chapters 6, 9 and 15 (Socrates); Book 1, chapters 15 and 24 (Sozomen)`

## 5. References

**FIX 3.** `briefReferences[0]`. The last sentence is untrue: the brief's opening words are a modern rendering of the Greek, not Hawkins's English. It is also process narration.
- Old: `Peter of Alexandria, Canonical Epistle, canon 1, tr. James B. H. Hawkins: the fourth passover of the persecution, those tortured until they gave way, the marks of Jesus, and the forty more days. The opening words are in Hawkins's English, with the Greek of the 1886 Pedalion beside it.`
- New: `Peter of Alexandria, Canonical Epistle, canon 1, tr. James B. H. Hawkins, and its Greek in the 1886 Pedalion: the fourth passover of the persecution, those tortured until they gave way, the marks of Jesus, and the forty more days.`

**FIX 4.** `briefReferences[1]`. The brief does not name Theonas.
- Old: `Peter bishop at Alexandria after Theonas, less than three years`
- New: `Peter bishop at Alexandria, less than three years`

**FIX 5.** `briefReferences[3]`. The brief does not tell the lapsed asking the martyrs for mercy.
- Old: `the archbishop of Alexandria governs all Egypt; the lapsed ask the martyrs for mercy; the two in prison`
- New: `the archbishop of Alexandria governs all Egypt; the two in prison`

**FIX 6.** `briefReferences[10]`. The brief does not say Peter was among the first victims.
- Old: `the persecution renewed under Maximinus and Peter among its first victims.`
- New: `the persecution renewed under Maximinus, and reaching Peter.`

**FIX 7.** `briefReferences[12]`. The brief does not name Zonaras or Balsamon.
- Old: `Hawkins: the canons in every collection of canons, with the notes of Zonaras and Balsamon.`
- New: `Hawkins: the canons in every collection of canons.`

**References that remain:** `[2]`, `[4]` to `[9]`, `[11]`, `[13]` and `[14]` as they stand, and the rest as fixed.

## 6. Census rules

The card uses only allowed keys and has no `briefLength`. It has three entries for the brief's three quoted spans, and none extra. No `briefReferences` entry has quotation marks. No audit, review or ruling is named. Spelling is American in the new text. No entry has a `secondReading`, since all three spans are new.
