# Church Family Tree: phone loading audit (2026-11-22)

Step 1 of the plan in Open-Gaps 352, "The home page is about 9.5 MB". Read-only: nothing on the site changed.

**The question.** The map's home page is 9.6 MB because the whole data set is copied into it. Which of those fields does the map actually read to start up, and which only when something is opened?

## Method

`scripts/build_tracer.py` makes a copy of `cft-website/index.html` in which the embedded data (`const DATA`) sits behind a Proxy. Every field the page reads is counted under the current phase, by path (for example `DATA.movements[].card.role`). Whole-object reads (spread, `Object.keys`, `JSON.stringify`) are counted separately; there were none.

`scripts/audit_run.js` drives the copy in Chromium at 1440 by 900 and sets the phase before each scenario:

| Phase | What it does |
|---|---|
| start-up | load and wait 7 s |
| zoom, reading and deep | zoom in with ctrl and wheel |
| People layer, Stories layer | turn each on |
| link tooltip, tradition tooltip, person tooltip | hover a link; call `tipFor` |
| card: tradition, built world, person, council | `openPanel` on Armenian conversion era, Donatism, Augustine, Nicaea |
| story card, link card, river card, era card | open each |
| people list for a tradition, a person from the list | `setWho`, then click a row |
| deep link | load `?world=augustine-of-hippo` fresh |

Sizes come from the pristine data in `index.html`, not from the instrumented page, which moves some fields while it runs (a first version measured from the running page and missed the person cards).

## Results

**Start-up reads 62 field paths, 43 of them leaf fields.** Zooming in, turning on People or Stories, and hovering a tradition or a person read nothing new. Everything those draw comes from the start-up fields.

| Data | When the map first reads it | MB (leaf values) |
|---|---|---|
| movements | start-up | 1.21 |
| movements | when a card opens | 4.44 |
| movements | not read in any scenario | 0.57 |
| edges (links) | start-up | 0.14 |
| edges | link tooltip (`note`) | 0.20 |
| edges | link card (`sources`) | 0.30 |
| edges | not read in any scenario | 0.51 |
| stories | story card | 0.18 |
| stories | start-up | 0.01 |

**Of the 1.21 MB read at start-up, 1.04 MB is `longDescription`.** The only start-up reader is the check that decides whether a tradition's recording matches its text: it hashes every long description at load. A stored hash per entry (about 41 KB) replaces it.

### What the map needs besides what a card shows

1. **The people lists read `card.role` for every person in the list** (14 KB for everyone). `role` stays in the start-up data although the rest of the person card moves out.
2. **Story markers need each story's `title` and `when` at start-up** (27 KB); the story `text`, sources and quotations only when a story opens.
3. **`people[]` (name, person, year), `modernCountries`, `placeLabel` and `dates` are read at start-up** for the people layer and the place line.
4. **A link tooltip reads `edges[].note`** (0.20 MB); a link card reads `edges[].sources` (0.97 MB of data in total, of which the audit exercised the parts one link shows).
5. **A deep link to a person reads that person's whole card on load**, so a card needs its file before it can open.
6. **No code enumerates whole entries**, so removing fields from an entry cannot break a spread or a copy.

### Proposed start-up schema

`startup_fields.json` lists the 43 fields. Add `movements[].card.role` and a hash of the long description. Then:

- Start-up data: about 0.37 MB of leaf values, about 0.42 MB as shipped (keys and punctuation), plus the code and styles (0.29 MB). Link tooltip text adds 0.20 MB if it stays in the page.
- A card file per entry (everything else): median 9.2 KB, 90th percentile 14.7 KB, 99th 26.7 KB, largest 31.2 KB (Tertullian's Voice and Nicaea are among the largest). Compressed, the median is roughly 2.6 KB.

### Estimate, updated

The page would be about 0.75 to 0.95 MB raw (from 9.6 MB) and roughly 0.2 to 0.3 MB compressed (from 2.6 MB); the compressed figure is an estimate. The ceiling test measured on a 1.9 MB page: names appeared after 3.0 s instead of 4.8 s on an emulated phone. A leaner page may do somewhat better; the roughly 3 s of drawing work is not touched.

## What the work would change in the repository

The map's data is not edited by hand. `python -m engine.m6.cli atlas-sync` splices the census's movements, links and eras into the page in place (`engine/m6/atlas_html.py`, `census_atlas_sync.py`, `cli.py`). So the build step is a change to that generator, which also has to write the per-entry files, not only a new script. Things that read the embedded `const DATA` and would change with it:

- `tools/validate-census.mjs` (`--atlas`, and the stories check near line 749)
- `tools/tests/validate_census_story_text.test.mjs`, `tools/tests/validate_census_river_origins.test.mjs`
- `Build/tools/generate_tree_pages.test.mjs`, `generate_docstory_narration.test.mjs`, `tree_map_view.test.mjs`
- `tools/check_spelling.py` (fixes embedded JSON), `tools/check_no_embedded_world_data.py`, `tools/check_live_commentary.py`
- `.github/workflows/ci.yml` (path filters that name `cft-website/index.html`)

The story kit's release steps rebuild the page with `atlas-sync` and validate it with `validate-census.mjs --atlas`; both would need to follow.

## What this audit did not cover

- **Fields never read are not proven unused.** 0.57 MB of movement fields and 0.51 MB of link fields were not read in any scenario (biggest: link `quote` 259 KB, `file` 118 KB, `statusDescription` 65 KB). Some are shown only for certain entries. Check them before dropping any.
- **One screen size.** The audit ran at 1440 px. A phone width takes other code paths (`narrowScreen()`), and the same scenarios need running at 390 px.
- **The tour, the Key and the connections panel read no new fields**, but the tour click found nothing to press, so the tour was not exercised.
- **No keyboard path and no error path** (a failed card fetch does not exist yet).

## Files

- `scripts/build_tracer.py`, `scripts/audit_run.js`, `scripts/analyze_fields.py`, `scripts/card_sizes.py`: the audit, re-runnable.
- `startup_fields.json`: the 43 start-up leaf fields.
