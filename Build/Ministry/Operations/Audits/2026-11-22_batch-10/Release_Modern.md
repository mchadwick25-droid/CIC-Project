# Batch 10 release, after the modern pass: stopped at the validator

This is the third release of the same twelve stories, after the modern pass (Decision-Log, "No modern opinion, guess or reconstruction in a story", Mark, 2026-11-23, "yes go ahead, option A stricter"). The brief is `Modern-Pass/M_Release.md`. The release stopped at the census validator, on a failure in card content (see Stopped). Nothing is committed.

## What changed

- **Cards.** Nothing applied, as the brief says. A script read each `<slug>/Card_Check_Modern_Applied.md` (108 entries in all) and found each new text standing in its card. The one entry it flagged is Rufinus's "(entry removed)" marker; the removed Fremantle Prolegomena entry is gone from the card.
- **`cic-website/data/world-census.json`.** For all twelve, `longDescription` is now `<slug>.brief.txt` with its final newline removed, and `card` is now `<slug>.card.json` (for Ephesus, `council`). Each value was replaced as an exact string; the file was not re-dumped and is still byte for byte its own JSON form. A field-by-field diff against HEAD shows exactly these 24 fields changed and nothing else.
- **`tools/quote_renderings.json`.** Unchanged. The 32 listings for these twelve each stand once, word for word, in their briefs. The validator reports no listing that no longer stands.
- **`tools/quote_scan_readings.json`.** Unchanged. The 14 readings batch 10 added (Ephesus Hefele 7244-7245, Frumentius PG 25 92806-92814, Pelagius PL 30 815-816, Mesrop T12 55858-55882) each still fall inside the lines of a card quotation. The validator reports none that no longer reads its file.
- **Rebuilt.** atlas-sync changed `cft-website/index.html`; `generate_tree_pages.mjs` changed the twelve story pages; `corpus_coverage.py` left `corpus-coverage.json` unchanged. Nothing else changed.

## Stopped

`node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json`:
`ERROR priscillian: quotation not found verbatim in the files it cites: "sixty years on"`, then `629 movements, 736 edges, 10 eras — 1 errors, 4 warnings`. The four warnings are shortName length, none of them ours.

- The cause is the new Prosper and Hydatius entry in Priscillian's `briefReferences`, added in this pass ("Edit 3 to 9", `priscillian/Card_Edits.md`, fourth pass). It ends `for "sixty years on".`, quoting the brief's own words.
- The quote check reads every double-quoted span in card prose as a quotation from a cited file. The phrase is ours, so it stands in no file. The card check's validator run used `--skip-quotes`, so it did not catch this.
- Both possible fixes are content, not mechanical. One is to reword the card entry so it names the brief's phrase without quotation marks, which is card text. The other is to list the phrase in `quote_renderings.json`, which would be a false listing, since it renders no original. Per the role, the release stops here for the card's owner.

## Checks run

- `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`: both `"eras_differ": false, "edges_differ": false, "changes": []`.
- `node tools/build_tree_site.mjs`: `tree site: 1779 own files (the map page slimmed, 629 card files added), 173 shared files, 0 mismatched, in .build/tree/`.
- `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`: `# tests 80`, `# pass 80`, `# fail 0`.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0.
- `python tools/check_spelling.py --enforce --base origin/main`: `0 British spelling(s) found in 0 file(s); 0 in enforced trees`, exit 0.
- `python tools/check_standard_lock.py --base origin/main`: exit 0, `Locked standard files changed, with a new Decision-Log entry carrying Mark's words` (`Kit.md`, `roles/checker.md`, `researcher.md`, `reviewer.md`).
- `python tools/check_open_gaps_numbers.py`: exit 0, no output.
- `python -m engine.m1.profile_readability --report` on the twelve briefs: `12 brief(s) graded, 0 failing`. Grades run from 7.0 to 8.6. Five carry the under-8 listener-read note: Cassian 7.0, Pelagius 7.5, Ephesus 7.7, Eutyches 7.7 and Rufinus 8.0 (rounded). Words: the council 580; persons 395 (Ephrem) to 672 (Pelagius); Chrysostom 445.

## Not done

- **The Priscillian card entry** above. Once it is fixed, rerun the validator, then the steps below.
- `node --test --test-concurrency=1 tools/tests/validate_census_*.test.mjs`: not run, as the release stopped first.
- **The ledger.** `Earlier-Approved.yaml` and `python tools/list_story_status.py --write` were not run.
- The census edits and rebuilt pages are left in the working tree, uncommitted, so the release can resume from them.
- No audio was recorded. No commit.
