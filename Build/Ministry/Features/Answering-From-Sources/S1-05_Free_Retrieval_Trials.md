# S1-05 free retrieval trials: status after the first pass

Worker for the Library thread. UTC start 2026-10-29 19:35. Stopped twice on Mark's allowance notices. Nothing paid was run: no API call, no hosted embedder.

## Status

| Trial | State | What exists |
|---|---|---|
| A. Free local embedder | Partial. Speed and size measured. No recall measured. | Code, 6,000 passages embedded (old segmentation) |
| B. Context lines written in-plan | Partial. 533 lines written and imported. No before/after recall. | Code, lines, selection rule |
| C. Free keys (sub-question, scripture, work+locus) | Not run. | Design below only |

No recall figure for A, B or C exists yet. The only recall numbers in this file are the existing no-context BM25 baseline, which I reproduced.

## Baseline reproduced (old segmentation, before the curations)

Rebuilt segmenter output and the lpc index on main as of PR #1291 (115,934 passages in 112 files; the earlier bench had 116,116). The bench gave the same 535 cases over 119 pairs and 47 records and the same headline rows:

| Row | @10 | @20 |
|---|---:|---:|
| visitor wording | 1% | 2% |
| wording + label | 2% | 4% |
| record routing (`retrieve_when`) | 31% | 39% |

The bench on the curated segmentation (main now carries 52 curation files) has not been run. The lpc segmentation rebuild after the rebase was started and stopped; see "First thing on resume".

## Trial A: local embedder

- Model: `intfloat/multilingual-e5-small`, int8 ONNX (`model_qint8_avx512_vnni.onnx`), 118 MB, plus a 17 MB tokenizer. Chosen because lpc is 47% Latin, 25% English, 19% French, 6% German, and an English-only model has no chance on the other 75%. 384 dimensions. Fetched from huggingface.co through the proxy with TLS verification on. Installed `tokenizers` only; `onnxruntime` and `numpy` were already present.
- Setup: query and passage prefixes, mean pooling, L2 norm, passages cut to the first 256 tokens (median lpc passage is 243 words, so about the first 60% of a typical passage is embedded; 512 tokens cost 4 times as much).
- Speed on this machine (4 cores shared with other sessions): 110 to 210 s per 1,000 passages at 256 tokens; 692 s per 1,000 at 512 tokens. Shard log median about 175 s per 1,000.
- Can it run in the plan? Yes, but slowly. Full lpc (116,116 passages) is about 5.6 hours of CPU at 175 s per 1,000; the union (354,589) about 17 hours. It uses no tokens and no money, but it holds all four cores and the session must stay alive. Vectors for lpc: 116,116 x 384 x 2 bytes = about 90 MB in float16.
- Run plan: embed the 11 files holding the bench's gold passages first (20,692 passages, 213 gold), then the other lpc passages in a fixed hash order, so recall can be read at several distractor fractions. Done: 6,000 passages, all from the gold files (old segmentation). Because the segmentation changed, these shards are stale for any curated file.
- Language problem, unmeasured: English queries against Latin passages rely on the model's cross-lingual transfer, which is weak for Latin. The gold files include one Latin file (Augustine sermons, 26 gold passages) and three smaller Latin or mixed files.

## Trial B: context lines

