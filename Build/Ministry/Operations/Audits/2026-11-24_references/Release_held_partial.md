# Release: the three person references

Basil of Caesarea (`basil-of-caesarea`), Epiphanius of Salamis (`epiphanius-of-salamis`) and John Chrysostom (`john-chrysostom`), brought to the kit of 2026-11-24 (Open-Gaps 406). A fix to live texts, run as a batch of its own. No new entries.

## What changed

### The checks applied

- **Basil, `Card_Check.md` (FIX).** Changes 1-5 and 7-18 applied word for word to `basil-of-caesarea.card.json`: the editors' dates taken out of `keyWorks[2].about`, `briefReferences[0]`, `[5]` and `[6]`, `datesNote`, `legacy.traces[0]` and `[6]`, `legacy.remembered[1]` and `uncertain[0]`-`[3]`, `[5]`-`[7]` and `[9]`; `uncertain[8]` (Hefele's synods) removed, so the old `[9]` and later items move up one. Change 6 applied to `Card_Edits.md`: its "Not found" bullet replaced by the new line on Letter 223.5, and the first "Left as they stand" bullet removed.
- **Epiphanius, `Card_Check.md` (PASS).** Nothing to apply.
- **Chrysostom, `Card_Check.md` (FIX).** Fix 1 applied: the clause on Stephens's note cut from `quotationOriginals[0].uncertain`.
- **`Second_Readings.md`.** `quotationOriginals[0].secondReading` and `[1].secondReading` set to "same" on Chrysostom's card. No reading changed meaning, so no brief sentence changed and nothing went for a targeted check.

### The census (`cic-website/data/world-census.json`)

For each of the three entries:

- `longDescription` is the batch's final brief, final newline removed. Each equals the frozen copy in `Brief-Kit/reference/<slug>/`.
- `card` is the batch's final card.
- `modernWorks`, new, placed before `card`: Basil 14 works, Epiphanius 5, Chrysostom 5, as listed under Entry fields in each `Card_Edits.md`.

Entry fields from `Card_Edits.md` that the checkers passed, word for word:

- Basil: `why`, `relationsSummary`, `teaser`.
- Epiphanius: `teaser`.
- Chrysostom: none (`Card_Edits.md` proposes no change to `why`, `relationsSummary`, `teaser`, `legacy`, `voices` or `sourcing`).

No other field changed. No tradition link was added, since there are no new entries.

### `tools/quote_renderings.json`

Two listings added for Chrysostom, each with `second_reading` pointing at this batch's `Second_Readings.md`, verdict "same":

- Q1, "When everyone ignored him...": Greek, `john-chrysostom_opera-pg52-epistulae-grc-lat_migne1862.txt` 822-827.
- Q2, "Do you want to honor Christ's body?...": English printed 1888, `npnf110_chrysostom-homilies-matthew.xml` 29931-29933.

Q3, "Glory to God for all things.", stands verbatim in Moore's English (`palladius_dialogue-life-of-chrysostom_moore1921.txt` 6498-6499) and needs no listing. Basil's three and Epiphanius's two listings stand as they were: their spans are unchanged in the new briefs. No listing was removed.

### Rebuild

- `atlas-sync` changed `cft-website/index.html` only, for these three entries. A second run reports `"changed": false`.
- `generate_tree_pages.mjs` regenerated 629 pages. Only `cft-website/tree/basil-of-caesarea.html`, `epiphanius-of-salamis.html` and `john-chrysostom.html` changed.
- `corpus_coverage.py` left `cic-website/data/corpus-coverage.json` unchanged. Every file the new cards cite was already counted.

Nothing else changed.

### Audio

Nothing recorded and no audio file deleted.

- `python Build/tools/align_tree_narration.py --check` lists `basil-of-caesarea` and `epiphanius-of-salamis` (exit 1): their paragraph times are stale against the new texts.
- Chrysostom has no paragraph times, so the check does not list him. His recording no longer matches his text either.
- None of the three tree pages now shows Listen. Basil's and Epiphanius's showed it before this release; Chrysostom's already did not.

### The ledger

None of the three stories was in `Earlier-Approved.yaml`, so nothing was removed. `python tools/list_story_status.py --write` left the ledger unchanged: all three were already listed on the kit (Basil and Epiphanius batch 9, Chrysostom batch 10).

## Judgment calls

