# Cross-world baseline test, 2026-11-02

Engine code, directives and read criteria frozen at `main` `a61c37f2` (the merge of #1450, Decision-Log 63 and 64). No world-specific record, sidecar or retrieve_when edits and no tuning before or between runs. One run per world. Nothing here was changed after it ran.

## What was run

- Worlds: `alx` (Alexandrian Christianity), `syr` (Syriac Christianity), `rzg` (Reformed Zurich and Geneva), with `lpc` beside them (its run is the `lpc` run of 2026-11-02 on the same frozen code, 28 sealed questions of 50).
- Questions: the 28 sealed probes, same wording in every world (`canon/sealed_probes`, read by probe id).
- Sidecar: built mechanically per world by `tools/build_answers_sidecar.py` from the fleet coverage maps, unreviewed (`*/..._Answers_Sidecar.yaml` in each world folder; alx 50, syr 56, rzg 39 of 130 sub-questions hold records). `lpc` used its hand-reviewed sidecar. Joining sentences: an empty list for the three new worlds.
- Pipeline: reader names a sub-question, offer by sub-question, bound drafting, one batched read, one rewrite, a read of the rewrite, compose (`engine.m3.test100`, `test100_bound`, `test100_check`, `test100_log`). Helper agents stood in for every model call (reader and safety classification, drafting, read, rewrite, re-read), the same method as the lpc runs.
- Old answers: the saved gate-replay sentences (`Stage1/data/gate-replay/<world>.jsonl`) with `removed=false` only (what the old engine showed), joined per probe. For `lpc` this replaces my earlier table that also counted sentences the old gates removed (45 of 489).
- Rating: one Opus reader per world, blind, 28 old and 28 new answers in random order (shuffle seed 20261114, written before the draw), one rubric: answers the question (yes, partly, no), depth (rich, adequate, thin, flat), plain to hear, speaks as the community, accuracy (ok, tier3, tier2, tier1). Separately, one Opus reader per world judged whether a record that fits the question was in the offer and whether one exists anywhere in the world's records.

## Results, per world, not pooled

| World | | Answers the question yes/partly/no | Depth rich/adequate/thin/flat | Plain to hear yes | Speaks as the community yes | Accuracy ok/tier3/tier2/tier1 |
|---|---|---|---|---|---|---|
| alx | old | 28 / 0 / 0 | 22 / 6 / 0 / 0 | 27 | 27 | 10 / 12 / 6 / 0 |
| alx | new | 14 / 5 / 9 | 3 / 13 / 7 / 5 | 21 | 16 | 10 / 18 / 0 / 0 |
| syr | old | 26 / 2 / 0 | 16 / 11 / 1 / 0 | 27 | 25 | 15 / 6 / 6 / 1 |
| syr | new | 14 / 11 / 3 | 2 / 17 / 6 / 3 | 27 | 19 | 19 / 8 / 1 / 0 |
| rzg | old | 24 / 4 / 0 | 20 / 8 / 0 / 0 | 27 | 28 | 11 / 7 / 9 / 1 |
| rzg | new | 12 / 10 / 6 | 2 / 16 / 8 / 2 | 27 | 24 | 16 / 12 / 0 / 0 |
| lpc | old | 19 / 9 / 0 | 8 / 16 / 4 / 0 | 25 | 27 | 16 / 9 / 1 / 2 |
| lpc | new | 14 / 11 / 3 | 2 / 18 / 7 / 1 | 25 | 19 | 19 / 9 / 0 / 0 |

| World | Clean | Rewritten | Abstained | Fitting record in the offer yes/partly/no | Fitting record exists in the world yes/partly/no | Exists in the world but not fully offered |
|---|---|---|---|---|---|---|
| alx | 11 | 13 | 4 | 18 / 8 / 2 | 21 / 7 / 0 | 3 |
| syr | 10 | 18 | 0 | 15 / 9 / 4 | 25 / 3 / 0 | 10 |
| rzg | 18 | 9 | 1 | 8 / 12 / 8 | 8 / 17 / 3 | 0 |
| lpc | 9 | 18 | 1 | 14 / 11 / 3 | 15 / 13 / 0 | 1 |

Question by question: `ratings/cw_<world>_rated.json` (with `cw_<world>_key.json` for which answer is old or new), `ratings/cw_<world>_offerfit.json`.

## The lpc runs

Every lpc run held by the Engine thread, with the code each ran on and its seed, is in `lpc-runs/INDEX.md` (tarballs of each work folder, the run9 directive patch, the offer and routing analyses and the pages put to Mark).

## Mechanical notes

- Story markers: the three new worlds' drafting helpers placed no `[[story:id:length]]` markers (no file they were given defined the length values), so the story door was not exercised there. Quote markers were placed.
- `syr` q014: the first draft failed shape and a second draft request was made and answered (`syr/replies/q014.voice.2.txt`).
- Several reads and re-reads reported a PLACED sentence while the PLACED PASSAGES list read "(none)"; the readers added an entry for the record as the prompt asks.
- Full stop after the tags: helpers differed on where it goes; the bound step accepted all of them (the earlier lpc run's stray full stop after the tags was not seen).
- The `lpc` folder holds the whole 50-question run; only q001 to q028 are in the comparison.

## What cannot be compared, and what is confounded

- The writer differs: old answers were written by the old engine with a live model, new answers by helper agents. That confounds most the columns that depend on how the answer is written: speaks as the community, plain to hear, and depth. It also bears on answers the question. It does not confound accuracy (judged against the records and texts), the sub-question routing, whether a fitting record was in the offer, or the abstention and shipped counts (decided by the engine's checks, though the checks' reads were also helper-written).
- The old engine's offer was not saved, so offer fit is judged against what the world holds, not against the old offer.
- The old answers are gate-replay sentences, not full conversations. The sealed probes are generic paraphrases, so they test the sealed cells, not each world's strongest material. One run per world, no variance estimate; each rating is one reader's view.
- Not run: the 106 set (written around lpc records and dates), per-world question sets, any record, sidecar or directive change.
