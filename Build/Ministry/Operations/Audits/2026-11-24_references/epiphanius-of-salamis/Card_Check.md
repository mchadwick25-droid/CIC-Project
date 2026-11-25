# Card check: Epiphanius of Salamis

Checked: `epiphanius-of-salamis.card.json` against `Card.existing.json`, with `Card_Edits.md`, the brief (744 words), `Outline.md`, `Review.md`, `Fresh_Read.md`, Part 1 of the kit, `kinds/person.md` and `roles/card.md`. There is a starting card and a census entry already (`atlasId` I.91), so no new entry is written.

## Verdict

PASS

## What was checked

1. **Edits against their evidence.** A field-by-field diff of the two cards shows exactly the changes `Card_Edits.md` lists (edits 1 to 19), and nothing else. I re-read each cited line in its file:
   - Edit 4. Jerome, Against John 11 (J6 41010-41014: "my voice, too, condemns that heresy", spoken of the Anthropomorphites). Sozomen on the earlier charge (SS 43503-43505). This replaces A. C. Zenos's modern note, which was cited as the witness, with the old witness it points to.
   - Edits 6, 7 and 8, the items the outline sends to the card:
     - Apollinaris: PG42 48831-48833 and 48852-48857.
     - Besauduc, the Cypriots' choice and the old monastery: SS 39793-39799, and J6 18734-18736 in Letter 82, which confirms the new `sources.about[2]` title.
     - The Jerusalem mockery and the crowds: J6 40982-40996.
   - Edit 9. Letter 90, from Theophilus to Epiphanius: J6 19694-19733.
   - Edits 1, 2, 3 and 5 take out dates and an identification that only modern works make:
     - "the 390s", which only editors' chronology gives.
     - Richardson's years: J3 41528, an endnote.
     - "about 428": AUG 1098, the editors' note.
     - "at Charlemagne's order": MEN title line only.

     Each new wording stands on old lines: the regnal date at HOLL1 13427-13429, the death at sea, and "extreme old age" at J3 41531-41533.
   - Every item in the outline's **For the card, not the story** is on the card. Q3 stays as the existing paraphrase in `uncertain[10]`, without quotation marks, since the brief does not quote it. `Review.md` and `Fresh_Read.md` send nothing to the card.
2. **Nothing else moved.** Every unlisted field is word for word.
3. **`briefReferences`.** The three items the brief no longer tells were taken out or moved to the card's other fields: Apollinaris, the mockery and crowds, and the birthplace. Each remaining entry names something the brief tells.
4. **Census rules.**
   - I put a scratch copy of the census, with this card, the brief as `longDescription` and the new teaser, through `node tools/validate-census.mjs` with the full Library quote check: 0 errors.
   - With the proposed `modernWorks` added (`--skip-quotes`): 0 errors.
   - `tools/list_second_readings.py`: 2 spans, both carried.
   - `quotationOriginals` has one entry for each of the brief's two quoted spans, and each `modern` matches the brief word for word.
   - Q2 `printed` is verbatim at J6 10920-10922.
   - I checked Q1's Greek by hand against HOLL1 12387-12391. It is verbatim, apart from the three scan slips that its `uncertain` names and `tools/quote_scan_readings.json` lists (TE, zal, χ). The scan also has a page mark "|" before ἐμπίπτειν.
   - Every cited file is in `sources`. No audit file is named, and the spelling is American.
5. **"Checked at card".** None. Both quotations run to six words or more and already carry `secondReading` "same".
6. **Not found.** The year 754 in `uncertain[11]` is not found in any held line; MEN has no "754". It stays where it is, as the role directs. Nothing I found is clearly wrong and left in.
7. **Entry fields.**
   - The teaser change has the same evidence as edit 1.
   - The `modernWorks` are the works in the outline's "Modern, clarifying an old text". Their titles, editors and translators come from the held title pages and headers: Holl and Hinrichs 1915, SPCK 1921 for Moore, Painter 1850 for Mendham, T&T Clark and Eerdmans for NPNF, and Zenos, Hartranft, Fremantle, Lewis and Martley. Each note says what the work covers.
   - No `atlasId` question arises.

## Considered, not a FIX

- **Q1's Greek, held only in Holl's scan.** The outline planned English alone unless the Greek was confirmed. The slips are three single-letter OCR misreads, the reading is unambiguous, and each slip is registered and named on the card. No printed English is held to stand alone. The existing, earlier-checked card kept the Greek, and Mark's ruling for this batch keeps approved wording that passes. It stays.
- **The entry's `dates`, `start`, `end` and `activeYear`.** They rest on Richardson's years only. The writer flagged them for Mark rather than changing them, which is right, since a rule for timeline years is a fleet-level call. `uncertain[4]` ("His dates are Richardson's reckoning") still describes them truly.

## Follow-up check (2026-11-25)

PASS.

- **Edit 20, `briefReferences[6]` (Letter 51).** Supported: J6 10676-10680 (the monastery of "the reverend presbyters, Jerome and Vincent"), 10703-10705 (the letter to the presbyters and brothers of that monastery, and "For a year before I had heard many of them complain that they had no one to celebrate for them the sacraments of the Lord"), and 10662-10665 ("the fear of God which has compelled me to act in this way ... I have simply made provision for the wants of the Church"). It matches the brief's paragraph on Jerome's brother. It keeps the list's old shape and reads cleanly. No quotation marks, no modern opinion or date.
- **Edit 21, `briefReferences[7]` (Letter 90).** Supported: J6 19745-19747 ("a few men have been expelled from the Church", with joy "throughout all Egypt"), and 19717-19719 for the Origenist monks of Nitria. It matches the brief: "he had put a few monks who followed Origen out of the church in Egypt." It reads cleanly before "and the call to gather the bishops of Cyprus." No modern opinion or date.
- **Nothing else moved.** `git diff` against HEAD shows only these two lines of the card changed. `briefReferences[8]` (Socrates on "the monks he had driven out") is Socrates's account, which the brief tells as his. `uncertain[7]` reports the letter at J6 10657-10659. Neither conflicts.
