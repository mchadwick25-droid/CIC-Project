# hal: identity-and-scaffolding record pass, adversarial review round 2 (2026-10-08)

Branch `records/identity-scaffolding-hal`, HEAD `fde58dba`. Round 1: `hal_identity_scaffolding_review_round1_2026-10-07.md`. Reviewer: Opus 5.5. This is a targeted recheck of the round 1 findings and of what changed after them. No model or API spend. No record was edited.

Diff checked: `git diff 0f7be296..HEAD -- records/hal Build/worlds/hal engine/m1/cross_world.py`. That covers the round 1 fixes (395ef324), the merge of main, the later reword of the `marriage-ending` opener, the removal of the hal scaffolding waiver, and the renumbering of the gap entry to OG-16.

**Verdict: CLEARED.**

## Method

- Read the new `text` of the six records touched since round 1 against the round 1 text: `apostolic`, `hell`, `marriage-ending`, `one-church` (body only), `practices` and `was-jesus-god`. Only the named sentences changed; the rest of each text is identical apart from line wrapping.
- Checked the touched sentences for quotation marks. None carries a quotation, so no vendored-file re-verification was needed. The one quoted string in a touched body (`hell`: 'It is not ours to judge you...') is unchanged.
- Read OG-16 in `Build/worlds/hal/Open_Gaps_Tracking.md` against the records, the diffs, the pin and the gate runs.
- Ran `engine.m1.spoken_scaffolding.scaffolding_hits` over `load_world_records('hal')` (175 records): `[]`.
- Confirmed `ACCEPTED_OPEN` in `engine/m1/cross_world.py` has no `spoken-scaffolding/hal` key; the other worlds' waivers are untouched.
- Re-ran these gates: `engine.m10.cli records hal` PASS; `engine.m10.cli regate hal --base origin/main` PASS (notes only on pre-existing voice_craft FRE failures, unchanged from the base); `engine.m2.cli determinism-check hal` PASS (no differing paths); `engine.m10.cli deployed hal` PASS (pre-existing source_anchor note); `engine.m9.cli check` clean, every waiver live and current; `tools/check_live_commentary.py --base origin/main --enforce` exit 0; `engine.m2.site_cli staleness-check` hal `stale: false`.
- Pin: `records/worlds/hal.yaml` points to `packages/hal/2026-10-08T05-12-13Z` with `sha256:a41590ca7b9dd1ff2fc33b18bb9f08a4c6d2fa69807d7b9ff613264b60703610`. That equals the SHA-256 of that package's `manifest.json`, and OG-16 names the same package.

## Round 1 substantial findings

1. **`apostolic` opener: fixed.** It reads "Some of our practices went back to the apostles, and some were new." This is the wording round 1 asked for. Nothing else changed.
2. **`marriage-ending` opener: fixed, with a later reword that holds.** Round 1 asked for "Our answer was not a ruling but Fabiola: divorced, she belonged here." The `no-build-attribution` gate matched "not a ruling", so the opener now reads "Our answer was Fabiola rather than a ruling: divorced, she belonged here." The first sentence answers the question, in the kind asked, through the one remembered case. The claim, the order and the `not_for` ("a general canon or ruling rather than one remembered case") all hold. It is 12 words, plain and active, with no hedge or assistant cadence. "Here" is logged in OG-16, as asked.
3. **`hell` "without softening": fixed.** It reads "We believed in real judgment and real punishment. We say so without softening." The phrase again describes the telling, not the doctrine. OG-16's `hell` bullet says so.
4. **`practices` end-times negative: fixed.** It reads "No end-of-the-world scheme like the rapture is in our pages." That is again the narrow, rapture-like denial that `positions` and `not_for` support. OG-16 gives the old and the new wording.
5. **`one-church` scope disclosure: fixed.** The body now ends "Whether this world is a living tradition is not decided in this record." The process attribution is gone. OG-16 records the cut, the kept clause, and both old OG-8 quotations with their new wording. OG-8 is untouched, and OG-16 serves as its cross-reference.
6. **`hell` body build narration: fixed.** "noted here for the later voice build" is gone; the rest of the note stands. OG-16 lists the removal and moves `hell` and `marriage-ending` to the kept list.
7. **Demonstration paragraph: fixed.** OG-16 now uses round 1's wording. I re-checked the counts against the nine `hal.demo.*` files and they are right.

Optional finding 8 was applied: `was-jesus-god` now reads "we never treated it as negotiable." "It" refers to Jesus being God, as "that" does. No claim changed. Findings 9 to 13 were left as they were, which round 1 allowed.

## New findings

8. **Not substantial: OG-16's `marriage-ending` bullet still gives the round 1 wording.** The "What each opener now states" bullet quotes "Our answer was not a ruling but Fabiola: ...". The merge paragraph further down gives the current text and the reason for the change, so the entry as a whole is accurate. Read on its own, though, the bullet is out of date. Recommended, not required: in that bullet, replace the quoted opener with "Our answer was Fabiola rather than a ruling: divorced, she belonged here." and add "(reworded 2026-10-08; see below)".

9. **Not substantial: OG-16 does not say that it resolves the scaffolding-check entry of 2026-10-06.** That entry ("Spoken text opens on a question or carries a stage direction", now OG-14) says the pass removes the waiver. The pass has done that, and the check returns zero hits. The scaffolding-check entry has no status line, and OG-16 refers to it only by its bare number ("main had taken OG-14 and OG-15"). Append-only rules keep that entry as it is. Recommended: add one sentence to OG-16's merge paragraph: "This resolves the scaffolding-check entry of 2026-10-06: `scaffolding_hits` finds no hal field, and the waiver is gone." Cite it by subject and date.

10. **Not substantial: the gates paragraph names the round 1 package.** The "Gates" paragraph gives `2026-10-07T01-25-20Z` and its hash. The merge paragraph names the current package `2026-10-08T05-12-13Z` but gives no hash, and does not say the gates were rerun on it. I reran them above and all pass, so nothing is wrong in the records. Optionally, add the current manifest hash to the merge paragraph.

11. **Not substantial: line wrapping.** The first line of the `marriage-ending` text and the edited `hell` and `one-church` body lines run past the file's usual wrap width. This is cosmetic; YAML folding and Markdown render them the same.

No new AI tells, no second-person stage directions, and no build commentary were found in the touched record files.
