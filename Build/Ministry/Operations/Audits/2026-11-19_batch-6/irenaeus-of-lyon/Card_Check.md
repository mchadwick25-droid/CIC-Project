# Card check: Irenaeus of Lyon (`irenaeus-of-lyon`), new card

**Verdict: FIX** (three card fixes, three reference fixes, one brief fix)

Read: `irenaeus-of-lyon.brief.txt` (final), `irenaeus-of-lyon.card.json`, `Card_Edits.md`, the census entry `irenaeus-of-lyon` (no `card`), `Outline.md` (Quotes), `Source_Sheet.md`. Every cited line below was re-read in its file.

## 1. Edits against their evidence

Every field was checked against the lines `Card_Edits.md` gives. All hold except the three below.

**FIX 1. `datesNote`: the Chronicle and 167.** McGiffert says the Chronicle's notice is "not placed opposite the seventh year of Marcus Aurelius ... but is placed after it, and grouped with the notice of Polycarp's martyrdom", and that Eusebius meant no single year by the grouping (EUS-ed 26708-26722). "Sets it beside 167" is what he denies. (The sheet's S4, "The Chronicle puts it at 167", has the same slip.)
- old: `Eusebius's Chronicle sets it beside 167, and McGiffert argues for 177.`
- new: `Eusebius's Chronicle places it after 167, grouped with Polycarp's martyrdom, and McGiffert holds that the grouping does not date it.`

**FIX 2. `uncertain[0]`: "No held line".** McGiffert (EUS-ed 24469) and Freese (PHOT 11596) are held, and both say he was born in Asia Minor. The next sentence of the card quotes them. What is meant is that no early source says.
- old: `No held line says where or when he was born.`
- new: `No early source says where or when he was born.`

**FIX 3. `uncertain[2]`: two letters run together.** The passage asking him to carry "this letter" comes from the martyrs' letter to Eleutherius, which Eusebius quotes in V.4 (EUS 27733-27739). The letter Valesius and Coxe thought he wrote is the account sent to the churches of Asia and Phrygia (EUS-ed 26855-26868; ANF-ed 29436-29437; EUS 27677-27678). The card makes them one letter, and its "it" moves from one to the other.
- old: `The year 177 and the martyrs' letter. The letter of the Christians of Vienne and Lyon says the imprisoned martyrs asked him to carry it to Eleutherius at Rome. It does not say he saw them die. Valesius thought he wrote it, and Coxe thinks so too;`
- new: `The year 177 and the martyrs' letters. In their letter to Eleutherius at Rome, which Eusebius quotes, the imprisoned martyrs asked him to carry it. Their letter to the churches of Asia and Phrygia does not say he saw them die. Valesius thought he wrote that letter, and Coxe thinks so too;`

## 2. Nothing else moved

There is no starting card, so nothing to diff. Nothing contradicts the entry's existing fields (`dates`, `sourcing`, `legacy`, `why`, `relationsSummary`). `Card_Edits.md`'s three notes on this are right.

## 3. References

Some parts name what the brief does not tell. The brief never names Eleutherius, and never says the truth came down by word of mouth (paragraphs 3, 5 and 7 say only "secret teaching", "about 180" and "to Rome").

**FIX 4. `briefReferences[1]`**
- old: `Against Heresies III.2: their claim that the truth came down by word of mouth and that they are wiser than the apostles. III.4.3: Valentinus at Rome.`
- new: `Against Heresies III.2: their claim that they are wiser than the apostles. III.4.3: Valentinus at Rome.`

**FIX 5. `briefReferences[2]`**
- old: `five books, written under Eleutherius, about 180.`
- new: `five books, about 180.`

**FIX 6. `briefReferences[3]`**
- old: `the letters sent from prison to Eleutherius at Rome, carried by Irenaeus, a presbyter of the church.`
- new: `the letters sent from prison to Rome, carried by Irenaeus, a presbyter of the church.`

The rest stays as written: [0], [4] to [11], and [1] to [3] once fixed. In [6], "down to Eleutherius" names the bishop the brief calls "the bishop of his own time", so it stays. [11], "his tradition", follows the census convention. The only quotation marks are around "the twelfth place from the apostles", which is verbatim in the brief.

## 4. Census rules

- Keys: all allowed, and there is no `briefLength`.
- Quoted spans: the brief has six, and there are six entries. None is stale.
- `printed` wordings: each stands at its file and lines, read in memory with tags removed and line-end hyphens joined:
  - Entry 2 also drops Holl's margin numbers "81,1" and "Ὁ182" and the page mark "|" (HOLL 32715-32716), as `Card_Edits.md` declares.
  - Entry 4 needs the `<pb>` inside "man-ner" (EUS 30812) removed.
  - Every `englishPrinted` stands at its lines.
