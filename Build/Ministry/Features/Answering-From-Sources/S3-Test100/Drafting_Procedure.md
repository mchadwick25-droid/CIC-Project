# Running the lpc test set in plan: drafting procedure

For the 106-question set (`lpc_106_questions.yaml`) after Stage 2 lands on lpc. No metered model call. Helpers in this plan stand in for the model by writing reply files. The runner is `engine/m3/test100.py`, the client `engine/m3/reply_client.py`, the sheet `engine/m3/test100_score.py`.

## Before the run

1. Check out main with the lpc package restored: `python -m engine.m2.cli restore lpc`.
2. Check the set against its seal (the runner does this) and the lpc pin (Stage 2's re-pin, if any).
3. Pick a work directory outside the repository. The runner refuses one inside it, because the pending requests for the 28 sealed questions carry the sealed wording.
4. Check the allowance ledger. Each voice prompt carries the world's whole compiled prompt (about 115 KB for lpc), shared across questions, and each question needs about three calls.

## Passes

One command per pass: `python -m engine.m3.test100 --set <set> --world lpc --work <dir>`. It runs every question as far as its replies allow and writes, for each missing reply, `pending/<question>.<kind>.<n>.prompt.txt` plus the shared `pending/system-*.txt` files it points to.

- Pass 1: the safety and reader calls for every question. Reply with one JSON object matching the schema printed at the top of the prompt file: `replies/<question>.submit_safety_classification.1.json` and `replies/<question>.submit_reader_output.1.json`.
- Pass 2: the voice call. Reply with the raw tagged text the voice would stream: `replies/<question>.voice.1.txt`.
- Pass 3 and later: any second voice call (a self-revision) and anything else the engine asks for. Repeat until a pass reports no pending questions. Stop at four passes and look at what is stuck.

Helpers: one list of prompt files per helper, about five questions each, with the exact reply path beside every prompt. A helper reads the shared system files once and reuses them for its list. Check every reply file exists and is one JSON object (or non-empty text) before the next pass. A reply that does not parse stops the run with the file named.

Each safety and reader reply is a classification of the visitor's message, as the model would make it. The voice reply is the draft as the voice would write it from the system prompt it was given. The helper does not see the records or the answers of any other question, and does not see the scoring.

## After the run

1. `python -m engine.m3.test100_score --set <set> --work <dir> --out <sheet.csv>`. The totals split the 28 sealed probes from the rest, and report the fit traps (group K) on their own line.
2. Compare the 28 beside the Stage 3 baseline (`Stage3_Change_Order.md`): 45 cuts, 13 orphan flags, more than 4 placed quotes, 233 words, reading grade 6.5 and ease 74.0.
3. Readers fill the empty columns: fit to the question, answers the question asked, the five quality marks, pass or fail, still-works. Blind reads by two helpers and a third to settle a split; a label stands at two of three, marked AI-adjudicated (Decision-Log 17).
4. Judge columns: the citation-recall judge and the verifier run over every shipped sentence through the goldset tooling, as in `Stage1/runs/judge-trial-1/README.md`.

## Helpers and the judge steps

- Helpers for drafting are the `voice-drafter` type (`.claude/agents/voice-drafter.md`): Read and Write only, the same pattern as `judge-reader`, so `judge-reader` keeps its labelling and judging role. A helper with other tools is not used.
- The current gates' verdict on each sentence comes from the run's own net output, not from `engine/m3/gate_replay.py`, which no longer matches the current answerer. `python -m engine.m3.test100_export --set <set> --work <dir> --out <export dir>` writes the run report and the gate rows in the shapes `goldset.pool` reads; then run `python -m goldset.pool --reports <export dir>/reports --gates <export dir>/gates --out <pool.jsonl>` from `Sandbox/Answering-From-Sources`.
- The run sets `story_placement` on in memory, so the story door is exercised on lpc, whose registered flag is off. `--no-story-placement` leaves the registered flag. A story is placed whole, as its `telling`; the short and medium lengths are not in the placement code yet.
- Citation attach is off in this run, because it makes extra model calls. The run's settings say so. A turn that would have gained a citation by attach is scored without it.
- The reader reply decides what retrieval offers. A reader reply whose `asks` does not match the question sends the turn to the wrong records, so reader replies must restate the question as the reader would.
