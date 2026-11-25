# Release: Montanism, the New Prophecy (`montanism-the-new-prophecy`, tradition)

Released alone, ahead of batch 11 (Decision-Log, "Batch 11: Montanism released alone and recorded" and "Batch 11: Montanism fixed and regraded before recording"). No other batch-11 story was touched. Not committed; no audio recorded.

## What changed

**Card file and card audit (step 1).**
- `montanism-the-new-prophecy.card.json`: `Card_Check.md` FIX 1 (`uncertain[10]`), FIX 2 (`briefReferences[3]`), FIX 3 (`briefReferences[4]`), word for word. `secondReading` set from `Second_Readings.md`: Q1 "same", Q2 "minor", Q3 "minor".
- `Card_Edits.md`: FIX 4, word for word. The `end` row now reads "not changed" (565 struck), and `dates` reads "2nd-6th c.".
- No reading changes meaning (SAME 1, MINOR 2, MEANING 0), so the brief is unchanged and no sentence goes for a targeted check.

**Census (`cic-website/data/world-census.json`, step 2).** Only these fields of the existing entry changed:
- `longDescription`: the final brief, with its final newline removed.
- `why`, `teaser`, `floorNote`: from the card, as `Card_Edits.md` lists them and `Card_Check.md` passes them.
- `documentedStories`: corrections 1-7. The Trevett and Heine lines move from `sources` to each story's `modernWorks`, and an Epiphanius source line is added to the second story.
- `dates`: `2nd-6th c.` (FIX 4).

`start` (165), `end` (400), `relationsSummary`, `sourcing`, `voices`, `legacy` and `people` are unchanged. The card leaves the last four word for word. No new keys were added, and there are no links, edge notes, map stories or narration for this entry.

**Mechanical fixes made because the old text was removed (step 5).**
- `cic-website/data/search-names.json`, row "Montanist": its `basis.text` quoted the old longDescription ("They did not call themselves Montanists — that was their opponents' label."). It now quotes the new brief's sentence: "Enemies called them Montanists or Phrygians, but they spoke of the New Prophecy, their name for the prophets and their words." The name, kind and target are unchanged.
- `tools/tests/validate_census_search_names.test.mjs`: its sample row quoted the same old words ("that was their opponents' label."). It now quotes "Enemies called them Montanists or Phrygians". Four tests had failed on this; all pass now.

**Rebuild (step 4).** `atlas-sync` changed only `cft-website/index.html`, and only the Montanism record. `generate_tree_pages.mjs` changed only `cft-website/tree/montanism-the-new-prophecy.html`. `corpus_coverage.py` left `corpus-coverage.json` unchanged (629 entries, 303 with vendored coverage). Nothing else changed.

On the tree page, the old "Audio Brief · Narrated Edition 1:13" player no longer shows, because the old recording does not match the new text. It returns once the new recording ruled for this release is made.

**Ledger (step 6).** `Earlier-Approved.yaml` holds no entries, so there was nothing to remove. `python tools/list_story_status.py --write` rewrote `Story-Ledger.md`. The rewrite adds an "On the kit, not in the census" list of all thirteen batch-11 slugs, Montanism among them. The tool only counts persons and councils (`KINDS`), so a tradition never counts as in the census, even when it is live. That is a gap in the tool. It is not fixed here.

## Held, not applied

- **Card fields with no home on a tradition:** `sources`, `quotationOriginals` (now with `secondReading`), `uncertain` and `briefReferences`. They stay in the card file until Mark rules where tradition cards live.
- **Top-level `modernWorks`:** the five editions listed in `Card_Edits.md` are held. The entry has no such field, and the header says to add no new keys.
- **Step 3, `tools/quote_renderings.json`: nothing listed.** Q1 is word for word in its cited English (NPNF 1890, commas aside), so it needs no listing. Q2 (the Latin of On Fasting 1) and Q3 (the Greek of Panarion 49.1) each need one.
  - A scratch trial of those two listings (`--renderings`, outside the repository) gave 4 validator errors. Each file "is not among the files montanism-the-new-prophecy cites", because the validator reads cited files only from `card.sources` or `council.sources`. Each span also "no longer stands", because `checkQuotes` runs only for a person or a council.
  - Both listings wait on the same ruling as the card. They are ready to add as soon as a tradition's sources have a home:
    - Q2: `tertullian_opera-pars1-lat_reifferscheid-wissowa-csel20.txt` 15495-15499, Latin, minor.
    - Q3: `epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt` 18758-18764, Greek, minor.
  - With record `Second_Readings.md`.
- **Passed card text the final brief now contradicts, not applied:** `briefReferences[11]` says "Pepuza razed and deserted". The grade dropped "razed" from the brief (`Grade_Fixes_Applied.md`, change 6), because no held source says who razed it. The field is held, so nothing reached the census. It should be edited when the card gets a home.
- **Applied, but worth Mark's eye:**
  - `documentedStories[1].text` keeps its old line: "The New Prophecy survived both the exorcists and the failed date by two centuries." This places the movement's end about 400, against the brief's sixth century. The card did not change the line (`Card_Edits.md`, Not found), so it was not a passed card edit, and it is already live. It is listed, not changed.
  - The new `dates` (2nd-6th c.) sits beside the old `end` 400.

## Judgment calls

