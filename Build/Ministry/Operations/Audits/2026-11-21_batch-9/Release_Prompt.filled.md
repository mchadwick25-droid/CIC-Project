# Batch header

- **Batch:** 9, folder `Build/Ministry/Operations/Audits/2026-11-21_batch-9/`. Eleven stories, all already in the census: basil-of-caesarea, eunomius-of-cyzicus, apollinaris-of-laodicea, evagrius-ponticus, gregory-of-nazianzus, gregory-of-nyssa, eusebius-of-nicomedia, hilary-of-poitiers, cyril-of-jerusalem, epiphanius-of-salamis, damasus-of-rome. No new person entry. Basil had no card: add it after `reviewStatus`.
- **Already applied:** every `Card_Check.md` change, word for word (`Card_Apply.md`), with five scan readings in `tools/quote_scan_readings.json`, and Mark's no-clean-print ruling for Eunomius and Hilary (Decision-Log, "Batch 9: two quoted spans with no clean print", 2026-11-22). Do not apply them again. Step 1 here is only the `secondReading` values in `Second_Readings.md` (B9-30 replaces B9-19; spans marked "checked at card" keep it).
- **Earlier-Approved.yaml** lists both Gregories' briefs: remove those two lines.
- Mark's rulings for this batch: Decision-Log entries headed "Batch 9: …" (2026-11-21, 2026-11-22).

---

# Release

You put one batch's finished work into the census and the tree. You write no story or card text of your own. Work in the repository root, from the batch folder `Build/Ministry/Operations/Audits/2026-11-21_batch-9/`.

1. **Apply the checks.** Apply each `Card_Check.md` FIX and each card change in `Second_Readings.md`, word for word, and set each `secondReading`.
2. **The census** (`cic-website/data/world-census.json`). Add each new person's `<slug>.entry.json` beside the other person entries of its era. For a rewritten story, `longDescription` becomes the brief (final newline removed) and `card` becomes the card. Change no other field. Add each new person's link to the tradition it is told within, as `cyril-and-methodius` is linked, and nothing else.
3. **`tools/quote_renderings.json`.** One listing per quoted span that is our modern English of an original, or of English printed before 1931, and not verbatim in a cited English file, with `second_reading` pointing at `Second_Readings.md`. Remove any listing for a span the batch no longer quotes.
4. **Rebuild.** `python -m engine.m6.cli atlas-sync`, `node Build/tools/generate_tree_pages.mjs` and `python cic/engine/corpus_coverage.py`. Only the batch's pages, the index and the coverage file should change; say if anything else does.
5. **Checks,** each with its output line: `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json`; `node --test tools/tests/validate_census_*.test.mjs`; `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`; `node tools/build_tree_site.mjs`; `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`; `python tools/check_live_commentary.py`; `python tools/check_spelling.py --enforce --base origin/main`; `python -m engine.m1.profile_readability` on each brief; `python tools/check_standard_lock.py --base origin/main`. Fix a failure only where the fix is mechanical. If a check fails for a reason in a brief's or card's content, stop and report it.
6. **The ledger.** Remove any of the batch's stories from `Build/Ministry/Features/Church-Family-Tree/Earlier-Approved.yaml`, then run `python tools/list_story_status.py --write`.
7. Write `Build/Ministry/Operations/Audits/2026-11-21_batch-9/Release.md`: what changed, judgment calls, the checks, and what is not done.

Do not record audio. Do not commit. Reply in under 200 words.
