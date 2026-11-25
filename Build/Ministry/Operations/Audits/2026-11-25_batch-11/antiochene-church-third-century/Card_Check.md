# Card check: The Church of Antioch in the Third Century

Checked: `antiochene-church-third-century.card.json` and `Card_Edits.md`, against `Card.existing.json`, the brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, Part 1 of the kit and `kinds/tradition.md`. There is no entry file, since the tradition already has its own census entry.

## Verdict

FIX

## What holds

- **Nothing else moved (check 2).** Field by field against `Card.existing.json`, only `sourcing`, `voices[0]`, `voices[1]`, `voices[4]` and `legacy` differ, and each is listed (edits 1-5). `why`, `relationsSummary`, `teaser` and `documentedStories` are word for word in the card file, and their changes are listed under Entry fields.
- **Edits 1-5.** Each one stands on its evidence: E-Eng 42173-42175 and E-Gk 11903-11904 (the charge); Thdt 40906-40911 against E-Eng 41993-41994 (who wrote the letter); E-Eng 42324-42330 (the ruling); Nic 5296-5306 (canon 19). Removing the Lucian-exegesis line agrees with the census edge (Inferential-Thin) and the Do not say.
- **Quotations (check 4).** There is one entry for each of the brief's three quoted spans, and none for a span the brief dropped. Each `modern` matches the brief exactly. No entry carries `secondReading`, and none needs "checked at card", since all three run six words or more. Each `printed` stands verbatim at its lines: E-Eng 42165-42168, Chrys 15435-15440 and Thdt 6063-6064. Each held original the outline renders from is carried: the Greek at E-Gk 11896-11900 and Epiph-Gk 45744-45746. Both Greek texts were re-checked by hand against the renderings, and both match. The Latin of Q3 was re-checked clause by clause, and it matches too. Both damaged scans are confirmed by a second held print (Rufinus 11951-11955 and McGiffert; Jackson).
- **Scratch census.** I merged the card fields, the brief as `longDescription` and every Entry-field change into a copy outside the repository. `node tools/validate-census.mjs <copy> --skip-quotes` gives 0 errors. The validator skips a tradition's quotations, so I also ran a scratch copy of it that checks them for this entry. All three `printed` pass. The two `original`s pass once the two scan readings in edit 6 are added. Both card-prose quotations stand in their files: "Paulianists" at Nic 5297 and "most equitably" at E-Eng 42326. The errors left are the ones release clears: `secondReading` is not yet set, and the brief's three renderings are not yet listed in `tools/quote_renderings.json`.
- **Other checks.** Every cited file is in `sources`. No audit file is named. The spelling is American.
- **`uncertain` a-k.** Each item was re-read at its lines and holds: E-Gk 11549-11550 and JerChr 44280-44287; Ath 58995, Hil 9772-9773; Ath 58970-58981 and 59053-59057, Hil 9607-9611; E-Eng 42084-42110 and 42178-42245; 41840-41851 and 42032-42042; 42290-42314; Thdt 40995-40998; Philost 138; Soz 31022-31035. Every item the outline sends to the card is on it: Cut first 1, 2, 3, 4, 6 and 7; Ruled 1, 2, 4 and 5; What came of it 2 and 3; D1-D4 and D6. The review and the fresh read send nothing to the card.
- **`briefReferences` (check 3).** All twelve match what the brief still tells.
- **Not found (check 6).** The not-found list is fair. `people[1].year` 268 can stay, since Jerome has Malchion flourish "under Claudius and Aurelianus" (Thdt 40911-40912).

## FIX

### Entry fields (for release)

1. `teaser`. A held source contradicts it. The bishops say that, since Paul is outside the faith, they will not judge his practices (E-Eng 42079-42084, 42262-42269). The writer used the same evidence for `why`.
   - Old: "A council removed the bishop of Antioch for what he taught and how he behaved, and could not make it stick"
   - New: "A council removed the bishop of Antioch for what he taught, and could not make it stick"
2. `relationsSummary`. This change replaces Card_Edits edit 12. Edit 12 puts Eusebius's word "ordinary man" into the bishops' charge, against the Do not say ("'ordinary man' is Eusebius's word (T1)"). The sentences around it are also a modern classification told as content: adoptionism and modalism as a "mirror" and as "opposite ways of refusing". "Modalism" and "monarchianism" are named without explanation (Part 1), and no census edge stands behind them.
   - Old: "Third-century Antioch was the seedbed of the fourth-century quarrel over the Son. Lucian's pupils led the Arian party. Three of them later taught Aetius, the first Anomoean teacher. Its tie to modalist monarchianism is a mirror, not a line of descent. Paul of Samosata taught adoptionism and Sabellius taught modalism. These were opposite ways of refusing the account of the Son that the century was working out."
   - New: "Third-century Antioch was the seedbed of the fourth-century quarrel over the Son. Lucian's pupils led the Arian party. Three of them later taught Aetius, the first Anomoean teacher."
3. `documentedStories[0].text`. It contradicts the finished brief ("Two generations later"). The role's rule is to correct the fewest words. It does not hold the fix over for another batch.
   - Old: "preaching on his feast at Antioch three generations later"
   - New: "preaching on his feast at Antioch two generations later"
4. `documentedStories[0].sources[1].note`. It names a modern translation. A modern work goes only in `modernWorks` (check 1).
   - Old: "The tradition of his one answer; PG 50:519–526, English in Wendy Mayer, The Cult of the Saints (SVS, 2006)."
   - New: "The tradition of his one answer; PG 50:519–526."
   - Add to `documentedStories[0].modernWorks`, after the Williams entry: `{"title": "The Cult of the Saints", "author": "Wendy Mayer", "year": "2006", "publisher": "SVS", "note": "An English translation of Chrysostom's Homily on the Martyr Lucian."}`
5. `documentedStories[0].caveat`. It states a modern opinion as content (check 1).
   - Old: "is asserted by Arius’ own party and disputed by modern scholars."
   - New: "is asserted by Arius’ own party."

### Card fields

6. `legacy`. Edit 5 adds a third thing after "Two things".
   - Old: "Two things went out of this council into the fourth century."
   - New: "Three things went out of this council into the fourth century."
7. `floorNote`. It sets Paul among the "monarchian currents", an identification only a modern work makes, and names "modalism" without explanation.
   - Old: "But Paul of Samosata's own teaching is a live, unresolved question about where the doctrinal line falls, distinct from the other monarchian currents of the period, such as Sabellius's modalism."
   - New: "But Paul of Samosata's own teaching is a live, unresolved question about where the doctrinal line falls."

### Card_Edits.md (evidence only; no card change)

- Item 9d: Basil's reason stands at Bas 27403-27407, not only at 27366-27368.
- Item 9j: Philost 178 holds the Aetius passage and supports nothing in `uncertain` j. It belongs to `relationsSummary`.
