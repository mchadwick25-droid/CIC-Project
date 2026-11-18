# Card edits: Cyril and Methodius

Batch 4, 2026-11-18. No census person entry exists, so the existing card is the finished batch 1 card, `Build/Ministry/Operations/Audits/2026-11-17_varied-batch/cyril-and-methodius/cyril-and-methodius.card.json`. Brief: `cyril-and-methodius.brief.txt` (469 words, about 3 minutes).

## Keys (to pass `tools/validate-census.mjs`)
- `dates` → `datesNote`, `place` → `placeNote`: same words, renamed to the keys the census allows.
- `name`, `tradition`, `briefLength` dropped: not card keys (CARD_KEYS, validate-census.mjs line 205). No wording changed.

## New
- **sources.about**, two entries added, because the quotations cite their files and the validator requires each cited file among the sources: the Life of Constantine (Dümmler and Miklosich, 1870, `vita-constantini_...duemmler-miklosich1870.txt`) and Patrologia Graeca 126 (Migne, 1864, `theophylact-ohrid_opera-t4-...migne1864.txt`). Titles from each file's header.
- **quotationOriginals[2]** (Q1, cut down in the brief to its first sentence).
  Old: modern "Does God's rain not fall on all alike? Does the sun ... blind and deaf."; printed "nonne pluvia ... iubentes ?"; lines 20307-20310.
  New: modern "Does God's rain not fall on all alike?"; printed "nonne pluvia a deo aequaliter super omnes cadit?"; lines 20307-20308.
  Evidence: brief, "In Venice, his Life says, Constantine asked the Latin clergy: "Does God's rain not fall on all alike?""; VC 20307-20308 ("aequa-/liter" across the line end).
- **quotationOriginals[4]** (Salzburg).
  Old: modern ""Greek", with his "newly invented Slavic letters", had partly cheapened the Latin Masses in the people's eyes"; printed the whole sentence; lines "13641-13643, 13662-13663".
  New: modern "Greek ... newly invented Slavic letters"; printed "quidam graecus, methodms nomine, noviter inventis sclavinis Hlieris,"; lines 13641-13642. The `uncertain` note now gives the rest of the sentence ("vilescerc fecil cunclo populo ex parte missas et evangelia", 13662-13663) as what the paraphrase rests on, keeping "partly" (ex parte).
  Evidence: the brief quotes only "Greek" and "newly invented Slavic letters". The validator matches `modern` only against the brief's quoted spans and takes one line range only. The sentence is broken by a page of footnotes (GZ 13644-13661), so one range cannot hold all of it.
- **quotationOriginals[5]** (Q3). Old modern: "he who made the three chief languages, ...". New: "For he who made the three chief languages, ...". Evidence: the brief's quotation now begins "For"; printed "qüoniam" (GZ 13974) carries it. Printed and lines unchanged.
- **briefReferences** (numbers are the old card's):
  - [1] Old: "Rastislav's embassy; "you are Thessalonians, and all Thessalonians speak pure Slavonic"; the letters made." New: "Rastislav's embassy, with teachers from Italy, Greece and Germany; the emperor's word that all Thessalonians speak pure Slavonic; the letters made." Evidence: those words are not in the brief, so they cannot stand in quotation marks; the teachers from Italy, Greece and Germany are in the brief and in VM 12203-12205; Thessalonians, VM 12212-12213.
  - [4] Added "his illness;" (brief, "Constantine fell ill"; VC 20408).
  - [5] Added ", and his plea not to give up his teaching for the mountain" (brief, "Constantine asked him not to give up his teaching for its sake"; VM 12253-12255).
  - [6] "the Latin Masses." → "the Latin Masses and Gospels." (brief, "the Latin Masses and Gospels"; CONV 13662, "missas et evangelia").
  - New item: "Pope John VIII, letter of 879 to Methodius: the earlier ban on Slavonic Mass repeated, with preaching in Slavonic still allowed." (brief, "Pope John VIII repeated a ban on Slavonic Mass in 879"; J8 13799-13808.)
  - [8] Added "the funeral in Latin, Greek and Slavonic, with crowds rich and poor, free and slave;" (brief, last sentence; VM 12543-12551).
  - [9] Added "the younger priests and deacons sold, the teachers chained, then stripped and driven out;" (brief, "the younger disciples were sold as slaves, and the teachers were chained, stripped and driven out"; PG 98396-98397, 98428-98429, 98681-98682).
  - New item: "Editor's note to the Life of Clement, PG 126: its author says he lived with Clement and was Bulgarian, though the work carries Theophylact's name." (brief, "That Life was written in Bulgaria a generation or more later"; PG 96729-96746.)
  - New item: "Lützow, Bohemia: Rostislav's mission to Constantinople in 862, for the 860s." (brief, "It had begun in the 860s"; LUT 1297-1301.)

## Clearly wrong
None found in the card's own statements.

## Second readings, awaiting
The batch 1 card has no `secondReading` on any entry, so none is copied. All seven are left out and await second reading:
1. "if they have letters for their language." (unchanged)
2. "who can write words on water, and who wants to be called a heretic?" (unchanged)
3. "Does God's rain not fall on all alike?" (changed)
4. "Look, brother, we were partners ploughing a single furrow. And I fall in the field, having finished my day." (unchanged)
5. "Greek" ... "newly invented Slavic letters" (changed)
6. "For he who made the three chief languages, ..." (changed)
7. "the first bishop of the Bulgarian tongue" (unchanged)

Batch 1's `Second_Readings.md` (2026-11-17_varied-batch) records "same" for 1, 2, 4 and 7, and for 6 without "For". The second-reading step may use them.

## Left alone (no longer told in the brief, not wrong)
- briefReferences [4] "the pope comes out to meet them with Clement's relics", [8] "Wiching set up", [9] "the plain sermons", [0] "the letters made after prayer": each describes its source passage correctly.
- Not found: none. Ginzel's 863, Wattenbach's suspicion and the other claims were not re-traced line by line. None contradicts the brief or a source read here.
