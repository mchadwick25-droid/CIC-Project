# Card check 2: The Church of Antioch in the Third Century

Checked: `antiochene-church-third-century.card.json` and `Card_Edits.md` (with its "Changes after the grade fixes" section), against `Card.existing.json`, the final brief (`antiochene-church-third-century.brief.txt`, after `Grade_Fixes_Applied.md` and `Grade2_Fixes_Applied.md`), `Outline.md`, `Review.md`, `Fresh_Read.md`, `Card_Check.md`, Part 1 of the kit and `kinds/tradition.md`. There is no entry file, since the tradition already has its own census entry.

## Verdict

FIX

## What holds

- **The earlier check's corrections are applied.** Card_Check 6 (`legacy`, "Three things") and 7 (`floorNote`) are in the card file. Card_Check 1-5 (`teaser`, `relationsSummary`, `documentedStories[0].text`, `.sources[1].note` with the Mayer entry, `.caveat`) are listed under Entry fields as edits 17-21, word for word as given. Edit 12 is withdrawn. Both evidence corrections (9d, 9j) are recorded.
- **Nothing else moved (check 2).** Field by field against `Card.existing.json`, only `sourcing`, `floorNote`, `voices[0]`, `voices[1]`, `voices[4]` and `legacy` differ, each as listed (edits 1-5, 15, 16). `why`, `relationsSummary`, `teaser`, `documentedStories` and `people` are word for word, and `Card.existing.json` still matches the live census entry.
- **The final brief.** Every `briefReferences` entry matches what the final brief tells; none names a thing it dropped. Edits 23 and 24 match the brief's new sentences on the church's house, the judges' request and Eusebius of Nicomedia. The cut Malchion judgment is on the card as `uncertain` item 4 (edit 22), credited to Eusebius, without quotation marks.
- **Quotations (checks 4, 5).** The final brief has three quoted spans; the card has one entry for each and none for a dropped span. Each `modern` matches the brief exactly. No entry needs "checked at card", since all three run six words or more, and none carries `secondReading`. Re-opened: McGiffert E-Eng 42165-42168, Chrysostom's Latin 15435-15440 and Jackson Thdt 6063-6064 each hold their `printed` verbatim. Schwartz E-Gk 11896-11900 and Oehler Epiph-Gk 45744-45746 hold the two `original`s as the scans read them. I checked both Greek texts and the Latin by hand against the renderings, and they match. Rufinus (11951-11955) and McGiffert confirm the damaged Eusebius scan, and Jackson confirms the damaged Epiphanius scan.
- **Cited lines.** I re-opened every line the card cites in `cic/texts/`, and each holds what the card says of it: E-Eng 41784-41785, 41836-41851, 41859-41861, 41894-41899, 41936-41954, 41977-41984, 41993-42072, 42079-42110, 42128-42178, 42178-42245, 42262-42330, 44730-44735, 48018-48023; E-Gk 11546-11553, 12114-12122; JerChr 44280-44287; Ath 58970-58998, 59053-59057; Hil 9607-9611, 9772-9773; Bas 27366-27368, 27403-27407; Thdt 5278-5283, 5752-5775, 6002, 6025-6031, 6045-6046, 6063-6064, 40904-40912, 40995-40998; Philost 138, 178; Soz 31022-31035; Nic 5296-5306. Card-prose quotations stand in their files: "Paulianists" (Nic 5297) and "most equitably" (E-Eng 42326).
- **Census rules.** Every cited file is in `sources`. No audit file is named. The spelling is American. The keys are the ones `Card_Edits.md` sets out. A scratch census copy outside the repository, with the card fields, the final brief as `longDescription` and Entry-field edits 13, 14 and 17-21 merged, gives 0 errors with `node tools/validate-census.mjs <copy> --skip-quotes`. The full run without `--skip-quotes` was killed for lack of memory in this container, so the quotations were checked by hand as above.
- **Items sent to the card.** All are on it: Cut first 1, 2, 3, 4, 6 and 7; Ruled 1, 2, 4 and 5; beat 4's Malchion judgment (Grade 2); What came of it 2 and 3; D1-D4 and D6; McGiffert's notes under `modernWorks`. The review and the fresh read send nothing to the card.
- **Not found and flagged.** The lists are fair, and nothing clearly wrong is left in the card file.

## FIX

### Entry fields (for release)

1. `relationsSummary` (the new text of edit 18). "Anomoean" is named without the explanation Part 1 requires. A held line gives its sense, in an opponent's mouth: Sophronius of Pompeiopolis says Aetius brought in "a dissimilitude of substance" by the word *anomoion*, "unlike as to substance or essence" (Socrates, Church History, Book 3, chapter 10, `npnf202` lines 10975-10983). The not-found claim "the first Anomoean teacher" stays.
   - Old: "Three of them later taught Aetius, the first Anomoean teacher."
   - New: "Three of them later taught Aetius, the first Anomoean teacher, whose opponents said he called the Son unlike the Father in substance."
2. `why` (as edit 10 leaves it). It names 'homoousios' without saying what the word meant (Part 1). The card's own `uncertain` and `legacy` gloss it. Held: "the Only begotten Son is said to be homoousios with God the Father" (Basil, `npnf208` line 39722).
   - Old: "In the 350s, bishops wary of Nicaea's word 'homoousios' pointed back to this council."
   - New: "In the 350s, bishops wary of Nicaea's word 'homoousios', which says the Son is of one being with the Father, pointed back to this council."

### Card fields

None.
