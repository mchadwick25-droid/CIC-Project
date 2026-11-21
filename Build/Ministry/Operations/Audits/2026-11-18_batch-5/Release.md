# Batch 5 release

Twelve entries: nestorius, cyril-of-alexandria, barsauma-of-nisibis, babai-the-great, timothy-i-of-baghdad, martin-luther, william-tyndale, john-calvin, john-wesley, augustine-of-hippo, patrick-of-ireland, athanasius-of-alexandria. No brief or card was changed.

## What changed

- `cic-website/data/world-census.json`: for each of the twelve, `longDescription` is the text of its `<slug>.brief.txt` (final newline removed, as batch 4 stored it) and `card` is its `<slug>.card.json`. Seven entries (nestorius, martin-luther, william-tyndale, john-calvin, john-wesley, augustine-of-hippo, patrick-of-ireland) had no card; it is added after `reviewStatus`. No other field changed.
- `tools/quote_renderings.json`: the twelve ids' old listings are replaced by 36 listings, one per quoted span that is our modern English of an original and is not verbatim in a cited English file. Each carries the original's file, lines and language from the card (the `originalFile`/`originalLines` pair where the card gives one, otherwise `file`/`lines`) and `second_reading` pointing at `Second_Readings.md` with the card's verdict. Three old listings whose spans are gone were removed (babai-the-great: one; athanasius-of-alexandria: two). Counts: barsauma 10, martin-luther 4, nestorius 3, cyril 3, john-calvin 3, athanasius 3, babai 2, timothy 2, augustine 2, patrick 2, tyndale 1, wesley 1.
- `tools/quote_scan_readings.json`: 11 readings added from the twelve `Scan_Readings.json` files (athanasius 4, barsauma 2, augustine 1, cyril 1, luther 1, nestorius 1, timothy 1).
- `cft-website/index.html`: rebuilt with `python -m engine.m6.cli atlas-sync`.
- `cft-website/tree/*.html`: rebuilt with `node Build/tools/generate_tree_pages.mjs`; exactly the twelve pages changed.

## Left out of the scan readings

- timothy-i-of-baghdad, Synodicon line 40545: no span on the card reaches that line.
- patrick-of-ireland, all six readings (White lines 2990, 2991-3008, 3009; Stokes 7372 twice, 7373): the shortened story no longer quotes those lines. The one carrying a `hold` key (White line 3009, the page-turn dash before "blush not to state it") is not added. The census check does not read those lines, so nothing fails on it; the person's page-image check it asks for is moot while the card does not quote the passage.

## Checks

- `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json` (run without `--base`): 619 movements, 736 edges, 10 eras, 0 errors, 4 warnings (shortName length, not ours).
- `node --test` on the eleven census tests: 99 pass, 0 fail.
- `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`: pass.
- `node tools/build_tree_site.mjs`: 0 mismatched. `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`: 63 pass, 0 fail.
- `python tools/check_live_commentary.py`: exit 0.
- `python tools/check_spelling.py`: exit 0; 3 British spellings found in 2 files, 0 in enforced trees: "catalogue" in `cft-website/tree/nestorius.html` (lines 153, 160) and `cic-website/data/world-census.json` line 82019. It comes from the card text, which was not to be changed. Not fixed.
- `python -m engine.m1.profile_readability` on the twelve briefs: 12 graded, 0 failing. Grade 7.2 to 8.6; seven are under 8 and carry the listener-read note.
- `pytest` tools tests: standard-lock, brief-variety, list-second-readings, tree-overlap: 17 pass. Live-commentary, scope, paths, live-watch, spelling: 280 pass.

## Not done

- CI's `--base` form of the census check (needs the main-branch copy) was not run.
- The engine suites in the CI workflow (engine/m1 and others) were not run; they are not tool tests.
- Nothing committed.
