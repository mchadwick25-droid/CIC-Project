# Card check: Marcionism (`marcion-marcionism`, tradition)

**Verdict: FIX.** Four changes, below. Everything else in `marcion-marcionism.card.json` and the **Entry fields** of `Card_Edits.md` passes as written.

## Fixes

1. `documentedStories[0].sources[0].note` (Eusebius, Church History IV.15.46). This is the same fault edit 3 corrected in the text: Eusebius does not call Metrodorus a presbyter, and he hedges (E-en 23679-23681: "who appears to have been a proselyte of the Marcionitic sect"). The new Pionius line carries the presbyter.
   - Old: "Metrodorus the Marcionite presbyter burned with Pionius."
   - New: "Metrodorus, who appears to have been a Marcionite, burned with Pionius."
2. `uncertain[4]` (the marriage rule). The held print says "destruction", not "corruption" (ANF5 15388-15389: "in affirming marriage to be destruction"). Hippolytus's Greek is not held.
   - Old: "Hippolytus says Marcion called marriage corruption, thinking to grieve the maker by abstaining."
   - New: "Hippolytus says Marcion called marriage destruction, thinking to grieve the maker by abstaining."
3. Entry field `end` (for release; Card_Edits left it open).
   - Old: `300`
   - New: `450`
   - Why: 300 contradicts the finished brief ("For about three hundred years"; "In the fifth century Theodoret ... eight villages") and the held sources: Cyril in the fourth century (Cyr 20353-20355), Epiphanius's "still now" in Rome and Italy (Epi 7466-7472), and Theodoret's Letter 81, written after "Five and twenty years" as bishop (Thdt 31501-31502, 31511). Jackson's reckoning puts the consecration in 423 (Thdt 2606-2607), the date the `theodoret-of-cyrrhus` entry already uses, so the letter falls about 448. Part 1 says a date that rests on one editor's reckoning is given only as roughly as the old sources allow. So the axis takes the round mid-fifth-century year, in the census's tradition form (Montanism 400, Manichaeism 650), and the shown `dates` read "5th c.", not a year. The span 140-450 matches the brief's "about three hundred years".
4. Entry field `livingEvidence.basis` (for release). Once the `legacy` edit lands, the entry's text no longer says the churches faded. The outline's Do not say also bars any claim that they died out ("no source tells their end").
   - Old: "The entry's own text says the churches faded and that nothing descends from them."
   - New: "The entry's own text says that nothing descends from them."

## Rulings on the dates

- **"by tradition in 144", dropped from `why`:** passed. The outline's Do not say bars any year for the break ("no held old source fixes it"). The finished brief says only "in the middle of the second century", and Part 1 keeps a claim the brief no longer makes off the entry. `uncertain[0]` carries the open year in Tertullian's voice.
- **Fifth century, in `dates` "2nd-5th c.", `teaser` and `relationsSummary`:** passed. The brief says "In the fifth century" (Theodoret). The outline's Setting rates "the fifth century" Widely Accepted (Thdt 31501, 31511). "2nd-5th c." is the census form for a span of centuries.
- **`start` 140:** stands, not changed. No held source gives 140, but none contradicts it either. Tertullian puts Marcion "in the reign of Antoninus for the most part" (ANF3 21334-21335, that is 138-161), and the brief says "the middle of the second century". The year no longer appears in any shown text. It sits before `marcion-of-pontus` (150), which is told within this entry. It is an axis position, not a claim, and it is not clearly wrong.
- **`end` 300:** clearly wrong. Fix 3 corrects it.

## Checks

1. **Edits against evidence:** each `Card_Edits.md` edit was re-read at its lines: E-en 23677-23681, 29119-29123, 29924-29930, 40459-40474, 47044-47058, 66158-66164, 28967-29199; Pion 5561-5563, 5584-5604, 5644-5658; ANF1 33572-33591; ANF3 898-901, 21331-21370, 23410-23420, 24445-24464, 24533-24542; Kr 16284-16289; Oe 4954-4958; ANF2 35336-35343; ANF5 12052-12061, 15385-15393, 38505-38552; CypLat 14582-14587; Epi 7466-7474, 7684-7755, 7890-7899, 8272-8283; E-gr 9657-9665, 24593-24599; VC-gr 13031-13041; Cyr 20270-20274, 20348-20362; Ephr 1585; Chrys 24417-24430; Thdt 17540-17546, 31490-31516, 33158-33167, 35004-35011, 35162-35167. All of them hold, except the two the card writer did not touch (Fixes 1 and 2).
   - Ephrem's "pray more than Daniel" stands at Ephr 1585: "they pray more than the righteous, as they say", set against Daniel's three times a day.
   - Every item the outline, review and fresh read send to the card is on it. The Lebaba inscription is rightly left off, since it is held only in Harnack's damaged modern print.
   - Modern works sit only in `modernWorks`, and each note says what the work covers.
2. **Fields not listed:** every field not listed in `Card_Edits.md` matches `Card.existing.json` word for word (checked by script). Those fields are `why`, `sourcing`, `floorNote`, `relationsSummary`, `teaser`, `voices`, `people`, and the documented story's `title`, `when`, `tier`, `verification` and `teaser`.
3. **`briefReferences`:** eight lines, one for each paragraph. Each names only what the brief tells.
4. **Census rules:**
   - There are four `quotationOriginals`, one for each quoted span in the brief, and each `modern` is verbatim in the brief.
   - Each `printed` and `englishPrinted` stands verbatim at its file and lines, checked by script with tags and notes stripped. Each of those files is in `sources.about`, and all sixteen files exist.
   - Kroymann's "statira" is confirmed as *statim* by Oehler, so the Latin may print. The Greek at Pion, E-gr, VC-gr and Epi was checked by hand.
   - British spelling appears only in printed wording ("neighbourhood"). No audit or ruling is named.
   - Validator: the full run was killed for lack of memory. `node tools/validate-census.mjs --skip-quotes` on a scratch copy outside the repo gives 0 errors and the same 4 warnings as the live census. That copy has the card merged, the brief as `longDescription`, the Entry-field changes, and Fixes 3 and 4. The quotes were checked by hand in its place.
   - The validator's quote pass reads straight double quotes only. Every double-quoted span in the card prose stands in a cited file.
5. **"checked at card":** "one Holy Catholic Church" is Gifford's "And in one Holy Catholic Church" (Cyr 20356-20357), with the leading "And in" dropped. The rendering is faithful. Cyril's Greek is not held.
6. **Not found:** the list in `Card_Edits.md` is accurate. I found no further claim that is clearly wrong apart from Fixes 1, 2 and 4.
   - The stale `documentedStories[0].verification` stays flagged for release, as the same case on other cards is tracked in `Open-Gaps.md`.
   - The caveat's "of which the Acts of Pionius survive" rests on comparing two held old texts: Eusebius IV.15.47 summarizes the contents of his Pionius document, and those contents match Gebhardt's Acts. It is Widely Accepted, and it passes.
7. **Census entry:** none (a tradition). The `atlasId` I.20 is unchanged.
