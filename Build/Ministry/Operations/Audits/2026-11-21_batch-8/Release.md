# Batch 8 release

Twelve people: nine new (francis-of-assisi, bernard-of-clairvaux, thomas-aquinas, jan-hus, catherine-of-siena, gregory-palamas, huldrych-zwingli, thomas-cranmer, teresa-of-avila) and three already on the tree (ambrose-of-milan, jerome, leo-of-rome). `constantine-the-great` passed review unchanged and was not touched. No brief or card was changed.

## What changed

- `cic-website/data/world-census.json`:
  - The nine `<slug>.entry.json` files (as `Census_Check.md` left them, Catherine's "honor" fix already in) were added as new movements beside the other person entries of their era: era 5 after `bonaventure`, era 6 after `john-wyclif`, era 7 after `ignatius-of-loyola`.
  - For Ambrose, Jerome and Leo, `longDescription` is the text of `<slug>.brief.txt` (final newline removed) and `card` is `<slug>.card.json`. Ambrose and Jerome had no card; it is added after `reviewStatus`. Leo's card replaced his old one.
  - Edges: the census links a person to the tradition that tells them through the tradition's `people` list (`{"person": id}`), not through `edges` (the `edges` list holds no entry for `cyril-and-methodius`). Each new person is added to the `people` list of their `toldWithin` tradition, in date order by `start`. No `edges` entry was added.
  - `meta.totalEntries` (620 to 629) and `meta.statusCounts` ("Within Another World (A5)" 255 to 264) by `python -m engine.m6.cli sync`.
- `tools/quote_renderings.json`: 43 listings added (266 to 309), one per quoted span that is our modern English of an original, or of English printed before 1931, and is not verbatim in a cited English file. Each carries the original's file, lines and language (the card's `originalFile`/`originalLines` where it gives them, otherwise `file`/`lines`) and `second_reading` pointing at `Second_Readings.md`. Verdicts: 40 same, 3 minor (bernard 0, zwingli 1, jerome 2). Counts: jan-hus 5, gregory-palamas 5, ambrose 5, thomas-aquinas 4, huldrych-zwingli 4, jerome 4, francis 3, catherine 3, teresa 3, leo 3, bernard 2, cranmer 2. None of the twelve had an old listing, so none was removed.
- `cft-website/index.html`: rebuilt with `python -m engine.m6.cli atlas-sync`.
- `cft-website/tree/*.html`: rebuilt with `node Build/tools/generate_tree_pages.mjs`. Nine pages new; three person pages changed (ambrose, jerome, leo).
- `python tools/list_story_status.py --write` run; `git status` shows `Story-Ledger.md` with no change against HEAD at the end (it showed modified once, midway). `Earlier-Approved.yaml` lists none of the twelve, so nothing was removed.

### Changed beyond the twelve pages and the index

- Nine tradition pages (their people lists changed): the-franciscan-movement, cistercian-monasticism, the-dominican-order, the-hussite-and-bohemian-brethren-movement, latin-papal-church-avignon-to-lateran-v, hesychasm-and-the-palamite-synthesis, the-reformed-cities-zurich-and-geneva, the-english-reformation-and-elizabethan-settleme, carmelite-reform-and-spanish-mystics.
- `cft-website/data.html` and `cft-website/method.html` (movement count 620 to 629) and `cft-website/sitemap.xml` (27 lines added for the nine pages).

## Judgment calls

- A named voice in a tradition's `people` list that is the same person as a new entry (Jan Hus, Catherine, Palamas, Zwingli, Cranmer, Teresa) is replaced by the person entry, as the validator requires ("already in this row as the person entry").
- `peopleNote` removed from `cistercian-monasticism` and `the-dominican-order`, which now name someone (the validator allows it only on an empty list).
- `modernCountries`: the validator requires each record's `place` to be a part of `placeLabel`. Records whose place is not on the label were dropped from the new entries: francis, bernard, jan-hus, zwingli, teresa (all emptied); thomas-aquinas (Italy and Germany dropped, France/Paris kept); catherine (Rome dropped, Avignon kept); palamas (Constantinople dropped); cranmer unchanged. This is the drafter's field, not the card's or the brief's; the alternative is to change `placeLabel`, which reads on the page. For Mark.
- The 13 spans the cards mark "checked at card" are listed with verdict "same"; no second reading was made of them (`Second_Readings.md`).
- Languages follow the cited lines: Francis's Canticle is listed as Italian, Palamas's "navel-souls" as Greek (the Greek at `originalLines`), Báñez's censure in Lewis's preface and the Cranmer and Foxe spans as English.

## Checks

- `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json`: 629 movements, 736 edges, 10 eras, **1 error**, 4 warnings (shortName length, not ours). The error: `francis-of-assisi: card.sources.about[2].disputed is not allowed (allowed: title, author, language, file, date)`. The Mirror of Perfection entry in the card's `about` list carries a `disputed` note; the schema allows `disputed` only under `ownWords`. This is card content, so it is not fixed here.
- `node --test tools/tests/validate_census_*.test.mjs`: 54 pass, **56 fail**. Each failing case I opened (the card test's "a valid card passes") fails on that one Francis error, because the tests validate the real census. Not re-run after a fix, since there is none yet.
- `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`: pass, no changes. `python -m engine.m6.cli check`: pass.
- `node tools/build_tree_site.mjs`: 0 mismatched. `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`: 65 pass, 0 fail.
- `python tools/check_live_commentary.py`: exit 0.
- `python tools/check_spelling.py`: exit 0, but **5 British spellings in 2 files, 0 in enforced trees**: "quarrelling" twice in `ambrose-of-milan.card.json` (text in the `uncertain` and election notes, so also in the census and the Ambrose tree page), and "councillors" once in `teresa-of-avila.brief.txt` (Teresa's census `longDescription`). Both are card and brief wording, so not changed here. The script also took about six minutes.
- `python -m engine.m1.profile_readability` on the briefs (the twelve and Constantine's): 13 graded, 0 failing. Grade 6.5 to 9.3; the twelve are 6.5 to 7.6, under 8, and carry the listener-read note; Constantine is 9.3.
- `pytest` tools tests: standard-lock, brief-variety, list-second-readings, tree-overlap, list-story-status: 23 pass. Live-commentary, spelling: 258 pass. Live-commentary scope, paths, live-watch: 28 pass.
- `python tools/check_standard_lock.py --base origin/main`: exit 0; "No locked standard file changed."

## Not done

- The three British spellings above (quarrelling, councillors): a mechanical fix in the card and the brief, left for you to order, since the rule is not to reword.
- The Francis `disputed` field (above): needs a ruling on the card, either dropping the key or moving the note into `uncertain`. Until then the census check fails and 56 census tests fail.
- CI's `--base` form of the census check was not run.
- The engine suites in the CI workflow were not run.
- Nothing committed. No audio recorded.
