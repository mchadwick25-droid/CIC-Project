# Spec 6: the conformance removals (chunk D6)

**Model:** Sonnet writes, Opus reviews. **Ruled:** Decision-Log 70.

**Purpose.** Remove the engine pieces the design does not call for and Mark approved for removal, with no change to what the live path says today.

**Remove.**
1. `engine/m1/gates_experimental.py` (never called; only comments name it). Rewrite those comments in `engine/m1/gates.py` and `engine/m2/builders.py` to state what the code does without naming the removed file.
2. The fleet floor line in `engine/m4/evidence.py` (defined, never wired).
3. Self-revision: `engine/m4/self_revision.py`, its call in `engine/m4/turn.py`, its setting in `engine/api/config.py` and `render.yaml`, its tests.
4. The r27 regeneration: its enforcement path in `engine/m4/turn.py` and its correction appendix. `engine/m4/uncited_claims.py` stays: `engine/m7/offline_checks.py` uses it.
5. Citation attach: `engine/m4/citation_attach.py`, its call in `turn.py`, its settings and tests.
6. The answer-record fallback on the new (shadow) path only. The live path keeps it until its gates retire.

**Must not touch.** Anything not named above; the Facilitator and safety code; the old cut step, silence check and withheld-claim rule; records; packages.

**Test written first.**
- Each removed module is gone and nothing imports it; each removed setting is gone from config and `render.yaml`.
- The shadow path, given an emptied answer, abstains in the world's fallback sentence; it never substitutes witness text.
- Replay: the live path's output on the saved drafts (`engine/m4/reports` replay of fleet run 1) is byte-equal before and after.
- The full engine test suite passes; `tools/check_live_commentary.py --base origin/main --enforce` passes.

**Done when.** Merged after one Opus review. **Cost:** none.
