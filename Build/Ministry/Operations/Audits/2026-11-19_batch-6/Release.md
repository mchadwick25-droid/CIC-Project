# Batch 6 release

Thirteen entries: pliny-the-younger, tacitus, suetonius, josephus, ignatius-of-antioch, irenaeus-of-lyon, polycrates-of-ephesus, hermas, valentinus, tatian, bardaisan-of-edessa, hippolytus-of-rome, polycarp-of-smyrna. No brief or card was changed.

## What changed

- `cic-website/data/world-census.json`: for each of the thirteen, `longDescription` is the text of its `<slug>.brief.txt` (final newline removed) and `card` is its `<slug>.card.json`. Irenaeus and Polycarp had no card; it is added after `reviewStatus`. No other field changed.
- `tools/quote_renderings.json`: 52 listings added, one per quoted span that is our modern English of an original, or of English printed before 1931, and is not verbatim in a cited English file. Each carries the original's file, lines and language from the card (the `originalFile`/`originalLines` pair where the card gives one, otherwise `file`/`lines`) and `second_reading` pointing at `Second_Readings.md` with the card's verdict. None of the thirteen ids had an old listing, so none was removed. Counts: polycarp 8, irenaeus 6, hippolytus 6, pliny 5, hermas 4, suetonius 3, tacitus 3, josephus 3, ignatius 3, valentinus 3, tatian 3, bardaisan 3, polycrates 2.
- `tools/quote_scan_readings.json`: unchanged; the census check did not need a further reading.
- `cft-website/index.html`: rebuilt with `python -m engine.m6.cli atlas-sync`.
- `cft-website/tree/*.html`: rebuilt with `node Build/tools/generate_tree_pages.mjs`; exactly the thirteen pages changed.
- `Build/Ministry/Features/Church-Family-Tree/Earlier-Approved.yaml`: the `polycarp-of-smyrna` entry removed. `Story-Ledger.md` rewritten by `python tools/list_story_status.py --write`.

## Judgment calls

- Listing languages follow the cited lines: the two Tatian and four Hippolytus (Liber Pontificalis) listings read Latin at those lines, so they are listed as Latin, not as the card's mixed source labels.
- Suetonius's bare quoted word "Chrestus" is verbatim in the cited Rolfe file, so it is not listed.

## Checks

- `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json` (no `--base`): 619 movements, 736 edges, 10 eras, 0 errors, 4 warnings (shortName length, not ours).
- `node --test tools/tests/validate_census_*.test.mjs` (twelve files, the eleven CI lists plus the card test): 107 pass, 0 fail.
- `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`: pass, no changes.
- `node tools/build_tree_site.mjs`: 0 mismatched. `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`: 63 pass, 0 fail.
- `python tools/check_live_commentary.py`: exit 0.
- `python tools/check_spelling.py`: exit 0; 0 British spellings.
- `python -m engine.m1.profile_readability` on the thirteen briefs: 13 graded, 0 failing. Grade 6.0 to 8.6; six are under 8 (pliny, ignatius, hermas, valentinus, hippolytus, polycarp) and carry the listener-read note.
- `pytest` tools tests: standard-lock, brief-variety, list-second-readings, tree-overlap, list-story-status: 20 pass. Live-commentary, spelling: 258 pass. Live-commentary scope, paths, live-watch: 28 pass.
- `python tools/check_standard_lock.py --base origin/main`: exit 0; reports `Brief-Kit/Kit.md` as a locked file changed on this branch, with its Decision-Log entry.

## Not done

- CI's `--base` form of the census check was not run.
- The engine suites in the CI workflow were not run.
- Nothing committed.
