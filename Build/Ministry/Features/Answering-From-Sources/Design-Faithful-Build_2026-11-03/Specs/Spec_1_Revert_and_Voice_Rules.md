# Spec 1: revert Decision-Log 63 and 64, and the shared voice change

**Model: Opus.** It changes the instructions the voice drafts from.

**Purpose.** Return the draft directive to its Stage 4 state (undo the stacked patches of Decision-Log 63 and 64, no third patch on top), and in the same pull request make the voice and length changes Mark approved.

**Inputs.** Commits 992dfb91 (Decision-Log 63) and 109c9fa3 (Decision-Log 64). Mark's approved wording for the pronoun rule and the length directive, as relayed by the coordination thread.

**Outputs.**
1. Two revert commits, newest first (`git revert 109c9fa3`, then `git revert 992dfb91`). They restore `engine/m4/answer_check.py`, `bound_draft.py`, `verify_step.py` and their tests.
2. Decision-Log entries are append-only (confirmed): entries 63 and 64 stay; the reverts do not apply to `Decision-Log.md`, and Decision-Log 69 records the revert.
3. `engine/shape/records/fleet_voice/_fleet.voice.fleet.md` `pronoun_rule`: replace "Strict we-voice, always" with: "we" when giving the tradition's own perspective, where the voice is not a person; "I" for its own acts in the present conversation; names people, places, councils, communities and cities wherever the sources name them; the Representative never claims to be a bishop or any person; "I am a representative of ..." at most once per turn; drop the ban on explaining the we.
4. `engine/m4/turn_prep.py`: replace the line at 225 to 226 ("fewest sentences", "between 120 and 220 words") with succinctness and no length cutoff: say it tightly, every sentence earns its place, nothing that does not bear on the question, a question that earns more takes more. In `LIMIT_LINE`, "plainly and briefly" becomes "plainly and succinctly". `NO_NEW_FIGURE_LINE` gives way where the visitor's question or the offered sources name the person (P8 as approved with the voice-rules correction).
5. The sentence-length report becomes pressure toward succinctness with no cutoff. The reading-level target stays a separate measure.

**May touch.** The files above and their tests; `engine/shape/__init__.py` (the `SHAPE_HASH` constant, one line); `Decision-Log.md` (append only).
**Must not touch.** The rest of the directive; `records/*/voice_craft/` (Library's, under the Voice Rules Correction change order, #1464); `Sandbox/`; the search package.

**Consequence to state in the pull request (expected).** Editing the fleet voice file changes `SHAPE_HASH`. `engine/m3/admission_conform.py` compares reports by shape hash, so every admission report made before the change stops counting as the same shape. This is expected. The shape test (`engine/shape/tests/test_shape.py`) must be updated with the new hash.

**Test written first (fails before, passes after).**
- `turn_prep` tests: the directive text holds no "120" and no "fewest sentences"; it holds "succinct"; `LIMIT_LINE` holds "plainly and succinctly".
- A fleet-voice test: `pronoun_rule` no longer contains "Strict we-voice, always" and contains the "I am a representative of" at-most-once rule.
- The Decision-Log 63 and 64 tests removed by the reverts do not return; `engine/m4/tests` pass.

**Done when.** Every touched file passes `tools/check_live_commentary.py --base origin/main --enforce`, the tests pass, `engine/shape` tests pass with the new hash, the diff shows the two reverts as separate commits, and the pull request states the shape-hash consequence. **Cost:** none.
