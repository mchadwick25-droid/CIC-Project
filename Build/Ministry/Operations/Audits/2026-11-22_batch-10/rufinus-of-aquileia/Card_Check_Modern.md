# Rufinus of Aquileia: card check, the modern pass (2026-11-23)

Checked `rufinus-of-aquileia.card.json` against `Card.pass3.json`, the **Fourth pass: no modern opinion (2026-11-23)** edit list in `Card_Edits.md`, and `rufinus-of-aquileia.brief.txt` as it now stands. Role: `Brief-Kit/roles/card.md`, check pass. Every cited line was opened.

**Verdict: FIX** (seven changes).

## The "about 390" substitution

The writer is right that N203 46255-46260 does not hold "the 390s": those lines give 374, 378, 381 and 397, and no decade. But the decade the brief cut is held elsewhere in Fremantle. It is the date of the dispute at Jerusalem:

- Fremantle's chronology: "a.d. 392: When Aterbius began the Origenist troubles at Jerusalem" (N203 44175-44176).
- A note to Rufinus's Epilogue to Pamphilus, in Fremantle's translation: "Epiphanius, whose anti-Origenistic sermon at Jerusalem in the year 394 greatly irritated the Bishops John and Rufinus" (N203 45640-45642).

Richardson's note (N203 42466, "Born 345, at Jerusalem about 390, died 410.") makes a different claim. It dates Rufinus's time at Jerusalem, not the dispute. It also sits badly with Fremantle's own reckoning that Jerusalem was his home for eighteen years, until 397 (N203 44097). So it does not stand in for the date the brief cut. The `Card_Edits.md` "Not found" note is also wrong: the 390s are held, at the lines above.

## The changes

1. **`uncertain[21]`** (the dispute's dates).
   - Old: `Richardson's note to Gennadius puts Rufinus at Jerusalem about 390. These dates are the editors' reckoning.`
   - New: `Fremantle dates the start of the troubles over Origen at Jerusalem, under Aterbius, to 392, and a note in his translation of Rufinus puts Epiphanius's sermon against Origen at Jerusalem in 394. These dates are Fremantle's reckoning.`

2. **`briefReferences[12]`** (clearly wrong). In Apology III.33, Jerome addresses Rufinus as "you". The one he translated the letter "for" is Epiphanius, the man who "wrote you down a heretic" (N203 55923-55927). The brief says "Jerome put it into Latin for the bishop".
   - Old: `Jerome, Apology against Rufinus III.33: he translated for Rufinus the letter in which Epiphanius wrote him down a heretic;`
   - New: `Jerome, Apology against Rufinus III.33: he translated for Epiphanius the letter in which Epiphanius wrote Rufinus down a heretic;`

3. **`briefReferences[1]`** (Fremantle's Prolegomena): remove the whole entry. What is left of it no longer matches anything the brief draws on. The brief no longer tells an estrangement. Its peace rests on Jerome's Apology III (`briefReferences[12]`, N203 55557-55560). Its unnamed friend rests on Rufinus's preface (`briefReferences[4]`). "Meant to show Jerome as his forerunner" is Fremantle's reading of Rufinus's intent, which the brief does not tell. The outline says nothing in the story rests on the editors (Outline.md 88). The estrangement and reconciliation are already credited to Fremantle in `uncertain[21]`.
   - Old: `W. H. Fremantle, Prolegomena on Rufinus: Rufinus and Jerome close friends in youth; estranged over Origen in Palestine and reconciled before Rufinus left; the preface to On First Principles meant to show Jerome as his forerunner.`
   - New: (entry removed)

4. **`datesNote`**: the year 410 for the Numbers preface is the note's date (N203 58972-58975, "Written in 410", with "The date is fixed by the burning of Rhegium"). It is credited to no one.
   - Old: `in Sicily in 410, when he wrote his preface to Origen on Numbers;`
   - New: `in Sicily when he wrote his preface to Origen on Numbers, in 410 by a note to Fremantle's translation;`

5. **`briefReferences[0]`** and **`briefReferences[13]`**: "the editors' heading" credits no one by name. The 1893 Jerome is W. H. Fremantle's edition (N206 527-530). The headings are at N206 3759 ("Written from Antioch, 374 a.d.") and N206 24629 ("The date of the letter is a.d. 409 or 410").
   - Old (`[0]`): `written from Antioch by the editors' heading:`
   - New (`[0]`): `written from Antioch by the heading in Fremantle's edition:`
   - Old (`[13]`): `dated 409 or 410 by the editors' heading:`
   - New (`[13]`): `dated 409 or 410 by the heading in Fremantle's edition:`

6. **`uncertain[17]`** (same date, same reason).
   - Old: `Jerome, in a letter his editors date to 409 or 410,`
   - New: `Jerome, in a letter Fremantle's edition dates to 409 or 410,`

7. **`uncertain[19]`** (same reason).
   - Old: `The editors of the 1893 translation head it "Written from Antioch, 374 a.d.",`
   - New: `W. H. Fremantle's 1893 translation heads it "Written from Antioch, 374 a.d.",`

## Checked and sound

- **Nothing else moved.** A JSON diff of `Card.pass3.json` against the card shows only the listed edits: `briefReferences` 0, 1, 10 (McGiffert) and 11 (ANF4) removed, the Numbers and Epiphanius entries changed, Gennadius 17 added, and `uncertain` 19 to 25 added.
- **Lines re-read and holding:** N206 3759-3760; N203 44027-44030, 44222, 44366-44368 (the quoted "This book closed the controversy. Rufinus did not reply, Jerome did not relent." is verbatim), 44447-44449, 46255-46260 (sides and 397), 58972-58975, 59013-59015, 55557-55560, 42466-42474, 38477-38480; N201 5232-5233; ANF4 22122-22124, 21996-22002.
- **`uncertain` 20, 22, 23, 24 and 25**: each modern view is credited by name (the Ante-Nicene Fathers, 1885; Fremantle; McGiffert, 1890; Richardson, 1892) and marked as modern or as the editors' own. In `[24]`, Richardson's 410 for the death holds at N203 42466.
- **`briefReferences`**: after change 3, every entry names something the brief still tells. The new Gennadius 17 entry matches brief line 15.
- **`quotationOriginals`**: the brief still quotes the same three spans, and each `printed` is unchanged and verbatim.
- **Rules.** The keys are the census keys, no audit is named, and the spelling is American (the title "Defence of Origen" in `uncertain[4]` is unchanged from the starting card).
