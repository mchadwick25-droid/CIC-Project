# V5: B behind a switch

**Owner:** engine thread. **Model:** Opus. This is core code on the turn path, and it sits behind a switch that is off.

**Purpose.** Build B exactly as `../Test_Plan.md` §3 defines it, first on `main` behind the off flag, then cherry-picked onto the test branch `v7/b-on-live` (Spec V2).

**Design.**
- **The switch.** A frame flag, `reading_context`. No world record sets it, and the compiler never writes it. It is set in memory only, by V2's `--arm b`.
- **When it is on, `engine/m4/evidence.py` `render_evidence_block`:**
  - adds each offered quote's reviewed modern rendering to its line;
  - adds "Reads differently today" from the lens note, or from the card's `reads_differently_today` where there is a card;
  - adds the card's lines under the record, where there is a card;
  - adds the `fit_step.context_blocks` window for the top two offered quotes or stories.
- **Budget.** Additions stop at 12,000 characters (change order 2026-11-03, `../Test_Plan.md` §3, item 7). Context windows are dropped first, then card lines, and the quote renderings are kept.
- **Guidance lines.** When the flag is on, `render_evidence_block` opens the evidence block with these lines. They go in the evidence block, not in `engine/m4/turn_prep.py`, because the harness that produced A sends no turn directive, and the block reaches the voice on both paths. The lines:
  > Answer what the visitor asked, first and plainly.
  > Draw the offered sources and our ground together: connect them, explain how belief and practice fit, and say what we understand them to mean.
  > Keep apart what a source says, what we understand it to mean, and what was disputed or uncertain, in plain words.
  > Say whose view a source gives, and how widely it was shared, only as far as its card or record says.
  > Read the surrounding text to understand a passage; cite the record, not the text around it.
- **Report-only signal.** A whole-world sentence whose only cited record has a single-author `whose_view` is counted in the turn's report. Nothing is withheld for it.
- **Unchanged.** Selection, the net, placement and every gate.

**May touch.** `engine/m4/evidence.py` (rendering only), a report counter, tests. **Must not touch.** Evidence selection, `grounding_net.py`, placement, `render.yaml`, any world record's flags.

**Tests written first.**
1. With the flag off, the evidence block is byte-equal to today's for all 84 probes, run in dry mode. On the test branch, it is byte-equal to A's saved `request`.
2. With the flag on, the offered record ids equal those with the flag off.
3. With the flag on, additions never exceed 12,000 characters. Context windows are dropped first.
4. A quote with no card still shows its rendering and lens note.
5. Context ids cannot be cited: a sentence tagged with one is treated as today.
6. The signal counts a fixture "we held" sentence bound only to a single-author card, and withholds nothing.

**Done when.**
- The tests pass on `main` and on the test branch.
- The full engine suite passes on `main`.
- `live` is untouched.

**Cost.** None.

## Test branch

`v7/b-on-live` is cut from `origin/live` at c869dd86. B runs there with exactly these changes, taken from the head of `claude/v7-v5-b-switch` (`<sha>`).

**Files copied whole** (`git checkout <sha> -- <path>`). None of them exists on `live`, so each is new there:
- `engine/m4/reading_context.py`
- `engine/m4/source_windows.py`
- `engine/m4/fit_step.py` (it imports only `engine.prose.locus_refs`)
- `engine/m4/reading_cards.py` (V4a's loader)
- `engine/m3/v7_run.py`
- `engine/m3/tests/test_v7_run.py`
- `engine/m4/tests/test_reading_context.py`
- `engine/m4/tests/test_source_windows.py`
- `engine/m4/tests/test_reading_cards.py`

**Diffs applied** (`git diff <base> <sha> -- <path> | git apply`):
- `engine/m4/evidence.py`: commit ee485aa8's diff for this file only (`git show ee485aa8 -- engine/m4/evidence.py | git apply`). It has three hunks: the `reading_context` import, the `reading_rendering` field on the quote line, and `render_evidence_block`'s keyword-only `world` and `reading` with `_render_with_reading`. It applies to `live` with no fuzz. Main's whole `evidence.py` is never copied, because it carries main-only selection changes.
- `engine/prose.py`: only the addition of `_SPAN_LANGUAGES`, `_VENDORED_SPAN` and `locus_refs` at the end of the file. That addition is the whole of `git diff origin/live origin/main -- engine/prose.py`.

**Not taken.** V4a's schema, gate and builder changes. No record and no package changes on the test branch: the cards and lens notes come from `--reading-records-dir`.

**Checked on a checkout of `live` with these changes:**
- the four test files pass, including the check that the runner's voice call is the one A's `LiveModelAnswerer` makes;
- with the flag off, the evidence block is byte-equal to `live`'s own for all 84 probes;
- a dry run of arm b answers from reply files and records `additions_chars`.
