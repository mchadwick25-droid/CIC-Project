# Card edits: Josephus

Card written to `josephus.card.json` from `Card.existing.json`. Every field not listed below is word for word. No census entry was written (the entry `josephus` exists). Files are in `cic/texts/` unless marked. JW = `josephus_works-antiquities-wars-life_whiston1859.txt`; EH = `npnf201_eusebius-church-history-life-of-constantine.xml`.

## Edits to existing fields

### briefReferences (entries that name what the brief no longer tells)

1. Entry 1. Old: "...the secret prayer, the lots, and the prediction to Vespasian." New: "...the secret prayer, and the lots." Evidence: the brief tells no prediction (outline Cut first 9).
2. Entry 2 removed whole (Jewish War 4, the release in 69; Book 5, the walls of Jerusalem in 70). Evidence: the brief tells neither (Cut first 8, 9).
3. Entry 3. Old: "...the Jews' wish to punish him and the Romans' charge of "treachery", the emperors' favor at Rome, and his closing words...". New: "...the emperors' favor at Rome, and his closing words...". Evidence: the brief has no treachery charge (Cut first 8); it keeps the emperors' favor and the close.
4. Entry 5 removed whole (Suetonius, Vespasian 5). Evidence: Cut first 9.
5. Entry 6. Old: "...and that he did not accept Jesus as the Christ. Origen never cites the passage on Jesus." New: the same without the last sentence. Evidence: Cut first 19; the fact stays on the timeline and in `uncertain`.
6. Entry 7. Old: "...and McGiffert's note that Eusebius is the first known to quote it. Church History 3.5: the fall of Jerusalem, from Josephus, as God's judgment on the Jews." New: "...as the word of a Hebrew historian." Evidence: the brief says Eusebius copied the passages, not that he was first (Do not say); 3.5 is outside the brief (Leave out). Both stay on the card elsewhere.
7. Entry 9 removed whole (McGiffert's notes and the four views). Evidence: the brief tells no modern view; the views stay in `uncertain`.
8. New entries added (7): the sword and the lots; why he wrote (War and Antiquities openings); the defence against Justus; the three Antiquities passages with lines; Eusebius 1.11, 2.23, 9.5 with lines; the Greek of the passage on Jesus; the Greek of the phrase on James. Evidence: brief paragraphs 3, 4, 5, 6, 7, 8; Source Sheet E5, E10, E11, E12 to E14, I1, I2.

### legacy.remembered (three added after the existing two)

- Jerome, late fourth century, Latin: "credebatur esse Christus", JVL lines 50905-50907 (brief paragraph 9).
- Sozomen: SOZ lines 26287-26304 (Source Sheet I4; the outline sends it to the card).
- Michael the Syrian: `michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt` lines 11161-11165 and 11230-11236 (Cut first 1 sends it to the card). "Syriac Orthodox patriarch": the file header, as the Source Sheet reads it.

### uncertain (three added after the existing seven)

- Why he went to Galilee: JW lines 1659-1681 and 106926-106929 (Source Sheet D1; Cut first 6).
- How the old copies word the key clause: EH 9232; JVL 50907; Michael lines 11233-11235; OMG 3731-3733 (D2; brief paragraph 9).
- Jerome's three additions: JV 39720-39724 (D4).

### sources.about

- Removed: "Dissertation I, on the testimonies of Josephus" (William Whiston). It is a modern work; it moves to `modernWorks` (below).
- Added, same file as Eusebius's existing entry: "Church History, Book 1, chapter 9; Book 2, chapter 23; Book 9, chapter 5". Added: Jerome, Illustrious Men 13 in English (JV); Sozomen, Church History 1 (SOZ); the Greek Martyrdom of Donatus (`acta-sanctorum_maii-tomus-5-lat_palme1866.txt`), the second held Greek print of the passage on Jesus.

### quotationOriginals (replaced by one entry per quoted span in the brief; the five old entries are for spans the brief no longer quotes, and the old entry for the prayer is for different words)

1. The prayer. modern: the brief's span. printed: JW lines 110852-110856, verbatim. No original: the Greek is not held. No `secondReading` (over six words).
2. The passage on Jesus. modern: the brief's span. printed: McGiffert's English, EH lines 9228-9232, verbatim ("the Greeks", which the brief's rendering follows; Whiston has "Gentiles"). The Greek is held only in two damaged scans (`jerome_opera-pl23-...` lines 50993-51005, Acta Sanctorum lines 80255-80262). They agree on these sentences, but my reading of them is a cleaned reading that does not stand verbatim in the scans, so the entry prints the English alone and gives the Greek in `uncertain`. The clause Ὁ Χριστὸς οὗτος ἦν stands clean at Acta Sanctorum line 80262 and Jerome file lines 50948-50949. Greek checked by hand.
3. James. modern: the brief's span. printed: Whiston, JW lines 91005-91009. original: Origen's Greek "τὸν ἀδελφὸν Ἰησοῦ τοῦ λεγομένου Χριστοῦ", OMG lines 3729-3730 (clean, checked by hand); it carries the phrase on Jesus only. "James by name" follows Eusebius's Greek in McGiffert's note (EH 13596-13602), whose scan is damaged, so it is not given as `original`; McGiffert's English "James by name" stands at EH line 13593.

### New fields

- `shortDescription`: the brief's first and second paragraphs (Jotapata, the command in Galilee, Vespasian, 67, the history at Rome, the three passages, Christians copying them).
- `briefSources`: the old sources the brief draws on, each with its file.
- `timeline`: ten periods built from the Source Sheet (E1 to E14, I1 to I5, I7, D2 to D4, D6), the outline and the card. Dates only where the old source fixes them or they are Widely Accepted (37, 66, 67, 69, 70, about 93); the rest say "Date unknown". No modern work or view is on it.

## Entry fields (for release; not applied here)

- `modernWorks`: add (moved word for word from `sources.about`): title "Dissertation I, on the testimonies of Josephus", author "William Whiston", note "The translator's study of the testimonies on John, James and Jesus, printed in the 1859 edition of his Josephus." No year, publisher or url is held for it. Rights: pre-1931, held in `cic/texts/`. McGiffert's notes and Chabot's note stay inside their old-source entries (an edition of an old text); say if they should also be listed.
- `longDescription`: the brief, final newline removed.
- `teaser`: now "A Jewish priest and historian at Rome, whose Antiquities of the Jews names Jesus and his brother James." It names a work without saying what it is. Proposed: "A Jewish priest who commanded against Rome, then wrote his people's history at Rome, in which a few lines tell of John the Baptist, James and Jesus." Evidence: brief paragraph 2.
- `dates` "37 to early 2nd c." and `end` 101: the death date is an editors' reckoning (EH 15900-15901; JV 39708 "died after 97"); no old source gives it (outline Do not say). Not changed here; see below.
- The entry has no `why` or `relationsSummary`.

## Conflicts with the entry and claims not found

- `datesNote` "Born 37; died early in the second century": the birth year stands (JW 1426-1428, with the accession of Gaius). The death date is not found in any old source; only modern editors give it. Left in place.
- `legacy` and `uncertain` carry McGiffert's and Whiston's views and McGiffert's "first writer known" claim. They are held and attributed (EH 9182-9214; JW 138244-138252; EH 13605-13616), and the outline sends them to the card. Left in place. The final check may rule on them under its item 1.
- `keyWorks`, Life: "written to answer his accusers". The held Life answers Justus (JW 4614-4632) and also records accusers at Rome (JW 5468-5482). Left in place.
- `uncertain` 5: "Whiston discusses why". Whiston's Dissertation takes up the James line (JW lines near 138200-141500), but the exact lines were not re-read. Left in place.
- `knownFor` and `legacy` name the Antiquities and the Church History without a gloss. Left in place (word for word).
- No claim of the existing card contradicts the brief or a held source.

## Validator run (census copy outside the repository, this card and the brief as `longDescription`)

`node tools/validate-census.mjs` on the copy: every check on the card passes (keys, `printed` and `original` stand at their lines, one entry per quoted span, cited files in `sources`). The only errors left are the three that release clears:

- `secondReading` is absent on all three entries (each is over six words), as the card role requires.
- `tools/quote_renderings.json` still holds three `josephus` records for the old renderings; they are for release to replace with the brief's three.
- The brief's three quoted spans are not yet in `tools/quote_renderings.json` (they are renderings, not verbatim print).
