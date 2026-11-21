# Batch 8: put the twelve into the census and rebuild the tree

You integrate finished work. You write no story or card text of your own except where this prompt names a fix. Batch 6's record of the same step is the model: `Build/Ministry/Operations/Audits/2026-11-19_batch-6/Release.md`. Work in the repository root.

## Do
1. **The census** (`cic-website/data/world-census.json`). For the nine new people, add each `<slug>/<slug>.entry.json` (as `Census_Check.md` left it) as a new movement, beside the other person entries of its era, in the file's order. For `ambrose-of-milan`, `jerome` and `leo-of-rome`: `longDescription` becomes the text of `<slug>.brief.txt` (final newline removed), and `card` becomes `<slug>.card.json`; Ambrose and Jerome had no card, so add it after `reviewStatus`. Change no other field. `constantine-the-great` passed review unchanged: leave it as it is.
2. **Edges.** If the census `edges` list links people to the tradition they are told within (check how `cyril-and-methodius` is linked), add the same link for each new person, and nothing else.
3. **`tools/quote_renderings.json`:** add one listing per quoted span that is our modern English of an original, or of English printed before 1931, and is not verbatim in a cited English file, as batch 6 did, with `second_reading` pointing at `Build/Ministry/Operations/Audits/2026-11-21_batch-8/Second_Readings.md`. Remove any listing for a span the twelve no longer quote.
4. **Rebuild:** `python -m engine.m6.cli atlas-sync`, then `node Build/tools/generate_tree_pages.mjs`. Only the twelve pages (nine new) and the index should change; say if anything else does.
5. **Checks, each reported with its output line:** `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json`; `node --test tools/tests/validate_census_*.test.mjs`; `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`; `node tools/build_tree_site.mjs`; `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`; `python tools/check_live_commentary.py`; `python tools/check_spelling.py`; `python -m engine.m1.profile_readability` on the twelve briefs; the `pytest` tool tests batch 6 ran; `python tools/check_standard_lock.py --base origin/main`.
   Fix a failure only where the fix is mechanical (a scan reading the validator names, a renderings listing). If a check fails for a reason in a brief or card's content, stop and report it; do not reword.
6. **The ledger:** `Build/Ministry/Features/Church-Family-Tree/Earlier-Approved.yaml` may list Ambrose, Jerome or Leo; remove any of the twelve that is listed. Then `python tools/list_story_status.py --write`.
7. Write `Build/Ministry/Operations/Audits/2026-11-21_batch-8/Release.md` in batch 6's form: what changed, judgment calls, checks, not done.

Do not record audio. Do not commit. Reply in under 200 words.
