# Card check: Tatian (`tatian.card.json`)

Checker, 2026-11-28. I did not write this card. I read `CLAUDE.md` ("Trust and source fidelity"), Brief Kit Part 1, `kinds/person.md`, the card role, the era 1 card Header's four sections, the brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, `Fresh_Applied.md`, `Source_Sheet.md`, the card, `Card_Edits.md`, the starting card and the census entry. I opened every cited file at its lines. Short file names are those of `Source_Sheet.md`; MA is `apologists-fragmentary_reliquiae-corpus-apologetarum-vol9-grc-lat_otto1872.txt` (Otto 9, with Prudentius Maran's prolegomena).

**Verdict: FIX.** Three card changes and one entry-field change, given exactly at the end. Everything else passes.

## 1. Evidence, items sent to the card, modern works

- Every field in `Card_Edits.md` stands on its evidence. Each timeline line was read at its lines (AG 5684-5693, 5738-5740, 5820-5834, 6526, 6550-6556, 6962-6978, 7026-7030, 7076-7081, 7129-7133, 7249-7252, 7280-7292, 7387-7391, 7457-7471; IR 33655-33676, 43907-43913; HI 13005-13013, 15349-15352; TE 55817-55821; EU 24054-24055, 26424-26434, 26479, 26484-26505, 29214-29223, 32129-32139; JC 42908-42912, 43057-43061; JE 33157-33166, 40082-40099, 40228-40229; EP 15995-16009, 16075-16076; TH 4228-4240, 29625-29645, 29725-29741; MA 14970-14998; AD 65; DI 1763-1768, 1902-1919, 2108-2112, 2193-2197, 10422-10435; SE 15829-15831, 15905-15907; MS 14340-14354; VC 23148-23158, 23203-23206). Each headline names its period. Jerome's chapter title stands in the NPNF heading (JE 40084), and Jerome's own capitula in PL 23 print "Tatianus heresiarches" (`jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt` 47398).
- One date has no working shown. The Ephrem line's "In the 300s" cites SE and DI, and neither gives a year. A held line does give one: the Chronicle of Edessa dates Ephrem's death to the year 684 (`chronicle-of-edessa_cowper.txt` 103), which the tree's other cards already use. FIX 3 adds it, under the Header's "Dates from the sources' own clues".
- Every item the outline sends to the card is on it. That covers Cut first 1-6 and 10-18; Leave out ("card") for D2, D3, Crescens, 'Abdisho, Rabbula and the writer against Artemon; Holl's Mesopotamia point, given as a fact about held texts with Holl in `modernWorks` (Review B2); and the Fresh_Read note on "I know not how" (`uncertain[8]`). The writer was right to leave out Aphrahat, the Codex Fuldensis and Hogg's verse counts. Each rests on an editor's inference or a modern detail.
- No modern opinion, date or identification is stated as content. The starting card's McGiffert, Zahn, Harnack, Hogg and Lightfoot items are gone, and the old-source questions behind them are kept in `uncertain`. Each `modernWorks` note says what the work covers. FIX 4 completes one of them.

## 2. Nothing else moved

This is a new card under "A new card". The fields kept word for word (`knownFor`, `sources.ownWords`, the Epiphanius and Theodoret (Maran) entries in `sources.about`, the first sentence of `remembered[2]`, and `keyWorks[0]` from "his conversion" on) match the starting card exactly.

## 3. `briefReferences`

All thirteen lines name things the brief tells. The dropped lines (Address 2, 32, 33, 35 "the turn", 42 "the closing stand", Coxe and Ryland, McGiffert's date, and Hogg's) were rightly dropped.

## 4. Census rules

