# Card check: Manichaeism (`manichaeism`, tradition)

Card checker, batch 11 (2026-11-26), under the check pass of `Card_Prompt.filled.md`. I wrote neither the card nor the brief. Read: `CLAUDE.md` (Trust and source fidelity), Kit Part 1, `kinds/tradition.md`, the brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, `manichaeism.card.json`, `Card_Edits.md`, `Card.existing.json` and the census entry `manichaeism`. I re-opened every cited line in `cic/texts/`.

**Verdict: FIX** (nine changes, below). Everything else passes.

## What holds

- **Check 2 (nothing else moved).** A field-by-field diff against `Card.existing.json` finds changes only in `voices[0]`, `legacy` (the old text is kept whole and a new paragraph is added after it), `documentedStories[0].sources` (BeDuhn removed), and the new `sources`, `uncertain`, `briefReferences` and `quotationOriginals`. Every one is listed. `why`, `floorNote`, `relationsSummary`, `teaser`, `people` and the story text are word for word.
- **Edit 1 (`voices[0]`).** Justified. BIR 29125-29138 and FIH 5112-5128 give flaying, two halves on two gates, or death in prison. All three put the death at a Persian king's hands.
- **Edit 2 (`legacy`).** Holds at FIH 5406-5431 (Samarkand's five hundred, the threat, the head tax, Baghdad's three hundred and five), BIR 29140-29147, Ephrem 640 and Prosper 54712-54717 (a. 443).
- **Edits 3-7, 10, 11.** Each `sources` file holds what its note says. Every `uncertain` and `briefReferences` line I re-read stands at its lines: BIR 12375-12376, 29054-29171; FIH 4360-4404, 4445-4462, 4878-4898, 4933-4940, 5240-5244, 5383-5396; CTh 86093-86097, 87272-87278; ALX 24494-24498; Migne 7605-7714, 12871-12904, 16828-16840; NPNF 1/4 2438-2439, 2743, 3733-3735, 4312-4314, 4338, 4471, 4512, 4615-4616; NPNF 1/1 6163-6174, 6334-6346; Knöll 5732-5733, 7333-7336; CHI 4928-4933, 6877-6886, 8671-8673, 8750-8751, 12205-12208, 12230-12233, 12381-12387, 13695-13702, 13958-13961, 14089-14095, 14114; KHU 15395-15433, 15729, 16579-16672, 17106-17125, 17347-17357, 17364-17371, 17443. The four `modernWorks` and BeDuhn's move are right. Each note says what the work covers. All are pre-1931 prints except BeDuhn, which is listed for reading only.
- **Edits 8-9 (`why`, `teaser`).** Each change is justified by the outline's Do not say list. The teaser needs one further change (FIX 2).
- **Check 1, items sent to the card.** Every Cut first item marked card (1-6, 8-13, 15-19, 21-29, and 32's Old Testament) is on the card. So are Leave out's card items and What came of it 4-5 (the old legacy keeps the insult; the new paragraph has Ephrem). There is one exception: the Fihrist's coronation scene (FIX 3).
- **Check 3.** Each of the eight `briefReferences` matches a run the brief still tells. The cut details inside them are the ones the outline sends to the card.
- **Check 4.** There are six `quotationOriginals`, one for each quoted span in the brief, and none for a dropped span. Each `modern` matches the brief exactly. Each `printed` and `original` is verbatim at its lines: Migne 7666-7667; KHU 17443; NPNF 1/1 6345-6346 with Knöll 5732-5733; BIR 29121-29122; NPNF 1/4 4523 with Migne 16422-16436; KHU 17347-17357. Q2's damaged Latin is confirmed clause for clause by Stothert, so it may be printed. Every file is in `sources`. No audit file is named, the spelling is American, and the card's new prose carries no double quotation marks.
- **Check 5 ("checked at card").** "You were at our prayer." renders *Interfuisti orationi*. The "our" is carried by *nostram conversationem* before it and by Augustine's reply, *orationi vestre interfuerim* (7666-7667, 7692). "to the Bad Place." is in Le Coq's "go to the Bad Place." "angels and gods" renders *angelos et deos* and Pilkington's print. All three pass.
- **Check 6 (not found).** Each item listed is truly unsupported in the held files, and none of the factual ones is clearly wrong, so they stay. The judgments are another matter (FIX 5 and 6).
- **Check 7.** There is no new entry and no `atlasId`.
- **Census run.** I made a scratch copy of the census outside the repository, merging in the card's fields, the brief as `longDescription`, the new `why` and `modernWorks` items. The full `node tools/validate-census.mjs <copy>` run (no `--skip-quotes`) gives 629 movements, 736 edges, 0 errors and 4 warnings, all on other entries.

## Rulings on the writer's flags

- **`floorNote` "most scholars".** FIX 1. This is a modern opinion stated as content. Check 1 bars it anywhere on the card, and this batch's Antiochene check fixed the same fault in a `floorNote`. The doctrinal ground stays as it is: two powers without beginning against "maker of all things". The fix only says that ground plainly, from the brief and BIR 29069-29070.
- **`experienceToday` (the Fujian temple).** No change. It sits outside the card and outside this pass's fields. By design it is the entry's present-day place to visit, as on every entry (Mor Gabriel, Hippo, Timgad), and it makes no claim about the past. The outline's Do not say list governs the story and the card. Those are now clear, since the teaser's Fujian clause goes out under edit 9. Whether `experienceToday` should also meet Part 1 is a fleet-wide question for Mark, not a fix to this card.
- **`people[2]` (the Faustus line).** No change. The writer is upheld. The line stands verbatim at NPNF 1/4 4338, it is not wrong, and the role allows only "new" and "clearly wrong" edits. The outline's Q2 note ("which this story's card replaces") explains why Q2 is not already on the tree. It does not tell anyone to swap the people entry, and Q2 is carried in `quotationOriginals`.

## FIX

**FIX 1. `floorNote` (an entry field, for release).** A modern opinion, and an unexplained term.
- Old: `Co-original dualism denies 'maker of all things'; most scholars: a distinct universal religion`
- New: `Its teaching of Light and Darkness as two powers without beginning denies the creed's 'maker of all things'`

**FIX 2. `teaser` (the new text under edit 9).** "Hearers" is a label left unexplained in a short text (Part 1, Explain it).
- Old: `and whose Hearers' prayer of confession was kept in a cave library near Dunhuang.`
- New: `and whose lay followers' prayer of confession was kept in a cave library near Dunhuang.`

**FIX 3. `uncertain[2]`.** Leave out sends "Mani's appearance at Shapur's coronation" to the card along with the lamps, and only the lamps are on it. FIH 4414-4420 has Mani come out in public on the day Shapur was crowned. The meeting with Shapur comes later, after about forty years of travel (4445-4449).
- Old: `How King Shapur received him. The Fihrist, from what the Manichaeans said, has Shapur honor him`
- New: `How King Shapur received him. The Fihrist, from what the Manichaeans said, has Mani first come forward in public on the day Shapur was crowned, and later has Shapur honor him`

**FIX 4. `uncertain[0]`.** "Ashkanians" is unexplained (Part 1). The gloss is at BIR 11727-11733.
- Old: `whom he believes to be Ardawan, the last of the Ashkanians;`
- New: `whom he believes to be Ardawan, the last of the Ashkanians, the kings who held Iraq before Ardashir rose;`

**FIX 5. `voices[2]`.** "Most effective" is a judgment of praise in the narrator's voice that no old witness makes (check 1; Part 1, the four faults).
- Old: `then the movement's most effective Latin opponent, and`
- New: `then the movement's Latin opponent, and`

**FIX 6. `legacy` (first paragraph).** "One of the few extinct ancient religions" is a modern comparative judgment stated as content (check 1). The claim that remains rests on the held books (Biruni's quotations of Mani, the Khuastuanift).
- Old: `Because of all this, it is one of the few extinct ancient religions that can now be read largely in its own words.`
- New: `Because of all this, it can now be read largely in its own words.`

**FIX 7. `uncertain[4]`.** The card should use the tree's spellings, as the brief does: Shapur, Gundeshapur. "Sapor" reads as a different king.
- Old: `hung at the gate of Gundisapur;`
- New: `hung at the gate of Gundeshapur;`
- Old: `heard that he served under Sapor and was put to death`
- New: `heard that he served under Shapur and was put to death`

**FIX 8. `briefReferences[4]`.** The same spelling.
- Old: `the skin hung at the gate of Gundisapur, still called the Mani-gate`
- New: `the skin hung at the gate of Gundeshapur, still called the Mani-gate`

**FIX 9. `sources[9].note`.** The same spelling.
- Old: `on Mani's death under Sapor;`
- New: `on Mani's death under Shapur;`
