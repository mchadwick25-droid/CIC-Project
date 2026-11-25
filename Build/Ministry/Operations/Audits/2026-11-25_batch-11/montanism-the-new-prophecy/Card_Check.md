# Card check: Montanism, the New Prophecy (`montanism-the-new-prophecy`, tradition)

Checked: `montanism-the-new-prophecy.card.json` and `Card_Edits.md`, against `Card.existing.json`, the brief, `Outline.md`, `Source_Sheet.md` (G7), `Review.md` and `Fresh_Read.md`, with each cited line re-read in its file.

## Verdict

**FIX.** Four changes, set out below. With them made, the card passes. Separately, its placement on a tradition entry is held for Mark before release (see Placement).

## What was checked

1. **Edits against their evidence.** Corrections 1-8 each stand on their lines. Correction 1: PanH 17218 reads »μετ᾽ ἐμὲ προφήτης οὐκέτι ἔσται, ἀλλὰ συντέλεια«, and HE 29880-29890 gives her predictions of "wars and anarchy". Correction 2: HE 29823-29878 names no place. Correction 7: ANF03 15819-15820 reads "probed". Correction 8: ANF05 13127-13130 and 13136-13138. Corrections 3-6 follow from 1. The `why` and `teaser` changes stand on HE 29577-29579 and HE 30275, and the brief's "in the second century". The 2000 finding is gone. The Trevett and Heine lines moved word for word. Every outline item marked card (Cut first 1-12, Leave out, Brief cuts 3-4, What came of it 2, 4 and 5, beat 4's Holl and Oehler, Ending 2) is on the card. The review and the fresh read send nothing to it. Each `modernWorks` note says what the work covers.
2. **Nothing else moved.** A field-by-field diff against `Card.existing.json` shows only the changes listed.
3. **`briefReferences`.** Thirteen lines, each re-read. Two name what the brief does not tell (FIX 2 and 3).
4. **Census rules, by hand, since `tools/validate-census.mjs` runs `checkCard` and `checkQuotes` only for a person or a council.** A scratch census, kept outside the repository, carried the card fields and brief on the entry: 0 errors. The same fields were then run as a person card, so the card and quote checks would run. All three `printed` and the `englishPrinted` stand at their lines. Each `modern` matches its span in the brief, all three spans are covered, and every cited file is in `sources`. No card prose carries a straight-quoted span. The only errors were the expected ones. `secondReading` is absent on all three: correct, since no second reading has run and none is claimed. Q2 and Q3 are renderings from the Latin and Greek, not a held English. Keys are allowed and no audit file is named. Spelling is American, except "colour" in the existing sister story's 'tender and lucid and of the colour of air'. That field is unchanged, and the writer lists the phrase as not found.
5. **Q3's Greek, by hand.** I checked PanH 18758-18764 against the rendering. ἐν ἰδέᾳ γυναικός / in the form of a woman; ἐσχηματισμένος ἐν στολῇ λαμπρᾷ / clothed in a shining robe; ἐνέβαλεν ἐν ἐμοὶ τὴν σοφίαν / put wisdom into me; ἀπεκάλυψέ ... τὸν τόπον εἶναι ἅγιον / showed me this place is holy; ὧδε ... κατιέναι / comes down here. Nothing is added. φησί is dropped as a speech tag. Oehler (PanO 3281-3287) confirms the reading, and its Latin (3357-3358) confirms τόπον, so printing the Greek is right. No quotation is under six words, so none is "checked at card".
6. **Not found.** Each listed item is truly unsupported in the held files and none is clearly wrong, so they stay. The same holds for the documented stories' `when` years. No held source gives them, and they were not proposed new.
7. **Entry fields.** The `why`, `teaser`, `floorNote` and `modernWorks` changes pass. The `relationsSummary` and `start` rows ("not changed") pass. `dates` and `end`: FIX 4.

## FIX

**FIX 1. `uncertain[10]` ("Women among them"). This moves Epiphanius's doubt onto the wrong detail.** He says "I do not know clearly whether among them or among the Phrygians" of the women called prophetesses (PanH 18766-18768). The women bishops and presbyters and the seven virgins come later, at PanH 18826-18834, and he states them of the Quintillians without doubt.
- Old: `He is not sure whether this was among them or among the Phrygians.`
- New: `He says their women were called prophetesses, though he is not sure whether this was among them or among the Phrygians.`

**FIX 2. `briefReferences[3]`.** The brief does not say "maturity". The lines (ANF04 2709-2741, "the direction of discipline") hold the brief's "called the church to a stricter life".
- Old: `the Paraclete as the Spirit Jesus promised, leading the church to maturity;`
- New: `the Paraclete as the Spirit Jesus promised, calling the church to a stricter discipline;`

**FIX 3. `briefReferences[4]`.** The brief does not name Ancyra.
- Old: `the elder disputing with them at Ancyra while the movement was new.`
- New: `the elder disputing with them while the movement was new.`

**FIX 4. Entry fields `end` and `dates` (`Card_Edits.md`, Entry fields table).**
- **`end`: the 565 row is struck.** No held source gives 565. It is the year Justinian died, and the writer chose it as the end of his reign. It dates no Montanist event, and nothing in the held record says the movement lasted to it. The brief and the outline's Setting give only "in the sixth century, under Justinian". A year no held source gives may not be proposed (CLAUDE.md, "never invent"; Kit Part 1 on dates). The old 400 is contradicted by Sozomen (NPNF202 30574-30577) and Procopius (Proc 2195-2197), but the card cannot replace it with a year no source holds. So `end` is not changed by this card. It is flagged for Mark with `start` 165: the timeline needs a year, and setting timeline years for a span the sources give only by century is a fleet-level call (precedent: `2026-11-24_references/epiphanius-of-salamis/Card_Check.md`). One option for his ruling, not proposed here: the census's own practice for century spans, such as `manichaeism` "3rd-7th c." with `end` 650, and `ebionite-nazoraean-current` "1st-4th c." with `end` 400.
  - Old row: `| end | 400 | 565 | Same evidence; the held record's last dated event falls under Justinian, whose reign ended in 565 (Widely Accepted). The axis needs a year; if a looser one is preferred, this is Mark's call. |`
  - New row: `| end | 400 | not changed | No held source gives a year for the end: the brief and Setting say "in the sixth century, under Justinian". 400 is contradicted by Sozomen (NPNF202 30574-30577) and Procopius (Proc 2195-2197). The axis needs a year: flagged for Mark, with start. |`
- **`dates`: the substance passes.** The second century and the sixth are both held, in the brief and the Setting. The form changes to the census's own form for century spans: "2nd-3rd c.", "3rd-7th c.", "4th-6th c.".
  - Old: `2nd-6th century`
  - New: `2nd-6th c.`

## Placement (for release, not a card fix)

A tradition has no `card` key. On the entry, the new `sources` object (`ownWords`/`about`), `uncertain`, `briefReferences` and `quotationOriginals` are not checked by the validator. `Build/tools/generate_tree_pages.mjs` also does not render them for a tradition: it reads a tradition's top-level `sources` as a list (`formatSourcesList`), so an object there would print "No sources recorded." Release should not merge these four fields as they stand. Mark must first rule where a tradition's card lives, and the validator and page builder must then read it. The card's content is ready for whatever home he picks.
