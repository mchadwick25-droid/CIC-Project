# V6 to V10: dry run, live sample, live run, reading, decision report

**Owner:** V7 lead.

## V6: dry run (Sonnet helpers; no spend)

- **What runs.** V2 in dry mode, with `voice-drafter` helpers writing the replies. 3 questions per world through every arm.
- **What it is for.** Finding bugs in the harness, the switch and the reader pipeline.
- **What it is not.** Its answers are helper-written and are never used as results.
- **Done when.**
  - the records are complete;
  - B's additions are inside the budget;
  - flag-off is byte-equal;
  - V3 produces its tables.

## V7: live sample (`v7-ab-alx-pahc-syr`, $2 cap)

- **What runs.** 2 questions per world, through A-live and B: 12 turns.
- **What it prints.** Model ids, route, settings, counts, tokens, latency and cost.
- **Next step.** The V7 lead sends the sample to the coordination thread, which takes it to Mark.
- **Stop rule.** If the sample's per-turn cost, scaled to 480 turns, comes to more than $27, stop and return.

## V8: live main run (same name, cap $28 minus the sample's spend)

- **What runs.** A-live and A-main once each, and B twice. 120 questions each time, interleaved per question.
- **If the cap is reached.** The run stops and reports what finished. It is not resumed without Mark.
- **Afterwards.** The guard's ledger and summary are filed with the run.

## V9: reading

- **Model readers.** V3 sends two blind `judge-reader` reads per answer: 480 answers, 960 reads, drawing on allowance.
- **Allowance check.** Reads are split into batches. If the weekly allowance's build half cannot carry them, they move to the next week rather than cutting a reader.
- **Human packets.** These go to the reviewers Mark arranges. If none can be arranged, the report says so.

## V10: decision report (Opus)

- **What it answers.** Mark's eight questions (`../Test_Plan.md` §8), with each finding labelled verified, assumption or hypothesis.
- **What it holds.**
  - every count with its total;
  - the noise floor;
  - reader agreement;
  - the human reviewers' errors that the model readers missed;
  - the actual cost and latency from the ledger;
  - the smallest next change the evidence justifies.
- **Where it goes.** An Artifact for Mark, plus the filed report in this folder.
- **On C.** If the report finds a problem B leaves that a selective check could fix, it proposes C as a change order. It does not build C.
