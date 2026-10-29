# S1-05 sample card: contextual indexing, lpc sample

Status: PENDING THE SEGMENTER: the segmenter's output (the passages folder of the answering-library out directory) does not exist yet. The files below are the default pick and every count is modeled from word counts at about 275 words a passage. Run the selector once the segmenter lands, then regenerate this card; the counts, the file list and the cap are recomputed.

Nothing has been run. No model call and no paid call was made to prepare this card. The run waits for Mark to approve this sample by name and set the cap (root CLAUDE.md, metered spend and paid bulk runs).

## What Mark is asked to approve

- Model: `claude-haiku-4-5-20251001` (Haiku 4.5 class, priced from `engine/m8/price_tables.py`).
- What it writes: one context line of at most 60 words per passage, placed in front of the passage in the search index only.
- Window: one call per passage; cached prefix = system instruction + work header + the whole division (or, for a division over 9000 tokens, the run of passages that fits), merged with neighbouring divisions until the prefix reaches 4300 tokens (the cache minimum, with margin); fresh part = the target's id plus, at a window edge, the last/first 60 words of the passage just outside; reply of at most 60 words.
- Sample: 242 passages in 3 lpc files, about 0.13M to 0.16M text tokens.
- Estimated cost: $0.36 to $0.57 on the standard path.
- Cap recommended: $3.00 (5 times the high estimate, rounded up, floor $1.00); that is 1.5% of the $200 indexing ceiling. The guard stops the run before the cap and the run resumes where it stopped.
- Suggested live-test name: `S1-05 contextual indexing lpc sample`.

## Files

| Role | File | Language | Passages | Text tokens (low to high) | Cost, low to high |
|---|---|---|---:|---|---|
| XML edition with divisions (English) | `npnf104_augustine-anti-manichaean-anti-donatist.xml` | eng | 150 | 76,224 to 94,384 | $0.22 to $0.35 |
| plain text, Latin | `cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt` | lat | 47 | 28,972 to 35,934 | $0.07 to $0.11 |
| plain text from a scan, French; the weak-OCR case | `hefele-leclercq_histoire-des-conciles-tome1-1-cyprien-novatiens-baptheme-slice-fra_1907.txt` | fra | 45 | 22,764 to 28,185 | $0.07 to $0.10 |

lpc's plain-text files hold no Greek-script characters (checked on the file contents), so this sample covers Latin script only, in three languages: Latin, English and French. A Greek check would need a file from the Cappadocian shelf; say so and the selector adds one small slice.

## Settings as the run prints them

```
CONTEXTUAL INDEXING RUN SETTINGS
live test: S1-05 contextual indexing lpc sample
cap: $3.00
model id: claude-haiku-4-5-20251001 (priced from engine/m8/price_tables.py: $1 in, $5 out, $1.25 cache write, $0.1 cache read, per million tokens)
prompt version: ctx-1
window definition: one call per passage; cached prefix = system instruction + work header + the whole division (or, for a division over 9000 tokens, the run of passages that fits), merged with neighbouring divisions until the prefix reaches 4300 tokens (the cache minimum, with margin); fresh part = the target's id plus, at a window edge, the last/first 60 words of the passage just outside; reply of at most 60 words
- Files: 3 (0 with segmenter output, 3 modeled from word counts)
- Passages: 242 (modeled at about 275 words each where not segmented)
- Windows (cached prefixes): 21
- Passage text tokens: 127,960 (low band) / 158,503 (high band)
- Input tokens, cached prefix (written once, then read): 1,085,499 (low band) / 1,937,187 (high band)
- Input tokens, fresh: 24,521 (low band) / 20,121 (high band)
- Output tokens: 13,299 (low band) / 24,180 (high band)
- Estimated cost, standard path (low to high): $0.36 to $0.57
- Cap against the estimate: $3.00 covers the high estimate $0.57
output path: the context folder of the answering-library out directory (gitignored)
```

Counts on the Input lines are token estimates from character counts (no tokenizer runs offline). The run's own usage log replaces them with measured tokens after the first calls.

## Commands

Select the sample from the segmenter's output (free, no network):

```
python Sandbox/answering-library/index/cli.py sample-select --world lpc
python Sandbox/answering-library/index/cli.py run --sample lpc --dry-run
```

