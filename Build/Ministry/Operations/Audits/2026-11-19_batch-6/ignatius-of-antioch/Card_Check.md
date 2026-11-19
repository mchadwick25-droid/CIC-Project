# Card check: Ignatius of Antioch

Card checker, batch 6 (2026-11-19), under `Card_Check_Prompt.md`. Read: `ignatius-of-antioch.brief.txt`, `ignatius-of-antioch.card.json`, `Card_Edits.md`, `Card.existing.json` (identical to the census card for `ignatius-of-antioch`), and each cited line in its file.

**Verdict: FIX** (four changes below).

## 1. Each edit is justified

- **sources.about, Polycarp "chapters 3, 9 and 13".** Justified. The brief's "which Paul had once written to" stands in Phil. 3 (ANF 3309–3310, "when absent from you, he wrote you a letter").
- **sources.about, Athanasius and Theodoret added.** Justified by the brief's "Later bishops used his words on Christ's real flesh in their own quarrels" (NPNF4 59204–59210; NPNF3 20266–20290).
- **sources.about, Great Horologion added.** It may stay. After FIX 1 no quotation entry cites the file. But briefReferences names it as the Greek that Quote 3 is rendered from, and a file named only there may be in `sources`.
- **briefReferences, 16 lines.** Each was checked against the brief. Three name things the brief no longer tells (FIX 2 to 4).
- **quotationOriginals, five entries.** Each modern span is word for word in the brief. Each printed wording stands at its file and lines. Every cited file is in `sources`. The Quote 3 original is ruled on below (FIX 1).

## 2. Nothing else moved

A field-by-field diff against `Card.existing.json` shows only the listed changes: sources.about[1].title, three entries added at the end of sources.about, and the new briefReferences and quotationOriginals. Every other field is word for word and in order.

## The ruling: an original copied verbatim from garbled OCR

An original copied verbatim from garbled OCR should **not** stand on a live card. Quote 3's Greek is left out, and Ante-Nicene Fathers' English stands alone as its printed wording.

1. **It is not what any page prints.** "ΒΊτος εἰμὶ τοῦ Θ εοὗ, και δὶ ὀδόντων ϑηρίων ἀλήϑομα!, ἵνα καϑαρὸς ἄρτος εὐρεϑῶ" (HOR 15547–15552) has a scan fault in almost every word. It even has a Latin B and an exclamation mark. On the card it would be shown as the Greek of Ignatius, and that is a wording no one wrote.
2. **Nothing held can correct it.** A reading in `tools/quote_scan_readings.json` has to say what the printed page reads. Here every correction (Σῖτος, Θεοῦ, καὶ δι᾽, ἀλήθομαι, εὑρεθῶ) would come from knowing the text of Eusebius, not from a held print. No Greek of Romans 4 is held: Mirbt's excerpts (2635–2690) do not include it. The file's own header says its accented Greek is "partly garbled". Compare Tatian: there the same edition prints the clause cleanly in a note, so a reading is confirmed.
3. **The check cannot see it.** The census fold drops every Greek letter. A Greek original passes the check whatever it says, so nothing downstream would catch it.
4. **It is not the full original of the span.** It is an 1851 prayer book quoting Eusebius. It lacks "of Christ", which the modern span carries from ANF 7041–7042.

The same rule covers every card in the batch. An original stands only as the page prints it. A scan fault inside it is allowed only when a reading resolves it, and that reading must be confirmed by a held print of the same words, or the fault must be a stray mark that is plainly no part of the text. Otherwise the original is left out.

One point for the second reading. The modern span's "I am ground" follows the Greek indicative, which can still be seen in the scan ("ἀλήϑομα!"). ANF prints "let me be ground". The Horologion stays in `sources` and in briefReferences, so that basis can still be traced.

`Source_Sheet.md` (Language, line 18) says the wheat sentence "is held in clean Greek". That is wrong. The Greek in the outline (line 64) is a reconstruction, not the file's text.

**FIX 1.** `quotationOriginals[2]`
- Remove `original` (old: "ΒΊτος εἰμὶ τοῦ Θ εοὗ, και δὶ ὀδόντων ϑηρίων ἀλήϑομα!, ἵνα καϑαρὸς ἄρτος εὐρεϑῶ"), `originalFile` (old: "cic/texts/horologion-to-mega_venice-edition-grc_koutloumousianos1851.txt") and `originalLines` (old: "15547-15552").
- `work`. Old: "Ignatius, Letter to the Romans 4, shorter form, Ante-Nicene Fathers vol. 1; Greek as the Great Horologion (Venice, 1851) prints it from Eusebius". New: "Ignatius, Letter to the Romans 4, shorter form, Ante-Nicene Fathers vol. 1".

## 3. References

Three references name things the brief no longer tells. Some parts are kept because they show where the brief's claims come from: "truly persecuted under Pontius Pilate" (the source of the brief's Pilate clause), "whose patience they had seen" (where "the blessed Ignatius" stands), and "to heed the bishop, the elders and the deacons" (what he cried aloud).

**FIX 2.** `briefReferences[4]`. The brief no longer says the bishop presides in God's place, or that they pray as one.
- Old: "Magnesians 6 and 7, Ephesians 20: the bishop presiding in the place of God, with the elders and the deacons; one prayer and one altar; one bread broken together."
- New: "Magnesians 6 and 7, Ephesians 20: the bishop, with the elders and the deacons; one altar; one bread broken together."

**FIX 3.** `briefReferences[14]`. The brief does not tell the eight forgeries or the two Greek forms.
- Old: "Ante-Nicene Fathers vol. 1, the translators' introduction to the letters: fifteen letters under his name, eight set aside as forgeries, the seven in a shorter and a longer Greek form, and the long dispute over them."
- New: "Ante-Nicene Fathers vol. 1, the translators' introduction to the letters: fifteen letters under his name, and the long dispute over them."

**FIX 4.** `briefReferences[15]`. The brief does not name Neapolis.
- Old: "Polycarp 8: he must suddenly sail from Troas to Neapolis, the last we hear in his own words."
- New: "Polycarp 8: he must suddenly sail from Troas, the last we hear in his own words."

## 4. Census rules

The card uses only allowed keys and has no `briefLength`. There are five entries for the brief's five quoted spans, and none extra. Every cited file is in `sources`. No briefReferences entry has quotation marks. No audit, review or ruling is named. Spelling is American. No entry has a `secondReading` yet: all five spans are new and wait for step 7.

## 5. Originals

The outline renders only Quote 3 from Greek, which is covered by the ruling above. Quotes 1 and 2 are rendered from ANF's English, because no Greek of the letters is held.

## 6. Not found, and anything clearly wrong left in

The card writer listed no claims as not found. The card holds nothing clearly wrong. One point about the brief, outside the card: the brief has Polycarp ask "for news of 'the blessed Ignatius'". That phrase stands in Phil. 9 (ANF 3487), about patience. The request for news is in Phil. 13, which says "Ignatius himself". The card's entry cites the phrase's real place correctly.