- Selection rule: the six files holding the most bench (sub-question, record) pairs; in each, every gold passage and the 10 passages before and after it. 1,551 passages: Cyprian volume `anf05` 410, Augustine Latin sermons 303, `npnf101` 111, `npnf103` 113, `npnf104` 282, `npnf106` 332. Covers 186 of the 213 gold passages. File: `S1-05_Context_Pilot_Lines/selection.json`.
- Done: all 410 `anf05` passages and the first 123 Latin sermon passages (batches 0001 to 0012) written by this session, 533 lines. 95 packets (about 1,000 passages) remain. The lines are in `S1-05_Context_Pilot_Lines/ans_001.txt` to `ans_012.txt`, numbered by packet; they are imported with `context-answer` then `context-import`.
- Method: each packet shows 12 or fewer adjacent passages as the first 110 and last 30 words (long passages are cut, so a line describes the head and tail of a passage, not its middle), the file header, and 60 words of the preceding passage. Lines are one sentence in plain English; no quotation. I wrote them from the passage only and did not consult the bench queries, but I knew which passages were gold, so the selection is not blind.
- Vocabulary check result (the existing `check_context_line`): of 533 imported lines, 272 pass and 261 are flagged (flagged lines stay out of the index). Two causes:
  1. A real defect, fixed: straight and curly apostrophes compared as different words ("God's" against "God’s"). The check now normalises them.
  2. A design limit, not fixed: the novelty rule counts every English word not found in the passage as invented. For a Latin passage that is every content word, so nearly every English line on a Latin file is flagged; in the Latin file 221 entity flags are plain words such as God, Church, Father. As written, the check cannot pass cross-language lines, which is where a context line would help most. Decision for Mark: relax the novelty rule for non-English files (keep the name and number test), or accept that the check admits only same-language lines.
- Not done: rebuild the index with the lines, measure the cases whose gold lies in the pilot files before and after, extrapolate to lpc. When measured, report two arms: lines that passed the check, and all lines, labelled as such.

## Trial C: free keys

Not run. Design, so the next pass can start:

- Held-out sub-question key: for each (sub-question, record) case, build the key from the other records of that sub-question (leave-one-out), never from the scored record. Report recall with BM25 ranking inside the key's file set, and separately the share of cases where the key shares a gold passage with another record (leakage), and recall with those cases removed. Sub-questions with one record cannot be scored this way.
- Coverage-map `source_hits`: file-level candidate set, BM25 inside it. Only cells with hits can be scored; most lpc cells in the bench have none, so the key can show little.
- Scripture and work+locus keys: `PASSAGES.sqlite` was not built; extracting references from visitor wording is expected to apply to the verse questions only (C5.S8, 14 cases).

## Code changes (all tested, in this branch)

- `Sandbox/answering-library/index/dense.py`: ONNX embedder, resumable shards, cosine ranking, reciprocal rank fusion.
- `index/trials.py`: gold cache keyed on passage spans, pilot selection, embedding order, recall tables.
- `index/contextwork.py`: packet export, numbered-answer parser, import with the vocabulary check, refusal of repeated, missing or hash-mismatched answers.
- `index/cli.py`: `embed`, `context-select`, `context-export`, `context-answer`, `context-import`.
- `index/bench.py`: `run_bench` takes an optional ranker and a gold cache.
- `index/check.py`: apostrophe normalisation.
- `answering_library/markers.py`: root-cause fix. `_ROMAN_SHAPE` used `re.I` on Unicode text, so the dotless `ı` matched a Roman `I` and crashed the segmenter on current main (`KeyError: 'ı'`). It is now ASCII-only, with a test. Without this, main's segmenter does not finish.
- Tests: `index/tests/test_trials.py` (7), one added to `tests/test_segmenter.py`.

## What the numbers do and do not show

They show only that the keyword baseline reproduces and that the embedder is affordable in time. They do not show whether a local embedder or context lines move recall. Do not read the 6,000 embedded passages or the 272 passing lines as a result.

## First thing on resume

1. Run the segmenter then `build-index --world lpc` on this branch (about 10 minutes; the manifest records the curations) and run the bench for the curated baseline.
2. Re-run `context-export` for the pilot (passage ids change in curated files; re-import and check which lines still match by text hash), finish the 95 packets, rebuild with `--db out/index/lpc_ctx.sqlite`, compare.
3. Re-embed on the curated segmentation (gold files first), add a dense-bench command using `run_bench(rank=...)`, report dense-only and rank-fused recall at @10/@20.
4. Trial C.

No hosted embedder is proposed or authorized.