Run after approval (live-tests environment only; the key is never set on Render). `NAME` and `CAP` are the approved values:

```
CIC_MODEL_ROUTE=anthropic CIC_ANTHROPIC_API_KEY=<live-tests key> \
python Sandbox/answering-library/index/cli.py run --sample lpc \
  --live-test "NAME" --cap-usd CAP
```

Without both flags the command prints the live-test rule and exits before any work. With them it prints the settings above, then the guard prints its own header (name, cap, model, route, ledger) before the first call. Every call is recorded in the guard's ledger and in the run log `_runs.jsonl` beside the context lines.

Look at the result:

```
python Sandbox/answering-library/index/cli.py show-sample --n 9
```

## How to judge it by eye

`show-sample` prints a spread of context lines, each beside its passage, with the mechanical check's verdict. Read about nine pairs across the three files and ask of each context line:

1. Does it name the right work, author and division, as the file header and the passage say?
2. Does it say where the passage sits (after what, before what) in a way a search could use?
3. Is every name, date and place in it also in the stretch the model was given? Nothing added from memory.
4. Is it one plain sentence, not a summary of the passage and not a quotation of it?

A bad one looks like this (illustrations written for this card, not output from a run):

| Defect | Illustration | Why it fails |
|---|---|---|
| Adds a fact | "Cyprian's De lapsis, written in the Decian persecution of 250, warns the lapsed." when neither the header nor the stretch mentions Decius or 250 | Invented context. The mechanical check flags an entity not in the window; such a line is kept in the log but left out of the index. |
| Restates the passage | "The bishop urges the brethren to keep one body in the unity of the church." | Copies the passage. Adds nothing a search could not already find. |
| Too generic | "A passage from a Latin text about the church." | Does not situate the passage; useless for retrieval. |
| Wrong place | Names a different work or division from the header | Misleads retrieval; the check cannot catch this, only the eye can. |
| Speaks as the source | "Here Cyprian himself says..." on a passage whose speaker is mixed | Context must not assign a voice the segmenter did not mark. The eye catches this one too. |

Decision rule suggested for the eye pass: approve if no more than one in nine is a defect of the last two kinds and the check flags no more than a few percent of lines; otherwise change the prompt and re-sample.

## What the context line is and is not

The context line is retrieval-only. It is prepended to the passage inside the search index so a query can match it, and it is stored in its own column. It is never stored in the passage text, never shown as source text, and never quoted. Every indexed passage keeps its file, byte span in the vendored file, division locus, ordinal, speaker, OCR score, apparatus flag, row ids and worlds. A retrieval hit returns the passage text and those fields separately from the context line, and `verify` checks that each passage text still equals its byte span in `cic/texts`. That keeps the three levels reachable: the marked text in an answer points to a passage id, the hover reads the passage's own fields, and the click-through opens the full record with the link to the vendored file and location.

## Whole-job figure this sample is a step toward

| Union of the twelve shelves | Low | High |
|---|---:|---:|
| Standard path | $438.12 | $745.54 |
| Batch path, half price (assumed; not reachable through the live-test guard today) | $219.06 | $372.77 |
| One call per window instead of per passage, standard path (estimate only) | $279.78 | $388.32 |

The union is 305,265 modeled passages and 154M to 198M text tokens, modeled from word counts until the segmenter lands. The about-$150 figure does not reproduce for per-passage calls on Haiku 4.5: it counts each text token once at the plain input rate, and per-passage calls also pay the 1.25 times cache-write premium on every token of every window, cache reads on each further passage in a window, and the output lines (the output alone is $83.95 to $152.63). Batch discount, the vendor's published batch rate is assumed to be half the standard rate (the repo carries no batch price), and the live-test guard does not expose the batch endpoint. The breakdown by file, world and cost driver is in `S1-05_Cost_Estimate.md`.

## Pending

- Mark: the sample's approval, the name and the cap.
- Segmenter output (one `passages/<file-stem>.jsonl` per file and `manifest.json` in the answering-library out directory): replaces the modeled counts with real ones.
- Embeddings are a separate metered class (proposal decision 2c) that Mark has not decided. The pipeline has only an interface for one (`index/embeddings.py`) and makes no embedder call.
- Batch path: needs a guard extension (the guarded client exposes only `messages.create` and `messages.stream`), which is a change to `engine/provider/guard.py` and its own change order.