- Keys: the census check passes the card. On a census copy kept outside the repository, `node tools/validate-census.mjs` (full quote check) gives only errors that release clears: the two missing `secondReading` values, the two renderings not yet in `tools/quote_renderings.json`, and the three stale Tatian listings there.
- Three quoted spans in the brief and three entries, with none for a dropped span. Each `printed` stands verbatim at its lines: AG 6971-6978, IR 33664-33668, and EP 16076 ("Τὸ διὰ τεσσάρων", checked by hand). Every cited file is in `sources`, once FIX 3 adds the Chronicle of Edessa. No audit file is named. Spelling is American; "centred" is in Ryland's printed wording.

### Ruling on the writer's flags: Greek originals of Quotes 1 and 2

**Upheld. English alone for both.** This follows the batch 6 rule (`2026-11-19_batch-6/Batch_Originals_Ruling.md`): a scan fault stands only where another held print confirms the reading.

- **Quote 1 (Address 29).** There are two held Greek prints, not one. Otto 1851 has it (AG-G 10387-10394). Maran's prolegomena quote the whole passage (MA 14018-14025). Goodspeed 1914 has no Greek letters at all, by its own header. Most faults in one print are clean in the other, and Otto's own note at AG-G 10558-10559 confirms the second "ὡς". Two words are misread in both prints and cannot be confirmed:
  - The first ὡς: Otto has "ὗς" (10389) and Maran has "εἷς" (14020).
  - καί: Otto has "sul" (10391) and Maran has "Kal" (14021), in Latin letters.

  So no `original` can be printed. The card's note that the Greek is "held only in a damaged scan" is not accurate, though: FIX 1.
- **Quote 2 (Irenaeus I.28.1).** Maran quotes the second half of the passage (MA 14149-14151): "Mara δὲ τὴν ἐκείνου μαρτυρίαν ἀποστὰς τῆς ἐκκλησίας, οἰήματι διδασκάλου ἐπαρϑεὶς καὶ τυφωϑείς, αἷς διαφέρων τῶν λοιπῶν, ἴδιον χαρακτῆρα διδασκαλείου συνεστήσατο." This includes the clause that Holl and Wendland both leave out. But two faults have no confirming print:
  - "ἐχείνῳ" (EP 15968): only Holl prints the first sentence.
  - "αἷς" (MA 14150): no other print has the clause.

  "Mara" is resolved by Holl and Wendland ("μετὰ"), but the passage as a whole is not. English alone. The `uncertain` should name Maran's print: FIX 2.

## 5. "checked at card"

`quotationOriginals[2]`: "through four" renders "Τὸ διὰ τεσσάρων" (EP 16076; the same in EU 26433 and TH 29726-29727). It drops the article and adds nothing. PASS.

## 6. Not found, and anything wrong

- Nothing is listed as not found, and I found nothing clearly wrong beyond FIX 1 and FIX 2.
- `legacy.traces[0]` narrates the Doctrine of Addai close to its own words without quotation marks. That is allowed. The writer's reason ("the sibling's span is barred") is mistaken, since `syriac-edessa-nisibis` does not quote this line, but nothing needs to change.
- Readability, from my own run on the card's running text, kept outside the repository: `2158 words, grade 7.8 (names out 6.0), reading ease names out 78.2, 14.7 words a sentence, 0.1 joining words per 100, 24% short sentences, longest sentence 30 words - pass (note: grade 7.8 is under 8: the listener read checks it is not flat)`. That is under the floor of 8 because of the one-fact timeline lines. The card's longer texts keep the sources' own wording. Pass, noted.

### Ruling on the entry fields "Edessa" and "Asia Minor"

**Both are wrong for Tatian. Neither changes under this card.**