1. **Where `modernWorks` sits.** Basil's `Card_Edits.md` says to place it before `card`. The other two give no place, so theirs go there too, for one shape across entries. These are the census's first `modernWorks`.
2. **Basil's and Epiphanius's listings keep their earlier records.** The prompt points `second_reading` at this batch's `Second_Readings.md`. That file reads only Chrysostom's two quotes. The other five quotes are carried unchanged, so their listings still point at the batch-9 readings that hold them.
3. **Basil's `Card_Edits.md` card edit 1** still says the year stays in `datesNote`, credited to Jackson. Card_Check change 7 overturns that, but it does not ask for the sentence to be edited, so the sentence is left as it stands.

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
| same, Epiphanius | `744 words, grade 8.9 (names out 7.3), reading ease names out 74.2, 17.7 words a sentence, 0.8 joining words per 100, 7% short sentences, longest sentence 31 words - pass` |
| same, Chrysostom | `742 words, grade 8.8 (names out 8.2), reading ease names out 69.9, 19.0 words a sentence, 0.4 joining words per 100, 13% short sentences, longest sentence 35 words - pass` |
| `python tools/check_standard_lock.py --base origin/main` | **FAIL**: `this pull request changes the locked writing standard` (10 files under `Brief-Kit/`: `kinds/person.md`, `reference/Scores.md` and the three reference folders). `It needs a new entry in Build/Ministry/Features/Church-Family-Tree/Decision-Log.md whose heading or **Decided** line names Mark and which quotes his words.` |

The standard-lock failure comes from the coordinator's commit `a46fbcb4` (the references frozen in `Brief-Kit/reference`). It does not come from this release, and the fix is a Decision-Log entry, which is the coordinator's to write. It is not mechanical within this step and is left open.

## Mark's rulings in the batch, and where they live

- **"keep them as they are, approved"** (2026-11-24, on the page https://claude.ai/artifact/LyXy1LGWYovdCDG3ADzUgB). This keeps all three lengths. It approves Chrysostom's two-sentence essence, the fresh-read counts as the `Scores.md` counts, and the three briefs. It lives in this batch only (batch README, Rulings). The counts are now in `Brief-Kit/reference/Scores.md`, under Person.
- **On length: "no, then we will end up with 8 minute audio for some and thats to long. these i approaved because they were close"**, beside "we don't want to leave anything critical out". The kit's length lines do not change. It lives in this batch only (batch README, Rulings). The three lengths stand because they were close, not as a precedent.

The Decision-Log carries no entry for either ruling yet; see the standard-lock check above.

## The reference counts

There is no `Reference_Read.md`. This batch's fresh reads are the references' counts (batch README, judgment call 2). So the counts the fresh reads recorded and those now in `Scores.md` are the same reads, and they match:

| | Basil | Epiphanius | Chrysostom |
|---|---|---|---|
| Words, frozen brief | 733 | 744 | 742 |
| Trust: sentences / held / summary holds | 34 / 16 / 18 | 41 / 33 / 7 | 37 / 26 / 11 |
| Trust: softened or changed | 0 | 1 | 0 |
| Trust: assumption added, modern only, not found | 0, 0, 0 | 0, 0, 0 | 0, 0, 0 |
| Listener: test lines unfilled | 1 (partly) | 0 | 0 |
| Listener: bare statements | 1 | 0 | 1 |
| Listener: sentences failing on one hearing | 5 | 4 | 0 |
| Listener: citations read aloud not called for | 1 | 0 | 1 |
| Listener: unexplained words | 2 | 2 | 4 |
| Listener: tells, short-sentence runs, talking down | 0, 0, 0 | 0, 0, 0 | 0, 0, 0 |

**The batch's faults beside theirs.** The batch's stories are the references themselves, so its faults are these counts. Each fresh read's exact changes were applied word for word, so the frozen briefs carry the fix for every blocking finding counted here: Basil's listener blocking point, Epiphanius's one softened clause and Chrysostom's bare sentence. There is no separate batch score to set beside them.

## What is not done

- **The standard lock** fails until the coordinator adds the Decision-Log entry for the freeze.
- **Audio.** Basil's, Epiphanius's and Chrysostom's recordings no longer match their texts. Their players are hidden. Nothing is recorded or deleted.
- **Epiphanius's `dates`, `start`, `end` and `activeYear`** rest only on editors' years and feed the timeline. Left unchanged; this is a fleet-level call (batch README, Open items).
- **Basil's `dates`, `start` and `end`** raise the same question (Basil `Card_Check.md`, Considered). Left unchanged.
- **Not committed**, per the prompt. Kit, `Scores.md`, Decision-Log and Open-Gaps are left to the coordinator.
