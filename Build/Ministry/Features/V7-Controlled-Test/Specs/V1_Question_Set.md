# V1: baseline A extracted, repeat draw, optional hard-case set

**Owner:** the V7 lead. The question thread takes the option, if Mark wants it.
**Model:** Sonnet for the extract. Opus for any option questions.

**Purpose.** Put arm A's saved answers into one frozen, checkable form. Draw B's repeat subset. If Mark takes the option, write up to 15 hard-case questions.

**Outputs.** All go in `../Set/`.
- **`A_<world>.jsonl`** for alx, pahc and syr. One line per probe, with these fields:
  - probe id and cell
  - `answer_text`, citations and citation entries
  - the offered record ids. These were not saved by the run, so the field is null. The set is rebuilt later by replaying evidence assembly (`../Test_Plan.md` §3, item 1). `draft_marker_ids` lists the ids the draft cited.
  - usage, `seconds_to_first_text`, `seconds_total`, stop reason, priced cost

  Each line is copied from the run's `<world>.json` and its ledger, in the `fleet-graded-run-1/` report folder on branch `claude/fleet-run-1-analysis` (not on `main`). No probe text is copied.
- **`A_reviews_<world>.json`**: the second-pass and outside-referee findings for the same probes, by probe id.
- **`repeat_draw.json`**: the seed, written before the draw, and the 42 drawn probe ids. That is 14 per world, stratified by family and register.
- **`SHA256SUMS`** over all of the above.
- **Option, only on Mark's word:**
  - `extra_<world>.yaml`, with 5 questions per world
  - `extra_<world>_trap_notes.yaml`, giving for each question what a faithful answer must not do, and the source and lines that show it
  - both frozen before the card thread starts

**May touch.** `../Set/` only.
**Must not touch.** The run branch, the records, the sealed probes and the engine.

**Tests written first.**
1. Each `A_<world>.jsonl` has 28 lines. Each `answer_text` is byte-equal to the run file's.
2. Joining the gate replay's shown sentences reproduces each `answer_text`. Source: `Build/Ministry/Features/Answering-From-Sources/Stage1/data/gate-replay/`.
3. No file holds probe text. This is checked by comparing hashes of normalized text against the sealed set, without printing either.
4. The repeat draw reproduces from its seed, with 14 per world and every family present.
5. `SHA256SUMS` matches the files.

**Done when.** The tests pass, the files are frozen, and any later change is a change order.

**Cost.** None metered.
