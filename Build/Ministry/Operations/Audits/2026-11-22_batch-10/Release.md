# Batch 10 release

This release covers twelve stories that are already in the census: council-of-ephesus-431, eutyches, theodoret-of-cyrrhus, pelagius, john-cassian, john-chrysostom, rufinus-of-aquileia, frumentius, mesrop-mashtots, ulfila, priscillian and ephrem-the-syrian. There is no new person entry, so no tradition link was added. The census now holds the current text and card of all twelve. The index and pages were rebuilt from it.

## What changed

- **Cards** (`<slug>/<slug>.card.json`). Each `Card_Check.md` FIX was compared with the card by script and by hand. That covers both passes, including the Old/New pairs, the added items, Pelagius's replaced `quotationOriginals[0]` and Frumentius's two Greek originals. Every new text is in the card and no old text remains. Nothing needed applying. `Second_Readings.md` asks for no change to an `original`. Its 29 `secondReading` values were set, each placed last in its entry: 20 "same" and 9 "minor". Entries marked "checked at card" were left alone. Ephrem's "changes meaning" and Chrysostom's "same" stand as they were.
- **`cic-website/data/world-census.json`.**
  - For all twelve, `longDescription` is now `<slug>.brief.txt` with its final newline removed. For Chrysostom and Ephrem this is the revised text, not `brief.approved.txt`.
  - `card` is now `<slug>.card.json`. For Ephesus the `council` field takes the card.
  - Eutyches, by Mark's ruling: `toldWithin` is null; `lane` is "3 Greek East & Orthodoxy", `laneLabel` "Greek East & Orthodoxy" and `laneOrder` 3; he is removed from the `people` list of `cyrilline-miaphysite-egyptian-christianity`.
  - A field-by-field diff against HEAD shows no other change.
- **`tools/quote_scan_readings.json`.** Fourteen readings were added, each first checked to stand once at its lines:
  - Ephesus: 4 readings in Hefele 7244-7245.
  - Frumentius: 6 readings in PG 25 92806-92814.
  - Pelagius: 3 readings in PL 30 815-816.
  - Mesrop: T12 55858-55882 listed as a drop (`kind` "footnotes"). Its `lines_held` are the 19 footnote lines of notes (1) to (3), listed the way the file lists other dropped ranges.
- **`tools/quote_renderings.json`.** 31 listings were added (336 to 367):
  - The 29 spans in `Second_Readings.md`, each with `second_reading.record` set to that file and its verdict. Each original is the card's `originalFile`/`originalLines` where the card gives them, otherwise its `file`/`lines`.
  - Languages: Greek for Ephesus [3], Eutyches [0], Theodoret [3] and Frumentius [2], [3]. Latin for Pelagius ×3, Rufinus [2], Frumentius [0], [1], Ulfila ×2 and Priscillian [0]. French for Mesrop ×3. English for the rest.
  - Two "checked at card" spans that are not word for word in their files: Ulfila "alone unbegotten" and Cassian "the Conferencer" (see Judgment calls).
  - Ephrem's one existing listing still stands in his brief. No listing was removed.
- **`tools/validate-census.mjs`.** A scan reading that joins lines is now padded with blank lines, so the lines below it keep their numbers (see Judgment calls).
- **Rebuilt.** `cft-website/index.html` (atlas-sync) and twelve story pages. Also `cft-website/tree/cyrilline-miaphysite-egyptian-christianity.html`, which lost Eutyches from its people under the ruling. `corpus_coverage.py` left `corpus-coverage.json` unchanged. Nothing else changed.
- **Ledger.** `Earlier-Approved.yaml` lists no stories, so nothing was removed. `Story-Ledger.md` was regenerated: 98 of 272 are now on the kit (it was 86), and era 2 lists the twelve as batch 10.

## Judgment calls

- **The validator fix.** Frumentius's reading at 92813-92814, "βίον χατ- \nἔστησεν" read as "βίου κατέστησεν", joins two lines into one. `withReadings` spliced in the shorter text, so every later line in the PG 25 file moved up by one. That broke `athanasius-of-alexandria` at 97994-97996. The code comment said line order kept the readings above in place, but nothing kept the lines below. I padded the joined text with blank lines. This keeps Frumentius's reading as listed and fixes the cause, not this one case. After the fix the validator gave 0 errors, and all 110 tests pass.
- **Ulfila "alone unbegotten".** This is lifted from `arius` under the slate, from the same lines (Kauffmann 15310). It is listed against that span's own blind reading, `2026-11-17_batch-3/Second_Readings_3.md`, verdict "same", because this batch made none.
- **Cassian "the Conferencer".** This is our English of the title "Contra Collatorem" (N211 15774-15775), checked at card. It follows batch 9's handling of "checked at card" spans that are not verbatim: listed as Latin, verdict "same", record `Second_Readings.md`. No blind reading was made of it.
- **Theodoret [0]** is listed against the English it cites (npnf203 38007-38010). Our wording follows Mansi's Latin (B10-06), but the card cites no Mansi file. Batch 9 handled Hilary [0] the same way.
- **Running alone.** Commits b70622fe and the cross-batch scoring commits (46f7bf24 to 0308aafc) landed while this ran, so other sessions were active. The validator still ran to the end and was not killed.

