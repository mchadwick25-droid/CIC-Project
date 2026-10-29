# Request to the engine thread: the live admission harness loses what it has not yet written, and does not match live use

Written 2026-10-29 by the fleet graded run 1 thread, at Mark's request. This is a request, not a change: no engine code was touched in the run. Everything below is on the branch `claude/fleet-graded-run-1`.

## What happened

cappadocian's admission world was run twice. Both times the harness refused to write its report and raised:

`RuntimeError: cappadocian: 29 calls and 28 answers for 28 probes - expected exactly one of each per probe` (`engine/m3/live_admission_run.py`, the check at line 343; the one at line 336 is the sibling check on usage records).

In each attempt exactly one call failed and the voice call retried it, so the harness counted 29 calls for 28 probes. Each failed call is charged at its full hold by the guard (`engine/provider/guard.py`, `settle(..., failed=True)`).

| | Failed call | Charged | Time (UTC) | World cost |
|---|---|---|---|---|
| Attempt 1 | probe index 3 | $0.2178 | 2026-10-29 00:12:02 | $1.1276 |
| Attempt 2 | probe index 12 | $0.2158 | 2026-10-29 03:26:38 | $1.1119 |

Together the two attempts cost $2.24 for a world whose preflight estimate was $0.63, and produced no report. The other eleven worlds ran with no failed call. Each cappadocian attempt did save 28 answers (`cappadocian.json.answers.jsonl`, `cappadocian-attempt2.json.answers.jsonl`), so the answers were graded by Opus. The automatic checks were never computed.

Evidence under `engine/m3/reports/fleet-graded-run-1/`: `cappadocian.stderr.txt`, `cappadocian-attempt2.stderr.txt`, `ledger-cappadocian.jsonl`, `ledger-cappadocian-attempt2.jsonl`, `checkpoint.json` (worlds.cappadocian).

## What the harness records as it goes, and what it does not

`_RecordingAnswerer` (line 241) appends one line per answer the moment it returns (line 254): `index`, `cell`, `answer_text`, `citations`. That part worked.

Held only in memory until a world completes, and then lost if the world is refused:
- each probe's automatic check results,
- the per-sentence citation entries (`citation_entries`), the raw reply, the request settings, the stop reason and the timings (the transcript),
- the error type and message of any failed call. The ledger line for a failed call carries only `failed: true` and no error text, so the cause of the cappadocian failures is not known.

## Requests

1. **Spill the full transcript and the checks as each probe finishes**, in the same append-only file or a sibling, so a world that stops part way keeps everything it paid for. Today only the answer text and record ids survive.
2. **Record the error of every failed call** (exception type and message, and whether the voice call retried it) in the ledger settle line or the answers file.
3. **Do not discard a completed world because the call count is off by a retried call.** Keep the report, mark the world "retried calls: n" and show the retried call, instead of raising. The one-call-per-probe check is a sound tripwire for a bug, but here it throws away a finished, paid-for world.
4. **Find out why cappadocian alone failed a call in both runs**, one call per run, at different probes. Possible places to look: the size of its prompt or one of its offers, a rule that redrafts, or a Bedrock-side limit. Reproducing it needs paid calls, so a small capped test by name, started by Mark, would be the way.

## Where the admission harness does not match live use

These came from the Opus reviewers of the twelve worlds. Please verify each against the code before acting; the reviewers read saved outputs and replayed the engine offline, with no model call.

- **Speaker-naming instruction.** `LiveModelAnswerer` (`engine/m3/generation.py`, line 156) never gives the voice the instruction to name a quote's speaker that live turns get from `engine/m4/turn_prep.py`, yet `apply_net` still removes a quote whose lead-in does not name its speaker. In syr, no quote reached a participant in any of 28 answers (21 attempts, all removed; 15 for this reason). pahc, don and lpc showed the same. So admission does not measure quote use.
- **No reader call.** Admission calls `assemble_evidence` with `asks=None` (line 181) and makes no reader call, so retrieval differs from a live turn. In don, 16 of 28 questions had no record tagged to their own question cell; in pahc, 13 of 28.
- **No reading-level gate.** `engine/m7/turn_readability.py` is not run on the admission path. Answers below the floor (FRE under 60, or FK over 10) passed the automatic checks in several worlds, for example rzg, ijc, alx and hal.
- **The automatic checks are too few.** Only `source_boundedness` and `register_coined_aphorism_heuristic` run. They passed all 28 answers in all twelve worlds, while Opus failed between 5 and 16 per world. They do not see invented facts, cut damage, build language in the voice, raw `[[…]]` tags, or stray characters.
- **No removal reasons in the transcript.** The saved transcript does not record why the net removed a sentence. A reviewer had to replay the engine offline to recover them.

## Not in scope here

The cut step's damage to answers (leftover pointers after a sentence is removed) and the world-level record fixes are described in the per-world reviews under `Build/worlds/<code>/Review-Artifacts/Fleet_Run1_Answer_Review_2026-10-28.md` and in the fleet summary Artifact. They are not part of this request.