1. I held the two rendering listings, against step 3 as written. Listing them makes the validator fail for a structural reason, not a content one, and the fix depends on Mark's ruling on where tradition cards live.
2. I rewrote the search-name basis and the test fixture against the new brief. Both were mechanical consequences of replacing the longDescription.
3. I applied FIX 4 to `Card_Edits.md` itself (the audit table), as the fix names it, and `dates` to the census.

## Checks (step 5)

| Check | Result |
|---|---|
| `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json` | `629 movements, 736 edges, 10 eras — 0 errors, 4 warnings` (the four shortName warnings already there) |
| `node --test tools/tests/validate_census_*.test.mjs` | first run `tests 118, pass 114, fail 4` (all four in `validate_census_search_names.test.mjs`, the old fixture text); after the fixture fix, that file `tests 6, pass 6, fail 0`. A second full run was stopped part-way (it was slow, about 14 s a test), after it had named the same four failures; the other 112 had passed in the first run. |
| `python -m engine.m6.cli atlas-check` | `"changes": []` |
| `python -m engine.m6.cli atlas-check --edges-only` | `"changes": []` |
| `node tools/build_tree_site.mjs` | `tree site: 1778 own files (the map page slimmed, 629 card files added), 174 shared files, 0 mismatched` |
| `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs` | `tests 80, pass 80, fail 0` |
| `python tools/check_live_commentary.py --base origin/main --enforce` | exit 0 (KEEP and WAIVED lines only) |
| `python tools/check_open_gaps_numbers.py` | exit 0, no output |
| `python tools/check_spelling.py --enforce --base origin/main` | `0 British spelling(s) found in 0 file(s); 0 in enforced trees` |
| `python -m engine.m1.profile_readability` (the brief) | `673 words, grade 9.5 (names out 8.3), reading ease names out 69.7, 19.2 words a sentence ... longest sentence 35 words - pass`; `1 brief(s) graded, 0 failing` |
| `python tools/check_standard_lock.py --base origin/main` | `No locked standard file changed.` |

No check failed on the brief's or the card's content.

## Mark's rulings in the batch, and where each lives

All from the batch README and the CFT Decision-Log, 2026-11-25. None changed a kit line. Each is "this batch only".

- "Batch 11: the slate approved": this batch only.
- "Batch 11: hearts and lengths approved": this batch only.
- "Batch 11: lengths, up to 4:30 and cut at the outline" (Montanism 540): this batch only. The brief runs 673 by the scorer and 675 by `wc -w`, past 540 because of review and grade fixes. This was shown to Mark (README, "For Mark (report, with the briefs)").
- "Batch 11: the first two briefs approved": this batch only (Antioch and the Roman Church; not Montanism).
- "Batch 11: the two long stories": this batch only (Manichaeism and Latin Pastoral).
- "Batch 11: Montanism released alone and recorded": this batch only. Whether traditions keep the council voice line is left for `Recording_Settings.md` after Mark hears it.
- "Batch 11: Montanism fixed and regraded before recording": this batch only. The regrade is C (`Grade2/Grade.md`), and the trust read of the changes is PASS.

## Reference counts beside the batch's

There is no `Reference_Read.md`. The batch README says the tradition kit names no reference stories of its kind, and `Brief-Kit/reference/` holds only person stories (Basil, Epiphanius, Chrysostom). So there is no same-kind reference to set beside these counts. Here are Montanism's fresh-read counts beside the person references in `reference/Scores.md`:

| | Basil | Epiphanius | Chrysostom | Montanism |
|---|---|---|---|---|
| Words | 733 | 756 | 742 | 673 (scorer) |
| Trust read: held / summary holds / softened / assumption / modern / not found | 16/18/0/0/0/0 | 33/7/1/0/0/0 | 26/11/0/0/0/0 | 16/11/0/0/0/0 (`Fresh_Trust.md`) |
| Second trust read | 11/20/0/0/0/0 | 14/10/2/0/0/0 | 26/11/0/0/0/0 | 19/8/0/0/0/0 (`Fresh_Trust_Second.md`, full brief); grade changes 3/5/0/0/0/0 (`Trust_Grade_Changes.md`) |
| Test lines unfilled | 1 (partly) | 0 | 0 | 0 |
| Bare statements | 1 | 0 | 1 | 0 |
| Sentences failing on one hearing | 5 | 4 | 0 | 2 |
| Citations not called for | 1 | 0 | 1 | 0 |
| Tells | 0 | 0 | 0 | 0 |
| Unexplained words | 2 | 2 | 4 | 3 |
| Short-sentence runs | 0 | 0 | 0 | 1 |
| Talking down | 0 | 0 | 0 | 0 |

Montanism's listener counts are from `Fresh_Listen.md`, before the grade fixes.

## Not done

- **Card placement (Mark's ruling):** where a tradition's card fields live; whether the validator checks them and the tree page shows them; and then the two rendering listings above.
- **`start` 165 and `end` 400 (Mark's ruling):** no held source gives either year, and 400 is contradicted (`Card_Check.md`, FIX 4).
- **The new recording** (ruled: council voice, `--char-cap 4000`): not made, as instructed. The page shows no player until it is.
- **Tool gap:** `list_story_status.py` does not count traditions as in the census.
- **Not done here:** commit, pull request, Open-Gaps entries.
