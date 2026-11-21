# Batch 7 release

Thirteen entries: tertullian-s-voice, cyprian-of-carthage, origen, methodius-of-olympus, lactantius, pamphilus-of-caesarea, dionysius-of-alexandria, novatian, pontius-the-deacon, eusebius-of-caesarea, anatolius-of-alexandria-and-laodicea, peter-of-alexandria, councils-of-rome-and-carthage-251. No brief was changed. One card note was corrected, as the prompt names.

**Held: the census check fails on the Cyprian card's content (see Checks). The release is not ready to merge until that is settled.**

## What changed

- `eusebius-of-caesarea/eusebius-of-caesarea.card.json`, `quotationOriginals[2].uncertain`: "Petavius's Latin in the same file (lines 44669-44675)" now names `cic/texts/epiphanius_panarion-haer-48-69-corpus-haereseologicum-t2-pars-posterior-grc-lat_oehler1860.txt`, where those lines carry the Latin ("Tene, inquit, Eusebi, sedere et innocentem Athanasium a te iudicari? ..."). Re-read there; in `npnf201_...xml` the same lines are Church History VIII.12. The lines were unchanged. The finding came from `Second_Readings.md`, "Notes for the card owner".
- `cic-website/data/world-census.json`: for each of the thirteen, `longDescription` is the text of its `<slug>.brief.txt` (final newline removed). For the twelve people, `card` is its `<slug>.card.json`. Tertullian, Cyprian, Pamphilus and Lactantius had no card, so it is added after `reviewStatus`. For the council, `council` is `councils-of-rome-and-carthage-251.card.json`. A field-by-field comparison with `HEAD` shows no other field changed.
- `Council-Profiles/era1/councils-of-rome-and-carthage-251.brief.txt` and `.entry.json`: unchanged. Batch 4 left `Council-Profiles/era2/council-of-nicaea-325.*` as they were (last changed in batch 3). The census entry and that `.entry.json` differ in shape and in almost every field, so these files do not mirror the census.
- `tools/quote_renderings.json`: 43 listings added. Each is a quoted span that is our modern English of an original, or of English printed before 1931, and is not verbatim in a cited file. Each carries the original's file, lines and language from the card: the `originalFile`/`originalLines` pair where the card gives one, otherwise `file`/`lines`. Each has `second_reading` pointing at `Second_Readings.md`, with the card's verdict. Counts: councils 6, tertullian 5, pamphilus 5, eusebius 5, cyprian 4, pontius 4, lactantius 3, dionysius 3, novatian 3, peter 3, anatolius 2. Origen's two older listings still stand in his new brief, so they are kept. Nothing was removed. Languages: 20 Latin, 18 English, 5 Greek. Verdicts: 41 same, 2 minor (Tertullian, Apology 1 and Against Praxeas 12).
- `tools/quote_scan_readings.json`: unchanged.
- `tools/tests/validate_census_card.test.mjs`: the test puts a test card on `tertullian-s-voice`, which now has a real card and real renderings listings. The validator then reported those listings' files as not among the files the test card cites. The test now passes the validator a copy of the listing without that person's renderings (`--renderings`, the flag the validator provides for tests). No assertion changed.
- `cft-website/index.html`: rebuilt with `python -m engine.m6.cli atlas-sync`.
- `cft-website/tree/*.html`: rebuilt with `node Build/tools/generate_tree_pages.mjs`. Exactly the thirteen pages changed.
- `Earlier-Approved.yaml`: lists none of the thirteen, so it is unchanged. `Story-Ledger.md` was rewritten by `python tools/list_story_status.py --write`: 62 of 263 on the kit, batch 7 "To do: 0". Cyril and Methodius now show as recorded, because `cft-website/audio/tree/cyril-and-methodius.mp3` now exists. That change is not from this release.

## Judgment calls

- Listing languages follow the cited lines. Eusebius's "of one being" is listed as Greek: its original is ὁμοούσιος at `npnf201` line 2091. Potamo's two sentences are listed as English: the card gives McGiffert's English (lines 1515-1523) and no `originalFile`.
- Pamphilus's split quotation ("If it is a joy ..." / "how much more ...") is listed as two spans, one card entry, the same way batch 6 listed fragments.
- Short spans the validator skips were checked by hand. "jointly" (Pamphilus) and "accused" (Eusebius) are verbatim in the cited English, so they are not listed.
- The card test fix is described above. It removes the test's dependence on whichever person it borrows still having no listings.

## Checks

- `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json` (no `--base`): 620 movements, 736 edges, 10 eras, **2 errors**, 4 warnings (shortName length, not ours). The errors: `cyprian-of-carthage: card.sources.about[0].disputed is not allowed` and the same for `about[3]`. The validator allows `disputed` only under `ownWords`. The card puts it under `about`, on the Life of Cyprian (Pontius's authorship) and on Hartel's CSEL 3.3. This is the card's content, so it is not changed here. All quotation errors are cleared.
- `node --test tools/tests/validate_census_*.test.mjs` (twelve files): 108 tests, 54 pass, **54 fail**. Every failure is a case that needs the published census to pass, and each fails on the two Cyprian errors. As a scratch run only, the two `disputed` keys were removed from a copy of the census, the suite was run, and the census was restored byte for byte: 108 pass, 0 fail.
- `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`: `"pass": true`, no changes.
- `node tools/build_tree_site.mjs`: 1618 own files, 173 shared, 0 mismatched.
- `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`: 63 pass, 0 fail.
- `python tools/check_live_commentary.py`: exit 0.
- `python tools/check_spelling.py`: exit 0; 0 British spellings.
- `python -m engine.m1.profile_readability` on the thirteen briefs: 13 graded, 0 failing. Grades run from 6.0 to 8.9. Four are under 8 and carry the listener-read note: anatolius 7.7, cyprian 7.7, dionysius 7.6, pontius 6.0.
- `pytest` tools tests:
  - standard-lock, brief-variety, list-second-readings, tree-overlap, list-story-status: 20 pass.
  - live-commentary, spelling: 258 pass.
  - live-commentary scope, paths, live-watch: 28 pass.
- `python tools/check_standard_lock.py --base origin/main`: exit 0, "No locked standard file changed."

## Not done

- The Cyprian card's two `about[].disputed` fields still need a decision from the card owner: move the notes, or rule that `about` may carry `disputed`.
- CI's `--base` form of the census check was not run.
- The engine suites in the CI workflow were not run.
- No audio was recorded. Nothing was committed.
