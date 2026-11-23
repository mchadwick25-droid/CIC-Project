# Card check, modern pass: Ephrem the Syrian

I checked `ephrem-the-syrian.card.json` against `Card.pass3.json`, the section "Fourth pass: no modern opinion (2026-11-23)" of `Card_Edits.md`, and `ephrem-the-syrian.brief.txt` as it now stands. I opened every cited line.

**Verdict: FIX.** Seven changes, listed below.

## 1. Edits justified

- **Edit 1 (Harmonius entry).** Gwynn's lines support it: npnf213 11234-11246 has "attributing the work, however, to Bardesan solely", and the quoted lines ("He fashioned hymns ...") do not name Bardaisan. Line 11236 has "not included in our selection". But the "sons" note at Mitchell-file line 2690 is not Mitchell's. It falls inside "INTRODUCTORY ESSAY / BY F. C. BURKITT" (lines 2585-2586, signed at 2777), and the file header (lines 5-7) credits Burkitt with Volume II's introduction. The essay says "I have published two separate translations of the great Hymn", which is Burkitt writing. See FIX 1. "Known only from the extract he prints" is also wrong. Gwynn cites the homily in *Opera Syriaca* II, p. 554 (endnote 265). It is held here only in his extract. See FIX 1.
- **Edit 2 (famine date).** The Chronicle of Edessa supports it: Cowper line 103 (year 684, Haziran) and line 34 (the Greek era is 311 years before Christ's birth, by Assemani's reckoning, and Assemani is named at line 28). Sozomen, npnf202 32138-32140, supports "shortly before his death". But "Modern dating" names no one. The modern source is Gwynn. He calls the famine story "undated" and assigns it "to the winter of 372–3" (npnf213 12355-12357), and he dates the death to 373 with "the chronologers", chief among them the Edessene Chronicle (12333-12340). See FIX 2.
- **Edit 3 (the prayer).** The file header (line 1) supports it: "being a confession-prayer of the Manichaean auditores", in JRAS 1911, from Tun-huang. Lines 16575-16585 and 16643-16672 have the Bright Root, the Dark Root, Light and Darkness "intermingled", and "will (again)" be parted. Neither range names Mani. Supported.
- **Edit 4 (Barhadbeshabba's date).** Scher 16929-16933 supports the Hnana half: "il fit ses études dans l'école de Nisibe sous Hnana d'Adiabène". The "about 600" half is not Scher's. "fl. c. 600" is in the Library's own file header (line 3), not in Scher's text. What Scher does say is that the author attended the synod of 605 (16975) and wrote the treatise at Nisibis "du vivant même de son maître Hnana" (16993-16994). See FIX 3. Leaving out the Inferential-Thin founder view is right: it was the outline's own rating, not a named modern author's view, and the brief no longer says it.
- **Edits 5-8.** The brief now gives no year, no prayer and no homily, and its last paragraph matches Scher 20740-20741 ("Les écoles se multiplièrent dans l'empire des Perses"). All supported.
- **Edit 9 (sources.about).** Both files exist and are cited. Supported.

## 2. Nothing else moved

A JSON diff of `Card.pass3.json` and the card shows only edits 1-9. Everything else is word for word.

## 3. briefReferences against the brief

No entry names wording the brief has dropped. The year, the prayer, the homily and "around 600" are all gone. The Palladius entry's quoted words stand verbatim in brief paragraph 1. A note, not a FIX: the Theodoret II.26 entry (Nisibis on the border) predates this pass. It supports the brief's border setting only by inference, as the first pass's Not found already records.

## 4. Census rules

Only allowed keys are used. The brief has one quoted span, and the card has one `quotationOriginals` entry for it. Its `modern` text is identical to the brief, and its `printed` text is verbatim at Clarke line 471. Every cited file is in `sources`. No audit is named, and the spelling is American.

## 5. "checked at card"

No quotation is under six words, so there is nothing to check.

## 6. Modern views not credited by name, and statements clearly wrong

These are modern views the card does not credit by name, or does not mark as modern:
- `uncertain[1]`: "Most writers date his death to 373, and some to 378." This is Gwynn's "373 according to most authorities, but some suppose him to have lived to 378" (npnf213 10627-10628). See FIX 4.
- `uncertain[4]`: "A modern editor of Eusebius" is A. C. McGiffert. The card's own `sources.about` names him, and the file credits him at npnf201 55-56. See FIX 5.
- `legacy.traces[2]`: "the account of his life nearest to his own time" is Gwynn's judgment: "what is of most weight", "the almost contemporary biographical particulars" (npnf213 10658-10660). See FIX 6.

This statement is clearly wrong against a held source:
- `keyWorks[2].about`: "names Bardaisan's hymns". The held lines (npnf213 11238-11244) do not name him. That reading is Gwynn's, as the card's own `uncertain[3]` now says. See FIX 7.

## FIX

**FIX 1. `uncertain[3]`.**
Old: `Modern judgment, John Gwynn: he reads Ephrem's Homily 53, known only from the extract he prints, as blaming Bardaisan alone (Gwynn, Nicene and Post-Nicene Fathers, series 2, vol. 13, introductory essay). The held lines of the homily do not name Bardaisan. C. W. Mitchell notes that Ephrem's Hymn 55 against Heresies gives the songs to Bardaisan's \"sons\".`
New: `Modern judgment, John Gwynn: he reads Ephrem's Homily 53, held here only in the extract he prints, as blaming Bardaisan alone (Gwynn, Nicene and Post-Nicene Fathers, series 2, vol. 13, introductory essay). The held lines of the homily do not name Bardaisan. F. C. Burkitt notes that Ephrem's Hymn 55 against Heresies gives the songs to Bardaisan's \"sons\".`

**FIX 2. `uncertain[5]`.**
Old: `Modern judgment: no old source gives the famine a year. Modern dating puts it about 372 and his death in 373, from the Chronicle of Edessa's year 684 (Cowper, translator) by Assemani's era reckoning. Sozomen places the famine shortly before his death.`
New: `Modern judgment, John Gwynn: no old source gives the famine a year, and he assigns it to the winter of 372-373. He dates the death to 373 with the old chronicles, among them the Chronicle of Edessa, whose year 684 (Cowper, translator) is 373 by Assemani's era reckoning. Sozomen places the famine shortly before his death.`

**FIX 3. `uncertain[7]`.**
Old: `Modern judgment, Addai Scher, editor of Barhadbeshabba: he dates the author about 600 and has him study at Nisibis under Hnana of Adiabene. The work itself gives no year.`
New: `Modern judgment, Addai Scher, editor of Barhadbeshabba: he has the author study at Nisibis under Hnana of Adiabene, write the work there while Hnana still lived, and attend a synod in 605. The work itself gives no year.`

**FIX 4. `uncertain[1]`.**
Old: `Most writers date his death to 373, and some to 378.`
New: `Modern judgment, John Gwynn: most authorities date his death to 373, and some to 378.`

**FIX 5. `uncertain[4]`.**
Old: `A modern editor of Eusebius writes that Bardaisan`
New: `Modern judgment, A. C. McGiffert, editor of Eusebius: he writes that Bardaisan`

**FIX 6. `legacy.traces[2]`.**
Old: `Gregory of Nyssa gave a speech in his praise, the account of his life nearest to his own time.`
New: `Gregory of Nyssa gave a speech in his praise. In the modern judgment of John Gwynn, it is the account of his life nearest to his own time.`

**FIX 7. `keyWorks[2].about`.**
Old: `A metrical homily that names Bardaisan's hymns as poison with sweetness.`
New: `A metrical homily that calls a heretic's hymns poison with sweetness.`

After the fixes are applied, run `tools/validate-census.mjs` again.