## Checks

- `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json`: 629 movements, 736 edges, 10 eras, **0 errors**, 4 warnings (shortName length, none of ours). The first run gave 3 errors: the athanasius line shift, and the two checked-at-card spans above.
- `node --test --test-concurrency=1 tools/tests/validate_census_*.test.mjs`: 110 pass, 0 fail.
- `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`: both `"changes": []`.
- `node tools/build_tree_site.mjs`: 1775 own files, 173 shared, 0 mismatched.
- `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`: 77 pass, 0 fail.
- `python tools/check_live_commentary.py`: exit 0.
- `python tools/check_spelling.py --enforce --base origin/main`: the release's first run failed on 6 British spellings in 3 files. The coordinator fixed the cause (2026-11-23): "grey" in Eutyches's modern rendering and in his card's `sources` note is our English and became "gray" in the brief, the card, the census, `tools/quote_renderings.json` and the rebuilt page (the printed 1881 wording keeps "grey"); "counselled" and "persuaded" in Ephesus's note are the print's words and are now in quotation marks; and `englishPrinted`, the verbatim English print, is now skipped as `printed` already was (`tools/check_spelling.py`; its 39 tests pass). Final run: **0 British spellings**.
- `python -m engine.m1.profile_readability` on the twelve briefs: 12 graded, 0 failing. Grades run from 7.4 to 9.0. Cassian (7.8) and Pelagius (7.4) carry the under-8 listener-read note.
- `python tools/check_standard_lock.py --base origin/main`: exit 0. `Kit.md` and `roles/researcher.md` changed, with a Decision-Log entry carrying Mark's words (the cut-first line).

## Mark's rulings in this batch

| Ruling (Decision-Log, 2026-11-23) | Where it lives now |
|---|---|
| "Batch 10: the slate approved" ("Approve as recommended"): the twelve and halves, the research order, Eutyches's home kept for now, the quotes, no direct-line change | This batch only |
| "Batch 10 hearts approved, with the lengths and a cut-first line in the kit" ("Approve as recommend"): the ten hearts; 4:30 at most (675 words; the council 585) with a Cut first list; Eutyches to the river; Priscillian not "the first" | The cut-first line is in Kit Part 3, Length, and `roles/researcher.md` item 2. Eutyches to the river is in the census (this release). The rest is this batch only |
| "Batch 10: six drafts past 4:30, and Ulfila's creed" ("Approve as recommend"): the reviewer names the cuts to 675, the reviser makes them; the creed sentence stays barred | This batch only |
| "Batch 10: the fresh read, and the fixes after it" ("Approve as recommended"): the five failing stories get the fresh reads' exact changes; minors that change meaning are applied, optional ones left; Chrysostom only "Not long before"; Chrysostom's name stays unheard; the release reports the averages | This batch only |
| "Batch 10: the cards carry what the outlines sent them" ("Approve as recommended"): one more pass per card for the outline's "to the card" items, then a check | This batch only (carries out the card role's existing line; no kit change) |

## Reference scores

As that ruling asks: **the batch averages below the references, and both reference stories moved from their fixed scores.**

| Story | Fixed (`Brief-Kit/reference/Scores.md`) V / C / R / A | This batch's read (`Reference_Read.md`) V / C / R / A |
|---|---|---|
| `basil-of-caesarea` | 4 / 4 / 5 / 4 (4.25) | 4 / 4 / 5 / 5 (4.5) |
| `epiphanius-of-salamis` | 4 / 5 / 4 / 5 (4.5) | 5 / 4 / 5 / 4 (4.5) |
| Reference average | 4.38 | 4.5 |

Batch 10 average, from the twelve `<slug>/Fresh_Read.md` scores before the fixes: **4.08**. By dimension: voice 4.0, craft 3.92, rigor 4.17, accessibility 4.25. By story: Ephesus 4.25, Frumentius 4.25, Cassian 4.25, Chrysostom 4.25, Mesrop 4.25, and 4.0 each for Ephrem, Eutyches, Priscillian, Rufinus, Theodoret and Ulfila. Pelagius is 3.75. No story was re-scored after the applied fixes.

## Not done

- **The `aksumite-christianity-conversion-era` census `why`** still says "shipwrecked" and "tutor", which are not in Rufinus. That is Mark's call: Open-Gaps 360.
- **Theodoret's card** already says the Religious History is held in Greek (fixed in the first card pass); nothing open.
- **Two flags for card owners** from `Second_Readings.md`, not changed: Rufinus [2]'s `uncertain` could note the scan's "qui" read as "quae". Theodoret [0]'s could cite Mansi V 88759-88763.
- **Recording.** Chrysostom and Ephrem changed and must be re-recorded, but `Story-Ledger.md` still marks both "Recorded: yes". The other ten are not recorded. I recorded no audio and made no commit.
