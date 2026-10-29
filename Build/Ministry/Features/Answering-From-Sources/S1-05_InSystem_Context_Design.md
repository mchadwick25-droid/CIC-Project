# S1-05 optional step: context lines written in-system, no API

Status: design only, optional, not authorized, nothing run. It is put to Mark only if the lpc retrieval bench (`S1-05_lpc_Retrieval_Bench.md`) shows the no-context index misses evidence that a context line would reach.

## What it is

The no-context index already carries an empty `context` column that is searched together with the passage text and is never shown as source. This step fills that column for lpc's passages. The lines are written by a Claude Code session working through batch files on disk, inside the session's own allowance. No API client is built or called, so the live-test guard has nothing to guard and no dollars are metered.

## Batch format

One batch is one window, built by the same window builder the metered design used (`windows.build_windows`): the work header, the whole division (or the run of passages that fits under 9,000 tokens), merged with neighbouring divisions up to 4,300 tokens. A window holds about 5 to 25 passages.

`context-export --world lpc --out <dir>` writes, per window, one packet `<file-stem>/<batch-no>.in.jsonl`:

- Line 1: `{"batch_id", "prompt_version", "instruction", "work_header", "file", "targets": [passage_id, ...]}`. The instruction is the same system prompt the metered design used (one sentence, at most 60 words, only facts in the header and the stretch, no quotation).
- One line per passage in the window: `{"passage_id", "division_locus", "division_title", "text_hash", "text"}`. Edge passages carry `"before"` and `"after"` fields with the 60 words just outside the window.

The session returns `<file-stem>/<batch-no>.out.jsonl`, one line per target: `{"passage_id", "text_hash", "context"}`.

## How a session fills the column

1. The exporter lists packets with no valid answer file. The session reads a packet and writes the answer file. Work is delegated to subagents, one per batch or per few batches, so exploration and reading do not grow the main thread; mechanical batches go to the cheapest model the usage rules allow.
2. `context-import <dir>` validates each answer file and only then writes records into the same `out/context/<file-stem>.jsonl` the metered path used, with the same fields (`passage_id`, `text_hash`, `prompt_version`, `context`, `status`, `reasons`) and `model_id` set to `claude-code-session:<model name>`, `usage` null, `live_test` null.
3. Import refuses a file that names a passage not in the packet, repeats one, omits one, or echoes a `text_hash` that differs from the packet's. A refused batch is exported again; a good one is never redone (resume keys are passage id, text hash, model id, prompt version).
4. `build-index` picks up the lines whose status is ok and rebuilds.

## How it is checked

- Mechanical: the existing vocabulary check (`check.check_context_line`) runs at import against the same supplied text the writer saw: registry header, window, edge snippets. A name, date or number not in that text, a line over 80 words, or a high share of words not in the text sets `status: flagged`. Flagged lines stay in the log and stay out of the index.
- By eye: Mark reads nine pairs per file with `show-sample` (context line beside its passage), as for the metered sample. The bad cases are the five on the sample card: an added fact, a restated passage, a generic line, the wrong place, a voice the segmenter did not mark.
- Independence: a separate subagent re-reads a random tenth of the imported lines against their windows and marks any it would not accept; its marks go to the log, not into the index.

## How it is versioned

The index version is a hash over each passage's id, text hash and context line, plus the model id and the pipeline code hash. For session-written lines the model id is the sorted set of `claude-code-session:<model>` values present, which joins the hash, so a different writing model or a changed prompt version gives a different index version. The code hash covers the prompt text, the window rules and the check. Changing any of these invalidates only the lines whose resume key no longer matches; the rest are kept.

## What it costs

Money: nothing metered. Allowance: every window is read once and about 50 tokens are written per passage. For lpc the estimator puts the passage text at about 49M to 61M tokens and 100,000 passages, so the session throughput is about 50M to 60M tokens read plus about 5M written. That is a large draw on the weekly allowance, and the share is not known. A pilot of one file (about 100 passages, 5 to 10 windows) measures the allowance used per passage before anything larger is chosen; the figure from the pilot decides whether lpc, a part of lpc, or none is worth it.

## What changes in the code when this is built

- `export.py` and `importer.py` for the two commands above, reusing `windows`, `prompting`, `check`, `generate.read_context_lines`.
- A `source` field on context records and a `context_models` entry in the index meta, included in the version hash.
- A test with a fake session: export, write answers, import, refuse a bad answer, rebuild, search by a word only the context line holds, and confirm the hit's `text` is the unchanged passage.

## Transparency

Unchanged from the no-context index. The context line is stored in its own column, used only to match, never returned as or inside source text. Every hit still returns its passage id, vendored file path, byte span, division locus and title, speaker, OCR score, row ids, worlds and roles, so the marked text, the hover and the click-through reach the passage and its document exactly as without a context line.
