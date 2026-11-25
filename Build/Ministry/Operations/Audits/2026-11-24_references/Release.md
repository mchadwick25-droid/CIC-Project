# Release: the three person references

Basil of Caesarea (`basil-of-caesarea`), Epiphanius of Salamis (`epiphanius-of-salamis`) and John Chrysostom (`john-chrysostom`), brought to the kit of 2026-11-24 (Open-Gaps 406). A fix to live texts, run as a batch of its own. No new entries.

This release was done afresh on the final files after the hold of 2026-11-24. `Release_held.patch` was read only as a guide. Each result below was then compared with it. The batch-folder edits and `tools/quote_renderings.json` came out byte for byte the same. The census, the map page and the tree pages differ from the held patch only where the batch changed after the hold: the new Basil and Epiphanius briefs, and Epiphanius's card edits 20 and 21.

## What changed

### The checks applied

- **Basil, `Card_Check.md` (FIX).** Changes 1-5 and 7-18 applied word for word to `basil-of-caesarea.card.json`:
  - the editors' dates taken out of `keyWorks[2].about`, `briefReferences[0]`, `[5]` and `[6]`;
  - `datesNote` and `legacy.traces[0]` and `[6]`;
  - `legacy.remembered[1]`;
  - `uncertain[0]`-`[3]`, `[5]`-`[7]` and `[9]`.

  `uncertain[8]` (Hefele's synods) is removed, so the old `[9]` and later items move up one. Change 6 is applied to `Card_Edits.md`: its "Not found" bullet is replaced by the new line on Letter 223.5, and the first "Left as they stand" bullet is removed.
- **Epiphanius, `Card_Check.md` (PASS, and the follow-up check of 2026-11-25 PASS).** Nothing to apply. Edits 20 and 21 were already on the card.
- **Chrysostom, `Card_Check.md` (FIX).** Fix 1 applied: the clause on Stephens's note is cut from `quotationOriginals[0].uncertain`.
- **`Second_Readings.md`.** On Chrysostom's card, `quotationOriginals[0].secondReading` and `[1].secondReading` are set to "same", placed after `lines` as in Q3. No reading changed meaning, so no brief sentence changed and nothing went for a targeted check.

### The census (`cic-website/data/world-census.json`)

For each of the three entries:

- `longDescription` is the batch's final brief, with its final newline removed. Each brief equals its frozen copy in `Brief-Kit/reference/<slug>/`.
- `card` is the batch's final card.
- `modernWorks` is new and placed before `card`: Basil 14 works, Epiphanius 5, Chrysostom 5. Each list is taken as given under Entry fields in that story's `Card_Edits.md`.

Entry fields from `Card_Edits.md` that the checkers passed, applied word for word:

- Basil: `why` (equal to the exact text in `Card_Check.md`), `relationsSummary` and `teaser`.
- Epiphanius: `teaser`.
- Chrysostom: none (`Card_Edits.md` proposes no change to `why`, `relationsSummary`, `teaser` or `legacy`).

No other field changed. No tradition link was added, since there are no new entries.

### `tools/quote_renderings.json`

Two listings are added for Chrysostom. Each has `second_reading` pointing at this batch's `Second_Readings.md`, with the verdict "same":

- Q1, "When everyone ignored him...": Greek, `john-chrysostom_opera-pg52-epistulae-grc-lat_migne1862.txt` 822-827.
- Q2, "Do you want to honor Christ's body?...": English printed 1888, `npnf110_chrysostom-homilies-matthew.xml` 29931-29933.

Q3, "Glory to God for all things.", stands verbatim in Moore's English (`palladius_dialogue-life-of-chrysostom_moore1921.txt` 6498-6499), so it needs no listing. Basil's three listings and Epiphanius's two stand as they were. Each of their spans still stands word for word in its new brief, and `tools/list_second_readings.py` reports all eight spans across the three stories as CARRIED. No listing was removed.

### Rebuild

- `atlas-sync` changed `cft-website/index.html` only, for these three entries. A second run reports `"changed": false`.
- `generate_tree_pages.mjs` changed only `cft-website/tree/basil-of-caesarea.html`, `epiphanius-of-salamis.html` and `john-chrysostom.html`.
- `corpus_coverage.py` (629 entries, 303 with vendored coverage) left `cic-website/data/corpus-coverage.json` unchanged.

Nothing else changed in the tree.

### Audio

Nothing was recorded and no audio file was deleted. All three mp3 files remain in `cft-website/audio/tree/`.

- `python Build/tools/align_tree_narration.py --check` lists `basil-of-caesarea` and `epiphanius-of-salamis` (exit 1). Their paragraph times are stale against the new texts.
- Chrysostom has no paragraph times, so the check does not list him.
- None of the three tree pages now shows the Listen player. Basil's and Epiphanius's pages showed it before this release. Chrysostom's did not.

### The ledger

None of the three stories was in `Earlier-Approved.yaml`, so nothing was removed. `python tools/list_story_status.py --write` left the ledger unchanged.

## Judgment calls

1. **Where `modernWorks` sits.** Basil's `Card_Edits.md` says to place it before `card`. The other two give no place, so theirs go there too, giving one shape across entries. These are the census's first `modernWorks`.
2. **Basil's and Epiphanius's listings keep their earlier records.** The prompt points `second_reading` at this batch's `Second_Readings.md`, but that file reads only Chrysostom's two quotes. The other five quotes are carried unchanged, so their listings still point at the batch-9 readings that hold them.
3. **Basil's `Card_Edits.md`, card edit 1,** still says the year stays in `datesNote`, credited to Jackson. Card_Check change 7 overturns that, but it does not ask for that sentence to be edited, so the sentence is left as it stands.

## The checks

| Check | Output line |
|---|---|
| `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json` | `629 movements, 736 edges, 10 eras — 0 errors, 4 warnings` (the four `shortName` warnings, all on other entries) |
| `node --test tools/tests/validate_census_*.test.mjs` | CENSUS_TESTS |
| `python -m engine.m6.cli atlas-check` | ATLAS_CHECK |
| `python -m engine.m6.cli atlas-check --edges-only` | ATLAS_EDGES |
| `node tools/build_tree_site.mjs` | `tree site: 1778 own files (the map page slimmed, 629 card files added), 174 shared files, 0 mismatched, in .build/tree/` |
| `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs` | `# tests 80`, `# pass 80`, `# fail 0` |
| `python tools/check_live_commentary.py --base origin/main --enforce` | exit 0 (KEEP and WAIVED lines only) |
| `python tools/check_open_gaps_numbers.py` | exit 0, no output |
| `python tools/check_spelling.py --enforce --base origin/main` | `0 British spelling(s) found in 0 file(s); 0 in enforced trees` |
| `python -m engine.m1.profile_readability`, Basil | `733 words, grade 8.7 (names out 7.9), reading ease names out 73.8, 19.8 words a sentence, 0.7 joining words per 100, 11% short sentences, longest sentence 34 words - pass` |
| same, Epiphanius | `756 words, grade 9.0 (names out 7.4), reading ease names out 73.8, 18.0 words a sentence, 0.8 joining words per 100, 7% short sentences, longest sentence 38 words - pass` |
| same, Chrysostom | `742 words, grade 8.8 (names out 8.2), reading ease names out 69.9, 19.0 words a sentence, 0.4 joining words per 100, 13% short sentences, longest sentence 35 words - pass` |
| `python tools/check_standard_lock.py --base origin/main` | exit 0: `Locked standard files changed, with a new Decision-Log entry carrying Mark's words:` (`kinds/person.md`, `reference/Scores.md` and the three reference folders) |

The standard lock failed in the held run. It passes now, on the coordinator's Decision-Log entry of 2026-11-25.

## Mark's rulings in the batch, and where they live

- **"keep them as they are, approved"** (2026-11-24, on the page https://claude.ai/artifact/LyXy1LGWYovdCDG3ADzUgB). This keeps all three lengths and approves the three briefs. It also approves Chrysostom's two-sentence essence and the fresh-read counts as the `Scores.md` counts. It applies to this batch only. It is recorded in the batch README (Rulings) and the Decision-Log ("The three person references brought to the kit, frozen and released", 2026-11-25, decision 1). The counts are in `Brief-Kit/reference/Scores.md`, under Person.
- **On length: "no, then we will end up with 8 minute audio for some and thats to long. these i approaved because they were close"**, said beside "we don't want to leave anything critical out". It applies to this batch only, and the kit's length lines do not change. It is recorded in the batch README (Rulings) and the Decision-Log (same entry, decision 2).
- **"a, second trust read on changed sentences"**, and on the sermons line, "it is ok to use later sources to show impact if they are reliable". The second trust read went into the kit by its own pull request, #1802 (kit). The sermons ruling applies to this batch. Both are recorded in the batch README (Open items, "After the hold") and the Decision-Log (same entry, decisions 3 and 4).

## The reference counts

There is no `Reference_Read.md`. This batch's fresh reads are the references' counts (batch README, judgment call 2). The counts the batch's reads recorded and those in `Scores.md` are therefore the same reads. I checked them against `Fresh_Read.md` and each story's `Second_Trust.md`, and they match.

| | Basil | Epiphanius | Chrysostom |
|---|---|---|---|
| Words, frozen brief | 733 | 756 | 742 |
| Trust: sentences / held / summary holds | 34 / 16 / 18 | 41 / 33 / 7 | 37 / 26 / 11 |
| Trust: softened or changed | 0 | 1 | 0 |
| Trust: assumption added, modern only, not found | 0, 0, 0 | 0, 0, 0 | 0, 0, 0 |
| Listener: test lines unfilled | 1 (partly) | 0 | 0 |
| Listener: bare statements | 1 | 0 | 1 |
| Listener: sentences failing on one hearing | 5 | 4 | 0 |
| Listener: citations read aloud not called for | 1 | 0 | 1 |
| Listener: unexplained words | 2 | 2 | 4 |
| Listener: tells, short-sentence runs, talking down | 0, 0, 0 | 0, 0, 0 | 0, 0, 0 |
| Second trust: changed sentences / held / summary holds | 31 / 11 / 20 | 26 / 14 / 10 | 37 / 26 / 11 |
| Second trust: softened or changed | 0 | 2 | 0 |

**The batch's faults beside theirs.** The batch's stories are the references themselves, so their faults are these counts. Each read's exact changes were applied word for word:

- Basil's listener blocking point.
- Epiphanius's one softened clause in the fresh read.
- Epiphanius's two softened sentences in the second trust read. Both exact sentences stand in the brief.
- Chrysostom's bare sentence.

The frozen briefs therefore carry the fix for every blocking finding counted here. There is no separate batch score to set beside them.

## What is not done

- **Audio.** Basil's, Epiphanius's and Chrysostom's recordings no longer match their texts, so their players are hidden. Nothing is recorded or deleted (Open-Gaps 413).
- **Epiphanius's `dates`, `start`, `end` and `activeYear`** rest only on editors' years and feed the timeline. They are left unchanged (Open-Gaps 414). Basil's `dates`, `start` and `end` raise the same question (Basil `Card_Check.md`, Considered) and are also left unchanged.
- **Originals not held** for Chrysostom's Homily 50 on Matthew and Epiphanius's Letter 51 (Open-Gaps 415).
- **Not committed**, per the prompt. The Kit, `Scores.md`, the Decision-Log and Open-Gaps are left to the coordinator.
