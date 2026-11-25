# Card check: Syriac Christianity (`syriac-edessa-nisibis`, tradition)

Checked `syriac-edessa-nisibis.card.json` and `Card_Edits.md` against `Card.existing.json`, the brief, `Outline.md`, `Review.md`, `Craft_Pass.md` and `Craft_Check.md`. There is no `Fresh_Read.md`. The fresh reads that exist (`Fresh_Listen.md`, `Fresh_Trust.md`, `Fresh_Trust_Second.md`) send nothing to the card. Nothing was edited. Nothing was committed.

## Verdict: FIX

The card needs five exact changes, set out below. Everything else passes.

## What passes

- **Nothing else moved.** Compared key by key with `Card.existing.json`, only these differ: `voices[2]`, `voices[4]` and `voices[5]`; `legacy` paragraphs 1 and 2 and the new paragraph 5; the Eusebius and Chronicle notes; `file` added to sources; nine sources added; three modern works removed; and three new keys. Each is listed in `Card_Edits.md`. Every other field is word for word, and the key order is kept.
- **Edits 1-7 are justified.** Edit 1 rests on Addai 65 and Do not say. Edit 2 rests on Chronicle 77 ("In the year 649, died Mar Jacob") and Theodoret, at lines 11124-11177. Edit 3 rests on Do not say, against the claims that women sang Ephrem's hymns and that they served in the church. Edit 4 rests on the slate's Inferential-Thin line. Edit 5 is the same change as edit 1. Edit 6 rests on Addai's own Abgar story. Edit 7 rests on Review B1.
- **Every item sent to the card is on it.** Cut first 1, 3, 4, 6-10 and 15-30 are there, along with What came of it 2-4, the Connection card line, and the Review MINOR item on the flood's year (`uncertain` c). The one exception is the Pearl item: see fix 4. Leaving out the "single one" item is upheld. Part 1 keeps a claim that rests only on modern work off the card.
- **The census rules hold.**
  - The scratch copy (outside the repo) gives 0 errors and the same 4 warnings as the live census.
  - The validator skips a tradition's quotations, so I checked them with my own script, using the validator's fold rule. All five `printed` texts stand at their files and lines: 25950-25953, 13733-13734, 1205, 1205 and 16165-16166. Each of those files is in `sources`.
  - The brief has five quoted spans, each with one entry, and no entry is left over.
  - Every quoted span in the card's prose stands in a cited file: "readers and daughters of the covenant.", "dead and buried within her,", "third peril", the Sozomen birthplace, "still in the hands of some.", "mounds and weapons and waves encircle me," and the taunt.
  - Quotation marks balance. No audit, review or ruling is named. The spelling is American.
- **No blind reading is claimed.** The four quotations of six words or more carry no `secondReading`. "prays with Satan." is the only `"checked at card"`. Mitchell 1205 prints "he who prays with the Manichaeans prays with Satan", and the rendering matches it exactly.
- **The French and Latin hold.** "les prêtres, les chefs et toute la sainte alliance" matches its rendering clause by clause. Parisot's *Sponsus meus* (18130-18134) supports "my bridegroom".
- **Rabbula's years are held.** "(411–435)" is not a modern date: Chronicle 145 has "The year 723, Rabula became bishop", and Chronicle 161 has his death in August of the year 746.
- **The entry fields pass,** except fix 5. These are `why`, `relationsSummary` and `modernWorks` (edits 13-15). Each modern work's `note` says what the work covers.

## Fixes

**1. `voices[6]`.** The writer flagged a "historians" opinion here. Ruling: remove it. It is a modern opinion stated as content, and "341 by the traditional count" is a modern reckoning too. The held acts (Braun 1302-1305) give no year of death at all. They date the start of the persecution in two ways that do not agree.
- Old: " His death opened the twenty-year vacancy the Persian church endured. The year itself is disputed: 341 by the traditional count, with some historians arguing for 344 instead."
- New: " His death opened the twenty-year vacancy the Persian church endured."

**2. `legacy`, paragraph 2.** The writer flagged a "historians" opinion here. Ruling: remove it, because it is a modern opinion stated as content. Rabbula's years stay (see above).
- Old: "Tradition credits Bishop Rabbula of Edessa (411–435) with the change; historians dispute whether he caused it or only presided over a shift already under way."
- New: "Tradition credits Bishop Rabbula of Edessa (411–435) with the change."

**3. `sources`, "Tatian, The Diatessaron" note.** This is clearly wrong and was left in. It makes the same claim that edits 1 and 5 corrected (Do not say, line 145; Review B2). Addai 65 is the only old witness.
- Old: "A single continuous gospel woven from all four, used as the standard gospel text in Syriac churches for centuries."
- New: "A single continuous gospel woven from all four, which Edessa's later founding story pictures its people hearing read."

**4. `sources`, the note on the Nativity, Epiphany and Pearl hymns.** Outline Leave out sends these hymns to the card for their teaching through symbols. The note does not carry that. Its words "not drawn on by the story" describe our process, not the work. The new wording quotes `npnf213` line 21795, a file the card already cites.
- Old: "More of Ephrem's teaching hymns, in the same volume as the Nisibene Hymns; not drawn on by the story."
- New: "More of Ephrem's teaching hymns, in the same volume as the Nisibene Hymns; in The Pearl he sees in a pearl \"mysteries pertaining to the Kingdom.\""

**5. Entry field `modernWorks`, the Brock item (`Card_Edits.md` edit 14).** The year is wrong for the series given. Cistercian Studies 124 is the revised edition of 1992; the 1985 edition was printed in Rome and was not in that series.
- Old: `"year": "1985"`
- New: `"year": "1992"`

## Not found, and what else was left in

- The not-found list in `Card_Edits.md` is accurate. Rabbula's years should come off it, since they are held (Chronicle 145, 161).
- The Peshitta clause in `legacy` paragraph 2 rests on no held old line. The only held mention, at `anf09` 1914-1920, is a modern introduction. It is not clearly wrong, so it is left as not found.
- The Bardaisan and Arendzen notes say Ephrem's hymns were written to answer Bardaisan. That fits Sozomen 32085-32103. Upheld as left.
