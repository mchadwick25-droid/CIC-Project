# Card check, what it was about pass: Ephrem the Syrian

Checked `ephrem-the-syrian.card.json` against `Card.pass2.json`, the section "Third pass: what it was about (2026-11-23)" of `Card_Edits.md`, and `ephrem-the-syrian.brief.txt` as it now stands. Every cited line was opened.

**Verdict: FIX.** Three changes, below.

## 1. Edits justified

- **Edits 1-2 (Palladius wording).** The new wording stands verbatim in brief paragraph 1, and it is the second sentence of `modern_rendering` in `records/syr/quote/syr.quote.palladius-hospitaller.md`. `printed` re-read: Clarke line 471, "See, on your behalf I appoint myself hospitaller." Verbatim. But see FIX 3.
- **Edit 3 (`secondReading` removed).** Right: the quotation is over six words and its rendering changed, so release sets it.
- **Edit 4 (Mani).** Mitchell 418 (Darkness framing the Body as a "Prison-house for the Soul"), 431 (two Roots), 727 (the Light "mixed and mingled"), 771. Supported, credited to Ephrem.
- **Edit 5 (Manichaean prayer).** Le Coq 16575-16585 (the Bright Root and the Dark Root), 16643-16672 (Light and Darkness intermingled, to be parted again). Supported. The file header confirms Le Coq, JRAS 1911, English translation, Tun-huang.
- **Edit 6 (Marcion).** Mitchell 592 (the Stranger came down; the Souls ascended), 596, 1003 (the Stranger above everything), 1603 (the Maker and the Stranger). Supported.
- **Edit 7 (Nisibene Hymn 51).** Gwynn 11200-11214 ("a book of Bardaisan ... if the body be not raised"); Gwynn 11189-11190 names it the 51st. Supported.
- **Edit 8 (new `uncertain` entry).** The McGiffert note (Eusebius 26542-26556) supports "seems" and Hort. Two other statements in the entry are contradicted by held sources. See FIX 1 and 2.

## 2. Nothing else moved

A JSON diff of `Card.pass2.json` and the card shows only edits 1-8. Everything else is word for word.

## 3. briefReferences against the brief

Every entry names something the brief tells. Nothing to remove.

## 4. Census rules

Only allowed keys. One quoted span in the brief, one `quotationOriginals` entry, its `modern` identical to the brief. `printed` verbatim at line 471. The quotation's `secondReading` is left for release, as the task directs. No audit file named. American spelling. New files are in `sources.about`, except the two FIX 2 adds.

## 5. "checked at card"

No quotation under six words. Nothing to check.

## 6. Not found, and clearly wrong

Two statements in the new `uncertain` entry are contradicted by held sources:

- "comes from Ephrem alone". Epiphanius, Panarion 56.2.1 (`cic/texts/epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt` lines 26497-26501), says Bardaisan, "τὴν τῶν νεκρῶν ἀνάστασιν ἀρνησάμενος", denied the resurrection of the dead. The Greek was checked by hand.
- "No work of Bardaisan's own is held." `cic/texts/anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` holds "Bardesan. The Book of the Laws of Divers Countries" (line 67888 onward). Its editor says Eusebius gives it to Bardaisan, and that critics take it as a pupil's work that "gives us the genuine opinions and reasonings of Bardesanes" (lines 67854-67858). It is on fate and free will (lines 67900-67906). A word search of it finds no passage on the resurrection. The batch's own `About_Check.md` and `Outline.md` item 5 carry the same premise; the card took it from them.

Also, the Palladius `briefReferences` entry credits the brief's modern wording to "tr. W. K. Lowther Clarke". Clarke's line 471 reads "hospitaller". This is FIX 3.

## FIX

**FIX 1. `uncertain`, last entry.**
Old: `The charge that Bardaisan denied the body would rise comes from Ephrem alone. A modern editor of Eusebius writes that Bardaisan \"seems\" to have denied the proper resurrection of the body, while Hort, whom he cites, held that Bardaisan kept the common faith except on isolated points. No work of Bardaisan's own is held.`
New: `The charge that Bardaisan denied the body would rise comes from his opponents, Ephrem and later Epiphanius of Salamis. A modern editor of Eusebius writes that Bardaisan \"seems\" to have denied the proper resurrection of the body, while Hort, whom he cites, held that Bardaisan kept the common faith except on isolated points. The one held work of his school, the Book of the Laws of Countries, is on fate and free will.`

**FIX 2. `sources.about`, two new entries after the McGiffert entry.**
Old: (none)
New:
```json
{
  "title": "Panarion, heresy 56 (Bardesanes)",
  "author": "Epiphanius of Salamis",
  "date": null,
  "language": "Greek",
  "file": "cic/texts/epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt"
},
{
  "title": "The Book of the Laws of Divers Countries",
  "author": "School of Bardaisan",
  "date": null,
  "language": "English translation",
  "file": "cic/texts/anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml"
}
```

**FIX 3. `briefReferences`, Palladius entry.**
Old: `the exchange, \"See, on your behalf I appoint myself to take in and care for the needy.\";`
New: `the exchange, in modern English, \"See, on your behalf I appoint myself to take in and care for the needy.\";`

## 7. Census entry

None written. Not applicable.
