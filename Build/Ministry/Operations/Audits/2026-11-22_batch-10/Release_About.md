# Batch 10 release, after the "what it was about" pass

This is the second release of the same twelve stories: council-of-ephesus-431, eutyches, theodoret-of-cyrrhus, pelagius, john-cassian, john-chrysostom, rufinus-of-aquileia, frumentius, mesrop-mashtots, ulfila, priscillian and ephrem-the-syrian. It follows the "what it was about" pass (README step 10). The first release is `Release.md`. There is no new person entry, so no tradition link was added.

## What changed

- **Cards** (`<slug>/<slug>.card.json`). Every FIX in this pass's `<slug>/Card_Check_About.md` and the one card change in `About-Pass/Second-Reading/Second_Readings.md` was checked by script. For each, the new text stands once in the card and the old text does not. Nothing needed applying.
  - FIX verdicts checked: Ephesus 2, Eutyches 1, Cassian 1, Chrysostom 3, Rufinus 2, Priscillian 1, Ephrem 3.
  - Structured checks: Eutyches `quotationOriginals[3].printed` is "two natures". Chrysostom's Socrates Book 1, chapter 5 source sits right after Book 7, chapter 45. Ephrem's Panarion 56 and Book of the Laws entries sit right after the editor's note on Bardesanes. Ephrem's `quotationOriginals[0].secondReading` is "minor".
  - Theodoret, Pelagius, Frumentius, Mesrop and Ulfila passed their checks with no FIX.
- **`cic-website/data/world-census.json`.**
  - For all twelve, `longDescription` is now `<slug>.brief.txt` with its final newline removed.
  - `card` is now `<slug>.card.json`. For Ephesus, the `council` field takes the card.
  - Each value was replaced as an exact string in the file. The file was not loaded and re-dumped. The result is still byte for byte the file's own JSON form.
  - A field-by-field diff against HEAD shows exactly these 24 fields changed and nothing else, inside or outside `movements`.
- **`tools/quote_renderings.json`.** One listing changed:
  - Ephrem's Palladius listing now quotes "See, on your behalf I appoint myself to take in and care for the needy." Its `second_reading` is `Build/Ministry/Operations/Audits/2026-11-22_batch-10/About-Pass/Second-Reading/Second_Readings.md`, verdict "minor". The original (Clarke 1918, line 471, English) is unchanged.
  - Before the change, that listing's old wording ("Look, on your behalf I appoint myself to run the shelter.") no longer stood in the brief. No other listing was dropped.
  - The other 31 listings for these twelve were checked by script. Each stands once, word for word, in its brief.
  - Eutyches "two natures" got no listing (see Judgment calls).
- **`tools/quote_scan_readings.json`.** Unchanged. The full validator, with the quote check, gives 0 errors, so no span this pass added needs a reading.
- **Rebuilt.** atlas-sync changed `cft-website/index.html`. `generate_tree_pages.mjs` changed the twelve story pages. `corpus_coverage.py` left `corpus-coverage.json` unchanged. Nothing else changed.
- **Ledger.** `Earlier-Approved.yaml` lists none of the twelve, so nothing was removed. `list_story_status.py --write` changed one row of `Story-Ledger.md`: Priscillian is now "Recorded: yes". The reason is `cft-website/audio/tree/priscillian.mp3`, which commit 9314147ad added. That is the 14:34 sample (see Not done).

## Judgment calls

- **Eutyches "two natures": no listing.** The role lists a span only when it is "not verbatim in a cited English file". The span is word for word in Feltoe's English at `cic/texts/npnf212_leo-great-gregory-great.xml` line 4560, which the card cites. The first release listed only the "checked at card" spans that were not word for word in their files: Ulfila "alone unbegotten" and Cassian "the Conferencer". The validator's quote check passes on the span as it stands.
- **Ephrem's original language stays "English".** The listing maps our modern English to Clarke's 1918 print ("appoint myself hospitaller"), which is English printed before 1931. Only the quote and the second reading changed.