- Cited files: every file a `quotationOriginals` entry cites is in `sources`: HOLL, ANF, EUS, HIPP (anf05) and TERT (anf03).
- Wording: the card names no audit, review or ruling. Its spelling is American, apart from verbatim printed wording ("skilful", "Irenæus").

**Scan readings for `tools/quote_scan_readings.json`: none needed.** No `printed` wording fails because of a scan fault. Entries 1 and 2 copy the OCR exactly as it stands, faults included. This is the census's existing practice for held Greek OCR, as in the Heikel, Oehler and Hussey entries.

Note for whoever owns the validator: `fold()` in `tools/validate-census.mjs` replaces every character outside a-z and 0-9, so Greek wording folds to an empty string. `wordingFault` then passes any Greek `printed` or `original`, right or wrong. The check above was done by hand for that reason.

For the second-reading step, which is not a FIX now: following that same practice, each Greek entry's `uncertain` should name its OCR faults. Suggested wording:
- [0]: `The file is OCR, kept as it stands: χ often stands for κ (εἰχόνος, χαλῆς, ἐχ, χαὶ, χυνὸς), Ψηφίδων reads ψηφίδων, ἀγϑρώπου reads ἀνθρώπου, and ἀλῴπεχος reads ἀλώπεκος; ϑ is the scan's θ.`
- [1]: `The file is OCR, kept as it stands: χ often stands for κ (χήρυγμα, χαὶ, ἐχχλησία, χαρδίαν), and προἔφαμεν reads προέφαμεν. Holl's margin numbers and page mark inside the span are left out.`

## 5. Originals

- Quotes 1 and 2 are rendered from the held Greek (HOLL), and the card carries that Greek with the ANF English beside it.
- Quote 3, the Florinus letter: Eusebius's Greek of Book V is not held, and the outline renders from McGiffert's English. The card cites that English.
- "The twelfth place": the Latin is not held, so the card cites the English.
- Hippolytus and Tertullian: the outline cites only their English.

Nothing is missing.

## 6. "Not found" claims, and the Florinus quote

`Card_Edits.md` lists nothing as not found, and its omissions are deliberate. All of them are acceptable.

**Florinus quote: the cut is real and hidden. FIX 7, in the brief.** The outline's Quote 3 rendering has five sentences. The fourth is "I can describe his comings and goings, the way he lived, how he looked, and his talks to the people." The brief keeps sentences 1, 2, 3 and 5 inside one pair of quotation marks. That joins "as he taught" straight to "And I can tell", with nothing in the text or in the voice to show that a sentence is missing. McGiffert's English (EUS 30807-30815) confirms that the missing sentence stands between them. The outline allowed the cut, but not a hidden one. So the span is not one continuous rendering.

The change: close the quote after "as he taught", tell the left-out middle in the narrator's voice, and reopen on the rendering's fifth sentence, which is whole. In paragraph 17 of `irenaeus-of-lyon.brief.txt`:
- old: `So I can describe the very place where the blessed Polycarp sat as he taught. And I can tell how he spoke of his time with John and the others who had seen the Lord."`
- new: `So I can describe the very place where the blessed Polycarp sat as he taught." He could describe, he wrote, how Polycarp came and went, how he lived and looked, and his talks to the people. "And I can tell how he spoke of his time with John and the others who had seen the Lord."`

The narrator's sentence restates EUS 30810-30814 ("his goings out and his comings in, and the manner of his life, and his physical appearance, and his discourses to the people"). It runs to 21 words. If 20 more words are too many, there is a second acceptable way: restore the outline's fourth sentence word for word inside the quote. That makes the span one continuous rendering.

What follows on the card, if the change above is made:
- `quotationOriginals[3].modern` stays as it is. The two spans, joined in order, are its present text, and the validator treats a quotation broken around narration as one entry. `printed` stays the whole sentence.
- `uncertain[8]`:
  - old: `and leave out the middle of his sentence, on Polycarp's comings and goings, his way of life, his looks and his talks to the people.`
  - new: `and the middle of his sentence, on Polycarp's comings and goings, his way of life, his looks and his talks to the people, is told in the narrator's words.`
- `briefReferences[8]`:
  - old: `the place where Polycarp sat, and his intercourse with John.`
  - new: `the place where Polycarp sat, his goings out and comings in, his manner of life, his appearance and his discourses to the people, and his intercourse with John.`

If the second way is taken instead, `quotationOriginals[3].modern` becomes the outline's full five-sentence rendering. `uncertain[8]` then drops the clause from "and leave out the middle" to "the people", and `briefReferences[8]` takes the same new text as above.

After the brief change, run `python -m engine.m1.profile_readability` on the brief again.
