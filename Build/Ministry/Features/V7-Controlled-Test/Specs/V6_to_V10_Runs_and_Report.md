# V6 to V10: dry run, live sample, live run, reading, decision report

**Owner:** V7 lead.

## V6: dry run (Sonnet helpers; no spend)

- **What runs.** V2 in dry mode on the test branch, with `voice-drafter` helpers writing the replies. 3 probes per world, with B on.
- **What it is for.** Finding bugs in the harness, the switch and the reader pipeline.
- **What it is not.** Its answers are helper-written and are never used as results.
- **Done when.**
  - the records are complete;
  - B's additions are inside the budget;
  - flag-off is byte-equal;
  - V3 produces its tables.

## V7: live sample (`v7-b-alx-pahc-syr`, $1 cap)

- **What runs.** 2 probes per world, B only: 6 turns.
- **What it prints.** Model ids, route, settings, counts, tokens, latency and cost.
- **Next step.** The V7 lead sends the sample to the coordination thread, which takes it to Mark.
- **Stop rule.** Code scales the sample's actual cost per turn to the remaining 120 turns. If the core run would pass $11, the repeat is cut to fit and the coordination thread is told before any further call (`../Test_Plan.md` §7).

## V8: live main run and repeat (same name, cap $12 minus the sample's spend)

- **What runs.** B on the remaining 78 probes, then B on the 42 repeat probes. Probes run world by world so the cached prefix stays warm.
- **If the cap is reached.** The run stops and reports what finished. It is not resumed without Mark.
- **Afterwards.** The guard's ledger and summary are filed with the run.

## V9: reading

- **Model readers.**
  - Two blind Opus readers per answer, at the highest effort, run as in-plan subagents: 210 answers, 420 reads, plus the seeded copies.
  - A third Opus pass adjudicates every item with any score or error disagreement, and every tier 1 or tier 2 finding (`../Test_Plan.md` §6).
  - The seeded catch rate is computed first. If it is below 9 of every 10, the readers' scores do not count. The reader instructions are then fixed by change order, and the reading is redone.
- **Allowance check.** Reads are split into batches. If the weekly allowance's build half cannot carry them, they move to the next week rather than being cut.
- **Mark's review page.** An Artifact, not a repository file, built from V3's review data.
  - **Layout.** One answer at a time, arm hidden: the question, the answer, the cited records, and the source lines in context.
  - **Guidance.** Short, plain notes on the error types and severity tiers, in non-specialist words.
  - **His record.** For each answer he can mark error yes or no, type, severity, how sure he is, and add a note.
  - **Saving.** Entries are saved by the page's own saved state, using the artifact capabilities, and read back for the report.
  - **Length.** Answers are kept short to read, to beat the 12-hour estimate.

## V10: decision report (Opus)

- **What it answers.** Mark's eight questions (`../Test_Plan.md` §8), with each finding labelled verified, assumption or hypothesis.
- **What it holds.**
  - every count with its total;
  - the noise floor;
  - reader agreement per dimension, and the seeded catch rate;
  - Mark's own findings, beside the Opus readers' findings for the same answers, with the errors he found that they missed and the reverse;
  - a plain statement that the human review is the project lead's, not an independent historian's;
  - the actual cost and latency from the ledger;
  - the smallest next change the evidence justifies.
- **Where it goes.** An Artifact for Mark, plus the filed report in this folder.
- **On C.** If the report finds a problem B leaves that a selective check could fix, it proposes C as a change order. It does not build C.