- **Edessa** (`region` "Rome, Edessa", `placeLabel` "Rome · Edessa", and the Edessa row of `modernCountries`). No held line puts Tatian at Edessa (S5, and the outline's Do not say). His held places are the land of the Assyrians, Rome, and, by Epiphanius alone, Mesopotamia. The card and brief do not repeat Edessa, so the conflict is in the entry, not the card. It is already registered (Open-Gaps, "Batch 6, era 1 (twelve stories and Polycarp): what is open at release", 2026-11-19, "Census fields outside the story and card"; owner: a census pass). A corrected `modernCountries` row needs place ids that no file here supplies, so release should not guess them.
- **Asia Minor** (`regions`). No held line puts him there. The value also fails the fleet rule, under which `regions` is the home tradition's: `syriac-edessa-nisibis` carries ["Middle East"]. This is the same case as Valentinus in this batch. Owner: the map build slice (Open-Gaps, the `regions` item carried in the era 3 release entries). Release should name Tatian in that item.

## 7. Census entry

There is no new entry: Tatian has one (`atlasId` I.76). The teaser is unchanged and says no more than `knownFor`.

## Exact changes

**FIX 1.** `card.quotationOriginals[0].uncertain`
- Old: `The modern English follows Otto's Greek of 1851, with each clause confirmed by Otto's Latin on the same page. That Greek and Latin are held only in a damaged scan, so Ryland's English is given as the printed wording. Ryland leaves out the clause on the clear account of how all things were made.`
- New: `The modern English follows Otto's Greek of 1851, with each clause confirmed by Otto's Latin on the same page. That Greek is held only in two damaged scans, Otto's edition and Prudentius Maran's quotation of the passage in Otto's ninth volume, and some words are misread in both, so Ryland's English is given as the printed wording. Ryland leaves out the clause on the clear account of how all things were made.`

**FIX 2.** `card.quotationOriginals[1].uncertain`
- Old: `The modern English follows the Greek of Irenaeus as Eusebius keeps it, which Karl Holl and Paul Wendland quote in their notes, two prints that agree. Both are held only in damaged scans, so the English of ANF 1 is given as the printed wording. Both leave out the clause puffed up as if he were better than the rest, which follows the English. The Greek word the English renders doctrine means a school.`
- New: `The modern English follows the Greek of Irenaeus as Eusebius keeps it, which Karl Holl and Paul Wendland quote in their notes, two prints that agree. Both leave out the clause puffed up as if he were better than the rest. Prudentius Maran's prolegomena, in Otto's ninth volume, quote the second half of the passage with that clause, and the rendering agrees with it there. All three are held only in damaged scans, and a word in the first sentence and one in that clause are misread in every print that has them, so the English of ANF 1 is given as the printed wording. The Greek word the English renders doctrine means a school.`

**FIX 3.** Two parts.
- (a) The `timeline` line with text `Later writers of the Church of the East say Ephrem, a deacon of Nisibis, commented on it.` gets a new `reference`.
  - Old: `Isho'dad of Merv, quoted in the introduction to the Arabic Diatessaron, cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml lines 1763-1768; Chronicle of Seert, cic/texts/barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt lines 15829-15831 and 15906-15907`
  - New: `Isho'dad of Merv, quoted in the introduction to the Arabic Diatessaron, cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml lines 1763-1768; Chronicle of Seert, cic/texts/barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt lines 15829-15831 and 15906-15907; Ephrem's death in the year 684 of the Greeks, so about 373, Chronicle of Edessa 30, cic/texts/chronicle-of-edessa_cowper.txt line 103`
- (b) In `card.sources.about`, insert this entry right after the `The Doctrine of Addai` entry:
  - `{"title": "Chronicle of Edessa, section 30", "author": null, "date": null, "language": "English translation", "file": "cic/texts/chronicle-of-edessa_cowper.txt"}`

**FIX 4 (entry field, for release).** In `modernWorks`, the entry titled `Corpus Apologetarum Christianorum saeculi secundi 9` gets a new `note`.
- Old: `Prints Theodoret's Greek and Latin on the Diatessaron and its copies.`
- New: `Prudentius Maran's prolegomena on Tatian, which quote the Greek of the Address, chapter 29, and of Irenaeus on the break, and Theodoret's Greek and Latin on the Diatessaron and its copies.`

With FIX 1-3 applied to a census copy kept outside the repository, the full census check gives the same release-owned errors and nothing new.