## Checks

- `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json`: `629 movements, 736 edges, 10 eras — 0 errors, 4 warnings`. The warnings are shortName length, none of them ours. The first run passed.
- `node --test --test-concurrency=1 tools/tests/validate_census_*.test.mjs`: `# pass 110`, `# fail 0`. They ran to the end in about 38 minutes, with other checks running beside them, and none was killed.
- `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`: both `"eras_differ": false, "edges_differ": false, "changes": []`.
- `node tools/build_tree_site.mjs`: `tree site: 1776 own files (the map page slimmed, 629 card files added), 173 shared files, 0 mismatched`.
- `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`: `# tests 77`, `# pass 77`, `# fail 0`.
- `python tools/check_live_commentary.py`: exit 0. With `--base origin/main --enforce`: exit 0. The census lines it reports are KEEP or WAIVED, none new.
- `python tools/check_spelling.py`: `0 British spelling(s) found in 0 file(s); 0 in enforced trees`. With `--enforce --base origin/main`: the same line, exit 0.
- `python -m engine.m1.profile_readability --report` on the twelve briefs: `12 brief(s) graded, 0 failing`. Grades run from 7.4 to 8.5. Four are under 8 and carry the listener-read note: Pelagius 7.4, Cassian 7.4, Eutyches 7.7 and Frumentius 7.9. Words: the council 585; persons up to 675; Chrysostom 450 and Ephrem 417.
- `python tools/check_standard_lock.py --base origin/main`: exit 0. `Kit.md` and `roles/checker.md`, `researcher.md` and `reviewer.md` changed, with a new Decision-Log entry carrying Mark's words.

## Mark's rulings in this pass

| Ruling | Where it lives now |
|---|---|
| "Explain it or leave it out: the kit asks what each thing was about" (Decision-Log, 2026-11-23; Mark: "a") | Kit Part 1, the test ("what it was about") and the stake line "Explain it or leave it out ..."; Part 3, Length ("cut an event before its meaning") and Story beats; Part 4, the bar ("missing essential material"); `roles/researcher.md`, `checker.md` and `reviewer.md`. It governs batch 11 on |
| "The live stories reopened for what each thing was about: scan everything, then a targeted pass" (Decision-Log, 2026-11-23; Mark: "a, scan all three") | Decision-Log only, as a change order to Kit Part 4's "it never reopens a finished story", for this one rule. The kit line itself is unchanged. Batch 10's twelve go first |
| "Fix the batch 10 files now and get them right before recording" (Mark, 2026-11-23; batch README step 10) | This batch only: the lengths (persons 675, the council 585, Chrysostom and Ephrem up to 450) and the order (cards, release, recording again, Priscillian re-recorded) |

The rulings of the first release (slate, hearts, the six long drafts, the fresh read and the cards) are in `Release.md` and stand as written there.

## Not done

- **Recording.** No audio was recorded. The two rulings above hold batch 10's recording, and the audio for fixed stories "is decided separately". `Story-Ledger.md` now marks three stories "Recorded: yes", and all three audio files predate their current briefs:
  - Priscillian: the 14:34 sample (`recording/batch10-run1-priscillian.log`), but the brief changed at 16:02 (commit 432e9d77b). README step 10 says he is to be re-recorded.
  - Chrysostom and Ephrem: their audio is from 2026-11-18, and both briefs have changed since then.
- **Carried from the first release**, unchanged: the `aksumite-christianity-conversion-era` census `why` (Open-Gaps 376), and the two flags for card owners on Rufinus [2] and Theodoret [0].
- **Flagged in this pass's card checks, outside the cards:** the outline citation for "Socrates is no friend of Theophilus" (Chrysostom's `Card_Check_About.md`), and the reversed file names in the third-pass headers of the Cassian and Rufinus `Card_Edits.md`. Both are already noted in those files.
- No commit.
