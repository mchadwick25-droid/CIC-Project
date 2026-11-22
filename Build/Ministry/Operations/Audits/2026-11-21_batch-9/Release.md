# Batch 9 release

Eleven stories already in the census: basil-of-caesarea, eunomius-of-cyzicus, apollinaris-of-laodicea, evagrius-ponticus, gregory-of-nazianzus, gregory-of-nyssa, eusebius-of-nicomedia, hilary-of-poitiers, cyril-of-jerusalem, epiphanius-of-salamis, damasus-of-rome. No new person entry, so no tradition link was added. The census and pages were built from the briefs as they stood at commit 65d9ae73 (the release prompt). Five briefs changed after that (see "Not done").

## What changed

- Cards (`<slug>/<slug>.card.json`): `secondReading` set on the 29 entries in `Second_Readings.md` ("Card changes needed"), with Eunomius `quotationOriginals[3]` = "minor" from B9-30. It was placed last in each entry, as most census cards have it. Entries marked "checked at card" were not touched. Every entry on the nine cards now has a `secondReading`. The two Gregories' cards already had theirs.
- `cic-website/data/world-census.json`: for all eleven, `longDescription` is `<slug>.brief.txt` with its final newline removed, and `card` is `<slug>.card.json`. Basil had no card, so his card was added after `reviewStatus`. No other field changed. The Gregories take `brief.txt`, not `brief.approved.txt` (Nazianzus: "Apollinaris"; Nyssa: the added sentence).
- `tools/quote_renderings.json`: 27 listings added (309 to 336), with `second_reading.record` set to `Second_Readings.md`. By story: Apollinaris 4, Basil 3, Cyril 5, Damasus 3, Epiphanius 2, Eunomius 1 ([3]), Eusebius 5 ([0], [1], [2], [5], [7]), Evagrius 2 ([0], [4]), Hilary 2 ([0], [6]). Each original is the card's `originalFile`/`originalLines` where the card gives them, otherwise its `file`/`lines`. Languages follow those lines: Greek for Basil [1], Apollinaris [0], [2], [3], Cyril [0], [1], Epiphanius [0] and Eusebius [5], [7]; Latin for the three Damasus spans; English for the rest. No old listing was removed. The five Gregory listings still stand in their briefs.
- Rebuilt: `cft-website/index.html` (atlas-sync) and the eleven `cft-website/tree/<slug>.html` pages. `corpus_coverage.py` left `corpus-coverage.json` unchanged. Nothing else changed: no tradition page, sitemap, data or method page.
- `Story-Ledger.md` regenerated: 86 of 272 on the kit (was 75). Era 2 now lists the eleven as batch 9.

## Judgment calls

- **Evagrius [1] is not listed.** It is our rewording of Dysinger's Praktikos 6, a 2026 English translation under CC BY 4.0. The card says the Greek is not held. That is neither our English of an original we hold nor English printed before 1931, so it does not meet the listing rule. The census check fails on it (see Checks). Mark needs to rule on one of three options: quote Dysinger word for word with his attribution, render from a held Greek text, or extend the listing rule to cover this case. Changing the wording to modern terms would also touch the CC BY "indicate changes" duty.
- **Eusebius [5] ("of one being,") and [7] ("those around Eusebius.") are listed with verdict "same".** Both are "checked at card" spans that are not word for word in their files. This follows batch 8. No blind reading was made of them.
- **Hilary [0] is listed against the English file it cites (npnf209), not PL 10.** B9-28 says our wording follows the Latin, but the card cites no Latin file, and a listing may only use a file the entry cites. Eusebius [0] is the same case: it follows the Greek aorist "said", but is listed against its cited English.
- **`Earlier-Approved.yaml`.** The header said to remove the two Gregory lines, but the file has listed no stories since batch 6, so nothing was removed.
- **Commits.** I made none. Other sessions committed this work in progress as it went (21d31288, a33101ba, cb702346).

## Checks

- `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json`: 629 movements, 736 edges, 10 eras, **1 error**, 4 warnings (shortName length, not ours). The error: `evagrius-ponticus: quotation not found verbatim in the files it cites: "Whether these thoughts can trouble the soul is not up to us. ..."`. This is card or brief content (above), so I did not fix it. Before the listings were added, there were 28 such errors.
- `node --test tools/tests/validate_census_*.test.mjs`: 110 tests, 109 pass, **1 fail** (named below). A run with the twelve files in parallel failed many tests because of resource contention, so that run is not counted.
- `python -m engine.m6.cli atlas-check` and `atlas-check --edges-only`: pass, `"changes": []`.
- `node tools/build_tree_site.mjs`: 1766 own files, 173 shared, 0 mismatched.
- `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`: 71 pass, 0 fail.
- `python tools/check_live_commentary.py`: exit 0.
- `python tools/check_spelling.py --enforce --base origin/main`: 0 British spellings in 0 files. `origin/main` was missing from this clone, so I fetched it first.
- `python -m engine.m1.profile_readability` on the eleven briefs: 11 graded, 0 failing. Grades run from 7.2 to 9.6. Basil 7.4, Cyril 7.3, Eunomius 7.4, Evagrius 7.2 and Hilary 8.0 carry the under-8 listener-read note. This ran on the briefs as they stood during the run.
- `python tools/check_standard_lock.py --base origin/main`: "No locked standard file changed."

## Not done

- **The census is behind five briefs.** After this release began, the fresh read and craft pass changed the briefs of Apollinaris, Eusebius, Hilary, Cyril and Damasus (23174106, 5c7b29ae, d2cfcc12). Their census `longDescription` and tree pages still hold the earlier text. Hilary's quotes changed as well: "of one substance" is gone, and the spans "like in substance," and "one in substance," have moved. So his card's `quotationOriginals` [1] to [4] no longer match his brief, and the card needs another pass. Once the briefs settle, steps 2 to 5 should be run again for these five.
- The Evagrius [1] ruling (above). Until it is made, the census check fails.
- Flags for the card owners, from `Second_Readings.md`: Eusebius [0] `uncertain` (the "said" follows the Greek); Eunomius [3] `uncertain` (drops the "if").
- `Story-Ledger.md` marks both Gregories "Recorded: yes", although both changed and need recording again.
- I recorded no audio. Audio and manifest changes from another session are in the working tree.
